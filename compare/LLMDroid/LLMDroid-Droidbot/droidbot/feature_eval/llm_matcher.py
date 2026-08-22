"""VLM/Gemini coverage judge.

The verdict is a semantic judgment of whether the executed GUI trace
actually carried out a feature. Token overlap is not the decision.
"""

import json
import os
import re

from .models import STATUS_COVERED, STATUS_NOT_COVERED, STATUS_PARTIAL


class LLMMatcher(object):
    def __init__(self, enabled=True, max_actions=40, max_screenshots=0,
                 journal_features=None, exploration_bank=None):
        self.enabled = enabled
        self.max_actions = max_actions
        self.max_screenshots = max_screenshots
        self.journal_features = journal_features or []
        self.exploration_bank = exploration_bank or []

    def judge(self, feature, trace, readme_text=""):
        """Return a parsed verdict dict, or None if the model call failed."""
        if not self.enabled:
            return None
        prompt = self._build_prompt(feature, trace, readme_text)
        last_raw = None
        for _attempt in range(2):
            raw = self._complete(prompt)
            if not raw:
                continue
            last_raw = raw
            parsed = extract_json(raw)
            if parsed:
                parsed["matcher"] = "vlm"
                return parsed
        if last_raw:
            print("Coverage VLM/Gemini judge returned unparseable JSON")
        return None

    def match(self, feature, trace, readme_text, deterministic_result=None):
        """Backward-compatible alias used by the old hybrid path."""
        return self.judge(feature, trace, readme_text)

    def judge_all(self, features, trace, readme_text=""):
        """Score many features in a few LLM calls instead of one call each."""
        if not self.enabled or not features:
            return []
        chunk_size = 7
        verdicts = []
        for start in range(0, len(features), chunk_size):
            chunk = features[start:start + chunk_size]
            print(
                "Coverage judge batch %d-%d / %d"
                % (start + 1, start + len(chunk), len(features)),
                flush=True,
            )
            parsed = self._judge_chunk(chunk, trace, readme_text)
            by_id = {}
            for item in parsed or []:
                fid = str(item.get("feature_id") or item.get("id") or "")
                if fid:
                    by_id[fid] = item
            for feature in chunk:
                item = by_id.get(feature.id)
                if item:
                    item["matcher"] = "vlm"
                    verdicts.append(item)
                else:
                    verdicts.append({
                        "feature_id": feature.id,
                        "status": STATUS_NOT_COVERED,
                        "confidence": 0.0,
                        "reasoning": "LLM batch omitted this feature.",
                        "evidence": [],
                        "matcher": "vlm",
                    })
        return verdicts

    def _judge_chunk(self, features, trace, readme_text):
        prompt = self._build_batch_prompt(features, trace, readme_text)
        raw = self._complete(prompt)
        parsed = extract_json_list(raw)
        if parsed:
            return parsed
        return None

    def _complete(self, prompt):
        try:
            from droidbot.GeminiAI import GeminiAi
            if hasattr(GeminiAi, "generate_content"):
                return GeminiAi.generate_content(prompt, timeout=60)
        except Exception as exc:
            print("Coverage VLM/Gemini judge failed: %s" % exc)
            return None
        return None

    def _build_batch_prompt(self, features, trace, readme_text):
        cards = []
        for feature in features:
            cards.append(self._feature_card(feature, trace))
        return (
            "You are TestCube's coverage judge. Score EVERY feature below.\n"
            "Do NOT use string/token overlap. Gold step order is not required.\n"
            "COVERED = the capability was carried out end to end (equivalent steps OK).\n"
            "PARTIAL = some necessary steps happened; keep partial, do not drop it.\n"
            "NOT_COVERED = never meaningfully attempted.\n"
            "Emit ONLY a JSON array, one compact object per feature, no extra prose:\n"
            '[{"feature_id":"F001","status":"covered|partial|not_covered",'
            '"confidence":0.8,"completion_ratio":0.0,'
            '"reasoning":"short","evidence":["one action"]}]\n'
            "completion_ratio is the fraction of the gold capability that happened (0-1).\n"
            "Keep reasoning under 12 words and evidence to one short action.\n\n"
            "Features:\n%s\n"
        ) % "\n\n".join(cards)

    def _feature_card(self, feature, trace):
        gold = []
        for path in feature.paths()[:1]:
            gold = [_clip(step, 80) for step in path[:6]]
        observed = [_clip(self._short_observed(line), 120) for line in self._observed_lines(feature, trace)[:8]]
        item = _closest_journal_feature(feature, self.journal_features)
        live = "none"
        if item:
            completed = "; ".join((item.get("completed_actions") or [])[:4])
            live = "%s%s" % (item.get("status") or "?", (" | " + completed) if completed else "")
            credited = item.get("credited_from") or []
            if credited:
                live += " | credited_from=%s" % ",".join(credited)
        return (
            "ID: %s\nName: %s\nGold: %s\nJournal: %s\nActions:\n%s"
            % (
                feature.id,
                feature.name,
                "; ".join(gold) or "(none)",
                live,
                "\n".join(observed) or "(none)",
            )
        )

    def _short_observed(self, line):
        line = str(line or "")
        match = re.search(r"\(([^()]*/[^()]+)\)", line)
        if match:
            kind = "touch"
            if line.lower().startswith("- "):
                kind = line[2:].split(" ", 1)[0]
            return "%s %s" % (kind, match.group(1))
        return _clip(line, 120)

    def _build_prompt(self, feature, trace, readme_text):
        expected_paths = feature.paths()
        path_text = []
        for index, path in enumerate(expected_paths, start=1):
            path_text.append("Path %d:" % index)
            for step_i, step in enumerate(path, start=1):
                path_text.append("  %d. %s" % (step_i, step))

        observed_lines = self._observed_lines(feature, trace)
        if not observed_lines:
            observed_lines.append("(no executed actions)")

        typed = [
            self._action_line(action)
            for action in (trace.actions or [])
            if (action.text_input or "").strip()
        ]
        typed_block = "\n".join(typed[:10]) if typed else "(no set_text values in this run)"

        journal_block = self._journal_block(feature)
        if len(journal_block) > 1600:
            journal_block = journal_block[:1600] + "\n...[truncated]..."
        readme = (readme_text or "").strip()
        if len(readme) > 1500:
            readme = readme[:1500] + "\n...[truncated]..."

        return (
            "You are TestCube's coverage judge for one Android GUI feature.\n"
            "Decide whether the executed test trace actually carried out this "
            "feature. Do NOT score by string or token overlap. Infer user intent "
            "from what was tapped, typed, and what the resulting screen showed.\n\n"
            "First reason in 2-4 sentences. Then emit ONLY JSON:\n"
            "{\n"
            '  "feature_id": "%s",\n'
            '  "status": "covered" | "partial" | "not_covered",\n'
            '  "confidence": 0.0,\n'
            '  "completion_ratio": 0.0,\n'
            '  "reasoning": "short justification",\n'
            '  "evidence": ["concrete executed actions or screen outcomes"]\n'
            "}\n\n"
            "Definitions:\n"
            "- covered: the user-facing capability was carried out end to end "
            "(equivalent steps count; labels need not match the gold wording; "
            "gold steps need NOT occur in the listed order).\n"
            "- partial: some necessary steps happened, even if later gold steps "
            "are missing or happened out of order. Keep PARTIAL. Do not convert "
            "it to not_covered just because the path is incomplete or shuffled.\n"
            "- not_covered: the run never meaningfully attempted this feature. "
            "Visiting a related screen or tapping an unrelated unlabeled widget "
            "is not coverage.\n"
            "Do NOT score by string/token overlap or require exact step order.\n"
            "Score the feature-specific actions listed below. If those actions "
            "clearly start or complete the capability (for example tapping "
            "Create Database during setup), that is at least partial even when "
            "later gold steps are missing. Unrelated screens from other features "
            "in the same run are not a reason to say not_covered.\n"
            "A widget merely appearing in a UI dump is not coverage.\n"
            "If screenshots are attached, use them as extra evidence of the "
            "destination screen after relevant actions.\n\n"
            "Application README (context only):\n%s\n\n"
            "Ground-truth feature:\n"
            "ID: %s\n"
            "Name: %s\n"
            "Description: %s\n\n"
            "Expected behavior (guidance only; order is not required):\n%s\n\n"
            "Typed text in this run:\n%s\n\n"
            "Live tester journal (may be incomplete; do not copy its status):\n%s\n\n"
            "Observed executed actions (chronological, already sent to the device):\n%s\n"
        ) % (
            feature.id,
            readme or "(none)",
            feature.id,
            feature.name,
            feature.description or "(none)",
            "\n".join(path_text) if path_text else "(none)",
            typed_block,
            journal_block,
            "\n".join(observed_lines),
        )

    def _action_line(self, action):
        dest = _short(action.stop_activity)
        texts = [item for item in (action.stop_texts or [])[:8] if item]
        dest_txt = _clip("; ".join(texts), 80)
        extra = []
        if dest:
            extra.append("activity=%s" % dest)
        if dest_txt:
            extra.append("screen=%s" % dest_txt)
        if action.state_changed:
            extra.append("state_changed")
        suffix = (" | " + " ".join(extra)) if extra else ""
        return "%s. [%s] %s%s" % (
            action.index + 1,
            action.test_case,
            action.summary(),
            suffix,
        )

    def _journal_block(self, feature):
        item = _closest_journal_feature(feature, self.journal_features)
        if not item:
            return "(none)"
        lines = [
            "Closest journal feature: %s %s (live status=%s, source=%s)"
            % (
                item.get("id") or "?",
                item.get("name") or "?",
                item.get("status") or "?",
                item.get("source") or "?",
            )
        ]
        completed = item.get("completed_actions") or []
        if completed:
            lines.append("Completed steps claimed: %s" % "; ".join(completed[:8]))
        remaining = item.get("remaining_actions") or []
        if remaining:
            lines.append("Remaining steps claimed: %s" % "; ".join(remaining[:8]))
        credited = item.get("credited_from") or []
        if credited:
            lines.append("Later features that completed leftover steps: %s" % ", ".join(credited))
        for step in (item.get("credited_steps") or [])[:6]:
            lines.append(
                "- credited %s via %s"
                % (step.get("matched_step") or "", step.get("from_feature") or "?")
            )
        for step in (item.get("steps") or [])[-6:]:
            lines.append(
                "- %s %s text=%s"
                % (
                    step.get("event_type") or step.get("decision") or "act",
                    step.get("event") or step.get("reason") or "",
                    step.get("text") or "",
                )
            )
        return "\n".join(lines)

    def _observed_lines(self, feature, trace):
        item = _closest_journal_feature(feature, self.journal_features)
        lines = []
        if item:
            for step in (item.get("steps") or [])[: self.max_actions]:
                event = step.get("event") or step.get("reason") or ""
                kind = step.get("event_type") or step.get("decision") or "act"
                text = step.get("text") or ""
                line = "- %s %s" % (kind, event)
                if text:
                    line += " text=%s" % text
                lines.append(line)
            for step in (item.get("credited_steps") or [])[:6]:
                lines.append(
                    "- credited %s via %s: %s"
                    % (
                        step.get("matched_step") or "",
                        step.get("from_feature") or "?",
                        step.get("event") or "",
                    )
                )
            later = 0
            fid = item.get("id")
            for entry in self.exploration_bank or []:
                if later >= 6:
                    break
                if not entry.get("feature_id") or entry.get("feature_id") == fid:
                    continue
                blob = entry.get("matched_step") or entry.get("event") or ""
                if not blob:
                    continue
                lines.append("- later %s: %s" % (entry.get("feature_id"), blob))
                later += 1
            if lines:
                return lines[: self.max_actions]
        return [self._action_line(action) for action in self._select_actions(feature, trace)]

    def _select_actions(self, feature, trace):
        actions = list(trace.actions or [])
        keywords = _feature_keywords(feature)
        selected = []
        for action in actions:
            blob = action.token_blob().lower()
            if action.text_input:
                selected.append(action)
                continue
            if any(word in blob for word in keywords):
                selected.append(action)
        if selected:
            return selected[: self.max_actions]
        if len(actions) <= self.max_actions:
            return actions
        head = actions[: self.max_actions // 2]
        tail = actions[-(self.max_actions - len(head)):]
        seen = set()
        merged = []
        for action in head + tail:
            if action.index in seen:
                continue
            seen.add(action.index)
            merged.append(action)
        return merged

    def _pick_screenshots(self, feature, trace):
        keywords = _feature_keywords(feature)
        ranked = []
        for action in trace.actions or []:
            path = action.screenshot
            if not path or not os.path.isfile(path):
                continue
            blob = action.token_blob().lower()
            score = sum(1 for word in keywords if word in blob)
            if action.text_input:
                score += 2
            ranked.append((score, action.index, path))
        ranked.sort(reverse=True)
        picked = []
        seen = set()
        for score, _index, path in ranked:
            if path in seen:
                continue
            if score <= 0 and picked:
                continue
            seen.add(path)
            picked.append(path)
            if len(picked) >= self.max_screenshots:
                break
        return picked


def _feature_keywords(feature):
    keywords = set()
    for word in feature.keywords or []:
        keywords.update(_tokens(word))
    keywords.update(_tokens(feature.name))
    keywords.update(_tokens(feature.description))
    for path in feature.paths():
        for step in path:
            keywords.update(_tokens(step))
    return {word for word in keywords if len(word) > 2}


def _closest_journal_feature(feature, journal_features):
    if not journal_features:
        return None
    try:
        from droidbot.feature_eval.confusion import name_similarity
    except Exception:
        name_similarity = None
    best, best_sim = None, -1.0
    needle = {
        "id": feature.id,
        "name": feature.name,
        "description": feature.description or "",
    }
    for item in journal_features:
        if name_similarity is not None:
            sim = name_similarity(needle, item)
        else:
            sim = 1.0 if (item.get("name") or "").lower() == (feature.name or "").lower() else 0.0
        if sim > best_sim:
            best, best_sim = item, sim
    if best is not None and best_sim >= 0.3:
        return best
    return None


def _tokens(text):
    return set(re.findall(r"[a-z0-9]+", (text or "").lower()))


def _short(name):
    if not name:
        return ""
    return name.replace("/", ".").split(".")[-1]


def _clip(text, length):
    text = " ".join(str(text).split())
    if len(text) <= length:
        return text
    return text[: length - 3] + "..."


def extract_json_list(text):
    if not text:
        return None
    text = text.strip()
    fenced = re.search(r"```(?:json)?\s*(\[.*)\s*```", text, re.DOTALL)
    blob = fenced.group(1) if fenced else text
    bracketed = re.search(r"\[.*", blob, re.DOTALL)
    if bracketed:
        blob = bracketed.group(0)
    try:
        parsed = json.loads(blob)
    except ValueError:
        parsed = None
        recovered = []
        for obj in re.findall(r"\{[^{}]*\}", blob):
            try:
                item = json.loads(obj)
            except ValueError:
                continue
            if isinstance(item, dict) and (item.get("feature_id") or item.get("id")):
                recovered.append(item)
        if recovered:
            return recovered
        # Close a truncated array after the last complete object.
        last = blob.rfind("}")
        if last != -1:
            candidate = blob[: last + 1]
            if not candidate.rstrip().endswith("]"):
                candidate = candidate + "]"
            if not candidate.lstrip().startswith("["):
                candidate = "[" + candidate
            try:
                parsed = json.loads(candidate)
            except ValueError:
                parsed = None
        if parsed is None:
            return None
    if isinstance(parsed, list):
        return [item for item in parsed if isinstance(item, dict)]
    if isinstance(parsed, dict) and isinstance(parsed.get("features"), list):
        return [item for item in parsed["features"] if isinstance(item, dict)]
    return None


def extract_json(text):
    if not text:
        return None
    text = text.strip()
    candidates = [text]
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fenced:
        candidates.insert(0, fenced.group(1))
    braced = re.search(r"\{.*\}", text, re.DOTALL)
    if braced:
        candidates.insert(0, braced.group(0))
    for candidate in candidates:
        try:
            parsed = json.loads(candidate)
        except ValueError:
            continue
        if isinstance(parsed, dict):
            status = parsed.get("status")
            if not status:
                if parsed.get("covered") is True:
                    parsed["status"] = STATUS_COVERED
                elif parsed.get("covered") is False:
                    parsed["status"] = STATUS_NOT_COVERED
            elif status not in (STATUS_COVERED, STATUS_PARTIAL, STATUS_NOT_COVERED):
                lowered = str(status).lower().replace(" ", "_")
                if lowered in (STATUS_COVERED, STATUS_PARTIAL, STATUS_NOT_COVERED):
                    parsed["status"] = lowered
            return parsed
    return None
