"""Shared bookkeeping for runtime coverage monitors.

The on-disk format matches LLMDroid's ``codecoverage.txt`` (a header, then one
sample per line) so a TestCube run and an LLMDroid run can be compared without
a converter. ``samples`` additionally keeps the series in memory for the JSON
report.
"""

import logging
import os
import time
from abc import ABCMeta, abstractmethod


class CodeCoverageMonitor(object):
    __metaclass__ = ABCMeta

    def __init__(self, save_dir):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.save_dir = save_dir
        self.file_path = os.path.join(save_dir, "codecoverage.txt") if save_dir else None
        self.samples = []
        self.started_at = time.time()
        self._current = 0.0

        if self.file_path:
            try:
                os.makedirs(save_dir, exist_ok=True)
                with open(self.file_path, "w") as handle:
                    handle.write("code coverage\n")
                    stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    handle.write("start time: %s\n" % stamp)
            except IOError as exc:
                self.logger.warning("cannot open coverage file: %s", exc)

    @abstractmethod
    def _get_code_coverage(self):
        """Return current coverage as a percentage."""

    @property
    def current(self):
        return self._current

    def sample(self, action_count=None):
        """Take one reading. Never raises — coverage must not break a run."""
        try:
            percentage = self._get_code_coverage()
        except Exception as exc:
            self.logger.warning("coverage sample failed: %s", exc)
            return self._current
        self._current = percentage
        entry = {
            "elapsed": round(time.time() - self.started_at, 2),
            "coverage": round(percentage, 5),
        }
        if action_count is not None:
            entry["action_count"] = action_count
        entry.update(self._extra_sample_fields())
        self.samples.append(entry)
        self._save_to_file(self._format_sample(entry))
        return percentage

    def _extra_sample_fields(self):
        return {}

    def _format_sample(self, entry):
        return "%8.5f%% @ %.2fs" % (entry["coverage"], entry["elapsed"])

    def _save_to_file(self, content):
        if not self.file_path:
            return
        try:
            with open(self.file_path, "a") as handle:
                handle.write(content + "\n")
        except IOError as exc:
            self.logger.warning("cannot write coverage file: %s", exc)

    def summary(self):
        return {
            "method": getattr(self, "method_name", "unknown"),
            "final_coverage": round(self._current, 5),
            "samples": self.samples,
            "duration": round(time.time() - self.started_at, 2),
            # Actions issued when the last sample was taken; the caller
            # overwrites this with the run's authoritative total.
            "total_actions": self.samples[-1].get("action_count") if self.samples else 0,
        }

    def stop(self):
        pass
