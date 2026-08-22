"""Serialize executed feature traces as replayable JSON test cases."""

import json
import os

from .signatures import step_from_event, widget_selector


def test_cases_dir(journal_root):
    path = os.path.join(journal_root, "test_cases")
    os.makedirs(path, exist_ok=True)
    return path


def append_step_payload(step, event, value=""):
    """Attach a replayable selector to a journal step dict (in place)."""
    payload = step_from_event(event, value=value)
    step["action_type"] = payload["action_type"]
    step["selector"] = payload["selector"]
    step["value"] = payload["value"]
    step["signature"] = payload["signature"]
    return step


def write_feature_test_case(journal_root, feature, source_run=""):
    steps = []
    for item in feature.get("steps") or []:
        if item.get("decision") not in (None, "act"):
            continue
        selector = item.get("selector")
        if not selector:
            continue
        if not any(selector.get(key) for key in (
            "resource_id", "text", "content_description", "class", "name", "x", "y",
        )):
            continue
        steps.append({
            "action_type": item.get("action_type") or "touch",
            "selector": selector,
            "value": item.get("value") or item.get("text") or "",
        })
    if not steps:
        return None
    payload = {
        "feature_id": feature.get("id"),
        "name": feature.get("name"),
        "steps": steps,
        "status": feature.get("status"),
        "source_run": source_run,
        "completion_source": feature.get("completion_source") or "executed",
    }
    folder = test_cases_dir(journal_root)
    path = os.path.join(folder, "%s.json" % (feature.get("id") or "feature"))
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    return path


def write_all_test_cases(journal, source_run=""):
    written = []
    root = getattr(journal, "root", None)
    if not root:
        return written
    for feature in journal.features():
        path = write_feature_test_case(root, feature, source_run=source_run or root)
        if path:
            written.append(path)
    return written


def load_test_case(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)
