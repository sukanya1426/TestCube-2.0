"""Dynamic text-field context: credentials, optional per-app functions, then LLM."""

import importlib.util
import os
import re

from droidbot.GeminiAI import GeminiAi

from .run_stats import STATS


DEFAULT_FUNCTIONS = {
    "get_search_query_for": lambda feature_context=None: "test query",
    "get_coupon_code": lambda: "SAVE10",
    "get_sample_name": lambda: "Testcube Playlist",
    "get_sample_amount": lambda: "10.00",
    "get_email": lambda: GeminiAi._credential_value(GeminiAi._credentials, "email") or "test@example.com",
    "get_password": lambda: GeminiAi._credential_value(GeminiAi._credentials, "pwd") or "Testcube123",
}


def load_context_module(path):
    if not path or not os.path.isfile(path):
        return {}
    spec = importlib.util.spec_from_file_location("testcube_context_functions", path)
    if spec is None or spec.loader is None:
        return {}
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    found = {}
    for name in dir(module):
        if name.startswith("_"):
            continue
        value = getattr(module, name)
        if callable(value):
            found[name] = value
    return found


def call_function(name, functions, feature_context=None):
    func = (functions or {}).get(name)
    if func is None:
        STATS.record_context(name, False, "")
        return None
    try:
        try:
            value = func(feature_context)
        except TypeError:
            value = func()
        STATS.record_context(name, True, value)
        return value
    except Exception:
        STATS.record_context(name, False, "")
        return None


def credential_category_match(view, remaining, feature=None):
    """Return (text, 'credential') when credential.txt has a matching category.

    Does not call the VLM/LLM. Returns (None, None) when no category matches.
    """
    blob = " ".join(str(item) for item in (remaining or [])).lower()
    name = ((feature or {}).get("name") or "").lower()
    view_blob = " ".join((
        str((view or {}).get("text") or ""),
        str((view or {}).get("content_description") or ""),
        str((view or {}).get("resource_id") or ""),
        str((view or {}).get("hint") or ""),
    )).lower()
    combined = " ".join((blob, name, view_blob))
    mapping = (
        (("search", "query", "song", "artist", "track"), "search_query"),
        (("playlist name", "display name", "full name", "first name"), "playlist_name"),
        (("email", "e-mail", "user"), "email"),
        (("pass", "pwd"), "pwd"),
        (("phone",), "phone"),
        (("amount", "price", "balance"), "rating"),
        (("city",), "city"),
        (("payee",), "f_name"),
        (("note", "memo", "comment", "category"), "comment"),
    )
    if "playlist" in combined and "search" not in combined:
        value = GeminiAi._credential_value(GeminiAi._credentials, "playlist_name")
        if value:
            return str(value), "credential"
    for needles, key in mapping:
        if any(token in combined for token in needles):
            value = GeminiAi._credential_value(GeminiAi._credentials, key)
            if value:
                return str(value), "credential"
    return None, None


def retrieve_text(view, remaining, feature=None, module_path=None):
    """Return (text, source). Source is credential|function:<name>|llm|fallback."""
    functions = dict(DEFAULT_FUNCTIONS)
    functions.update(load_context_module(module_path))
    blob = " ".join(str(item) for item in (remaining or [])).lower()
    name = ((feature or {}).get("name") or "").lower()
    context = {"remaining": remaining, "feature": feature, "view": view}

    view_blob = " ".join((
        str((view or {}).get("text") or ""),
        str((view or {}).get("content_description") or ""),
        str((view or {}).get("resource_id") or ""),
        str((view or {}).get("hint") or ""),
    )).lower()
    wants_search = any(
        word in blob or word in name or word in view_blob
        for word in ("search", "query", "song", "artist", "track")
    )
    if wants_search:
        cred = GeminiAi._credential_value(GeminiAi._credentials, "search_query")
        if cred:
            return cred, "credential"
        value = call_function("get_search_query_for", functions, context)
        if value:
            return str(value), "function:get_search_query_for"
    if "coupon" in blob or "promo" in blob:
        value = call_function("get_coupon_code", functions, context)
        if value:
            return str(value), "function:get_coupon_code"
    if "playlist" in blob or any(phrase in blob for phrase in (
        "playlist name", "display name", "full name", "first name", "last name", "your name",
    )):
        value = call_function("get_sample_name", functions, context)
        if value:
            return str(value), "function:get_sample_name"
    if "amount" in blob or "price" in blob:
        value = call_function("get_sample_amount", functions, context)
        if value:
            return str(value), "function:get_sample_amount"

    if GeminiAi.is_disabled():
        return GeminiAi._fallback_field_input(
            str((view or {}).get("text") or ""),
            str((view or {}).get("resource_id") or ""),
            bool((view or {}).get("is_password")),
        ), "fallback"

    STATS.record_llm("context_retrieval")
    prompt = (
        "A GUI tester needs a value for one Android text field.\n"
        "Feature: %s\nRemaining steps: %s\n"
        "Decide: emit JSON {\"text\":\"...\"} OR {\"function\":\"get_search_query_for\"} "
        "from this list: %s.\nReturn ONLY JSON."
        % (
            name,
            remaining,
            sorted(functions.keys()),
        )
    )
    try:
        raw = GeminiAi.generate_content(prompt)
        parsed = GeminiAi._parse_object(raw) or {}
    except Exception:
        parsed = {}
    func_name = parsed.get("function") or ""
    if func_name:
        well = func_name in functions and re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", func_name)
        if well:
            value = call_function(func_name, functions, context)
            if value:
                return str(value), "function:%s" % func_name
        STATS.record_context(func_name, False, "")
    text = parsed.get("text")
    if text:
        return str(text), "llm"
    return GeminiAi._fallback_field_input(
        str((view or {}).get("text") or ""),
        str((view or {}).get("resource_id") or ""),
        bool((view or {}).get("is_password")),
    ), "fallback"
