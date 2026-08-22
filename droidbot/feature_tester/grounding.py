"""Detect unlabeled Flutter-style screens and ground taps from a screenshot."""

import json
import logging
import os


LOGGER = logging.getLogger("TestCube.grounding")
LOW_SIGNAL_RATIO = 0.8
DESTINATION_WORDS = (
    "search", "settings", "plugin", "library", "playlist",
    "lyrics", "download", "equalizer",
)


def _view_text(value):
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return " ".join(_view_text(item) for item in value if item not in (None, "")).strip()
    return str(value)


def visible_label(event):
    """Widget text/content-desc/id — not inferred bottom-nav names."""
    name = (getattr(event, "name", "") or "")
    if (name or "").upper() == "BACK" or getattr(event, "event_type", "") == "key":
        return name or "KEY"
    view = getattr(event, "view", None) or {}
    rid = _view_text(view.get("resource_id"))
    parts = [
        _view_text(view.get("text")),
        _view_text(view.get("content_description")),
        rid.split("/")[-1] if rid else "",
    ]
    return " ".join(str(part) for part in parts if part)


def is_set_text(event):
    return getattr(event, "event_type", "") == "set_text" or event.__class__.__name__ == "SetTextEvent"


def is_bottom_nav(event):
    extra = (getattr(event, "nav_label", None) or "").lower()
    return "bottom navigation" in extra or "nav tab" in extra


def _is_back(event):
    name = (getattr(event, "name", "") or "").upper()
    return name == "BACK" or getattr(event, "event_type", "") == "key"


def widget_has_signal(event):
    if is_set_text(event):
        return True
    visible = visible_label(event).strip()
    if visible:
        return True
    view = getattr(event, "view", None) or {}
    rid = (view.get("resource_id") or "").split("/")[-1]
    if rid and rid not in ("content", "action_bar_root"):
        return True
    return False


def actionable_events(events):
    kept = []
    for event in events or []:
        if _is_back(event):
            continue
        etype = (getattr(event, "event_type", "") or "").lower()
        if etype == "scroll":
            continue
        kept.append(event)
    return kept


def screen_signal(events):
    scope = actionable_events(events)
    if not scope:
        return {
            "low_signal": False,
            "ratio": 0.0,
            "unlabeled": 0,
            "total": 0,
            "unlabeled_nav": 0,
        }
    unlabeled = [event for event in scope if not widget_has_signal(event)]
    unlabeled_nav = [event for event in unlabeled if is_bottom_nav(event)]
    ratio = float(len(unlabeled)) / float(len(scope))
    low = ratio >= LOW_SIGNAL_RATIO or len(unlabeled_nav) >= 3
    return {
        "low_signal": low,
        "ratio": round(ratio, 3),
        "unlabeled": len(unlabeled),
        "total": len(scope),
        "unlabeled_nav": len(unlabeled_nav),
    }


def destination_missing(feature, events):
    """True when remaining steps name a dest that no visible widget shows."""
    blob = " ".join(
        [(feature or {}).get("name") or "", (feature or {}).get("description") or ""]
        + list((feature or {}).get("remaining_actions") or [])
        + list((feature or {}).get("nav_hints") or [])
    ).lower()
    labels = " ".join(visible_label(event).lower() for event in events or [])
    needed = [dest for dest in DESTINATION_WORDS if dest in blob]
    if not needed:
        return False
    return not any(dest in labels for dest in needed)


def needs_visual_ground(feature, events):
    signal = screen_signal(events)
    missing = destination_missing(feature, events)
    force = bool(signal["low_signal"] or (missing and signal["unlabeled_nav"] >= 2))
    signal["destination_missing"] = missing
    signal["force_visual"] = force
    return force, signal


def screen_size(state):
    width, height = 0, 0
    for view in getattr(state, "views", None) or []:
        bounds = view.get("bounds") or [[0, 0], [0, 0]]
        try:
            width = max(width, bounds[1][0])
            height = max(height, bounds[1][1])
        except (TypeError, IndexError):
            continue
    return width or 1080, height or 1920


def dump_low_signal_state(journal, state, signal):
    if journal is None or state is None:
        return None
    folder = os.path.join(journal.root, "low_signal_states")
    try:
        os.makedirs(folder, exist_ok=True)
    except Exception:
        return None
    state_str = getattr(state, "state_str", "") or "unknown"
    path = os.path.join(folder, "state_%s.json" % state_str[:16])
    if os.path.isfile(path):
        return path
    clickable = []
    for view in getattr(state, "views", None) or []:
        if not view.get("clickable") and not view.get("editable"):
            continue
        clickable.append({
            "class": (view.get("class") or "").split(".")[-1],
            "text": view.get("text") or "",
            "content_description": view.get("content_description") or "",
            "resource_id": view.get("resource_id") or "",
            "editable": bool(view.get("editable")),
            "bounds": view.get("bounds"),
            "view_str": view.get("view_str") or "",
        })
    payload = {
        "state_str": state_str,
        "activity": getattr(state, "foreground_activity", ""),
        "screenshot": getattr(state, "screenshot_path", None),
        "signal": signal,
        "semantics_note": (
            "content_description present means Flutter semantics are on for that node. "
            "Empty text/content-description/resource-id on a clickable View means the "
            "app did not expose a label (typical for icon-only bottom navigation)."
        ),
        "clickable_or_editable": clickable[:40],
    }
    try:
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.write("\n")
    except Exception:
        return None
    LOGGER.info("low_signal_screen dump written: %s (unlabeled %s/%s nav=%s)" % (
        path, signal.get("unlabeled"), signal.get("total"), signal.get("unlabeled_nav"),
    ))
    return path


def parse_normalized_tap(parsed, width, height):
    if not isinstance(parsed, dict):
        return None
    nx = parsed.get("tap_nx")
    ny = parsed.get("tap_ny")
    if nx is None or ny is None:
        point = parsed.get("tap_point") or parsed.get("point")
        if isinstance(point, (list, tuple)) and len(point) >= 2:
            nx, ny = point[0], point[1]
    try:
        nx = float(nx)
        ny = float(ny)
    except (TypeError, ValueError):
        return None
    if 0.0 <= nx <= 1.0 and 0.0 <= ny <= 1.0:
        if nx < 0.03 or ny < 0.03 or nx > 0.97 or ny > 0.97:
            return None
        # VLM "I don't know" default is the screenshot center.
        if abs(nx - 0.5) <= 0.08 and abs(ny - 0.5) <= 0.08:
            return None
        x = int(round(nx * width))
        y = int(round(ny * height))
    elif 0.0 <= nx <= width and 0.0 <= ny <= height:
        x, y = int(nx), int(ny)
    else:
        return None
    if x < 24 or y < 24:
        return None
    if width and x > width - 8:
        return None
    if height and y > height - 8:
        return None
    return x, y


def plausible_typed_value(text):
    value = (text or "").strip()
    if not value or len(value) > 80:
        return False
    lower = value.lower()
    if "<" in value or "bound_box" in lower or value.startswith("{") or "button id=" in lower:
        return False
    if lower in ("search to get results", "search songs", "none", "null", "placeholder"):
        return False
    if "value if typing" in lower or "remaining step" in lower:
        return False
    if lower.startswith("why this") or "action_id" in lower:
        return False
    if " " in value and len(value.split()) > 8:
        return False
    return True
