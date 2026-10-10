"""Reconstruct TestCube's executed action trace from existing output.

The linear execution order is already recorded in events/event_*.json.
Each EventLog contains start_state, stop_state, event_str, and the
serialized event (type, view, intent, key, text).

This loader does not add a second action logger. It only reads:
  results/events/*.json
  results/states/state_*.json
  results/utg.js  (optional activity/screenshot enrichment)
"""

import json
import os
import re

from .models import ExecutionTrace, ObservedAction, TestCaseTrace


SESSION_SPLIT_TYPES = {"kill_app"}

# LLMDroid serialises a state's view hierarchy as one HTML-ish string, e.g.
#   <button id=20 class="TextView" content-desc="Messages" >Messages</button>
# while TestCube writes a list of view dicts. Normalising LLMDroid's form into
# the same dicts at load time is what lets one evaluator score both tools, so
# the feature-coverage numbers stay comparable instead of one tool scoring zero.
_MARKUP_TAG = re.compile(r"<\s*([A-Za-z_][\w-]*)([^>]*?)>([^<]*)")
_MARKUP_ATTR = re.compile(r'([A-Za-z_][\w-]*)\s*=\s*"([^"]*)"')

# LLMDroid attribute name -> the key TestCube's view dicts use.
_ATTR_TO_VIEW_KEY = {
    "content-desc": "content_description",
    "content_desc": "content_description",
    "resource-id": "resource_id",
    "resource_id": "resource_id",
    "class": "class",
    "text": "text",
}


def views_from_markup(markup):
    """Turn LLMDroid's view markup into TestCube-shaped view dicts."""
    views = []
    for tag, attrs, inner in _MARKUP_TAG.findall(markup or ""):
        view = {"class": tag}
        for name, value in _MARKUP_ATTR.findall(attrs or ""):
            key = _ATTR_TO_VIEW_KEY.get(name.lower())
            if key and value:
                view[key] = value
        inner = (inner or "").strip()
        if inner:
            view["text"] = inner
        # Keep only views that carry something a matcher could read.
        if view.get("text") or view.get("content_description") or view.get("resource_id"):
            views.append(view)
    return views


def normalise_views(payload):
    """Give a state payload a list-of-dicts ``views``, whatever tool wrote it."""
    views = payload.get("views")
    if isinstance(views, str):
        payload = dict(payload)
        payload["views"] = views_from_markup(views)
    return payload


class TraceLoader(object):
    def load(self, results_dir):
        if not results_dir or not os.path.isdir(results_dir):
            raise ValueError("Results directory not found: %s" % results_dir)

        states = self._load_states(self._first_dir(results_dir, "states"))
        utg = self._load_utg(self._first_file(results_dir, "utg.js"))
        self._enrich_states_from_utg(states, utg)

        event_dir = os.path.join(results_dir, "events")
        raw_events = self._load_events(event_dir)
        actions = []
        for index, payload in enumerate(raw_events):
            actions.append(self._to_action(index, payload, states, utg))

        test_cases = self._split_sessions(actions)
        package = None
        if utg:
            package = utg.get("app_package")
        if not package:
            package = self._infer_package(actions)

        return ExecutionTrace(
            app_package=package,
            app_name=package,
            actions=actions,
            test_cases=test_cases,
            states=states,
        )

    def _first_dir(self, results_dir, name):
        candidates = [
            os.path.join(results_dir, ".droidbot", name),
            os.path.join(results_dir, name),
        ]
        for path in candidates:
            if os.path.isdir(path):
                return path
        return candidates[-1]

    def _first_file(self, results_dir, name):
        candidates = [
            os.path.join(results_dir, ".droidbot", name),
            os.path.join(results_dir, name),
        ]
        for path in candidates:
            if os.path.isfile(path):
                return path
        return candidates[-1]

    def _load_events(self, event_dir):
        if not os.path.isdir(event_dir):
            return []
        files = [
            os.path.join(event_dir, name)
            for name in os.listdir(event_dir)
            if name.startswith("event_") and name.endswith(".json")
        ]
        files.sort()
        events = []
        for path in files:
            try:
                with open(path, "r", encoding="utf-8") as handle:
                    payload = json.load(handle)
            except (OSError, ValueError):
                continue
            if isinstance(payload, dict):
                events.append(payload)
        return events

    def _load_states(self, state_dir):
        states = {}
        if not os.path.isdir(state_dir):
            return states
        for name in os.listdir(state_dir):
            if not (name.startswith("state_") and name.endswith(".json")):
                continue
            path = os.path.join(state_dir, name)
            try:
                with open(path, "r", encoding="utf-8") as handle:
                    payload = json.load(handle)
            except (OSError, ValueError):
                continue
            if not isinstance(payload, dict):
                continue
            payload = normalise_views(payload)
            state_str = payload.get("state_str")
            if not state_str:
                continue
            screenshot = self._sibling_screenshot(state_dir, payload.get("tag"), name)
            if screenshot:
                payload = dict(payload)
                payload["screenshot"] = screenshot
            # Keep the first dump of a given state_str; later revisits
            # share the same hash and do not add new evidence.
            if state_str not in states:
                states[state_str] = payload
        return states

    def _sibling_screenshot(self, state_dir, tag, state_filename):
        if tag:
            for ext in (".png", ".jpg"):
                candidate = os.path.join(state_dir, "screen_%s%s" % (tag, ext))
                if os.path.isfile(candidate):
                    return candidate
        suffix = state_filename[len("state_"):-len(".json")]
        for ext in (".png", ".jpg"):
            candidate = os.path.join(state_dir, "screen_%s%s" % (suffix, ext))
            if os.path.isfile(candidate):
                return candidate
        return None

    def _load_utg(self, utg_path):
        if not os.path.isfile(utg_path):
            return None
        try:
            with open(utg_path, "r", encoding="utf-8") as handle:
                text = handle.read()
        except OSError:
            return None
        match = re.search(r"\{.*\}\s*$", text, re.DOTALL)
        if not match:
            return None
        try:
            return json.loads(match.group(0))
        except ValueError:
            return None

    def _enrich_states_from_utg(self, states, utg):
        if not utg:
            return
        for node in utg.get("nodes") or []:
            state_str = node.get("state_str") or node.get("id")
            if not state_str:
                continue
            existing = states.get(state_str) or {}
            if "foreground_activity" not in existing and node.get("activity"):
                package = node.get("package") or ""
                activity = node.get("activity") or ""
                if package and activity and not activity.startswith(package):
                    existing["foreground_activity"] = "%s/%s" % (package, activity)
                else:
                    existing["foreground_activity"] = activity
            if "screenshot" not in existing and node.get("image"):
                existing["screenshot"] = node.get("image")
            if "search_content" not in existing and node.get("content"):
                existing["search_content"] = node.get("content")
            states[state_str] = existing

    def _to_action(self, index, payload, states, utg):
        event = payload.get("event") or {}
        view = event.get("view") or {}
        start_state = payload.get("start_state")
        stop_state = payload.get("stop_state")
        start_info = states.get(start_state) or {}
        stop_info = states.get(stop_state) or {}
        start_activity = start_info.get("foreground_activity")
        stop_activity = stop_info.get("foreground_activity")
        stop_texts = self._visible_texts(stop_info)
        screenshot = stop_info.get("screenshot") or start_info.get("screenshot")
        event_type = event.get("event_type") or ""
        text_input = event.get("text")
        if not text_input:
            text_input = None
        return ObservedAction(
            index=index,
            tag=str(payload.get("tag") or index),
            test_case="",
            event_type=event_type,
            event_str=str(payload.get("event_str") or ""),
            view_text=view.get("text"),
            content_description=view.get("content_description"),
            resource_id=view.get("resource_id"),
            view_class=view.get("class"),
            text_input=text_input,
            key_name=event.get("name"),
            intent=event.get("intent") or event.get("stop_intent"),
            start_state=start_state,
            stop_state=stop_state,
            start_activity=start_activity,
            stop_activity=stop_activity,
            stop_texts=stop_texts,
            screenshot=screenshot,
            state_changed=bool(start_state and stop_state and start_state != stop_state),
        )

    def _visible_texts(self, state):
        texts = []
        views = state.get("views")
        if isinstance(views, str):                 # a state that bypassed the loader
            views = views_from_markup(views)
        for view in views or []:
            if not isinstance(view, dict):         # never crash on an unexpected shape
                if view:
                    texts.append(str(view))
                continue
            for key in ("text", "content_description"):
                value = view.get(key)
                if value:
                    texts.append(str(value))
        content = state.get("search_content")
        if content:
            texts.append(str(content))
        return texts

    def _split_sessions(self, actions):
        sessions = []
        current = []

        def flush():
            if not current:
                return
            session_id = "test_%03d" % (len(sessions) + 1)
            for action in current:
                action.test_case = session_id
            sessions.append(TestCaseTrace(id=session_id, actions=list(current)))
            del current[:]

        for action in actions:
            if self._is_session_boundary(action):
                flush()
            current.append(action)
        flush()
        if not sessions and actions:
            for action in actions:
                action.test_case = "test_001"
            sessions.append(TestCaseTrace(id="test_001", actions=list(actions)))
        return sessions

    def _is_session_boundary(self, action):
        if action.event_type in SESSION_SPLIT_TYPES:
            return True
        if action.event_type != "intent" or not action.intent:
            return False
        intent = action.intent.lower()
        return (
            "force-stop" in intent
            or "am start" in intent
            or intent.strip().startswith("start ")
        )

    def _infer_package(self, actions):
        for action in actions:
            if action.resource_id and ":" in action.resource_id:
                return action.resource_id.split(":")[0]
            if action.intent and "am start" in (action.intent or ""):
                match = re.search(r"([\w.]+)/", action.intent)
                if match:
                    return match.group(1)
        return None
