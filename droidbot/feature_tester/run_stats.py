"""Run-level counters for paper metrics (LLM calls, wall clock, VLM fallbacks)."""

import time


class RunStats(object):
    def __init__(self):
        self.started_at = time.time()
        self.llm_calls = {
            "feature_extraction": 0,
            "widget_scoring": 0,
            "context_retrieval": 0,
            "hybrid_discovery": 0,
            "other": 0,
        }
        self.vlm_fallbacks = []
        self.sparse_screens = []
        self.mechanisms = []
        self.text_inputs = []
        self.context_calls = []
        self.field_resolutions = []

    def record_llm(self, kind="other"):
        if kind not in self.llm_calls:
            kind = "other"
        self.llm_calls[kind] = self.llm_calls.get(kind, 0) + 1

    def record_mechanism(self, name, detail=""):
        self.mechanisms.append({"name": name, "detail": detail, "t": time.time() - self.started_at})

    def record_vlm(self, heuristic_confidence, llm_confidence, agreed, outcome, state_str=""):
        self.vlm_fallbacks.append({
            "heuristic_confidence": heuristic_confidence,
            "llm_confidence": llm_confidence,
            "agreed": agreed,
            "outcome": outcome,
            "state": state_str,
        })
        lows = [row for row in self.vlm_fallbacks[-6:] if row.get("state") == state_str]
        if state_str and len(lows) >= 3 and all((row.get("llm_confidence") or 0) < 0.5 for row in lows):
            if state_str not in self.sparse_screens:
                self.sparse_screens.append(state_str)

    def record_text(self, value, source="", field="", accepted=None):
        if value is None:
            return
        self.text_inputs.append({
            "value": str(value),
            "source": source,
            "field": field or "",
            "accepted": accepted,
        })

    def record_field_resolution(self, source, field="", value="", accepted=None):
        self.field_resolutions.append({
            "source": source or "",
            "field": field or "",
            "value": "" if value is None else str(value),
            "accepted": accepted,
        })

    def record_context(self, function_name, well_formed, value=""):
        self.context_calls.append({
            "function": function_name,
            "well_formed": well_formed,
            "value": value,
        })

    def wall_clock_seconds(self):
        return time.time() - self.started_at

    def to_dict(self):
        return {
            "wall_clock_seconds": round(self.wall_clock_seconds(), 2),
            "llm_calls": dict(self.llm_calls),
            "llm_calls_total": sum(self.llm_calls.values()),
            "vlm_fallbacks": len(self.vlm_fallbacks),
            "sparse_screens": list(self.sparse_screens),
            "mechanisms": list(self.mechanisms),
            "text_inputs": list(self.text_inputs),
            "context_calls": list(self.context_calls),
            "field_fills": self.field_fill_counts(),
            "field_resolutions": list(self.field_resolutions),
        }

    def field_fill_counts(self):
        counts = {"credential": 0, "vlm": 0, "unresolved": 0, "optional-blank": 0}
        for row in self.field_resolutions:
            source = row.get("source") or ""
            if source == "llm":
                source = "vlm"
            if source in counts:
                counts[source] += 1
        return counts


STATS = RunStats()


def reset_stats():
    """Re-init the module singleton in place.

    Callers that did ``from .run_stats import STATS`` keep the same object
    identity; rebinding here used to leave those imports on a stale empty
    counter (llm_calls always 0 in metrics.md).
    """
    STATS.__init__()
    return STATS
