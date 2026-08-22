"""Walk README features one by one instead of randomly exploring the UI."""

import json
import logging
import os
import re
import time

from droidbot.input_event import IntentEvent, KeyEvent, LongTouchEvent, ScrollEvent, SetTextEvent
from droidbot.input_policy import (
    EVENT_FLAG_START_APP,
    EVENT_FLAG_STOP_APP,
    InputInterruptedException,
    UtgBasedInputPolicy,
)
from droidbot.permission_dialog import (
    grant_runtime_permissions,
    is_permission_screen,
    make_allow_event,
    normalize_label,
)
from .advisor import (
    EMPTY_TOKENS,
    ERROR_TOKENS,
    FeatureAdvisor,
    _dead_end_text,
    _event_label,
    _is_set_text,
    _is_typing_step,
    _looks_like_empty_label,
    _looks_like_error_label,
    _looks_like_loading_label,
    _looks_like_search_placeholder,
    _player_step_intent,
    _tokens,
    _view_text,
    _visible_label,
    _widget_player_role,
)
from .chain_memory import ChainMemory, decide_shared_flow
from .config import get_config
from .fallback_features import extract_features_locally
from .journal import (
    FeatureJournal,
    STATUS_BLOCKED,
    STATUS_COVERED,
    STATUS_DROPPED,
    STATUS_NOT_PRESENT,
    STATUS_PARTIAL,
)
from .mechanisms import (
    feature_keywords,
    find_affordance_event,
    is_stagnant,
    needs_affordance_search,
    non_idempotent_key,
    pick_untried_plausible,
)
from .run_stats import STATS, reset_stats
from .signatures import widget_signature
from .step_bank import ExplorationBank
from .test_cases import append_step_payload


ONBOARDING_CTA = (
    "let's get started",
    "lets get started",
    "get started",
    "start now",
    "continue",
    "next",
    "got it",
    "i agree",
    "accept",
)
SKIP_CTA = (
    "skip this nonsense",
    "continue as guest",
    "skip",
    "maybe later",
    "not now",
    "close",
    "done",
    "finish",
    "got it",
)

MAX_STEPS_PER_FEATURE = 60
MAX_NO_PROGRESS = 12
MAX_OUTSIDE_STEPS = 6
MAX_FILE_PICKER_STEPS = 8
MAX_RESTARTS = 5
MIN_STEPS_BEFORE_ABSENT = 16

FILE_PICKER_MARKERS = (
    "documentsui",
    "documentsui.picker",
    "filepicker",
    "fileexplorer",
    "com.android.documentsui",
    "com.google.android.documentsui",
    "com.google.android.apps.photos",
    "com.android.gallery3d",
    "com.google.android.providers.media",
    "com.android.intentresolver",
)

BROWSER_MARKERS = (
    "com.android.chrome",
    "org.chromium",
    "com.android.browser",
    "customtab",
    "customtabs",
    "com.google.android.gm",
    "youtube.music",
    "audiopreview",
)

INTERSTITIAL_MARKERS = (
    "help this project grow",
    "contribute on github",
    "donate on open collective",
    "install a metadata provider",
)
PROMO_TOKENS = (
    "github",
    "donate",
    "patreon",
    "open collective",
    "buy me a coffee",
)

CLOSE_CTA = (
    "skip this nonsense",
    "continue as guest",
    "maybe later",
    "not now",
    "no thanks",
    "close",
    "dismiss",
)


class FeatureGuidedPolicy(UtgBasedInputPolicy):
    def __init__(self, device, app, random_input):
        super(FeatureGuidedPolicy, self).__init__(device, app, random_input)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.journal = None
        self.advisor = None
        self._ready = False
        self._current = None
        self._feature_steps = 0
        self._no_progress = 0
        self._outside_steps = 0
        self._restarts = 0
        self._last_state_str = None
        self._last_event_trace = ""
        self._finished = False
        self._granted_perms = False
        self._await_dialog = False
        self._switch_depth = 0
        self._recent_states = []
        self._tap_counts = {}
        self._seen_hub = False
        self._onboarding_states = set()
        self._banned_actions = set()
        self._last_action_key = None
        self._waited_states = set()
        self._sent_home = False
        self._create_db_taps = 0
        self.cfg = get_config()
        self.chain_memory = ChainMemory()
        self._feature_sigs = []
        self._backtrack_count = 0
        self._afford_tried = set()
        self._tried_on_state = {}
        self._tried_widgets = set()
        self._seen_run_states = set()
        self._novelty_window = []
        self._remaining_window = []
        self._stagnation_last = None
        self._stagnation_escalated = False
        self._discovery_done = False
        self._discovery_phase = False
        self._discovery_steps = 0
        self._discovery_pairs = set()
        self._discovery_seen_states = set()
        self._discovery_tried_widgets = set()
        self._discovery_label_baseline = 0
        self._discovery_state_repeats = {}
        self._observed_labels = []
        self._interstitial_dismisses = 0
        self._empty_search_attempted = False
        self._waited_loading = set()
        self._feature_seen_states = set()
        self._states_before_feature = set()
        self._feature_reset_tried = False
        self._retry_pass_started = False
        self._first_pass_complete = False
        self._pending_fill = None
        self._pending_next_feature = None
        self._restart_between_features = False
        self._feature_switch_restart = False
        self._restart_phase = None
        self._features_finished = 0
        self.step_bank = ExplorationBank()
        self._unresolved_fields = set()
        self._input_manager = None
        self._recent_coords = []

    def start(self, input_manager):
        """Do not KillApp first — that dismisses the permission dialog with HOME."""
        self.action_count = 0
        self._input_manager = input_manager
        interrupted = False
        try:
            self._ensure_ready()
            self._grant_permissions()
            while input_manager.enabled and self.action_count < input_manager.event_count:
                try:
                    event = self.generate_event()
                    input_manager.add_event(event)
                except KeyboardInterrupt:
                    interrupted = True
                    self.logger.info("Keyboard interrupt; writing coverage report.")
                    break
                except InputInterruptedException as exc:
                    self.logger.warning("stop sending events: %s" % exc)
                    break
                except Exception as exc:
                    self.logger.warning("exception during sending events: %s" % exc)
                    import traceback
                    traceback.print_exc()
                    continue
                self.action_count += 1
        finally:
            if self.journal and not self._finished:
                if self._input_manager and self.action_count >= getattr(self._input_manager, "event_count", 0):
                    never = [
                        item.get("id") for item in self.journal.features()
                        if item.get("source") != "action_inferred"
                        and not item.get("attempts")
                        and not item.get("steps")
                    ]
                    if never:
                        line = (
                            "Run hit event budget with features never attempted: %s"
                            % ", ".join(never)
                        )
                        self.logger.info(line)
                        self.journal._append_log(line)
                        self.journal.session["never_attempted"] = never
                self._finalize_journal(run_discovery=not interrupted)
                self.logger.info(
                    "Feature test report: %s" % self.journal.report_md_path
                )

    def _grant_permissions(self):
        if self._granted_perms:
            return
        try:
            grant_runtime_permissions(self.device, self.app)
        except Exception as exc:
            self.logger.warning("Could not pre-grant permissions: %s" % exc)
        self._granted_perms = True

    def generate_event_based_on_utg(self):
        self._ensure_ready()
        state = self.current_state
        if state is None:
            return KeyEvent(name="BACK")

        if self._current:
            self._note_progress(state)

        if self._restart_between_features:
            switched = self._advance_feature_restart(state)
            if switched is not None:
                return switched

        if self.journal.all_done() and not self._hybrid_still_pending():
            self._finish_run("All features processed.")
            raise InputInterruptedException("Feature testing complete.")

        if self._current and self._feature_steps >= MAX_STEPS_PER_FEATURE:
            self._drop_current(
                STATUS_PARTIAL if self._current.get("completed_actions") else STATUS_DROPPED,
                "Hit the per-feature step limit.",
            )

        event = self._maybe_start_app(state)
        if event is not None:
            return event

        if self._await_dialog:
            self._await_dialog = False
            refreshed = self._refresh_if_permission(state)
            if refreshed is not None:
                state = refreshed
                self.current_state = state
        elif is_permission_screen(state):
            refreshed = self._refresh_if_permission(state)
            if refreshed is not None:
                state = refreshed
                self.current_state = state

        allow_event = make_allow_event(state)
        if allow_event is not None:
            self.logger.info("Granting runtime permission.")
            return self._emit(allow_event, "Allow the system permission dialog.", matched="Dismiss permission or login prompts that block the home screen")

        if is_permission_screen(state):
            self.logger.info("Permission dialog visible but Allow was not dumpable; granting via adb.")
            self._grant_permissions()
            time.sleep(1.0)
            state = self.device.get_current_state() or state
            self.current_state = state
            allow_event = make_allow_event(state)
            if allow_event is not None:
                return self._emit(
                    allow_event,
                    "Allow the system permission dialog.",
                    matched="Dismiss permission or login prompts that block the home screen",
                )

        outside = self._outside_kind(state)
        if outside == "unrelated":
            activity = state.foreground_activity or ""
            if self._is_launcher(activity):
                return self._start_app_event("Launcher is in front; starting the app.")
            self._outside_steps += 1
            self.logger.info("Left the app (%s). Returning." % activity)
            if self._outside_steps <= 4:
                return KeyEvent(name="BACK")
            if self._outside_steps <= 7:
                return KeyEvent(name="HOME")
            return IntentEvent(intent=self.app.get_start_intent())
        if outside is None:
            self._outside_steps = 0
            self._sent_home = False

        possible = list(state.get_possible_input())
        if self._in_web_browser(state, possible) and not self._back_would_leave_app(state):
            self.logger.info("In a web browser; going back to the app.")
            return KeyEvent(name="BACK")
        if self._current is None:
            nxt = self._next_work_feature()
            started = self._start_or_restart_next(nxt) if nxt is not None else None
            if started is not None:
                return started
        self._note_screen_kind(state, possible)
        if self._pending_fill:
            verified = self._verify_pending_fill(state, possible)
            if verified is not None:
                return verified
        discovered = self._maybe_hybrid_discovery(possible, state)
        if discovered is not None:
            return discovered
        if self._current is None:
            nxt = self._next_work_feature()
            if nxt is not None:
                started = self._start_or_restart_next(nxt)
                if started is not None:
                    return started
            elif self._hybrid_still_pending():
                self._commit_discovery("no-candidate")
                nxt = self._next_work_feature()
                if nxt is not None:
                    started = self._start_or_restart_next(nxt)
                    if started is not None:
                        return started
            if self._current is None:
                self._finish_run("All features processed.")
                raise InputInterruptedException("Feature testing complete.")
        self._maybe_complete_arrival_steps(state, possible)
        if self._skip_satisfied_feature(state, possible):
            return self._continue_next_feature(possible, state)
        if self._is_setup_feature() and self._seen_hub:
            self._drop_current(STATUS_COVERED, "Reached the main screen.")
            return self._continue_next_feature(possible, state)
        stall = self._maybe_feature_cluster_stall(possible, state)
        if stall is not None:
            return stall
        filled = self._mandatory_fill(possible, state)
        if filled is not None:
            return filled
        if self._should_leave_file_picker(state, outside):
            self.logger.info("Leaving the file picker to test the current feature.")
            return KeyEvent(name="BACK")
        if self._should_dismiss_first_run(state, possible):
            dismiss = self._dismiss_first_run(possible)
            if dismiss is not None and self._tap_count(state, dismiss) < 4:
                dismiss.skip_oracle = True
                return self._emit(dismiss, "Finish first-run / tutorial.", matched="")
        if self._last_action_key and self._seen_hub and self._is_onboarding_screen(state, possible):
            self._banned_actions.add(self._last_action_key)
            self.logger.info("Banned the action that returned to first-run setup.")
        if not self._back_would_leave_app(state) and not self._looks_like_hub(possible, state):
            possible.append(KeyEvent(name="BACK"))

        if self._current and not (self._current.get("remaining_actions") or []):
            status = STATUS_COVERED if self._current.get("completed_actions") else STATUS_PARTIAL
            self._drop_current(status, "Listed steps are done.")
            return self._continue_next_feature(possible, state)

        shared = self._maybe_reuse_shared_flow(possible, state)
        if shared is not None:
            return shared

        if self._in_state_cycle():
            recovered = self._try_loop_recovery(possible, state)
            if recovered is not None:
                return recovered
            self.logger.info("Detected a repeating screen cycle; leaving this feature.")
            status = STATUS_PARTIAL if self._current.get("completed_actions") else STATUS_DROPPED
            self._drop_current(status, "Stuck in a repeating screen loop.")
            return self._continue_next_feature(possible, state)

        stagnant = self._maybe_stagnation(possible, state)
        if stagnant is not None:
            return stagnant

        possible = self._prepare_events(possible, state)
        if not possible:
            raw = list(state.get_possible_input()) if state else []
            if self._is_onboarding_screen(state, raw):
                dismiss = self._dismiss_first_run(raw)
                if dismiss is not None:
                    dismiss.skip_oracle = True
                    return self._emit(
                        dismiss,
                        "Leave first-run after returning to onboarding.",
                        matched="",
                    )
                possible = raw
            elif not self._looks_like_hub(raw, state) and not self._back_would_leave_app(state):
                return self._emit(KeyEvent(name="BACK"), "No remaining actions; going back.", matched="")
            else:
                return self._start_app_event("No unused in-app actions; bringing the app to the front.")
        waited = self._maybe_wait_loading(state, possible)
        if waited:
            fresh = self.device.get_current_state()
            if fresh is not None:
                state = fresh
                self.current_state = state
                possible = self._prepare_events(list(state.get_possible_input()), state)
        recover = self._recover_dead_end(possible, state)
        if recover is not None:
            event, reason = recover
            event.skip_oracle = True
            return self._emit(event, reason, matched="")

        if self._looks_like_hub(possible, state) and self._is_sparse_screen(state, possible):
            state_key = getattr(state, "state_str", "") or ""
            if state_key not in self._waited_states:
                self._waited_states.add(state_key)
                time.sleep(1.6)
                fresh = self.device.get_current_state()
                if fresh is not None:
                    state = fresh
                    self.current_state = state
                    possible = self._prepare_events(list(state.get_possible_input()), state)

        if outside == "file_picker":
            self._outside_steps += 1
            if self._outside_steps > MAX_FILE_PICKER_STEPS:
                self.logger.info("File picker took too long; going back.")
                return KeyEvent(name="BACK")

        close_event = self._try_dismiss_interstitial(state, possible)
        if close_event is not None:
            close_event.skip_oracle = True
            self._interstitial_dismisses += 1
            return self._emit(
                close_event,
                "Dismiss contribute/plugin interstitial to reach the app.",
                matched="",
            )

        if self._feature_wants_onboarding_cta():
            cta = self._onboarding_cta(possible)
            if cta is not None and self._tap_count(state, cta) < 2:
                cta.skip_oracle = True
                return self._emit(cta, "Continue onboarding.", matched="Tap Get Started or Continue if shown")
        elif self._feature_wants_guest_skip() and not self._seen_hub:
            skip = self._guest_skip_cta(possible)
            if skip is not None and self._tap_count(state, skip) < 2:
                skip.skip_oracle = True
                return self._emit(
                    skip,
                    "Continue as guest.",
                    matched=(self._current.get("remaining_actions") or [""])[0],
                )
            cta = self._onboarding_cta(possible)
            if cta is not None and self._tap_count(state, cta) < 2:
                cta.skip_oracle = True
                return self._emit(cta, "Advance onboarding toward guest login.", matched="")

        stuck = self._no_progress >= 4
        remaining = list((self._current or {}).get("remaining_actions") or [])
        if (
            self.cfg.enabled("afford_search")
            and remaining
            and needs_affordance_search(remaining)
            and (stuck or self._no_progress >= 2)
        ):
            afford = self._try_affordance_search(possible)
            if afford is not None:
                return afford
        decision = self.advisor.decide(
            feature=self._current,
            state=state,
            events=possible,
            outside_kind=outside,
            stuck=stuck,
            no_progress=self._no_progress,
            screenshot_path=getattr(state, "screenshot_path", None),
        )
        return self._apply_decision(decision, possible, state)

    def _ensure_ready(self):
        if self._ready:
            return
        reset_stats()
        bot = None
        try:
            from droidbot.droidbot import DroidBot
            bot = DroidBot.get_instance()
        except Exception:
            bot = None
        output_dir = getattr(bot, "output_dir", None) or getattr(self.device, "output_dir", None)
        readme_path = getattr(bot, "readme_path", None)
        features_path = getattr(bot, "features_path", None)
        app_name = self.app.app_name if self.app else None
        payload = _load_feature_payload(
            output_dir=output_dir,
            readme_path=readme_path,
            features_path=features_path,
            app_name=app_name,
            apk_path=getattr(bot, "app_path", None) or getattr(self.app, "app_path", None),
            guide_path=getattr(bot, "guide_features_path", None) or self.cfg.guide_features_path,
        )
        self.journal = FeatureJournal(output_dir, app_name=payload.get("app") or app_name)
        self.journal.load_or_create(payload)
        self.journal.session["features_path"] = payload.get("live_features_path") or features_path or (
            os.path.join(output_dir, "features_from_readme.json") if output_dir else None
        )
        self.journal.session["feature_source"] = payload.get("feature_source")
        self.journal.session["guide_vs_readme"] = payload.get("guide_vs_readme")
        self.journal.session["guide_features_path"] = payload.get("guide_features_path")
        self.journal.session["apk_path"] = (
            getattr(bot, "app_path", None) or getattr(self.app, "app_path", None)
        )
        self.journal.save()
        self.advisor = FeatureAdvisor(app_name=payload.get("app") or app_name)
        self.advisor.journal = self.journal
        self._ready = True
        self.logger.info(
            "Feature-guided testing with %d features. Journal: %s"
            % (len(self.journal.features()), self.journal.root)
        )

    def _begin_feature(self, feature):
        self._current = feature
        self._feature_steps = 0
        self._no_progress = 0
        self._recent_states = []
        self._last_state_str = None
        self._feature_sigs = []
        self._backtrack_count = 0
        self._afford_tried = set()
        self._tried_widgets = set()
        self._stagnation_escalated = False
        self._novelty_window = []
        self._remaining_window = []
        self._stagnation_last = None
        self._empty_search_attempted = False
        self._feature_seen_states = set()
        self._states_before_feature = set(self._seen_run_states)
        self._feature_reset_tried = False
        self._pending_fill = None
        self._unresolved_fields = set()
        self._recent_coords = []
        feature["attempts"] = int(feature.get("attempts") or 0) + 1
        self.journal.start_feature(feature)
        self.logger.info("Testing feature %s: %s" % (feature["id"], feature["name"]))

    def _apply_decision(self, decision, possible, state):
        kind = (decision.decision or "act").replace("-", "_")
        if kind in ("feature_complete", "complete"):
            if self._should_ignore_complete(state, possible):
                self.logger.info("Ignoring early feature_complete; first-run/home is not done.")
                fallback = self._dismiss_first_run(possible) or self._fallback_in_app_event(possible, state)
                if fallback is not None:
                    fallback.skip_oracle = True
                    return self._emit(fallback, "First-run is not finished; continuing setup.", matched="")
            status = STATUS_COVERED
            if self._current.get("remaining_actions"):
                status = STATUS_PARTIAL
            self._drop_current(status, decision.reason or "Feature completed.")
            return self._continue_next_feature(possible, state)
        if kind in ("feature_not_present", "not_present"):
            if self._screen_is_dead_end(state, possible):
                recover = self._recover_dead_end(possible, state)
                if recover is not None:
                    event, reason = recover
                    event.skip_oracle = True
                    return self._emit(event, reason, matched="")
            if (
                self._feature_steps < MIN_STEPS_BEFORE_ABSENT
                or self._screen_is_dead_end(state, possible)
                or self._looks_like_hub(possible, state)
            ):
                nav = self.advisor.navigate(self._current, possible) if self.advisor else None
                if nav is not None:
                    return self._apply_decision(nav, possible, state)
                self.logger.info("Ignoring early not_present; still trying to reach the feature.")
                fallback = self._fallback_in_app_event(possible, state)
                if fallback is not None:
                    fallback.skip_oracle = True
                    return self._emit(
                        fallback,
                        "Current screen is not the feature yet; navigating inside the app.",
                        matched="",
                    )
            if self._looks_like_hub(possible, state) or self._screen_is_dead_end(state, possible):
                status = STATUS_PARTIAL if self._current.get("completed_actions") else STATUS_DROPPED
                self._drop_current(status, "Could not reach the feature from this screen.")
                return self._continue_next_feature(possible, state)
            self._drop_current(STATUS_NOT_PRESENT, decision.reason or "Feature is not in the app.")
            return self._continue_next_feature(possible, state)
        if kind in ("drop_feature", "drop"):
            afford = self._try_affordance_search(possible)
            if afford is not None:
                return afford
            status = STATUS_PARTIAL if self._current.get("completed_actions") else STATUS_DROPPED
            self._drop_current(status, decision.reason or "Dropped; action would leave the feature.")
            return self._continue_next_feature(possible, state)
        if kind == "restart_app":
            return self._restart_app(decision.reason or "Advisor requested restart.")

        remaining = list((self._current or {}).get("remaining_actions") or [])
        typing = bool(remaining) and _is_typing_step(remaining[0])
        event = None
        if typing:
            for alt in possible:
                if not _can_set_text(alt):
                    continue
                text = decision.text
                if not text and self.advisor:
                    text = self.advisor.fill_text(
                        getattr(alt, "view", None), remaining,
                        feature=self._current, allow_unresolved=False,
                    )
                if text is None:
                    continue
                event = alt
                decision.text = text
                decision.matched_step = ""
                decision.reason = "Type into the visible field for the remaining step."
                self._arm_pending_fill(alt, remaining, state, text)
                break
        else:
            decision.text = ""
        if event is None and getattr(decision, "tap_x", None) and getattr(decision, "tap_y", None):
            from droidbot.custom_input_event import CustomTouchEvent
            x, y = int(decision.tap_x), int(decision.tap_y)
            if self._coord_repeat_blocked(x, y):
                self.logger.info("Ignoring repeated screenshot tap (%s, %s)." % (x, y))
            else:
                event = CustomTouchEvent(x=x, y=y)
                if remaining and _is_typing_step(remaining[0]):
                    decision.matched_step = ""
                self.logger.info(
                    "Applying screenshot tap (%s, %s) source=%s"
                    % (decision.tap_x, decision.tap_y, decision.source)
                )
        if event is None:
            index = decision.action_index if decision.action_index is not None else 0
            if index < 0 or index >= len(possible):
                index = 0
            event = possible[index]
            if remaining and _is_typing_step(remaining[0]) and not _can_set_text(event):
                for alt in possible:
                    if not _can_set_text(alt):
                        continue
                    text = decision.text
                    if not text and self.advisor:
                        text = self.advisor.fill_text(
                            getattr(alt, "view", None), remaining,
                            feature=self._current, allow_unresolved=False,
                        )
                    if text is None:
                        continue
                    event = alt
                    decision.text = text
                    decision.matched_step = ""
                    decision.reason = "Type into the visible field for the remaining step."
                    self._arm_pending_fill(alt, remaining, state, text)
                    break
        grounded_tap = bool(getattr(decision, "tap_x", None) and getattr(decision, "tap_y", None))
        if not grounded_tap:
            if self._seen_hub and not self._is_setup_feature() and not self._feature_wants_guest_skip():
                if self._is_stale_onboarding_cta(event) and not self._is_onboarding_screen(state, possible):
                    event = self._fallback_in_app_event(possible, state) or event
                    decision.matched_step = ""
            if self._is_dead_end_copy(event):
                recover = self._recover_dead_end(possible, state)
                if recover is not None:
                    event, decision.reason = recover
                    decision.matched_step = ""
                    decision.text = ""
            if self._is_back(event) and self._back_would_leave_app(state):
                event = self._fallback_in_app_event(possible, state)
            if self._looks_like_external_link(event):
                event = self._fallback_in_app_event(possible, state) or event
            if self._is_unhelpful_scroll(event, remaining):
                alt = self._replace_scroll(possible, state)
                if alt is not None:
                    event = alt
                    decision.matched_step = ""
                    decision.reason = "Ignored unhelpful scroll; using an in-app control instead."
        if typing and decision.text and _can_set_text(event):
            event.text = decision.text
            self.logger.info("set_text value=%r source=%s" % (decision.text, decision.source))
            if self.journal:
                self.journal._append_log("set_text value=%r" % decision.text)
        blocked = self._swap_non_idempotent(event, possible, state)
        if blocked is not None:
            event = blocked
        event.skip_oracle = True
        self._switch_depth = 0
        return self._emit(
            event,
            decision.reason,
            matched=decision.matched_step,
            source=decision.source,
            text=decision.text,
        )

    def _emit(self, event, reason, matched="", source="rule", text=""):
        self._feature_steps += 1
        activity = ""
        if self.current_state:
            activity = self.current_state.foreground_activity
            self._last_action_key = self._action_key(self.current_state, event)
            self._tap_counts[self._last_action_key] = self._tap_counts.get(self._last_action_key, 0) + 1
            tried = self._tried_on_state.setdefault(getattr(self.current_state, "state_str", "") or "", set())
            tried.add(self._last_action_key)
            widget_key = self._widget_try_key(event)
            if widget_key:
                self._tried_widgets.add(widget_key)
        if self._current:
            step = {
                "decision": "act",
                "event": _safe_event_str(event, self.current_state),
                "reason": reason,
                "matched_step": matched,
                "source": source,
                "activity": activity,
                "event_type": getattr(event, "event_type", "") or event.__class__.__name__,
                "text": text,
                "screenshot": getattr(self.current_state, "screenshot_path", None),
                "state": getattr(self.current_state, "state_str", None),
            }
            try:
                append_step_payload(step, event, value=text)
                if step.get("signature"):
                    self._feature_sigs.append(step["signature"])
            except Exception:
                sig = widget_signature(event)
                if sig:
                    self._feature_sigs.append(sig)
            key = non_idempotent_key(event)
            if key:
                self.chain_memory.executed_non_idempotent.add(key)
            self.journal.record_step(self._current, step)
            bank = getattr(self, "step_bank", None)
            if bank is not None:
                bank.record(step, self._current.get("id"))
                self.journal.session["exploration_bank"] = bank.to_list()
            self._credit_cross_feature()
        self.logger.info(
            "[%s] %s | %s"
            % (
                (self._current or {}).get("id") or "-",
                _event_label(event) or event.__class__.__name__,
                reason,
            )
        )
        return event

    def _drop_current(self, status, reason):
        if not self._current:
            return
        extra = {}
        if self._current.get("completion_source"):
            extra["completion_source"] = self._current.get("completion_source")
        if self._current.get("reference_chain"):
            extra["reference_chain"] = self._current.get("reference_chain")
        if self._current.get("stagnation_detected"):
            extra["stagnation_detected"] = True
        if self._current.get("blocked_no_progress"):
            extra["blocked_no_progress"] = True
        if self._current.get("retry_attempted") and status in (STATUS_COVERED, STATUS_PARTIAL):
            extra["completed_on_retry"] = True
            self._current["completed_on_retry"] = True
        if self._current.get("retry_attempted") and status in (STATUS_DROPPED, STATUS_BLOCKED):
            extra["blocked_still"] = True
            self._current["blocked_still"] = True
        self._current["status"] = status
        if self.cfg.enabled("shared_flow") and self._feature_sigs:
            entry = self.chain_memory.register(
                self._current,
                self._feature_sigs,
                terminal_state=self._last_state_str or "",
                status=status,
            )
            if entry:
                line = "chain %s finalized as %s" % (entry.get("id"), entry.get("status"))
                self.logger.info(line)
                if self.journal:
                    self.journal._append_log(line)
        self.journal.finish_feature(self._current, status, reason, **extra)
        self.logger.info("Feature %s -> %s (%s)" % (self._current.get("id"), status, reason))
        self._features_finished = getattr(self, "_features_finished", 0) + 1
        self._credit_cross_feature()
        self._current = None
        self._feature_steps = 0
        self._no_progress = 0

    def _note_progress(self, state):
        state_str = state.state_str if state else None
        if state_str and state_str == self._last_state_str:
            self._no_progress += 1
        else:
            self._no_progress = 0
        self._last_state_str = state_str
        if state_str:
            self._feature_seen_states.add(state_str)
            self._seen_run_states.add(state_str)
        if self._current and self._no_progress >= MAX_NO_PROGRESS:
            if not self._current.get("remaining_actions"):
                self._drop_current(STATUS_COVERED, "No remaining steps; screen stopped changing.")
            else:
                self._mark_blocked_or_drop("Stuck on the same screen.")

    def _maybe_start_app(self, state):
        depth = state.get_app_activity_depth(self.app)
        if depth == 0:
            self._restarts = 0
            self._sent_home = False
            self._outside_steps = 0
            return None
        if depth > 0:
            return None
        return self._start_app_event("App is not in the foreground; starting it.")

    def _start_app_event(self, reason):
        if self._last_event_trace.endswith(EVENT_FLAG_START_APP) and not self._feature_switch_restart:
            self._restarts += 1
        self._last_event_trace += EVENT_FLAG_START_APP
        if self._restarts > MAX_RESTARTS:
            if self._current:
                self._drop_current(STATUS_DROPPED, "Could not keep the app in the foreground.")
            nxt = self.journal.next_pending() if self.journal else None
            if nxt is None:
                self._finish_run("App would not stay running.")
                raise InputInterruptedException("The app cannot be started.")
            self._restarts = 0
            self._begin_feature(nxt)
        self.logger.info(reason)
        if self._current:
            self.journal._append_log(
                "App was not in the foreground; restarting to resume %s."
                % self._current.get("id")
            )
        self._await_dialog = True
        self._outside_steps = 0
        self._last_action_key = None
        return IntentEvent(intent=self.app.get_start_intent())

    def _restart_app(self, reason):
        self.logger.info("Restarting app: %s" % reason)
        self._outside_steps = 0
        if self._current:
            self.journal._append_log("Restart: %s" % reason)
        depth = -1
        state = self.current_state
        if state is not None:
            try:
                depth = state.get_app_activity_depth(self.app)
            except Exception:
                depth = -1
        if depth == 0:
            self._last_event_trace += EVENT_FLAG_STOP_APP
            return IntentEvent(intent=self.app.get_stop_intent())
        return self._start_app_event(reason)

    def _idle_or_home(self):
        nxt = self._next_work_feature()
        if nxt is None:
            if self._hybrid_still_pending():
                self._await_dialog = False
                return IntentEvent(intent=self.app.get_start_intent())
            self._finish_run("All features processed.")
            raise InputInterruptedException("Feature testing complete.")
        started = self._start_or_restart_next(nxt)
        if started is not None:
            return started
        self._await_dialog = False
        return IntentEvent(intent=self.app.get_start_intent())

    def _start_or_restart_next(self, nxt):
        if nxt is None:
            return None
        if getattr(self, "_features_finished", 0) > 0:
            self._pending_next_feature = nxt
            self._restart_between_features = True
            self._feature_switch_restart = True
            self._restart_phase = "stop"
            self.logger.info("Restart before testing %s." % nxt.get("id"))
            if self.journal:
                self.journal._append_log("Restart before testing %s." % nxt.get("id"))
            self._last_event_trace = getattr(self, "_last_event_trace", "") + EVENT_FLAG_STOP_APP
            return IntentEvent(intent=self.app.get_stop_intent())
        self._begin_feature(nxt)
        return None

    def _advance_feature_restart(self, state):
        phase = getattr(self, "_restart_phase", None) or "stop"
        if phase == "stop":
            self._restart_phase = "start"
            return self._start_app_event("Restart before next feature.")
        depth = -1
        try:
            depth = state.get_app_activity_depth(self.app) if state is not None else -1
        except Exception:
            depth = -1
        if depth == 0:
            nxt = self._pending_next_feature
            self._pending_next_feature = None
            self._restart_between_features = False
            self._feature_switch_restart = False
            self._restart_phase = None
            self._restarts = 0
            if nxt is not None and self._current is None:
                self._begin_feature(nxt)
            return None
        return self._start_app_event("Restart before next feature.")

    def _credit_cross_feature(self):
        bank = getattr(self, "step_bank", None)
        if not self.journal or bank is None:
            return
        upgraded = self.journal.credit_from_bank(bank)
        for feat in upgraded:
            self.logger.info(
                "Feature %s upgraded to %s from later exploration (%s)."
                % (
                    feat.get("id"),
                    feat.get("status"),
                    ", ".join(feat.get("credited_from") or []) or "other features",
                )
            )

    def _continue_next_feature(self, possible, state):
        nxt = self._next_work_feature()
        if nxt is None:
            discovered = self._maybe_hybrid_discovery(possible, state)
            if discovered is not None:
                return discovered
            self._finish_run("All features processed.")
            raise InputInterruptedException("Feature testing complete.")
        depth = getattr(self, "_switch_depth", 0) + 1
        self._switch_depth = depth
        started = self._start_or_restart_next(nxt)
        if started is not None:
            return started
        if self._skip_satisfied_feature(state, possible):
            return self._continue_next_feature(possible, state)
        self._maybe_complete_arrival_steps(state, possible)
        possible = self._prepare_events(list(possible or []), state)
        outside = self._outside_kind(state)
        if self._should_leave_file_picker(state, outside):
            return KeyEvent(name="BACK")
        if self._should_dismiss_first_run(state, possible):
            dismiss = self._dismiss_first_run(possible)
            if dismiss is not None:
                dismiss.skip_oracle = True
                return self._emit(dismiss, "Finish first-run / tutorial.", matched="")
        if depth > 4:
            self._switch_depth = 0
            fallback = self._fallback_in_app_event(possible, state)
            if fallback is not None:
                fallback.skip_oracle = True
                return self._emit(
                    fallback,
                    "Moving to the next feature on the current screen.",
                    matched="",
                )
            self._await_dialog = True
            return IntentEvent(intent=self.app.get_start_intent())
        close_event = self._try_dismiss_interstitial(state, possible)
        if close_event is not None:
            close_event.skip_oracle = True
            self._interstitial_dismisses += 1
            return self._emit(
                close_event,
                "Dismiss contribute/plugin interstitial to reach the app.",
                matched="",
            )
        recover = self._recover_dead_end(possible, state)
        if recover is not None:
            event, reason = recover
            event.skip_oracle = True
            return self._emit(event, reason, matched="")
        decision = self.advisor.decide(
            feature=self._current,
            state=state,
            events=possible,
            outside_kind=self._outside_kind(state),
            stuck=False,
            no_progress=0,
            screenshot_path=getattr(state, "screenshot_path", None),
        )
        return self._apply_decision(decision, possible, state)

    def _feature_blob(self):
        feat = self._current or {}
        parts = [feat.get("name"), feat.get("description")]
        parts.extend(feat.get("remaining_actions") or feat.get("actions") or [])
        parts.extend(feat.get("keywords") or [])
        parts.extend(feat.get("nav_hints") or [])
        return " ".join(str(part) for part in parts if part).lower()

    def _feature_wants_plugins(self):
        blob = self._feature_blob()
        return "plugin" in blob or "metadata provider" in blob

    def _feature_wants_guest_skip(self):
        remaining = " ".join(self._current.get("remaining_actions") or []).lower()
        if not remaining:
            return False
        return any(word in remaining for word in ("guest", "skip"))

    def _feature_wants_onboarding_cta(self):
        remaining = " ".join(self._current.get("remaining_actions") or []).lower()
        if not remaining:
            return False
        if self._feature_wants_guest_skip():
            return False
        return any(word in remaining for word in ("get started", "onboard", "next", "continue"))

    def _is_setup_feature(self, feature=None):
        feat = feature or self._current or {}
        blob = "%s %s" % (feat.get("name") or "", feat.get("description") or "")
        blob = blob.lower()
        return any(token in blob for token in (
            "first-run", "first run", "onboard", "setup", "create database", "open database",
            "get started", "guest login", "continue as guest", "skip this", "permission",
            "welcome", "intro",
        ))

    def _is_home_only_feature(self, feature=None):
        feat = feature or self._current or {}
        if self._is_setup_feature(feat):
            return False
        blob = "%s %s" % (feat.get("name") or "", " ".join(feat.get("actions") or []))
        blob = blob.lower()
        return "home screen" in blob or "home icon" in blob

    def _feature_wants_file_picker(self, feature=None):
        feat = feature or self._current or {}
        blob = self._feature_blob() if feat is self._current else (
            "%s %s %s" % (
                feat.get("name") or "",
                feat.get("description") or "",
                " ".join(feat.get("remaining_actions") or feat.get("actions") or []),
            )
        ).lower()
        return any(token in blob for token in (
            "import", "export", "file", "database", "csv", "qif", "mmb", "save as",
        ))

    def _should_dismiss_first_run(self, state, events):
        # After the hub, Get Started/Next re-enters onboarding. Skip still leaves it.
        if self._seen_hub and not self._is_setup_feature() and not self._feature_wants_guest_skip():
            return self._is_onboarding_screen(state, events)
        if not self._is_onboarding_screen(state, events):
            activity = (getattr(state, "foreground_activity", "") or "").lower() if state else ""
            if "passwordactivity" in activity and (self._is_setup_feature() or not self._seen_hub):
                return True
            return False
        if self._create_db_taps >= 2 and not self._is_setup_feature():
            return False
        return True

    def _should_leave_file_picker(self, state, outside):
        if outside != "file_picker":
            return False
        if self._is_setup_feature() or self._feature_wants_file_picker():
            return self._outside_steps > MAX_FILE_PICKER_STEPS
        return True

    def _skip_satisfied_feature(self, state, events):
        if not self._current:
            return False
        if self._seen_hub and self._is_home_only_feature():
            self._drop_current(STATUS_COVERED, "Already on the home screen.")
            return True
        if self._onboarding_already_done(state, events):
            self._drop_current(STATUS_COVERED, "Onboarding already finished; main screen is visible.")
            return True
        return False

    def _onboarding_already_done(self, state, events):
        if not (self._is_setup_feature() or self._feature_wants_guest_skip()):
            return False
        if self._is_onboarding_screen(state, events):
            return False
        return bool(self._seen_hub or self._looks_like_hub(events, state))

    def _guest_skip_cta(self, events):
        for phrase in ("continue as guest", "skip this nonsense", "skip"):
            for event in events:
                label = normalize_label(_event_label(event))
                if _label_has_phrase(label, phrase) and not self._looks_like_external_link(event):
                    return event
        return None

    def _screen_blob(self, state, events):
        parts = [_event_label(event) for event in events or []]
        try:
            ui_text, _activity, _indexed = state.get_text_representation()
            parts.append(ui_text or "")
        except Exception:
            pass
        if state is not None:
            parts.append(getattr(state, "search_content", "") or "")
        return normalize_label(" ".join(str(part) for part in parts if part))

    def _try_dismiss_interstitial(self, state, possible):
        if self._feature_wants_plugins():
            return None
        if self._interstitial_dismisses >= 2:
            return None
        close_event = self._dismiss_interstitial(state, possible)
        if close_event is None:
            return None
        if self._tap_count(state, close_event) >= 2:
            return None
        return close_event

    def _dismiss_interstitial(self, state, events):
        blob = self._screen_blob(state, events)
        markers = any(marker in blob for marker in INTERSTITIAL_MARKERS)
        promo_hits = sum(1 for token in PROMO_TOKENS if token in blob)
        # After the hub, donate/github strings often linger in the tree and
        # unlabeled top-left taps bounce home <-> contribute forever.
        if self._seen_hub and not markers:
            return None
        if not markers and promo_hits < 2:
            return None
        for phrase in CLOSE_CTA:
            for event in events:
                label = normalize_label(_event_label(event))
                if _label_has_phrase(label, phrase) and not self._looks_like_external_link(event):
                    return event
        if self._seen_hub:
            return None
        for event in events:
            if self._is_back(event) or self._looks_like_external_link(event):
                continue
            view = getattr(event, "view", None) or {}
            bounds = view.get("bounds")
            if not bounds:
                continue
            left, top = bounds[0]
            right, bottom = bounds[1]
            width = right - left
            height = bottom - top
            if left <= 160 and top <= 320 and width <= 180 and height <= 180:
                return event
        return None

    def _augment_events(self, events, feature):
        blob = " ".join((feature or {}).get("remaining_actions") or []).lower()
        blob += " " + " ".join((feature or {}).get("keywords") or []).lower()
        if not any(phrase in blob for phrase in ("long-press", "long press", "longpress")):
            return events
        extra = []
        seen = set()
        for event in events:
            view = getattr(event, "view", None)
            if not view:
                continue
            event_type = getattr(event, "event_type", "")
            if event_type in ("set_text", "scroll", "key", "long_touch"):
                continue
            if not _event_label(event).strip():
                continue
            key = view.get("view_str") or id(view)
            if key in seen:
                continue
            seen.add(key)
            extra.append(LongTouchEvent(view=view, duration=1500))
            if len(extra) >= 6:
                break
        return extra + list(events)

    def _outside_kind(self, state):
        if is_permission_screen(state):
            return None
        activity = (state.foreground_activity or "").lower()
        depth = state.get_app_activity_depth(self.app)
        if depth == 0:
            return None
        if any(marker in activity for marker in FILE_PICKER_MARKERS):
            return "file_picker"
        if any(marker in activity for marker in BROWSER_MARKERS):
            return "unrelated"
        if depth > 0:
            # Another activity is above the app (picker, share sheet, etc.)
            if any(marker in activity for marker in FILE_PICKER_MARKERS):
                return "file_picker"
            package = activity.split("/")[0]
            if self.app and package.startswith(self.app.get_package_name()):
                return None
            return "file_picker" if "picker" in activity or "document" in activity else "unrelated"
        return "unrelated"

    def _permission_or_cta(self, state, events):
        allow_event = make_allow_event(state)
        if allow_event is not None:
            return allow_event
        return self._onboarding_cta(events)

    def _onboarding_cta(self, events):
        for phrase in ONBOARDING_CTA:
            for event in events:
                label = normalize_label(_event_label(event))
                if _label_has_phrase(label, phrase) and not self._looks_like_external_link(event):
                    return event
        for phrase in SKIP_CTA:
            for event in events:
                label = normalize_label(_event_label(event))
                if _label_has_phrase(label, phrase):
                    return event
        return None

    def _refresh_if_permission(self, state):
        time.sleep(1.2)
        fresh = self.device.get_current_state()
        return fresh or state

    def _back_would_leave_app(self, state):
        if state is None:
            return False
        if is_permission_screen(state):
            return True
        try:
            return state.get_app_activity_depth(self.app) == 0
        except Exception:
            return False

    def _is_back(self, event):
        return isinstance(event, KeyEvent) and (getattr(event, "name", "") or "").upper() == "BACK"

    def _is_scroll(self, event):
        if event is None:
            return False
        return isinstance(event, ScrollEvent) or (getattr(event, "event_type", "") or "") == "scroll"

    def _step_wants_scroll(self, step):
        low = (step or "").lower()
        return any(word in low for word in ("scroll", "swipe", "browse"))

    def _is_unhelpful_scroll(self, event, remaining):
        if not self._is_scroll(event):
            return False
        if remaining and self._step_wants_scroll(remaining[0]):
            return False
        return True

    def _replace_scroll(self, possible, state):
        blob = self._feature_blob()
        names = []
        if any(word in blob for word in ("search", "query", "find")):
            names.extend(("search",))
        if any(word in blob for word in ("play", "song", "track", "library")):
            names.extend(("songs", "tracks", "library", "home"))
        names.extend(("home", "library", "tracks"))
        tab = self._nav_tab_matching(possible, tuple(names))
        if tab is not None and not self._is_scroll(tab):
            return tab
        return self._fallback_in_app_event(possible, state)

    def _in_web_browser(self, state, events=None):
        activity = (getattr(state, "foreground_activity", "") or "").lower() if state else ""
        if any(marker in activity for marker in BROWSER_MARKERS):
            return True
        blob = self._screen_blob(state, events)
        return any(token in blob for token in (
            "github.com/",
            "http://github.com",
            "https://github.com",
        ))

    def _looks_like_external_link(self, event):
        label = normalize_label(_event_label(event))
        return any(token in label for token in (
            "github",
            "donate",
            "open collective",
            "patreon",
            "play store",
            "chrome",
            "browser",
        ))

    def _fallback_in_app_event(self, possible, state):
        usable = [
            event for event in possible
            if not self._is_back(event)
            and not self._looks_like_external_link(event)
            and not self._is_dead_end_copy(event)
        ]
        blob = self._feature_blob()
        actions = list((self._current or {}).get("remaining_actions") or [])
        typing = bool(actions) and _is_typing_step(actions[0])
        intent = _player_step_intent(self._current, actions)
        if intent:
            for event in usable:
                role = _widget_player_role(event)
                if intent == "open" and role == "card":
                    return event
                if intent == role:
                    return event
            tab = self._nav_tab_matching(usable, ("songs", "tracks", "library", "home"))
            if tab is not None:
                return tab
        wants_search = typing or bool(_tokens(blob) & {
            "search", "find", "query",
        })
        if wants_search:
            field = self._find_search_field(usable)
            if field is not None:
                return field
            tab = self._nav_tab_matching(usable, ("search", "library"))
            if tab is not None:
                return tab
        for event in usable:
            if getattr(event, "nav_label", None):
                return event
            if _event_label(event).strip():
                return event
        for event in possible:
            if not self._is_back(event) and not self._is_dead_end_copy(event):
                return event
        return None

    def _note_screen_kind(self, state, events):
        state_str = getattr(state, "state_str", "") or ""
        if state_str and (not self._recent_states or self._recent_states[-1] != state_str):
            self._recent_states.append(state_str)
            self._recent_states = self._recent_states[-12:]
        if self._is_onboarding_screen(state, events):
            self._onboarding_states.add(state_str)
        if self._looks_like_hub(events, state):
            self._seen_hub = True

    def _maybe_complete_arrival_steps(self, state, events=None):
        if not self._current or not self._seen_hub:
            return
        remaining = list(self._current.get("remaining_actions") or [])
        blob = self._screen_blob(state, events)
        for action in remaining:
            low = action.lower()
            matched = ""
            if any(token in low for token in (
                "reach the", "home screen", "main screen", "main ui", "main app",
            )):
                matched = action
            elif _is_typing_step(action):
                continue
            elif any(token in low for token in ("create", "play button", "adjust", "save", "sync", "edit", "manage installed")):
                continue
            elif "search" in low and any(word in low for word in ("icon", "tab", "bar")) and _has_searchish_field(events):
                matched = action
            elif "settings" in low and "settings" in blob and any(word in low for word in ("icon", "tab", "open")):
                matched = action
            elif "playlist" in low and "playlist" in blob and any(word in low for word in ("select", "open", "tab")):
                matched = action
            elif any(token in low for token in (
                "now playing", "currently playing", "playing card", "mini player", "open the player",
            )):
                activity = (getattr(state, "foreground_activity", "") or "").lower() if state else ""
                if any(token in activity for token in ("nowplaying", "playeractivity", "playingactivity")):
                    matched = action
            if not matched:
                continue
            self.journal.record_step(self._current, {
                "decision": "act",
                "event": "(screen already shows this destination)",
                "reason": "The current screen already matches this navigation step.",
                "matched_step": matched,
                "source": "rule",
                "activity": getattr(state, "foreground_activity", "") if state else "",
                "event_type": "nav",
                "text": "",
                "screenshot": getattr(state, "screenshot_path", None) if state else None,
                "state": getattr(state, "state_str", None) if state else None,
            })
            break

    def _in_state_cycle(self):
        seq = self._recent_states
        if len(seq) >= 6 and seq[-3:] == seq[-6:-3]:
            return True
        if len(seq) >= 4 and seq[-1] == seq[-3] and seq[-2] == seq[-4]:
            return True
        return False

    def _action_key(self, state, event):
        view = getattr(event, "view", None) or {}
        return (
            getattr(state, "state_str", "") or "",
            view.get("view_str") or _event_label(event) or event.__class__.__name__,
        )

    def _widget_try_key(self, event):
        """Feature-scoped widget identity (resource_id/text/type), no state hash."""
        return widget_signature(event) or _event_label(event) or event.__class__.__name__

    def _tap_count(self, state, event):
        return self._tap_counts.get(self._action_key(state, event), 0)

    def _coord_repeat_blocked(self, x, y):
        key = (int(x) // 24, int(y) // 24)
        bucket = getattr(self, "_recent_coords", None)
        if bucket is None:
            self._recent_coords = []
            bucket = self._recent_coords
        bucket.append(key)
        self._recent_coords = bucket[-8:]
        return self._recent_coords.count(key) >= 3

    def _filter_banned(self, events, state):
        kept = []
        for event in events:
            key = self._action_key(state, event)
            if key in self._banned_actions:
                continue
            if self._tap_counts.get(key, 0) >= 2 and not self._is_back(event):
                continue
            kept.append(event)
        if kept:
            return kept
        if not self._looks_like_hub(events, state) and not self._back_would_leave_app(state):
            backs = [event for event in events if self._is_back(event)]
            if backs:
                return backs
            return [KeyEvent(name="BACK")]
        labeled = []
        for event in events:
            if self._is_back(event) or self._looks_like_external_link(event):
                continue
            if not _event_label(event).strip() and not getattr(event, "nav_label", None):
                continue
            key = self._action_key(state, event)
            if key in self._banned_actions:
                continue
            labeled.append(event)
        return labeled

    def _prepare_events(self, events, state):
        possible = self._annotate_bottom_nav(list(events or []), state)
        possible = self._drop_stale_onboarding(possible, state)
        possible = self._drop_dead_end_copy(possible) or possible
        possible = self._filter_banned(possible, state)
        possible = self._augment_events(possible, self._current)
        return possible

    def _is_launcher(self, activity):
        return "launcher" in (activity or "").lower()

    def _is_stale_onboarding_cta(self, event):
        label = normalize_label(_event_label(event))
        return any(_label_has_phrase(label, phrase) for phrase in (
            "skip this nonsense",
            "continue as guest",
            "skip",
            "let's get started",
            "lets get started",
            "get started",
            "install a metadata provider",
            "donate on open collective",
        ))

    def _drop_stale_onboarding(self, events, state=None):
        if not self._seen_hub or self._is_setup_feature() or self._feature_wants_guest_skip():
            return events
        if self._is_onboarding_screen(state, events):
            return events
        kept = []
        for event in events:
            if self._feature_wants_plugins() and "metadata" in _event_label(event).lower():
                kept.append(event)
                continue
            if self._is_stale_onboarding_cta(event):
                continue
            kept.append(event)
        return kept or events

    def _is_dead_end_copy(self, event):
        label = _event_label(event)
        if _looks_like_loading_label(label):
            return True
        if _looks_like_search_placeholder(label) and not _can_set_text(event) and not _is_set_text(event):
            return True
        if not (_looks_like_empty_label(label) or _looks_like_error_label(label)):
            return False
        lower = label.lower()
        if any(word in lower for word in ("retry", "close", "dismiss")) and not _looks_like_empty_label(label):
            return False
        return True

    def _drop_dead_end_copy(self, events):
        return [event for event in events if not self._is_dead_end_copy(event)]

    def _screen_is_dead_end(self, state, events):
        return _dead_end_text(self._screen_blob(state, events))

    def _nav_tab_matching(self, events, names):
        for event in events:
            blob = ("%s %s" % (
                getattr(event, "nav_label", None) or "",
                _event_label(event),
            )).lower()
            if any(name in blob for name in names):
                return event
        return None

    def _find_plus_or_add(self, events):
        for event in events:
            if self._is_dead_end_copy(event):
                continue
            label = _event_label(event).lower()
            if "plus" in label or label.strip() in ("+", "add") or "fab" in label:
                return event
            view = getattr(event, "view", None) or {}
            rid = (_view_text(view.get("resource_id")) or "").lower()
            if any(token in rid for token in ("fab", "plus", "add")):
                return event
        return None

    def _recover_dead_end(self, possible, state):
        blob = self._screen_blob(state, possible)
        if _looks_like_loading_label(blob):
            return None
        if not _dead_end_text(blob):
            return None
        remaining = " ".join((self._current or {}).get("remaining_actions") or []).lower()
        error = any(token in blob for token in ERROR_TOKENS) and not _looks_like_loading_label(blob)
        empty = _looks_like_empty_label(blob)
        intent = _player_step_intent(self._current, (self._current or {}).get("remaining_actions") or [])
        if error:
            for phrase in ("close", "dismiss", "retry", "ok", "got it"):
                for event in possible:
                    if self._is_dead_end_copy(event) or self._looks_like_external_link(event):
                        continue
                    label = normalize_label(_event_label(event))
                    if phrase in label and self._tap_count(state, event) < 2:
                        return event, "Leave error/log screen."
            home = self._nav_tab_matching(possible, ("home",))
            if home is not None and self._tap_count(state, home) < 2:
                return home, "Return to hub from error screen."
            if not self._looks_like_hub(possible, state) and not self._back_would_leave_app(state):
                return KeyEvent(name="BACK"), "Back out of error screen."
            return None
        if empty:
            if intent:
                for event in possible:
                    if self._is_dead_end_copy(event):
                        continue
                    role = _widget_player_role(event)
                    if (intent == "open" and role == "card") or intent == role:
                        if self._tap_count(state, event) < 3:
                            return event, "Use the mini-player for this step."
                tab = self._nav_tab_matching(possible, ("songs", "tracks", "library"))
                if tab is not None and self._tap_count(state, tab) < 2:
                    return tab, "Leave empty list toward the feature."
                if intent in ("pause", "next", "prev", "shuffle", "repeat"):
                    return None
            wants_create = any(word in remaining for word in ("add", "create", "new", "plus"))
            wants_elsewhere = any(word in remaining for word in (
                "import", "export", "filter", "sort", "settings", "search",
                "plugin", "lyrics", "playlist", "account", "play",
                "song", "track", "share", "rate",
            ))
            if wants_create and not wants_elsewhere:
                plus = self._find_plus_or_add(possible)
                if plus is not None and self._tap_count(state, plus) < 2:
                    return plus, "Create from empty list."
            if wants_elsewhere:
                if not self._empty_search_attempted:
                    field = self._find_search_field(possible)
                    if field is not None:
                        self._empty_search_attempted = True
                        return field, "Search from an empty list to reach the feature."
                tab = self._nav_tab_matching(possible, ("search", "library", "playlist"))
                if tab is not None and self._tap_count(state, tab) < 2:
                    return tab, "Leave empty list toward the feature."
            return None
        return None

    def _find_search_field(self, possible):
        ranked = []
        for event in possible:
            if self._is_dead_end_copy(event):
                continue
            if not _can_set_text(event) and not _is_set_text(event):
                continue
            view = getattr(event, "view", None) or {}
            blob = " ".join((
                _view_text(view.get("text")),
                _view_text(view.get("content_description")),
                _view_text(view.get("resource_id")),
                _view_text(view.get("hint")),
            )).lower()
            score = 1
            if any(token in blob for token in ("search", "query", "find")):
                score = 3
            ranked.append((score, event))
        if not ranked:
            return None
        ranked.sort(key=lambda item: item[0], reverse=True)
        return ranked[0][1]

    def _bottom_nav_views(self, events):
        rows = []
        for event in events:
            view = getattr(event, "view", None) or {}
            bounds = view.get("bounds")
            if not bounds:
                continue
            left, top = bounds[0]
            right, bottom = bounds[1]
            rows.append((top, left, right, bottom, event))
        if not rows:
            return []
        screen_h = max(item[3] for item in rows)
        nav = [item for item in rows if item[0] >= screen_h * 0.88]
        nav.sort(key=lambda item: item[1])
        uniq = []
        seen_x = []
        for item in nav:
            if any(abs(item[1] - prior) < 40 for prior in seen_x):
                continue
            seen_x.append(item[1])
            uniq.append(item)
        return uniq

    def _looks_like_hub(self, events, state=None):
        if self._is_onboarding_screen(state, events):
            return False
        activity = ""
        if state is not None:
            activity = (getattr(state, "foreground_activity", "") or "").lower()
        if any(token in activity for token in ("documentsui", "picker", "packageinstaller")):
            return False
        if "mainactivity" in activity and "selectdatabase" not in activity:
            return True
        if len(self._bottom_nav_views(events)) >= 3:
            return True
        blob = " ".join(_event_label(event).lower() for event in events or [])
        hits = sum(
            1 for token in (
                "search", "library", "home", "settings",
                "accounts", "budget", "reports",
                "tracks", "songs", "albums", "artists", "playlists",
                "browse", "explore", "downloads", "radio",
            ) if token in blob
        )
        return hits >= 2

    def _is_onboarding_screen(self, state, events):
        activity = ""
        if state is not None:
            activity = (getattr(state, "foreground_activity", "") or "").lower()
        if any(token in activity for token in (
            "tutorial", "welcome", "onboarding", "intro", "splash",
            "gettingstarted", "getting_started", "selectdatabase",
        )):
            return True
        blob = self._screen_blob(state, events)
        return any(token in blob for token in (
            "skip this nonsense",
            "let's get started",
            "lets get started",
            "create database",
            "open database",
            "continue as guest",
            "swipe left",
            "swipe right",
            "anonymous usage",
            "send anonymous",
            "usage summary",
            "help us sending",
        ))

    def _dismiss_first_run(self, events):
        blob = " ".join(_event_label(event).lower() for event in events or [])
        if "password" in blob:
            for event in events:
                label = normalize_label(_event_label(event))
                if _label_has_phrase(label, "ok") or "btnsubmit" in label:
                    return event
        analytics = any(token in blob for token in (
            "anonymous usage", "send anonymous", "usage summary", "help us sending",
        ))
        if analytics:
            up = self._toolbar_up(events)
            if up is not None:
                return up
            for event in events:
                if self._is_back(event):
                    return event
        for phrase in (
            "create database", "open database", "close", "done", "finish",
            "skip this nonsense", "continue as guest", "skip",
            "get started", "next",
        ):
            if self._seen_hub and phrase in ("get started", "next", "create database", "open database"):
                continue
            for event in events:
                label = normalize_label(_event_label(event))
                if _label_has_phrase(label, phrase) and not self._looks_like_external_link(event):
                    if analytics and phrase in ("skip", "next", "close"):
                        continue
                    if phrase in ("create database", "open database"):
                        if self._create_db_taps >= 2:
                            continue
                        self._create_db_taps += 1
                    return event
        for event in events:
            if isinstance(event, ScrollEvent) and (getattr(event, "direction", "") or "") == "left":
                return event
        return None

    def _toolbar_up(self, events):
        for event in events:
            label = normalize_label(_event_label(event))
            rid = ""
            view = getattr(event, "view", None) or {}
            rid = _view_text(view.get("resource_id")).lower()
            if "navigate up" in label or label.endswith(" up") or rid.endswith("/up"):
                return event
            cls = _view_text(view.get("class"))
            text = _view_text(view.get("text")).strip()
            if "ImageButton" in cls and not text and not _view_text(view.get("content_description")).strip():
                bounds = view.get("bounds") or [[999, 999], [999, 999]]
                left, top = bounds[0]
                if left < 200 and top < 280:
                    return event
        return None

    def _should_ignore_complete(self, state, events):
        remaining = list((self._current or {}).get("remaining_actions") or [])
        needs_home = any(
            any(token in action.lower() for token in ("reach the", "home screen", "main screen", "main ui"))
            for action in remaining
        )
        if needs_home and (not self._seen_hub or self._is_onboarding_screen(state, events)):
            return True
        if self._is_onboarding_screen(state, events):
            return True
        activity = ""
        if state is not None:
            activity = (getattr(state, "foreground_activity", "") or "").lower()
        if any(token in activity for token in ("documentsui", "picker", "tutorial", "selectdatabase")):
            return True
        return False

    def _maybe_wait_loading(self, state, events):
        blob = self._screen_blob(state, events)
        if not _looks_like_loading_label(blob):
            return False
        key = getattr(state, "state_str", "") or ""
        if key in self._waited_loading:
            return False
        self._waited_loading.add(key)
        self.logger.info("Loading/progress screen; waiting before acting.")
        time.sleep(2.0)
        return True

    def _is_sparse_screen(self, state, events):
        labeled = [
            event for event in events
            if _visible_label(event).strip()
            and not self._is_back(event)
            and not _looks_like_empty_label(_event_label(event))
        ]
        return len(labeled) <= 1

    def _annotate_bottom_nav(self, events, state):
        activity = ""
        if state is not None:
            activity = (getattr(state, "foreground_activity", "") or "").lower()
        if any(token in activity for token in ("documentsui", "picker", "packageinstaller")):
            return events
        nav = self._bottom_nav_views(events)
        if len(nav) < 3:
            return events
        for index, item in enumerate(nav):
            event = item[4]
            event.nav_label = "bottom navigation tab %d of %d" % (index + 1, len(nav))
        return events

    def _maybe_reuse_shared_flow(self, possible, state):
        if not self.cfg.enabled("shared_flow") or not self._current:
            return None
        remaining = list(self._current.get("remaining_actions") or [])
        if not remaining or len(self._feature_sigs) < self.cfg.shared_k:
            return None
        decision = decide_shared_flow(
            self.chain_memory,
            self._feature_sigs,
            remaining,
            lambda fid: self.journal.get_feature(fid) if self.journal else None,
            k=self.cfg.shared_k,
            threshold=self.cfg.shared_threshold,
        )
        if not decision:
            return None
        if decision["action"] != "reuse":
            STATS.record_mechanism("shared_flow", "diverge after %s" % decision.get("match_length"))
            return None
        skipped = decision.get("skipped") or 0
        completed = self._current.setdefault("completed_actions", [])
        for action in remaining:
            if action not in completed:
                completed.append(action)
        self._current["remaining_actions"] = []
        self._current["completion_source"] = "shared_flow_reuse"
        self._current["reference_chain"] = (decision.get("chain") or {}).get("id")
        self.chain_memory.note_reuse(self._current.get("id"), decision.get("chain"), skipped)
        STATS.record_mechanism("shared_flow", "reuse %s skip %d" % (
            (decision.get("chain") or {}).get("id"), skipped,
        ))
        self._drop_current(
            STATUS_COVERED,
            "Covered by shared-flow reuse of %s." % (decision.get("chain") or {}).get("id"),
        )
        return self._continue_next_feature(possible, state)

    def _try_loop_recovery(self, possible, state):
        if not self.cfg.enabled("backtrack"):
            return None
        if self._backtrack_count >= self.cfg.max_backtracks:
            line = "Backtrack cap hit (%d) for %s; not re-selecting tried widgets." % (
                self.cfg.max_backtracks,
                (self._current or {}).get("id") or "-",
            )
            self.logger.info(line)
            if self.journal:
                self.journal._append_log(line)
            return None
        event = self._pick_backtrack_event(possible, state)
        if event is None:
            return None
        self._backtrack_count += 1
        STATS.record_mechanism("backtrack", "loop attempt %d" % self._backtrack_count)
        event.skip_oracle = True
        return self._emit(
            event,
            "Loop detected; trying an untried widget (backtrack %d/%d)."
            % (self._backtrack_count, self.cfg.max_backtracks),
            matched="",
        )

    def _pick_backtrack_event(self, possible, state):
        tried = self._tried_widgets
        remaining = list((self._current or {}).get("remaining_actions") or [])
        event, why = pick_untried_plausible(
            possible,
            remaining,
            feature_keywords(self._current),
            tried,
            self._widget_try_key,
            floor=2.0,
        )
        if event is not None:
            self.logger.info(
                "Backtrack found a new widget (%s); tried-set size=%d"
                % (_event_label(event) or event.__class__.__name__, len(tried))
            )
            return event
        if why:
            return None
        if not self._looks_like_hub(possible, state) and not self._back_would_leave_app(state):
            return KeyEvent(name="BACK")
        return None

    def _try_affordance_search(self, possible):
        if not self.cfg.enabled("afford_search") or not self._current:
            return None
        remaining = list(self._current.get("remaining_actions") or [])
        if not needs_affordance_search(remaining):
            return None
        event, tier = find_affordance_event(possible, self._afford_tried)
        if event is None or not tier:
            return None
        self._afford_tried.add(tier)
        STATS.record_mechanism("afford_search", tier)
        event.skip_oracle = True
        return self._emit(
            event,
            "Affordance search before drop (%s)." % tier,
            matched="",
            source="afford_search",
        )

    def _swap_non_idempotent(self, event, possible, state):
        if not self.cfg.enabled("non_idempotent") or event is None:
            return None
        key = non_idempotent_key(event)
        if not key or key not in self.chain_memory.executed_non_idempotent:
            return None
        STATS.record_mechanism("non_idempotent", "blocked %s" % key)
        for alt in possible or []:
            if alt is event:
                continue
            alt_key = non_idempotent_key(alt)
            if alt_key and alt_key in self.chain_memory.executed_non_idempotent:
                continue
            if self._is_back(alt):
                continue
            return alt
        return None

    def _maybe_stagnation(self, possible, state):
        if not self.cfg.enabled("stagnation") or not self._current:
            return None
        state_str = getattr(state, "state_str", "") or ""
        is_new = bool(state_str) and state_str != getattr(self, "_stagnation_last", None)
        self._stagnation_last = state_str or self._stagnation_last
        self._novelty_window.append(1 if is_new else 0)
        self._remaining_window.append(len(self._current.get("remaining_actions") or []))
        window = self.cfg.stagnation_window
        self._novelty_window = self._novelty_window[-window:]
        self._remaining_window = self._remaining_window[-window:]
        if not is_stagnant(
            self._novelty_window, self._remaining_window,
            window=window, novelty_floor=self.cfg.stagnation_novelty,
        ):
            return None
        if not self._stagnation_escalated:
            self._stagnation_escalated = True
            recovered = self._try_loop_recovery(possible, state)
            if recovered is not None:
                STATS.record_mechanism("stagnation", "escalate")
                return recovered
        self._current["stagnation_detected"] = True
        STATS.record_mechanism("stagnation", "terminate")
        self._mark_blocked_or_drop(
            "Stagnation: novelty below threshold and remaining steps did not shrink.",
        )
        return self._continue_next_feature(possible, state)

    def _mark_blocked_or_drop(self, reason):
        if not self._current:
            return
        if self._current.get("retry_attempted"):
            status = STATUS_PARTIAL if self._current.get("completed_actions") else STATUS_DROPPED
            self._drop_current(status, reason)
            return
        self._current["blocked_no_progress"] = True
        self._drop_current(STATUS_BLOCKED, reason or "blocked_no_progress")

    def _next_work_feature(self):
        """Pending guide feature, else one retry of blocked features. Hybrid is leftover."""
        if not self.journal:
            return None
        nxt = self.journal.next_pending()
        if nxt is not None:
            return nxt
        self._first_pass_complete = True
        if self._start_retry_pass():
            return self.journal.next_pending()
        return None

    def _hybrid_still_pending(self):
        return bool(
            getattr(self, "cfg", None)
            and self.cfg.enabled("hybrid_discovery")
            and not self._discovery_done
            and self._seen_hub
            and self._first_pass_complete
        )

    def _start_retry_pass(self):
        if self._retry_pass_started or not self.journal:
            return False
        blocked = [
            item for item in self.journal.features()
            if item.get("status") == STATUS_BLOCKED and not item.get("retry_attempted")
        ]
        if not blocked:
            return False
        self._retry_pass_started = True
        for item in blocked:
            item["retry_attempted"] = True
            item["status"] = "pending"
            item["reason"] = "Retry after later features discovered new states."
        line = "Retry pass: re-attempting %d blocked feature(s): %s" % (
            len(blocked),
            ", ".join(item.get("id") for item in blocked),
        )
        self.logger.info(line)
        self.journal._append_log(line)
        self.journal.save()
        return True

    def _maybe_feature_cluster_stall(self, possible, state):
        if not self._current:
            return None
        stall_n = int(getattr(self.cfg, "progress_stall_steps", 10) or 10)
        if self._feature_steps < stall_n:
            return None
        new_states = [
            item for item in self._feature_seen_states
            if item and item not in self._states_before_feature
        ]
        if new_states:
            return None
        if not self._feature_reset_tried:
            self._feature_reset_tried = True
            reset = self._hub_reset_event(possible, state)
            line = (
                "Feature %s made no new states after %d actions; hard navigation reset."
                % ((self._current or {}).get("id"), stall_n)
            )
            self.logger.info(line)
            if self.journal:
                self.journal._append_log(line)
            if reset is not None:
                reset.skip_oracle = True
                return self._emit(reset, "Hard navigation reset after no-progress cluster.", matched="")
            return self._restart_app("Hard reset: restart app after no-progress cluster.")
        self._mark_blocked_or_drop(
            "blocked_no_progress: stayed in the same state cluster after %d actions." % stall_n,
        )
        return self._continue_next_feature(possible, state)

    def _hub_reset_event(self, possible, state):
        home = self._nav_tab_matching(possible, ("home", "tracks", "songs", "library"))
        if home is not None:
            return home
        if self._looks_like_hub(possible, state):
            return None
        if not self._back_would_leave_app(state):
            return KeyEvent(name="BACK")
        return None

    def _mandatory_fill(self, possible, state):
        remaining = list((self._current or {}).get("remaining_actions") or [])
        if not remaining or not _is_typing_step(remaining[0]):
            return None
        fields = [event for event in possible or [] if _can_set_text(event)]
        if not fields:
            return None
        for event in fields:
            view = getattr(event, "view", None) or {}
            key = "%s|%s|%s" % (
                view.get("resource_id") or "",
                view.get("text") or "",
                view.get("content_description") or "",
            )
            if key in self._unresolved_fields:
                continue
            text = None
            if self.advisor:
                text = self.advisor.fill_text(
                    view, remaining, feature=self._current, allow_unresolved=False,
                )
            if text is None:
                self._unresolved_fields.add(key)
                continue
            event.text = text
            event.skip_oracle = True
            self._arm_pending_fill(event, remaining, state, text)
            return self._emit(
                event,
                "Mandatory fill of required text field.",
                matched="",
                source="mandatory_fill",
                text=text,
            )
        return None

    def _arm_pending_fill(self, event, remaining, state, text):
        view = getattr(event, "view", None) or {}
        self._pending_fill = {
            "step": (remaining or [""])[0],
            "value": text,
            "state_before": getattr(state, "state_str", "") or "",
            "field": view.get("text") or view.get("resource_id") or "text field",
        }

    def _verify_pending_fill(self, state, possible):
        pending = self._pending_fill
        if not pending:
            return None
        self._pending_fill = None
        value = pending.get("value") or ""
        before = pending.get("state_before") or ""
        now = getattr(state, "state_str", "") or ""
        blob = self._screen_blob(state, possible)
        error = any(token in blob for token in (
            "invalid", "required field", "can't be empty", "cannot be empty",
            "this field", "enter a valid",
        ))
        shown = False
        for view in getattr(state, "views", None) or []:
            text = str(view.get("text") or "")
            if value and value in text:
                shown = True
                break
        accepted = (not error) and (now != before or shown)
        from .run_stats import STATS
        STATS.record_text(value, "verify", field=pending.get("field") or "", accepted=accepted)
        line = "set_text accepted=%s value=%r field=%r" % (
            accepted, value, pending.get("field"),
        )
        self.logger.info(line)
        if self.journal:
            self.journal._append_log(line)
        if accepted and self._current:
            self.journal.complete_step(self._current, pending.get("step") or "")
        return None

    def _maybe_hybrid_discovery(self, possible, state):
        if self._discovery_done or not self.cfg.enabled("hybrid_discovery"):
            return None
        if not self._seen_hub:
            return None
        from .discovery import collect_affordance_labels
        for label in collect_affordance_labels(possible):
            if label not in self._observed_labels:
                self._observed_labels.append(label)
        # Observe during first-run setup but do not crawl or commit yet —
        # undocumented features live on later screens (search, plugins, …).
        if self._current and self._is_setup_feature():
            return None
        if not self._first_pass_complete:
            return None
        # Guide-list features (including the retry pass) go first; hybrid is leftover.
        if self._current is not None:
            return None
        state_str = getattr(state, "state_str", "") or ""
        visits = self._discovery_state_repeats.get(state_str, 0) if state_str else 0
        if state_str:
            self._discovery_state_repeats[state_str] = visits + 1
        if visits >= 2:
            self._commit_discovery("repeat-detected")
            return None
        budget = self.cfg.discovery_budget
        if self._discovery_steps < budget:
            if not self._discovery_phase:
                self._discovery_label_baseline = len(self._observed_labels)
            self._discovery_phase = True
            for event in possible or []:
                if self._is_back(event) or self._looks_like_external_link(event):
                    continue
                if self._is_stale_onboarding_cta(event):
                    continue
                if self._is_dead_end_copy(event):
                    continue
                widget_key = self._widget_try_key(event)
                pair = (state_str, widget_key)
                if pair in self._discovery_pairs:
                    continue
                if widget_key in self._discovery_tried_widgets:
                    continue
                if self._tap_counts.get(self._action_key(state, event), 0) > 0:
                    continue
                unlabeled = not _event_label(event).strip()
                if unlabeled and not getattr(event, "nav_label", None):
                    continue
                self._discovery_pairs.add(pair)
                self._discovery_tried_widgets.add(widget_key)
                if state_str:
                    self._discovery_seen_states.add(state_str)
                self._discovery_steps += 1
                STATS.record_mechanism("hybrid_discovery", "crawl %d" % self._discovery_steps)
                event.skip_oracle = True
                self.logger.info("Hybrid discovery crawl: %s" % _event_label(event))
                if self.journal:
                    self.journal._append_log(
                        "Hybrid discovery observed: %s" % _event_label(event)
                    )
                return event
            self._commit_discovery("repeat-detected")
            return None
        self._commit_discovery("budget-exhausted")
        return None

    def _commit_discovery(self, reason="budget-exhausted"):
        if self._discovery_done:
            return
        self._discovery_done = True
        self._discovery_phase = False
        n_new = max(0, len(self._observed_labels) - int(self._discovery_label_baseline or 0))
        line = (
            "Hybrid discovery stopped after %d actions, %d new affordances found, "
            "exited due to %s"
            % (self._discovery_steps, n_new, reason)
        )
        self.logger.info(line)
        if self.journal:
            self.journal._append_log(line)
        from .discovery import infer_missing_features
        added = infer_missing_features(
            self._observed_labels,
            self.journal.features() if self.journal else [],
            app_name=self.app.app_name if self.app else "",
        )
        if added and self.journal:
            records = self.journal.append_features(added)
            STATS.record_mechanism("hybrid_discovery", "added %d" % len(records))
            self.logger.info("Hybrid discovery added %d features." % len(records))
        elif not added:
            empty = "Hybrid discovery proposed 0 mergeable features (none, all discarded, or LLM disabled)."
            self.logger.info(empty)
            if self.journal:
                self.journal._append_log(empty)

    def _finish_run(self, reason):
        if self._finished:
            return
        self.logger.info(reason)
        self._finalize_journal()

    def _finalize_journal(self, run_discovery=True):
        if self._finished:
            return
        if (
            run_discovery
            and not self._discovery_done
            and getattr(self, "cfg", None)
            and self.cfg.enabled("hybrid_discovery")
            and self._seen_hub
        ):
            try:
                self._commit_discovery("run-finished")
            except KeyboardInterrupt:
                self.logger.info("Hybrid discovery interrupted; writing coverage anyway.")
            except Exception as exc:
                self.logger.warning("Hybrid discovery at finish skipped: %s" % exc)
        if self.journal:
            extra = {
                "shared_flow_reuses": list(self.chain_memory.reuses),
                "run_cost": STATS.to_dict(),
                "exploration_bank": getattr(self, "step_bank", None),
            }
            try:
                self.journal.finalize(extra=extra)
            except KeyboardInterrupt:
                try:
                    self.journal.finalize(extra=extra)
                except Exception as exc:
                    self.logger.warning("Could not write coverage after interrupt: %s" % exc)
            except Exception as exc:
                self.logger.warning("Could not write coverage report: %s" % exc)
            try:
                self.chain_memory.save(os.path.join(self.journal.root, "chain_memory.json"))
            except Exception:
                pass
        self._finished = True


def _can_set_text(event):
    return isinstance(event, SetTextEvent) or getattr(event, "event_type", "") == "set_text"


def _has_searchish_field(events):
    """True when a visible field is actually a search/query box, not any EditText."""
    for event in events or []:
        if not _can_set_text(event) and not _is_set_text(event):
            view = getattr(event, "view", None) or {}
            cls = (_view_text(view.get("class")) or "").lower()
            if not any(token in cls for token in ("edittext", "textfield", "searchview", "autocompletetext")):
                continue
        view = getattr(event, "view", None) or {}
        blob = " ".join((
            _view_text(view.get("text")),
            _view_text(view.get("content_description")),
            _view_text(view.get("resource_id")),
            _view_text(view.get("hint")),
        )).lower()
        if any(token in blob for token in ("search", "query", "find")):
            return True
    return False


def _label_has_phrase(label, phrase):
    if not label or not phrase:
        return False
    if " " in phrase or "'" in phrase or len(phrase) >= 10:
        return phrase in label
    return re.search(r"\b%s\b" % re.escape(phrase), label) is not None


def _safe_event_str(event, state):
    try:
        if state is not None:
            return event.get_event_str(state)
    except Exception:
        pass
    return event.__class__.__name__


def _load_feature_payload(output_dir, readme_path, features_path, app_name,
                          apk_path=None, guide_path=None):
    """Load the live exploration list.

    Priority: guide_features.json > non-gold -features JSON > README extract >
    local parser. README extraction always runs (and is written) when a README
    exists; it does not silently merge into the live list.
    """
    from .guide import (
        classify_ground_truth_source,
        diff_feature_lists,
        discover_guide_features,
        load_feature_json,
        mark_source,
    )
    from .specs import is_eval_only_feature_list

    if not guide_path:
        guide_path = discover_guide_features(apk_path)

    readme_extracted = _extract_readme_features(output_dir, readme_path, app_name)

    live = None
    source = None
    live_path = None
    if guide_path and os.path.isfile(guide_path):
        live = load_feature_json(guide_path)
        if live:
            source = "guide"
            live_path = os.path.abspath(guide_path)
            print("Live exploration driven by guide list: %s (%d features)" % (
                live_path, len(live.get("features") or []),
            ))
    if live is None and features_path and os.path.isfile(features_path):
        if is_eval_only_feature_list(features_path):
            print(
                "Ignoring %s for live guidance (evaluation-only)." % features_path
            )
        else:
            live = load_feature_json(features_path)
            if live:
                source = "cli"
                live_path = os.path.abspath(features_path)
                print("Live exploration driven by -features: %s (%d features)" % (
                    live_path, len(live.get("features") or []),
                ))
    if live is None and readme_extracted and readme_extracted.get("features"):
        live = readme_extracted
        source = "readme"
        live_path = os.path.join(output_dir, "features_from_readme.json") if output_dir else None
        print("Live exploration driven by README extraction (%d features)." % (
            len(live.get("features") or []),
        ))
    if live is None:
        live = extract_features_locally(
            "", app_name=app_name, allow_numbered_spec=False,
        )
        try:
            from droidbot.feature_tester.granularity import refine_granularity
            live = refine_granularity(live, app_name=app_name)
        except Exception:
            pass
        source = "local_readme"

    live = mark_source(live, source or "readme")
    live["feature_source"] = source or "readme"
    live["guide_features_path"] = live_path if source == "guide" else guide_path
    live["live_features_path"] = live_path

    if source in ("guide", "cli") and readme_extracted and readme_extracted.get("features"):
        diff = diff_feature_lists(live, readme_extracted)
        live["guide_vs_readme"] = diff
        print(
            "Guide vs README-extracted: both=%d guide-only=%d readme-only=%d"
            % (len(diff["both"]), len(diff["guide_only"]), len(diff["readme_only"]))
        )
        if output_dir:
            from droidbot.output_layout import hidden_file
            path = hidden_file(output_dir, "guide_vs_readme.json") or os.path.join(output_dir, "guide_vs_readme.json")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(diff, handle, indent=2)
                handle.write("\n")
    else:
        live["guide_vs_readme"] = None

    if output_dir:
        _write_live_features(output_dir, live)
    return live


def _extract_readme_features(output_dir, readme_path, app_name):
    cached = None
    for cached_path in _readme_cache_paths(output_dir):
        if cached_path and os.path.isfile(cached_path):
            try:
                with open(cached_path, "r", encoding="utf-8") as handle:
                    cached = json.load(handle)
            except Exception:
                cached = None
            if cached and cached.get("features"):
                for item in cached.get("features") or []:
                    item.setdefault("source", "readme")
                return cached
            break
    readme = ""
    if readme_path and os.path.isfile(readme_path):
        with open(readme_path, "r", encoding="utf-8") as handle:
            readme = handle.read()
        try:
            from droidbot.feature_eval.feature_extractor import FeatureExtractor
            extracted = FeatureExtractor().extract(
                readme_path=readme_path,
                app_name=app_name,
                allow_numbered_spec=False,
            )
            if extracted and extracted.get("features"):
                for item in extracted.get("features") or []:
                    item.setdefault("source", "readme")
                if output_dir:
                    _write_readme_features(output_dir, extracted)
                try:
                    from droidbot.feature_tester.run_stats import STATS
                    STATS.record_llm("feature_extraction")
                except Exception:
                    pass
                return extracted
        except Exception as exc:
            print("README LLM extract failed, using local parser: %s" % exc)
    payload = extract_features_locally(
        readme, app_name=app_name, allow_numbered_spec=False,
    )
    try:
        from droidbot.feature_tester.granularity import refine_granularity
        payload = refine_granularity(payload, app_name=app_name)
    except Exception:
        pass
    for item in payload.get("features") or []:
        item.setdefault("source", "readme")
    if output_dir:
        _write_readme_features(output_dir, payload)
    return payload


def _readme_cache_paths(output_dir):
    if not output_dir:
        return []
    from droidbot.output_layout import hidden_file
    return [
        hidden_file(output_dir, "features_from_readme.json"),
        os.path.join(output_dir, "features_from_readme.json"),
    ]


def _write_readme_features(output_dir, payload):
    if not output_dir:
        return
    from droidbot.output_layout import hidden_file
    path = hidden_file(output_dir, "features_from_readme.json") or os.path.join(
        output_dir, "features_from_readme.json"
    )
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def _write_live_features(output_dir, payload):
    if not output_dir:
        return
    test_dir = os.path.join(output_dir, "feature_test")
    os.makedirs(test_dir, exist_ok=True)
    with open(os.path.join(test_dir, "features.json"), "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
