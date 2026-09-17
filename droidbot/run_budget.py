"""Wall-clock budget for one test run.

A run used to end when the explorer decided it had finished exploring, which
makes a batch of APKs take an unpredictable amount of time and makes two tools
incomparable: whichever one keeps going longer wins on coverage by default.
Instead every run gets the same fixed wall-clock threshold — one hour — and
TestCube and LLMDroid are both measured over that same hour.

Two layers enforce it:

* the **soft** deadline, checked at the top of the policy loop and again in
  ``InputManager.add_event`` — the one chokepoint every policy routes through,
  so ``dfs_greedy`` is cut off exactly like ``feature_guided``. Crossing it
  raises ``InputInterruptedException``, so the run unwinds along its normal
  shutdown path and every report is written.
* the **hard** deadline, ``grace`` seconds later, enforced by a daemon thread.
  It only fires when the soft deadline could not — a model call that never
  returns, an adb command that hangs — so one wedged app cannot stall a batch
  overnight. It runs ``on_expire`` (which writes the coverage and feature
  reports) before killing the process, and gives it a bounded amount of time
  so a hang in the finalizer cannot defeat the hard stop either.
"""

import logging
import os
import sys
import threading
import time

# One hour. Long enough that both tools saturate on the apps measured so far,
# short enough to run a batch of APKs overnight.
DEFAULT_RUN_SECONDS = 3600
# Headroom for the action in flight to finish before the process is killed.
DEFAULT_GRACE_SECONDS = 300
# Seconds the watchdog waits for the reports to be written before exiting.
FINALIZE_TIMEOUT = 60
# Exit status for a run killed by the watchdog, so a batch driver can tell it
# apart from a clean finish.
EXIT_HARD_STOP = 3

_LOGGER = logging.getLogger("RunBudget")


class RunBudget(object):
    """Tracks the wall clock for a single run.

    ``seconds <= 0`` disables the budget entirely, which is how the old
    "explore until done" behaviour is restored.
    """

    def __init__(self, seconds=DEFAULT_RUN_SECONDS, grace=DEFAULT_GRACE_SECONDS,
                 on_expire=None, logger=None):
        self.seconds = float(seconds or 0)
        self.grace = max(0.0, float(grace or 0))
        self.on_expire = on_expire
        self.logger = logger or _LOGGER
        self.started_at = None
        self.expired_at = None
        self._done = threading.Event()
        self._watchdog = None

    @property
    def enabled(self):
        return self.seconds > 0

    def start(self):
        if self.started_at is not None:
            return self
        self.started_at = time.time()
        if self.enabled:
            self.logger.info(
                "Run budget: %.0fs of wall clock (hard stop at +%.0fs)",
                self.seconds, self.grace,
            )
            self._start_watchdog()
        return self

    def elapsed(self):
        if self.started_at is None:
            return 0.0
        return time.time() - self.started_at

    def remaining(self):
        if not self.enabled:
            return float("inf")
        return self.seconds - self.elapsed()

    def fraction_used(self):
        """0.0 at the start, 1.0 at the deadline; 0.0 when no budget is set."""
        if not self.enabled or self.started_at is None:
            return 0.0
        return min(1.0, self.elapsed() / self.seconds)

    def expired(self):
        if not self.enabled or self.started_at is None:
            return False
        if self.remaining() > 0:
            return False
        if self.expired_at is None:
            self.expired_at = time.time()
        return True

    def reason(self):
        return "wall-clock run budget of %.0fs reached" % self.seconds

    def cancel(self):
        """The run finished on its own; stand the watchdog down."""
        self._done.set()

    # -- hard stop ---------------------------------------------------------

    def _start_watchdog(self):
        self._watchdog = threading.Thread(target=self._watch, name="run-budget-watchdog")
        self._watchdog.daemon = True
        self._watchdog.start()

    def _watch(self):
        if self._done.wait(self.seconds + self.grace):
            return
        self.logger.error(
            "Run is still going %.0fs past its %.0fs budget; writing reports "
            "and killing the process.", self.grace, self.seconds,
        )
        self._finalize()
        for stream in (sys.stdout, sys.stderr):
            try:
                stream.flush()
            except Exception:
                pass
        os._exit(EXIT_HARD_STOP)

    def _finalize(self):
        if not self.on_expire:
            return
        # In its own thread: whatever wedged the run may well wedge the
        # finalizer too, and the hard stop has to happen either way.
        worker = threading.Thread(target=self._run_on_expire, name="run-budget-finalize")
        worker.daemon = True
        worker.start()
        worker.join(FINALIZE_TIMEOUT)
        if worker.is_alive():
            self.logger.error(
                "Reports did not finish writing within %ds; exiting anyway.",
                FINALIZE_TIMEOUT,
            )

    def _run_on_expire(self):
        try:
            self.on_expire()
        except Exception as exc:
            self.logger.error("Could not write reports before hard stop: %s", exc)
