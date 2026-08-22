"""Path layout: apks/, feature/<stem>/, scripts/. No device required."""

import os
import tempfile
import unittest
from types import SimpleNamespace

from droidbot.feature_tester.specs import (
    apk_stem,
    apply_run_paths,
    discover_credentials,
    discover_readme,
    extra_spec_texts,
    resolve_apk_path,
)


def _touch(path, body="x"):
    parent = os.path.dirname(path)
    if parent and not os.path.isdir(parent):
        os.makedirs(parent)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(body)


class LayoutPathTests(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        _touch(os.path.join(self.root, "apks", "spotube.apk"), "apk")
        _touch(os.path.join(self.root, "apks", "money.apk"), "apk")
        _touch(
            os.path.join(self.root, "feature", "spotube", "README.md"),
            "# Spotube\n\nPlay music.",
        )
        _touch(
            os.path.join(self.root, "feature", "spotube", "credential.txt"),
            "email: a@b.c\nsearch_query: Taylor Swift\n",
        )
        _touch(
            os.path.join(self.root, "feature", "spotube", "notes.txt"),
            "Extra GUI note for spotube only.",
        )
        _touch(
            os.path.join(self.root, "feature", "money", "README.md"),
            "# Money\n\nTrack expenses.",
        )
        _touch(
            os.path.join(self.root, "feature", "money", "credential.txt"),
            "database_name: testcube.mmb\n",
        )
        _touch(
            os.path.join(self.root, "feature", "money", "notes.txt"),
            "Money-only note that must not leak into Spotube.",
        )

    def test_apk_stem_aliases(self):
        self.assertEqual(apk_stem("apks/spotube.apk"), "spotube")
        self.assertEqual(apk_stem("final.apk"), "spotube")
        self.assertEqual(apk_stem("Spotube-android-all-arch.apk"), "spotube")
        self.assertEqual(apk_stem("money.apk"), "money")

    def test_resolve_apk_from_stem(self):
        found = resolve_apk_path("spotube", cwd=self.root)
        self.assertTrue(found.endswith(os.path.join("apks", "spotube.apk")))
        self.assertTrue(os.path.isfile(found))

    def test_resolve_apk_alias_final(self):
        found = resolve_apk_path("final.apk", cwd=self.root)
        self.assertTrue(found.endswith(os.path.join("apks", "spotube.apk")))

    def test_discover_readme_per_app(self):
        spotube = discover_readme("apks/spotube.apk", cwd=self.root)
        money = discover_readme("apks/money.apk", cwd=self.root)
        self.assertTrue(spotube.endswith(os.path.join("feature", "spotube", "README.md")))
        self.assertTrue(money.endswith(os.path.join("feature", "money", "README.md")))
        self.assertNotEqual(spotube, money)

    def test_discover_credentials_per_app(self):
        spotube = discover_credentials("apks/spotube.apk", cwd=self.root)
        money = discover_credentials("apks/money.apk", cwd=self.root)
        self.assertTrue(spotube.endswith(os.path.join("feature", "spotube", "credential.txt")))
        self.assertTrue(money.endswith(os.path.join("feature", "money", "credential.txt")))

    def test_extra_notes_stay_in_app_folder(self):
        readme = discover_readme("spotube", cwd=self.root)
        extras = extra_spec_texts(readme_path=readme, cwd=self.root)
        bodies = " ".join(body for _, body in extras)
        self.assertIn("spotube only", bodies)
        self.assertNotIn("Money-only", bodies)

    def test_empty_readme_is_skipped(self):
        _touch(os.path.join(self.root, "apks", "newpipe.apk"), "apk")
        _touch(os.path.join(self.root, "feature", "newpipe", "README.md"), "")
        self.assertIsNone(discover_readme("newpipe", cwd=self.root))

    def test_apply_run_paths(self):
        opts = SimpleNamespace(
            apk_path="spotube",
            readme_path=None,
            credential_path=None,
            output_dir=None,
        )
        self.assertTrue(apply_run_paths(opts, cwd=self.root))
        self.assertTrue(os.path.isfile(opts.apk_path))
        self.assertTrue(opts.readme_path.endswith("README.md"))
        self.assertTrue(opts.credential_path.endswith("credential.txt"))
        self.assertEqual(opts.output_dir, os.path.join("output", "spotube"))

    def test_missing_apk(self):
        opts = SimpleNamespace(apk_path="does-not-exist", readme_path=None, credential_path=None, output_dir=None)
        self.assertFalse(apply_run_paths(opts, cwd=self.root))


if __name__ == "__main__":
    unittest.main()
