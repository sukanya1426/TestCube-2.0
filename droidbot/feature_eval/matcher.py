"""Deterministic feature matching over TestCube action traces.

A widget being present in a UI dump is not coverage. Matching only
considers events that TestCube actually sent, plus the destination
state of those events (for outcome steps such as "results appear").
"""

import logging
import re

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
        sessions = list(trace.test_cases or [])
        if not sessions and trace.actions:
            from .models import TestCaseTrace
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
            session_best = None
            for path in paths:
                result = self._match_path(feature, path, session.actions, session.id)
                if session_best is None or STATUS_RANK_VALUE(result.status) > STATUS_RANK_VALUE(session_best.status):
                    session_best = result
                elif (session_best and result.status == session_best.status
                      and result.confidence > session_best.confidence):
                    session_best = result
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
        for step in path:
            best = None
            for index, action in enumerate(actions):
                if index in used:
                    continue
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
            matched_steps.append(step)
            confidences.append(confidence)
            evidence.append("%s: %s (%s)" % (step, action.summary(), why))

        if len(matched_steps) == len(path):
            status = STATUS_COVERED
        elif len(matched_steps) > 0:
            status = STATUS_PARTIAL
        else:
            status = STATUS_NOT_COVERED

        confidence = 0.0
        if confidences:
            confidence = sum(confidences) / float(len(path))
            if status == STATUS_COVERED:
                confidence = max(confidence, 0.85)
        return FeatureResult(
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
                else (float(len(matched_steps)) / float(len(path)) if path else 0.0)
            ),
        )

    def step_matches(self, expected, action):
        expected_tokens = tokenize(expected)
        if not expected_tokens:
            return False, 0.0, "empty expected step"

        if is_outcome_step(expected_tokens):
            return self._match_outcome(expected_tokens, action)

        type_ok = event_type_compatible(expected_tokens, action.event_type, action.key_name)
        if not type_ok:
            return False, 0.0, "event type mismatch"

        observed_tokens = tokenize(action.token_blob())
        content = content_tokens(expected_tokens)
        if not content:
            content = expected_tokens
        expanded_observed = expand_synonyms(observed_tokens)
        matched = set()
        for token in content:
            options = expand_synonyms({token})
            if options & expanded_observed:
                matched.add(token)
        if not matched:
            return False, 0.0, "no token overlap"

        ratio = float(len(matched)) / float(len(content))
        # Distinctive nouns (search, playlist, email) matter more than
        # generic verbs. Require either all content tokens or a strong
        # majority that includes a non-verb.
        distinctive = content - {
            "tap", "click", "press", "touch", "open", "enter", "input",
            "type", "fill", "select", "view", "see", "go", "use",
        }
        distinctive_ok = True
        if distinctive:
            distinctive_matched = set()
            for token in distinctive:
                if expand_synonyms({token}) & expanded_observed:
                    distinctive_matched.add(token)
            distinctive_ok = len(distinctive_matched) >= max(1, int(round(0.5 * len(distinctive))))
            if not distinctive_ok:
                return False, 0.0, "missing distinctive tokens"

        if ratio < 0.5:
            return False, 0.0, "weak overlap"
        why = "tokens=%s" % ",".join(sorted(matched))
        return True, min(1.0, 0.7 + 0.3 * ratio), why

    def _match_outcome(self, expected_tokens, action):
        observed = tokenize(action.token_blob() + " " + " ".join(action.stop_texts[:40]))
        if action.state_changed:
            observed.add("changed")
            observed.add("navigation")
        expanded_observed = expand_synonyms(observed)
        content = content_tokens(expected_tokens)
        matched = set()
        for token in content:
            if expand_synonyms({token}) & expanded_observed:
                matched.add(token)
        if action.state_changed and (content & OUTCOME_HINTS or not content):
            matched.add("changed")
        if not matched:
            return False, 0.0, "outcome not observed"
        success_tokens = {"successful", "success", "logged"}
        if expected_tokens & success_tokens and not action.state_changed:
            return False, 0.0, "success outcome without state change"
        core = content - OUTCOME_HINTS
        if core:
            core_hit = False
            for token in core:
                if expand_synonyms({token}) & expanded_observed:
                    core_hit = True
                    break
            if not core_hit and not action.state_changed:
                return False, 0.0, "outcome missing core tokens"
        ratio = float(len(matched)) / float(max(1, len(content)))
        if ratio < 0.5 and not action.state_changed:
            return False, 0.0, "outcome weak"
        return True, min(1.0, 0.6 + 0.4 * ratio), "outcome tokens=%s" % ",".join(sorted(matched))

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


def STATUS_RANK_VALUE(status):
    from .models import STATUS_RANK
    return STATUS_RANK.get(status, 0)


def unique(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def tokenize(text):
    if not text:
        return set()
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


def content_tokens(tokens):
    return set(tokens) - STOPWORDS


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
