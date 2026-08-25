"""Tests for TestCube feature-coverage evaluation.

These tests use synthetic traces. They do not run dfs_greedy, Gemini
text input, or ImageComparer.
"""

import json
import os
import tempfile
import unittest

from droidbot.feature_eval.coverage import CoverageCalculator
from droidbot.feature_eval.evaluator import evaluate_feature_coverage
from droidbot.feature_eval.feature_loader import FeatureLoader
from droidbot.feature_eval.matcher import FeatureMatcher
from droidbot.feature_eval.models import (
    STATUS_COVERED,
    STATUS_NOT_COVERED,
    STATUS_PARTIAL,
    ExecutionTrace,
    Feature,
    FeatureResult,
    ObservedAction,
    TestCaseTrace,
)
from droidbot.feature_eval.report import ReportGenerator
from droidbot.feature_eval.trace_loader import TraceLoader


def action(event_type, test_case="test_001", **kwargs):
    values = {
        "index": kwargs.pop("index", 0),
        "tag": kwargs.pop("tag", "t"),
        "test_case": test_case,
        "event_type": event_type,
    }
    values.update(kwargs)
    return ObservedAction(**values)


def make_trace(actions, test_id="test_001"):
    labeled = []
    for index, item in enumerate(actions):
        item.index = index
        item.test_case = test_id
        labeled.append(item)
    return ExecutionTrace(
        actions=labeled,
        test_cases=[TestCaseTrace(id=test_id, actions=labeled)],
    )


class FeatureLoaderTests(unittest.TestCase):
    def test_stable_ids_and_valid_paths(self):
        payload = {
            "app": "Spotube",
            "features": [
                {
                    "id": "F001",
                    "name": "Search for a song",
                    "actions": ["Open search", "Enter search query"],
                },
                {
                    "id": "F002",
                    "name": "Play a song",
                    "valid_paths": [
                        ["Search", "Play"],
                        ["Album", "Play"],
                    ],
                },
            ],
        }
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(payload, handle)
            path = handle.name
        try:
            loaded = FeatureLoader().load(path)
        finally:
            os.remove(path)
        self.assertEqual(loaded["app"], "Spotube")
        self.assertEqual([item.id for item in loaded["features"]], ["F001", "F002"])
        self.assertEqual(len(loaded["features"][1].paths()), 2)


class DeterministicMatchingTests(unittest.TestCase):
    def setUp(self):
        self.matcher = FeatureMatcher(use_llm=False)

    def test_exact_match_covered(self):
        feature = Feature(
            id="F001",
            name="Search for a song",
            actions=["tap Search", "input query", "tap Search"],
        )
        trace = make_trace([
            action("touch", view_text="Search", view_class="android.widget.Button"),
            action("set_text", resource_id="app:id/search_query", text_input="Imagine Dragons", view_text="query"),
            action("touch", view_text="Search", view_class="android.widget.Button"),
        ])
        result = self.matcher.match_feature(feature, trace)
        self.assertEqual(result.status, STATUS_COVERED)
        self.assertEqual(result.test_cases, ["test_001"])

    def test_semantic_match_click_search_icon(self):
        feature = Feature(
            id="F001",
            name="Search for a song",
            actions=["Tap Search"],
        )
        trace = make_trace([
            action(
                "touch",
                content_description="search icon",
                view_class="android.widget.ImageView",
            ),
        ])
        result = self.matcher.match_feature(feature, trace)
        self.assertEqual(result.status, STATUS_COVERED)

    def test_partial_execution_not_counted_as_covered(self):
        feature = Feature(
            id="F001",
            name="Search for a song",
            actions=[
                "Open search",
                "Enter search query",
                "Submit search",
            ],
        )
        trace = make_trace([
            action("touch", content_description="search icon"),
            action("set_text", resource_id="app:id/search_query", view_text="Search"),
        ])
        result = self.matcher.match_feature(feature, trace)
        self.assertEqual(result.status, STATUS_PARTIAL)
        coverage = CoverageCalculator().calculate("Spotube", [result])
        self.assertEqual(coverage.covered_features, 0)
        self.assertEqual(coverage.partial_features, 1)
        self.assertEqual(coverage.exercised_features, 1)
        self.assertEqual(coverage.coverage, 0.0)
        self.assertEqual(coverage.coverage_formula, "covered / total")
        self.assertAlmostEqual(coverage.weighted_coverage, 2.0 / 3.0)
        self.assertAlmostEqual(result.completion_ratio, 2.0 / 3.0)

    def test_incomplete_long_path_stays_partial(self):
        """A matching prefix is kept as PARTIAL even when average path confidence is low."""
        feature = Feature(
            id="F002",
            name="Create First/New Account",
            actions=[
                "Tap Add Account (+)",
                "Enter an Account Name",
                "Select an Account Type",
                "Select Currency",
                "Enter Initial Balance",
                "Set Opening Date",
                "Optionally toggle Set as Default",
                "Tap Save or OK",
            ],
        )
        trace = make_trace([
            action("touch", view_text="Add Account", view_class="android.widget.Button"),
        ])
        result = self.matcher.match_feature(feature, trace)
        self.assertEqual(result.status, STATUS_PARTIAL)
        self.assertTrue(result.evidence)

    def test_ui_discovery_is_not_coverage(self):
        feature = Feature(
            id="F004",
            name="Add song to playlist",
            actions=["Tap add to playlist", "Select playlist", "Confirm add"],
        )
        # The destination screen mentions the button, but TestCube never tapped it.
        trace = make_trace([
            action(
                "touch",
                view_text="Home",
                stop_texts=["Add to Playlist", "Liked songs"],
                state_changed=True,
            ),
        ])
        result = self.matcher.match_feature(feature, trace)
        self.assertEqual(result.status, STATUS_NOT_COVERED)

    def test_repeated_coverage_counts_once(self):
        feature = Feature(id="F001", name="Search for a song", actions=["Tap Search"])
        sessions = []
        all_actions = []
        for index in range(3):
            test_id = "test_%03d" % (index + 1)
            item = action("touch", test_case=test_id, view_text="Search")
            item.index = index
            sessions.append(TestCaseTrace(id=test_id, actions=[item]))
            all_actions.append(item)
        trace = ExecutionTrace(actions=all_actions, test_cases=sessions)
        result = self.matcher.match_feature(feature, trace)
        self.assertEqual(result.status, STATUS_COVERED)
        self.assertEqual(result.test_cases, ["test_001", "test_002", "test_003"])
        coverage = CoverageCalculator().calculate("Spotube", [result])
        self.assertEqual(coverage.covered_features, 1)
        self.assertEqual(coverage.total_features, 1)

    def test_multiple_paths_count_once(self):
        feature = Feature(
            id="F002",
            name="Play a song",
            valid_paths=[
                ["Open search", "Press play"],
                ["Open album", "Press play"],
            ],
        )
        path_a = make_trace([
            action("touch", view_text="Search"),
            action("touch", view_text="Play"),
        ], test_id="test_001")
        path_b_actions = [
            action("touch", view_text="Album", test_case="test_002"),
            action("touch", view_text="Play", test_case="test_002"),
        ]
        for index, item in enumerate(path_b_actions):
            item.index = index
        trace = ExecutionTrace(
            actions=path_a.actions + path_b_actions,
            test_cases=[
                path_a.test_cases[0],
                TestCaseTrace(id="test_002", actions=path_b_actions),
            ],
        )
        result = self.matcher.match_feature(feature, trace)
        self.assertEqual(result.status, STATUS_COVERED)
        coverage = CoverageCalculator().calculate("Spotube", [result])
        self.assertEqual(coverage.covered_features, 1)

    def test_no_traces_zero_coverage(self):
        features = [
            Feature(id="F%03d" % (i + 1), name="Feature %d" % (i + 1), actions=["Tap Search"])
            for i in range(20)
        ]
        trace = ExecutionTrace(actions=[], test_cases=[])
        results = self.matcher.match_all(features, trace)
        coverage = CoverageCalculator().calculate("Spotube", results)
        self.assertEqual(coverage.total_features, 20)
        self.assertEqual(coverage.covered_features, 0)
        self.assertEqual(coverage.coverage, 0.0)

    def test_full_coverage(self):
        features = [
            Feature(id="F%03d" % (i + 1), name="Tap %d" % i, actions=["Tap Search"])
            for i in range(10)
        ]
        trace = make_trace([action("touch", view_text="Search")])
        results = self.matcher.match_all(features, trace)
        coverage = CoverageCalculator().calculate("Spotube", results)
        self.assertEqual(coverage.covered_features, 10)
        self.assertEqual(coverage.total_features, 10)
        self.assertEqual(coverage.coverage, 1.0)
        self.assertEqual(coverage.coverage_percentage, 100.0)

    def test_out_of_order_steps_still_cover(self):
        feature = Feature(
            id="F001",
            name="Search for a song",
            actions=["tap Search", "input query"],
        )
        trace = make_trace([
            action("set_text", resource_id="app:id/search_query", text_input="Imagine Dragons", view_text="query"),
            action("touch", view_text="Search", view_class="android.widget.Button"),
        ])
        result = self.matcher.match_feature(feature, trace)
        self.assertEqual(result.status, STATUS_COVERED)

    def test_partial_and_covered_both_count_in_coverage(self):
        covered = FeatureResult(
            id="F001", name="A", status=STATUS_COVERED, confidence=0.9,
        )
        partial = FeatureResult(
            id="F002", name="B", status=STATUS_PARTIAL, confidence=0.6,
        )
        missing = FeatureResult(
            id="F003", name="C", status=STATUS_NOT_COVERED, confidence=0.0,
        )
        coverage = CoverageCalculator().calculate("Spotube", [covered, partial, missing])
        self.assertEqual(coverage.covered_features, 1)
        self.assertEqual(coverage.partial_features, 1)
        self.assertEqual(coverage.uncovered_features, 1)
        self.assertEqual(coverage.exercised_features, 2)
        self.assertAlmostEqual(coverage.coverage, 1.0 / 3.0)
        self.assertAlmostEqual(coverage.weighted_coverage, 0.5)


class TraceLoaderTests(unittest.TestCase):
    def test_reconstructs_linear_trace_from_event_json(self):
        with tempfile.TemporaryDirectory() as root:
            event_dir = os.path.join(root, "events")
            state_dir = os.path.join(root, "states")
            os.makedirs(event_dir)
            os.makedirs(state_dir)
            start_state = {
                "tag": "2025-08-04_151136",
                "state_str": "state-a",
                "foreground_activity": "com.example.splapp/.Login",
                "views": [{"text": "Email", "content_description": None}],
            }
            stop_state = {
                "tag": "2025-08-04_151145",
                "state_str": "state-b",
                "foreground_activity": "com.example.splapp/.Home",
                "views": [{"text": "Search", "content_description": None}],
            }
            with open(os.path.join(state_dir, "state_2025-08-04_151136.json"), "w") as handle:
                json.dump(start_state, handle)
            with open(os.path.join(state_dir, "state_2025-08-04_151145.json"), "w") as handle:
                json.dump(stop_state, handle)
            events = [
                {
                    "tag": "2025-08-04_151130",
                    "event": {"event_type": "kill_app", "stop_intent": "am force-stop com.example.splapp"},
                    "start_state": "state-a",
                    "stop_state": "state-a",
                    "event_str": "KillAppEvent()",
                },
                {
                    "tag": "2025-08-04_151136",
                    "event": {
                        "event_type": "set_text",
                        "text": "",
                        "view": {
                            "text": "Enter your email",
                            "content_description": None,
                            "resource_id": "com.example.splapp:id/etEmail",
                            "class": "android.widget.EditText",
                        },
                    },
                    "start_state": "state-a",
                    "stop_state": "state-a",
                    "event_str": "CustomSetTextEvent(... EditText-Enter your)",
                },
                {
                    "tag": "2025-08-04_151145",
                    "event": {
                        "event_type": "touch",
                        "view": {
                            "text": "Login",
                            "content_description": None,
                            "resource_id": "com.example.splapp:id/btnLogin",
                            "class": "android.widget.Button",
                        },
                    },
                    "start_state": "state-a",
                    "stop_state": "state-b",
                    "event_str": "CustomTouchEvent(... Button-Login)",
                },
            ]
            for item in events:
                with open(os.path.join(event_dir, "event_%s.json" % item["tag"]), "w") as handle:
                    json.dump(item, handle)

            trace = TraceLoader().load(root)
            self.assertEqual([item.event_type for item in trace.actions], ["kill_app", "set_text", "touch"])
            self.assertEqual(trace.actions[1].resource_id, "com.example.splapp:id/etEmail")
            self.assertTrue(trace.actions[2].state_changed)
            self.assertEqual(trace.actions[2].stop_activity, "com.example.splapp/.Home")
            self.assertGreaterEqual(len(trace.test_cases), 1)


class EvaluatorIntegrationTests(unittest.TestCase):
    def test_writes_report_without_touching_existing_output(self):
        with tempfile.TemporaryDirectory() as root:
            event_dir = os.path.join(root, "events")
            os.makedirs(event_dir)
            with open(os.path.join(event_dir, "event_2025-08-04_151145.json"), "w") as handle:
                json.dump({
                    "tag": "2025-08-04_151145",
                    "event": {
                        "event_type": "touch",
                        "view": {
                            "text": "Search",
                            "class": "android.widget.Button",
                            "resource_id": "app:id/search",
                            "content_description": None,
                        },
                    },
                    "start_state": "a",
                    "stop_state": "b",
                    "event_str": "CustomTouchEvent(Search)",
                }, handle)
            features_path = os.path.join(root, "features.json")
            with open(features_path, "w") as handle:
                json.dump({
                    "app": "Spotube",
                    "features": [
                        {"id": "F001", "name": "Search for a song", "actions": ["Tap Search"]},
                        {"id": "F002", "name": "Create playlist", "actions": ["Tap create playlist"]},
                    ],
                }, handle)
            sentinel = os.path.join(root, "utg.js")
            with open(sentinel, "w") as handle:
                handle.write('var utg = {"nodes": [], "edges": [], "app_package": "oss.krtirtho.spotube"}\n')

            report, paths = evaluate_feature_coverage(
                results_dir=root,
                features_path=features_path,
                use_llm=False,
            )
            self.assertTrue(os.path.isfile(paths["json"]))
            self.assertTrue(os.path.isfile(paths["txt"]))
            self.assertTrue(os.path.isfile(sentinel))
            self.assertEqual(report.total_features, 2)
            self.assertEqual(report.covered_features, 1)
            self.assertEqual(report.coverage_percentage, 50.0)
            text = ReportGenerator().render_text(report)
            self.assertIn("F001", text)
            self.assertIn("COVERED", text)
            self.assertIn("NOT COVERED", text)


class VlmCoverageJudgeTests(unittest.TestCase):
    def test_ai_covers_when_labels_do_not_match_gold_wording(self):
        class FakeJudge(object):
            def judge(self, feature, trace, readme_text=""):
                return {
                    "status": "covered",
                    "confidence": 0.91,
                    "reasoning": "Opened search, typed a track, and results appeared.",
                    "evidence": ["set_text Taylor Swift"],
                }

        matcher = FeatureMatcher(
            use_llm=True, llm_matcher=FakeJudge(), matcher_mode="ai",
        )
        feature = Feature(
            id="F001",
            name="Search for Music",
            actions=["Tap the Search tab", "Enter a track name"],
        )
        trace = make_trace([
            action("touch", view_text="", content_description="", view_class="ImageView"),
            action("set_text", text_input="Taylor Swift"),
        ])
        result = matcher.match_feature(feature, trace)
        self.assertEqual(result.status, STATUS_COVERED)
        self.assertEqual(result.matcher, "vlm")
        self.assertIn("Opened search", " ".join(result.evidence))

    def test_ai_rejects_token_overlap_that_is_not_the_feature(self):
        class FakeJudge(object):
            def judge(self, feature, trace, readme_text=""):
                return {
                    "status": "not_covered",
                    "confidence": 0.86,
                    "reasoning": "The Search token was a settings row, not music search.",
                    "evidence": ["touch Settings Search"],
                }

        matcher = FeatureMatcher(
            use_llm=True, llm_matcher=FakeJudge(), matcher_mode="ai",
        )
        feature = Feature(
            id="F001",
            name="Search for Music",
            actions=["tap Search"],
        )
        trace = make_trace([
            action("touch", view_text="Search", view_class="android.widget.Button"),
        ])
        token = FeatureMatcher(use_llm=False).match_feature(feature, trace)
        self.assertEqual(token.status, STATUS_COVERED)
        result = matcher.match_feature(feature, trace)
        self.assertEqual(result.status, STATUS_NOT_COVERED)
        self.assertEqual(result.matcher, "vlm")

    def test_ai_batch_judge_all_scores_every_feature(self):
        class FakeJudge(object):
            def judge(self, feature, trace, readme_text=""):
                return None

            def judge_all(self, features, trace, readme_text=""):
                out = []
                for feature in features:
                    out.append({
                        "feature_id": feature.id,
                        "status": "partial" if feature.id == "F002" else "covered",
                        "confidence": 0.8,
                        "reasoning": "batch",
                        "evidence": ["tap"],
                    })
                return out

        matcher = FeatureMatcher(
            use_llm=True, llm_matcher=FakeJudge(), matcher_mode="ai",
        )
        features = [
            Feature(id="F001", name="A", actions=["Tap Search"]),
            Feature(id="F002", name="B", actions=["Tap Play"]),
        ]
        trace = make_trace([action("touch", view_text="Search")])
        results = matcher.match_all(features, trace)
        self.assertEqual([item.status for item in results], ["covered", "partial"])
        coverage = CoverageCalculator().calculate("Spotube", results)
        self.assertEqual(coverage.exercised_features, 2)
        self.assertEqual(coverage.covered_features, 1)
        self.assertEqual(coverage.partial_features, 1)
        self.assertAlmostEqual(coverage.coverage, 0.5)
        self.assertAlmostEqual(coverage.weighted_coverage, 0.75)

        from droidbot.feature_eval.llm_matcher import extract_json_list
        recovered = extract_json_list(
            '```json\n[{"feature_id":"F001","status":"covered","confidence":0.9,'
            '"reasoning":"ok","evidence":["tap"]},\n{"feature_id":"F002","status":"partial"'
        )
        self.assertEqual(recovered[0]["feature_id"], "F001")
        self.assertEqual(recovered[0]["status"], "covered")

    def test_ai_failure_does_not_fall_back_to_string_matching(self):
        class FakeJudge(object):
            def judge(self, feature, trace, readme_text=""):
                return None

        matcher = FeatureMatcher(
            use_llm=True, llm_matcher=FakeJudge(), matcher_mode="ai",
        )
        feature = Feature(
            id="F001",
            name="Search for a song",
            actions=["tap Search", "input query"],
        )
        trace = make_trace([
            action("touch", view_text="Search", view_class="android.widget.Button"),
            action("set_text", resource_id="app:id/search_query", text_input="x", view_text="query"),
        ])
        result = matcher.match_feature(feature, trace)
        self.assertEqual(result.status, STATUS_NOT_COVERED)
        self.assertEqual(result.matcher, "vlm")


class EvidenceSelectionTest(unittest.TestCase):
    """Evidence handed to the LLM judge must come from the whole trace.

    Regression: keywords were substring-matched against a blob containing
    "android.widget.*", so the stopword "and" matched every action. The
    filter selected the entire trace and then kept the FIRST max_actions
    entries -- app startup -- so real evidence later in a long run was
    never shown to the judge and every feature scored 0.
    """

    def _long_trace(self, relevant_index=300, total=400):
        from droidbot.feature_eval.llm_matcher import LLMMatcher  # noqa: F401
        actions = []
        for i in range(total):
            if i == relevant_index:
                actions.append(action(
                    "touch", view_text="Shuffle all",
                    resource_id="app:id/title",
                    view_class="android.widget.TextView",
                ))
            else:
                actions.append(action(
                    "touch", resource_id="app:id/player_repeat_button",
                    view_class="android.widget.ImageButton",
                ))
        return make_trace(actions)

    def _shuffle_feature(self):
        return Feature(
            id="F009", name="Shuffle All",
            description="Start shuffled playback from the overflow menu.",
            actions=["Tap the three dot overflow menu", "Tap Shuffle all"],
        )

    def test_stopwords_do_not_match_android_widget_classes(self):
        from droidbot.feature_eval.llm_matcher import (
            _informative_keywords, _keyword_hits, _tokens,
        )
        keywords = _informative_keywords(self._shuffle_feature())
        self.assertNotIn("and", keywords)
        noise = _tokens("touch app:id/player_repeat_button android.widget.ImageButton")
        self.assertEqual(_keyword_hits(noise, keywords), 0)
        real = _tokens("touch Shuffle all app:id/title android.widget.TextView")
        self.assertGreater(_keyword_hits(real, keywords), 0)

    def test_relevant_action_late_in_trace_is_selected(self):
        from droidbot.feature_eval.llm_matcher import LLMMatcher
        trace = self._long_trace(relevant_index=300, total=400)
        selected = LLMMatcher()._select_actions(self._shuffle_feature(), trace)
        self.assertTrue(
            any(a.view_text == "Shuffle all" for a in selected),
            "evidence at index 300 must reach the judge, not be truncated away",
        )

    def test_selection_stays_chronological(self):
        from droidbot.feature_eval.llm_matcher import LLMMatcher
        trace = self._long_trace()
        selected = LLMMatcher()._select_actions(self._shuffle_feature(), trace)
        indexes = [a.index for a in selected]
        self.assertEqual(indexes, sorted(indexes))


if __name__ == "__main__":
    unittest.main()
