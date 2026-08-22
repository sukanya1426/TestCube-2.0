"""Global store of executed GUI actions for later feature completion.

If feature A stopped after steps a→b→c, later actions from feature P that
match A's remaining gold steps d and e can upgrade A to covered.
"""


class ExplorationBank(object):
    def __init__(self, events=None):
        self.events = list(events or [])

    def record(self, step, feature_id):
        if not step:
            return
        blob = " ".join(
            str(item or "")
            for item in (
                step.get("event"),
                step.get("matched_step"),
                step.get("reason"),
                step.get("activity"),
                step.get("text"),
                step.get("event_type"),
            )
        )
        self.events.append({
            "feature_id": feature_id,
            "event": step.get("event") or "",
            "event_type": step.get("event_type") or "",
            "matched_step": step.get("matched_step") or "",
            "activity": step.get("activity") or "",
            "text": step.get("text") or "",
            "blob": blob.strip(),
        })

    def events_from_other_features(self, feature_id):
        return [
            item for item in self.events
            if item.get("feature_id") and item.get("feature_id") != feature_id
        ]

    def to_list(self):
        return list(self.events)
