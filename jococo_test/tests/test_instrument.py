"""Basic tests for jococo_test helpers (no device required)."""

import json
import os
import sys
import tempfile
import unittest


class InstrumentManifestTests(unittest.TestCase):
    def test_patch_manifest_adds_receiver(self):
        scripts = os.path.join(os.path.dirname(__file__), "..", "scripts")
        sys.path.insert(0, os.path.abspath(scripts))
        from instrument_apk import patch_manifest, RECEIVER_CLASS

        with tempfile.NamedTemporaryFile("w", suffix=".xml", delete=False) as handle:
            handle.write(
                '<?xml version="1.0"?>\n<manifest><application>\n'
                '    <activity android:name=".Main"/>\n'
                '</application></manifest>\n'
            )
            path = handle.name
        try:
            patch_manifest(path)
            text = open(path, encoding="utf-8").read()
            self.assertIn(RECEIVER_CLASS, text)
            self.assertIn("com.llmdroid.jacoco.COLLECT_COVERAGE", text)
        finally:
            os.remove(path)


class ConfigTests(unittest.TestCase):
    def test_write_config_roundtrip(self):
        scripts = os.path.join(os.path.dirname(__file__), "..", "scripts")
        sys.path.insert(0, os.path.abspath(scripts))
        from instrument_apk import write_config

        with tempfile.TemporaryDirectory() as tmp:
            path = write_config(tmp, "com.example.app", "test.ec", os.path.join(tmp, "classes"))
            with open(path, encoding="utf-8") as handle:
                cfg = json.load(handle)
            self.assertEqual(cfg["package"], "com.example.app")
            self.assertEqual(cfg["EcFileName"], "test.ec")
            self.assertIn("ClassFilePath", cfg)


if __name__ == "__main__":
    unittest.main()
