#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Score feature coverage for both tools, offline, with identical parameters.

Scoring is LLM work with no device involved, so it does not belong inside a
per-app run budget: inline, one TestCube evaluation took 6h24m and turned a
1-hour app into 7.5 hours. Doing it here also guarantees the only thing that
makes the two numbers comparable -- the same ground truth, the same matcher,
the same evidence window, and `--trace-only` on both.

`--trace-only` is the default and matters. TestCube writes a journal of its own
per-feature verdicts, and the judge's prompt otherwise contains
`Journal: covered | ...` for TestCube and `Journal: none` for LLMDroid: the
judge is told the answer for one tool only. Scoring from the observed trace
alone is what makes it a comparison.

    python scripts/score_features.py                      # every app with a trace
    python scripts/score_features.py --apps markor,money
    python scripts/score_features.py --tools llmdroid     # one side only
    python scripts/score_features.py --timeout 1800       # per evaluation
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
TOOL_DIRS = {"testcube": "output/experiment/testcube",
             "llmdroid": "output/experiment/llmdroid"}


def has_trace(path):
    return os.path.isdir(os.path.join(path, "events"))


def score(tool, app, args):
    """Returns (status, detail). Never raises."""
    results = os.path.join(REPO, TOOL_DIRS[tool], app)
    truth = os.path.join(REPO, "feature", app, "ground_truth.json")
    readme = os.path.join(REPO, "feature", app, "README.md")
    if not has_trace(results):
        return "no_trace", "no events/ under %s" % os.path.relpath(results, REPO)
    if not os.path.isfile(truth):
        return "no_truth", "no feature/%s/ground_truth.json" % app
    report = os.path.join(results, "feature_coverage", "report.json")
    if os.path.isfile(report) and not args.force:
        return "skipped", "already scored (use --force)"

    command = [sys.executable, "scripts/evaluate_features.py",
               "--results", results, "--features", truth,
               "--matcher", args.matcher]
    if args.trace_only:
        command.append("--trace-only")
    if os.path.isfile(readme):
        command += ["--readme", readme]

    env = dict(os.environ)
    env["TESTCUBE_JUDGE_EVIDENCE"] = str(args.evidence)
    began = time.time()
    try:
        proc = subprocess.run(command, cwd=REPO, env=env, timeout=args.timeout,
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              universal_newlines=True)
    except subprocess.TimeoutExpired:
        return "timeout", "exceeded %ds" % args.timeout
    took = time.time() - began
    if proc.returncode != 0:
        tail = [l for l in (proc.stdout or "").splitlines() if l.strip()][-1:]
        return "failed", "rc=%s %s" % (proc.returncode, tail[0][:90] if tail else "")
    return "ok", "%.0fs" % took


def read_score(tool, app):
    p = os.path.join(REPO, TOOL_DIRS[tool], app, "feature_coverage", "report.json")
    if not os.path.isfile(p):
        return None
    try:
        d = json.load(io.open(p, encoding="utf-8"))
    except (OSError, ValueError):
        return None
    covered = d.get("covered_features")
    partial = d.get("partial_features")
    return {
        "coverage": d.get("coverage_percentage"),
        "covered": covered if isinstance(covered, int) else len(covered or []),
        "partial": partial if isinstance(partial, int) else len(partial or []),
        "total": d.get("total_features"),
        "actions": d.get("total_actions"),
        "matcher": d.get("matcher_mode"),
        "trace_only": d.get("trace_only"),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apps", default="", help="Comma-separated app stems (default: all)")
    parser.add_argument("--tools", default="testcube,llmdroid")
    parser.add_argument("--matcher", default="ai", choices=["ai", "deterministic", "hybrid"])
    parser.add_argument("--evidence", type=int, default=24,
                        help="Evidence lines per feature, identical for both tools")
    parser.add_argument("--timeout", type=int, default=2700,
                        help="Hard cap per evaluation, in seconds")
    parser.add_argument("--force", action="store_true", help="Re-score even if a report exists")
    parser.add_argument("--no-trace-only", dest="trace_only", action="store_false",
                        help="Let TestCube use its journal. Makes the two tools NOT comparable.")
    # Accepted explicitly too, since it is the thing that makes the comparison
    # valid and is worth being able to state on the command line.
    parser.add_argument("--trace-only", dest="trace_only", action="store_true",
                        help="Score both tools from the observed trace only (the default).")
    parser.set_defaults(trace_only=True)
    parser.add_argument("--table-only", action="store_true", help="Print existing scores, score nothing")
    args = parser.parse_args(argv)

    tools = [t.strip() for t in args.tools.split(",") if t.strip()]
    if args.apps:
        apps = [a.strip() for a in args.apps.split(",") if a.strip()]
    else:
        apps = sorted({name for tool in tools
                       for name in os.listdir(os.path.join(REPO, TOOL_DIRS[tool]))
                       if has_trace(os.path.join(REPO, TOOL_DIRS[tool], name))})

    if not args.trace_only:
        print("WARNING: --no-trace-only lets TestCube's journal into the judge's prompt.\n"
              "         The two tools are then not comparable.\n")

    if not args.table_only:
        print("Scoring %d app(s) x %d tool(s): matcher=%s evidence=%d trace_only=%s\n"
              % (len(apps), len(tools), args.matcher, args.evidence, args.trace_only))
        for app in apps:
            for tool in tools:
                print("  %-22s %-9s ... " % (app, tool), end="")
                sys.stdout.flush()
                status, detail = score(tool, app, args)
                print("%-9s %s" % (status, detail))

    print("\n%-22s %-28s %-28s" % ("app", "TestCube feature cov.", "LLMDroid feature cov."))
    print("-" * 80)
    both = 0
    for app in apps:
        cells = []
        for tool in ("testcube", "llmdroid"):
            s = read_score(tool, app)
            cells.append("%6.2f%% (%s+%sp / %s)" % (s["coverage"], s["covered"], s["partial"], s["total"])
                         if s else "          -")
        if all(c.strip() != "-" for c in cells):
            both += 1
        print("%-22s %-28s %-28s" % (app, cells[0], cells[1]))
    print("\n%d app(s) have both tools scored." % both)
    return 0


if __name__ == "__main__":
    sys.exit(main())
