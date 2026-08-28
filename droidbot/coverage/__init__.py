"""Runtime code-coverage monitoring.

Mirrors the structure of LLMDroid's ``droidbot/coverage`` package so the two
tools' ``codecoverage.txt`` files can be diffed directly. Unlike LLMDroid we
keep coverage a pure observer: it never feeds back into exploration or
termination decisions, so the number stays a measurement rather than a signal
the policy is optimising against.
"""

from .base_monitor import CodeCoverageMonitor
from .androlog_monitor import AndroLogCVMonitor

__all__ = ["CodeCoverageMonitor", "AndroLogCVMonitor", "make_monitor"]


def make_monitor(method, output_dir, **kwargs):
    """Build a monitor, or return None when coverage is disabled."""
    if not method or method == "none":
        return None
    if method == "androlog":
        return AndroLogCVMonitor(save_dir=output_dir, **kwargs)
    raise ValueError("unknown coverage method: %s" % method)
