#!/usr/bin/env python
"""Compare code coverage between TestCube runs and LLMDroid runs.

Both tools write a ``codecoverage.txt`` in the same format, so a run folder
from either tool can be passed. TestCube runs additionally carry the series in
``feature_test/report.json``.

    python scripts/compare_coverage.py \
        --testcube output/newpipe-cov1 \
        --llmdroid compare/LLMDroid/LLMDroid-Droidbot/output/newpipe-cov1

Emits a markdown table plus coverage-over-time series for a plot. Runs are only
comparable when they used the same instrumented APK (same tag and denominator);
the script checks this and refuses to print a headline delta when they differ.
"""

import argparse
import json
import os
import re
import sys

SAMPLE_RE = re.compile(
    r"\[(?P<tag>[^\]]+)\]\s+(?P<pct>[\d.]+)%\s+\((?P<hit>\d+)/(?P<total>\d+)\)"
    r"(?:\s+@\s+(?P<elapsed>[\d.]+)s)?"
    r"(?:\s+\|\s+activities\s+(?P<apct>[\d.]+)%\s+\((?P<ahit>\d+)/(?P<atotal>\d+)\))?"
    # LLMDroid ends each sample with its growth rate instead of an elapsed
    # time and never records activities (androlog_monitor.py:105).
    r"(?:\s+-->\s+(?P<rate>[-\d.]+))?"
)
# LLMDroid's jacoco path writes a bare percentage per line.
BARE_RE = re.compile(r"^(?P<pct>[\d.]+)%$")


def read_coverage_file(path):
    """Parse a codecoverage.txt written by either tool."""
    info = {"tag": None, "total": None, "total_activities": None, "samples": []}
    if not os.path.exists(path):
        return None
    with open(path) as handle:
        for line in handle:
            line = line.strip()
            if line.startswith("tag:"):
                info["tag"] = line.split(":", 1)[1].strip()
                continue
            if line.startswith("total methods:"):
                info["total"] = int(line.split(":", 1)[1].strip())
                continue
            if line.startswith("total activities:"):
                info["total_activities"] = int(line.split(":", 1)[1].strip())
                continue
            match = SAMPLE_RE.search(line)
            if match:
                info["tag"] = info["tag"] or match.group("tag")
                info["total"] = info["total"] or int(match.group("total"))
                sample = {
                    "coverage": float(match.group("pct")),
                    "methods_hit": int(match.group("hit")),
                    "elapsed": float(match.group("elapsed") or 0.0),
                }
                if match.group("apct") is not None:
                    sample["activity_coverage"] = float(match.group("apct"))
                    sample["activities_hit"] = int(match.group("ahit"))
                    info["total_activities"] = int(match.group("atotal"))
                info["samples"].append(sample)
                continue
            bare = BARE_RE.match(line)
            if bare:
                info["samples"].append({
                    "coverage": float(bare.group("pct")),
                    "methods_hit": None,
                    "elapsed": None,
                })
    return info if info["samples"] else None


UTG_ACTIVITY_KEYS = ("num_reached_activities", "app_num_total_activities")


def read_utg(run_dir):
    """Activity counts and wall time from utg.js, which both tools emit.

    LLMDroid's AndroLog monitor tracks methods only — it has no activity
    handling at all — so its activity coverage has to come from here. TestCube
    writes utg.js under .droidbot/; LLMDroid writes it at the top level.
    """
    for candidate in (
        os.path.join(run_dir, "utg.js"),
        os.path.join(run_dir, ".droidbot", "utg.js"),
    ):
        if not os.path.exists(candidate):
            continue
        try:
            with open(candidate) as handle:
                text = handle.read()
            data = json.loads(text[text.index("{"):])
        except (ValueError, IOError):
            continue
        reached = data.get("num_reached_activities")
        total = data.get("app_num_total_activities")
        info = {
            "duration": data.get("time_spent"),
            "total_actions": data.get("num_effective_events"),
        }
        if reached is not None and total:
            info.update({
                "activities_hit": reached,
                "total_activities": total,
                "activity_coverage": reached / float(total) * 100.0,
                "activity_source": "utg",
            })
        return info
    return {}


def load_run(run_dir):
    """Read one run folder, preferring the richer TestCube report.json."""
    name = os.path.basename(os.path.normpath(run_dir))
    run = None

    report = os.path.join(run_dir, "feature_test", "report.json")
    if os.path.exists(report):
        try:
            with open(report) as handle:
                data = json.load(handle)
            cov = (data.get("session") or {}).get("code_coverage")
            if cov:
                run = {
                    "name": name,
                    "path": run_dir,
                    "tag": cov.get("tag"),
                    "total": cov.get("total_methods"),
                    "final": cov.get("final_coverage"),
                    "methods_hit": cov.get("methods_hit"),
                    "duration": cov.get("duration"),
                    "total_actions": cov.get("total_actions"),
                    "activity_coverage": cov.get("activity_coverage"),
                    "activities_hit": cov.get("activities_hit"),
                    "total_activities": cov.get("total_activities"),
                    "activity_source": (
                        "androlog" if cov.get("activity_coverage") is not None else None
                    ),
                    "samples": cov.get("samples") or [],
                }
        except (ValueError, IOError):
            run = None

    if run is None:
        parsed = read_coverage_file(os.path.join(run_dir, "codecoverage.txt"))
        if not parsed:
            return None
        last = parsed["samples"][-1]
        run = {
            "name": name,
            "path": run_dir,
            "tag": parsed["tag"],
            "total": parsed["total"],
            "final": last["coverage"],
            "methods_hit": last["methods_hit"],
            "duration": last.get("elapsed"),
            "total_actions": last.get("action_count"),
            "activity_coverage": last.get("activity_coverage"),
            "activities_hit": last.get("activities_hit"),
            "total_activities": parsed.get("total_activities"),
            "activity_source": (
                "androlog" if last.get("activity_coverage") is not None else None
            ),
            "samples": parsed["samples"],
        }

    # LLMDroid's AndroLog monitor records methods only, so its activity
    # coverage and wall time have to come from utg.js. Only fill gaps —
    # a tool's own instrumented numbers always win.
    events_dir = os.path.join(run_dir, "events")
    if run.get("total_actions") is None and os.path.isdir(events_dir):
        run["total_actions"] = len(
            [f for f in os.listdir(events_dir) if f.endswith(".json")]
        )

    for key, value in read_utg(run_dir).items():
        if value is None:
            continue
        current = run.get(key)
        # LLMDroid's samples carry a growth rate, not an elapsed time, so its
        # parsed duration is 0.0 rather than absent — treat that as missing.
        if current is None or (key == "duration" and not current):
            run[key] = value
    return run


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Compare code coverage across tools.")
    parser.add_argument("--testcube", action="append", default=[], help="TestCube run dir (repeatable)")
    parser.add_argument("--llmdroid", action="append", default=[], help="LLMDroid run dir (repeatable)")
    parser.add_argument("--out", default=None, help="Write markdown + json here")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if not args.testcube and not args.llmdroid:
        sys.stderr.write("Pass at least one --testcube or --llmdroid run.\n")
        return 2

    groups = []
    for label, dirs in (("TestCube", args.testcube), ("LLMDroid", args.llmdroid)):
        for run_dir in dirs:
            run = load_run(run_dir)
            if not run:
                sys.stderr.write("[!] no coverage data in %s (skipped)\n" % run_dir)
                continue
            run["tool"] = label
            groups.append(run)

    if not groups:
        sys.stderr.write("No runs with coverage data.\n")
        return 1

    lines = ["# Code coverage comparison", ""]
    lines.append(
        "| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | "
        "Activities | Activity cov. | Duration |"
    )
    lines.append("| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for run in groups:
        act = run.get("activity_coverage")
        marker = "*" if run.get("activity_source") == "utg" else ""
        lines.append("| %s | %s | %s | %s | %s | %s | %.2f%% | %s | %s | %s |" % (
            run["tool"], run["name"], run.get("tag") or "—",
            run.get("total_actions") if run.get("total_actions") is not None else "—",
            run.get("methods_hit") if run.get("methods_hit") is not None else "—",
            run.get("total") or "—",
            run.get("final") or 0.0,
            ("%s/%s" % (run.get("activities_hit"), run.get("total_activities")))
            if run.get("total_activities") else "—",
            ("%.2f%%%s" % (act, marker)) if act is not None else "—",
            ("%.0fs" % run["duration"]) if run.get("duration") is not None else "—",
        ))
    if any(r.get("activity_source") == "utg" for r in groups):
        lines.append("")
        lines.append(
            "\\* activity coverage taken from `utg.js` (screens the explorer reached), "
            "not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks "
            "methods only. The two count slightly differently, so treat a mixed-source "
            "activity comparison as indicative rather than exact."
        )
    lines.append("")

    # A delta is only meaningful against an identical denominator.
    tc = [r for r in groups if r["tool"] == "TestCube"]
    ld = [r for r in groups if r["tool"] == "LLMDroid"]
    if tc and ld:
        totals = {r.get("total") for r in groups if r.get("total")}
        tags = {r.get("tag") for r in groups if r.get("tag")}
        if len(totals) > 1 or len(tags) > 1:
            lines.append(
                "> **Not comparable.** Runs used different instrumentation "
                "(tags %s, denominators %s). Re-run both tools on the same "
                "instrumented APK." % (sorted(tags), sorted(totals))
            )
        else:
            best_tc = max(r["final"] for r in tc)
            best_ld = max(r["final"] for r in ld)
            delta = best_tc - best_ld
            rel = (delta / best_ld * 100.0) if best_ld else float("nan")
            lines.append("**Code coverage — TestCube %.2f%% vs LLMDroid %.2f%%: %+.2f pp (%+.1f%% relative).**"
                         % (best_tc, best_ld, delta, rel))
            act_tc = [r["activity_coverage"] for r in tc if r.get("activity_coverage") is not None]
            act_ld = [r["activity_coverage"] for r in ld if r.get("activity_coverage") is not None]
            if act_tc and act_ld:
                bt, bl = max(act_tc), max(act_ld)
                sources = {r.get("activity_source") for r in tc + ld
                           if r.get("activity_coverage") is not None}
                lines.append("")
                if len(sources) > 1:
                    lines.append(
                        "**Activity coverage — TestCube %.2f%% vs LLMDroid %.2f%% "
                        "(%+.2f pp), but measured differently on each side (%s); "
                        "compare like-for-like before quoting this.**"
                        % (bt, bl, bt - bl, ", ".join(sorted(s for s in sources if s)))
                    )
                else:
                    lines.append("**Activity coverage — TestCube %.2f%% vs LLMDroid %.2f%%: %+.2f pp.**"
                                 % (bt, bl, bt - bl))
        lines.append("")

    # Coverage rises monotonically, so an unequal budget can manufacture a
    # difference. Report whether each run actually saturated: a run that
    # flattened well before its budget was not cut short.
    if tc and ld:
        notes = []
        for run in groups:
            xs = run.get("samples") or []
            if len(xs) < 5:
                continue
            final = xs[-1]["coverage"]
            if not final:
                continue
            idx = next(
                (i for i, smp in enumerate(xs) if smp["coverage"] >= 0.99 * final), None
            )
            if idx is None:
                continue
            notes.append("%s reached 99%% of its final coverage %.0f%% of the way through (%d/%d samples)"
                         % (run["tool"], (idx + 1) / float(len(xs)) * 100, idx + 1, len(xs)))
        if notes:
            lines.append("**Saturation** — " + "; ".join(notes) +
                         ". A run that flattened early was not truncated by its budget.")
            lines.append("")

    markdown = "\n".join(lines)
    print(markdown)

    if args.out:
        os.makedirs(args.out, exist_ok=True)
        with open(os.path.join(args.out, "coverage_comparison.md"), "w") as handle:
            handle.write(markdown + "\n")
        with open(os.path.join(args.out, "coverage_comparison.json"), "w") as handle:
            json.dump(groups, handle, indent=2)
        print("\n[✓] Written to %s" % args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
