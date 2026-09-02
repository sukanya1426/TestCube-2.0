#!/usr/bin/env python
"""Collect JaCoCo method coverage from a running instrumented app.

Uses JacocoBridge.jar (same protocol as LLMDroid):
  1. adb broadcast → app writes .ec file
  2. adb pull .ec
  3. Analyze vs instrumented .class files

Examples:

    python jococo_test/scripts/collect_coverage.py \\
        --config jococo_test/output/spotube/jacoco.config.json

    python jococo_test/scripts/collect_coverage.py \\
        --config jococo_test/output/spotube/jacoco.config.json \\
        --watch 300 --out jococo_test/output/spotube/codecoverage.txt
"""

from __future__ import print_function

import argparse
import json
import os
import subprocess
import sys
import time

JOCO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_JAR = os.path.join(JOCO_ROOT, "JacocoBridge", "JacocoBridge.jar")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Collect JaCoCo coverage via JacocoBridge.")
    parser.add_argument("--config", required=True, help="jacoco.config.json from instrument_apk.py")
    parser.add_argument("--device", default=None, help="adb serial (-s)")
    parser.add_argument("--jar", default=DEFAULT_JAR, help="JacocoBridge.jar path")
    parser.add_argument(
        "--watch",
        type=int,
        default=0,
        help="Sample every 3s for N seconds (0 = single sample)",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Write samples to this file (default: <config_dir>/codecoverage.txt)",
    )
    parser.add_argument(
        "--pull-dir",
        default=None,
        help="Local dir for pulled .ec files (default: config directory)",
    )
    return parser.parse_args(argv)


def load_config(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def run_bridge(jar, udid, pull_dir, class_path, ec_path, ec_name):
    bridge_cmd = [
        "java", "-jar", jar,
        "-t", "1",
        "--classFile", class_path,
        "--ecFilePath", ec_path,
        "--ecFileName", ec_name,
        "--pullPath", pull_dir,
        "-o", os.path.join(pull_dir, ".coverage_once.txt"),
    ]
    if udid:
        bridge_cmd.extend(["-s", udid])
    print("[*] %s" % " ".join(bridge_cmd))
    result = subprocess.run(bridge_cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.returncode != 0:
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        return None
    out_file = os.path.join(pull_dir, ".coverage_once.txt")
    if os.path.isfile(out_file):
        with open(out_file, "r", encoding="utf-8") as handle:
            lines = [line.strip() for line in handle if line.strip()]
        if lines:
            return float(lines[-1].rstrip("%"))
    return None


def main(argv=None):
    args = parse_args(argv)
    if not os.path.isfile(args.jar):
        sys.stderr.write("JacocoBridge.jar not found: %s\nRun bash jococo_test/setup.sh\n" % args.jar)
        return 2

    cfg = load_config(os.path.abspath(args.config))
    config_dir = os.path.dirname(os.path.abspath(args.config))
    pull_dir = os.path.abspath(args.pull_dir or config_dir)
    out_path = args.out or os.path.join(config_dir, "codecoverage.txt")

    class_path = cfg.get("ClassFilePath") or cfg.get("class_file_path")
    ec_path = cfg.get("EcFilePath") or cfg.get("ec_file_path")
    ec_name = cfg.get("EcFileName") or cfg.get("ec_file_name")
    if not all((class_path, ec_path, ec_name)):
        sys.stderr.write("Config must include ClassFilePath, EcFilePath, EcFileName\n")
        return 2
    if not os.path.isdir(class_path):
        sys.stderr.write("ClassFilePath not found: %s\n" % class_path)
        return 2

    os.makedirs(pull_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write("code coverage\n")
        handle.write("start time: %s\n" % time.strftime("%Y-%m-%d %H:%M:%S"))

    deadline = time.time() + args.watch if args.watch else time.time()
    sample = 0
    while True:
        pct = run_bridge(args.jar, args.device, pull_dir, class_path, ec_path, ec_name)
        sample += 1
        if pct is not None:
            line = "%.5f%%" % pct
            print("[sample %d] %s" % (sample, line))
            with open(out_path, "a", encoding="utf-8") as handle:
                handle.write(line + "\n")
        else:
            print("[sample %d] failed" % sample, file=sys.stderr)

        if time.time() >= deadline:
            break
        time.sleep(3)

    print("Wrote %s" % out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
