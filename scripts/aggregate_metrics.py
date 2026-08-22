#!/usr/bin/env python
"""Aggregate TestCube run folders into metrics.json + metrics.md for a paper table."""

import argparse
import json
import os
import sys


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Aggregate TestCube feature-test metrics.")
    parser.add_argument(
        "runs",
        nargs="+",
        help="One or more -o output directories (output/spotube-5, output/money-4, …)",
    )
    parser.add_argument(
        "--out",
        default="output/metrics",
        help="Directory for metrics.json and metrics.md",
    )
    parser.add_argument(
        "--ground-truth",
        action="append",
        default=[],
        help="Optional ground_truth.json (repeatable, matched by order to runs)",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    from droidbot.feature_eval.metrics_collect import collect_run_metrics, write_text_input_sample

    rows = []
    missing = [run for run in args.runs if not os.path.isdir(run)]
    if missing:
        sys.stderr.write(
            "Run folder not found: %s\n"
            "Use the -o directory from the droidbot command "
            "(this repo defaults to output/spotube and output/money).\n"
            % ", ".join(missing)
        )
        return 2
    for index, run in enumerate(args.runs):
        gt = args.ground_truth[index] if index < len(args.ground_truth) else None
        metrics = collect_run_metrics(run, ground_truth_path=gt)
        sample = os.path.join(args.out, "%s_text_inputs.tsv" % (metrics.get("app") or "app"))
        report = {}
        report_path = os.path.join(run, "feature_test", "report.json")
        if os.path.isfile(report_path):
            with open(report_path, encoding="utf-8") as handle:
                report = json.load(handle)
        write_text_input_sample(report, sample)
        metrics["text_input_sample"] = sample
        rows.append(metrics)

    os.makedirs(args.out, exist_ok=True)
    json_path = os.path.join(args.out, "metrics.json")
    md_path = os.path.join(args.out, "metrics.md")
    with open(json_path, "w", encoding="utf-8") as handle:
        json.dump({"runs": rows}, handle, indent=2)
        handle.write("\n")
    with open(md_path, "w", encoding="utf-8") as handle:
        handle.write(_render_markdown(rows))
    sys.stdout.write("Wrote %s\n" % json_path)
    sys.stdout.write("Wrote %s\n" % md_path)
    return 0


def _pct(value):
    try:
        return "%.1f%%" % (100.0 * float(value or 0.0))
    except (TypeError, ValueError):
        return "—"


def _render_markdown(rows):
    lines = [
        "# TestCube aggregated metrics",
        "",
        "| App | Online cov. | Offline cov. | Extracted/GT | Completeness | False not_present | Chain len (mean) | LLM calls | Wall s | Shared-flow skips | Activities |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        online = row.get("online_coverage") or {}
        offline = row.get("offline_coverage") or {}
        inf = row.get("feature_inference") or {}
        cost = row.get("run_cost") or {}
        skips = sum(item.get("actions_skipped") or 0 for item in (row.get("shared_flow_reuses") or []))
        chain = row.get("action_chain_length_covered") or {}
        expl = row.get("exploration") or {}
        extracted = inf.get("extracted_count")
        gt_n = inf.get("ground_truth_count")
        ratio = inf.get("feature_completeness_ratio")
        completeness = "—" if ratio is None else "%.2f" % ratio
        extracted_gt = "—" if gt_n in (None, 0) else "%s/%s" % (extracted, gt_n)
        lines.append(
            "| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |"
            % (
                row.get("app") or "?",
                _pct(online.get("coverage")),
                _pct(offline.get("coverage") if isinstance(offline, dict) else None),
                extracted_gt,
                completeness,
                inf.get("false_not_present") or 0,
                chain.get("mean") or 0,
                cost.get("llm_calls_total") or 0,
                cost.get("wall_clock_seconds") or 0,
                skips,
                expl.get("unique_activities") or 0,
            )
        )
    thresholds = sorted({
        row.get("matcher_min_confidence") for row in rows
        if row.get("matcher_min_confidence") is not None
    })
    threshold_text = ", ".join("%.2f" % value for value in thresholds) if thresholds else "0.50"
    lines.extend(["", "Online coverage is the live journal (covered / extracted features).",
                  "Offline coverage is feature_eval vs ground-truth JSON when present.",
                  "Matcher min-confidence threshold: %s "
                  "(deterministic ablation only; LLM coverage keeps PARTIAL "
                  "and does not require gold step order)."
                  % threshold_text,
                  "Feature completeness ratio is extracted (live) feature count / ground-truth count.",
                  "P/R/F1 is withheld from this table when live and ground-truth IDs collide; "
                  "matching is by name similarity. Do not cite P/R/F1 until a re-run confirms it.",
                  "Text field samples for human validity labels are written as `*_text_inputs.tsv`.",
                  ""])
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
