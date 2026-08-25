"""Flag and optionally split coarse README features that bundle several outcomes."""

import logging
import re

from droidbot.GeminiAI import GeminiAi


LOGGER = logging.getLogger("TestCube.granularity")
MAX_ACTIONS = 6
OUTCOME_VERBS = (
    "adjust", "change", "toggle", "enable", "disable", "set", "save",
    "create", "delete", "share", "download", "play", "pause", "shuffle",
    "repeat", "search", "login", "skip", "blacklist", "equalizer",
)


FEATURE_DEFINITION = (
    "A feature is a finite ordered sequence of user operations where "
    "(a) each operation is necessary — removing it changes or breaks the outcome, "
    "and (b) the sequence ends in a visibly different, checkable app state. "
    "Do not bundle multiple distinct outcomes or toggles into one feature "
    "just because they live on the same screen."
)


def _outcome_verb_count(text):
    blob = (text or "").lower()
    found = [verb for verb in OUTCOME_VERBS if re.search(r"\b%s\b" % re.escape(verb), blob)]
    return len(found)


def looks_coarse(item):
    actions = list(item.get("actions") or [])
    blob = "%s %s %s" % (
        item.get("name") or "",
        item.get("description") or "",
        " ".join(str(step) for step in actions),
    )
    if len(actions) > MAX_ACTIONS:
        return True
    if _outcome_verb_count(blob) >= 3 and (
        " and " in blob.lower() or " & " in blob or "," in (item.get("name") or "")
    ):
        return True
    return False


def _reindex(features):
    for index, item in enumerate(features or [], start=1):
        item["id"] = "F%03d" % index
    return features


def try_llm_split(item, app_name=""):
    if GeminiAi.is_disabled():
        return None
    prompt = (
        "%s\n"
        "Split this bundled GUI feature into separate features, one outcome each.\n"
        "App: %s\nName: %s\nDescription: %s\nActions: %s\n"
        "Return JSON {\"features\":[{\"name\":\"...\",\"actions\":[\"step\",...]}]}. "
        "If it is already one outcome, return a one-item list. JSON only."
        % (
            FEATURE_DEFINITION,
            app_name,
            item.get("name"),
            item.get("description") or "",
            item.get("actions") or [],
        )
    )
    try:
        raw = GeminiAi.generate_content(prompt)
        parsed = GeminiAi._parse_object(raw) or {}
    except Exception as exc:
        LOGGER.info("Granularity split LLM failed for %s: %s" % (item.get("name"), exc))
        return None
    if isinstance(parsed, list):
        parsed = {"features": parsed}
    out = []
    for child in parsed.get("features") or []:
        if not isinstance(child, dict):
            continue
        name = (child.get("name") or "").strip()
        actions = [str(step) for step in (child.get("actions") or []) if step]
        if not name or not actions:
            continue
        record = dict(item)
        record["name"] = name
        record["description"] = child.get("description") or item.get("description") or ""
        record["actions"] = actions
        record["granularity_flag"] = "split"
        out.append(record)
    if len(out) <= 1:
        return None
    return out


MIN_ACTIONS = 3
ENRICH_TARGET = 6


def looks_thin(item):
    """A feature whose step list is too shallow to steer exploration.

    A one-line guide action ("Add a transaction") is satisfied by a single
    tap, so the feature is marked covered after one action while the gold
    list expects four to nine concrete steps.
    """
    return len(item.get("actions") or []) < MIN_ACTIONS


def try_llm_expand(item, app_name="", readme_text=""):
    """Expand one thin feature into concrete GUI steps.

    Reads only the guide entry and the app README. It must never read the
    gold list -- that stays eval-only (docs/PROJECT.md).
    """
    if GeminiAi.is_disabled():
        return None
    context = (readme_text or "").strip()
    if len(context) > 1200:
        context = context[:1200]
    prompt = (
        "%s\n"
        "Expand this app feature into the concrete GUI steps a user performs.\n"
        "App: %s\nName: %s\nDescription: %s\nKnown steps: %s\nNavigation hints: %s\n"
        "App README (context only):\n%s\n\n"
        "Write %d to %d steps. Each step is one observable UI action, phrased as "
        "an imperative starting with a verb (Tap/Enter/Select/Open/Scroll). "
        "Do not invent capabilities the app does not have. "
        "Return JSON {\"actions\":[\"step\",...]}. JSON only."
        % (
            FEATURE_DEFINITION,
            app_name,
            item.get("name"),
            item.get("description") or "",
            item.get("actions") or [],
            item.get("nav_hints") or [],
            context or "(none)",
            MIN_ACTIONS,
            ENRICH_TARGET,
        )
    )
    try:
        raw = GeminiAi.generate_content(prompt)
        parsed = GeminiAi._parse_object(raw) or {}
    except Exception as exc:
        LOGGER.info("Granularity expand LLM failed for %s: %s" % (item.get("name"), exc))
        return None
    if isinstance(parsed, list):
        parsed = {"actions": parsed}
    actions = [
        " ".join(str(step).split())
        for step in (parsed.get("actions") or [])
        if step and str(step).strip()
    ]
    actions = [step for step in actions if len(step) > 2][:ENRICH_TARGET]
    if len(actions) < MIN_ACTIONS:
        return None
    return actions


def enrich_thin_features(payload, app_name="", readme_text=""):
    """Deepen guide features that carry too few steps to steer exploration."""
    if not payload or not payload.get("features"):
        return payload
    enriched_names = []
    out = []
    for item in payload["features"]:
        if not looks_thin(item):
            out.append(item)
            continue
        actions = try_llm_expand(
            item, app_name=app_name or payload.get("app") or "", readme_text=readme_text
        )
        if not actions:
            out.append(item)
            continue
        item = dict(item)
        item["original_actions"] = list(item.get("actions") or [])
        item["actions"] = actions
        item["granularity_flag"] = "auto_enriched"
        enriched_names.append(item.get("name"))
        out.append(item)
    if not enriched_names:
        return payload
    LOGGER.info("Auto-enriched %d thin guide features." % len(enriched_names))
    payload = dict(payload)
    payload["features"] = out
    payload["enriched_features"] = enriched_names
    return payload


def refine_granularity(payload, app_name=""):
    """Flag coarse features; try an LLM split; otherwise keep and mark for review."""
    if not payload or not payload.get("features"):
        return payload
    flags = []
    kept = []
    for item in payload["features"]:
        if not looks_coarse(item):
            kept.append(item)
            continue
        name = item.get("name") or ""
        flags.append(name)
        LOGGER.info("Granularity flag (candidate for split): %s (%d actions)" % (
            name, len(item.get("actions") or []),
        ))
        split = try_llm_split(item, app_name=app_name or payload.get("app") or "")
        if split:
            LOGGER.info("Granularity auto-split %r into %d features." % (name, len(split)))
            kept.extend(split)
        else:
            item = dict(item)
            item["granularity_flag"] = "needs_split"
            kept.append(item)
    payload = dict(payload)
    payload["features"] = _reindex(kept)
    payload["granularity_flags"] = flags
    return payload
