#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Instrument every catalogue APK and record which ones actually work.

This answers the only question that decides whether an app can be used at all:
does it survive AndroLog/Soot instrumentation? It is not predictable from the
app -- docs/CODE_COVERAGE.md records the least obfuscated APK measured failing
while an obfuscated one passed -- so it is measured, once, and the verdict is
written back into experiment/apps.json as `instrumentation_status`.

It does NOT install or launch anything, so it needs no emulator and can run
unattended. The dex-verification half of the gate still happens inside
scripts/run_experiment.py, which installs and greps for VerifyError.

    python scripts/survey_instrumentation.py            # everything not yet done
    python scripts/survey_instrumentation.py --redo     # including known results
    python scripts/survey_instrumentation.py --only markor,aegis
"""

from __future__ import print_function

import argparse
import io
import json
import os
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOGUE = os.path.join(REPO, "experiment", "apps.json")
PER_APK_TIMEOUT = 1800


def classify(output):
    if "[0..1]" in output or "Integer1Type" in output:
        return "fail_soot_0_1", "Soot [0..1] bug (Integer1Type leaked from the type assigner)"
    if "OutOfMemoryError" in output or "java.lang.OutOfMemory" in output:
        return "fail_oom", "Soot ran out of memory"
    for line in output.splitlines():
        if "Exception" in line or "Error" in line:
            return "fail_other", line.strip()[:120]
    return "fail_other", "instrumentation produced no APK"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--only", default="")
    parser.add_argument("--pool", default="selected", choices=["selected", "reserve", "all"])
    parser.add_argument("--redo", action="store_true",
                        help="Re-test apps that already have a recorded verdict")
    args = parser.parse_args(argv)

    catalogue = json.load(io.open(CATALOGUE, encoding="utf-8"))
    only = set(s.strip() for s in args.only.split(",") if s.strip())
    apps = [a for a in catalogue["apps"]
            if (args.pool == "all" or a["pool"] == args.pool)
            and (not only or a["stem"] in only)]

    sys.path.insert(0, REPO)
    from droidbot.coverage.androlog_monitor import total_methods_from_apk

    started = time.time()
    results = {}
    for index, app in enumerate(apps, start=1):
        stem = app["stem"]
        source = os.path.join(REPO, "apks", "%s.apk" % stem)
        target = os.path.join(REPO, "apks", "instrumented", "%s.apk" % stem)
        label = "[%2d/%d] %-22s" % (index, len(apps), stem)

        if not os.path.isfile(source):
            print("%s no APK in apks/" % label)
            results[stem] = ("no_apk", "no binary")
            continue
        if os.path.isfile(target) and not args.redo:
            total = total_methods_from_apk(target) or 0
            print("%s already instrumented, %d methods" % (label, total))
            results[stem] = ("verified_ok", total)
            continue
        if app.get("instrumentation_status", "").startswith("fail") and not args.redo:
            print("%s known failure, skipping (--redo to retest)" % label)
            continue

        print("%s instrumenting ... " % label, end="")
        sys.stdout.flush()
        began = time.time()
        try:
            proc = subprocess.run(
                [sys.executable, "scripts/instrument_apk.py", source,
                 "--tag", app["coverage_tag"]],
                cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                universal_newlines=True, timeout=PER_APK_TIMEOUT)
            output = proc.stdout or ""
        except subprocess.TimeoutExpired:
            print("TIMEOUT after %ds" % PER_APK_TIMEOUT)
            results[stem] = ("fail_timeout", "exceeded %ds" % PER_APK_TIMEOUT)
            continue

        took = time.time() - began
        if os.path.isfile(target):
            total = total_methods_from_apk(target) or 0
            print("OK   %7d methods  (%.0fs)" % (total, took))
            results[stem] = ("verified_ok", total)
        else:
            status, detail = classify(output)
            print("FAIL %s  (%.0fs)" % (detail, took))
            results[stem] = (status, detail)

        for entry in catalogue["apps"]:
            if entry["stem"] == stem:
                entry["instrumentation_status"] = results[stem][0]
        with io.open(CATALOGUE, "w", encoding="utf-8") as handle:
            handle.write(json.dumps(catalogue, indent=2, ensure_ascii=False))
            handle.write(u"\n")

    ok = [s for s, (status, _) in results.items() if status == "verified_ok"]
    bad = [(s, d) for s, (status, d) in results.items() if status.startswith("fail")]
    print("\n%d usable, %d failed, in %.0f min."
          % (len(ok), len(bad), (time.time() - started) / 60.0))
    if ok:
        print("\nUsable with both tools:")
        for stem in ok:
            print("  %-22s %s methods" % (stem, results[stem][1]))
    if bad:
        print("\nFailed instrumentation:")
        for stem, detail in bad:
            print("  %-22s %s" % (stem, detail))
    print("\nVerdicts written to experiment/apps.json.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
