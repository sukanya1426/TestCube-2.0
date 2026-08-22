"""Action-centric feature discovery after the hub is reached."""

import logging

from droidbot.GeminiAI import GeminiAi

from .run_stats import STATS


def collect_affordance_labels(events):
    labels = []
    for event in events or []:
        view = getattr(event, "view", None) or {}
        parts = [
            view.get("text"),
            view.get("content_description"),
            (view.get("resource_id") or "").split("/")[-1] if view.get("resource_id") else "",
        ]
        label = " ".join(str(part) for part in parts if part).strip()
        if label and label not in labels:
            labels.append(label[:80])
        if len(labels) >= 40:
            break
    return labels


def infer_missing_features(observed_labels, existing_features, app_name=""):
    logger = logging.getLogger("TestCube.discovery")
    existing = [
        "%s: %s" % (item.get("id"), item.get("name"))
        for item in existing_features or []
    ]
    if GeminiAi.is_disabled():
        logger.info("Hybrid discovery propose-features skipped (LLM disabled).")
        return []
    STATS.record_llm("hybrid_discovery")
    logger.info(
        "Hybrid discovery invoking propose-features LLM (%d observed labels, %d existing features)."
        % (len(observed_labels or []), len(existing))
    )
    prompt = (
        "You are listing extra GUI capabilities of an Android app from observed actions.\n"
        "App: %s\nAlready listed features:\n%s\nObserved on-screen actions:\n%s\n"
        "Propose user-facing features that are NOT already listed. "
        "Each feature is a short necessary action sequence ending in a checkable state. "
        "Do not restate Open/Closed toggles or empty-state copy as features.\n"
        "Return JSON {\"features\":[{\"name\":\"...\",\"actions\":[\"step\",...]}]} "
        "ONLY for capabilities not already listed. Empty list if none. JSON only."
        % (app_name, existing, observed_labels[:40])
    )
    try:
        raw = GeminiAi.generate_content(prompt)
        parsed = GeminiAi._parse_object(raw) or {}
    except Exception as exc:
        logger.info("Hybrid discovery propose-features LLM failed: %s" % exc)
        return []
    if isinstance(parsed, list):
        parsed = {"features": parsed}
    if not isinstance(parsed, dict):
        logger.info("Hybrid discovery proposed 0 features (unparseable LLM output).")
        return []
    added = []
    for item in parsed.get("features") or []:
        if not isinstance(item, dict):
            continue
        name = (item.get("name") or "").strip()
        actions = [str(step) for step in (item.get("actions") or []) if step]
        if not name or not actions:
            logger.info("Hybrid discovery discarded (empty name/actions): %r" % name)
            continue
        logger.info("Hybrid discovery proposed candidate: %s (%d steps)" % (name, len(actions)))
        added.append({
            "name": name,
            "description": item.get("description") or "Inferred from observed UI affordances.",
            "actions": actions,
            "keywords": [],
            "nav_hints": [],
            "source": "action_inferred",
        })
    if not added:
        logger.info("Hybrid discovery proposed 0 candidate features.")
    return added
