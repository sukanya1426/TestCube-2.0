"""Compare live journal labels with ground-truth + offline matcher results.

Live README extraction and hand-authored ground_truth.json often reuse
F001/F002/… for *different* features. Name/description similarity is the
primary key; ID is only a tiebreaker.
"""

import re
import sys


NAME_SIM_FLOOR = 0.3
ID_COLLISION_FRACTION = 0.5


def _tokens(text):
    return set(re.findall(r"[a-z0-9]{3,}", (text or "").lower()))


def feature_blob_tokens(item):
    parts = [
        (item or {}).get("name"),
        (item or {}).get("description"),
    ]
    parts.extend((item or {}).get("keywords") or [])
    return _tokens(" ".join(str(part) for part in parts if part))


def name_similarity(left, right):
    """Jaccard over names, then over name+description+keywords; take the max.

    Descriptions often dilute short, clearly-related names (e.g. "Search for
    Music" vs "Search for a song").
    """
    scores = []
    name_a = _tokens((left or {}).get("name"))
    name_b = _tokens((right or {}).get("name"))
    if name_a and name_b:
        scores.append(float(len(name_a & name_b)) / float(len(name_a | name_b)))
    blob_a = feature_blob_tokens(left)
    blob_b = feature_blob_tokens(right)
    if blob_a and blob_b:
        scores.append(float(len(blob_a & blob_b)) / float(len(blob_a | blob_b)))
    return max(scores) if scores else 0.0


def _best_journal_match(gt_item, journal_features, min_sim=NAME_SIM_FLOOR):
    """Return (journal_item_or_None, similarity). Never match on ID alone."""
    ranked = []
    for item in journal_features or []:
        sim = name_similarity(gt_item, item)
        ranked.append((sim, item))
    if not ranked:
        return None, 0.0
    ranked.sort(key=lambda row: row[0], reverse=True)
    best_sim, best = ranked[0]
    if best_sim < min_sim:
        return None, best_sim
    ties = [item for sim, item in ranked if abs(sim - best_sim) < 1e-9]
    gt_id = (gt_item or {}).get("id")
    if gt_id and len(ties) > 1:
        for item in ties:
            if item.get("id") == gt_id:
                return item, best_sim
    return best, best_sim


def colliding_id_pairs(ground_truth_features, journal_features, min_sim=NAME_SIM_FLOOR):
    """ID-aligned pairs whose names are semantically unrelated."""
    journal_by_id = {item.get("id"): item for item in journal_features or []}
    collisions = []
    for gt in ground_truth_features or []:
        other = journal_by_id.get(gt.get("id"))
        if not other:
            continue
        sim = name_similarity(gt, other)
        if sim < min_sim:
            collisions.append({
                "id": gt.get("id"),
                "ground_truth_name": gt.get("name"),
                "journal_name": other.get("name"),
                "name_similarity": round(sim, 3),
            })
    return collisions


def warn_id_collisions(ground_truth_features, journal_features, min_sim=NAME_SIM_FLOOR):
    journal_by_id = {item.get("id") for item in journal_features or [] if item.get("id")}
    id_aligned = [
        item for item in ground_truth_features or []
        if item.get("id") in journal_by_id
    ]
    collisions = colliding_id_pairs(ground_truth_features, journal_features, min_sim=min_sim)
    if not id_aligned:
        return collisions, False
    fraction = float(len(collisions)) / float(len(id_aligned))
    loud = fraction >= ID_COLLISION_FRACTION and len(collisions) >= 1
    if loud:
        sys.stderr.write(
            "WARNING: ground truth and live feature list appear to use colliding "
            "IDs for different features — results would be unreliable if matched "
            "by ID. %d/%d ID-aligned pairs have name similarity < %.2f.\n"
            % (len(collisions), len(id_aligned), min_sim)
        )
        for row in collisions[:8]:
            sys.stderr.write(
                "  %s: GT %r vs live %r (sim=%.2f)\n"
                % (row["id"], row["ground_truth_name"], row["journal_name"], row["name_similarity"])
            )
    return collisions, loud


def confusion_rows(ground_truth_features, journal_features, offline_results=None):
    warn_id_collisions(ground_truth_features, journal_features)
    offline_by_id = {}
    offline_list = list(offline_results or [])
    for item in offline_list:
        offline_by_id[item.get("id")] = item
    rows = []
    used_journal = set()
    for gt in ground_truth_features or []:
        journal, sim = _best_journal_match(gt, journal_features)
        if journal and journal.get("id") in used_journal:
            # Prefer not to double-assign a live feature; try next-best later.
            alt = None
            alt_sim = 0.0
            for item in journal_features or []:
                if item.get("id") in used_journal:
                    continue
                score = name_similarity(gt, item)
                if score >= NAME_SIM_FLOOR and score > alt_sim:
                    alt, alt_sim = item, score
            journal, sim = (alt, alt_sim) if alt else (None, sim)
        if journal and journal.get("id"):
            used_journal.add(journal.get("id"))
        offline = offline_by_id.get(gt.get("id")) or {}
        if not offline and journal:
            # Offline results are keyed by GT id; name-match if needed.
            for item in offline_list:
                if name_similarity(gt, item) >= NAME_SIM_FLOOR:
                    offline = item
                    break
        journal_status = (journal or {}).get("status") or "missing"
        rows.append({
            "ground_truth_id": gt.get("id"),
            "ground_truth_name": gt.get("name"),
            "journal_id": (journal or {}).get("id"),
            "journal_name": (journal or {}).get("name"),
            "name_similarity": round(sim, 3),
            "matched_by": "name" if journal else "none",
            "journal_status": journal_status,
            "offline_status": offline.get("status"),
            "exists_in_gt": True,
            "predicted_not_present": journal_status == "not_present",
            "false_not_present": journal_status == "not_present",
        })
    return rows


def inference_scores(rows):
    """Precision/recall of feature *extraction* vs ground truth.

    A GT feature is a true positive if a *semantically matched* journal
    feature exists and is not 'not_present'. Unmatched GT features are
    false negatives (the live extractor missed them). Extra journal
    features are counted separately via extra_journal_features.
    """
    tp = sum(
        1 for row in rows
        if row.get("journal_id")
        and row.get("journal_status") not in ("not_present", "missing", None)
    )
    fn = sum(
        1 for row in rows
        if not row.get("journal_id") or row.get("journal_status") in ("not_present", "missing", None)
    )
    fp = 0
    precision = float(tp) / float(tp + fp) if (tp + fp) else 0.0
    recall = float(tp) / float(tp + fn) if (tp + fn) else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
    false_not_present = sum(1 for row in rows if row.get("false_not_present"))
    return {
        "true_positives": tp,
        "false_negatives": fn,
        "false_positives": fp,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "false_not_present": false_not_present,
        "false_not_present_rate": (float(false_not_present) / float(len(rows))) if rows else 0.0,
    }


def extra_journal_features(ground_truth_features, journal_features):
    matched = set()
    for gt in ground_truth_features or []:
        journal, _sim = _best_journal_match(gt, journal_features)
        if journal and journal.get("id"):
            matched.add(journal.get("id"))
    extras = []
    for item in journal_features or []:
        if item.get("id") in matched:
            continue
        extras.append(item.get("id"))
    return extras
