#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Download the experiment's APKs from F-Droid into apks/<stem>.apk.

Every app in the selected pool is open source and published on F-Droid, so the
binaries can be fetched by package name rather than hunted for by hand. The stem
in experiment/apps.json decides the filename, because that is what
droidbot/feature_tester/specs.py uses to find feature/<stem>/.

Each download is verified before it is kept:

  * the file is a real ZIP containing classes.dex and AndroidManifest.xml
  * the package name inside the APK matches the one in the catalogue

An APK that fails either check is deleted rather than left to fail later inside
an experiment run, where a corrupt download looks like an instrumentation bug.

The dataset documents a specific version per app. This prefers that exact
versionName and falls back to F-Droid's suggested version, saying which it used,
because a spec written against 2.16.1 may not match a much later build.

    python scripts/fetch_apks.py                    # everything still missing
    python scripts/fetch_apks.py --only markor,aegis
    python scripts/fetch_apks.py --force            # re-download existing
    python scripts/fetch_apks.py --list             # show the plan, download nothing
"""

from __future__ import print_function

import argparse
import io
import json
import os
import re
import shutil
import sys
import zipfile

try:
    from urllib.request import urlopen, Request
    from urllib.error import URLError, HTTPError
except ImportError:                                       # Python 2
    from urllib2 import urlopen, Request, URLError, HTTPError

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOGUE = os.path.join(REPO, "experiment", "apps.json")
API = "https://f-droid.org/api/v1/packages/%s"
DOWNLOAD = "https://f-droid.org/repo/%s_%d.apk"
# Builds age out of the main index into the archive repo. newpipe 0.27.0 is the
# version this project measures, and F-Droid no longer lists it.
ARCHIVE = "https://f-droid.org/archive/%s_%d.apk"
UA = {"User-Agent": "TestCube-experiment-fetcher/1.0"}
TIMEOUT = 120


def fetch(url, timeout=TIMEOUT):
    return urlopen(Request(url, headers=UA), timeout=timeout)


def human(size):
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return "%.1f%s" % (size, unit)
        size /= 1024.0


def pick_version(package, wanted, wanted_code=None, pinned=None):
    """(versionCode, versionName, note) for the build to download.

    A `pin_version_code` in the catalogue wins over everything, including
    F-Droid's suggestion. newpipe is the reason: 0.27.0 instruments cleanly and
    0.29.1 does not, so "latest" silently rebuilds apks/ with a broken APK.
    """
    if pinned:
        return pinned, None, "pinned by the catalogue"
    try:
        data = json.loads(fetch(API % package, timeout=45).read().decode("utf-8"))
    except (URLError, HTTPError, ValueError) as exc:
        return None, None, "F-Droid has no API entry for %s (%s)" % (package, exc)
    builds = data.get("packages") or []
    if not builds:
        return None, None, "F-Droid lists no builds for %s" % package

    if wanted:
        for build in builds:
            if build.get("versionName") == wanted:
                return build["versionCode"], wanted, "exact version from the dataset"
    # The dataset writes "F-Droid build 28" for apps with no marketing version;
    # that number is the versionCode, so it pins a build just as precisely.
    if wanted_code is not None:
        for build in builds:
            if build.get("versionCode") == wanted_code:
                return (wanted_code, build.get("versionName"),
                        "exact F-Droid build %d from the dataset" % wanted_code)
    suggested = data.get("suggestedVersionCode")
    for build in builds:
        if build.get("versionCode") == suggested:
            return (build["versionCode"], build.get("versionName"),
                    "latest (dataset wanted %s)" % wanted if wanted else "latest")
    newest = max(builds, key=lambda b: b.get("versionCode", 0))
    return (newest["versionCode"], newest.get("versionName"),
            "newest available (dataset wanted %s)" % wanted if wanted else "newest available")


def verify(path, expected_package):
    """(ok, detail). A download that is not a usable APK must not be kept."""
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
    except Exception as exc:
        return False, "not a valid ZIP/APK: %s" % exc
    if "AndroidManifest.xml" not in names:
        return False, "no AndroidManifest.xml"
    if not any(n.startswith("classes") and n.endswith(".dex") for n in names):
        return False, "no classes.dex"
    try:
        sys.path.insert(0, REPO)
        # androguard logs the whole manifest parse at DEBUG; without this the
        # useful line for each app is buried under thousands of lines.
        try:
            from loguru import logger as _androguard_logger
            _androguard_logger.remove()
        except Exception:
            pass
        from androguard.core.apk import APK
        found = APK(path).get_package()
    except Exception:
        return True, "structure ok (package not checked: androguard unavailable)"
    if expected_package and found != expected_package:
        return False, "package is %s, expected %s" % (found, expected_package)
    return True, "package %s" % found


def download(url, destination):
    partial = destination + ".part"
    with fetch(url) as response:
        total = int(response.headers.get("Content-Length") or 0)
        got = 0
        with open(partial, "wb") as handle:
            while True:
                chunk = response.read(262144)
                if not chunk:
                    break
                handle.write(chunk)
                got += len(chunk)
                if total:
                    sys.stdout.write("\r      %s / %s (%d%%)"
                                     % (human(got), human(total), got * 100 // total))
                    sys.stdout.flush()
    if total:
        sys.stdout.write("\r" + " " * 40 + "\r")
        sys.stdout.flush()
    shutil.move(partial, destination)
    return got


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--only", default="", help="Comma-separated stems")
    parser.add_argument("--pool", default="selected", choices=["selected", "reserve", "all"])
    parser.add_argument("--force", action="store_true", help="Re-download even if present")
    parser.add_argument("--list", action="store_true", help="Show the plan and stop")
    args = parser.parse_args(argv)

    catalogue = json.load(io.open(CATALOGUE, encoding="utf-8"))
    only = set(s.strip() for s in args.only.split(",") if s.strip())
    apps = [a for a in catalogue["apps"]
            if (args.pool == "all" or a["pool"] == args.pool)
            and (not only or a["stem"] in only)]

    apk_dir = os.path.join(REPO, "apks")
    if not os.path.isdir(apk_dir):
        os.makedirs(apk_dir)

    done, skipped, failed = [], [], []
    for index, app in enumerate(apps, start=1):
        stem, package = app["stem"], app.get("package")
        destination = os.path.join(apk_dir, "%s.apk" % stem)
        label = "[%d/%d] %-22s" % (index, len(apps), stem)

        if os.path.isfile(destination) and not args.force:
            print("%s already at apks/%s.apk (%s)"
                  % (label, stem, human(os.path.getsize(destination))))
            skipped.append(stem)
            continue
        if not package:
            print("%s no package name in the catalogue" % label)
            failed.append((stem, "no package name"))
            continue

        wanted = (app.get("dataset_version") or "").strip()
        wanted_code = None
        match = re.match(r"F-Droid build (\d+)", wanted)
        if match:
            wanted_code = int(match.group(1))
        if match or wanted.startswith("LLMDroid"):
            wanted = ""                     # not a versionName F-Droid would match
        code, name, note = pick_version(package, wanted, wanted_code,
                                        app.get("pin_version_code"))
        if not code:
            print("%s %s" % (label, note))
            failed.append((stem, note))
            continue
        if args.list:
            print("%s %s  v%s (code %d)  [%s]"
                  % (label, package, name or "?", code, note))
            continue

        print("%s %s v%s ... " % (label, package, name or "code %d" % code), end="")
        sys.stdout.flush()
        size, last = None, None
        try:
            for url in (DOWNLOAD % (package, code), ARCHIVE % (package, code)):
                try:
                    size = download(url, destination)
                    break
                except (URLError, HTTPError) as exc:
                    last = exc                  # aged out of /repo/; try /archive/
        except KeyboardInterrupt:
            for leftover in (destination + ".part",):
                if os.path.isfile(leftover):
                    os.remove(leftover)
            print("\ninterrupted.")
            break
        if size is None:
            print("download failed: %s" % last)
            failed.append((stem, "download failed: %s" % last))
            continue

        ok, detail = verify(destination, package)
        if not ok:
            os.remove(destination)
            print("REJECTED (%s)" % detail)
            failed.append((stem, detail))
            continue
        print("%s ok, %s [%s]" % (human(size), detail, note))
        done.append(stem)

    if args.list:
        return 0
    print("\n%d downloaded, %d already present, %d failed." % (len(done), len(skipped), len(failed)))
    if failed:
        print("\nFailed:")
        for stem, why in failed:
            print("  %-22s %s" % (stem, why))
        print("\nFetch these by hand from f-droid.org and save as apks/<stem>.apk.")
    if done:
        print("\nNext: python scripts/check_experiment_setup.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
