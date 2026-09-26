#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""One-click TestCube vs LLMDroid experiment across a list of APKs.

Per app, in order, exactly as docs/CODE_COVERAGE.md prescribes:

    1. instrument   scripts/instrument_apk.py -> apks/instrumented/<stem>.apk
                    and read back the real method count
    2. verify       install, launch, grep logcat for VerifyError / FATAL EXCEPTION
                    (bytecode rewriting does not always produce verifiable dex;
                    vinyl.apk installs fine and is silently dead)
    3. TestCube     start.py -policy feature_guided --code-coverage androlog
    4. LLMDroid     scripts/run_llmdroid.py, SAME instrumented APK, same budget
    5. compare      scripts/compare_coverage.py
    6. feature eval scripts/evaluate_features.py against ground_truth.json

Steps 1 and 2 are the compatibility gate. Whether an APK works with both tools is
not predictable from the app -- docs/CODE_COVERAGE.md records six of eight failing
on one Soot 4.6.0 bug, including the least obfuscated APK measured -- so it is
measured here rather than assumed, and the result is written back into
experiment/apps.json.

Everything is configured in experiment/config.json. One app failing never stops
the run: each app is isolated, its failure is recorded, and the next one starts.

    python scripts/run_experiment.py                  # uses experiment/config.json
    python scripts/run_experiment.py --count 5
    python scripts/run_experiment.py --apps markor,aegis,fossifyclock
    python scripts/run_experiment.py --dry-run        # show the plan, run nothing
    python scripts/run_experiment.py --resume         # skip apps already finished
"""

from __future__ import print_function

import argparse
import datetime
import io
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import zipfile

# =============================================================================
#  EDIT THESE TWO TO CHOOSE WHAT RUNS
# =============================================================================
#
#  APK_NAMES wins. NUM_APKS is only consulted when APK_NAMES is empty.
#
#    APK_NAMES = ["money", "newpipe"]   -> runs exactly those two, in that order
#    APK_NAMES = []                     -> runs the first NUM_APKS apps that have
#                                          a binary in apks/, in catalogue order
#
#  Names are the "stem" column of experiment/apps.json, which is also the APK
#  filename without .apk: apks/money.apk -> "money".
#
APK_NAMES = ["money", "newpipe"]
NUM_APKS = 5
#
#  Everything else (budget, output folders, policy) is in experiment/config.json.
#  Both of these can still be overridden for one run without editing the file:
#      python scripts/run_experiment.py --apps markor,aegis
#      python scripts/run_experiment.py --count 5
# =============================================================================

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(REPO, "experiment", "config.json")
CATALOGUE = os.path.join(REPO, "experiment", "apps.json")
LLMDROID = os.path.join(REPO, "compare", "LLMDroid", "LLMDroid-Droidbot")

# Exit status the run-budget watchdog uses when it kills a wedged run.
EXIT_HARD_STOP = 3

LOCK = os.path.join(REPO, "output", "experiment", ".runner.lock")


def _alive(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    except Exception:
        return True
    return True


def acquire_lock():
    """Refuse to start while another runner is driving the device.

    Two runners on one emulator interleave taps and installs, and each
    uninstalls the app out from under the other at teardown. The symptom is an
    idle-looking screen and coverage that never grows, which reads like a hang
    rather than the collision it is.
    """
    folder = os.path.dirname(LOCK)
    if not os.path.isdir(folder):
        os.makedirs(folder)
    if os.path.isfile(LOCK):
        try:
            other = int(io.open(LOCK, encoding="utf-8").read().split()[0])
        except Exception:
            other = None
        if other and other != os.getpid() and _alive(other):
            return False, other
        os.remove(LOCK)          # stale: the previous runner is gone
    with io.open(LOCK, "w", encoding="utf-8") as handle:
        handle.write(u"%d %s\n" % (os.getpid(), datetime.datetime.now().isoformat()))
    return True, os.getpid()


def release_lock():
    try:
        if os.path.isfile(LOCK):
            os.remove(LOCK)
    except Exception:
        pass


# ---------------------------------------------------------------- utilities

class Tee(object):
    """Write to the console and to the app's log file at once."""

    def __init__(self, path):
        self.handle = io.open(path, "a", encoding="utf-8")

    def write(self, text):
        sys.stdout.write(text)
        sys.stdout.flush()
        self.handle.write(text if isinstance(text, type(u"")) else text.decode("utf-8", "replace"))
        self.handle.flush()

    def close(self):
        try:
            self.handle.close()
        except Exception:
            pass


def say(text):
    """Progress that survives being piped: this run lasts hours behind a tee."""
    sys.stdout.write(text + "\n")
    sys.stdout.flush()


def stamp():
    return datetime.datetime.now().strftime("%H:%M:%S")


def human(seconds):
    seconds = int(seconds)
    return "%dh%02dm%02ds" % (seconds // 3600, (seconds % 3600) // 60, seconds % 60)


def run(command, cwd=None, log=None, env=None, timeout=None, label=""):
    """Run a command, stream it to the log, and return (rc, combined_output).

    Never raises on a non-zero exit: the caller decides whether that ends the
    app or the experiment.
    """
    if log:
        log.write(u"\n[%s] $ %s\n" % (stamp(), " ".join(command)))
    merged = dict(os.environ)
    merged.update(env or {})
    start = time.time()
    try:
        proc = subprocess.Popen(
            command, cwd=cwd or REPO, env=merged,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            universal_newlines=True, bufsize=1,
        )
    except OSError as exc:
        if log:
            log.write(u"[%s] could not start %s: %s\n" % (stamp(), label or command[0], exc))
        return 127, str(exc)

    # A watchdog thread, not a check inside the read loop: readline() blocks, so a
    # command that hangs while printing nothing -- adb with no device attached, for
    # one -- would never reach an in-loop deadline test.
    killed = []

    def on_timeout():
        killed.append(True)
        try:
            proc.kill()
        except Exception:
            pass

    watchdog = threading.Timer(timeout, on_timeout) if timeout else None
    if watchdog:
        watchdog.daemon = True
        watchdog.start()

    # Drain in a thread and wait on the CHILD, never on end-of-pipe. A grandchild
    # that outlives its parent keeps the write end open -- LLMDroid's AndroLog
    # monitor leaves an `adb logcat -s TAG` behind holding inherited stderr -- and
    # then reading to EOF blocks forever on a command that already finished.
    lines = []

    def drain():
        try:
            for line in iter(proc.stdout.readline, ""):
                lines.append(line)
                if log:
                    log.write(line if line.endswith("\n") else line + "\n")
        except Exception:
            pass

    reader = threading.Thread(target=drain, name="output-reader")
    reader.daemon = True
    reader.start()

    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.terminate()
        raise
    finally:
        if watchdog:
            watchdog.cancel()

    # The child is gone; give its own output a moment to land, then stop caring
    # whether anything else still holds the pipe.
    reader.join(5)
    if reader.is_alive():
        # Close the descriptor, not the file object: BufferedReader.close() waits
        # on the very lock the blocked readline() is holding, so it deadlocks too.
        # os.close() goes under that lock and makes the pending read fail out.
        try:
            os.close(proc.stdout.fileno())
        except Exception:
            pass
        reader.join(2)
        if log:
            log.write(u"[%s] %s exited but left the output pipe open "
                      u"(orphaned grandchild); continuing.\n" % (stamp(), label or command[0]))
    if killed and log:
        log.write(u"[%s] killed %s after %s\n" % (stamp(), label or command[0], human(timeout)))
    return (124 if killed else proc.returncode), "".join(lines)


def adb(args, serial=None, log=None, timeout=60):
    command = ["adb"] + (["-s", serial] if serial else []) + list(args)
    return run(command, log=log, timeout=timeout, label="adb")


def load_json(path):
    return json.load(io.open(path, encoding="utf-8"))


def save_json(path, payload):
    with io.open(path, "w", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, indent=2, ensure_ascii=False))
        handle.write(u"\n")


# ------------------------------------------------------------------- steps

METHOD_COUNT = re.compile(r"(?:total|methods?)[^\d]{0,24}?([\d,]{3,})", re.I)
TAG_IN_DEX = re.compile(rb"[A-Z0-9][A-Z0-9_]{1,30}_SUPER_LOG")


def tag_from_apk(apk):
    """The AndroLog tag actually baked into the APK.

    Authoritative over the catalogue. The tag is what the monitor greps logcat
    for, so guessing it wrong produces the worst possible failure mode: the app
    installs, launches, verifies, explores, and reports 0.00000% coverage with
    no error anywhere. Read it from the binary for the same reason the
    denominator is read from the binary.
    """
    counts = {}
    try:
        with zipfile.ZipFile(apk) as archive:
            for name in archive.namelist():
                if name.endswith(".dex"):
                    for found in TAG_IN_DEX.findall(archive.read(name)):
                        key = found.decode("ascii", "replace")
                        counts[key] = counts.get(key, 0) + 1
    except Exception:
        return None
    if not counts:
        return None
    return max(counts, key=lambda k: counts[k])


def instrument(app, cfg, log):
    """Instrument the APK and read back the real denominator and tag.

    Returns (instrumented_path, total_methods, tag) or (None, reason, None).
    """
    stem, tag = app["stem"], app["coverage_tag"]
    source = os.path.join(REPO, cfg["apk_dir"], "%s.apk" % stem)
    target = os.path.join(REPO, cfg["instrumented_dir"], "%s.apk" % stem)
    if not os.path.isfile(source) and cfg.get("auto_fetch_apks", True):
        log.write(u"[%s] no APK at %s; fetching from F-Droid\n"
                  % (stamp(), os.path.relpath(source, REPO)))
        run([sys.executable, "scripts/fetch_apks.py", "--only", stem],
            log=log, label="fetch", timeout=1800)
    if not os.path.isfile(source):
        return None, ("no APK at %s (auto-fetch %s)"
                      % (os.path.relpath(source, REPO),
                         "failed" if cfg.get("auto_fetch_apks", True) else "disabled")), None

    if os.path.isfile(target) and cfg.get("skip_completed", True):
        log.write(u"[%s] already instrumented: %s\n" % (stamp(), os.path.relpath(target, REPO)))
    else:
        rc, out = run([sys.executable, "scripts/instrument_apk.py", source, "--tag", tag],
                      log=log, label="instrument")
        if rc != 0 or not os.path.isfile(target):
            reason = "instrumentation failed (rc=%s)" % rc
            if "[0..1]" in out or "Integer1Type" in out:
                reason = "Soot [0..1] bug (Integer1Type leaked from the type assigner)"
            elif "OutOfMemory" in out:
                reason = "Soot ran out of memory"
            return None, reason, None

    # The denominator has to come from the APK under test, never from a table.
    total = None
    try:
        sys.path.insert(0, REPO)
        from droidbot.coverage.androlog_monitor import total_methods_from_apk
        total = total_methods_from_apk(target)
    except Exception as exc:
        log.write(u"[%s] could not read the denominator from the APK: %s\n" % (stamp(), exc))
    if not total:
        return None, "no AndroLog probes found in the instrumented APK", None

    baked = tag_from_apk(target)
    if baked and baked != tag:
        # Happens whenever the APK was instrumented earlier under a different
        # name than the catalogue would generate from the stem.
        log.write(u"[%s] tag in the APK is %s, not the catalogue's %s; using the APK's.\n"
                  % (stamp(), baked, tag))
        tag = baked
    elif not baked:
        log.write(u"[%s] could not read a tag from the APK; trusting the catalogue (%s)\n"
                  % (stamp(), tag))
    log.write(u"[%s] denominator: %d methods, tag %s\n" % (stamp(), total, tag))
    return target, total, tag


def package_name(apk, log):
    try:
        sys.path.insert(0, REPO)
        from droidbot.app import App
        return App(apk).get_package_name()
    except Exception as exc:
        log.write(u"[%s] could not read the package name: %s\n" % (stamp(), exc))
        return None


def verify(apk, package, cfg, log):
    """Install, launch, and fail the app if the rewritten dex does not verify."""
    serial = cfg.get("device_serial")
    adb(["install", "-r", "-g", apk], serial, log, timeout=600)
    adb(["logcat", "-c"], serial, log)
    adb(["shell", "monkey", "-p", package, "-c",
         "android.intent.category.LAUNCHER", "1"], serial, log)
    time.sleep(12)
    _, out = adb(["logcat", "-d"], serial, log=None, timeout=180)
    hits = [line for line in out.splitlines()
            if "VerifyError" in line or "FATAL EXCEPTION" in line]
    adb(["uninstall", package], serial, log)
    if hits:
        log.write(u"[%s] %d verify/crash line(s); first: %s\n"
                  % (stamp(), len(hits), hits[0][:200]))
        return False, "dex does not verify (%d VerifyError/FATAL lines)" % len(hits)
    log.write(u"[%s] launch clean, no VerifyError\n" % stamp())
    return True, ""


def write_llmdroid_config(app, total, log):
    """Fill TotalMethod from the instrumentation we just did.

    LLMDroid reads Tag and TotalMethod from ./config.json and refuses an androlog
    run without them. The number must be the one measured from this exact APK, or
    the two tools end up with different denominators and nothing is comparable.
    """
    path = os.path.join(LLMDROID, "config.json.%s" % app["stem"])
    if not os.path.isfile(path):
        return False, "missing %s (run scripts/make_feature_specs.py)" % os.path.basename(path)
    config = load_json(path)
    config["Tag"] = app["coverage_tag"]
    config["TotalMethod"] = total
    save_json(path, config)
    log.write(u"[%s] %s: Tag=%s TotalMethod=%d\n"
              % (stamp(), os.path.basename(path), config["Tag"], total))
    return True, ""


def run_testcube(app, apk, cfg, log):
    out_dir = os.path.join(REPO, cfg["testcube_output"], app["stem"])
    command = [
        sys.executable, "start.py",
        "-a", apk,
        "-o", out_dir,
        "-is_emulator",
        "-policy", cfg.get("policy", "feature_guided"),
        "-llm", cfg.get("llm_backend", "local"),
        "--code-coverage", "androlog",
        "--coverage-tag", app["coverage_tag"],
        "--max-run-seconds", str(cfg["budget_seconds"]),
        "--run-grace-seconds", str(cfg["grace_seconds"]),
        "-keep_env", "-grant_perm",
    ]
    if cfg.get("device_serial"):
        command += ["-d", cfg["device_serial"]]
    # Deliberately no -keep_app: droidbot installs only when the package is absent
    # and uninstalls at teardown. Keeping the app would let LLMDroid skip its own
    # install and inherit TestCube's state, and -grant_perm would silently do nothing.
    rc, _ = run(command, log=log, label="testcube",
                timeout=cfg["budget_seconds"] + cfg["grace_seconds"] + 600)
    return rc, out_dir


def last_error_lines(output, limit=3):
    """The lines worth reading from a failed command.

    experiment_results.json is committed but *.log is gitignored, so without
    this a collaborator's failure arrives as a bare `rc=1` with no way to tell
    why. This puts the reason in the artifact that actually travels.
    """
    interesting = [line.strip() for line in (output or "").splitlines()
                   if any(marker in line for marker in
                          ("Error", "error:", "Exception", "Traceback",
                           "ModuleNotFound", "No such file", "refused"))]
    return interesting[-limit:] if interesting else [
        line.strip() for line in (output or "").splitlines() if line.strip()][-limit:]


def run_llmdroid(app, cfg, log):
    out_dir = os.path.join(REPO, cfg["llmdroid_output"], app["stem"])
    command = [
        sys.executable, "scripts/run_llmdroid.py",
        "--app", app["stem"],
        "--tag", app["coverage_tag"],
        "--out", out_dir,
        "--timeout", str(cfg["budget_seconds"]),
        "--policy", cfg.get("llmdroid_policy", "dfs_greedy"),
        "--code-coverage", "androlog",
    ]
    rc, out = run(command, log=log, label="llmdroid",
                  timeout=cfg["budget_seconds"] + cfg["grace_seconds"] + 600)
    return rc, out_dir, (last_error_lines(out) if rc != 0 else [])


def run_compare(app, tc_dir, ld_dir, cfg, log):
    out_dir = os.path.join(REPO, cfg["compare_output"], app["stem"])
    rc, _ = run([sys.executable, "scripts/compare_coverage.py",
                 "--testcube", tc_dir, "--llmdroid", ld_dir, "--out", out_dir,
                 "--budget", str(cfg["budget_seconds"])],
                log=log, label="compare", timeout=600)
    return rc, out_dir


def run_feature_eval(app, tc_dir, cfg, log):
    folder = os.path.join(REPO, "feature", app["stem"])
    truth = os.path.join(folder, "ground_truth.json")
    if not os.path.isfile(truth):
        return 0
    command = [sys.executable, "scripts/evaluate_features.py",
               "--results", tc_dir, "--features", truth,
               "--matcher", cfg.get("feature_matcher", "ai")]
    readme = os.path.join(folder, "README.md")
    if os.path.isfile(readme):
        command += ["--readme", readme]
    rc, _ = run(command, log=log, label="evaluate", timeout=1800)
    return rc


# ------------------------------------------------------------ orchestration

def do_app(app, cfg, log):
    """Everything for one app. Returns a result dict; never raises for app failure."""
    result = {"stem": app["stem"], "package": app.get("package", ""),
              "tag": app["coverage_tag"], "started": datetime.datetime.now().isoformat(),
              "steps": {}, "status": "ok", "reason": ""}
    started = time.time()

    if cfg.get("reinstall_between_runs", True) and app.get("package"):
        # Belt and braces: a crashed run can leave the app installed, and droidbot
        # installs only when the package is absent, so the next run would inherit
        # that state instead of starting clean.
        adb(["uninstall", app["package"]], cfg.get("device_serial"), log, timeout=120)

    apk, total, tag = instrument(app, cfg, log)
    if not apk:
        result.update(status="skipped_instrumentation", reason=total)
        result["steps"]["instrument"] = "fail"
        return result
    # Everything downstream greps logcat for this tag, so it has to be the one
    # in the binary, not the one the catalogue guessed.
    app = dict(app, coverage_tag=tag)
    result["steps"]["instrument"] = "ok"
    result["total_methods"] = total
    result["tag"] = tag

    package = package_name(apk, log)
    result["package"] = package or result["package"]

    if cfg.get("verify_instrumentation", True) and package:
        ok, reason = verify(apk, package, cfg, log)
        result["steps"]["verify"] = "ok" if ok else "fail"
        if not ok:
            result.update(status="skipped_verify", reason=reason)
            return result

    ok, reason = write_llmdroid_config(app, total, log)
    result["steps"]["llmdroid_config"] = "ok" if ok else "fail"
    if not ok:
        log.write(u"[%s] %s -- LLMDroid will be skipped\n" % (stamp(), reason))

    tc_dir = os.path.join(REPO, cfg["testcube_output"], app["stem"])
    if cfg.get("run_testcube", True):
        log.write(u"\n[%s] === TestCube: %s ===\n" % (stamp(), app["stem"]))
        rc, tc_dir = run_testcube(app, apk, cfg, log)
        result["steps"]["testcube"] = "ok" if rc == 0 else ("hard_stop" if rc == EXIT_HARD_STOP
                                                            else "rc=%s" % rc)
        result["testcube_output"] = os.path.relpath(tc_dir, REPO)
        if rc == EXIT_HARD_STOP:
            log.write(u"[%s] TestCube was killed by the run-budget watchdog; "
                      u"its reports are partial.\n" % stamp())
    else:
        log.write(u"[%s] TestCube skipped (--no-testcube)\n" % stamp())

    ld_dir = None
    if cfg.get("run_llmdroid", True) and ok:
        log.write(u"\n[%s] === LLMDroid: %s ===\n" % (stamp(), app["stem"]))
        rc2, ld_dir, why = run_llmdroid(app, cfg, log)
        result["steps"]["llmdroid"] = "ok" if rc2 == 0 else "rc=%s" % rc2
        result["llmdroid_output"] = os.path.relpath(ld_dir, REPO)
        if why:
            result["llmdroid_error"] = why
            log.write(u"[%s] LLMDroid failed: %s\n" % (stamp(), " | ".join(why)))

    # Comparison and feature scoring both need TestCube output. With
    # --no-testcube they run only if an earlier TestCube result is on disk.
    have_tc = os.path.isfile(os.path.join(tc_dir, "code_coverage.json"))
    if cfg.get("run_compare", True) and ld_dir and have_tc:
        rc3, cmp_dir = run_compare(app, tc_dir, ld_dir, cfg, log)
        result["steps"]["compare"] = "ok" if rc3 == 0 else "rc=%s" % rc3
        result["compare_output"] = os.path.relpath(cmp_dir, REPO)
        summary = os.path.join(cmp_dir, "coverage_comparison.json")
        if os.path.isfile(summary):
            try:
                result["coverage"] = load_json(summary)
            except Exception:
                pass

    if cfg.get("run_feature_eval", True) and have_tc:
        rc4 = run_feature_eval(app, tc_dir, cfg, log)
        result["steps"]["feature_eval"] = "ok" if rc4 == 0 else "rc=%s" % rc4

    # Zero coverage after real exploration is the vinyl failure mode: dex that
    # installs, launches and verifies while never executing a probe. Recording it
    # as a successful 0% would put a fake data point in the comparison.
    summary_path = os.path.join(tc_dir, "code_coverage.json")
    if cfg.get("run_testcube", True) and os.path.isfile(summary_path):
        try:
            tc = load_json(summary_path)
            if not tc.get("final_coverage") and (tc.get("total_actions") or 0) >= 10:
                result["steps"]["testcube"] = "zero_coverage"
                result["zero_coverage"] = (
                    "0.00000%% after %s actions: the APK ran but emitted no AndroLog "
                    "probes. Treat as a failed instrumentation, not a real 0%%."
                    % tc.get("total_actions"))
                log.write(u"[%s] %s\n" % (stamp(), result["zero_coverage"]))
        except Exception:
            pass

    failures = [k for k, v in result["steps"].items() if v not in ("ok",)]
    if failures:
        result["status"] = "partial"
        result["reason"] = "steps not clean: " + ", ".join(sorted(failures))
    result["elapsed_seconds"] = round(time.time() - started, 1)
    return result


def choose_apps(cfg, catalogue, args):
    """Decide which apps run, and say out loud which rule decided it.

    Precedence, most specific first: --apps / --count on the command line, then
    the APK_NAMES / NUM_APKS variables at the top of this file. APK_NAMES wins
    over NUM_APKS, which is the part that is easy to get wrong, so it is printed.
    """
    by_stem = dict((a["stem"], a) for a in catalogue["apps"])
    names = [s.strip() for s in args.apps.split(",") if s.strip()] if args.apps else list(APK_NAMES)
    count = args.count if args.count is not None else NUM_APKS
    # --all and an explicit --count both mean "ignore the name list", otherwise
    # there is no way to widen the run without editing the file.
    if args.all or args.count is not None:
        names = []
    if args.all:
        count = len(catalogue["apps"])

    if names:
        source = "--apps" if args.apps else "APK_NAMES in scripts/run_experiment.py"
        say("Selecting by name (%s): %s" % (source, ", ".join(names)))
        if args.count is not None or (not args.apps and NUM_APKS):
            say("  (NUM_APKS/--count is ignored while a name list is set)")
        chosen, unknown = [], []
        for stem in names:
            (chosen if stem in by_stem else unknown).append(by_stem.get(stem, stem))
        if unknown:
            sys.stderr.write("[!] not in experiment/apps.json: %s\n"
                             % ", ".join(str(u) for u in unknown))
        missing = [a["stem"] for a in chosen
                   if not os.path.isfile(os.path.join(REPO, cfg["apk_dir"], "%s.apk" % a["stem"]))]
        if missing:
            how = ("they will be fetched from F-Droid at run time"
                   if cfg.get("auto_fetch_apks", True)
                   else "auto_fetch_apks is off, so they will be skipped")
            sys.stderr.write("[i] no binary yet in %s/ for: %s\n    (%s)\n"
                             % (cfg["apk_dir"], ", ".join(missing), how))
        return chosen

    source = ("--all" if args.all else
              "--count" if args.count is not None else
              "NUM_APKS in scripts/run_experiment.py")
    pool = [a for a in catalogue["apps"] if a["pool"] == "selected"]
    if args.usable_only:
        skipped = [a["stem"] for a in pool
                   if str(a.get("instrumentation_status", "")).startswith("fail")]
        pool = [a for a in pool
                if not str(a.get("instrumentation_status", "")).startswith("fail")]
        if skipped:
            say("Skipping %d app(s) recorded as failing instrumentation: %s"
                % (len(skipped), ", ".join(skipped)))
    present = [a for a in pool
               if os.path.isfile(os.path.join(REPO, cfg["apk_dir"], "%s.apk" % a["stem"]))
               or cfg.get("auto_fetch_apks", True)]
    absent = [a["stem"] for a in pool if a not in present]
    say("Selecting the first %d app(s) with a binary (%s); %d of %d have one."
        % (count, source, len(present), len(pool)))
    if absent:
        sys.stderr.write("[i] no APK in %s/ for: %s\n" % (cfg["apk_dir"], ", ".join(absent)))
    return present[:count]


ANDROLOG_JAR = os.path.join(REPO, "tools", "AndroLog", "target",
                            "androlog-0.1-jar-with-dependencies.jar")
ANDROID_PLATFORMS = os.path.join(REPO, "tools", "android-platforms")


def check_llmdroid_deps():
    """LLMDroid imports `openai` and `jpype` at module load.

    `jpype` is only used by the JaCoCo path, but utg_based_policy imports
    JacocoCVMonitor unconditionally, so both are required even for an androlog
    run. Missing either makes LLMDroid exit 1 for *every* app while TestCube --
    which imports neither -- succeeds, so the batch looks half-working and
    produces no comparison at all. Checked up front for that reason.
    """
    missing = []
    for module in ("openai", "jpype"):
        probe = ("import sys; sys.path.insert(0, %r); import %s"
                 % (LLMDROID, module))
        try:
            subprocess.check_output([sys.executable, "-c", probe],
                                    stderr=subprocess.STDOUT)
        except Exception:
            missing.append(module)
    if not missing:
        return True
    sys.stderr.write(
        "\nLLMDroid cannot import: %s\n\n"
        "It imports these at module load, so every LLMDroid run would exit 1 while\n"
        "TestCube kept working -- a batch that produces no comparison. Install them:\n\n"
        "    pip install openai jpype1\n\n"
        "Or run with --no-llmdroid to measure TestCube only.\n"
        % ", ".join("openai" if m == "openai" else "jpype1" for m in missing))
    return False


def check_toolchain():
    """Fail immediately when the instrumentation toolchain is absent.

    `tools/` is gitignored, so a fresh clone has neither the AndroLog jar nor the
    Soot platform stubs. Without them every single APK fails to instrument, which
    reads as "all the APKs are broken" rather than "one setup step was skipped".
    Checked before anything is downloaded so that mistake costs a second, not a
    1 GB download and twenty failed runs.
    """
    problems = []
    if not os.path.isfile(ANDROLOG_JAR):
        problems.append("AndroLog jar missing: %s" % os.path.relpath(ANDROLOG_JAR, REPO))
    if not os.path.isdir(ANDROID_PLATFORMS) or not os.listdir(ANDROID_PLATFORMS):
        problems.append("Android platforms missing: %s"
                        % os.path.relpath(ANDROID_PLATFORMS, REPO))
    try:
        subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT)
    except Exception:
        problems.append("java not on PATH (JDK 17+ required)")
    if not problems:
        return True
    sys.stderr.write(
        "\nThe instrumentation toolchain is not set up, so every APK would fail:\n\n")
    for problem in problems:
        sys.stderr.write("  - %s\n" % problem)
    sys.stderr.write(
        "\ntools/ is gitignored, so a fresh clone never has these. Run the one-time\n"
        "setup, which clones and builds them and then smoke-tests instrumentation:\n\n"
        "    bash scripts/setup_tools.sh\n\n"
        "Then re-run this command. See docs/CODE_COVERAGE.md for the manual steps.\n")
    return False


def prefetch_apks(apps, cfg, log_say=None):
    """Download every APK in the run list before the first app starts.

    The instrument step can fetch a missing APK on its own, but doing it up
    front means a broken download or a vanished F-Droid build is reported in the
    first minute rather than eighteen hours into a batch.
    """
    say_ = log_say or say
    missing = [a["stem"] for a in apps
               if not os.path.isfile(os.path.join(REPO, cfg["apk_dir"], "%s.apk" % a["stem"]))]
    if not missing:
        say_("All %d APK(s) already in %s/." % (len(apps), cfg["apk_dir"]))
        return [], []
    if not cfg.get("auto_fetch_apks", True):
        say_("%d APK(s) missing and auto_fetch_apks is off: %s"
             % (len(missing), ", ".join(missing)))
        return [], missing

    say_("Fetching %d missing APK(s) from F-Droid: %s" % (len(missing), ", ".join(missing)))
    rc, _ = run([sys.executable, "scripts/fetch_apks.py", "--only", ",".join(missing)],
                label="fetch", timeout=120 * 60)
    still = [stem for stem in missing
             if not os.path.isfile(os.path.join(REPO, cfg["apk_dir"], "%s.apk" % stem))]
    got = [stem for stem in missing if stem not in still]
    if got:
        say_("Fetched %d: %s" % (len(got), ", ".join(got)))
    if still:
        say_("Could NOT fetch %d: %s" % (len(still), ", ".join(still)))
        say_("  They will be reported as skipped_instrumentation; the batch continues.")
    return got, still


def update_catalogue(results):
    """Record what instrumentation actually did, so the next run knows."""
    try:
        catalogue = load_json(CATALOGUE)
    except Exception:
        return
    status = {}
    for item in results:
        if item["steps"].get("instrument") == "fail":
            status[item["stem"]] = "fail_instrument"
        elif item["steps"].get("verify") == "fail":
            status[item["stem"]] = "fail_verify"
        elif item["steps"].get("instrument") == "ok":
            status[item["stem"]] = "verified_ok"
    changed = False
    for app in catalogue["apps"]:
        new = status.get(app["stem"])
        if not new or app.get("instrumentation_status") == new:
            continue
        was = app.get("instrumentation_status")
        if was == "verified_ok" and new != "verified_ok":
            # Do not erase a verdict another machine measured successfully. The
            # same APK and Soot can differ by JDK, so this is a disagreement to
            # surface, not a correction to apply.
            app["instrumentation_conflict"] = new
            say("[!] %s instrumented fine elsewhere but failed here (%s); keeping "
                "verified_ok and recording the conflict." % (app["stem"], new))
            changed = True
            continue
        app["instrumentation_status"] = new
        changed = True
    if changed:
        save_json(CATALOGUE, catalogue)


def write_summary(results, cfg, path):
    lines = ["# Experiment summary", "",
             "Budget: %ds wall clock per tool per app (grace %ds)."
             % (cfg["budget_seconds"], cfg["grace_seconds"]), "",
             "| App | Package | Methods | Status | TestCube | LLMDroid | Elapsed | Note |",
             "| --- | --- | ---: | --- | --- | --- | ---: | --- |"]
    for item in results:
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
            item["stem"], item.get("package") or "-",
            item.get("total_methods", "-"), item["status"],
            item["steps"].get("testcube", "-"), item["steps"].get("llmdroid", "-"),
            human(item.get("elapsed_seconds", 0)), item.get("reason", "") or "",
        ))
    ok = [r for r in results if r["status"] == "ok"]
    gated = [r for r in results if r["status"].startswith("skipped")]
    lines += ["", "%d of %d completed cleanly; %d never got past the instrumentation gate."
              % (len(ok), len(results), len(gated))]
    if gated:
        lines += ["", "Gated out (compatibility is measured, not assumed):", ""]
        lines += ["- `%s` - %s" % (r["stem"], r["reason"]) for r in gated]
    with io.open(path, "w", encoding="utf-8") as handle:
        handle.write(u"\n".join(lines) + u"\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--config", default=CONFIG)
    parser.add_argument("--apps", default="", help="Comma-separated stems, overrides the config")
    parser.add_argument("--count", type=int, default=None,
                        help="How many apps to run. Overrides APK_NAMES.")
    parser.add_argument("--all", action="store_true",
                        help="Run every selected app that has a binary. Overrides APK_NAMES.")
    parser.add_argument("--usable-only", action="store_true",
                        help="Skip apps already recorded as failing instrumentation.")
    parser.add_argument("--budget-seconds", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true", help="Print the plan and stop")
    parser.add_argument("--resume", action="store_true",
                        help="Skip apps that already have a TestCube code_coverage.json")
    parser.add_argument("--no-llmdroid", action="store_true",
                        help="Run TestCube only.")
    parser.add_argument("--no-testcube", action="store_true",
                        help="Run LLMDroid only. Comparison and feature eval are skipped "
                             "unless a TestCube result for the app already exists.")
    args = parser.parse_args(argv)

    cfg = load_json(args.config)
    catalogue = load_json(CATALOGUE)
    if not args.dry_run:
        if not check_toolchain():
            return 2
        if cfg.get("run_llmdroid", True) and not check_llmdroid_deps():
            return 2
    if args.budget_seconds is not None:
        cfg["budget_seconds"] = args.budget_seconds
    if args.no_llmdroid:
        cfg["run_llmdroid"] = False
    if args.no_testcube:
        cfg["run_testcube"] = False
    if args.no_llmdroid and args.no_testcube:
        sys.stderr.write("--no-llmdroid and --no-testcube together leave nothing to run.\n")
        return 2

    if not args.dry_run:
        ok, holder = acquire_lock()
        if not ok:
            sys.stderr.write(
                "Another runner (pid %s) is already using the device.\n"
                "Two runners on one emulator collide: they interleave taps and each\n"
                "uninstalls the app the other is testing. Wait for it, or stop it with\n"
                "    kill %s\n" % (holder, holder))
            return 2
        rc, out = run(["adb"] + (["-s", cfg["device_serial"]] if cfg.get("device_serial") else [])
                      + ["devices"], timeout=30, label="adb")
        attached = [l for l in out.splitlines()[1:] if l.strip() and "offline" not in l]
        if rc != 0 or not attached:
            sys.stderr.write(
                "No device is attached (adb devices is empty). Start the emulator first:\n"
                "    cd ~/Library/Android/sdk/emulator && ./emulator -avd Pixel_5\n"
                "and wait for the home screen. Use --dry-run to check the plan meanwhile.\n")
            return 2
        say("Device: %s" % attached[0].split()[0])

    apps = choose_apps(cfg, catalogue, args)
    if args.resume:
        remaining = []
        for app in apps:
            done = os.path.join(REPO, cfg["testcube_output"], app["stem"], "code_coverage.json")
            if os.path.isfile(done):
                say("[=] %s already has coverage, skipping (--resume)" % app["stem"])
            else:
                remaining.append(app)
        apps = remaining
    if not apps:
        sys.stderr.write("Nothing to run. Put APKs in %s/ as <stem>.apk "
                         "(stems are listed in experiment/apps.json).\n" % cfg["apk_dir"])
        return 1

    for folder in ("testcube_output", "llmdroid_output", "compare_output", "log_dir",
                   "instrumented_dir"):
        path = os.path.join(REPO, cfg[folder])
        if not os.path.isdir(path):
            os.makedirs(path)

    missing_now = [a["stem"] for a in apps
                   if not os.path.isfile(os.path.join(REPO, cfg["apk_dir"], "%s.apk" % a["stem"]))]
    tools = ((1 if cfg.get("run_testcube", True) else 0)
             + (1 if cfg.get("run_llmdroid", True) else 0))
    total_budget = len(apps) * max(1, tools) * (cfg["budget_seconds"] + cfg["grace_seconds"])
    say("\n%d app(s): %s" % (len(apps), ", ".join(a["stem"] for a in apps)))
    say("Budget %ds per tool per app -> worst case about %s in total."
          % (cfg["budget_seconds"], human(total_budget)))
    say("TestCube -> %s\nLLMDroid -> %s\nLogs     -> %s\n"
          % (cfg["testcube_output"], cfg["llmdroid_output"], cfg["log_dir"]))
    if missing_now:
        say("%d APK(s) not yet downloaded: %s" % (len(missing_now), ", ".join(missing_now)))
        say("  %s\n" % ("they will be fetched before the first app starts"
                        if cfg.get("auto_fetch_apks", True)
                        else "auto_fetch_apks is off, so these will be skipped"))
    if args.dry_run:
        say("--dry-run: nothing executed.")
        return 0

    # Everything the batch needs, downloaded before any of it runs.
    prefetch_apks(apps, cfg)

    # AndroLog floods the default logcat buffer.
    adb(["logcat", "-G", cfg.get("logcat_buffer", "64M")], cfg.get("device_serial"))

    results = []
    run_started = time.time()
    for index, app in enumerate(apps, start=1):
        log_path = os.path.join(REPO, cfg["log_dir"], "%s.log" % app["stem"])
        log = Tee(log_path)
        header = u"\n%s\n[%d/%d] %s  (%s)\n%s\n" % (
            "=" * 72, index, len(apps), app["stem"], app.get("dataset_name", ""), "=" * 72)
        log.write(header)
        try:
            result = do_app(app, cfg, log)
        except KeyboardInterrupt:
            log.write(u"\n[%s] interrupted by the user.\n" % stamp())
            log.close()
            say("\nInterrupted. Partial results kept.")
            break
        except Exception as exc:
            # One app must never take the experiment down with it.
            import traceback
            log.write(u"\n[%s] unhandled error: %s\n%s\n"
                      % (stamp(), exc, traceback.format_exc()))
            result = {"stem": app["stem"], "status": "error", "reason": str(exc),
                      "steps": {}, "elapsed_seconds": 0}
        finally:
            log.close()
        results.append(result)
        say("[%s] %-22s %-24s %s"
              % (stamp(), app["stem"], result["status"],
                 result.get("reason", "") or human(result.get("elapsed_seconds", 0))))

        summary_dir = os.path.join(REPO, cfg["compare_output"])
        save_json(os.path.join(summary_dir, "experiment_results.json"),
                  {"config": cfg, "results": results})
        write_summary(results, cfg, os.path.join(summary_dir, "experiment_summary.md"))
        update_catalogue(results)

    release_lock()
    say("\nDone in %s. %d app(s) attempted." % (human(time.time() - run_started), len(results)))
    say("Summary: %s" % os.path.join(cfg["compare_output"], "experiment_summary.md"))
    gated = [r for r in results if r["status"].startswith("skipped")]
    if gated:
        say("\n%d app(s) did not pass the instrumentation gate:" % len(gated))
        for item in gated:
            say("  %-22s %s" % (item["stem"], item["reason"]))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    finally:
        release_lock()
