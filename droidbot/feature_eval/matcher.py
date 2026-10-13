"""Deterministic feature matching over TestCube action traces.

A widget being present in a UI dump is not coverage. Matching only
considers events that TestCube actually sent, plus the destination
state of those events (for outcome steps such as "results appear").
"""

import logging
import re
from math import ceil as _ceil

from .models import (
    STATUS_COVERED,
    STATUS_NOT_COVERED,
    STATUS_PARTIAL,
    FeatureResult,
    better_status,
)

LOGGER = logging.getLogger("TestCube.matcher")

# Step/path matches below this do not count as evidence or PARTIAL credit.
DEFAULT_MIN_STEP_CONFIDENCE = 0.5

# Consecutive steps of one feature must be executed close together. Without
# this a 729-action trace can "cover" a feature by matching step 1 at action 5
# and step 2 at action 600, which is not an execution of the feature.
MAX_STEP_GAP = 20

# Ground-truth step order is written by hand and two adjacent steps are often
# interchangeable ("enter the query" / "tap Search"). Allowing a step to match
# just behind the cursor tolerates that without reopening the whole trace.
STEP_BACKTRACK = 3

# Steps and widget labels both name an operation. "Open the habit list" against
# a button labelled "Add habit" shares the noun but the operations disagree, and
# that disagreement is the only thing distinguishing them for a token matcher.
VERB_GROUPS = [
    {"tap", "click", "press", "touch", "select", "choose", "hit", "long"},
    {"open", "launch", "goto", "navigate", "view", "show", "see", "display"},
    {"create", "new", "add", "make", "insert"},
    {"delete", "remove", "clear", "discard", "trash"},
    {"edit", "change", "modify", "rename", "update"},
    {"save", "store", "keep", "apply"},
    {"cancel", "dismiss", "close", "exit"},
    {"share", "export", "send"},
    {"import", "restore", "load"},
    {"search", "find", "filter", "query"},
    {"archive", "unarchive"},
    {"play", "pause", "stop", "resume"},
    {"enable", "disable", "toggle"},
]

# Surfaces that are definitionally not the app under test. The home screen and
# the status bar are excluded because a tap on the launcher's own "Settings"
# label is not the app's settings. Other packages are kept: a contacts feature
# legitimately hands off to the camera or the dialer, and a permission dialog
# is part of the flow being exercised.
NON_APP_SURFACES = (
    "nexuslauncher",
    "com.android.launcher",
    "com.google.android.launcher",
    "com.android.systemui",
    "com.teslacoilsw.launcher",
)

# At least this share of a widget's own label tokens must be accounted for by
# the step, or the step only clipped a word out of unrelated prose.
MIN_LABEL_COVERAGE = 0.34

# A token used by more than this share of an app's ground-truth features says
# nothing about which feature is which -- "contact" in a contacts app. It is
# measured over the ground truth, which both tools share, and never over a
# trace: "contact" covers 35% of TestCube's actions but 7% of LLMDroid's, so a
# per-trace rule would silently forbid TestCube from matching steps that
# LLMDroid is allowed to match.
UNINFORMATIVE_SHARE = 0.40

# Control labels present on nearly every screen. Such a step may be matched
# once its feature has been located, but may not be what locates it.
GENERIC_CONTROLS = {
    "save", "delete", "remove", "cancel", "close", "exit", "next",
    "previous", "yes", "no", "accept", "allow", "deny", "continue",
    "finish", "dismiss", "edit",
}

# Words that name a widget rather than a feature. "tap the + button" shares
# "button" with every Button in the app, so these are excluded when deciding
# whether a step matched something app-specific.
UI_GENERIC = {
    "button", "tab", "icon", "menu", "item", "items", "field", "label",
    "dialog", "bar", "title", "option", "options", "toggle", "switch",
    "entry", "widget", "header", "row", "cell", "card", "panel", "section",
    "box", "area", "list", "listview", "text", "textview", "layout",
    "activity", "fragment", "window", "popup", "sheet", "drawer", "checkbox",
    "spinner", "slider", "picker", "prompt", "top", "bottom",
    "left", "right", "corner", "center", "value", "values",
}

# Adjectives and quantifiers that carry no app-specific meaning. Counting
# "current" in "view the current time" as a token the trace must contain makes
# an otherwise matchable step unmatchable.
FILLER = {
    "current", "existing", "selected", "desired", "specific", "certain",
    "any", "all", "some", "first", "last", "next", "previous", "same",
    "other", "another", "given", "chosen", "available", "correct", "valid",
    "proper", "whole", "full", "entire", "single", "multiple", "several",
    "various", "one", "two", "its", "their", "your", "each", "every",
    "optionally", "optional", "then", "also", "already", "just", "via",
}

# Verbs describing how a step is performed rather than what it acts on.
STEP_VERBS = {
    "tap", "click", "press", "touch", "select", "choose", "hit",
    "input", "enter", "type", "fill", "write", "set",
    "open", "launch", "goto", "navigate", "view", "show", "see",
    "submit", "send", "confirm", "go", "done", "ok", "apply",
    "create", "new", "add", "make", "back", "return",
    "scroll", "swipe", "long", "tick", "untick", "check", "uncheck",
    "use", "using", "perform", "do", "again",
}



STOPWORDS = {
    "a", "an", "the", "to", "for", "of", "and", "or", "in", "on", "at",
    "with", "from", "user", "can", "a", "app", "application", "screen",
    "page", "the", "be", "is", "are", "that", "this", "it",
}

SYNONYM_GROUPS = [
    {"tap", "click", "press", "touch", "select", "choose", "hit"},
    {"input", "enter", "type", "fill", "set_text", "write", "set"},
    {"search", "find", "query", "lookup"},
    {"submit", "send", "confirm", "go", "done", "ok", "apply"},
    {"open", "launch", "goto", "navigate", "view", "show", "see"},
    {"play", "playback", "playing", "start"},
    {"login", "signin", "sign", "log"},
    {"password", "pass", "pwd"},
    {"email", "mail", "username", "user"},
    {"playlist", "list"},
    {"song", "track", "music", "audio"},
    {"back", "return"},
    {"create", "new", "add", "make"},
    {"result", "results", "appears", "appear", "appeared", "displayed"},
    {"successful", "success", "logged"},
]

OUTCOME_HINTS = {
    "appear", "appears", "appeared", "visible", "shown", "display",
    "displayed", "view", "see", "starts", "playing", "successful",
    "success", "logged", "result", "results", "navigation",
}

EVENT_TYPE_HINTS = {
    "tap": {"touch", "long_touch", "select"},
    "click": {"touch", "long_touch", "select"},
    "press": {"touch", "long_touch", "select", "key"},
    "touch": {"touch", "long_touch"},
    "select": {"touch", "select"},
    "input": {"set_text"},
    "enter": {"set_text"},
    "type": {"set_text"},
    "fill": {"set_text"},
    "scroll": {"scroll", "swipe"},
    "swipe": {"swipe", "scroll"},
    "back": {"key"},
    "key": {"key"},
    "open": {"touch", "intent"},
    "launch": {"intent"},
    "submit": {"touch", "key"},
    "play": {"touch"},
    "start": {"intent", "touch"},
}


class FeatureMatcher(object):
    """Map observed TestCube actions onto ground-truth features.

    Default is a VLM/Gemini semantic judge. Token overlap is ablation-only
    (``matcher_mode=deterministic`` or ``hybrid``). The ``ai`` path never
    falls back to string matching.
    """

    def __init__(self, use_llm=True, llm_matcher=None, readme_text="",
                 min_step_confidence=None, matcher_mode=None):
        if matcher_mode is None:
            matcher_mode = "ai" if use_llm else "deterministic"
        self.matcher_mode = matcher_mode
        self.use_llm = matcher_mode in ("ai", "hybrid")
        self.llm_matcher = llm_matcher
        self.readme_text = readme_text or ""
        if min_step_confidence is None:
            min_step_confidence = DEFAULT_MIN_STEP_CONFIDENCE
        self.min_step_confidence = float(min_step_confidence)
        self.uninformative = set()

    def _learn_uninformative(self, features):
        """Ground-truth words too common in this app to identify a feature.

        Derived from the feature list, which is the same file for both tools,
        so the two are judged by an identical rule. A trace-derived version was
        tried and rejected: token frequencies differ per run, which handed one
        tool matches the other was refused.
        """
        self.uninformative = set()
        items = list(features or [])
        if len(items) < 5:
            return
        seen = {}
        for feature in items:
            words = set()
            words |= tokenize(getattr(feature, "name", "") or "")
            for path in (feature.paths() if hasattr(feature, "paths") else []) or []:
                for step in path:
                    words |= tokenize(step)
            for word in words:
                seen[word] = seen.get(word, 0) + 1
        ceiling = UNINFORMATIVE_SHARE * len(items)
        self.uninformative = set(
            word for word, count in seen.items() if count > ceiling
        )

    def match_all(self, features, trace):
        if self.matcher_mode == "ai" and self.llm_matcher and hasattr(self.llm_matcher, "judge_all"):
            batch = self.llm_matcher.judge_all(features, trace, self.readme_text)
            if batch and len(batch) == len(features):
                results = []
                for feature, verdict in zip(features, batch):
                    result = self._result_from_llm(feature, trace, verdict)
                    if result is None:
                        result = FeatureResult(
                            id=feature.id,
                            name=feature.name,
                            status=STATUS_NOT_COVERED,
                            confidence=0.0,
                            evidence=["LLM coverage judge did not return a verdict."],
                            matcher="vlm",
                        )
                    results.append(result)
                return results
        self._learn_uninformative(features)
        return [self.match_feature(feature, trace) for feature in features]

    def match_feature(self, feature, trace):
        if self.matcher_mode == "ai":
            judged = None
            if self.llm_matcher:
                judged = self._judge_with_vlm(feature, trace)
            if judged is not None:
                return judged
            return FeatureResult(
                id=feature.id,
                name=feature.name,
                status=STATUS_NOT_COVERED,
                confidence=0.0,
                evidence=["LLM coverage judge did not return a verdict."],
                matcher="vlm",
            )
        best = self._match_deterministic(feature, trace)
        if self.matcher_mode == "hybrid" and self.llm_matcher and best.status != STATUS_COVERED:
            llm_result = self.llm_matcher.match(feature, trace, self.readme_text, best)
            if llm_result is not None:
                covering = list(best.test_cases) if best.status == STATUS_COVERED else []
                partial = list(best.test_cases) if best.status == STATUS_PARTIAL else []
                best = self._merge_llm(best, llm_result, covering, partial)
        return best

    def _judge_with_vlm(self, feature, trace):
        llm_result = self.llm_matcher.judge(feature, trace, self.readme_text)
        return self._result_from_llm(feature, trace, llm_result)

    def _result_from_llm(self, feature, trace, llm_result):
        if not llm_result:
            return None
        status = llm_result.get("status")
        if status not in (STATUS_COVERED, STATUS_PARTIAL, STATUS_NOT_COVERED):
            if llm_result.get("covered") is True:
                status = STATUS_COVERED
            elif llm_result.get("covered") is False:
                status = STATUS_NOT_COVERED
            else:
                return None
        evidence = [str(item) for item in (llm_result.get("evidence") or []) if item]
        reasoning = llm_result.get("reasoning")
        if reasoning:
            evidence = [str(reasoning)] + evidence
        try:
            confidence = float(llm_result.get("confidence"))
        except (TypeError, ValueError):
            confidence = 0.7 if status == STATUS_COVERED else 0.4
        ratio = llm_result.get("completion_ratio")
        try:
            ratio = float(ratio)
        except (TypeError, ValueError):
            ratio = None
        if status == STATUS_COVERED:
            ratio = 1.0
        elif ratio is None:
            if status == STATUS_PARTIAL:
                ratio = 0.5
            else:
                ratio = 0.0
        test_cases = []
        if status != STATUS_NOT_COVERED and trace.test_cases:
            test_cases = [item.id for item in trace.test_cases[:1]]
        elif status != STATUS_NOT_COVERED:
            test_cases = ["test_001"]
        return FeatureResult(
            id=feature.id,
            name=feature.name,
            status=status,
            test_cases=test_cases,
            confidence=max(0.0, min(1.0, confidence)),
            evidence=evidence,
            matched_path=None,
            matcher="vlm",
            completion_ratio=max(0.0, min(1.0, ratio)),
        )

    def _match_deterministic(self, feature, trace):
        """Best strict path match for this feature, with where it happened.

        Two passes. The per-session pass says which executed sessions
        independently exercised the feature, which is what the report
        attributes. The whole-trace pass then catches a feature whose steps
        straddle a session boundary: how a trace is cut into sessions is a
        property of the tool, not the app (TestCube's median session is 4
        actions against LLMDroid's 14), so scoring only per session would score
        identical behaviour differently for each tool. Ordering and
        MAX_STEP_GAP carry the "these steps happened together" requirement in a
        tool-neutral way instead.
        """
        from .models import TestCaseTrace
        sessions = list(trace.test_cases or [])
        if not sessions and trace.actions:
            sessions = [TestCaseTrace(id="test_001", actions=list(trace.actions))]
        best = FeatureResult(
            id=feature.id,
            name=feature.name,
            status=STATUS_NOT_COVERED,
            confidence=0.0,
            matcher="deterministic",
        )
        covering = []
        partial = []

        paths = feature.paths()
        for session in sessions:
            session_best = self._best_over_paths(feature, paths, session.actions, session.id)
            if session_best is None:
                continue
            if session_best.status == STATUS_COVERED:
                covering.append(session.id)
                if STATUS_RANK_VALUE(session_best.status) >= STATUS_RANK_VALUE(best.status):
                    best = session_best
            elif session_best.status == STATUS_PARTIAL:
                partial.append(session.id)
                if best.status != STATUS_COVERED:
                    if (best.status != STATUS_PARTIAL
                            or session_best.confidence > best.confidence):
                        best = session_best

        if not any(self.step_checkable(step) for path in paths for step in path):
            best.status = STATUS_NOT_COVERED
            best.completion_ratio = None   # unscorable: excluded from the totals
            best.evidence = [
                "Not scorable from a trace: no step names anything app-specific."
            ]
            best.checkable_steps = 0
            return best

        whole = self._best_over_paths(feature, paths, list(trace.actions or []), "trace")
        if whole is not None and _is_better(whole, best):
            whole.test_cases = self._sessions_for(trace, sessions,
                                                  getattr(whole, "matched_indices", []))
            best = whole
            if whole.status == STATUS_COVERED and not covering:
                covering = list(best.test_cases)
            elif whole.status == STATUS_PARTIAL and not partial:
                partial = list(best.test_cases)

        if covering:
            best.status = STATUS_COVERED
            best.test_cases = unique(covering)
            best.completion_ratio = 1.0
            if best.confidence < 0.8:
                best.confidence = 0.9
        elif partial:
            best.status = STATUS_PARTIAL
            best.test_cases = unique(partial)
            if best.completion_ratio is None:
                best.completion_ratio = 0.5
        else:
            best.status = STATUS_NOT_COVERED
            best.test_cases = []
            best.completion_ratio = 0.0
        return best

    def _best_over_paths(self, feature, paths, actions, label):
        """Highest-ranked match for any of the feature's valid paths."""
        session_best = None
        for path in paths:
            result = self._match_path(feature, path, actions, label)
            if session_best is None or _is_better(result, session_best):
                session_best = result
        return session_best

    def _sessions_for(self, trace, sessions, indices):
        """Session ids holding the actions a whole-trace match used."""
        if not indices:
            return []
        owner = {}
        for session in sessions:
            for item in session.actions or []:
                owner[id(item)] = session.id
        actions = list(trace.actions or [])
        found = []
        for index in indices:
            if 0 <= index < len(actions):
                name = owner.get(id(actions[index]))
                if name and name not in found:
                    found.append(name)
        return found

    def _match_path(self, feature, path, actions, test_case_id):
        if not path:
            return FeatureResult(
                id=feature.id,
                name=feature.name,
                status=STATUS_NOT_COVERED,
                test_cases=[],
                confidence=0.0,
                completion_ratio=0.0,
            )
        used = set()
        matched_steps = []
        evidence = []
        confidences = []
        # Steps must be found in order and close together. Scanning the whole
        # trace for each step independently, as this did before, let step 3
        # match an action that ran before step 1 and let the steps of one
        # feature be spread over hundreds of unrelated actions.
        cursor = -1
        for step in path:
            best = None
            if cursor < 0 and self._weak_anchor(step):
                # "Tap Save" must not be what locates a feature in the trace:
                # with no earlier step matched it would scan the whole run and
                # settle on any Save button, on any screen.
                continue
            if cursor < 0:
                start, limit = 0, len(actions)
            else:
                start = max(0, cursor - STEP_BACKTRACK + 1)
                limit = min(len(actions), cursor + 1 + MAX_STEP_GAP)
            for index in range(start, limit):
                if index in used:
                    continue
                action = actions[index]
                matched, confidence, why = self.step_matches(step, action)
                if not matched:
                    continue
                if confidence < self.min_step_confidence:
                    LOGGER.info(
                        "weak step match skipped: %s vs %s (confidence=%.2f < %.2f)"
                        % (step, action.summary(), confidence, self.min_step_confidence)
                    )
                    continue
                if best is None or confidence > best[0]:
                    best = (confidence, index, why, action)
            if best is None:
                continue
            confidence, index, why, action = best
            used.add(index)
            cursor = max(cursor, index)
            matched_steps.append(step)
            confidences.append(confidence)
            evidence.append("%s: %s (%s)" % (step, action.summary(), why))

        checkable = [step for step in path if self.step_checkable(step)]
        denominator = len(checkable)
        if denominator and len(matched_steps) >= denominator:
            status = STATUS_COVERED
        elif len(matched_steps) > 0:
            status = STATUS_PARTIAL
        else:
            status = STATUS_NOT_COVERED

        confidence = 0.0
        if confidences:
            confidence = sum(confidences) / float(max(1, denominator))
            if status == STATUS_COVERED:
                confidence = max(confidence, 0.85)
        result = FeatureResult(
            id=feature.id,
            name=feature.name,
            status=status,
            test_cases=[test_case_id] if status != STATUS_NOT_COVERED else [],
            confidence=round(confidence, 4),
            evidence=evidence,
            matched_path=path if status == STATUS_COVERED else matched_steps or None,
            matcher="deterministic",
            completion_ratio=(
                1.0 if status == STATUS_COVERED
                else (float(len(matched_steps)) / float(denominator) if denominator else 0.0)
            ),
        )
        result.checkable_steps = denominator
        result.total_steps = len(path)
        result.matched_indices = sorted(used)
        return result

    def _distinctive(self, content):
        """What a step is about: not how it is done, not the widget it uses.

        The ground-truth frequency filter is a tie-breaker, not a censor. If
        dropping those words would leave the step with nothing to match on, the
        words are kept, so a step never becomes unmatchable just because its
        subject is what the app is about.
        """
        core = set(content) - STEP_VERBS - UI_GENERIC - FILLER
        trimmed = core - self.uninformative
        return trimmed or core

    def _weak_anchor(self, step):
        """True when a step names only ubiquitous controls."""
        distinctive = self._distinctive(content_tokens(tokenize(step)))
        return bool(distinctive) and distinctive <= GENERIC_CONTROLS

    def step_checkable(self, expected):
        """Can a trace evidence this step at all?

        "tap the + button" contains no app-specific word: every Button in the
        app matches it equally, so no trace can confirm or deny it. Such a step
        is excluded from the denominator rather than counted as a failure,
        otherwise one unwritable step makes a whole feature uncoverable and
        every tool scores zero. This reads the ground-truth wording only -- not
        the trace -- so the set of excluded steps is the same for both tools.
        """
        tokens = tokenize(expected)
        if not tokens:
            return False
        content = content_tokens(tokens)
        if is_outcome_step(tokens):
            return bool(content - OUTCOME_HINTS - STEP_VERBS - UI_GENERIC - FILLER)
        return bool(content - STEP_VERBS - UI_GENERIC - FILLER)

    def step_matches(self, expected, action):
        """Best match for the step, trying each alternative it offers.

        "Open Settings (or the overflow menu)" is one step with two ways to
        perform it. Scored as a single bag of words it demanded "settings" and
        "overflow" together and so matched neither.
        """
        best = (False, 0.0, "no alternative matched")
        for alternative in _alternatives(expected):
            matched, confidence, why = self._step_matches_one(alternative, action)
            if matched and confidence > best[1]:
                best = (matched, confidence, why)
        return best

    def _step_matches_one(self, expected, action):
        expected_tokens = tokenize(expected)
        if not expected_tokens:
            return False, 0.0, "empty expected step"

        if _on_non_app_surface(action):
            return False, 0.0, "action on the home screen or status bar"

        if is_outcome_step(expected_tokens):
            return self._match_outcome(expected_tokens, action)

        type_ok = event_type_compatible(expected_tokens, action.event_type, action.key_name)
        if not type_ok:
            return False, 0.0, "event type mismatch"

        # content_blob, not token_blob: see ObservedAction.content_blob for why
        # scoring against event_str/resource-id metadata produced matches like
        # "tap the + button" -> touch Button "OK".
        observed_tokens = tokenize(action.content_blob())
        content = content_tokens(expected_tokens)
        if not content:
            content = expected_tokens
        expanded_observed = comparable(observed_tokens)
        matched = set()
        for token in content:
            options = comparable({token})
            if options & expanded_observed:
                matched.add(token)

        # What the step is actually about: not how it is performed (STEP_VERBS),
        # not the widget it happens to use (UI_GENERIC), and not a token this
        # trace repeats everywhere (self.uninformative).
        distinctive = self._distinctive(content)
        if distinctive:
            # The visible label carries the match when the widget has one. A
            # resource id is an internal name and matching only there let
            # "Open the task editor" match a button reading "SAVE" because its
            # id happened to be editor_action_save.
            visible = tokenize("%s %s" % (action.view_text or "",
                                          action.content_description or ""))
            distinctive_matched = set()
            for token in distinctive:
                options = comparable({token})
                hits = [o for o in observed_tokens if options & comparable({o})]
                hits = [o for o in hits if agrees_in_number(token, o)]
                if not hits:
                    continue
                if visible and not any(o in visible for o in hits):
                    continue
                distinctive_matched.add(token)
            need = _required_hits(len(distinctive))
            if len(distinctive_matched) < need:
                return False, 0.0, "missing distinctive tokens"
            # The step must also account for a fair share of the widget's own
            # label, which is what rules out matching one word of a paragraph.
            # The label keeps its filler words -- discounting "first" let "Open
            # the contact" match an EditText named "First name" -- but loses the
            # app's own subject words, which otherwise pad every widget's id.
            # "contact" sits in 68% of this app's features and in the id of
            # every field, so counting it made contact_surname look half
            # explained by a step that had only said "contact".
            label = tokenize(action.label_blob()) - STOPWORDS - self.uninformative
            if label:
                expanded_expected = comparable(content)
                explained = set(t for t in label if comparable({t}) & expanded_expected)
                if float(len(explained)) / float(len(label)) < MIN_LABEL_COVERAGE:
                    return False, 0.0, "step explains only %d/%d label tokens" % (
                        len(explained), len(label))
                conflict = _verb_conflict(content, label)
                if conflict:
                    return False, 0.0, "operation mismatch: step says %s, widget says %s" % conflict

            ratio = float(len(distinctive_matched)) / float(len(distinctive))
            why = "tokens=%s" % ",".join(sorted(distinctive_matched))
            return True, min(1.0, 0.7 + 0.3 * ratio), why

        # No app-specific words at all ("tap OK", "tap the + button"). Matching
        # the widget class was tried here and rejected: tapping some Button is
        # not evidence that the "+" button was tapped. Such a step is reported
        # unmatched rather than guessed at, which costs both tools equally.
        if matched:
            return False, 0.45, "only generic tokens: %s" % ",".join(sorted(matched))
        return False, 0.0, "no token overlap"

    def _match_outcome(self, expected_tokens, action):
        """An outcome step ("the results appear") needs the thing on screen.

        state_changed used to rescue any weak outcome, so every navigating
        action satisfied almost every outcome step; and the observed text
        included the action metadata, so "the full-screen clock is displayed"
        matched an am-start intent on the token "clock". The destination screen
        text is the only admissible evidence here.
        """
        screen = tokenize(" ".join(action.stop_texts[:60]))
        observed = screen | tokenize(action.content_blob())
        expanded_observed = comparable(observed)
        content = content_tokens(expected_tokens)
        core = self._distinctive(content - OUTCOME_HINTS)
        if not core:
            # Nothing app-specific to look for; a state change is all that can
            # be checked, which is too weak to count as covering a step.
            return False, 0.0, "outcome has no checkable content"
        core_matched = set(
            token for token in core
            if comparable({token}) & expanded_observed
        )
        need = _required_hits(len(core))
        if len(core_matched) < need:
            return False, 0.0, "outcome not observed on screen"
        success_tokens = {"successful", "success", "logged"}
        if expected_tokens & success_tokens and not action.state_changed:
            return False, 0.0, "success outcome without state change"
        ratio = float(len(core_matched)) / float(len(core))
        return True, min(1.0, 0.6 + 0.4 * ratio), "outcome tokens=%s" % ",".join(
            sorted(core_matched)
        )

    def _merge_llm(self, deterministic, llm_result, covering, partial):
        status = llm_result.get("status")
        if status not in (STATUS_COVERED, STATUS_PARTIAL, STATUS_NOT_COVERED):
            if llm_result.get("covered") is True:
                status = STATUS_COVERED
            elif llm_result.get("covered") is False:
                status = STATUS_NOT_COVERED
            else:
                status = deterministic.status

        # LLM may promote PARTIAL/NOT_COVERED, but cannot demote COVERED.
        merged_status = better_status(deterministic.status, status)
        evidence = list(deterministic.evidence)
        for item in llm_result.get("evidence") or []:
            if item and item not in evidence:
                evidence.append(str(item))
        confidence = llm_result.get("confidence")
        try:
            confidence = float(confidence)
        except (TypeError, ValueError):
            confidence = deterministic.confidence
        if merged_status == STATUS_COVERED:
            test_cases = unique(covering or deterministic.test_cases)
        elif merged_status == STATUS_PARTIAL:
            test_cases = unique(deterministic.test_cases or partial)
        else:
            test_cases = []
        matcher_name = deterministic.matcher
        if merged_status != deterministic.status:
            matcher_name = "llm"
        elif deterministic.matcher != "llm":
            matcher_name = deterministic.matcher + "+llm"
        return FeatureResult(
            id=deterministic.id,
            name=deterministic.name,
            status=merged_status,
            test_cases=test_cases,
            confidence=max(deterministic.confidence, confidence),
            evidence=evidence,
            matched_path=deterministic.matched_path,
            matcher=matcher_name,
        )


def _on_non_app_surface(action):
    """True when the action was performed on the launcher or the status bar."""
    for activity in (action.start_activity, action.stop_activity):
        if not activity:
            continue
        lowered = activity.lower()
        if any(surface in lowered for surface in NON_APP_SURFACES):
            return True
    return False


_OR_SPLIT = re.compile(r"\s+or\s+", re.I)


def _alternatives(step):
    """A step's interchangeable forms, split on "or".

    Brackets are opened out first: in "Open Settings (or the overflow menu)"
    the "or" is glued to a parenthesis, so the step read as one bag of words
    demanded "settings" and "overflow" together.
    """
    opened = re.sub(r"[()\[\]]", " ", step or "")
    parts = [part.strip() for part in _OR_SPLIT.split(opened) if part.strip()]
    if len(parts) < 2:
        return [step]
    # The full wording stays in the list: "Pause, resume, reset or delete a
    # timer" splits into fragments that each lose the noun.
    return [step] + parts


def _required_hits(total):
    """How many of a step's key words the action must carry.

    Capped, because a descriptive step such as "enable Touch to capture;
    tapping anywhere on the preview takes a photo" has seven key words and no
    single widget will ever carry five of them.
    """
    return max(1, min(int(_ceil(0.6 * total)), 3))


def _verb_conflict(step_tokens, label_tokens):
    """Operations named by the step and by the widget that cannot be the same.

    Returns a (step_verb, label_verb) pair, or None when they are compatible.
    Verbs in no known group, or absent from either side, never conflict.
    """
    def groups_for(tokens):
        found = []
        for index, group in enumerate(VERB_GROUPS):
            if tokens & group:
                found.append(index)
        return found

    step_groups = groups_for(step_tokens)
    label_groups = groups_for(label_tokens)
    if not step_groups or not label_groups:
        return None
    if set(step_groups) & set(label_groups):
        return None
    # Tapping is how nearly every step is performed, so it never conflicts.
    if step_groups == [0] or label_groups == [0]:
        return None
    step_verb = sorted(step_tokens & VERB_GROUPS[step_groups[0]])[0]
    label_verb = sorted(label_tokens & VERB_GROUPS[label_groups[0]])[0]
    return step_verb, label_verb


def _is_better(candidate, incumbent):
    """Higher status wins; equal status breaks on confidence."""
    if incumbent is None:
        return True
    rank = STATUS_RANK_VALUE(candidate.status) - STATUS_RANK_VALUE(incumbent.status)
    if rank != 0:
        return rank > 0
    return candidate.confidence > incumbent.confidence


def STATUS_RANK_VALUE(status):
    from .models import STATUS_RANK
    return STATUS_RANK.get(status, 0)


def unique(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


_CAMEL = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")


def tokenize(text):
    if not text:
        return set()
    # Split camelCase before lowercasing: resource ids such as
    # actionCreateHabit otherwise survive as one unmatchable token.
    text = _CAMEL.sub(" ", str(text))
    text = text.lower().replace("_", " ")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    tokens = set()
    for raw in text.split():
        if raw in STOPWORDS:
            continue
        tokens.add(raw)
        # Split resource-id style camelCase leftovers already lowercased.
        if len(raw) > 3:
            tokens.add(raw)
    return tokens


_BRITISH = (
    ("isation", "ization"), ("isational", "izational"), ("ise", "ize"),
    ("ising", "izing"), ("ised", "ized"), ("iser", "izer"),
    ("our", "or"), ("ours", "ors"), ("oured", "ored"), ("ouring", "oring"),
    ("logue", "log"), ("ogramme", "ogram"), ("yse", "yze"),
)


def stem(token):
    """Fold spelling and inflection so ground truth and UI labels can meet.

    Ground truth is written in British English by hand while apps ship
    American identifiers: "Customise colours" has to reach
    settings_color_customization_holder, and "contacts" has to reach
    "contact". Deliberately crude -- it only has to make these two
    vocabularies comparable, and it is applied to both sides equally.
    """
    word = token
    for british, american in _BRITISH:
        if word.endswith(british):
            word = word[: -len(british)] + american
            break
    for suffix in ("ization", "isation"):
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            word = word[: -len(suffix)] + "ize"
            break
    if word.endswith("ies") and len(word) > 4:
        word = word[:-3] + "y"
    elif word.endswith("ses") and len(word) > 4:
        word = word[:-2]
    elif word.endswith("s") and not word.endswith("ss") and len(word) > 3:
        word = word[:-1]
    if word.endswith("ing") and len(word) > 6:
        word = word[:-3]
    elif word.endswith("ed") and len(word) > 5:
        word = word[:-2]
    if word.endswith("e") and len(word) > 4:
        word = word[:-1]
    return word


def _plural(token):
    """Crude number test, enough to tell "note" from "notes"."""
    return bool(token) and token.endswith("s") and not token.endswith("ss") and len(token) > 3


def agrees_in_number(expected, observed):
    """True when two tokens are the same word in the same grammatical number.

    Stemming folds "notes" onto "note", which is wanted for spelling and
    inflection but not here: a step that says "Open a note" matching a list
    header labelled "Notes" is the collection, not an instance of it. That one
    pattern produced 7 of the 22 false positives found by hand across both
    tools.
    """
    if expected == observed:
        return True
    return _plural(expected) == _plural(observed)


def stems(tokens):
    return set(stem(token) for token in tokens)


def content_tokens(tokens):
    return set(tokens) - STOPWORDS


def comparable(tokens):
    """Synonym-expanded and stemmed, the form both sides are compared in."""
    return stems(expand_synonyms(tokens))


def expand_synonyms(tokens):
    expanded = set(tokens)
    for token in list(tokens):
        for group in SYNONYM_GROUPS:
            if token in group:
                expanded |= group
    return expanded


def is_outcome_step(tokens):
    if tokens & OUTCOME_HINTS:
        action_verbs = {"tap", "click", "press", "touch", "input", "enter", "type", "fill"}
        if not (tokens & action_verbs):
            return True
    return False


def event_type_compatible(expected_tokens, event_type, key_name):
    event_type = (event_type or "").lower()
    # "long-press the habit" is a different gesture from tapping it, and the
    # generic press hint accepted both -- so an ordinary touch on a label
    # reading "Habits" satisfied a step about long-pressing a habit.
    if expected_tokens & {"long", "hold", "longpress"} and (
            expected_tokens & {"press", "touch", "tap", "click", "hold"}):
        return event_type == "long_touch"
    allowed = None
    for token in expected_tokens:
        hinted = EVENT_TYPE_HINTS.get(token)
        if hinted:
            allowed = hinted if allowed is None else allowed | hinted
    if allowed is None:
        return True
    if event_type in allowed:
        return True
    if event_type == "key" and key_name and key_name.lower() in expected_tokens:
        return True
    return False
