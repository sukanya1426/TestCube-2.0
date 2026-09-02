#!/usr/bin/env python
"""Patch an open-source Android Gradle project for JaCoCo (LLMDroid style).

Adds:
  - jacoco plugin + testCoverageEnabled on debug
  - CoverageReceiver.java under app/src/main/java/com/testcube/jacoco/
  - Receiver registration in the launch Activity (best-effort)

After patching, rebuild the debug APK and copy class files:

    ./gradlew assembleDebug
    cp -r app/build/intermediates/javac/debug/classes jococo_test/output/<app>/classes

Then write jacoco.config.json with EcFilePath = getExternalFilesDir path for that package.
"""

from __future__ import print_function

import argparse
import os
import re
import shutil
import sys

JOCO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECEIVER_SRC = os.path.join(
    JOCO_ROOT, "android", "com", "testcube", "jacoco", "CoverageReceiver.java",
)
BROADCAST_ACTION = "com.llmdroid.jacoco.COLLECT_COVERAGE"


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Patch Android Gradle project for JaCoCo.")
    parser.add_argument("project", help="Root of the Android app project")
    parser.add_argument(
        "--activity",
        default=None,
        help="Launch activity Java file (auto-detect MainActivity if omitted)",
    )
    return parser.parse_args(argv)


def find_app_gradle(root):
    for candidate in (
        os.path.join(root, "app", "build.gradle"),
        os.path.join(root, "app", "build.gradle.kts"),
    ):
        if os.path.isfile(candidate):
            return candidate
    return None


def patch_gradle(path):
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    changed = False
    if "apply plugin: 'jacoco'" not in text and 'id("jacoco")' not in text:
        text = "apply plugin: 'jacoco'\n\njacoco {\n    toolVersion = \"0.8.8\"\n}\n\n" + text
        changed = True
    if "testCoverageEnabled" not in text:
        text = re.sub(
            r"(buildTypes\s*\{\s*debug\s*\{)",
            r"\1\n            testCoverageEnabled true",
            text,
            count=1,
        )
        changed = True
    if changed:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
    return changed


def find_main_activity(root):
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            if name.endswith("MainActivity.java") or name.endswith("MainActivity.kt"):
                return os.path.join(dirpath, name)
    return None


def patch_activity(path):
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    if "CoverageReceiver" in text:
        return False

    imports = (
        "import android.content.IntentFilter;\n"
        "import com.testcube.jacoco.CoverageReceiver;\n"
    )
    if "import com.testcube.jacoco.CoverageReceiver" not in text:
        if "package " in text:
            text = re.sub(
                r"(package [^\n]+\n)",
                r"\1\n" + imports,
                text,
                count=1,
            )

    field = "    private CoverageReceiver coverageReceiver;\n"
    if "coverageReceiver" not in text:
        text = re.sub(
            r"(public class \w+[^{]+\{)",
            r"\1\n" + field,
            text,
            count=1,
        )

    on_create_hook = (
        "        IntentFilter coverageFilter = new IntentFilter(\"%s\");\n"
        "        coverageReceiver = new CoverageReceiver();\n"
        "        registerReceiver(coverageReceiver, coverageFilter);\n"
    ) % BROADCAST_ACTION

    if "registerReceiver(coverageReceiver" not in text:
        text = re.sub(
            r"(super\.onCreate\([^)]*\);\s*)",
            r"\1\n" + on_create_hook,
            text,
            count=1,
        )

    destroy_hook = (
        "        if (coverageReceiver != null) {\n"
        "            unregisterReceiver(coverageReceiver);\n"
        "            coverageReceiver = null;\n"
        "        }\n"
    )
    if "unregisterReceiver(coverageReceiver" not in text:
        if "onDestroy" in text:
            text = re.sub(
                r"(super\.onDestroy\(\);\s*)",
                r"\1\n" + destroy_hook,
                text,
                count=1,
            )
        else:
            text += (
                "\n    @Override\n    protected void onDestroy() {\n"
                + destroy_hook
                + "        super.onDestroy();\n    }\n"
            )

    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return True


def main(argv=None):
    args = parse_args(argv)
    project = os.path.abspath(args.project)
    gradle = find_app_gradle(project)
    if not gradle:
        sys.stderr.write("Could not find app/build.gradle under %s\n" % project)
        return 2

    java_root = os.path.join(project, "app", "src", "main", "java", "com", "testcube", "jacoco")
    os.makedirs(java_root, exist_ok=True)
    shutil.copy2(RECEIVER_SRC, os.path.join(java_root, "CoverageReceiver.java"))

    patch_gradle(gradle)
    activity = args.activity or find_main_activity(os.path.join(project, "app", "src"))
    if activity:
        patch_activity(activity)
        print("[✓] Patched activity: %s" % activity)
    else:
        print("[!] Launch activity not found — register CoverageReceiver manually.")

    print("[✓] Gradle + CoverageReceiver patched under %s" % project)
    print("    Rebuild: ./gradlew assembleDebug")
    print("    See jococo_test/README.md for config.json fields.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
