"""Tests for the one-hour wall-clock budget (droidbot/run_budget.py).

Every run is cut off at a fixed wall clock so a batch of APKs takes a
predictable time and neither tool wins the coverage comparison just by
exploring for longer. These pin the two things that has to guarantee: the run
stops within one action of the deadline, and it stops that way for *every*
policy, not only feature_guided.
"""

import logging
import time

import pytest

from droidbot import input_manager as im
from droidbot.feature_tester.config import FeatureTesterConfig, get_config, set_config
from droidbot.feature_tester.policy import FeatureGuidedPolicy
from droidbot.input_policy import InputInterruptedException, InputPolicy
from droidbot.run_budget import RunBudget


class _SlowPolicy(InputPolicy):
    """Each event costs real time, standing in for a model call."""

    def __init__(self, cost=0.2):
        self.logger = logging.getLogger("SlowPolicy")
        self.action_count = 0
        self.master = object()
        self.cost = cost

    def generate_event(self):
        time.sleep(self.cost)
        return object()


class _FakeDevice(object):
    serial = "emulator-test"
    output_dir = None
    pause_sending_event = False


class _FakeApp(object):
    app_path = None
    activities = []

    def get_package_name(self):
        return "com.example"


class _NoopEventLog(object):
    def __init__(self, *args, **kwargs):
        pass

    def start(self):
        pass

    def stop(self):
        pass


@pytest.fixture
def manager(monkeypatch):
    """An InputManager wired to fakes, with a 1s budget and no watchdog."""
    previous = get_config()
    cfg = FeatureTesterConfig()
    cfg.max_run_seconds = 1
    cfg.run_grace_seconds = 3600     # keep the hard stop out of the test
    cfg.code_coverage = "none"
    set_config(cfg)
    monkeypatch.setattr(im, "EventLog", _NoopEventLog)

    manager = im.InputManager.__new__(im.InputManager)
    manager.logger = logging.getLogger("InputEventManager")
    manager.enabled = True
    manager.device = _FakeDevice()
    manager.app = _FakeApp()
    manager.policy_name = "dfs_greedy"
    manager.policy = _SlowPolicy()
    manager.events = []
    manager.event_count = 10 ** 8
    manager.event_interval = 0
    manager.profiling_method = None
    manager.monkey = None
    manager.script = None
    manager.budget = RunBudget(seconds=0)
    manager.coverage_monitor = None
    yield manager
    manager.budget.cancel()
    set_config(previous)


def test_budget_reads_the_configured_threshold(manager):
    manager._start_run_budget()
    assert manager.budget.seconds == 1
    assert manager.budget.grace == 3600


def test_add_event_refuses_once_the_deadline_passes(manager):
    manager._start_run_budget()
    manager.add_event(object())
    assert len(manager.events) == 1

    time.sleep(1.05)
    with pytest.raises(InputInterruptedException):
        manager.add_event(object())
    # The refused event is not recorded: it was never sent, so it must not
    # count towards the actions the run is credited with.
    assert len(manager.events) == 1


def test_run_stops_within_one_action_of_the_deadline(manager):
    started = time.time()
    manager.start()
    elapsed = time.time() - started
    assert 1.0 <= elapsed < 1.0 + 2 * manager.policy.cost


def test_budget_disabled_by_zero():
    budget = RunBudget(seconds=0).start()
    assert not budget.enabled
    assert not budget.expired()
    assert budget.remaining() == float("inf")


def test_fraction_used_tracks_the_clock():
    budget = RunBudget(seconds=10, grace=3600).start()
    assert budget.fraction_used() == pytest.approx(0.0, abs=0.05)
    budget.started_at = time.time() - 9
    assert budget.fraction_used() == pytest.approx(0.9, abs=0.05)
    budget.cancel()


def test_pacing_follows_whichever_budget_binds():
    """With an hour on the clock the event cap never fires, so pacing that
    counted only actions would think the run had barely started."""
    policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
    policy.cfg = FeatureTesterConfig()
    policy.action_count = 0
    policy._budget = RunBudget(seconds=10)

    policy.action_count = policy.cfg.max_run_events // 2
    assert policy._budget_used() == pytest.approx(0.5, abs=0.01)

    policy.action_count = 0
    policy._budget.start()
    policy._budget.started_at = time.time() - 9
    assert policy._budget_used() == pytest.approx(0.9, abs=0.05)
    assert policy._budget_left() == pytest.approx(0.1, abs=0.05)
    policy._budget.cancel()


def test_budget_helpers_survive_a_half_built_policy():
    """_finalize_journal calls these on interrupt paths, where the policy may
    never have been fully constructed."""
    policy = FeatureGuidedPolicy.__new__(FeatureGuidedPolicy)
    assert policy._budget_used() == 0.0
    assert policy._budget_left() == 1.0
