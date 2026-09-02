"""JaCoCo runtime coverage monitor (LLMDroid-compatible, TestCube observer).

Requires a JaCoCo-instrumented APK (see jococo_test/scripts/instrument_apk.py)
and a jacoco.config.json with ClassFilePath / EcFilePath / EcFileName.
"""

import logging
import os
import subprocess
import threading
import time

from droidbot.coverage.base_monitor import CodeCoverageMonitor

JOCO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "jococo_test")
)
DEFAULT_JAR = os.path.join(JOCO_ROOT, "JacocoBridge", "JacocoBridge.jar")


class JacocoCVMonitor(CodeCoverageMonitor):
    method_name = "jacoco"

    def __init__(
        self,
        save_dir,
        ec_file_name,
        ec_file_path,
        class_file_path,
        jarpath=None,
        udid=None,
    ):
        super(JacocoCVMonitor, self).__init__(save_dir=save_dir)
        self.jar_path = jarpath or DEFAULT_JAR
        self.udid = udid or ""
        self.ec_file_name = ec_file_name
        self.ec_file_path = ec_file_path
        self.class_file_path = class_file_path
        self._lock = threading.Lock()
        self._last = 0.0
        self._jvm = None
        self._bridge_class = None
        self.logger = logging.getLogger(self.__class__.__name__)

        if not os.path.isfile(self.jar_path):
            raise FileNotFoundError(
                "JacocoBridge.jar not found at %s — run bash jococo_test/setup.sh"
                % self.jar_path
            )
        if not os.path.isdir(self.class_file_path):
            raise FileNotFoundError(
                "ClassFilePath not found: %s (instrument APK first)" % self.class_file_path
            )
        self._start_jvm()

    def _start_jvm(self):
        try:
            import jpype
            import jpype.imports
            from jpype.types import JString
        except ImportError as exc:
            raise ImportError(
                "JaCoCo monitor needs jpype1: pip install jpype1"
            ) from exc
        if not jpype.isJVMStarted():
            self.logger.info("Starting JVM for JacocoBridge")
            jpype.startJVM(classpath=self.jar_path)
        self._jpype = jpype
        self._JString = JString
        self._bridge_class = jpype.JClass("org.jacoco.examples.JacocoBridge")

    def _get_code_coverage(self):
        event = threading.Event()
        result_holder = {"value": self._last}

        def worker():
            try:
                bridge = self._bridge_class(
                    self._JString(self.udid),
                    self._JString(self.save_dir or "."),
                )
                java_file = self._jpype.JClass("java.io.File")
                ratio = bridge.getMethodCoverage(
                    self._JString(self.ec_file_name),
                    self._JString(self.ec_file_path),
                    java_file(self.class_file_path),
                )
                pct = float(ratio) * 100.0
                with self._lock:
                    self._last = pct
                    result_holder["value"] = pct
            except Exception as exc:
                self.logger.warning("JacocoBridge sample failed: %s", exc)
            finally:
                event.set()

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()
        if not event.wait(1.5):
            self.logger.warning("JacocoBridge timed out; using last sample")
        return result_holder["value"]

    def summary(self):
        data = super(JacocoCVMonitor, self).summary()
        data.update({
            "ec_file_name": self.ec_file_name,
            "ec_file_path": self.ec_file_path,
            "class_file_path": self.class_file_path,
            "methods_hit": None,
            "total_methods": None,
        })
        return data

    def stop(self):
        try:
            if self._jpype and self._jpype.isJVMStarted():
                self.logger.info("Shutting down JVM")
                self._jpype.shutdownJVM()
        except Exception:
            pass


def load_jacoco_config(path):
    import json
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def monitor_from_config(config_path, save_dir, udid=None):
    cfg = load_jacoco_config(config_path)
    return JacocoCVMonitor(
        save_dir=save_dir,
        ec_file_name=cfg.get("EcFileName") or cfg.get("ec_file_name"),
        ec_file_path=cfg.get("EcFilePath") or cfg.get("ec_file_path"),
        class_file_path=cfg.get("ClassFilePath") or cfg.get("class_file_path"),
        udid=udid,
    )
