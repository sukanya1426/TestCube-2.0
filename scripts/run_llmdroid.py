#!/usr/bin/env python
"""Run LLMDroid and keep its output next to TestCube's, under output/llmdroid/.

LLMDroid must be started from its own directory (it reads ./config.json), so
its -o path lands inside compare/LLMDroid/LLMDroid-Droidbot/output/ and is easy
to lose. This wrapper runs it from the right cwd but points -o at a directory
under the repo's own output/llmdroid/, and swaps in the matching config.json
for the app being tested.

    python scripts/run_llmdroid.py --app spotube --tag SPOTUBE_SUPER_LOG

Result lands in output/llmdroid/<app>/ alongside output/<app>/ for TestCube.
"""

import argparse
import os
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LLMDROID = os.path.join(REPO, "compare", "LLMDroid", "LLMDroid-Droidbot")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Run LLMDroid with output under output/llmdroid/.")
    parser.add_argument("--app", required=True, help="App stem, e.g. spotube (uses apks/instrumented/<app>.apk)")
    parser.add_argument("--tag", default=None, help="AndroLog tag (default: <APP>_SUPER_LOG)")
    parser.add_argument("--apk", default=None, help="Override APK path")
    parser.add_argument("--out", default=None, help="Override output dir")
    parser.add_argument("--config", default=None, help="config.json to use (default: config.json.<app>)")
    parser.add_argument("--timeout", type=int, default=2700)
    parser.add_argument("--count", type=int, default=300)
    parser.add_argument("--interval", type=int, default=3)
    parser.add_argument("--policy", default="dfs_greedy")
    parser.add_argument("--code-coverage", dest="code_coverage", default="androlog",
                        choices=["none", "time", "androlog", "jacoco"])
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    apk = args.apk or os.path.join(REPO, "apks", "instrumented", "%s.apk" % args.app)
    if not os.path.exists(apk):
        sys.stderr.write("APK not found: %s\nInstrument it first with scripts/instrument_apk.py\n" % apk)
        return 2

    out_dir = args.out or os.path.join(REPO, "output", "llmdroid", args.app)
    os.makedirs(os.path.dirname(out_dir), exist_ok=True)

    # LLMDroid reads ./config.json from its own directory; swap in the app's
    # config and restore whatever was there afterwards.
    active = os.path.join(LLMDROID, "config.json")
    chosen = args.config or os.path.join(LLMDROID, "config.json.%s" % args.app)
    backup = None
    if not os.path.exists(chosen):
        sys.stderr.write(
            "No config for '%s': %s\nCreate it with Tag + TotalMethod (see docs/CODE_COVERAGE.md).\n"
            % (args.app, chosen)
        )
        return 2
    if os.path.exists(active):
        backup = active + ".bak-runner"
        shutil.copy2(active, backup)
    shutil.copy2(chosen, active)

    command = [
        sys.executable, "start.py",
        "-a", apk,
        "-o", out_dir,
        "-is_emulator",
        "-policy", args.policy,
        "-code_coverage", args.code_coverage,
        "-timeout", str(args.timeout),
        "-count", str(args.count),
        "-interval", str(args.interval),
        "-keep_app", "-keep_env", "-grant_perm",
    ]
    print("[*] cwd: %s" % LLMDROID)
    print("[*] %s" % " ".join(command))
    print("[*] output -> %s" % out_dir)
    try:
        result = subprocess.run(command, cwd=LLMDROID)
    finally:
        if backup:
            shutil.move(backup, active)
    print("\n[✓] LLMDroid output: %s" % out_dir)
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
