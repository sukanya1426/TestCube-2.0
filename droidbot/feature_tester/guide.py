"""Human-authored guide lists vs README extraction vs ground-truth scoring."""

import json
import os

from .specs import apk_stem, is_eval_only_feature_list


def discover_guide_features(apk_path=None, cwd=None):
    stem = apk_stem(apk_path)
    if not stem:
        return None
    path = os.path.join(cwd or os.getcwd(), "feature", stem, "guide_features.json")
    if os.path.isfile(path):
        return os.path.abspath(path)
    return None


def discover_ground_truth_addendum(apk_path=None, cwd=None):
    stem = apk_stem(apk_path)
    if not stem:
        return None
    path = os.path.join(cwd or os.getcwd(), "feature", stem, "ground_truth_addendum.json")
    if os.path.isfile(path):
        return os.path.abspath(path)
    return None


def load_feature_json(path):
    if not path or not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict) or not payload.get("features"):
        return None
    return payload


def _names(payload):
    return [
        (item.get("name") or "").strip()
        for item in (payload or {}).get("features") or []
        if (item.get("name") or "").strip()
    ]


def diff_feature_lists(guide_payload, readme_payload, min_sim=0.3):
    """Classify features as guide-only, readme-only, or in both (by name similarity)."""
    from droidbot.feature_eval.confusion import name_similarity

    guide_items = list((guide_payload or {}).get("features") or [])
    readme_items = list((readme_payload or {}).get("features") or [])
    used_readme = set()
    both = []
    guide_only = []
    for gitem in guide_items:
        best, best_sim, best_idx = None, 0.0, None
        for index, ritem in enumerate(readme_items):
            if index in used_readme:
                continue
            sim = name_similarity(gitem, ritem)
            if sim > best_sim:
                best, best_sim, best_idx = ritem, sim, index
        if best is not None and best_sim >= min_sim:
            used_readme.add(best_idx)
            both.append({
                "guide_id": gitem.get("id"),
                "guide_name": gitem.get("name"),
                "readme_id": best.get("id"),
                "readme_name": best.get("name"),
                "name_similarity": round(best_sim, 3),
            })
        else:
            guide_only.append({
                "id": gitem.get("id"),
                "name": gitem.get("name"),
            })
    readme_only = [
        {"id": item.get("id"), "name": item.get("name")}
        for index, item in enumerate(readme_items)
        if index not in used_readme
    ]
    return {
        "guide_count": len(guide_items),
        "readme_count": len(readme_items),
        "both": both,
        "guide_only": guide_only,
        "readme_only": readme_only,
    }


def classify_ground_truth_source(guide_path, ground_truth_path):
    """same_as_guide_list vs independent_labeled_set."""
    if not ground_truth_path or not os.path.isfile(ground_truth_path):
        return None
    if not guide_path or not os.path.isfile(guide_path):
        return "independent_labeled_set"
    try:
        if os.path.samefile(guide_path, ground_truth_path):
            return "same_as_guide_list"
    except OSError:
        pass
    if os.path.abspath(guide_path) == os.path.abspath(ground_truth_path):
        return "same_as_guide_list"
    guide = load_feature_json(guide_path)
    truth = load_feature_json(ground_truth_path)
    guide_names = set(name.lower() for name in _names(guide))
    truth_names = set(name.lower() for name in _names(truth))
    if guide_names and guide_names == truth_names:
        return "same_as_guide_list"
    return "independent_labeled_set"


def mark_source(payload, source):
    if not payload:
        return payload
    for item in payload.get("features") or []:
        item.setdefault("source", source)
    payload["feature_source"] = source
    return payload


def is_live_override_json(path):
    """True when -features is a real exploration list, not a gold JSON."""
    if not path or not os.path.isfile(path):
        return False
    return not is_eval_only_feature_list(path)
