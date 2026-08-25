"""Ablation flags for TestCube feature-guided experiments.

Disable mechanisms with ``--disable afford_search,backtrack,...`` or
``TESTCUBE_DISABLE=shared_flow,hybrid_discovery``.
"""

import os


MECHANISMS = (
    "afford_search",
    "backtrack",
    "context_functions",
    "hybrid_discovery",
    "vlm_logging",
    "shared_flow",
    "stagnation",
    "non_idempotent",
)


class FeatureTesterConfig(object):
    def __init__(self):
        self.afford_search = True
        self.backtrack = True
        self.context_functions = True
        self.hybrid_discovery = True
        self.vlm_logging = True
        self.shared_flow = True
        self.stagnation = True
        self.non_idempotent = True
        self.max_backtracks = 3
        self.shared_k = 3
        self.shared_threshold = 0.7
        self.stagnation_window = 8
        self.stagnation_novelty = 0.2
        self.discovery_budget = 12
        self.progress_stall_steps = 10
        # Run-level budgets. Without these a run with no -count/-timeout can
        # only stop when the policy raises InputInterruptedException, because
        # droidbot defaults to event_count=1e8 / timeout=-1.
        self.max_run_events = 600
        # A 28-feature app needs more than 45 min even after the model-call
        # cuts; too small a budget silently starves the tail of the list.
        self.max_run_seconds = 5400
        self.max_steps_per_feature = 60
        self.max_feature_attempts = 2
        self.max_restart_attempts = 8
        # A widget tapped this many times inside one feature attempt stops
        # being offered. Keyed on widget signature, not (state, view), so it
        # still fires when a stepper mutates the state hash on every tap.
        self.max_widget_taps = 6
        # Vision calls are the dominant cost per feature; cap them and only
        # escalate once remaining-step progress has genuinely stalled.
        self.max_vlm_calls_per_feature = 8
        self.vlm_stall_steps = 2
        # Step matching: containment ratio rather than a raw token-count cutoff.
        self.step_match_threshold = 0.5
        self.replay_path = None
        self.ground_truth_path = None
        self.guide_features_path = None
        self.context_module_path = None

    def enabled(self, name):
        return bool(getattr(self, name, False))

    def disable(self, names):
        for name in names or []:
            name = (name or "").strip()
            if name and hasattr(self, name):
                setattr(self, name, False)

    @classmethod
    def from_options(cls, opts=None):
        cfg = cls()
        env = os.environ.get("TESTCUBE_DISABLE") or ""
        cfg.disable(part.strip() for part in env.split(",") if part.strip())
        if opts is not None:
            cfg.replay_path = getattr(opts, "replay_path", None)
            cfg.ground_truth_path = getattr(opts, "ground_truth_path", None)
            cfg.guide_features_path = getattr(opts, "guide_features_path", None)
            cfg.context_module_path = getattr(opts, "context_module_path", None)
            disable = getattr(opts, "disable_mechanisms", None) or ""
            cfg.disable(part.strip() for part in disable.split(",") if part.strip())
            if getattr(opts, "max_backtracks", None) is not None:
                cfg.max_backtracks = int(opts.max_backtracks)
            for name in (
                "max_run_events", "max_run_seconds", "max_steps_per_feature",
                "max_feature_attempts", "max_restart_attempts",
                "max_widget_taps", "max_vlm_calls_per_feature",
            ):
                value = getattr(opts, name, None)
                if value is not None:
                    setattr(cfg, name, int(value))
        for name in (
            "max_run_events", "max_run_seconds", "max_steps_per_feature",
            "max_feature_attempts", "max_restart_attempts",
            "max_widget_taps", "max_vlm_calls_per_feature",
        ):
            raw = os.environ.get("TESTCUBE_%s" % name.upper())
            if raw:
                try:
                    setattr(cfg, name, int(raw))
                except ValueError:
                    pass
        return cfg


_CURRENT = None


def get_config():
    global _CURRENT
    if _CURRENT is None:
        _CURRENT = FeatureTesterConfig.from_options(None)
    return _CURRENT


def set_config(cfg):
    global _CURRENT
    _CURRENT = cfg
    return cfg


def add_cli_flags(parser):
    parser.add_argument(
        "--replay",
        dest="replay_path",
        default=None,
        help="Replay a saved feature_test/test_cases/*.json file (no feature-guided inference).",
    )
    parser.add_argument(
        "--ground-truth",
        dest="ground_truth_path",
        default=None,
        help="Ground-truth features JSON for offline coverage (default: feature/<stem>/ground_truth.json).",
    )
    parser.add_argument(
        "--disable",
        dest="disable_mechanisms",
        default="",
        help="Comma-separated mechanisms to disable for ablation: %s." % ",".join(MECHANISMS),
    )
    parser.add_argument(
        "--max-backtracks",
        dest="max_backtracks",
        type=int,
        default=None,
        help="Cap on same-feature loop backtracks (default: 3).",
    )
    return parser
