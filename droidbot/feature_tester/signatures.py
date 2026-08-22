"""Normalized widget / action signatures shared by journal, replay, and chain memory."""

import re

from .advisor import _view_text


def widget_selector(event):
    """Stable selector used in replayable test cases."""
    view = getattr(event, "view", None) or {}
    rid = _view_text(view.get("resource_id"))
    selector = {
        "resource_id": rid,
        "text": _view_text(view.get("text")),
        "content_description": _view_text(view.get("content_description")),
        "class": _view_text(view.get("class")),
        "name": getattr(event, "name", None) or "",
        "direction": getattr(event, "direction", None) or "",
    }
    x = getattr(event, "x", None)
    y = getattr(event, "y", None)
    if x not in (None, 0) and y not in (None, 0):
        try:
            selector["x"] = int(x)
            selector["y"] = int(y)
        except (TypeError, ValueError):
            pass
    return selector


def widget_signature(event=None, selector=None):
    """Order-sensitive identity: (type, resource_id, visible label)."""
    selector = selector or (widget_selector(event) if event is not None else {})
    event_type = ""
    if event is not None:
        event_type = (getattr(event, "event_type", "") or event.__class__.__name__).lower()
    rid = _norm(selector.get("resource_id") or "")
    if "/" in rid:
        rid = rid.split("/")[-1]
    label = _norm(selector.get("text") or selector.get("content_description") or "")
    kind = _norm(selector.get("class") or "").split(".")[-1]
    name = _norm(selector.get("name") or "")
    direction = _norm(selector.get("direction") or "")
    return "|".join(part for part in (event_type, rid, label, kind, name, direction) if part)


def step_from_event(event, value=""):
    selector = widget_selector(event)
    action_type = (getattr(event, "event_type", "") or event.__class__.__name__).lower()
    if action_type in ("set_text", "settext", "customsettextevent"):
        action_type = "set_text"
    elif "scroll" in action_type:
        action_type = "scroll"
    elif "key" in action_type or action_type == "key":
        action_type = "key"
    elif "intent" in action_type:
        action_type = "intent"
    else:
        action_type = "touch"
    return {
        "action_type": action_type,
        "selector": selector,
        "value": value or getattr(event, "text", "") or "",
        "signature": widget_signature(event, selector),
    }


def selector_score(event, selector):
    """Higher is a better match of a saved selector onto a live event."""
    if not selector:
        return 0
    live = widget_selector(event)
    score = 0
    want_rid = (selector.get("resource_id") or "").split("/")[-1].lower()
    got_rid = (live.get("resource_id") or "").split("/")[-1].lower()
    if want_rid and want_rid == got_rid:
        score += 8
    for key in ("text", "content_description"):
        want = _norm(selector.get(key) or "")
        got = _norm(live.get(key) or "")
        if want and want == got:
            score += 6
        elif want and want in got:
            score += 3
    want_cls = _norm(selector.get("class") or "").split(".")[-1]
    got_cls = _norm(live.get("class") or "").split(".")[-1]
    if want_cls and want_cls == got_cls:
        score += 1
    if selector.get("name") and (getattr(event, "name", "") or "") == selector.get("name"):
        score += 8
    if selector.get("direction") and (getattr(event, "direction", "") or "") == selector.get("direction"):
        score += 4
    return score


def pick_event(events, selector, action_type=""):
    best = None
    for event in events or []:
        event_type = (getattr(event, "event_type", "") or "").lower()
        if action_type == "set_text" and "set_text" not in event_type and "settext" not in event.__class__.__name__.lower():
            continue
        if action_type == "scroll" and "scroll" not in event_type and "scroll" not in event.__class__.__name__.lower():
            continue
        if action_type == "key" and (getattr(event, "name", "") or "") != (selector.get("name") or "BACK"):
            if getattr(event, "name", "") or "":
                pass
            elif "key" not in event_type:
                continue
        score = selector_score(event, selector)
        if best is None or score > best[0]:
            best = (score, event)
    if best and best[0] >= 3:
        return best[1]
    return None


def _norm(text):
    return re.sub(r"\s+", " ", (text or "").strip().lower())
