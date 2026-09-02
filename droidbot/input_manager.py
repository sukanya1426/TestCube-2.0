#TestCube-2.0/droidbot/input_manager.py
import json
import logging
import os
import subprocess
import time

from .input_event import EventLog
from .input_policy import UtgBasedInputPolicy, UtgNaiveSearchPolicy, UtgGreedySearchPolicy, \
                         UtgReplayPolicy, \
                         ManualPolicy, \
                         POLICY_NAIVE_DFS, POLICY_GREEDY_DFS, \
                         POLICY_NAIVE_BFS, POLICY_GREEDY_BFS, \
                         POLICY_REPLAY, POLICY_MEMORY_GUIDED, POLICY_LLM_GUIDED, \
                         POLICY_FEATURE_GUIDED, \
                         POLICY_MANUAL, POLICY_MONKEY, POLICY_NONE

DEFAULT_POLICY = POLICY_GREEDY_DFS
DEFAULT_EVENT_INTERVAL = 1
DEFAULT_EVENT_COUNT = 100000000
DEFAULT_TIMEOUT = -1


class UnknownInputException(Exception):
    pass


class InputManager(object):
    """
    This class manages all events to send during app running
    """

    def __init__(self, device, app, policy_name, random_input,
                 event_count, event_interval,
                 script_path=None, profiling_method=None, master=None,
                 replay_output=None):
        """
        manage input event sent to the target device
        :param device: instance of Device
        :param app: instance of App
        :param policy_name: policy of generating events, string
        :return:
        """
        self.logger = logging.getLogger('InputEventManager')
        self.enabled = True

        self.device = device
        self.app = app
        self.policy_name = policy_name
        self.random_input = random_input
        self.events = []
        self.policy = None
        self.script = None
        self.event_count = event_count
        self.event_interval = event_interval
        self.replay_output = replay_output

        self.monkey = None

        if script_path is not None:
            f = open(script_path, 'r')
            script_dict = json.load(f)
            from .input_script import DroidBotScript
            self.script = DroidBotScript(script_dict)

        self.policy = self.get_input_policy(device, app, master)
        self.profiling_method = profiling_method

    def get_input_policy(self, device, app, master):
        if self.policy_name == POLICY_NONE:
            input_policy = None
        elif self.policy_name == POLICY_MONKEY:
            input_policy = None
        elif self.policy_name in [POLICY_NAIVE_DFS, POLICY_NAIVE_BFS]:
            input_policy = UtgNaiveSearchPolicy(device, app, self.random_input, self.policy_name)
        elif self.policy_name in [POLICY_GREEDY_DFS, POLICY_GREEDY_BFS]:
            input_policy = UtgGreedySearchPolicy(device, app, self.random_input, self.policy_name)
        elif self.policy_name == POLICY_MEMORY_GUIDED:
            from .input_policy2 import MemoryGuidedPolicy
            input_policy = MemoryGuidedPolicy(device, app, self.random_input)
        elif self.policy_name == POLICY_LLM_GUIDED:
            from .input_policy3 import LLM_Guided_Policy
            input_policy = LLM_Guided_Policy(device, app, self.random_input)
        elif self.policy_name == POLICY_FEATURE_GUIDED:
            from droidbot.feature_tester.config import get_config
            cfg = get_config()
            if cfg.replay_path:
                from droidbot.feature_tester.replay import ReplayPolicy
                input_policy = ReplayPolicy(device, app, self.random_input, cfg.replay_path)
            else:
                from .feature_tester.policy import FeatureGuidedPolicy
                input_policy = FeatureGuidedPolicy(device, app, self.random_input)
        elif self.policy_name == POLICY_REPLAY:
            input_policy = UtgReplayPolicy(device, app, self.replay_output)
        elif self.policy_name == POLICY_MANUAL:
            input_policy = ManualPolicy(device, app)
        else:
            self.logger.warning("No valid input policy specified. Using policy \"none\".")
            input_policy = None
        if isinstance(input_policy, UtgBasedInputPolicy):
            input_policy.script = self.script
            input_policy.master = master
        return input_policy

    def _start_coverage_monitor(self):
        """Attach a runtime coverage monitor if one was requested.

        Lives here rather than in a policy so every policy — including the
        plain dfs_greedy baseline we compare against — is measured the same way.
        Never fatal: a coverage problem must not abort a test run.
        """
        self.coverage_monitor = None
        try:
            from .feature_tester.config import get_config
            cfg = get_config()
        except Exception:
            return
        method = getattr(cfg, "code_coverage", "none")
        if not method or method == "none":
            return
        try:
            from .coverage import make_monitor

            output_dir = getattr(self.device, "output_dir", None) or getattr(
                self.app, "output_dir", None
            )
            udid = getattr(self.device, "serial", None)

            if method == "jacoco":
                jacoco_config = getattr(cfg, "jacoco_config", None)
                if not jacoco_config:
                    self.logger.warning(
                        "Coverage disabled: --jacoco-config is required for --code-coverage jacoco"
                    )
                    return
                monitor = make_monitor(
                    method, output_dir,
                    jacoco_config=jacoco_config,
                    udid=udid,
                )
                self.coverage_monitor = monitor
                self.logger.info("Code coverage monitor started (jacoco, config=%s)", jacoco_config)
                return

            from .coverage.androlog_monitor import total_methods_from_apk

            total = getattr(cfg, "coverage_total_methods", None)
            if not total:
                apk_path = getattr(self.app, "app_path", None)
                if apk_path and os.path.exists(apk_path):
                    total = total_methods_from_apk(apk_path)
                    self.logger.info("Coverage denominator read from APK: %d methods", total)
            if not total:
                self.logger.warning(
                    "Coverage disabled: pass --coverage-total-methods, or use an "
                    "APK carrying AndroLog probes."
                )
                return
            tag = getattr(cfg, "coverage_tag", None)
            if not tag:
                self.logger.warning("Coverage disabled: --coverage-tag is required.")
                return
            # Manifest-declared activities are the activity-coverage
            # denominator, matching how LLMDroid reports it.
            activities = getattr(self.app, "activities", None) or []
            monitor = make_monitor(
                method, output_dir, tag=tag, total_methods=total,
                activities=activities,
                udid=udid,
            )
            monitor.start()
            self.coverage_monitor = monitor
            self.logger.info("Code coverage monitor started (%s, tag=%s)", method, tag)
        except Exception as exc:
            self.logger.warning("Could not start coverage monitor: %s", exc)
            self.coverage_monitor = None

    def _sample_coverage(self):
        monitor = getattr(self, "coverage_monitor", None)
        if not monitor:
            return
        try:
            from .feature_tester.config import get_config
            interval = max(1, int(getattr(get_config(), "coverage_interval", 10) or 10))
        except Exception:
            interval = 10
        count = len(self.events)
        if count % interval:
            return
        monitor.sample(action_count=count)

    def _stop_coverage_monitor(self):
        """Take a final sample and write the summary next to the run."""
        monitor = getattr(self, "coverage_monitor", None)
        if not monitor:
            return
        try:
            monitor.sample(action_count=len(self.events))
            summary = monitor.summary()
            # Total actions the tool actually issued. Coverage is only
            # interpretable next to the effort that produced it.
            summary["total_actions"] = len(self.events)
            self.coverage_summary = summary
            output_dir = getattr(self.device, "output_dir", None)
            if output_dir:
                try:
                    with open(os.path.join(output_dir, "code_coverage.json"), "w") as handle:
                        json.dump(summary, handle, indent=2)
                except IOError as exc:
                    self.logger.warning("Could not write code_coverage.json: %s", exc)
            self.logger.info(
                "Final code coverage: %.5f%% (%s/%s methods) after %d actions",
                summary.get("final_coverage", 0.0),
                summary.get("methods_hit", "?"),
                summary.get("total_methods", "?"),
                summary.get("total_actions", 0),
            )
            if summary.get("total_activities"):
                self.logger.info(
                    "Final activity coverage: %.2f%% (%s/%s activities)",
                    summary.get("activity_coverage", 0.0),
                    summary.get("activities_hit", "?"),
                    summary.get("total_activities", "?"),
                )
        except Exception as exc:
            self.logger.warning("Could not finalize coverage: %s", exc)
        finally:
            try:
                monitor.stop()
            except Exception:
                pass
            self.coverage_monitor = None

    def add_event(self, event):
        """
        add one event to the event list
        :param event: the event to be added, should be subclass of AppEvent
        :return:
        """
        if event is None:
            return
        self.events.append(event)

        event_log = EventLog(self.device, self.app, event, self.profiling_method)
        event_log.start()
        while True:
            time.sleep(self.event_interval)
            if not self.device.pause_sending_event:
                break
        event_log.stop()
        self._sample_coverage()

    def start(self):
        """
        start sending event
        """
        self.logger.info("start sending events, policy is %s" % self.policy_name)
        self._start_coverage_monitor()

        try:
            if self.policy is not None:
                self.policy.start(self)
            elif self.policy_name == POLICY_NONE:
                self.device.start_app(self.app)
                if self.event_count == 0:
                    return
                while self.enabled:
                    time.sleep(1)
            elif self.policy_name == POLICY_MONKEY:
                throttle = self.event_interval * 1000
                monkey_cmd = "adb -s %s shell monkey %s --ignore-crashes --ignore-security-exceptions" \
                             " --throttle %d -v %d" % \
                             (self.device.serial,
                              "" if self.app.get_package_name() is None else "-p " + self.app.get_package_name(),
                              throttle,
                              self.event_count)
                self.monkey = subprocess.Popen(monkey_cmd.split(),
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                for monkey_out_line in iter(self.monkey.stdout.readline, ''):
                    if not isinstance(monkey_out_line, str):
                        monkey_out_line = monkey_out_line.decode()
                    self.logger.info(monkey_out_line)
                # may be disturbed from outside
                if self.monkey is not None:
                    self.monkey.wait()
            elif self.policy_name == POLICY_MANUAL:
                self.device.start_app(self.app)
                while self.enabled:
                    keyboard_input = input("press ENTER to save current state, type q to exit...")
                    if keyboard_input.startswith('q'):
                        break
                    state = self.device.get_current_state()
                    if state is not None:
                        state.save2dir()
        except KeyboardInterrupt:
            pass

        self._stop_coverage_monitor()
        self.stop()
        self.logger.info("Finish sending events")

    def stop(self):
        """
        stop sending event
        """
        if self.monkey:
            if self.monkey.returncode is None:
                self.monkey.terminate()
            self.monkey = None
            pid = self.device.get_app_pid("com.android.commands.monkey")
            if pid is not None:
                self.device.adb.shell("kill -9 %d" % pid)
        self.enabled = False

