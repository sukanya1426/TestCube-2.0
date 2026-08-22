"""Toggleable coverage-improvement helpers (ablation-friendly)."""

from droidbot.input_event import ScrollEvent

from .advisor import _event_label, _looks_like_fab, _score_event, _tokens
from .chain_memory import is_non_idempotent
from .signatures import widget_signature


CREATE_WORDS = ("create", "select", "add", "new", "plus")
MENU_TOKENS = ("more options", "overflow", "more", "three-dot", "menu")


def needs_affordance_search(remaining):
    blob = " ".join(remaining or []).lower()
    return any(word in blob for word in CREATE_WORDS)


def _extent(events):
    max_right = 0
    max_bottom = 0
    for event in events or []:
        bounds = (getattr(event, "view", None) or {}).get("bounds") or [[0, 0], [0, 0]]
        max_right = max(max_right, bounds[1][0])
        max_bottom = max(max_bottom, bounds[1][1])
    return max_right, max_bottom


def find_affordance_event(events, tried_tiers=None):
    """Try FAB, plus icons, overflow/menu, then scroll. Return (event, tier)."""
    tried = set(tried_tiers or [])
    max_right, max_bottom = _extent(events)
    if "fab" not in tried:
        for event in events or []:
            if _looks_like_fab(event, max_right, max_bottom):
                return event, "fab"
    if "plus" not in tried:
        for event in events or []:
            label = _event_label(event).lower()
            rid = str((getattr(event, "view", None) or {}).get("resource_id") or "").lower()
            if "plus" in label or label.strip() in ("+", "add") or "fab" in label:
                return event, "plus"
            if any(token in rid for token in ("plus", "add", "fab")):
                return event, "plus"
    if "menu" not in tried:
        for event in events or []:
            label = _event_label(event).lower()
            rid = str((getattr(event, "view", None) or {}).get("resource_id") or "").lower()
            blob = label + " " + rid
            if any(token in blob for token in MENU_TOKENS):
                return event, "menu"
    if "scroll" not in tried:
        for event in events or []:
            event_type = (getattr(event, "event_type", "") or "").lower()
            if isinstance(event, ScrollEvent) or "scroll" in event_type:
                return event, "scroll"
    return None, None


def pick_untried_plausible(events, remaining, keywords, tried_keys, action_key_fn, floor=2.0):
    """Best unused widget whose heuristic score is above `floor`."""
    current_step = remaining[0] if remaining else ""
    best = None
    for event in events or []:
        key = action_key_fn(event)
        if key in tried_keys:
            continue
        score, why = _score_event(event, current_step, remaining, keywords, stuck=True)
        if score < floor:
            continue
        if best is None or score > best[0]:
            best = (score, event, why)
    if best is None:
        return None, ""
    return best[1], best[2]


def feature_keywords(feature):
    keywords = set(_tokens((feature or {}).get("name")))
    for word in (feature or {}).get("keywords") or []:
        keywords.update(_tokens(word))
    for word in (feature or {}).get("nav_hints") or []:
        keywords.update(_tokens(word))
    for action in ((feature or {}).get("remaining_actions") or [])[:3]:
        keywords.update(_tokens(action))
    return keywords


def non_idempotent_key(event):
    label = _event_label(event)
    sig = widget_signature(event)
    if not is_non_idempotent(sig, label):
        return None
    return sig or label.lower()


def is_stagnant(novelty_window, remaining_window, window=8, novelty_floor=0.2):
    if len(novelty_window) < window or len(remaining_window) < window:
        return False
    novelty = float(sum(novelty_window[-window:])) / float(window)
    remaining_shrunk = remaining_window[-1] < remaining_window[-window]
    return novelty < novelty_floor and not remaining_shrunk
