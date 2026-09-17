#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Check that every app in the experiment catalogue is ready to run.

Two different questions, kept apart on purpose:

* **Files** - are the four spec files and the LLMDroid config present and valid?
  Checkable for every app, right now, without a device.
* **Compatibility** - does the APK survive AndroLog/Soot instrumentation and does
  the rewritten dex verify? NOT checkable without the binary. docs/CODE_COVERAGE.md
  records six of eight APKs failing, and neither obfuscation nor dex version
  predicts it, so this column reports measured evidence only and says "no APK" or
  "untested" rather than guessing.

    python scripts/check_experiment_setup.py
    python scripts/check_experiment_setup.py --pool all --verbose
"""

from __future__ import print_function

import argparse
import io
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LLMDROID = os.path.join(REPO, "compare", "LLMDroid", "LLMDroid-Droidbot")

REQUIRED_SPECS = ("README.md", "ground_truth.json", "guide_features.json", "credential.txt")
# The tester types these; a spec missing all of them cannot fill a form.
USEFUL_CREDENTIAL_KEYS = ("search_query", "email", "pwd", "title", "note_title",
                          "file_name", "folder_name", "account_name", "label")


def load(path):
    return json.load(io.open(path, encoding="utf-8"))


def check_feature_json(path, kind):
    """Return (n_features, [problems])."""
    problems = []
    try:
        data = load(path)
    except Exception as exc:
        return 0, ["%s is not valid JSON: %s" % (kind, exc)]
    features = data.get("features")
    if not isinstance(features, list) or not features:
        return 0, ["%s has no 'features' list" % kind]
    for index, item in enumerate(features):
        for field in ("id", "name", "actions"):
            if not item.get(field):
                problems.append("%s feature #%d has no '%s'" % (kind, index + 1, field))
        if not isinstance(item.get("actions"), list) or not item.get("actions"):
            problems.append("%s feature %s has no action steps" % (kind, item.get("id")))
        if len(problems) > 4:
            problems.append("%s ... further problems suppressed" % kind)
            break
    return len(features), problems


def check_app(app, args):
    stem = app["stem"]
    row = {"stem": stem, "problems": [], "warnings": []}
    folder = os.path.join(REPO, "feature", stem)

    for name in REQUIRED_SPECS:
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            row["problems"].append("missing feature/%s/%s" % (stem, name))
        elif os.path.getsize(path) == 0:
            row["problems"].append("empty feature/%s/%s" % (stem, name))

    gt_path = os.path.join(folder, "ground_truth.json")
    guide_path = os.path.join(folder, "guide_features.json")
    row["gt"] = row["guide"] = 0
    if os.path.isfile(gt_path):
        row["gt"], problems = check_feature_json(gt_path, "ground_truth")
        row["problems"] += problems
    if os.path.isfile(guide_path):
        row["guide"], problems = check_feature_json(guide_path, "guide_features")
        row["problems"] += problems

    # The rule that decides whether a score is coverage or guided-execution coverage.
    row["independence"] = "-"
    if os.path.isfile(gt_path) and os.path.isfile(guide_path):
        try:
            sys.path.insert(0, REPO)
            from droidbot.feature_tester.guide import classify_ground_truth_source
            row["independence"] = classify_ground_truth_source(guide_path, gt_path)
            if row["independence"] != "independent_labeled_set":
                row["problems"].append(
                    "guide and ground truth share a name set: the run would be graded "
                    "against the list that drove it")
        except Exception as exc:
            row["warnings"].append("could not classify independence: %s" % exc)

    credential = os.path.join(folder, "credential.txt")
    if os.path.isfile(credential):
        text = io.open(credential, encoding="utf-8").read()
        keys = set(line.split(":", 1)[0].strip() for line in text.splitlines() if ":" in line)
        row["cred_keys"] = len(keys)
        if not keys & set(USEFUL_CREDENTIAL_KEYS):
            row["warnings"].append("credential.txt has no commonly used field names")
    else:
        row["cred_keys"] = 0

    config_path = os.path.join(LLMDROID, "config.json.%s" % stem)
    row["llmdroid"] = "missing"
    if os.path.isfile(config_path):
        try:
            config = load(config_path)
            missing = [k for k in ("AppName", "Description", "Tag", "TotalMethod")
                       if k not in config]
            if missing:
                row["problems"].append("config.json.%s lacks %s" % (stem, ", ".join(missing)))
                row["llmdroid"] = "incomplete"
            elif not config.get("TotalMethod"):
                # Expected until the APK is instrumented; the runner fills it in.
                row["llmdroid"] = "TotalMethod=0"
            else:
                row["llmdroid"] = "TotalMethod=%d" % config["TotalMethod"]
            if not config.get("Description", "").strip():
                row["problems"].append("config.json.%s has an empty Description "
                                       "(LLMDroid's only app context)" % stem)
        except Exception as exc:
            row["problems"].append("config.json.%s is not valid JSON: %s" % (stem, exc))
    else:
        row["problems"].append("missing config.json.%s" % stem)

    apk = os.path.join(REPO, "apks", "%s.apk" % stem)
    instrumented = os.path.join(REPO, "apks", "instrumented", "%s.apk" % stem)
    row["apk"] = os.path.isfile(apk)
    row["instrumented"] = os.path.isfile(instrumented)

    status = app.get("instrumentation_status", "untested")
    if not row["apk"]:
        row["compat"] = "no APK"
    elif status == "verified_ok":
        row["compat"] = "VERIFIED both"
    elif status.startswith("known_fail") or status.startswith("fail"):
        row["compat"] = "FAILS (%s)" % status
    else:
        row["compat"] = "untested"
    return row


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pool", default="selected", choices=["selected", "reserve", "all"])
    parser.add_argument("--verbose", action="store_true", help="List every problem")
    args = parser.parse_args(argv)

    catalogue = load(os.path.join(REPO, "experiment", "apps.json"))
    apps = [a for a in catalogue["apps"] if args.pool == "all" or a["pool"] == args.pool]

    print("%-22s %4s %5s %-24s %4s %-16s %-7s %-6s %s"
          % ("app", "GT", "guide", "independence", "cred", "llmdroid cfg",
             "apk", "instr", "compatibility"))
    print("-" * 118)
    bad = []
    for app in apps:
        row = check_app(app, args)
        if row["problems"]:
            bad.append(row)
        print("%-22s %4d %5d %-24s %4d %-16s %-7s %-6s %s" % (
            row["stem"], row["gt"], row["guide"],
            row["independence"].replace("_labeled_set", "").replace("independent", "independent"),
            row["cred_keys"], row["llmdroid"],
            "yes" if row["apk"] else "-", "yes" if row["instrumented"] else "-",
            row["compat"]))

    print()
    ok = len(apps) - len(bad)
    print("Files: %d of %d app(s) complete and valid." % (ok, len(apps)))
    if bad:
        print("\nProblems:")
        for row in bad:
            for problem in (row["problems"] if args.verbose else row["problems"][:2]):
                print("  %-22s %s" % (row["stem"], problem))

    verified = [a for a in apps if check_app(a, args)["compat"] == "VERIFIED both"]
    no_apk = [a for a in apps if not os.path.isfile(
        os.path.join(REPO, "apks", "%s.apk" % a["stem"]))]
    print("\nCompatibility: %d verified on both tools, %d have no APK to test, %d untested."
          % (len(verified), len(no_apk), len(apps) - len(verified) - len(no_apk)))
    if no_apk:
        print("  Compatibility cannot be asserted without the binary: it means surviving")
        print("  Soot instrumentation and dex verification, which docs/CODE_COVERAGE.md")
        print("  shows is not predictable from the app. Drop each APK at apks/<stem>.apk")
        print("  and run scripts/run_experiment.py; its preflight decides.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
