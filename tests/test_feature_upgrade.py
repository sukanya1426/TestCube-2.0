"""Tests for replayable test cases, dual coverage, and shared-flow detection."""

import json
import os
import tempfile
import unittest
from types import SimpleNamespace

from droidbot.input_event import ScrollEvent
from droidbot.feature_eval.confusion import (
    confusion_rows,
    inference_scores,
    name_similarity,
    warn_id_collisions,
    _best_journal_match,
)
from droidbot.feature_tester.chain_memory import (
    ChainMemory,
    contiguous_prefix_match,
    decide_shared_flow,
    is_non_idempotent,
)
from droidbot.feature_tester.config import FeatureTesterConfig, set_config
from droidbot.feature_tester.journal import (
    FeatureJournal,
    STATUS_COVERED,
    STATUS_PARTIAL,
)
from droidbot.feature_tester.mechanisms import find_affordance_event, non_idempotent_key
from droidbot.feature_tester.policy import FeatureGuidedPolicy
from droidbot.feature_tester.signatures import pick_event, step_from_event
from droidbot.feature_tester.test_cases import write_feature_test_case


def _event(text, event_type="touch", resource_id="", content_desc="", cls="Button"):
    return SimpleNamespace(
        event_type=event_type,
        view={
            "text": text,
            "resource_id": resource_id,
            "content_description": content_desc,
            "class": "android.widget." + cls,
        },
        name="",
        direction="",
    )


CHECKOUT = [
    "touch|add|add to cart|button||",
    "touch|cart|cart|button||",
    "touch|checkout|checkout|button||",
    "touch|pay|pay now|button||",
]


class ChainMemoryTests(unittest.TestCase):
    def test_contiguous_prefix_match(self):
        current = CHECKOUT[:3]
        prior = list(CHECKOUT)
        self.assertGreaterEqual(contiguous_prefix_match(current, prior, min_len=3), 3)

    def test_reuse_marks_contained_remaining(self):
        memory = ChainMemory()
        prior = {
            "id": "F001",
            "actions": ["Add to cart", "Open cart", "Checkout", "Pay now"],
            "completed_actions": ["Add to cart", "Open cart", "Checkout", "Pay now"],
        }
        memory.register(prior, CHECKOUT, terminal_state="paid")
        decision = decide_shared_flow(
            memory,
            CHECKOUT[:3],
            ["Pay now"],
            lambda fid: prior,
            k=3,
            threshold=0.7,
        )
        self.assertEqual(decision["action"], "reuse")
        self.assertEqual(decision["skipped"], 1)

    def test_diverge_when_remaining_is_novel(self):
        memory = ChainMemory()
        prior = {
            "id": "F001",
            "actions": ["Add to cart", "Open cart", "Checkout", "Pay now"],
            "completed_actions": ["Add to cart", "Open cart", "Checkout", "Pay now"],
        }
        memory.register(prior, CHECKOUT)
        decision = decide_shared_flow(
            memory,
            CHECKOUT[:3],
            ["Apply coupon code"],
            lambda fid: prior,
            k=3,
        )
        self.assertEqual(decision["action"], "diverge")

    def test_pay_is_non_idempotent(self):
        self.assertTrue(is_non_idempotent(label="Place order"))
        self.assertTrue(is_non_idempotent(label="Pay now"))
        self.assertFalse(is_non_idempotent(label="Open cart"))


class SharedFlowPolicyTests(unittest.TestCase):
    def tearDown(self):
        set_config(FeatureTesterConfig())

    def _policy(self, tmpdir, shared_flow=True):
        cfg = FeatureTesterConfig()
        if not shared_flow:
            cfg.shared_flow = False
        set_config(cfg)
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.cfg = cfg
        policy.chain_memory = ChainMemory()
        policy.journal = FeatureJournal(tmpdir, app_name="Shop")
        policy.journal.load_or_create({
            "app": "Shop",
            "features": [
                {
                    "id": "F001",
                    "name": "Buy product A",
                    "actions": ["Add to cart", "Open cart", "Checkout", "Pay now"],
                },
                {
                    "id": "F002",
                    "name": "Buy product B",
                    "actions": ["Add to cart", "Open cart", "Checkout", "Pay now"],
                },
            ],
        })
        policy._current = None
        policy._feature_sigs = []
        policy._feature_steps = 0
        policy._no_progress = 0
        policy._last_state_str = ""
        policy.logger = __import__("logging").getLogger("SharedFlowPolicyTests")
        policy._continue_next_feature = lambda possible, state: "NEXT"
        return policy

    def test_second_feature_covered_by_reference(self):
        tmpdir = tempfile.mkdtemp()
        policy = self._policy(tmpdir, shared_flow=True)
        first = policy.journal.get_feature("F001")
        first["completed_actions"] = list(first["actions"])
        first["remaining_actions"] = []
        policy._current = first
        policy._feature_sigs = list(CHECKOUT)
        policy._drop_current(STATUS_COVERED, "Paid once.")
        self.assertEqual(len(policy.chain_memory.chains), 1)
        self.assertEqual(policy.chain_memory.chains[0]["status"], "completed")
        self.assertNotEqual(policy.chain_memory.chains[0]["status"], "in_progress")

        second = policy.journal.get_feature("F002")
        policy._current = second
        policy.journal.start_feature(second)
        policy._feature_sigs = list(CHECKOUT[:3])
        result = policy._maybe_reuse_shared_flow([], SimpleNamespace())
        self.assertEqual(result, "NEXT")
        second = policy.journal.get_feature("F002")
        self.assertEqual(second.get("status"), STATUS_COVERED)
        self.assertEqual(second.get("completion_source"), "shared_flow_reuse")
        self.assertEqual(second.get("remaining_actions"), [])
        self.assertEqual(len(policy.chain_memory.reuses), 1)
        self.assertGreaterEqual(policy.chain_memory.reuses[0]["actions_skipped"], 1)

    def test_covered_feature_finalizes_chain_out_of_in_progress(self):
        tmpdir = tempfile.mkdtemp()
        policy = self._policy(tmpdir, shared_flow=True)
        first = policy.journal.get_feature("F001")
        first["status"] = "in_progress"
        first["completed_actions"] = list(first["actions"])
        first["remaining_actions"] = []
        policy._current = first
        policy._feature_sigs = list(CHECKOUT)
        policy._last_state_str = "terminal_hash"
        policy._drop_current(STATUS_COVERED, "Paid once.")
        chain = policy.chain_memory.chains[0]
        self.assertEqual(chain["status"], "completed")
        self.assertNotEqual(chain["status"], "in_progress")
        self.assertEqual(chain["terminal_state"], "terminal_hash")
        with open(policy.journal.log_path, encoding="utf-8") as handle:
            log_text = handle.read()
        self.assertIn("chain C001 finalized as completed", log_text)

    def test_disabled_shared_flow_does_not_reuse(self):
        tmpdir = tempfile.mkdtemp()
        policy = self._policy(tmpdir, shared_flow=False)
        first = policy.journal.get_feature("F001")
        policy.chain_memory.register(first, CHECKOUT)
        second = policy.journal.get_feature("F002")
        policy._current = second
        policy._feature_sigs = list(CHECKOUT[:3])
        self.assertIsNone(policy._maybe_reuse_shared_flow([], SimpleNamespace()))
        self.assertEqual(second.get("status"), "pending")

    def test_coverage_does_not_regress_vs_disabled(self):
        with_dir = tempfile.mkdtemp()
        without_dir = tempfile.mkdtemp()
        with_policy = self._policy(with_dir, shared_flow=True)
        without_policy = self._policy(without_dir, shared_flow=False)
        for policy in (with_policy, without_policy):
            first = policy.journal.get_feature("F001")
            first["completed_actions"] = list(first["actions"])
            first["remaining_actions"] = []
            policy._current = first
            policy._feature_sigs = list(CHECKOUT)
            policy._drop_current(STATUS_COVERED, "done")
            second = policy.journal.get_feature("F002")
            policy._current = second
            policy.journal.start_feature(second)
            policy._feature_sigs = list(CHECKOUT[:3])
            policy._maybe_reuse_shared_flow([], SimpleNamespace())
        with_report = with_policy.journal.finalize()
        without_report = without_policy.journal.finalize()
        self.assertGreaterEqual(with_report["covered"], without_report["covered"])
        self.assertIn("online_coverage", with_report)
        self.assertIn("Covered:", with_policy.journal._render_markdown(with_report))
        self.assertIn("Online coverage:", with_policy.journal._render_markdown(with_report))
        self.assertIn("Shared flows detected", with_policy.journal._render_markdown(with_report))

    def test_non_idempotent_not_double_triggered(self):
        tmpdir = tempfile.mkdtemp()
        policy = self._policy(tmpdir)
        pay = _event("Place order")
        cart = _event("Open cart")
        key = non_idempotent_key(pay)
        self.assertTrue(key)
        policy.chain_memory.executed_non_idempotent.add(key)
        swapped = policy._swap_non_idempotent(pay, [pay, cart], SimpleNamespace())
        self.assertIs(swapped, cart)


class AffordanceAndReplayTests(unittest.TestCase):
    def test_affordance_tiers_fab_then_menu_then_scroll(self):
        home = _event("Home")
        home.view["bounds"] = [[0, 0], [1080, 1920]]
        fab = _event("add", resource_id="app:id/fab")
        fab.view["bounds"] = [[900, 1600], [1040, 1740]]
        menu = _event("More options", resource_id="app:id/overflow")
        menu.view["bounds"] = [[20, 40], [100, 120]]
        scroll = ScrollEvent(direction="DOWN")
        event, tier = find_affordance_event([home, menu, scroll, fab], tried_tiers=set())
        self.assertEqual(tier, "fab")
        event, tier = find_affordance_event([home, menu, scroll], tried_tiers={"fab", "plus"})
        self.assertEqual(tier, "menu")
        event, tier = find_affordance_event([scroll], tried_tiers={"fab", "plus", "menu"})
        self.assertEqual(tier, "scroll")

    def test_test_case_schema_and_pick_event(self):
        tmpdir = tempfile.mkdtemp()
        journal = FeatureJournal(tmpdir, app_name="Shop")
        journal.load_or_create({
            "app": "Shop",
            "features": [{"id": "F001", "name": "Search", "actions": ["Type query"]}],
        })
        feature = journal.get_feature("F001")
        feature["status"] = STATUS_PARTIAL
        event = _event("Search", event_type="set_text", cls="EditText")
        step = step_from_event(event, value="beatles")
        step["decision"] = "act"
        feature["steps"] = [step]
        path = write_feature_test_case(journal.root, feature, source_run="test")
        self.assertTrue(path and os.path.isfile(path))
        with open(path, encoding="utf-8") as handle:
            payload = json.load(handle)
        self.assertEqual(payload["feature_id"], "F001")
        self.assertEqual(payload["status"], STATUS_PARTIAL)
        self.assertIn("source_run", payload)
        self.assertEqual(payload["steps"][0]["action_type"], "set_text")
        self.assertEqual(payload["steps"][0]["value"], "beatles")
        self.assertIn("selector", payload["steps"][0])
        live = [_event("Search", event_type="set_text", cls="EditText")]
        matched = pick_event(live, payload["steps"][0]["selector"], action_type="set_text")
        self.assertIsNotNone(matched)

    def test_blocked_feature_still_writes_test_case(self):
        tmpdir = tempfile.mkdtemp()
        journal = FeatureJournal(tmpdir, app_name="App")
        journal.load_or_create({
            "app": "App",
            "features": [{"id": "F001", "name": "Search", "actions": ["Tap Search"]}],
        })
        feature = journal.get_feature("F001")
        feature["status"] = "blocked"
        event = _event("Search", event_type="touch", cls="Button")
        step = step_from_event(event)
        step["decision"] = "act"
        feature["steps"] = [step]
        path = write_feature_test_case(journal.root, feature, source_run="test")
        self.assertTrue(path and os.path.isfile(path))
        with open(path, encoding="utf-8") as handle:
            payload = json.load(handle)
        self.assertEqual(payload["status"], "blocked")
        self.assertEqual(payload["steps"][0]["selector"]["text"], "Search")

    def test_existing_report_fields_kept(self):
        tmpdir = tempfile.mkdtemp()
        journal = FeatureJournal(tmpdir, app_name="Shop")
        journal.load_or_create({
            "app": "Shop",
            "features": [{"id": "F001", "name": "A", "actions": ["Tap A"]}],
        })
        feature = journal.get_feature("F001")
        journal.finish_feature(feature, STATUS_COVERED, "ok")
        report = journal.finalize()
        for key in (
            "app", "started_at", "finished_at", "total_features", "covered",
            "partial", "dropped", "not_present", "coverage", "features",
            "session_path", "log_path",
        ):
            self.assertIn(key, report)
        self.assertIn("online_coverage", report)
        markdown = journal._render_markdown(report)
        self.assertIn("- Covered:", markdown)
        self.assertIn("- Coverage:", markdown)
        self.assertIn("Online coverage:", markdown)


class ConfusionAndMetricsTests(unittest.TestCase):
    def test_confusion_and_false_not_present(self):
        gt = [
            {"id": "F001", "name": "Search"},
            {"id": "F002", "name": "Play"},
        ]
        journal = [
            {"id": "F001", "name": "Search", "status": "covered"},
            {"id": "F002", "name": "Play", "status": "not_present"},
        ]
        rows = confusion_rows(gt, journal)
        scores = inference_scores(rows)
        self.assertEqual(scores["false_not_present"], 1)
        self.assertEqual(scores["true_positives"], 1)
        self.assertEqual(scores["false_negatives"], 1)

    def test_colliding_ids_do_not_match_unrelated_features(self):
        gt = [{
            "id": "F001",
            "name": "Create a New Database",
            "description": "Create a new Money Manager Ex database during first-time setup.",
        }]
        journal = [{
            "id": "F001",
            "name": "Play a song",
            "description": "Start playback of the selected track.",
            "status": "covered",
        }]
        self.assertLess(name_similarity(gt[0], journal[0]), 0.3)
        match, sim = _best_journal_match(gt[0], journal)
        self.assertIsNone(match)
        self.assertLess(sim, 0.3)
        collisions, loud = warn_id_collisions(gt, journal)
        self.assertTrue(loud)
        self.assertEqual(len(collisions), 1)
        rows = confusion_rows(gt, journal)
        self.assertIsNone(rows[0]["journal_id"])
        self.assertEqual(rows[0]["matched_by"], "none")
        self.assertNotEqual(rows[0]["journal_status"], "covered")

    def test_same_name_still_matches_across_id_schemes(self):
        gt = [{"id": "GT001", "name": "Search for a song"}]
        journal = [{"id": "F007", "name": "Search for a song", "status": "covered"}]
        match, sim = _best_journal_match(gt[0], journal)
        self.assertIsNotNone(match)
        self.assertEqual(match["id"], "F007")
        self.assertGreaterEqual(sim, 0.3)
        rows = confusion_rows(gt, journal)
        self.assertEqual(rows[0]["journal_id"], "F007")
        self.assertEqual(rows[0]["matched_by"], "name")

    def test_report_txt_withholds_prf1_on_id_collision(self):
        from droidbot.feature_eval.models import CoverageReport
        from droidbot.feature_eval.report import ReportGenerator
        report = CoverageReport(
            application="Spotube",
            total_features=29,
            covered_features=0,
            uncovered_features=29,
            partial_features=0,
            coverage=0.0,
            coverage_percentage=0.0,
        )
        report.feature_inference = {
            "precision": 0.2,
            "recall": 0.07,
            "f1": 0.1,
            "prf1_withheld": True,
            "extracted_count": 10,
            "ground_truth_count": 29,
            "feature_completeness_ratio": 0.345,
        }
        report.confusion = [{
            "ground_truth_id": "F001",
            "ground_truth_name": "Anonymous / Guest Login",
            "journal_id": "F001",
            "journal_name": "Complete first-run setup",
            "journal_status": "covered",
            "offline_status": None,
            "name_similarity": 0.0,
            "matched_by": "none",
        }]
        text = ReportGenerator().render_text(report)
        self.assertIn("withheld", text)
        self.assertNotIn("0.20 / 0.07 / 0.10", text)
        self.assertIn("Anonymous / Guest Login", text)
        self.assertIn("Complete first-run setup", text)
        self.assertIn("10 / 29", text)

    def test_aggregate_metrics_script(self):
        tmpdir = tempfile.mkdtemp()
        journal = FeatureJournal(tmpdir, app_name="Shop")
        journal.load_or_create({
            "app": "Shop",
            "features": [{"id": "F001", "name": "A", "actions": ["Tap A"]}],
        })
        feature = journal.get_feature("F001")
        journal.finish_feature(feature, STATUS_COVERED, "ok")
        journal.finalize()
        out = os.path.join(tmpdir, "agg")
        import importlib.util
        script = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "scripts",
            "aggregate_metrics.py",
        )
        spec = importlib.util.spec_from_file_location("aggregate_metrics_cli", script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        code = module.main([tmpdir, "--out", out])
        self.assertEqual(code, 0)
        self.assertTrue(os.path.isfile(os.path.join(out, "metrics.json")))
        self.assertTrue(os.path.isfile(os.path.join(out, "metrics.md")))
        with open(os.path.join(out, "metrics.json"), encoding="utf-8") as handle:
            payload = json.load(handle)
        self.assertEqual(len(payload["runs"]), 1)
        self.assertIn("coverage_vs_rank", payload["runs"][0])
        self.assertIn("action_chain_length_covered", payload["runs"][0])
        self.assertIn("exploration", payload["runs"][0])
        with open(os.path.join(out, "metrics.md"), encoding="utf-8") as handle:
            markdown = handle.read()
        self.assertIn("Matcher min-confidence threshold", markdown)


class ReplayStartIndexTests(unittest.TestCase):
    def test_replay_increments_past_start(self):
        from droidbot.feature_tester.replay import ReplayPolicy
        tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump({
            "feature_id": "F001",
            "steps": [{"action_type": "key", "selector": {"name": "BACK"}, "value": ""}],
        }, tmp)
        tmp.close()
        policy = ReplayPolicy.__new__(ReplayPolicy)
        policy.path = tmp.name
        with open(tmp.name, encoding="utf-8") as handle:
            policy.case = json.load(handle)
        policy._index = 0
        policy.results = []
        policy._finished = False
        policy.app = SimpleNamespace(get_start_intent=lambda: "start")
        policy.logger = __import__("logging").getLogger("replay")
        first = ReplayPolicy.generate_event_based_on_utg(policy)
        self.assertEqual(policy._index, 1)
        self.assertEqual(first.event_type, "intent")
        policy.current_state = SimpleNamespace(get_possible_input=lambda: [])
        second = ReplayPolicy.generate_event_based_on_utg(policy)
        self.assertEqual(second.event_type, "key")


class BacktrackTriedSetTests(unittest.TestCase):
    def _policy(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.cfg = FeatureTesterConfig()
        policy.logger = __import__("logging").getLogger("BacktrackTriedSetTests")
        policy.journal = None
        policy._current = {
            "id": "F003",
            "name": "Import transactions",
            "remaining_actions": ["Tap Save", "Confirm import"],
            "keywords": ["save", "import"],
        }
        policy._tried_widgets = set()
        policy._backtrack_count = 0
        policy._looks_like_hub = lambda *a, **k: True
        policy._back_would_leave_app = lambda *a, **k: True
        policy._widget_try_key = FeatureGuidedPolicy._widget_try_key.__get__(policy)
        return policy

    def test_second_backtrack_does_not_reselect_tried_widget(self):
        from droidbot.feature_tester.signatures import widget_signature
        policy = self._policy()
        first_widget = _event("Save", resource_id="app:id/save")
        other = _event("Confirm", resource_id="app:id/confirm")
        state = SimpleNamespace(state_str="loop_state_v1")
        picked = policy._pick_backtrack_event([first_widget, other], state)
        self.assertIsNotNone(picked)
        first_key = widget_signature(picked)
        policy._tried_widgets.add(first_key)
        # Same widget still available; state hash changed (the original bug).
        state2 = SimpleNamespace(state_str="loop_state_v2")
        second = policy._pick_backtrack_event([first_widget, other], state2)
        if second is not None:
            self.assertNotEqual(widget_signature(second), first_key)
            self.assertNotIn(widget_signature(second), {first_key})
        self.assertNotIn(first_key, {
            widget_signature(second)
        } if second is not None else set())


class HybridDiscoveryRepeatTests(unittest.TestCase):
    def _policy(self, feature_name, tmpdir):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.cfg = FeatureTesterConfig()
        policy.cfg.discovery_budget = 12
        policy.logger = __import__("logging").getLogger("HybridDiscoveryRepeatTests")
        policy.journal = FeatureJournal(tmpdir, app_name="App")
        policy.journal.load_or_create({
            "app": "App",
            "features": [{"id": "F001", "name": feature_name, "actions": ["Open"]}],
        })
        policy.app = SimpleNamespace(app_name="App")
        policy._discovery_done = False
        policy._discovery_phase = False
        policy._discovery_steps = 0
        policy._discovery_pairs = set()
        policy._discovery_seen_states = set()
        policy._discovery_tried_widgets = set()
        policy._discovery_state_repeats = {}
        policy._discovery_label_baseline = 0
        policy._observed_labels = []
        policy._seen_hub = True
        policy._current = policy.journal.get_feature("F001")
        policy._feature_steps = 0
        policy._tap_counts = {}
        policy._is_back = lambda event: False
        policy._looks_like_external_link = lambda event: False
        policy._is_stale_onboarding_cta = lambda event: False
        policy._widget_try_key = FeatureGuidedPolicy._widget_try_key.__get__(policy)
        policy._action_key = FeatureGuidedPolicy._action_key.__get__(policy)
        policy._first_pass_complete = True
        return policy

    def test_setup_feature_does_not_crawl_or_commit(self):
        tmpdir = tempfile.mkdtemp()
        policy = self._policy("Complete first-run setup", tmpdir)
        open_btn = _event("Open")
        state_a = SimpleNamespace(state_str="hash_a")
        first = policy._maybe_hybrid_discovery([open_btn], state_a)
        self.assertIsNone(first)
        self.assertFalse(policy._discovery_done)
        self.assertEqual(policy._discovery_steps, 0)

    def test_repeat_state_stops_after_second_visit(self):
        tmpdir = tempfile.mkdtemp()
        policy = self._policy("Search for a song", tmpdir)
        policy._is_setup_feature = lambda feature=None: False
        open_btn = _event("Open")
        closed_btn = _event("Closed")
        state_a = SimpleNamespace(state_str="hash_a")
        policy._current = None
        first = policy._maybe_hybrid_discovery([open_btn, closed_btn], state_a)
        self.assertIsNotNone(first)
        second = policy._maybe_hybrid_discovery([open_btn, closed_btn], state_a)
        self.assertIsNotNone(second)
        self.assertNotEqual(first.view["text"], second.view["text"])
        third = policy._maybe_hybrid_discovery([open_btn, closed_btn], state_a)
        self.assertIsNone(third)
        self.assertTrue(policy._discovery_done)
        with open(policy.journal.log_path, encoding="utf-8") as handle:
            log_text = handle.read()
        self.assertIn("exited due to repeat-detected", log_text)
        self.assertIn("stopped after 2 actions", log_text)


class BlockedRetryTests(unittest.TestCase):
    def test_retry_pass_requeues_blocked_once(self):
        tmpdir = tempfile.mkdtemp()
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.cfg = FeatureTesterConfig()
        policy.logger = __import__("logging").getLogger("BlockedRetryTests")
        policy.journal = FeatureJournal(tmpdir, app_name="App")
        policy.journal.load_or_create({
            "app": "App",
            "features": [
                {"id": "F001", "name": "Search", "actions": ["Tap Search"]},
                {"id": "F002", "name": "Play", "actions": ["Tap Play"]},
            ],
        })
        policy._retry_pass_started = False
        first = policy.journal.get_feature("F001")
        first["status"] = "blocked"
        first["blocked_no_progress"] = True
        second = policy.journal.get_feature("F002")
        second["status"] = "covered"
        self.assertTrue(policy._start_retry_pass())
        self.assertEqual(first["status"], "pending")
        self.assertTrue(first.get("retry_attempted"))
        self.assertFalse(policy._start_retry_pass())
        recovered = 0
        first["retry_attempted"] = True
        first["completed_on_retry"] = True
        first["status"] = "covered"
        policy.journal.finish_feature(first, "covered", "retry")
        for item in policy.journal.features():
            if item.get("completed_on_retry"):
                recovered += 1
        self.assertEqual(recovered, 1)

    def test_next_work_requeues_blocked_before_hybrid(self):
        tmpdir = tempfile.mkdtemp()
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.cfg = FeatureTesterConfig()
        policy.logger = __import__("logging").getLogger("BlockedRetryTests")
        policy.journal = FeatureJournal(tmpdir, app_name="App")
        policy.journal.load_or_create({
            "app": "App",
            "features": [
                {"id": "F001", "name": "Search", "actions": ["Tap Search"]},
                {"id": "F002", "name": "Play", "actions": ["Tap Play"]},
            ],
        })
        policy._retry_pass_started = False
        policy._first_pass_complete = False
        blocked = policy.journal.get_feature("F001")
        blocked["status"] = "blocked"
        blocked["blocked_no_progress"] = True
        policy.journal.get_feature("F002")["status"] = "covered"
        nxt = policy._next_work_feature()
        self.assertIsNotNone(nxt)
        self.assertEqual(nxt["id"], "F001")
        self.assertEqual(nxt["status"], "pending")
        self.assertTrue(nxt.get("retry_attempted"))
        self.assertTrue(policy._first_pass_complete)
        self.assertTrue(policy._retry_pass_started)


class RunStatsIdentityTests(unittest.TestCase):
    def test_reset_stats_does_not_orphan_imported_singleton(self):
        from droidbot.feature_tester.run_stats import STATS, reset_stats
        from droidbot.feature_tester import run_stats as run_stats_mod
        imported = STATS
        reset_stats()
        imported.record_llm("widget_scoring")
        self.assertIs(run_stats_mod.STATS, imported)
        self.assertEqual(imported.llm_calls["widget_scoring"], 1)
        self.assertEqual(imported.to_dict()["llm_calls_total"], 1)
        reset_stats()
        self.assertEqual(imported.llm_calls["widget_scoring"], 0)


class InterruptFinalizeTests(unittest.TestCase):
    def test_ctrl_c_still_writes_coverage_without_hybrid_llm(self):
        tmpdir = tempfile.mkdtemp()
        os.makedirs(os.path.join(tmpdir, "events"), exist_ok=True)
        gt = os.path.join(tmpdir, "ground_truth.json")
        with open(gt, "w", encoding="utf-8") as handle:
            json.dump({"app": "App", "features": [{"id": "F001", "name": "Search", "actions": ["Tap Search"]}]}, handle)
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy._finished = False
        policy._discovery_done = False
        policy._seen_hub = True
        from droidbot.feature_tester.config import FeatureTesterConfig, set_config
        cfg = FeatureTesterConfig()
        cfg.ground_truth_path = gt
        set_config(cfg)
        policy.cfg = cfg
        policy.chain_memory = ChainMemory()
        policy.logger = __import__("logging").getLogger("InterruptFinalizeTests")
        policy.journal = FeatureJournal(tmpdir, app_name="App")
        policy.journal.load_or_create({
            "app": "App",
            "features": [{"id": "F001", "name": "Search", "actions": ["Tap Search"]}],
        })
        called = []

        def boom(reason=""):
            called.append(reason)
            raise KeyboardInterrupt()

        policy._commit_discovery = boom
        policy._finalize_journal(run_discovery=False)
        self.assertFalse(called)
        self.assertTrue(os.path.isfile(os.path.join(tmpdir, "feature_test", "report.json")))
        self.assertTrue(os.path.isdir(os.path.join(tmpdir, "feature_coverage")))


class DroidBotImeConnectTests(unittest.TestCase):
    def test_unknown_ime_does_not_abort(self):
        from droidbot.adapter.droidbot_ime import DroidBotIme

        class FakeAdb(object):
            def get_installed_apps(self):
                return []

            def shell(self, extra_args, check=True):
                return "Unknown input method io.github.ylimit.droidbotapp/.DroidBotIME cannot be enabled for user #0\n"

            def run_cmd(self, extra_args, check=True):
                return "Success"

        ime = DroidBotIme.__new__(DroidBotIme)
        ime.logger = __import__("logging").getLogger("DroidBotImeConnectTests")
        ime.device = SimpleNamespace(adb=FakeAdb())
        ime.connected = False
        ime.connect()
        self.assertFalse(ime.connected)


class CrossFeatureBankTests(unittest.TestCase):
    def test_later_feature_completes_earlier_partial(self):
        tmpdir = tempfile.mkdtemp()
        journal = FeatureJournal(tmpdir, app_name="Vinyl")
        journal.load_or_create({
            "app": "Vinyl",
            "features": [
                {
                    "id": "F001",
                    "name": "Play a song",
                    "actions": [
                        "Open library",
                        "Tap song",
                        "Open now playing",
                        "Tap pause",
                    ],
                },
                {
                    "id": "F002",
                    "name": "Now playing controls",
                    "actions": ["Open now playing", "Tap pause"],
                },
            ],
        })
        first = journal.get_feature("F001")
        first["status"] = STATUS_PARTIAL
        first["completed_actions"] = ["Open library", "Tap song"]
        first["remaining_actions"] = ["Open now playing", "Tap pause"]
        from droidbot.feature_tester.step_bank import ExplorationBank
        bank = ExplorationBank()
        bank.record(
            {
                "event": "touch Now playing",
                "matched_step": "Open now playing",
                "event_type": "touch",
                "text": "Now playing",
            },
            "F002",
        )
        bank.record(
            {
                "event": "touch Pause",
                "matched_step": "Tap pause",
                "event_type": "touch",
                "text": "Pause",
            },
            "F002",
        )
        upgraded = journal.credit_from_bank(bank)
        first = journal.get_feature("F001")
        self.assertTrue(upgraded)
        self.assertEqual(first["status"], STATUS_COVERED)
        self.assertEqual(first.get("completion_source"), "cross_feature")
        self.assertAlmostEqual(first.get("completion_ratio"), 1.0)
        self.assertIn("F002", first.get("credited_from") or [])
        self.assertEqual(first.get("remaining_actions"), [])


class FeatureSwitchRestartTests(unittest.TestCase):
    def test_restart_before_second_feature(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy._features_finished = 1
        policy._pending_next_feature = None
        policy._restart_between_features = False
        policy._feature_switch_restart = False
        policy._restart_phase = None
        policy._current = None
        policy._last_event_trace = ""
        policy._restarts = 0
        policy._await_dialog = False
        policy._outside_steps = 0
        policy._last_action_key = None
        policy.logger = __import__("logging").getLogger("FeatureSwitchRestartTests")
        policy.journal = SimpleNamespace(_append_log=lambda *a, **k: None)
        policy.app = SimpleNamespace(
            get_stop_intent=lambda: "am force-stop com.poupa.vinylmusicplayer",
            get_start_intent=lambda: "am start com.poupa.vinylmusicplayer/.Main",
        )
        event = policy._start_or_restart_next({"id": "F002", "name": "Search"})
        self.assertIsNotNone(event)
        self.assertEqual(event.event_type, "intent")
        self.assertIn("force-stop", event.intent)
        self.assertTrue(policy._restart_between_features)
        self.assertEqual(policy._pending_next_feature["id"], "F002")
        self.assertEqual(policy._restart_phase, "stop")

    def test_first_feature_does_not_restart(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy._features_finished = 0
        policy._pending_next_feature = None
        policy._restart_between_features = False
        policy._feature_switch_restart = False
        policy._restart_phase = None
        policy._current = None
        policy.logger = __import__("logging").getLogger("FeatureSwitchRestartTests")
        policy.journal = SimpleNamespace(
            start_feature=lambda feat: None,
            _append_log=lambda *a, **k: None,
        )
        begun = []
        policy._begin_feature = lambda nxt: begun.append(nxt)
        event = policy._start_or_restart_next({"id": "F001", "name": "Setup"})
        self.assertIsNone(event)
        self.assertEqual(begun[0]["id"], "F001")


if __name__ == "__main__":
    unittest.main()
