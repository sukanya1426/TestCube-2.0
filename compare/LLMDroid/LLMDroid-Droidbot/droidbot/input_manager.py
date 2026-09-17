import subprocess
import time
from typing import Literal

from .input_event import EventLog
from .run_budget import RunBudget, DEFAULT_GRACE_SECONDS, DEFAULT_RUN_SECONDS
from .policy.input_policy import *
from .policy.manual_policy import ManualPolicy
from .policy.utg_based_policy import UtgBasedInputPolicy
from .policy.utg_greedy_search_policy import UtgGreedySearchPolicy
from .policy.utg_naive_search_policy import UtgNaiveSearchPolicy
from .policy.utg_replay_policy import UtgReplayPolicy

# UtgGreedySearchPolicy, \
#                          UtgReplayPolicy, \
#                          ManualPolicy

DEFAULT_POLICY = POLICY_GREEDY_DFS
DEFAULT_EVENT_INTERVAL = 1
DEFAULT_EVENT_COUNT = 100000000
# One hour, matching TestCube. A run that stops when the explorer decides it is
# done takes an unpredictable amount of time and cannot be compared against a
# tool that happened to run longer.
DEFAULT_TIMEOUT = DEFAULT_RUN_SECONDS


class UnknownInputException(Exception):
    pass


class InputManager(object):
    """
    This class manages all events to send during app running
    """

    def __init__(self, device, app, policy_name, random_input,
                 event_count, event_interval,
                 code_coverage: Literal['time', 'androlog', 'jacoco'],
                 script_path=None, profiling_method=None, master=None,
                 replay_output=None, timeout=DEFAULT_TIMEOUT,
                 grace=DEFAULT_GRACE_SECONDS
                 ):
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
        # Wall-clock budget for the run. Started in start(), enforced in
        # add_event() so it binds on every policy.
        self.timeout = timeout
        self.grace = grace
        self.budget = RunBudget(seconds=0)
        self._coverage_finalized = False

        if script_path is not None:
            f = open(script_path, 'r')
            script_dict = json.load(f)
            from .input_script import DroidBotScript
            self.script = DroidBotScript(script_dict)

        self.policy = self.get_input_policy(device, app, master, code_coverage)
        self.profiling_method = profiling_method

    def get_input_policy(self, device, app, master, code_coverage):
        if self.policy_name == POLICY_NONE:
            input_policy = None
        elif self.policy_name == POLICY_MONKEY:
            input_policy = None
        elif self.policy_name in [POLICY_NAIVE_DFS, POLICY_NAIVE_BFS]:
            input_policy = UtgNaiveSearchPolicy(device, app, self.random_input, self.policy_name, code_coverage)
        elif self.policy_name in [POLICY_GREEDY_DFS, POLICY_GREEDY_BFS]:
            input_policy = UtgGreedySearchPolicy(device, app, self.random_input, self.policy_name, code_coverage)
        elif self.policy_name == POLICY_MEMORY_GUIDED:
            from .input_policy2 import MemoryGuidedPolicy
            input_policy = MemoryGuidedPolicy(device, app, self.random_input, code_coverage)
        elif self.policy_name == POLICY_LLM_GUIDED:
            from .input_policy3 import LLM_Guided_Policy
            input_policy = LLM_Guided_Policy(device, app, self.random_input)
        elif self.policy_name == POLICY_REPLAY:
            input_policy = UtgReplayPolicy(device, app, self.replay_output)
        elif self.policy_name == POLICY_MANUAL:
            input_policy = ManualPolicy(device, app, code_coverage)
        else:
            self.logger.warning("No valid input policy specified. Using policy \"none\".")
            input_policy = None
        if isinstance(input_policy, UtgBasedInputPolicy):
            input_policy.script = self.script
            input_policy.master = master
        return input_policy

    def _start_run_budget(self):
        """Start the wall clock for this run."""
        self.budget = RunBudget(
            seconds=self.timeout, grace=self.grace,
            on_expire=self._write_reports_for_hard_stop,
            logger=self.logger,
        )
        self.budget.start()

    def _write_reports_for_hard_stop(self):
        """Salvage the reports when the watchdog is about to kill the run.

        Called from the watchdog thread, so it can only touch things that do
        not need the event loop — which is exactly what is stuck.
        """
        self.enabled = False
        self._finalize_coverage()
        finalize = getattr(self.policy, "finalize_on_hard_stop", None)
        if callable(finalize):
            try:
                finalize()
            except Exception as e:
                self.logger.warning("Could not finalize the policy report: %s" % e)

    def _finalize_coverage(self):
        """Take one last coverage sample.

        codecoverage.txt is appended to once per step, so the file survives any
        ending; without this the final number would be up to one step stale,
        and the last step is where a time-bounded run stops.

        Once only: stop() is reached more than once per run, and a repeated
        sample would pad codecoverage.txt with flat entries and skew the
        saturation figure computed from it.
        """
        if self._coverage_finalized:
            return
        self._coverage_finalized = True
        finalize = getattr(self.policy, "finalize_coverage", None)
        if callable(finalize):
            try:
                finalize()
            except Exception as e:
                self.logger.warning("Could not take the final coverage sample: %s" % e)

    def add_event(self, event):
        """
        add one event to the event list
        :param event: the event to be added, should be subclass of AppEvent
        :return:
        """
        if event is None:
            return
        # Checked here rather than only at the top of the policy loop:
        # generating one event can take minutes of model calls, and an event
        # produced after the deadline must not still be sent.
        if self.budget.expired():
            raise InputInterruptedException(self.budget.reason())
        self.events.append(event)

        event_log = EventLog(self.device, self.app, event, self.profiling_method)
        event_log.start()
        while True:
            time.sleep(self.event_interval)
            if not self.device.pause_sending_event:
                break
        event_log.stop()

    def start(self):
        """
        start sending event
        """
        self.logger.info("start sending events, policy is %s" % self.policy_name)
        self._start_run_budget()

        try:
            if self.policy is not None:
                self.policy.start(self)
            elif self.policy_name == POLICY_NONE:
                self.device.start_app(self.app)
                if self.event_count == 0:
                    return
                while self.enabled and not self.budget.expired():
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
        except InputInterruptedException as e:
            # A policy that does not handle it itself (monkey, none, manual).
            self.logger.info("stop sending events: %s" % e)

        self._finalize_coverage()
        self.stop()
        self.logger.info(
            "Finish sending events (%d actions in %.0fs)"
            % (len(self.events), self.budget.elapsed())
        )

    def stop(self):
        """
        stop sending event
        """
        if self.policy and isinstance(self.policy, UtgBasedInputPolicy):
            self.policy.debug_states()

        if self.monkey:
            if self.monkey.returncode is None:
                self.monkey.terminate()
            self.monkey = None
            pid = self.device.get_app_pid("com.android.commands.monkey")
            if pid is not None:
                self.device.adb.shell("kill -9 %d" % pid)
        self.enabled = False

