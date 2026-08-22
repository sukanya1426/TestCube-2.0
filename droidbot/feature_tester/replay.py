"""Replay a saved feature_test/test_cases/*.json file against the device."""

import json
import logging
import os

from droidbot.input_event import IntentEvent, KeyEvent, ScrollEvent, SetTextEvent
from droidbot.input_policy import InputInterruptedException, UtgBasedInputPolicy

from .signatures import pick_event, widget_selector


class ReplayPolicy(UtgBasedInputPolicy):
    def __init__(self, device, app, random_input, test_case_path):
        super(ReplayPolicy, self).__init__(device, app, random_input)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.path = test_case_path
        with open(test_case_path, "r", encoding="utf-8") as handle:
            self.case = json.load(handle)
        self._index = 0
        self.results = []
        self._finished = False

    def generate_event_based_on_utg(self):
        if self._index == 0:
            self._index = 1
            return IntentEvent(intent=self.app.get_start_intent())
        steps = self.case.get("steps") or []
        offset = self._index - 1
        if offset >= len(steps):
            self._write_report()
            raise InputInterruptedException("Replay complete.")
        step = steps[offset]
        self._index += 1
        state = self.current_state
        events = list(state.get_possible_input()) if state else []
        action_type = (step.get("action_type") or "touch").lower()
        selector = step.get("selector") or {}
        if action_type == "key":
            event = KeyEvent(name=selector.get("name") or "BACK")
            event.skip_oracle = True
            self.results.append({"index": offset, "ok": True, "reason": "key"})
            return event
        if action_type == "intent":
            return IntentEvent(intent=self.app.get_start_intent())
        matched = pick_event(events, selector, action_type=action_type)
        if matched is None:
            self.results.append({
                "index": offset,
                "ok": False,
                "reason": "selector not found: %s" % selector,
            })
            self.logger.warning("Replay step %d failed: selector not found" % offset)
            if offset + 1 >= len(steps):
                self._write_report()
                raise InputInterruptedException("Replay failed.")
            return KeyEvent(name="BACK")
        if action_type == "set_text":
            matched.text = step.get("value") or ""
        matched.skip_oracle = True
        self.results.append({
            "index": offset,
            "ok": True,
            "reason": "matched %s" % widget_selector(matched),
        })
        return matched

    def _write_report(self):
        if self._finished:
            return
        self._finished = True
        passed = sum(1 for row in self.results if row.get("ok"))
        payload = {
            "feature_id": self.case.get("feature_id"),
            "path": self.path,
            "passed": passed,
            "failed": len(self.results) - passed,
            "total": len(self.case.get("steps") or []),
            "steps": self.results,
        }
        out_dir = os.path.dirname(self.path)
        report_path = os.path.join(out_dir, "%s.replay.json" % (self.case.get("feature_id") or "replay"))
        with open(report_path, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.write("\n")
        self.logger.info("Replay report: %s (%d/%d passed)" % (
            report_path, passed, payload["total"],
        ))
