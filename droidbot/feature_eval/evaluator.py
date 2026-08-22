"""Orchestrate post-run feature coverage evaluation."""

import os

from .coverage import CoverageCalculator
from .feature_loader import FeatureLoader
from .llm_matcher import LLMMatcher
from .matcher import FeatureMatcher
from .report import ReportGenerator
from .trace_loader import TraceLoader


def evaluate_feature_coverage(results_dir, features_path, readme_path=None,
                              output_dir=None, use_llm=True, journal_features=None,
                              min_confidence=None, matcher_mode=None):
    """Evaluate feature coverage for an existing TestCube run.

    Parameters
    ----------
    results_dir : str
        TestCube output directory (contains events/, states/, utg.js).
    features_path : str
        Manually prepared ground-truth features.json.
    readme_path : str, optional
        Application README used only as LLM context.
    output_dir : str, optional
        Defaults to <results_dir>/feature_coverage.
    use_llm : bool
        If True (default), VLM/Gemini is the coverage judge. Token overlap
        is ablation-only (``matcher_mode=deterministic`` or ``hybrid``).
        The ``ai`` path does not fall back to string matching.
    matcher_mode : str, optional
        ``ai`` (default), ``deterministic``, or ``hybrid`` (old string-first
        behavior, kept for ablation).
    """
    loaded = FeatureLoader().load(features_path)
    trace = TraceLoader().load(results_dir)
    readme_text = ""
    if readme_path:
        if not os.path.isfile(readme_path):
            raise ValueError("README not found: %s" % readme_path)
        with open(readme_path, "r", encoding="utf-8") as handle:
            readme_text = handle.read()
    if not readme_text:
        sibling = os.path.join(os.path.dirname(features_path), "README.md")
        if os.path.isfile(sibling):
            with open(sibling, "r", encoding="utf-8") as handle:
                readme_text = handle.read()

    from .matcher import DEFAULT_MIN_STEP_CONFIDENCE
    if min_confidence is None:
        min_confidence = DEFAULT_MIN_STEP_CONFIDENCE
    if matcher_mode is None:
        matcher_mode = "ai" if use_llm else "deterministic"
    journal = _load_journal_features(results_dir, journal_features)
    bank = _load_exploration_bank(results_dir)
    if journal and bank:
        try:
            from droidbot.feature_tester.journal import apply_bank_credit
            apply_bank_credit(journal, bank)
        except Exception:
            pass
    llm_matcher = None
    if matcher_mode in ("ai", "hybrid"):
        llm_matcher = LLMMatcher(
            enabled=True,
            journal_features=journal,
            exploration_bank=bank,
        )
    matcher = FeatureMatcher(
        use_llm=matcher_mode != "deterministic",
        llm_matcher=llm_matcher,
        readme_text=readme_text,
        min_step_confidence=min_confidence,
        matcher_mode=matcher_mode,
    )
    print(
        "Coverage judge: scoring %d features in LLM batches" % len(loaded["features"]),
        flush=True,
    )
    results = matcher.match_all(loaded["features"], trace)
    _apply_journal_completion_ratios(results, loaded["features"], journal)

    application = loaded.get("app") or trace.app_name or "unknown"
    report = CoverageCalculator().calculate(
        application=application,
        feature_results=results,
        results_dir=results_dir,
        readme_path=readme_path,
        features_path=features_path,
    )
    report.matcher_min_confidence = float(min_confidence)
    report.matcher_mode = matcher_mode
    _attach_confusion(report, loaded["features"], results_dir, journal_features)
    try:
        from droidbot.feature_tester.guide import classify_ground_truth_source
        session_path = os.path.join(results_dir, "feature_test", "session.json")
        guide_path = None
        if os.path.isfile(session_path):
            import json
            with open(session_path, encoding="utf-8") as handle:
                session = json.load(handle)
            guide_path = session.get("guide_features_path")
        report.ground_truth_source = classify_ground_truth_source(guide_path, features_path)
    except Exception:
        report.ground_truth_source = None

    if output_dir is None:
        output_dir = os.path.join(results_dir, "feature_coverage")
    paths = ReportGenerator().write(report, output_dir)
    return report, paths


def _apply_journal_completion_ratios(results, features, journal):
    from .models import STATUS_COVERED
    by_name = {}
    for item in journal or []:
        key = (item.get("name") or "").strip().lower()
        if key:
            by_name[key] = item
        fid = item.get("id")
        if fid:
            by_name[str(fid).lower()] = item
    for result, feature in zip(results, features or []):
        item = by_name.get((feature.name or "").strip().lower()) or by_name.get(
            (feature.id or "").lower()
        )
        if item and item.get("status") == "covered" and item.get("completion_source") == "cross_feature":
            result.status = STATUS_COVERED
            result.completion_ratio = 1.0
            extra = "Completed by later features: %s" % (
                ", ".join(item.get("credited_from") or []) or "exploration bank"
            )
            if extra not in (result.evidence or []):
                result.evidence = list(result.evidence or []) + [extra]
            continue
        if result.status == STATUS_COVERED:
            result.completion_ratio = 1.0
            continue
        if result.completion_ratio is not None:
            continue
        if result.status == "partial":
            gold = feature.paths()[0] if feature.paths() else []
            matched = result.matched_path or []
            if gold:
                result.completion_ratio = min(1.0, float(len(matched)) / float(len(gold)))
            else:
                result.completion_ratio = 0.5
        else:
            result.completion_ratio = 0.0


def _load_journal_features(results_dir, journal_features):
    if journal_features:
        return journal_features
    path = os.path.join(results_dir, "feature_test", "report.json")
    if not os.path.isfile(path):
        path = os.path.join(results_dir, "feature_test", "session.json")
    if not os.path.isfile(path):
        return []
    import json
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return payload.get("features") or []


def _load_exploration_bank(results_dir):
    path = os.path.join(results_dir, "feature_test", "session.json")
    if not os.path.isfile(path):
        path = os.path.join(results_dir, "feature_test", "report.json")
    if not os.path.isfile(path):
        return []
    import json
    try:
        with open(path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except Exception:
        return []
    return payload.get("exploration_bank") or []


def _attach_confusion(report, ground_truth_features, results_dir, journal_features):
    try:
        from .confusion import confusion_rows, extra_journal_features, inference_scores
    except Exception:
        return
    gt_dicts = []
    for item in ground_truth_features or []:
        if hasattr(item, "id"):
            gt_dicts.append({
                "id": item.id,
                "name": item.name,
                "description": getattr(item, "description", "") or "",
                "keywords": list(getattr(item, "keywords", None) or []),
            })
        else:
            gt_dicts.append(item)
    journal = _load_journal_features(results_dir, journal_features)
    offline = [
        {"id": item.id, "name": item.name, "status": item.status}
        for item in (report.features or [])
    ]
    rows = confusion_rows(gt_dicts, journal, offline)
    extras = extra_journal_features(gt_dicts, journal)
    scores = inference_scores(rows)
    scores["false_positives"] = len(extras)
    if extras:
        denom = scores["true_positives"] + scores["false_positives"]
        scores["precision"] = float(scores["true_positives"]) / float(denom) if denom else 0.0
        prec, rec = scores["precision"], scores["recall"]
        scores["f1"] = (2 * prec * rec / (prec + rec)) if (prec + rec) else 0.0
    extracted_n = len(journal or [])
    gt_n = len(gt_dicts)
    scores["extracted_count"] = extracted_n
    scores["ground_truth_count"] = gt_n
    scores["feature_completeness_ratio"] = (
        round(float(extracted_n) / float(gt_n), 3) if gt_n else None
    )
    from .confusion import warn_id_collisions
    collisions, loud = warn_id_collisions(gt_dicts, journal)
    scores["id_collisions"] = collisions
    scores["id_collisions_loud"] = loud
    scores["prf1_withheld"] = bool(loud)
    report.confusion = rows
    report.feature_inference = scores

