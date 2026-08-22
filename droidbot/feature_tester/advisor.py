"""Choose the next GUI action for the current feature.

Heuristics run first. A local Ollama VLM is preferred for screenshot
decisions; Gemini is the cloud fallback.
"""

import logging
import os
import re

from droidbot.GeminiAI import GeminiAi
from droidbot.input_event import KeyEvent, LongTouchEvent, ScrollEvent, SetTextEvent
from droidbot.input_policy import CTA_LABELS, PERMISSION_CONFIRM_LABELS, PERMISSION_DENY_LABELS


STOPWORDS = {
    "the", "a", "an", "for", "to", "of", "and", "or", "in", "on", "with",
    "your", "this", "that", "from", "into", "open", "tap", "click", "use",
    "the", "app", "screen", "confirm", "visible", "action", "primary",
}

HEURISTIC_TRUST = 0.55
MAX_CATALOG = 36

TYPING_WORDS = ("enter", "type", "input", "query")
TYPING_FIELD_WORDS = ("name", "password", "email", "amount", "search")

ERROR_TOKENS = (
    "exception", "dioexception", "something went wrong", "view logs",
    "an error", "error occurred", "failed to", "timeout", "crash",
)
EMPTY_TOKENS = (
    "no records", "no results", "nothing here", "no items",
    "try adjusting", "empty list", "nothing to show", "no data",
    "0 songs", "0 song", "0 tracks", "0 track", "0 playlists", "0 playlist",
    "streamed overall", "nothing playing", "no songs", "no tracks",
    "nothing streamed", "nothing to play",
    "haven't listened", "have not listened", "minutes listened",
    "listened to music", "0 minutes", "0 artist's", "0 artists",
)
EMPTY_COUNT_RE = re.compile(
    r"(?:^|[\s|/])0\s+(?:songs?|tracks?|playlists?|albums?|items?|results?|artists?)\b",
    re.I,
)
SEARCH_PLACEHOLDERS = (
    "search to get results",
    "search songs",
    "type to search",
    "search here",
    "search for a song",
)
LOADING_TOKENS = (
    "building your timeline",
    "please wait",
    "loading…",
    "loading...",
    "just a moment",
)

NAV_DESTINATIONS = (
    ("search", ("search",)),
    ("library", ("library", "playlist")),
    ("settings", ("settings", "plugin", "theme", "language")),
    ("home", ("home", "connect device")),
    ("lyrics", ("lyrics",)),
    ("queue", ("queue",)),
    ("player", ("player", "now playing", "shuffle", "repeat", "sleep")),
    ("login", ("log in", "login", "spotify")),
    ("guest", ("skip this", "continue as guest")),
    ("accounts", ("accounts",)),
    ("budget", ("budget",)),
    ("reports", ("reports",)),
    ("payee", ("payee", "payees")),
)


class AdvisorDecision(object):
    def __init__(self, decision="act", action_index=None, text="", matched_step="",
                 reason="", confidence=0.0, source="heuristic", leave_app_mode=None,
                 tap_x=None, tap_y=None, used_screenshot=False):
        self.decision = decision
        self.action_index = action_index
        self.text = text
        self.matched_step = matched_step
        self.reason = reason
        self.confidence = confidence
        self.source = source
        self.leave_app_mode = leave_app_mode
        self.tap_x = tap_x
        self.tap_y = tap_y
        self.used_screenshot = used_screenshot


class FeatureAdvisor(object):
    def __init__(self, app_name=None):
        self.app_name = app_name
        self._cache = {}
        self._llm_failures = 0
        self.logger = logging.getLogger("TestCube.advisor")
        self.journal = None

    def decide(self, feature, state, events, outside_kind=None, stuck=False,
               no_progress=0, screenshot_path=None):
        if not events:
            return AdvisorDecision(
                decision="restart_app",
                reason="No UI actions are available on this screen.",
                source="rule",
            )

        remaining = feature.get("remaining_actions") or feature.get("actions") or []
        cache_key = (
            feature.get("id"),
            state.state_str if state else "",
            tuple(remaining),
            outside_kind,
            stuck,
            no_progress,
        )
        if cache_key in self._cache:
            return self._cache[cache_key]

        if outside_kind == "file_picker":
            decision = self._file_picker_decision(events, remaining)
            self._cache[cache_key] = decision
            return decision
        if outside_kind:
            back_index = _find_back(events)
            decision = AdvisorDecision(
                decision="act",
                action_index=back_index if back_index is not None else 0,
                reason="Left the app unintentionally; going back.",
                matched_step="",
                confidence=0.9,
                source="rule",
                leave_app_mode=outside_kind,
            )
            self._cache[cache_key] = decision
            return decision

        from .grounding import dump_low_signal_state, needs_visual_ground

        heuristic = self._heuristic(feature, events, remaining, stuck=stuck)
        if remaining and _is_typing_step(remaining[0]) and heuristic.action_index is not None:
            if 0 <= heuristic.action_index < len(events) and _is_set_text(events[heuristic.action_index]):
                self._cache[cache_key] = heuristic
                return heuristic
        force_visual, signal = needs_visual_ground(feature, events)
        if force_visual:
            line = (
                "low_signal_screen state=%s unlabeled=%s/%s nav=%s dest_missing=%s "
                "skipping heuristic-first (ratio=%.2f)"
                % (
                    getattr(state, "state_str", "") or "-",
                    signal.get("unlabeled"),
                    signal.get("total"),
                    signal.get("unlabeled_nav"),
                    signal.get("destination_missing"),
                    signal.get("ratio") or 0.0,
                )
            )
            self.logger.info(line)
            if self.journal:
                self.journal._append_log(line)
                dump_low_signal_state(self.journal, state, signal)
            visual = self._visual_ground(
                feature, state, events, remaining, heuristic,
                screenshot_path=screenshot_path, signal=signal,
            )
            if visual is not None:
                self._cache[cache_key] = visual
                return visual
        if heuristic.confidence >= HEURISTIC_TRUST and not stuck and not force_visual:
            self._cache[cache_key] = heuristic
            return heuristic

        if remaining and not heuristic.matched_step and no_progress >= 10:
            nav = self.navigate(feature, events)
            if nav is not None:
                self._cache[cache_key] = nav
                return nav
            decision = AdvisorDecision(
                decision="drop_feature",
                reason="Could not progress this feature after several attempts.",
                confidence=0.7,
                source="rule",
            )
            self._cache[cache_key] = decision
            return decision

        llm = self._ask_llm(
            feature, state, events, remaining, heuristic,
            stuck=stuck, screenshot_path=screenshot_path,
            force_screenshot=force_visual,
        )
        decision = llm or heuristic
        if decision.decision in ("feature_not_present", "drop_feature", "not_present", "drop"):
            nav = self.navigate(feature, events)
            if nav is not None and no_progress < 10:
                decision = nav
        if not remaining and decision.decision == "act" and decision.confidence < 0.4:
            decision = AdvisorDecision(
                decision="feature_complete",
                reason="No remaining steps and the current screen looks like a result.",
                source="heuristic",
                confidence=0.5,
            )
        self._cache[cache_key] = decision
        return decision

    def navigate(self, feature, events):
        """Pick a labeled in-app control that moves toward the feature."""
        if not events:
            return None
        remaining = feature.get("remaining_actions") or feature.get("actions") or []
        hints = list(feature.get("nav_hints") or [])
        blob = " ".join(
            [feature.get("name") or "", feature.get("description") or ""]
            + remaining
            + (feature.get("keywords") or [])
            + hints
        ).lower()
        typing = bool(remaining) and _is_typing_step(remaining[0])
        has_text = any(_is_set_text(event) for event in events)
        ranked = []
        for index, event in enumerate(events):
            label = _event_label(event).lower()
            if _looks_like_empty_label(label) or _looks_like_error_label(label):
                continue
            if _is_set_text(event) and (
                typing or (_tokens(blob) & {"search", "find", "query", "song", "play"})
            ):
                ranked.append((8, index, "search field"))
                continue
            if not label.strip():
                # Unlabeled top-left close is handled by the interstitial policy,
                # not navigation — tapping it after the hub bounces the same screens.
                continue
            if any(token in label for token in ("github", "donate", "open collective", "patreon")):
                continue
            score = 0
            why = "nav"
            for hint in hints:
                if hint.lower() in label:
                    score += 8
                    why = "nav hint %s" % hint
            skip_nav_dest = typing and has_text
            if not skip_nav_dest:
                for dest, labels in NAV_DESTINATIONS:
                    if dest in blob or any(word in blob for word in labels):
                        if any(word in label for word in labels) or dest in label:
                            score += 6
                            why = "navigate to %s" % dest
            if "skip" in blob and "skip" in label:
                score += 7
                why = "guest skip"
            if isinstance(event, KeyEvent):
                score = 1 if score == 0 else score
            ranked.append((score, index, why))
        ranked.sort(reverse=True)
        if not ranked or ranked[0][0] < 4:
            return None
        _score, index, why = ranked[0]
        return AdvisorDecision(
            decision="act",
            action_index=index,
            reason=why,
            confidence=0.6,
            source="nav",
        )

    def fill_text(self, view, remaining, feature=None, allow_unresolved=True):
        view = view or {}
        from .context import credential_category_match
        from .grounding import plausible_typed_value
        from .run_stats import STATS
        field = (
            _view_text(view.get("text"))
            or _view_text(view.get("content_description"))
            or _view_text(view.get("resource_id"))
            or "text field"
        )
        blob = " ".join(_view_text(item) for item in (remaining or [])).lower()
        label = ("%s %s" % (
            _view_text(view.get("text")),
            _view_text(view.get("content_description")),
        )).lower()
        if "leave blank" in blob or ("optional" in blob and "password" in (blob + label)):
            self._log_text_generation(field, "", "optional-blank", remaining)
            STATS.record_field_resolution("optional-blank", field=field, value="")
            STATS.record_text("", "optional-blank", field=field)
            return ""

        text, source = "", ""
        try:
            text, source = credential_category_match(view, remaining, feature=feature)
        except Exception:
            text, source = None, None
        if not plausible_typed_value(text):
            text, source = "", ""
        if text:
            STATS.record_field_resolution("credential", field=field, value=text)
            STATS.record_text(text, "credential", field=field)
            self._log_text_generation(field, text, "credential", remaining)
            return text

        if not (GeminiAi.is_disabled() or self._llm_failures >= 3):
            try:
                staged = GeminiAi.suggest_field_input_for_step(view, remaining, feature=feature)
                if plausible_typed_value(staged):
                    STATS.record_field_resolution("vlm", field=field, value=staged)
                    STATS.record_text(staged, "llm", field=field)
                    self._log_text_generation(field, staged, "vlm", remaining)
                    return staged
            except Exception:
                self._llm_failures += 1

        line = "field_unresolved: field=%r remaining=%r descriptor=%r" % (
            field, (remaining or [""])[0] if remaining else "",
            {"text": _view_text(view.get("text")), "content_description": _view_text(view.get("content_description")),
             "resource_id": _view_text(view.get("resource_id")), "class": _view_text(view.get("class"))},
        )
        self.logger.info(line)
        if self.journal:
            self.journal._append_log(line)
        STATS.record_field_resolution("unresolved", field=field, value="")
        if not allow_unresolved:
            return None
        fallback = GeminiAi._fallback_field_input(
            _view_text(view.get("text")) or _view_text(view.get("content_description")),
            _view_text(view.get("resource_id")),
            bool(view.get("is_password")),
        )
        STATS.record_text(fallback, "fallback", field=field)
        self._log_text_generation(field, fallback, "fallback", remaining)
        return fallback

    def _log_text_generation(self, field, text, source, remaining):
        line = (
            "Text generation: field=%r remaining=%r value=%r source=%s"
            % (field, (remaining or [""])[0] if remaining else "", text, source)
        )
        self.logger.info(line)
        if self.journal:
            self.journal._append_log(line)

    def _heuristic(self, feature, events, remaining, stuck=False):
        current_step = remaining[0] if remaining else (feature.get("name") or "")
        keywords = set(_tokens(feature.get("name")))
        for word in feature.get("keywords") or []:
            keywords.update(_tokens(word))
        for word in feature.get("nav_hints") or []:
            keywords.update(_tokens(word))
        for action in remaining[:3]:
            keywords.update(_tokens(action))

        if remaining and _is_typing_step(remaining[0]):
            typed = self._best_typing_event(
                events, remaining, keywords, stuck=stuck, feature=feature,
            )
            if typed is not None:
                return typed

        ranked = []
        max_right = 0
        max_bottom = 0
        for event in events:
            bounds = (getattr(event, "view", None) or {}).get("bounds") or [[0, 0], [0, 0]]
            max_right = max(max_right, bounds[1][0])
            max_bottom = max(max_bottom, bounds[1][1])
        nav_tabs = [event for event in events if _is_bottom_nav(event)]
        rightmost_nav = nav_tabs[-1] if nav_tabs else None
        settings_blob = " ".join(remaining).lower() + " " + (feature.get("name") or "").lower()
        wants_settings = any(word in settings_blob for word in ("settings", "plugin", "metadata", "about"))
        for index, event in enumerate(events):
            score, why = _score_event(event, current_step, remaining, keywords, stuck=stuck)
            if remaining and any(word in current_step.lower() for word in ("create", "new", "add", "plus")):
                if _looks_like_fab(event, max_right, max_bottom):
                    score += 6
                    why = "add/create control"
            if wants_settings and event is rightmost_nav and _visible_label(event).strip():
                score += 8
                why = "rightmost navigation tab"
            intent = _player_step_intent(feature, remaining)
            if intent:
                role = _widget_player_role(event)
                bounds = (getattr(event, "view", None) or {}).get("bounds") or [[0, 0], [0, 0]]
                if intent == "open" and role == "card":
                    score += 12
                    why = "mini-player card"
                elif intent == role:
                    score += 12
                    why = "player control %s" % role
                elif intent == "open" and role in ("pause", "next", "prev", "shuffle", "repeat"):
                    score -= 6
                    why = "player chrome, not the card"
                elif intent == "open" and max_bottom and bounds[1][1] >= max_bottom * 0.82:
                    width = bounds[1][0] - bounds[0][0]
                    if role not in ("pause", "next", "prev") and width >= max(80, max_right * 0.4):
                        score += 7
                        why = "bottom player bar"
            ranked.append((score, index, why))
        ranked.sort(reverse=True)
        if not ranked:
            return AdvisorDecision(decision="drop_feature", reason="Empty action catalog.", source="heuristic")

        best_score, best_index, why = ranked[0]
        event = events[best_index]
        confidence = min(0.95, best_score / 8.0)
        text = ""
        typing = bool(remaining) and _is_typing_step(remaining[0])
        if typing and (isinstance(event, SetTextEvent) or _is_set_text(event)):
            try:
                text = self.fill_text(getattr(event, "view", None), remaining, feature=feature)
            except Exception:
                text = ""
        elif not typing and (isinstance(event, SetTextEvent) or _is_set_text(event)):
            # Don't type into a random field when the remaining step is a tap.
            for index, alt in enumerate(events):
                if not (_is_set_text(alt) or isinstance(alt, SetTextEvent)):
                    best_index = index
                    event = alt
                    break
        matched = ""
        if _event_fits_step(event, current_step) and _label_supports_step(event, current_step):
            if best_score >= 4 or (_tokens(_visible_label(event)) & _step_content_tokens(current_step)):
                matched = current_step
        if stuck and best_score < 3:
            back_index = _find_back(events)
            if back_index is not None:
                return AdvisorDecision(
                    decision="act",
                    action_index=back_index,
                    reason="Stuck; trying BACK to recover.",
                    confidence=0.45,
                    source="heuristic",
                )
        if not remaining and best_score < 3:
            return AdvisorDecision(
                decision="feature_complete",
                reason="Expected steps are done.",
                confidence=0.6,
                source="heuristic",
            )
        return AdvisorDecision(
            decision="act",
            action_index=best_index,
            text=text,
            matched_step=matched,
            reason=why,
            confidence=confidence,
            source="heuristic",
        )

    def _best_typing_event(self, events, remaining, keywords, stuck=False, feature=None):
        current_step = remaining[0]
        best = None
        for index, event in enumerate(events):
            if not _is_set_text(event):
                continue
            score, why = _score_event(event, current_step, remaining, keywords, stuck=stuck)
            if best is None or score > best[0]:
                best = (score, index, why, event)
        if best is None:
            return None
        _score, index, why, event = best
        try:
            text = self.fill_text(getattr(event, "view", None), remaining, feature=feature)
        except Exception:
            text = ""
        if text is None:
            return None
        return AdvisorDecision(
            decision="act",
            action_index=index,
            text=text,
            matched_step=current_step,
            reason=why or "type into the visible field",
            confidence=0.92,
            source="heuristic",
        )

    def _file_picker_decision(self, events, remaining):
        blob = " ".join(remaining or []).lower()
        prefer_ext = _picker_extensions(blob)
        file_step = _is_file_related_step(blob)
        deny = (
            "preview", "youtube", "camera", "record",
            "breadcrumb", "audio", "music", ".ogg", ".mp3", ".wav", ".m4a",
            "new folder", "create_dir", "create directory", "folder name",
            "option_menu_create", "more options",
        )
        if any(word in blob for word in ("music", "audio", "mp3", "song", "track")):
            deny = (
                "preview", "youtube", "camera", "record",
                "new folder", "create_dir", "folder name", "option_menu_create",
            )
        if not any(word in blob for word in ("image", "photo", "png", "jpg")):
            deny += ("images", "pictures", "photos", ".jpg", ".png")
        all_labels = " ".join(_event_label(event).lower() for event in events or [])
        in_folder_dialog = "folder name" in all_labels or (
            "new folder" in all_labels and "alerttitle" in all_labels
        )
        if in_folder_dialog:
            for index, event in enumerate(events):
                lower = _event_label(event).lower()
                if "cancel" in lower or (isinstance(event, KeyEvent) and (getattr(event, "name", "") or "").upper() == "BACK"):
                    return AdvisorDecision(
                        decision="act",
                        action_index=index,
                        reason="Cancel folder creation in the file picker.",
                        matched_step="",
                        confidence=0.9,
                        source="rule",
                        leave_app_mode="file_picker",
                    )
            return AdvisorDecision(
                decision="act",
                action_index=_find_back(events) or 0,
                reason="Back out of folder creation in the file picker.",
                source="rule",
                leave_app_mode="file_picker",
            )
        save_as = any(
            _is_set_text(event) and any(
                token in _event_label(event).lower()
                for token in (".mmb", ".csv", ".qif", "your_data", "filename", "file name", "title")
            )
            for event in events
        )
        best = None
        text = ""
        for index, event in enumerate(events):
            label = _event_label(event)
            lower = label.lower()
            if any(deny_word in lower for deny_word in PERMISSION_DENY_LABELS):
                continue
            if any(token in lower for token in deny):
                continue
            if "cancel" in lower:
                continue
            score = 0
            if any(word in lower for word in ("save as", "save", "use this folder")):
                score = 16
            elif save_as and _is_set_text(event):
                existing = _view_text((getattr(event, "view", None) or {}).get("text")).strip()
                if existing and "." in existing:
                    score = 0
                else:
                    score = 3
                    text = "testcube.mmb"
            elif any(ext in lower for ext in prefer_ext):
                score = 12
            elif save_as and (
                lower.strip() in ("ok", "ok button1")
                or ("ok" in lower and "button" in lower)
            ):
                score = 12
            elif (not save_as) and any(word in lower for word in ("document", "files", "browse")):
                score = 8
            elif any(word in lower for word in ("open", "select", "just once", "allow", "use this", "done")):
                score = 6
            elif _is_set_text(event):
                score = 2
                text = "testcube.mmb"
            elif isinstance(event, ScrollEvent):
                score = 1
            if best is None or score > best[0]:
                best = (score, index, label, text if _is_set_text(event) else "")
        if not best or best[0] < 2:
            return AdvisorDecision(
                decision="act",
                action_index=_find_back(events) or 0,
                reason="File picker had no matching document; going back.",
                source="rule",
                leave_app_mode="file_picker",
            )
        matched = ""
        if file_step and remaining and best[0] >= 8:
            matched = remaining[0]
        return AdvisorDecision(
            decision="act",
            action_index=best[1],
            text=best[3] or "",
            reason="Picking a file/confirming in the system picker: %s" % best[2][:80],
            matched_step=matched,
            confidence=0.8,
            source="rule",
            leave_app_mode="file_picker",
        )

    def _visual_ground(self, feature, state, events, remaining, heuristic,
                       screenshot_path=None, signal=None):
        """Ask the VLM for screenshot tap coordinates, not unlabeled action_ids."""
        from .grounding import parse_normalized_tap, plausible_typed_value, screen_size
        feature_id = (feature or {}).get("id") or "-"
        use_screenshot = bool(screenshot_path and os.path.isfile(screenshot_path))
        line = (
            "visual_ground for %s screenshot_attached=%s path=%s signal=%s"
            % (feature_id, use_screenshot, screenshot_path or "", signal or {})
        )
        self.logger.info(line)
        if self.journal:
            self.journal._append_log(line)
        if not use_screenshot:
            return None
        if GeminiAi.is_disabled() or self._llm_failures >= 3:
            return None
        catalog = catalog_actions(events)
        width, height = screen_size(state)
        prompt = (
            "You are TestCube, testing ONE Android app feature from a screenshot.\n"
            "Many widgets are unlabeled Views (icon-only bottom navigation is common). "
            "Do NOT pick an action_id from a list of indistinguishable Views. "
            "Look at the screenshot and return tap coordinates for the control that "
            "advances the remaining step.\n"
            "Unlabeled icons along the bottom edge are typically primary navigation "
            "(home / search / library / settings, left to right or similar). "
            "Use the screenshot, not the action catalog, to choose.\n"
            "Return ONLY JSON:\n"
            "{"
            '"decision":"act",'
            '"tap_nx":0.0,'
            '"tap_ny":0.0,'
            '"text":"",'
            '"matched_step":"",'
            '"reason":"what you tapped in the screenshot"'
            "}\n"
            "tap_nx and tap_ny are 0-1 relative to the screenshot (left/top = 0). "
            "If the remaining step is enter/type/search and a text field is visible, "
            "put the string to type in text and still return the field's tap point "
            "only if no set_text action exists.\n"
            "App: %s\nFeature: %s %s\nDescription: %s\n"
            "Remaining steps: %s\nCompleted: %s\nNav hints: %s\n"
            "Screen size px: %sx%s\n"
            "Action catalog (unreliable when labels are empty):\n%s\n"
        ) % (
            self.app_name or GeminiAi._app_name or "unknown",
            feature.get("id"),
            feature.get("name"),
            (feature.get("description") or "")[:400],
            remaining or ["(none)"],
            feature.get("completed_actions") or [],
            feature.get("nav_hints") or [],
            width, height,
            "\n".join(
                "%s. %s %s" % (item["id"], item.get("type"), item.get("label") or "")
                for item in catalog
            ),
        )
        try:
            from PIL import Image
            image = Image.open(screenshot_path)
            image.thumbnail((768, 768))
            parts = [prompt, image]
        except Exception:
            self.logger.info("visual_ground could not load screenshot %s" % screenshot_path)
            return None
        try:
            from .run_stats import STATS
            STATS.record_llm("visual_ground")
            raw = GeminiAi.generate_content(parts)
            parsed = GeminiAi._parse_object(raw) or {}
        except Exception as exc:
            self._llm_failures += 1
            self.logger.info("visual_ground LLM failed: %s" % exc)
            return None
        point = parse_normalized_tap(parsed, width, height)
        text = parsed.get("text") or ""
        if not plausible_typed_value(text):
            text = ""
        if remaining and _is_typing_step(remaining[0]):
            for index, event in enumerate(events):
                if _is_set_text(event):
                    if not text:
                        text = self.fill_text(getattr(event, "view", None), remaining, feature=feature)
                    return AdvisorDecision(
                        decision="act",
                        action_index=index,
                        text=text,
                        matched_step=remaining[0],
                        reason=parsed.get("reason") or "Type into the visible field.",
                        confidence=0.8,
                        source="visual_ground",
                        used_screenshot=True,
                    )
        if point is None:
            self.logger.info("visual_ground returned no usable tap point: %s" % parsed)
            return None
        matched = ""
        if remaining and not _is_typing_step(remaining[0]):
            matched = parsed.get("matched_step") or ""
            if remaining and matched not in remaining:
                matched = ""
        result = AdvisorDecision(
            decision=str(parsed.get("decision") or "act").strip() or "act",
            action_index=heuristic.action_index,
            text=text,
            matched_step=matched,
            reason=parsed.get("reason") or "Screenshot tap for unlabeled widgets.",
            confidence=0.8,
            source="visual_ground",
            tap_x=point[0],
            tap_y=point[1],
            used_screenshot=True,
        )
        self.logger.info(
            "visual_ground tap=(%s,%s) nx/ny from screenshot for %s"
            % (point[0], point[1], feature_id)
        )
        return result

    def _ask_llm(self, feature, state, events, remaining, heuristic,
                 stuck=False, screenshot_path=None, force_screenshot=False):
        feature_id = (feature or {}).get("id") or "-"
        line = (
            "LLM/VLM fallback path entered for %s (stuck=%s heuristic_conf=%.2f)"
            % (feature_id, stuck, getattr(heuristic, "confidence", 0.0) or 0.0)
        )
        self.logger.info(line)
        if self.journal:
            self.journal._append_log(line)
        if GeminiAi.is_disabled() or self._llm_failures >= 3:
            skip = (
                "LLM/VLM fallback skipped for %s (disabled=%s failures=%d)"
                % (feature_id, GeminiAi.is_disabled(), self._llm_failures)
            )
            self.logger.info(skip)
            if self.journal:
                self.journal._append_log(skip)
            return None
        catalog = catalog_actions(events)
        ui_text = ""
        try:
            ui_text, activity, _indexed = state.get_text_representation()
        except Exception:
            activity = getattr(state, "foreground_activity", "")
            ui_text = state.search_content if state else ""
        prompt = (
            "You are TestCube, testing ONE Android app feature. "
            "Pick the single next UI action that advances this feature. "
            "If this screen is onboarding, a contribute/donate interstitial, or another hub, "
            "NAVIGATE toward the feature (Skip/Guest, Search, Library, Settings, Home, Player, Accounts). "
            "Unlabeled widgets along the bottom of the screenshot are often navigation tabs; "
            "pick the Search/Library/Home tab that matches the remaining steps. "
            "A bottom navigation tab is not a search bar or text field: if remaining says enter/type/input/query, "
            "you MUST pick a set_text action and put the value in text. "
            "If remaining says Select/Create/Play/Adjust, tap a control whose visible label matches that word. "
            "Do not mark matched_step complete for unlabeled widgets. matched_step must copy a remaining step exactly, or be empty. "
            "Do not tap empty-state copy (no records, no results, 0 songs, streamed overall) or error/log text; those do not advance any feature. "
            "After typing a search query, tap Search/submit or a result row — do not skip the submit tap. "
            "Error and empty screens are not feature_not_present: Close, Retry, BACK, or a labeled nav item toward remaining steps. "
            "Do not tap Skip/Get Started after the main hub is already reached. "
            "Do not tap random empty areas or the center of the screenshot. "
            "Do not pick a scroll/swipe action to open Search, play a track, or tap a tab; "
            "choose the matching bottom-navigation tab or a visible list row instead. "
            "Do not press BACK from the main hub — that restarts first-run. "
            "A first-run analytics/settings page is NOT the home screen: tap Navigate up or BACK, then Create Database. "
            "In a Save-as file picker, tap SAVE/OK; do not clear the file name and do not open Audio/Downloads. "
            "Do not mark the feature missing just because the current screen is not it yet. "
            "Do not open GitHub, Donate, Chrome, or the file manager except to complete a required pick/upload. "
            "matched_step must be empty unless this exact action performs that step (typing vs tap vs scroll).\n"
            "Return ONLY JSON:\n"
            "{"
            '"decision":"act|drop_feature|feature_not_present|feature_complete|restart_app",'
            '"action_id":0,'
            '"tap_nx":null,'
            '"tap_ny":null,'
            '"text":"value if typing",'
            '"matched_step":"",'
            '"reason":"why this action advances the remaining step"'
            "}\n"
            "When widgets are unlabeled Views, ignore action_id and set tap_nx/tap_ny "
            "(0-1 relative to the screenshot) for the control that matches remaining steps. "
            "Use act whenever a tap, type, long-press, or skip can move closer to the remaining steps. "
            "Use feature_not_present only if the app clearly has no such feature after you already reached its area. "
            "If remaining steps already happened, use feature_complete.\n\n"
            "App: %s\nFeature: %s %s\nDescription: %s\n"
            "Remaining steps: %s\nCompleted: %s\nNav hints: %s\nStuck: %s\n"
            "Activity: %s\nUI:\n%s\n\nActions:\n%s\nHeuristic guess: id=%s (%s)\n"
        ) % (
            self.app_name or GeminiAi._app_name or "unknown",
            feature.get("id"),
            feature.get("name"),
            (feature.get("description") or "")[:400],
            remaining or ["(none)"],
            feature.get("completed_actions") or [],
            feature.get("nav_hints") or [],
            stuck,
            activity,
            (ui_text or "")[:3500],
            "\n".join(
                "%s. %s %s" % (item["id"], item.get("type"), item.get("label") or item.get("name") or "")
                for item in catalog
            ),
            heuristic.action_index,
            heuristic.reason,
        )
        parts = prompt
        use_screenshot = screenshot_path and os.path.isfile(screenshot_path)
        prefer_vision = False
        try:
            from droidbot.local_vlm import LocalVLM
            prefer_vision = LocalVLM.is_available()
        except Exception:
            prefer_vision = False
        attach_image = use_screenshot and (prefer_vision or _sparse_ui(ui_text) or force_screenshot)
        if attach_image:
            try:
                from PIL import Image
                image = Image.open(screenshot_path)
                image.thumbnail((768, 768))
                parts = [prompt, image]
            except Exception:
                parts = prompt
        shot_line = (
            "LLM prompt for %s includes_screenshot=%s force=%s path=%s"
            % (feature_id, isinstance(parts, list), force_screenshot, screenshot_path or "")
        )
        self.logger.info(shot_line)
        if self.journal:
            self.journal._append_log(shot_line)
        try:
            from .run_stats import STATS
            STATS.record_llm("widget_scoring")
            raw = GeminiAi.generate_content(parts)
            parsed = GeminiAi._parse_object(raw) or {}
        except Exception as exc:
            self._llm_failures += 1
            print("Feature advisor LLM failed: %s" % exc)
            return None
        decision = str(parsed.get("decision") or "act").strip()
        action_id = parsed.get("action_id")
        try:
            action_id = int(action_id) if action_id is not None else heuristic.action_index
        except (TypeError, ValueError):
            action_id = heuristic.action_index
        if action_id is not None and not (0 <= action_id < len(events)):
            action_id = heuristic.action_index
        from .grounding import parse_normalized_tap, plausible_typed_value, screen_size
        text = parsed.get("text") or ""
        if not plausible_typed_value(text):
            text = ""
        if action_id is not None and _is_set_text(events[action_id]) and not text:
            text = self.fill_text(getattr(events[action_id], "view", None), remaining, feature=feature)
        matched = parsed.get("matched_step") or ""
        if "expected step" in matched.lower():
            matched = ""
        if remaining and _is_typing_step(remaining[0]):
            if action_id is None or not _is_set_text(events[action_id]):
                for index, event in enumerate(events):
                    if _is_set_text(event):
                        action_id = index
                        if not text:
                            text = self.fill_text(getattr(event, "view", None), remaining, feature=feature)
                        matched = remaining[0]
                        break
        if action_id is not None and remaining and matched:
            if not _event_fits_step(events[action_id], remaining[0]) and not _event_fits_step(events[action_id], matched):
                matched = ""
            elif not _label_supports_step(events[action_id], matched) and not _label_supports_step(events[action_id], remaining[0]):
                matched = ""
        chosen = events[action_id] if action_id is not None else None
        if chosen is not None and remaining:
            is_scroll = isinstance(chosen, ScrollEvent) or getattr(chosen, "event_type", "") == "scroll"
            wants_scroll = any(word in remaining[0].lower() for word in ("scroll", "swipe", "browse"))
            if is_scroll and not wants_scroll:
                nav = self.navigate(feature, events)
                if nav is not None:
                    return nav
                for index, event in enumerate(events):
                    if isinstance(event, ScrollEvent) or getattr(event, "event_type", "") == "scroll":
                        continue
                    if _visible_label(event).strip() or getattr(event, "nav_label", None):
                        action_id = index
                        chosen = event
                        matched = ""
                        parsed["reason"] = parsed.get("reason") or "Replaced scroll with a labeled control."
                        break
        if chosen is not None and (
            _looks_like_empty_label(_event_label(chosen))
            or _looks_like_error_label(_event_label(chosen))
        ):
            nav = self.navigate(feature, events)
            if nav is not None:
                return nav
            back_index = _find_back(events)
            if back_index is not None:
                return AdvisorDecision(
                    decision="act",
                    action_index=back_index,
                    reason="Leave empty/error copy instead of tapping it.",
                    matched_step="",
                    confidence=0.6,
                    source="rule",
                )
        used_vlm = isinstance(parts, list)
        width, height = screen_size(state)
        point = parse_normalized_tap(parsed, width, height) if used_vlm else None
        result = AdvisorDecision(
            decision=decision,
            action_index=action_id,
            text=text,
            matched_step=matched,
            reason=parsed.get("reason") or "LLM action choice",
            confidence=0.75,
            source="llm",
            tap_x=point[0] if point else None,
            tap_y=point[1] if point else None,
            used_screenshot=used_vlm,
        )
        self._log_vlm_fallback(used_vlm, heuristic, result, state)
        return result

    def _log_vlm_fallback(self, used_vlm, heuristic, decision, state):
        if not used_vlm:
            return
        try:
            from .config import get_config
            from .run_stats import STATS
            if not get_config().enabled("vlm_logging"):
                return
            STATS.record_vlm(
                getattr(heuristic, "confidence", 0) or 0,
                getattr(decision, "confidence", 0) or 0,
                agreed=(getattr(heuristic, "action_index", None) == getattr(decision, "action_index", None)),
                outcome=getattr(decision, "decision", "") or "",
                state_str=getattr(state, "state_str", "") or "",
            )
        except Exception:
            pass


def catalog_actions(events):
    items = []
    for index, event in enumerate(events):
        view = getattr(event, "view", None) or {}
        item = {
            "id": index,
            "type": getattr(event, "event_type", event.__class__.__name__),
            "label": _event_label(event)[:80],
            "resource_id": (view.get("resource_id") or "").split("/")[-1],
            "class": (view.get("class") or "").split(".")[-1],
            "name": getattr(event, "name", None),
            "direction": getattr(event, "direction", None),
        }
        items.append(item)
        if len(items) >= MAX_CATALOG:
            break
    return items


def _score_event(event, current_step, remaining, keywords, stuck=False):
    visible = _visible_label(event)
    label = _event_label(event)
    tokens = _tokens(visible)
    step_tokens = _tokens(current_step)
    overlap = tokens & (step_tokens | keywords)
    score = 2.0 * len(overlap)
    why = "label overlap %s" % sorted(overlap) if overlap else "weak match"
    step_content = _step_content_tokens(current_step)
    if step_content & tokens:
        score += 4
        why = "visible label matches the remaining step"
    step_blob = " ".join(remaining).lower()
    typing = _is_typing_step(current_step)

    if _looks_like_error_label(label):
        return -8.0, "error/log text"
    if _looks_like_empty_label(label):
        return -8.0, "empty-state copy"
    if _looks_like_search_placeholder(label) and not _is_set_text(event):
        return -8.0, "search placeholder"
    if _looks_like_loading_label(label):
        return -8.0, "loading copy"

    if _is_set_text(event):
        if typing:
            score += 8
            why = "input field for a typing step"
        else:
            score -= 1
    elif typing:
        view = getattr(event, "view", None) or {}
        cls = (_view_text(view.get("class")) or "").lower()
        rid = (_view_text(view.get("resource_id")) or "").lower()
        if any(token in cls for token in ("edittext", "textfield", "searchview", "autocompletetext")):
            score += 7
            why = "text field for typing step"
        elif any(token in rid for token in ("search", "query", "edit", "input", "field")):
            score += 5
            why = "likely input control"
    if isinstance(event, ScrollEvent) or getattr(event, "event_type", "") == "scroll":
        if any(word in step_blob for word in ("browse", "list", "scroll", "swipe")):
            score += 0.5
        else:
            score -= 8
        why = "scroll"
    if (isinstance(event, KeyEvent) or getattr(event, "event_type", "") == "key") and (
        getattr(event, "name", "") or ""
    ).upper() == "BACK":
        score = 4 if stuck else 0.2
        why = "BACK"
    if any(phrase in label.lower() for phrase in CTA_LABELS):
        if any(word in step_blob for word in ("started", "next", "continue", "onboard", "guest", "skip")):
            score += 5
            why = "onboarding CTA"
        else:
            score += 0.5
    if isinstance(event, LongTouchEvent):
        if any(phrase in step_blob for phrase in ("long-press", "long press", "context menu")):
            score += 5
            why = "long-press for context menu"
        else:
            score -= 2
    if not typing:
        nav_blob = step_blob + " " + " ".join(sorted(keywords))
        nav_label = (visible + " " + (getattr(event, "nav_label", None) or "")).lower()
        for dest, labels in NAV_DESTINATIONS:
            if dest in nav_blob or any(word in nav_blob for word in labels):
                if dest in nav_label or any(word in nav_label for word in labels):
                    if dest == "settings" and "settings" not in nav_label and "plugin" not in nav_label:
                        continue
                    if not visible.strip() and dest not in (getattr(event, "nav_label", None) or "").lower():
                        continue
                    score += 5
                    why = "navigate to %s" % dest
    if "skip" in step_blob and "skip" in label.lower():
        score += 6
        why = "guest skip"
    if any(word in label.lower() for word in PERMISSION_CONFIRM_LABELS):
        score += 4
    if any(word in label.lower() for word in PERMISSION_DENY_LABELS):
        score -= 6
    if not visible.strip() and not _is_set_text(event):
        score -= 3
    if any(token in visible.lower() for token in (".mmb", ".csv", ".qif")):
        if not any(word in step_blob for word in ("file", "import", "export", "database", "csv", "qif")):
            score -= 8
            why = "filename control, not this feature"
    lower = visible.lower()
    step_l = current_step.lower()
    intent = _player_step_intent({"name": ""}, remaining)
    role = _widget_player_role(event)
    if intent and role:
        if intent == "open" and role == "card":
            score += 8
            why = "mini-player card"
        elif intent == role:
            score += 10
            why = "player control %s" % role
        elif intent == "open" and role in ("pause", "next", "prev", "shuffle", "repeat"):
            score -= 5
            why = "player chrome, not the card"
    if any(word in current_step.lower() for word in ("add", "create", "new", "plus")):
        if "plus" in lower or lower.strip() in ("+", "add") or "fab" in lower:
            score += 6
            why = "add/create control"
    if any(word in step_l for word in ("song", "track", "result")) and any(
        word in step_l for word in ("list", "row", "item", "tap")
    ):
        if _looks_like_result_row(event):
            score += 6
            why = "likely result row"
    if re.search(r"\b(tap|press|click|hit)\s+(the\s+)?(search|submit)\b", step_l):
        if _looks_like_search_placeholder(label) or _looks_like_empty_label(label):
            score -= 8
            why = "search placeholder, not submit"
        elif "search" in label.lower() and not _is_bottom_nav(event) and not _is_set_text(event):
            score += 7
            why = "search submit"
    if any(word in current_step.lower() for word in ("import", "export", "filter", "sort", "settings", "plugin", "metadata")):
        if any(token in lower for token in ("menu", "more", "overflow", "settings", "sort", "filter", "plugin", "metadata")):
            score += 5
            why = "menu/settings row"
        if _looks_like_empty_label(label) or "plus" in lower:
            if not any(word in current_step.lower() for word in ("add", "create", "new", "plus")):
                score -= 4
    return score, why


def _event_label(event):
    if isinstance(event, KeyEvent):
        return getattr(event, "name", "") or "KEY"
    extra = getattr(event, "nav_label", None) or ""
    visible = _visible_label(event)
    direction = getattr(event, "direction", None)
    return " ".join(str(part) for part in (extra, visible, direction) if part)


def _visible_label(event):
    """Widget text the user can see — not inferred bottom-nav names."""
    if isinstance(event, KeyEvent):
        return getattr(event, "name", "") or "KEY"
    view = getattr(event, "view", None) or {}
    rid = _view_text(view.get("resource_id"))
    parts = [
        _view_text(view.get("text")),
        _view_text(view.get("content_description")),
        rid.split("/")[-1] if rid else "",
    ]
    return " ".join(str(part) for part in parts if part)


def _view_text(value):
    """Flatten UIAutomator text/content-description (str, list, or tuple) to a string."""
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return " ".join(_view_text(item) for item in value if item not in (None, "")).strip()
    return str(value)


def _is_set_text(event):
    return isinstance(event, SetTextEvent) or getattr(event, "event_type", "") == "set_text"


def _find_back(events):
    for index, event in enumerate(events):
        if isinstance(event, KeyEvent) and (getattr(event, "name", "") or "").upper() == "BACK":
            return index
    return None


def _tokens(text):
    words = set(re.findall(r"[a-z0-9]+", (text or "").lower()))
    return {word for word in words if word not in STOPWORDS and len(word) > 2}


def _sparse_ui(ui_text):
    if not ui_text:
        return True
    return ui_text.count("\n") < 6


def _event_fits_step(event, step):
    step_l = (step or "").lower()
    event_type = (getattr(event, "event_type", "") or event.__class__.__name__).lower()
    if _is_typing_step(step):
        return _is_set_text(event)
    if "long-press" in step_l or "long press" in step_l:
        return isinstance(event, LongTouchEvent) or "long" in event_type
    if any(word in step_l for word in ("swipe", "scroll")):
        return isinstance(event, ScrollEvent) or event_type == "scroll"
    if isinstance(event, ScrollEvent) or event_type == "scroll":
        return any(word in step_l for word in ("swipe", "scroll", "browse"))
    if _is_set_text(event):
        return _is_typing_step(step)
    if _is_bottom_nav(event) and any(word in step_l for word in (
        "bar", "field", "query", "select", "create", "play", "adjust", "save", "edit", "sync", "manage",
    )):
        return False
    if isinstance(event, KeyEvent) or event_type == "key":
        return "back" in step_l
    return True


def _is_typing_step(step):
    step_l = (step or "").lower()
    return any(word in step_l for word in TYPING_WORDS)


def _player_step_intent(feature, remaining):
    """Whether the remaining step is open-player vs a transport control."""
    actions = list(remaining or [])
    step = (actions[0] if actions else "").lower()
    blob = " ".join(actions).lower() + " " + ((feature or {}).get("name") or "").lower()
    if any(word in step for word in ("pause", "resume")):
        return "pause"
    if re.search(r"\bnext\b", step):
        return "next"
    if re.search(r"\bskip\b", step) and any(word in step for word in ("song", "track", "forward")):
        return "next"
    if re.search(r"\b(previous|prev)\b", step):
        return "prev"
    if "shuffle" in step:
        return "shuffle"
    if "repeat" in step:
        return "repeat"
    if any(word in blob for word in (
        "now playing", "currently playing", "mini player", "playing card",
        "full player", "full-screen player", "open the player",
    )):
        return "open"
    return ""


def _widget_player_role(event):
    view = getattr(event, "view", None) or {}
    blob = " ".join((
        _view_text(view.get("resource_id")),
        _view_text(view.get("content_description")),
        _view_text(view.get("text")),
        getattr(event, "nav_label", None) or "",
    )).lower()
    if any(token in blob for token in (
        "play_pause", "playpause", "pause_button", "btn_pause", "action_pause",
    )) or re.search(r"\bpause\b", blob):
        return "pause"
    if any(token in blob for token in ("skip_next", "next_song", "btn_next", "action_next")) or re.search(
        r"\b(next|skip|forward)\b", blob
    ):
        return "next"
    if any(token in blob for token in ("skip_prev", "previous_song", "btn_prev", "action_prev")) or re.search(
        r"\b(previous|prev|rewind)\b", blob
    ):
        return "prev"
    if "shuffle" in blob:
        return "shuffle"
    if "repeat" in blob:
        return "repeat"
    if any(token in blob for token in (
        "mini_player_image", "mini_player_title", "now_playing_bar", "player_bar",
        "playing_bar", "player_title", "miniplayer_title", "miniplayer_image",
        "mini_player", "now_playing", "miniplayer",
    )):
        return "card"
    return ""


def _is_bottom_nav(event):
    extra = (getattr(event, "nav_label", None) or "").lower()
    return "bottom navigation" in extra or "nav tab" in extra


def _step_content_tokens(step):
    tokens = _tokens(step)
    tokens -= {"tap", "click", "open", "select", "icon", "button"}
    return tokens


def _looks_like_add_label(event):
    lower = _visible_label(event).lower()
    return "plus" in lower or "fab" in lower or lower.strip() in ("+", "add", "create")


def _looks_like_fab(event, max_right, max_bottom):
    if _is_set_text(event) or _is_bottom_nav(event):
        return False
    if _looks_like_add_label(event):
        return True
    view = getattr(event, "view", None) or {}
    bounds = view.get("bounds")
    if not bounds or max_right < 80 or max_bottom < 80:
        return False
    left, top = bounds[0]
    right, bottom = bounds[1]
    width = right - left
    height = bottom - top
    if not (36 <= width <= 220 and 36 <= height <= 220):
        return False
    return right >= max_right * 0.72 and bottom >= max_bottom * 0.70 and top < max_bottom * 0.88


def _label_supports_step(event, step):
    if not step:
        return False
    if _is_typing_step(step):
        return _is_set_text(event)
    if _is_set_text(event):
        return False
    content = _step_content_tokens(step)
    visible = _tokens(_visible_label(event))
    if content & visible:
        return True
    step_l = step.lower()
    if any(word in step_l for word in ("create", "new", "add", "plus")) and _looks_like_add_label(event):
        return True
    return False


def _looks_like_error_label(label):
    lower = (label or "").lower()
    return any(token in lower for token in ERROR_TOKENS)


def _looks_like_empty_label(label):
    lower = (label or "").lower()
    if any(token in lower for token in EMPTY_TOKENS):
        return True
    return bool(EMPTY_COUNT_RE.search(lower))


def _looks_like_search_placeholder(label):
    lower = (label or "").lower()
    return any(token in lower for token in SEARCH_PLACEHOLDERS)


def _looks_like_loading_label(label):
    lower = (label or "").lower()
    return any(token in lower for token in LOADING_TOKENS)


def _looks_like_result_row(event):
    if _is_set_text(event) or _is_bottom_nav(event):
        return False
    if isinstance(event, (ScrollEvent, KeyEvent, LongTouchEvent)):
        return False
    if _looks_like_search_placeholder(_event_label(event)):
        return False
    if _looks_like_empty_label(_event_label(event)) or _looks_like_error_label(_event_label(event)):
        return False
    visible = _visible_label(event).strip()
    if not visible or len(visible) > 80:
        return False
    lower = visible.lower()
    cta = {item.lower() for item in CTA_LABELS}
    if lower.strip() in cta or lower.strip() in ("skip", "close", "dismiss"):
        return False
    return True


def _dead_end_text(blob):
    lower = (blob or "").lower()
    return any(token in lower for token in ERROR_TOKENS + EMPTY_TOKENS)


def _picker_extensions(blob):
    blob = blob or ""
    found = []
    mapping = (
        ("csv", (".csv",)),
        ("qif", (".qif",)),
        ("mmb", (".mmb",)),
        ("database", (".mmb", ".db")),
        ("json", (".json",)),
        ("zip", (".zip",)),
        ("plugin", (".zip", ".json", ".hetu")),
        ("mp3", (".mp3", ".m4a", ".flac", ".wav", ".ogg")),
        ("audio", (".mp3", ".m4a", ".flac", ".wav", ".ogg")),
    )
    for needle, exts in mapping:
        if needle in blob:
            found.extend(exts)
    if found:
        return tuple(found)
    return (".csv", ".qif", ".mmb", ".json", ".txt", ".zip")


def _is_file_related_step(blob):
    blob = (blob or "").lower()
    return any(token in blob for token in (
        "file", "database", "import", "export", "csv", "qif", "mmb",
        "save", "open database", "create database", "filename",
    ))
