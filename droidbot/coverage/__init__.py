"""Runtime code-coverage monitoring.

Mirrors the structure of LLMDroid's ``droidbot/coverage`` package so the two
tools' ``codecoverage.txt`` files can be diffed directly. Unlike LLMDroid we
keep coverage a pure observer: it never feeds back into exploration or
termination decisions, so the number stays a measurement rather than a signal
the policy is optimising against.
"""

import os

from .base_monitor import CodeCoverageMonitor
from .androlog_monitor import AndroLogCVMonitor

__all__ = ["CodeCoverageMonitor", "AndroLogCVMonitor", "make_monitor"]


def make_monitor(method, output_dir, **kwargs):
    """Build a monitor, or return None when coverage is disabled."""
    if not method or method == "none":
        return None
    if method == "androlog":
        return AndroLogCVMonitor(save_dir=output_dir, **kwargs)
    if method == "jacoco":
        config_path = kwargs.pop("jacoco_config", None)
        if not config_path:
            raise ValueError(
                "JaCoCo coverage requires --jacoco-config pointing to "
                "jococo_test/output/<app>/jacoco.config.json"
            )
        import sys
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        if repo_root not in sys.path:
            sys.path.insert(0, repo_root)
        from jococo_test.monitor.jacoco_monitor import monitor_from_config
        return monitor_from_config(
            config_path,
            save_dir=output_dir,
            udid=kwargs.pop("udid", None),
        )
    raise ValueError("unknown coverage method: %s" % method)
