"""Per-run paper metrics derived from a TestCube output folder."""

import json
import os
import statistics

from droidbot.feature_eval.confusion import (
    confusion_rows, extra_journal_features, inference_scores, warn_id_collisions,
)
from droidbot.feature_eval.matcher import DEFAULT_MIN_STEP_CONFIDENCE


def _load_json(path):
    if not path or not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _chain_lengths(features, status="covered"):
    lengths = []
    for item in features or []:
        if status and item.get("status") != status:
            continue
        steps = [step for step in (item.get("steps") or []) if step.get("selector") or step.get("decision") == "act"]
        if steps:
            lengths.append(len(steps))
    return lengths


def _length_stats(values):
    if not values:
        return {"min": 0, "max": 0, "mean": 0.0, "median": 0.0, "n": 0}
    return {
        "min": min(values),
        "max": max(values),
        "mean": round(float(sum(values)) / float(len(values)), 2),
        "median": statistics.median(values),
        "n": len(values),
    }


def _coverage_vs_rank(features):
    ordered = list(features or [])
    points = []
    covered = 0
    for index, item in enumerate(ordered, start=1):
        if item.get("status") == "covered":
            covered += 1
        points.append({
            "k": index,
            "covered": covered,
            "coverage": float(covered) / float(index),
        })
    return points


def _activity_state_counts(results_dir):
    states_dir = os.path.join(results_dir, "states")
    activities = set()
    state_files = 0
    if os.path.isdir(states_dir):
        for name in os.listdir(states_dir):
            if not name.endswith(".json"):
                continue
            state_files += 1
            path = os.path.join(states_dir, name)
            try:
                payload = _load_json(path)
            except Exception:
                payload = None
            if isinstance(payload, dict):
                activity = payload.get("foreground_activity") or payload.get("activity")
                if activity:
                    activities.add(activity)
    return {"unique_activities": len(activities), "state_dumps": state_files}


def write_text_input_sample(report, dest_path, limit=40):
    rows = ((report.get("run_cost") or {}).get("text_inputs") or [])[:limit]
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as handle:
        handle.write("field\tvalue\tsource\tlabel_valid_invalid\n")
        for row in rows:
            handle.write("%s\t%s\t%s\t\n" % (
                str(row.get("field") or "").replace("\t", " "),
                str(row.get("value") or "").replace("\t", " "),
                row.get("source") or "",
            ))
    return dest_path


def _guess_ground_truth(results_dir):
    stem = os.path.basename(os.path.abspath(results_dir).rstrip(os.sep))
    base = stem.split("-")[0]
    cursor = os.path.abspath(results_dir)
    for _ in range(6):
        candidate = os.path.join(cursor, "feature", base, "ground_truth.json")
        if os.path.isfile(candidate):
            return candidate
        cursor = os.path.dirname(cursor)
    return None


def collect_run_metrics(results_dir, ground_truth_path=None):
    results_dir = os.path.abspath(results_dir)
    report = _load_json(os.path.join(results_dir, "feature_test", "report.json")) or {}
    session = _load_json(os.path.join(results_dir, "feature_test", "session.json")) or {}
    features = report.get("features") or session.get("features") or []
    gt = None
    if ground_truth_path:
        gt = _load_json(ground_truth_path)
    if gt is None:
        gt = _load_json(_guess_ground_truth(results_dir))
    gt_features = (gt or {}).get("features") or []
    rows = confusion_rows(gt_features, features, (report.get("offline_coverage") or {}).get("features"))
    extras = extra_journal_features(gt_features, features)
    scores = inference_scores(rows)
    scores["false_positives"] = len(extras)
    if extras:
        denom = scores["true_positives"] + scores["false_positives"]
        scores["precision"] = float(scores["true_positives"]) / float(denom) if denom else 0.0
        prec, rec = scores["precision"], scores["recall"]
        scores["f1"] = (2 * prec * rec / (prec + rec)) if (prec + rec) else 0.0
    extracted_n = len(features or [])
    gt_n = len(gt_features)
    scores["extracted_count"] = extracted_n
    scores["ground_truth_count"] = gt_n
    scores["feature_completeness_ratio"] = (
        round(float(extracted_n) / float(gt_n), 3) if gt_n else None
    )
    collisions, loud = warn_id_collisions(gt_features, features)
    scores["id_collisions"] = collisions
    scores["id_collisions_loud"] = loud
    scores["prf1_withheld"] = bool(loud)

    offline_eval = _load_json(os.path.join(results_dir, "feature_coverage", "report.json")) or {}
    matcher_min = offline_eval.get("matcher_min_confidence")
    if matcher_min is None:
        matcher_min = DEFAULT_MIN_STEP_CONFIDENCE

    lengths = _chain_lengths(features, "covered")
    metrics = {
        "app": report.get("app") or session.get("app"),
        "results_dir": results_dir,
        "online_coverage": report.get("online_coverage") or {
            "covered": report.get("covered"),
            "total": report.get("total_features"),
            "coverage": report.get("coverage"),
        },
        "offline_coverage": report.get("offline_coverage"),
        "feature_inference": scores,
        "confusion": rows,
        "coverage_vs_rank": _coverage_vs_rank(features),
        "action_chain_length_covered": _length_stats(lengths),
        "false_not_present": scores.get("false_not_present"),
        "false_not_present_rate": scores.get("false_not_present_rate"),
        "run_cost": report.get("run_cost") or {},
        "shared_flow_reuses": report.get("shared_flow_reuses") or [],
        "exploration": _activity_state_counts(results_dir),
        "matcher_min_confidence": matcher_min,
    }
    return metrics
