"""Regression tests for first-run, file-picker, and README feature extraction."""

import os
import unittest
from types import SimpleNamespace

from droidbot.feature_tester.advisor import (
    FeatureAdvisor,
    _event_fits_step,
    _is_file_related_step,
    _label_supports_step,
    _looks_like_empty_label,
    _looks_like_search_placeholder,
    _player_step_intent,
    _view_text,
    _widget_player_role,
)
from droidbot.feature_tester.context import retrieve_text
from droidbot.GeminiAI import GeminiAi
from droidbot.feature_tester.fallback_features import extract_features_locally
from droidbot.feature_tester.journal import (
    _followup_submit_step,
    _is_file_related_matched,
    _match_remaining_action,
)
from droidbot.feature_tester.policy import FeatureGuidedPolicy
from droidbot.feature_tester.specs import apply_run_paths, resolve_output_dir
from droidbot.input_event import KeyEvent


def _event(text="", resource_id="", event_type="touch", cls="TextView", nav_label=None):
    return SimpleNamespace(
        event_type=event_type,
        nav_label=nav_label,
        direction="DOWN" if event_type == "scroll" else None,
        name="BACK" if event_type == "key" else None,
        view={
            "text": text,
            "content_description": "",
            "resource_id": resource_id,
            "class": cls,
            "bounds": [[0, 0], [80, 40]],
        },
    )


class OutputAliasTests(unittest.TestCase):
    def test_default_output_dir(self):
        self.assertEqual(resolve_output_dir(None, "apks/money.apk"), os.path.join("output", "money"))
        self.assertEqual(resolve_output_dir(None, "spotube"), os.path.join("output", "spotube"))

    def test_old_outputdir_names(self):
        self.assertEqual(resolve_output_dir("outputDir-money"), os.path.join("output", "money"))
        self.assertEqual(resolve_output_dir("outputDir-spotube2"), os.path.join("output", "spotube"))

    def test_missing_readme_falls_back(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        opts = SimpleNamespace(
            apk_path="money",
            readme_path="feature/money.txt",
            credential_path=None,
            output_dir="outputDir-money",
        )
        self.assertTrue(apply_run_paths(opts, cwd=root))
        self.assertTrue(opts.readme_path.endswith(os.path.join("feature", "money", "README.md")))
        self.assertEqual(opts.output_dir, os.path.join("output", "money"))


class FeatureExtractTests(unittest.TestCase):
    def test_money_readme_yields_database_and_import(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(root, "feature", "money", "README.md")
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        payload = extract_features_locally(text, app_name="Money Manager Ex")
        names = [item["name"].lower() for item in payload["features"]]
        self.assertTrue(any("first-run" in name or "setup" in name for name in names))
        self.assertTrue(any("database" in name for name in names), names)
        self.assertTrue(any("import" in name or "export" in name for name in names), names)
        self.assertFalse(any("explore main" in name for name in names))
        self.assertFalse(any("guest" in name for name in names))

    def test_numbered_gold_list_is_not_used_for_live_extract(self):
        gold = """
1. Create a New Database
Tap Create Database
Enter a file name
Tap Save
2. Add a Transaction
Tap Add Transaction
Enter Amount
Tap Ok
3. Set Up a Budget
Tap Budget
Tap Create
"""
        live = extract_features_locally(
            gold, app_name="Money Manager Ex", allow_numbered_spec=False,
        )
        names = [item["name"] for item in live["features"]]
        self.assertFalse(any(name == "Create a New Database" for name in names), names)
        self.assertTrue(any("first-run" in name.lower() or "setup" in name.lower() for name in names))

    def test_gold_json_is_eval_only_and_not_live_payload(self):
        from droidbot.feature_tester.specs import (
            is_eval_only_feature_list,
            redirect_eval_only_feature_list,
        )
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        gt = os.path.join(root, "feature", "money", "ground_truth.json")
        self.assertTrue(is_eval_only_feature_list(gt))
        opts = SimpleNamespace(features_path=gt, ground_truth_path=None)
        redirect_eval_only_feature_list(opts)
        self.assertIsNone(opts.features_path)
        self.assertEqual(opts.ground_truth_path, os.path.abspath(gt))
        spotube_features = os.path.join(root, "feature", "spotube", "features.json")
        self.assertTrue(is_eval_only_feature_list(spotube_features))


class FilePickerTests(unittest.TestCase):
    def test_save_as_prefers_ok_not_downloads(self):
        events = [
            _event("Downloads", "breadcrumb_text"),
            _event("your_data_20260818.mmb", "title", event_type="set_text", cls="EditText"),
            _event("OK", "button1"),
        ]
        decision = FeatureAdvisor()._file_picker_decision(
            events,
            remaining=["Tap a main navigation item", "Open a list or detail screen"],
        )
        chosen = events[decision.action_index]
        self.assertEqual(chosen.view["text"], "OK")
        self.assertFalse(decision.matched_step)

    def test_new_folder_is_cancelled(self):
        events = [
            _event("New folder", "alertTitle"),
            _event("Folder name", "text1", event_type="set_text", cls="EditText"),
            _event("OK", "button1"),
            _event("CANCEL", "button2"),
        ]
        decision = FeatureAdvisor()._file_picker_decision(
            events,
            remaining=["Enter a file name if asked and confirm Save"],
        )
        chosen = events[decision.action_index]
        self.assertEqual(chosen.view["text"], "CANCEL")

    def test_create_dir_is_not_chosen_on_save(self):
        events = [
            _event("New folder", "option_menu_create_dir"),
            _event("your_data_20260818.mmb", "title", event_type="set_text", cls="EditText"),
            _event("SAVE", "menu_save"),
        ]
        decision = FeatureAdvisor()._file_picker_decision(
            events,
            remaining=["Tap Create Database or Open Database if shown"],
        )
        chosen = events[decision.action_index]
        self.assertEqual(chosen.view["text"], "SAVE")

    def test_file_steps_can_match(self):
        self.assertTrue(_is_file_related_step("Enter a file name if asked and confirm Save"))
        self.assertFalse(_is_file_related_step("Tap a main navigation item"))
        self.assertFalse(_is_file_related_matched(
            "Tap a main navigation item",
            ["Tap a main navigation item"],
        ))


class FillTextTests(unittest.TestCase):
    def test_tuple_text_does_not_crash(self):
        view = {
            "text": ("Search songs",),
            "content_description": ("search",),
            "resource_id": "oss.krtirtho.spotube:id/field",
            "is_password": False,
        }
        value = FeatureAdvisor().fill_text(view, remaining=["Enter a song name"])
        self.assertTrue(isinstance(value, str))

    def test_view_text_flattens_tuples(self):
        self.assertEqual(_view_text(("Search", "songs")), "Search songs")
        self.assertEqual(_view_text(None), "")


class StepMatchTests(unittest.TestCase):
    def test_placeholder_does_not_complete_step(self):
        remaining = ["Enter a song name"]
        self.assertIsNone(_match_remaining_action(
            remaining, "the expected step this action completes or empty",
        ))

    def test_scroll_does_not_complete_plugin_search(self):
        remaining = ["Search for a plugin"]
        self.assertIsNone(_match_remaining_action(
            remaining,
            "Search for a plugin",
            event_str="ScrollEvent DOWN",
            event_type="scroll",
        ))

    def test_tap_does_not_complete_typing(self):
        remaining = ["Enter search query"]
        self.assertIsNone(_match_remaining_action(
            remaining,
            "Enter search query",
            event_str="TouchEvent Search",
            event_type="touch",
        ))

    def test_set_text_completes_typing(self):
        remaining = ["Enter search query"]
        self.assertEqual(
            _match_remaining_action(
                remaining,
                "Enter search query",
                event_str="SetTextEvent",
                event_type="set_text",
            ),
            "Enter search query",
        )

    def test_set_text_does_not_complete_tap_search(self):
        remaining = ["Tap Search"]
        self.assertIsNone(_match_remaining_action(
            remaining,
            "Tap Search",
            event_str="SetTextEvent",
            event_type="set_text",
        ))

    def test_followup_submit_after_typing(self):
        self.assertIsNone(_followup_submit_step(
            ["Tap Search"], "SetTextEvent", "set_text",
        ))
        self.assertIsNone(_followup_submit_step(
            ["Tap the play button next to the song"], "SetTextEvent", "set_text",
        ))

    def test_catalog_label_does_not_complete_step(self):
        remaining = ["Select Playlists"]
        self.assertIsNone(_match_remaining_action(
            remaining,
            "bottom navigation home tab 1 of 5",
            event_str="TouchEvent",
            event_type="touch",
        ))


class CoverageHeuristicTests(unittest.TestCase):
    def test_typing_step_prefers_set_text_over_search_tab(self):
        events = [
            _event("Search", nav_label="bottom navigation search tab 2 of 4"),
            _event("Search songs", resource_id="search_field", event_type="set_text", cls="EditText"),
            _event("Home", nav_label="bottom navigation home tab 1 of 4"),
        ]
        decision = FeatureAdvisor()._heuristic(
            feature={"id": "F003", "name": "Search", "keywords": ["search"]},
            events=events,
            remaining=["Enter search query"],
        )
        chosen = events[decision.action_index]
        self.assertEqual(chosen.event_type, "set_text")
        self.assertGreaterEqual(decision.confidence, 0.55)

    def test_empty_state_copy_is_not_chosen(self):
        events = [
            _event("No records were found. Try adjusting the visible period"),
            _event("Sort", resource_id="menu_sort"),
            _event("Settings", resource_id="menu_settings"),
        ]
        decision = FeatureAdvisor()._heuristic(
            feature={"id": "F007", "name": "Import", "keywords": ["import"]},
            events=events,
            remaining=["Open import from the menu"],
        )
        chosen = events[decision.action_index]
        self.assertNotIn("No records", chosen.view["text"])

    def test_zero_songs_stats_is_empty_and_not_chosen(self):
        self.assertTrue(_looks_like_empty_label("0 songs Streamed overall"))
        self.assertTrue(_looks_like_empty_label("0 tracks"))
        self.assertFalse(_looks_like_empty_label("Search"))
        events = [
            _event("0 songs Streamed overall"),
            _event("Search", resource_id="search"),
        ]
        decision = FeatureAdvisor()._heuristic(
            feature={"id": "F004", "name": "Play a song", "keywords": ["play"]},
            events=events,
            remaining=["Tap on the song in the list"],
        )
        chosen = events[decision.action_index]
        self.assertNotIn("0 songs", chosen.view["text"])

    def test_scroll_does_not_fit_plugin_search_step(self):
        scroll = _event(event_type="scroll")
        self.assertFalse(_event_fits_step(scroll, "Search for a plugin"))

    def test_nav_tab_does_not_complete_search_bar_step(self):
        tab = _event("Search", nav_label="bottom navigation search tab 2 of 4")
        self.assertFalse(_event_fits_step(tab, "Tap on the search bar"))

    def test_unlabeled_nav_does_not_complete_select_audio(self):
        tab = _event("", nav_label="bottom navigation menu tab 5 of 5")
        self.assertFalse(_label_supports_step(tab, "Select Audio"))
        self.assertFalse(_event_fits_step(tab, "Select Audio"))

    def test_set_text_does_not_fit_tap_search(self):
        field = _event("Search songs", event_type="set_text", cls="EditText")
        self.assertFalse(_event_fits_step(field, "Tap Search"))

    def test_select_row_prefers_visible_label(self):
        events = [
            _event("", nav_label="bottom navigation tab 5 of 5"),
            _event("Audio", resource_id="audio_row"),
        ]
        decision = FeatureAdvisor()._heuristic(
            feature={"id": "F008", "name": "Audio", "keywords": ["audio", "settings"]},
            events=events,
            remaining=["Select Audio"],
        )
        chosen = events[decision.action_index]
        self.assertEqual(chosen.view["text"], "Audio")
        self.assertEqual(decision.matched_step, "Select Audio")


class FilterBannedTests(unittest.TestCase):
    def test_does_not_restore_banned_taps(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy._banned_actions = set()
        tap = _event("No records were found. Try adjusting the visible period")
        back = KeyEvent(name="BACK")
        state = SimpleNamespace(state_str="same")
        key = FeatureGuidedPolicy._action_key(policy, state, tap)
        policy._tap_counts = {key: 2}
        policy._looks_like_hub = lambda events, state=None: False
        policy._back_would_leave_app = lambda state: False
        kept = FeatureGuidedPolicy._filter_banned(policy, [tap, back], state)
        self.assertTrue(any(getattr(event, "name", "") == "BACK" for event in kept))
        self.assertFalse(any("No records" in (event.view.get("text") or "") for event in kept if getattr(event, "view", None)))


class RecoverForegroundTests(unittest.TestCase):
    def _policy(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.app = SimpleNamespace(
            get_package_name=lambda: "oss.example.app",
            get_start_intent=lambda: "am start oss.example.app/.Main",
        )
        policy._restarts = 0
        policy._sent_home = False
        policy._outside_steps = 0
        policy._last_event_trace = ""
        policy._last_action_key = None
        policy._current = {"id": "F004"}
        policy._await_dialog = False
        policy.journal = SimpleNamespace(_append_log=lambda *a, **k: None)
        import logging
        policy.logger = logging.getLogger("RecoverForegroundTests")
        policy._seen_hub = True
        policy._is_setup_feature = lambda feature=None: False
        policy._feature_wants_guest_skip = lambda: False
        return policy

    def test_launcher_starts_app_instead_of_back(self):
        policy = self._policy()
        state = SimpleNamespace(
            foreground_activity="com.google.android.apps.nexuslauncher/.NexusLauncherActivity",
            get_app_activity_depth=lambda app: -1,
        )
        event = FeatureGuidedPolicy._maybe_start_app(policy, state)
        self.assertEqual(event.event_type, "intent")
        self.assertIn("start", event.intent)

    def test_keeps_skip_when_back_on_onboarding(self):
        policy = self._policy()
        skip = _event("Skip this nonsense")
        search = _event("Search")
        state = SimpleNamespace(foreground_activity="oss.example.app/.Main")
        kept = FeatureGuidedPolicy._drop_stale_onboarding(policy, [skip, search], state)
        self.assertTrue(any("Skip" in (event.view.get("text") or "") for event in kept))


class EmptyHomeCoverageTests(unittest.TestCase):
    def _policy(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy._seen_hub = True
        policy._interstitial_dismisses = 0
        policy._empty_search_attempted = False
        policy._tap_counts = {}
        policy._current = {
            "id": "F004",
            "name": "Play a song",
            "description": "Play a song from the library or search results.",
            "remaining_actions": ["Tap on the song in the list", "Tap play"],
            "keywords": ["play", "music"],
            "nav_hints": ["play", "play song"],
        }
        return policy

    def test_search_icon_not_completed_by_generic_field(self):
        policy = self._policy()
        policy._current["remaining_actions"] = ["Tap the search icon", "Enter song title"]
        recorded = []
        policy.journal = SimpleNamespace(record_step=lambda feat, step: recorded.append(step))
        policy._screen_blob = lambda state, events: "home"
        field = _event("Name", resource_id="playlist_name", event_type="set_text", cls="EditText")
        FeatureGuidedPolicy._maybe_complete_arrival_steps(
            policy,
            SimpleNamespace(foreground_activity="", screenshot_path=None, state_str="x"),
            [field],
        )
        self.assertEqual(recorded, [])

    def test_search_icon_completed_when_search_field_visible(self):
        policy = self._policy()
        policy._current["remaining_actions"] = ["Tap the search icon", "Enter song title"]
        recorded = []
        policy.journal = SimpleNamespace(record_step=lambda feat, step: recorded.append(step))
        policy._screen_blob = lambda state, events: "search"
        field = _event("Search songs", resource_id="search_query", event_type="set_text", cls="EditText")
        FeatureGuidedPolicy._maybe_complete_arrival_steps(
            policy,
            SimpleNamespace(foreground_activity="", screenshot_path=None, state_str="x"),
            [field],
        )
        self.assertEqual(recorded[0]["matched_step"], "Tap the search icon")

    def test_fallback_skips_empty_stats(self):
        policy = self._policy()
        empty = _event("0 songs Streamed overall")
        share = _event("Share")
        chosen = FeatureGuidedPolicy._fallback_in_app_event(policy, [empty, share], None)
        self.assertEqual(chosen.view["text"], "Share")

    def test_recover_empty_play_uses_search_field(self):
        policy = self._policy()
        empty = _event("0 songs Streamed overall")
        field = _event("", resource_id="search_bar", event_type="set_text", cls="EditText")
        state = SimpleNamespace(
            foreground_activity="app/.Main",
            search_content="",
            get_text_representation=lambda: ("0 songs Streamed overall", "x", []),
        )
        result = FeatureGuidedPolicy._recover_dead_end(policy, [empty, field], state)
        self.assertIsNotNone(result)
        self.assertEqual(result[0].event_type, "set_text")
        self.assertIn("Search from an empty list", result[1])

    def test_interstitial_ignored_after_hub_without_markers(self):
        policy = self._policy()
        policy._screen_blob = lambda state, events: "github donate home library"
        close = _event("", cls="View")
        close.view["bounds"] = [[10, 10], [80, 80]]
        self.assertIsNone(FeatureGuidedPolicy._dismiss_interstitial(policy, None, [close]))

    def test_drop_dead_end_removes_zero_songs(self):
        policy = self._policy()
        empty = _event("0 songs Streamed overall")
        search = _event("Search")
        kept = FeatureGuidedPolicy._drop_dead_end_copy(policy, [empty, search])
        self.assertEqual(len(kept), 1)
        self.assertEqual(kept[0].view["text"], "Search")

    def test_empty_listened_copy_is_dead_end(self):
        self.assertTrue(_looks_like_empty_label("Looks like you haven't listened to anything yet"))
        self.assertTrue(_looks_like_empty_label("0 minutes Listened to music"))
        self.assertTrue(_looks_like_search_placeholder("Search to get results"))
        policy = self._policy()
        empty = _event("Looks like you haven't listened to anything yet")
        search = _event("Search")
        kept = FeatureGuidedPolicy._drop_dead_end_copy(policy, [empty, search])
        self.assertEqual([event.view["text"] for event in kept], ["Search"])

    def test_play_step_does_not_tap_search_placeholder(self):
        events = [
            _event("Search to get results"),
            _event("Taylor Swift - Blank Space"),
        ]
        decision = FeatureAdvisor()._heuristic(
            feature={"id": "F004", "name": "Play a song", "keywords": ["play"]},
            events=events,
            remaining=["Tap on a song in the library or search results"],
        )
        chosen = events[decision.action_index]
        self.assertNotIn("Search to get results", chosen.view["text"])

    def test_song_name_step_uses_search_query_not_playlist(self):
        previous = GeminiAi._credentials
        GeminiAi._credentials = "search_query: Taylor Swift\nplaylist_name: TestCube Playlist\n"
        try:
            text, source = retrieve_text(
                {},
                ["Enter song name or artist"],
                feature={"name": "Search for a song"},
            )
            self.assertEqual(text, "Taylor Swift")
            self.assertEqual(source, "credential")
        finally:
            GeminiAi._credentials = previous

    def test_skip_leaves_onboarding_after_hub(self):
        policy = self._policy()
        policy._is_setup_feature = lambda feature=None: False
        policy._feature_wants_guest_skip = lambda: False
        policy._is_onboarding_screen = lambda state, events: True
        self.assertTrue(FeatureGuidedPolicy._should_dismiss_first_run(policy, None, []))
        policy._is_onboarding_screen = lambda state, events: False
        self.assertFalse(FeatureGuidedPolicy._should_dismiss_first_run(policy, None, []))


class LowSignalAndTextInputTests(unittest.TestCase):
    def test_unlabeled_bottom_nav_forces_visual_ground(self):
        from droidbot.feature_tester.grounding import needs_visual_ground, plausible_typed_value
        events = [
            _event("0 minutes Listened to music"),
            _event("", nav_label="bottom navigation tab 1 of 4"),
            _event("", nav_label="bottom navigation tab 2 of 4"),
            _event("", nav_label="bottom navigation tab 3 of 4"),
            _event("", nav_label="bottom navigation tab 4 of 4"),
        ]
        force, signal = needs_visual_ground(
            {
                "name": "Add a plugin",
                "remaining_actions": ["Open settings", "Add a metadata plugin"],
            },
            events,
        )
        self.assertTrue(force)
        self.assertGreaterEqual(signal["unlabeled_nav"], 3)
        self.assertTrue(signal["destination_missing"])
        self.assertFalse(plausible_typed_value("<button id=0 text='Streaming fees'>"))
        self.assertFalse(plausible_typed_value("Search to get results"))
        self.assertTrue(plausible_typed_value("Taylor Swift"))

    def test_parse_normalized_tap(self):
        from droidbot.feature_tester.grounding import parse_normalized_tap
        self.assertEqual(parse_normalized_tap({"tap_nx": 0.5, "tap_ny": 0.9}, 1080, 2400), (540, 2160))
        self.assertIsNone(parse_normalized_tap({"action_id": 3}, 1080, 2400))

    def test_enter_track_name_emits_set_text(self):
        previous = GeminiAi._credentials
        GeminiAi._credentials = "search_query: Taylor Swift\nplaylist_name: TestCube Playlist\n"
        try:
            field = _event(
                "Search", resource_id="search_bar", event_type="set_text", cls="EditText",
            )
            tab = _event("", nav_label="bottom navigation tab 2 of 4")
            decision = FeatureAdvisor()._heuristic(
                feature={"id": "F003", "name": "Search for a song", "keywords": ["search"]},
                events=[tab, field],
                remaining=["Enter a track name"],
            )
            chosen = [tab, field][decision.action_index]
            self.assertEqual(chosen.event_type, "set_text")
            self.assertTrue(decision.text)
            self.assertNotEqual(decision.text.strip().lower(), "search")
            from droidbot.feature_tester.grounding import plausible_typed_value
            self.assertTrue(plausible_typed_value(decision.text))
        finally:
            GeminiAi._credentials = previous

    def test_unlabeled_rightmost_nav_is_not_boosted(self):
        events = [
            _event("", nav_label="bottom navigation tab 1 of 4"),
            _event("", nav_label="bottom navigation tab 2 of 4"),
            _event("", nav_label="bottom navigation tab 3 of 4"),
            _event("", nav_label="bottom navigation tab 4 of 4"),
            _event("Share"),
        ]
        decision = FeatureAdvisor()._heuristic(
            feature={"id": "F002", "name": "Add a plugin", "keywords": ["plugin", "settings"]},
            events=events,
            remaining=["Open settings", "Add a plugin"],
        )
        chosen = events[decision.action_index]
        self.assertNotEqual(chosen, events[3])


class GranularityTests(unittest.TestCase):
    def test_bundled_playback_settings_is_coarse(self):
        from droidbot.feature_tester.granularity import looks_coarse, refine_granularity
        item = {
            "id": "F010",
            "name": "Customize playback settings",
            "description": "Adjust volume and equalizer and save shuffle/repeat.",
            "actions": [
                "Open settings",
                "Adjust volume",
                "Open equalizer",
                "Toggle shuffle",
                "Toggle repeat",
                "Set sleep timer",
                "Save",
            ],
        }
        self.assertTrue(looks_coarse(item))
        payload = refine_granularity({"features": [item], "app": "Spotube"}, app_name="Spotube")
        self.assertIn("Customize playback settings", payload.get("granularity_flags") or [])


class GuideListAndInputTests(unittest.TestCase):
    def test_guide_list_drives_live_payload(self):
        import json
        import tempfile
        from droidbot.feature_tester.policy import _load_feature_payload
        tmp = tempfile.mkdtemp()
        guide = {
            "app": "Spotube",
            "source": "guide",
            "features": [
                {"id": "F001", "name": "Search for Music", "actions": ["Tap Search", "Type a query"]},
                {"id": "F002", "name": "Play a Track", "actions": ["Tap play"]},
            ],
        }
        gpath = os.path.join(tmp, "guide_features.json")
        with open(gpath, "w", encoding="utf-8") as handle:
            json.dump(guide, handle)
        with open(os.path.join(tmp, "features_from_readme.json"), "w", encoding="utf-8") as handle:
            json.dump({
                "app": "Spotube",
                "features": [
                    {"id": "F001", "name": "Complete first-run setup", "actions": ["Skip"]},
                    {"id": "F002", "name": "Search for Music", "actions": ["Search"]},
                ],
            }, handle)
        payload = _load_feature_payload(
            tmp, None, None, "Spotube", guide_path=gpath,
        )
        self.assertEqual(payload["feature_source"], "guide")
        names = [item["name"] for item in payload["features"]]
        self.assertEqual(names, ["Search for Music", "Play a Track"])
        diff = payload["guide_vs_readme"]
        self.assertEqual(diff["guide_count"], 2)
        self.assertEqual(diff["readme_count"], 2)
        self.assertTrue(any(row.get("guide_name") == "Search for Music" for row in diff["both"]))
        self.assertTrue(any(row.get("name") == "Play a Track" for row in diff["guide_only"]))
        self.assertTrue(any(row.get("name") == "Complete first-run setup" for row in diff["readme_only"]))

    def test_gold_cli_still_eval_only(self):
        from droidbot.feature_tester.specs import (
            is_eval_only_feature_list,
            redirect_eval_only_feature_list,
        )
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        gt = os.path.join(root, "feature", "spotube", "ground_truth.json")
        self.assertTrue(is_eval_only_feature_list(gt))
        opts = SimpleNamespace(features_path=gt, ground_truth_path=None)
        redirect_eval_only_feature_list(opts)
        self.assertIsNone(opts.features_path)

    def test_credential_field_does_not_call_vlm(self):
        previous = GeminiAi._credentials
        orig = GeminiAi.suggest_field_input_for_step
        calls = []

        @classmethod
        def boom(cls, *args, **kwargs):
            calls.append(1)
            return "SHOULD_NOT_USE"

        GeminiAi._credentials = "search_query: Taylor Swift\nplaylist_name: TestCube Playlist\n"
        GeminiAi.suggest_field_input_for_step = boom
        try:
            view = {"text": "Search", "resource_id": "search_query", "class": "EditText"}
            value = FeatureAdvisor().fill_text(
                view, ["Enter a track name"],
                feature={"name": "Search for Music"},
                allow_unresolved=False,
            )
            self.assertEqual(value, "Taylor Swift")
            self.assertEqual(calls, [])
        finally:
            GeminiAi.suggest_field_input_for_step = orig
            GeminiAi._credentials = previous

    def test_unmatched_field_calls_vlm_once(self):
        previous = GeminiAi._credentials
        orig = GeminiAi.suggest_field_input_for_step
        calls = []

        @classmethod
        def fake(cls, view, remaining, feature=None):
            calls.append(1)
            return "ABC-123"

        GeminiAi._credentials = "search_query: Taylor Swift\n"
        GeminiAi.suggest_field_input_for_step = fake
        try:
            view = {"text": "License key", "resource_id": "license_id", "class": "EditText"}
            value = FeatureAdvisor().fill_text(
                view, ["Enter the license key"],
                feature={"name": "Activate product"},
                allow_unresolved=False,
            )
            self.assertEqual(value, "ABC-123")
            self.assertEqual(len(calls), 1)
        finally:
            GeminiAi.suggest_field_input_for_step = orig
            GeminiAi._credentials = previous

    def test_ground_truth_source_same_as_guide(self):
        import json
        import tempfile
        from droidbot.feature_tester.guide import classify_ground_truth_source
        tmp = tempfile.mkdtemp()
        payload = {
            "features": [
                {"id": "F001", "name": "Search for Music"},
                {"id": "F002", "name": "Play a Track"},
            ]
        }
        guide = os.path.join(tmp, "guide_features.json")
        gt = os.path.join(tmp, "ground_truth.json")
        with open(guide, "w", encoding="utf-8") as handle:
            json.dump(payload, handle)
        with open(gt, "w", encoding="utf-8") as handle:
            json.dump(payload, handle)
        self.assertEqual(classify_ground_truth_source(guide, gt), "same_as_guide_list")
        other = os.path.join(tmp, "other.json")
        with open(other, "w", encoding="utf-8") as handle:
            json.dump({"features": [{"id": "GT001", "name": "Something else"}]}, handle)
        self.assertEqual(classify_ground_truth_source(guide, other), "independent_labeled_set")

    def test_benchmark_guides_are_not_copies_of_ground_truth(self):
        from droidbot.feature_tester.guide import classify_ground_truth_source
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for stem in ("spotube", "money", "vinyl"):
            guide = os.path.join(root, "feature", stem, "guide_features.json")
            gt = os.path.join(root, "feature", stem, "ground_truth.json")
            self.assertTrue(os.path.isfile(guide), guide)
            self.assertTrue(os.path.isfile(gt), gt)
            self.assertEqual(
                classify_ground_truth_source(guide, gt),
                "independent_labeled_set",
                stem,
            )

    def test_placeholder_typed_values_are_rejected(self):
        from droidbot.feature_tester.grounding import plausible_typed_value
        self.assertFalse(plausible_typed_value("value if typing"))
        self.assertFalse(plausible_typed_value("why this action advances the remaining step"))
        self.assertTrue(plausible_typed_value("Taylor Swift"))

    def test_near_origin_screenshot_taps_are_rejected(self):
        from droidbot.feature_tester.grounding import parse_normalized_tap
        self.assertIsNone(parse_normalized_tap({"tap_nx": 0.0, "tap_ny": 0.0}, 1080, 1920))
        self.assertIsNone(parse_normalized_tap({"tap_nx": 0.003, "tap_ny": 0.002}, 1080, 1920))
        point = parse_normalized_tap({"tap_nx": 0.5, "tap_ny": 0.8}, 1080, 1920)
        self.assertEqual(point, (540, 1536))
        self.assertIsNone(parse_normalized_tap({"tap_nx": 0.5, "tap_ny": 0.5}, 1080, 2340))

    def test_guest_login_is_treated_as_setup(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy._current = {
            "name": "Guest login",
            "description": "Skip the getting-started screen and continue as a guest.",
            "remaining_actions": ["Skip or continue as guest"],
        }
        self.assertTrue(policy._is_setup_feature())

    def test_music_tabs_count_as_hub(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        tracks = _event("Tracks")
        search = _event("Search")
        state = SimpleNamespace(foreground_activity="app/.AudioServiceActivity")
        self.assertTrue(FeatureGuidedPolicy._looks_like_hub(policy, [tracks, search], state))

    def test_guest_skip_is_not_a_player_next_step(self):
        self.assertEqual(
            _player_step_intent(
                {"name": "Guest login"},
                ["Skip or continue as guest"],
            ),
            "",
        )
        self.assertEqual(
            _player_step_intent(
                {"name": "Next"},
                ["Tap the Next button"],
            ),
            "next",
        )

    def test_open_player_taps_card_not_pause(self):
        pause = _event("", resource_id="mini_player_play_pause_button", cls="ImageButton")
        pause.view["bounds"] = [[900, 1720], [980, 1880]]
        card = _event("Song title", resource_id="mini_player_title", cls="TextView")
        card.view["bounds"] = [[40, 1700], [700, 1900]]
        self.assertEqual(_widget_player_role(pause), "pause")
        self.assertEqual(_widget_player_role(card), "card")
        decision = FeatureAdvisor()._heuristic(
            feature={"id": "F003", "name": "Now playing", "keywords": ["player"]},
            events=[pause, card],
            remaining=["Tap the bottom playing card to open the currently playing screen"],
        )
        chosen = [pause, card][decision.action_index]
        self.assertEqual(chosen.view["resource_id"], "mini_player_title")


if __name__ == "__main__":
    unittest.main()
