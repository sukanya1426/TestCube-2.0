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
