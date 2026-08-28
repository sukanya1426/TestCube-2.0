"""AndroLog-based method coverage.

An APK instrumented by AndroLog (https://github.com/JordanSamhi/AndroLog)
emits one logcat line per executed method under a chosen tag::

    D <TAG>: METHOD=<pkg.Class: void method()>

We tail logcat, count *distinct* methods, and divide by the number of probes
the APK actually carries. That denominator is read from the APK itself
(``total_methods_from_apk``) rather than hardcoded, so it always matches the
binary under test.
"""

import os
import re
import subprocess
import threading
import zipfile

from .base_monitor import CodeCoverageMonitor


METHOD_RE = re.compile(r"METHOD=(<[^>]+>)")
CLASS_RE = re.compile(r"CLASS=(\S+)")
ACTIVITY_RE = re.compile(r"ACTIVITY=(\S+)")
PROBE_RE = re.compile(rb"METHOD=<[^>]{1,600}>")


def total_methods_from_apk(apk_path):
    """Count distinct METHOD= probe strings across every dex in the APK.

    This is the denominator AndroLog itself would report, recovered from the
    instrumented binary so it cannot drift from what is installed.
    """
    found = set()
    with zipfile.ZipFile(apk_path) as archive:
        for name in archive.namelist():
            if not name.endswith(".dex"):
                continue
            for match in PROBE_RE.findall(archive.read(name)):
                found.add(match)
    return len(found)


class AndroLogCVMonitor(CodeCoverageMonitor):

    method_name = "androlog"

    def __init__(self, save_dir, tag, total_methods, activities=None,
                 udid=None, adb_path="adb", buffer_size="64M"):
        super(AndroLogCVMonitor, self).__init__(save_dir=save_dir)
        if not total_methods:
            raise ValueError("total_methods must be a positive count")
        self.tag = tag
        self.total_methods = int(total_methods)
        # Declared activities from the manifest. AndroLog also probes abstract
        # base activities, which are not launchable screens, so the denominator
        # is the manifest list rather than the probe count.
        self.activities = set(activities or ())
        self.udid = udid
        self.adb_path = adb_path
        self.buffer_size = buffer_size

        self._lock = threading.Lock()
        self._methods = set()
        self._classes = set()
        self._activities = set()
        self._lines_seen = 0
        self._lines_at_last_sample = 0
        self._stalled_samples = 0
        self._restarts = 0
        self._process = None
        self._thread = None
        self._stop = threading.Event()

        self._save_to_file("tag: %s" % tag)
        self._save_to_file("total methods: %d" % self.total_methods)
        if self.activities:
            self._save_to_file("total activities: %d" % len(self.activities))
        self.logger.info(
            "AndroLog coverage: tag=%s, total methods=%d, total activities=%d",
            tag, self.total_methods, len(self.activities),
        )

    def _adb(self, *args):
        command = [self.adb_path]
        if self.udid:
            command += ["-s", self.udid]
        return command + list(args)

    def start(self):
        """Clear the log buffer and begin tailing in a daemon thread.

        AndroLog emits one line per executed method, which overruns the
        default 2 MiB ring buffer within seconds — logcat then drops lines
        ("chatty" expiry) and coverage silently stops rising. We enlarge the
        buffer and keep the reader on a dedicated thread that does nothing but
        consume, so the pipe never backs up.
        """
        try:
            subprocess.run(
                self._adb("logcat", "-G", self.buffer_size), check=False, timeout=30
            )
        except Exception as exc:
            self.logger.warning("could not resize logcat buffer: %s", exc)
        try:
            subprocess.run(self._adb("logcat", "-c"), check=False, timeout=30)
        except Exception as exc:
            self.logger.warning("could not clear logcat: %s", exc)

        def listen():
            while not self._stop.is_set():
                try:
                    self._process = subprocess.Popen(
                        self._adb("logcat", "-s", self.tag),
                        stdout=subprocess.PIPE,
                        stderr=subprocess.DEVNULL,
                        text=True,
                        errors="replace",
                    )
                    for line in self._process.stdout:
                        if self._stop.is_set():
                            break
                        self._consume(line)
                except Exception as exc:
                    self.logger.warning("logcat listener error: %s", exc)
                if self._stop.is_set():
                    break
                # The device can drop the connection mid-run; resume tailing
                # without clearing, so counts already collected survive. Any
                # methods logged during the gap are lost, so this is counted
                # and surfaced in the summary rather than passing silently.
                self._restarts += 1
                self.logger.warning(
                    "logcat listener stopped; restarting (restart #%d — "
                    "some probe lines may have been missed)", self._restarts
                )

        self._thread = threading.Thread(target=listen, daemon=True)
        self._thread.start()
        return self

    def _consume(self, line):
        self._lines_seen += 1
        method = METHOD_RE.search(line)
        if method:
            with self._lock:
                self._methods.add(method.group(1))
            return
        activity = ACTIVITY_RE.search(line)
        if activity:
            with self._lock:
                self._activities.add(activity.group(1))
            return
        klass = CLASS_RE.search(line)
        if klass:
            with self._lock:
                self._classes.add(klass.group(1))

    def _get_code_coverage(self):
        with self._lock:
            hit = len(self._methods)
        return (hit / float(self.total_methods)) * 100.0

    def activity_coverage(self):
        """Percentage of manifest-declared activities reached.

        Only activities actually declared in the manifest are counted, so
        abstract bases picked up by the probes cannot push this above 100%.
        """
        if not self.activities:
            return None
        with self._lock:
            reached = self._activities & self.activities
        return (len(reached) / float(len(self.activities))) * 100.0

    def _check_liveness(self):
        """Warn if the reader has stopped receiving lines while the app runs.

        A frozen counter looks exactly like genuine saturation, so a stalled
        reader would otherwise be reported as a real (too low) coverage
        number. Surfacing it keeps a broken measurement from being mistaken
        for a finished one.
        """
        if self._lines_seen == self._lines_at_last_sample:
            self._stalled_samples += 1
            if self._stalled_samples == 3:
                self.logger.warning(
                    "No new AndroLog lines across %d samples — the logcat "
                    "reader may have stalled or the app may be idle. "
                    "Coverage is frozen at %.5f%%.",
                    self._stalled_samples, self._current,
                )
        else:
            self._stalled_samples = 0
        self._lines_at_last_sample = self._lines_seen

    def _extra_sample_fields(self):
        self._check_liveness()
        fields = {}
        with self._lock:
            fields["methods_hit"] = len(self._methods)
            fields["classes_hit"] = len(self._classes)
            if self.activities:
                fields["activities_hit"] = len(self._activities & self.activities)
        coverage = self.activity_coverage()
        if coverage is not None:
            fields["activity_coverage"] = round(coverage, 5)
        return fields

    def _format_sample(self, entry):
        line = "[%s] %8.5f%% (%d/%d) @ %.2fs" % (
            self.tag,
            entry["coverage"],
            entry.get("methods_hit", 0),
            self.total_methods,
            entry["elapsed"],
        )
        if "activity_coverage" in entry:
            line += " | activities %6.2f%% (%d/%d)" % (
                entry["activity_coverage"],
                entry.get("activities_hit", 0),
                len(self.activities),
            )
        return line

    def summary(self):
        data = super(AndroLogCVMonitor, self).summary()
        with self._lock:
            data.update({
                "tag": self.tag,
                "total_methods": self.total_methods,
                "methods_hit": len(self._methods),
                "classes_hit": len(self._classes),
                "lines_seen": self._lines_seen,
                "listener_restarts": self._restarts,
                "stalled_samples": self._stalled_samples,
            })
            if self.activities:
                reached = self._activities & self.activities
                data.update({
                    "total_activities": len(self.activities),
                    "activities_hit": len(reached),
                    "activity_coverage": round(
                        len(reached) / float(len(self.activities)) * 100.0, 5
                    ),
                    "activities_reached": sorted(reached),
                })
        return data

    def covered_methods(self):
        with self._lock:
            return sorted(self._methods)

    def stop(self):
        self._stop.set()
        if self._process:
            try:
                self._process.terminate()
            except Exception:
                pass
        if self._thread:
            self._thread.join(timeout=3)
