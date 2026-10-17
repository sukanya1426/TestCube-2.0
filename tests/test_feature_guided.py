"""Regression tests for first-run, file-picker, and README feature extraction."""

import logging
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
from droidbot.feature_tester.policy import (
    EVICT_AFTER_TRIPS,
    RUN_WIDGET_TAP_CAP,
    MAX_PERMISSION_SCREEN_STEPS,
    MAX_RETRY_ROUNDS,
    MAX_SWITCH_RESTART_TRIES,
    FeatureGuidedPolicy,
)
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


class StepperLoopTests(unittest.TestCase):
    """A widget that mutates the state hash on every tap must still be capped.

    Regression: a date stepper was tapped 68 times in one run. Every tap
    produced a different state_str, so the adjacent-compare loop detectors
    never fired. The ceiling is keyed on widget signature, not (state, view).
    """

    def _policy(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy._banned_actions = set()
        policy._tap_counts = {}
        policy._widget_taps = {}
        policy._looks_like_hub = lambda events, state=None: False
        policy._back_would_leave_app = lambda state: False
        return policy

    def test_widget_ceiling_survives_a_churning_state_hash(self):
        from droidbot.feature_tester.config import get_config
        policy = self._policy()
        stepper = _event("", resource_id="app:id/nextDayButton")
        back = KeyEvent(name="BACK")
        key = FeatureGuidedPolicy._widget_try_key(policy, stepper)
        policy._widget_taps = {key: get_config().max_widget_taps}
        # Each tap lands on a brand-new state, as the real stepper did.
        state = SimpleNamespace(state_str="state-never-seen-before")
        kept = FeatureGuidedPolicy._filter_banned(policy, [stepper, back], state)
        self.assertFalse(
            any(getattr(e, "view", None) and "nextDayButton" in str(e.view.get("resource_id"))
                for e in kept),
            "a widget past its tap ceiling must not be offered again",
        )

    def test_widget_below_ceiling_is_still_offered(self):
        policy = self._policy()
        stepper = _event("", resource_id="app:id/nextDayButton")
        state = SimpleNamespace(state_str="s1")
        key = FeatureGuidedPolicy._widget_try_key(policy, stepper)
        policy._widget_taps = {key: 1}
        kept = FeatureGuidedPolicy._filter_banned(policy, [stepper], state)
        self.assertEqual(len(kept), 1)


class PopulatedListTests(unittest.TestCase):
    """A "0 Songs" stats tile must not mark a populated screen as empty.

    Regression: Vinyl's home screen shows "This month - 0 Songs" next to a
    full song list. The empty-label token matched the whole screen, so the
    tester detoured into search instead of tapping a song, and "Play a song"
    was dropped without ever touching the library.
    """

    def _policy(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy._current = {}
        return policy

    def _row(self, text):
        event = _event(text)
        event.view["clickable"] = True
        return event

    def test_song_rows_beat_a_zero_count_tile(self):
        policy = self._policy()
        events = [
            self._row("This month  -  0 Songs"),
            self._row("TestCube Track One"),
            self._row("TestCube Track Three"),
        ]
        self.assertTrue(
            FeatureGuidedPolicy._has_content_rows(policy, events, None),
            "a screen with real song rows is not empty",
        )

    def test_genuinely_empty_screen_reports_no_content(self):
        policy = self._policy()
        events = [self._row("No results"), self._row("0 Songs")]
        self.assertFalse(
            FeatureGuidedPolicy._has_content_rows(policy, events, None)
        )


class RevisitProgressTests(unittest.TestCase):
    def _policy(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy._no_progress = 0
        policy._last_state_str = None
        policy._feature_seen_states = set()
        policy._seen_run_states = set()
        policy._current = None
        return policy

    def test_revisiting_a_state_is_not_progress(self):
        policy = self._policy()
        for name in ("a", "b", "a", "b"):
            FeatureGuidedPolicy._note_progress(policy, SimpleNamespace(state_str=name))
        self.assertGreater(
            policy._no_progress, 0,
            "an A-B-A-B cycle must register as lack of progress",
        )

    def test_genuinely_new_states_reset_progress(self):
        policy = self._policy()
        for name in ("a", "b", "c", "d"):
            FeatureGuidedPolicy._note_progress(policy, SimpleNamespace(state_str=name))
        self.assertEqual(policy._no_progress, 0)


if __name__ == "__main__":
    unittest.main()


class _FakeJournal(object):
    """Minimal journal: just the feature list and the calls the policy makes."""

    def __init__(self, features):
        self._features = features
        self.logs = []
        self.saved = 0

    def features(self):
        return self._features

    def _append_log(self, line):
        self.logs.append(line)

    def save(self):
        self.saved += 1

    def finish_feature(self, feature, status, reason="", **extra):
        feature["status"] = status
        feature["reason"] = reason


def _policy_shell(features, budget_used=0.1):
    """A FeatureGuidedPolicy with only the fields these paths touch."""
    policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
    policy.journal = _FakeJournal(features)
    policy.logger = logging.getLogger("test.policy")
    policy._retry_pass_started = False
    policy._retry_rounds = 0
    policy._attempt_bonus = 0
    policy._budget_used = lambda: budget_used
    return policy


class RestartRecoveryTests(unittest.TestCase):
    """A failed feature switch is recoverable and must not end the run.

    MAX_SWITCH_RESTART_TRIES=3 spends 4 start attempts per failed switch, so
    with max_restart_attempts=8 two unlucky switches used to trip the
    restart_loop abort. That ended 6 of 17 runs, materialfiles after 3 of its
    60 minutes.
    """

    def test_giving_up_on_one_switch_clears_the_restart_counters(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.journal = _FakeJournal([])
        policy.logger = logging.getLogger("test.policy")
        policy._restart_phase = "start"
        policy._switch_restart_tries = MAX_SWITCH_RESTART_TRIES + 1
        policy._restart_between_features = True
        policy._feature_switch_restart = True
        policy._pending_next_feature = {"id": "G002", "status": "pending"}
        policy._restart_attempts = 7
        policy._restarts = 3

        state = SimpleNamespace(get_app_activity_depth=lambda app: -1)
        policy.app = None
        self.assertIsNone(policy._advance_feature_restart(state))

        self.assertEqual(policy._restart_attempts, 0)
        self.assertEqual(policy._restarts, 0)
        self.assertEqual(policy._pending_next_feature, None)


class RetryRoundTests(unittest.TestCase):
    """Unspent budget must be used, not handed back.

    Across 17 apps TestCube used a mean of 26 minutes of its 60 and stopped
    with all_features_done on 10 of them, while its coverage was still rising.
    """

    def _features(self):
        return [
            {"id": "G001", "status": "covered", "attempts": 1},
            {"id": "G002", "status": "dropped", "attempts": 2},
            {"id": "G003", "status": "partial", "attempts": 2},
            {"id": "G004", "status": "blocked", "attempts": 1},
            {"id": "G005", "status": "not_present", "attempts": 1},
        ]

    def test_first_round_takes_blocked_only(self):
        policy = _policy_shell(self._features())
        self.assertTrue(policy._start_retry_pass())
        by_id = {f["id"]: f for f in policy.journal.features()}
        self.assertEqual(by_id["G004"]["status"], "pending")
        self.assertEqual(by_id["G002"]["status"], "dropped")
        self.assertEqual(by_id["G003"]["status"], "partial")

    def test_later_rounds_reopen_dropped_and_partial(self):
        policy = _policy_shell(self._features())
        self.assertTrue(policy._start_retry_pass())    # blocked
        self.assertTrue(policy._start_retry_pass())    # dropped + partial
        by_id = {f["id"]: f for f in policy.journal.features()}
        self.assertEqual(by_id["G002"]["status"], "pending")
        self.assertEqual(by_id["G003"]["status"], "pending")
        # A feature the app does not have is never worth retrying.
        self.assertEqual(by_id["G005"]["status"], "not_present")
        # Covered work is left alone.
        self.assertEqual(by_id["G001"]["status"], "covered")

    def test_each_round_grants_an_attempt_so_features_are_not_dropped_at_once(self):
        policy = _policy_shell(self._features())
        policy._start_retry_pass()
        self.assertEqual(policy._attempt_bonus, 1)
        policy._start_retry_pass()
        self.assertEqual(policy._attempt_bonus, 2)

    def test_no_new_round_near_the_end_of_the_budget(self):
        policy = _policy_shell(self._features(), budget_used=0.95)
        self.assertFalse(policy._start_retry_pass())
        self.assertEqual(
            [f["status"] for f in policy.journal.features()],
            ["covered", "dropped", "partial", "blocked", "not_present"],
        )

    def test_rounds_are_bounded_so_a_run_still_ends(self):
        policy = _policy_shell(self._features())
        for _ in range(MAX_RETRY_ROUNDS + 4):
            policy._start_retry_pass()
        self.assertLessEqual(policy._retry_rounds, MAX_RETRY_ROUNDS)

    def test_nothing_to_reopen_reports_no_round(self):
        policy = _policy_shell([{"id": "G001", "status": "covered", "attempts": 1}])
        self.assertFalse(policy._start_retry_pass())


class CleanStartTests(unittest.TestCase):
    """Restarting between features is skipped when the app is already home.

    Stop plus start intents were 23% of every action TestCube issued across 17
    runs (564 of 2361) and 62% on materialfiles, and the restart only exists to
    reach a known starting point the hub already is.
    """

    def _policy(self, depth, hub):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.app = object()
        policy.current_state = SimpleNamespace(
            get_app_activity_depth=lambda app: depth,
            foreground_activity="pkg/.MainActivity",
        )
        policy._looks_like_hub = lambda events, state=None: hub
        return policy

    def test_on_the_hub_no_restart_is_needed(self):
        self.assertTrue(self._policy(0, True)._already_at_a_clean_start())

    def test_not_on_the_hub_still_restarts(self):
        self.assertFalse(self._policy(0, False)._already_at_a_clean_start())

    def test_app_in_the_background_still_restarts(self):
        self.assertFalse(self._policy(-1, True)._already_at_a_clean_start())

    def test_no_state_still_restarts(self):
        policy = self._policy(0, True)
        policy.current_state = None
        self.assertFalse(policy._already_at_a_clean_start())

    def test_a_broken_state_object_still_restarts(self):
        policy = self._policy(0, True)

        def boom(app):
            raise RuntimeError("no depth")

        policy.current_state = SimpleNamespace(get_app_activity_depth=boom)
        self.assertFalse(policy._already_at_a_clean_start())


class ViewAtTests(unittest.TestCase):
    """A screenshot-driven tap records the widget it landed on.

    Half of TestCube's actions named no widget at all -- 71 of 142 on
    fossifyclock -- so work it had really done was invisible to anything
    reading the trace. The tap location is unaffected.
    """

    def _state(self, views):
        return SimpleNamespace(views=views)

    def _policy(self):
        return FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)

    def test_picks_the_smallest_identifiable_view_containing_the_point(self):
        state = self._state([
            {"bounds": [[0, 0], [1000, 2000]], "resource_id": "root"},
            {"bounds": [[0, 100], [500, 300]], "text": "Alarm"},
            {"bounds": [[0, 100], [500, 200]], "text": "Alarm tab"},
        ])
        hit = self._policy()._view_at(state, 100, 150)
        self.assertEqual(hit["text"], "Alarm tab")

    def test_containers_without_identity_are_not_used(self):
        state = self._state([
            {"bounds": [[0, 0], [100, 100]], "class": "android.widget.FrameLayout"},
            {"bounds": [[0, 0], [900, 900]], "text": "Settings"},
        ])
        hit = self._policy()._view_at(state, 50, 50)
        self.assertEqual(hit["text"], "Settings")

    def test_a_point_outside_every_view_is_none(self):
        state = self._state([{"bounds": [[0, 0], [10, 10]], "text": "x"}])
        self.assertIsNone(self._policy()._view_at(state, 500, 500))

    def test_malformed_bounds_are_skipped_not_raised(self):
        state = self._state([
            {"bounds": None, "text": "bad"},
            {"bounds": [[0, 0]], "text": "short"},
            {"bounds": [[0, 0], [50, 50]], "text": "good"},
            "not-a-dict",
        ])
        self.assertEqual(self._policy()._view_at(state, 10, 10)["text"], "good")

    def test_no_views_is_none(self):
        self.assertIsNone(self._policy()._view_at(SimpleNamespace(views=None), 1, 1))


class RecoveryCounterTests(unittest.TestCase):
    """The recovery cap means "cannot be brought back", not "dropped out often".

    materialfiles leaves for the system storage-permission screen repeatedly; a
    lifetime cap of 4 was spent by the half-hour mark of a run that was making
    progress the whole time.
    """

    def test_the_app_coming_back_clears_the_recovery_count(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.app = object()
        policy._restarts = 3
        policy._restart_attempts = 7
        policy._restart_recoveries = 4
        state = SimpleNamespace(get_app_activity_depth=lambda app: 0)

        self.assertIsNone(policy._maybe_start_app(state))

        self.assertEqual(policy._restart_recoveries, 0)
        self.assertEqual(policy._restart_attempts, 0)
        self.assertEqual(policy._restarts, 0)

    def test_the_app_still_missing_does_not_clear_it(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.app = object()
        policy._restart_recoveries = 2
        policy._restart_attempts = 1
        policy._restarts = 0
        policy._last_event_trace = ""
        policy._await_dialog = False
        policy._outside_steps = 0
        policy.logger = logging.getLogger("test.policy")
        policy.journal = None
        policy._current = None
        policy.cfg = SimpleNamespace(max_restart_attempts=8)
        policy.app = SimpleNamespace(get_start_intent=lambda: "start")
        state = SimpleNamespace(get_app_activity_depth=lambda app: -1)

        policy._maybe_start_app(state)

        self.assertEqual(policy._restart_recoveries, 2)


class PermissionEscapeTests(unittest.TestCase):
    """A permission screen that will not resolve is abandoned, not explored.

    The "manage all files" grant is a page in system Settings with a toggle,
    and MANAGE_EXTERNAL_STORAGE is an appop that adb pm grant cannot set.
    _outside_kind returns None for any permission screen, which cleared
    _outside_steps and disabled the escape, so the run explored Settings
    instead of the app: 70 of materialfiles' 134 actions were in
    com.android.settings against 54 in the app.
    """

    def test_the_counter_clears_when_the_app_is_back_in_front(self):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.app = object()
        policy._restarts = 1
        policy._restart_attempts = 1
        policy._restart_recoveries = 1
        policy._permission_steps = 3
        state = SimpleNamespace(get_app_activity_depth=lambda app: 0)

        policy._maybe_start_app(state)

        self.assertEqual(policy._permission_steps, 0)

    def test_the_escape_threshold_leaves_room_for_a_real_dialog(self):
        # A normal runtime dialog is granted in one or two steps, so the cap
        # must sit above that or ordinary permission handling would break.
        self.assertGreaterEqual(MAX_PERMISSION_SCREEN_STEPS, 3)


class RetryWithoutBlockedTests(unittest.TestCase):
    """An app with no blocked features must still get retry rounds.

    Gating the first round on blocked features alone meant _retry_pass_started
    stayed False when there were none, so the general rounds were unreachable.
    markor ended its pass with 3 covered and 11 partial, no blocked, and
    stopped with 18 of its 60 minutes unspent having retried nothing.
    """

    def test_partial_features_are_reopened_when_nothing_is_blocked(self):
        features = [
            {"id": "G001", "status": "covered", "attempts": 1},
            {"id": "G002", "status": "partial", "attempts": 2},
            {"id": "G003", "status": "partial", "attempts": 2},
        ]
        policy = _policy_shell(features)
        self.assertTrue(policy._start_retry_pass())
        self.assertEqual(
            [f["status"] for f in features], ["covered", "pending", "pending"])
        self.assertEqual(policy._attempt_bonus, 1)

    def test_a_fully_covered_app_still_reports_no_round(self):
        policy = _policy_shell([
            {"id": "G001", "status": "covered", "attempts": 1},
            {"id": "G002", "status": "not_present", "attempts": 1},
        ])
        self.assertFalse(policy._start_retry_pass())


class ForeignAppEvictionTests(unittest.TestCase):
    """An app that keeps stealing the foreground is force-stopped.

    Open Camera's gallery button hands the screen to Google Photos. BACK and
    HOME did not win it back and the start intent lost the race every time: 62
    of the run's 70 actions were inside Photos, 51 of them start intents, and
    feature coverage fell from 29.97% to 0.61%.
    """

    def _policy(self, own="net.sourceforge.opencamera"):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy.logger = logging.getLogger("test.policy")
        policy.journal = None
        policy.app = SimpleNamespace(get_package_name=lambda: own)
        policy.shelled = []
        policy.device = SimpleNamespace(
            adb=SimpleNamespace(shell=lambda cmd: policy.shelled.append(cmd)))
        return policy

    def test_a_foreign_app_is_stopped(self):
        policy = self._policy()
        self.assertTrue(policy._evict_foreign_app("com.google.android.apps.photos"))
        self.assertEqual(policy.shelled, ["am force-stop com.google.android.apps.photos"])

    def test_the_app_under_test_is_never_stopped(self):
        policy = self._policy()
        self.assertFalse(policy._evict_foreign_app("net.sourceforge.opencamera"))
        self.assertEqual(policy.shelled, [])

    def test_the_launcher_and_system_ui_are_never_stopped(self):
        policy = self._policy()
        for package in ("com.google.android.apps.nexuslauncher",
                        "com.android.systemui", "android"):
            self.assertFalse(policy._evict_foreign_app(package))
        self.assertEqual(policy.shelled, [])

    def test_a_failing_shell_is_reported_not_raised(self):
        policy = self._policy()

        def boom(cmd):
            raise RuntimeError("adb gone")

        policy.device.adb.shell = boom
        self.assertFalse(policy._evict_foreign_app("com.google.android.apps.photos"))

    def test_eviction_waits_for_a_repeat_trip(self):
        # BACK and HOME get a chance first; one excursion must not force-stop.
        self.assertGreaterEqual(EVICT_AFTER_TRIPS, 2)


class TapOracleTests(unittest.TestCase):
    """The screenshot-comparison oracle around each tap is opt-in.

    It only prints its verdict -- the tap is sent either way and the result
    reaches neither the policy nor the return value -- while costing two
    screenshots, a 1.5s sleep and an image-comparison VLM call per clickable
    Button, at least 90s each on the local backend. Open Camera managed 3
    actions in its 63-minute budget and scored 0 feature coverage.
    """

    def test_off_by_default_and_switchable(self):
        from droidbot.custom_input_event import _tap_oracle_enabled
        previous = os.environ.pop("TESTCUBE_TAP_ORACLE", None)
        try:
            self.assertFalse(_tap_oracle_enabled())
            os.environ["TESTCUBE_TAP_ORACLE"] = "1"
            self.assertTrue(_tap_oracle_enabled())
            os.environ["TESTCUBE_TAP_ORACLE"] = "0"
            self.assertFalse(_tap_oracle_enabled())
        finally:
            os.environ.pop("TESTCUBE_TAP_ORACLE", None)
            if previous is not None:
                os.environ["TESTCUBE_TAP_ORACLE"] = previous

    def test_the_tap_is_still_sent_without_the_oracle(self):
        from droidbot.custom_input_event import CustomTouchEvent
        taps = []
        device = SimpleNamespace(
            view_long_touch=lambda x, y, duration=2000: taps.append((x, y, duration)),
            take_screenshot=lambda: self.fail("no screenshot without the oracle"),
        )
        event = CustomTouchEvent(x=120, y=340, view={
            "class": "android.widget.Button", "clickable": True, "bounds": [[0, 0], [240, 680]],
        })
        self.assertTrue(event.send(device))
        self.assertEqual(taps, [(120, 340, 200)])


class ExhaustedWidgetTests(unittest.TestCase):
    """A widget that goes nowhere all run stops being offered.

    max_widget_taps is cleared by _begin_feature, so each feature attempt hands
    the same useless control another allowance. VLC spent its whole hour on a
    permission dialog: touch_outside tapped 96 times, 20 distinct actions out
    of 288, nothing covered.
    """

    def _policy(self, taps):
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy._run_widget_taps = dict(taps)
        return policy

    def test_a_widget_under_the_cap_is_kept(self):
        p = self._policy({"w": RUN_WIDGET_TAP_CAP - 1})
        self.assertFalse(p._widget_is_exhausted("w"))

    def test_a_widget_at_the_cap_is_suppressed(self):
        p = self._policy({"w": RUN_WIDGET_TAP_CAP})
        self.assertTrue(p._widget_is_exhausted("w"))

    def test_revealing_a_new_state_zeroes_the_tally(self):
        # The policy sets the count to 0 when the widget reveals a new state,
        # so it has to earn the full cap again before being suppressed.
        p = self._policy({"w": 0})
        self.assertFalse(p._widget_is_exhausted("w"))

    def test_an_unknown_or_missing_key_is_kept(self):
        p = self._policy({})
        self.assertFalse(p._widget_is_exhausted("never-seen"))
        self.assertFalse(p._widget_is_exhausted(None))

    def test_the_cap_survives_a_feature_switch(self):
        # _begin_feature clears _widget_taps; the run-level tally must persist.
        policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
        policy._run_widget_taps = {"w": RUN_WIDGET_TAP_CAP}
        policy._widget_taps = {}          # as _begin_feature leaves it
        self.assertTrue(policy._widget_is_exhausted("w"))
