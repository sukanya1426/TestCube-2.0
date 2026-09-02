#!/usr/bin/env python
"""Instrument any Android APK with JaCoCo (LLMDroid-compatible workflow).

Pipeline (APK mode):
  1. Decode APK with apktool (-s keeps binary dex)
  2. For each classes*.dex: dex2jar → jacococli instrument → jar2dex
  3. Merge a support dex (JaCoCo runtime + CoverageReceiver)
  4. Register CoverageReceiver in AndroidManifest.xml
  5. Rebuild, zipalign, sign

Outputs under jococo_test/output/<stem>/:
  - instrumented.apk
  - classes/          instrumented .class tree for JacocoBridge analysis
  - jacoco.config.json  EcFilePath, ClassFilePath, ec file name, package

Requirements:
  - Java, apktool, d2j-dex2jar + d2j-jar2dex (dex-tools)
  - ANDROID_HOME with build-tools (zipalign, apksigner, d8)
  - jococo_test/setup.sh run once

Open-source alternative:
  python jococo_test/scripts/patch_gradle.py /path/to/android/project
"""

from __future__ import print_function

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

JOCO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(JOCO_ROOT)
LIB = os.path.join(JOCO_ROOT, "lib")
JACOCOCLI = os.path.join(LIB, "jacococli.jar")
SUPPORT_DEX = os.path.join(JOCO_ROOT, "templates", "jacoco_support.dex")
RECEIVER_CLASS = "com.testcube.jacoco.CoverageReceiver"
BROADCAST_ACTION = "com.llmdroid.jacoco.COLLECT_COVERAGE"


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="JaCoCo-instrument an Android APK.")
    parser.add_argument("apk", help="Path to the original APK")
    parser.add_argument(
        "--out",
        default=None,
        help="Output directory (default: jococo_test/output/<stem>)",
    )
    parser.add_argument(
        "--ec-name",
        default=None,
        help="Runtime .ec filename (default: <package>_coverage.ec)",
    )
    parser.add_argument(
        "--keystore",
        default=os.path.join(JOCO_ROOT, "templates", "debug.keystore"),
        help="Keystore for signing (auto-created debug keystore if missing)",
    )
    parser.add_argument(
        "--skip-sign",
        action="store_true",
        help="Skip zipalign/apksigner (unsigned APK)",
    )
    parser.add_argument(
        "--keep-work",
        action="store_true",
        help="Keep intermediate work directory",
    )
    return parser.parse_args(argv)


def run(cmd, **kwargs):
    print("[*] %s" % " ".join(cmd))
    return subprocess.run(cmd, **kwargs)


def which(name):
    path = shutil.which(name)
    if path:
        return path
    for candidate in (name + ".sh", name + ".bat"):
        found = shutil.which(candidate)
        if found:
            return found
    return None


def require_tools():
    missing = []
    for tool in ("java", "apktool", "d2j-dex2jar", "d2j-jar2dex"):
        if not which(tool):
            missing.append(tool)
    if not os.path.isfile(JACOCOCLI):
        missing.append(JACOCOCLI)
    if not os.path.isfile(SUPPORT_DEX):
        missing.append(
            "%s (run: bash jococo_test/setup.sh with ANDROID_HOME set)" % SUPPORT_DEX
        )
    android_home = os.environ.get("ANDROID_HOME") or os.environ.get("ANDROID_SDK_ROOT")
    if not android_home:
        missing.append("ANDROID_HOME")
    if missing:
        sys.stderr.write(
            "Missing requirements:\n  - %s\n\n"
            "Install dex-tools (dex2jar), apktool, Android SDK, then:\n"
            "  bash jococo_test/setup.sh\n" % "\n  - ".join(missing)
        )
        return None
    bt = sorted(
        glob_build_tools(android_home),
        key=_version_key,
    )
    if not bt:
        missing.append("Android build-tools (zipalign, apksigner)")
        sys.stderr.write("Missing build-tools under %s\n" % android_home)
        return None
    return android_home, bt[-1]


def glob_build_tools(android_home):
    root = os.path.join(android_home, "build-tools")
    if not os.path.isdir(root):
        return []
    return [os.path.join(root, name) for name in os.listdir(root)]


def _version_key(path):
    name = os.path.basename(path)
    parts = []
    for chunk in re.split(r"[.\-]", name):
        try:
            parts.append(int(chunk))
        except ValueError:
            parts.append(0)
    return parts


def read_package(apk_path):
    try:
        from androguard.core.apk import APK
        apk = APK(apk_path)
        return apk.get_package()
    except Exception:
        pass
    with zipfile.ZipFile(apk_path) as archive:
        if "AndroidManifest.xml" in archive.namelist():
            pass
    return os.path.splitext(os.path.basename(apk_path))[0]


def ensure_debug_keystore(path):
    if os.path.isfile(path):
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    run([
        "keytool", "-genkeypair", "-v",
        "-keystore", path,
        "-storepass", "android",
        "-alias", "androiddebugkey",
        "-keypass", "android",
        "-keyalg", "RSA", "-keysize", "2048", "-validity", "10000",
        "-dname", "CN=TestCube Debug,O=TestCube,C=US",
    ], check=True)


def extract_classes_from_jar(jar_path, dest_dir):
    with zipfile.ZipFile(jar_path) as archive:
        for name in archive.namelist():
            if not name.endswith(".class"):
                continue
            target = os.path.join(dest_dir, name)
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with archive.open(name) as src, open(target, "wb") as dst:
                dst.write(src.read())


def instrument_dex(dex_path, work_dir, classes_root):
    base = os.path.splitext(os.path.basename(dex_path))[0]
    jar_in = os.path.join(work_dir, base + ".jar")
    jar_out = os.path.join(work_dir, base + "-instrumented.jar")
    dex_out = os.path.join(work_dir, base + "-instrumented.dex")

    dex2jar = which("d2j-dex2jar")
    jar2dex = which("d2j-jar2dex")
    result = run([dex2jar, dex_path, "-o", jar_in, "-f"], check=False)
    if result.returncode != 0:
        raise RuntimeError("dex2jar failed for %s" % dex_path)

    result = run([
        "java", "-jar", JACOCOCLI, "instrument", jar_in, "--dest", jar_out,
    ], check=False)
    if result.returncode != 0:
        raise RuntimeError("jacococli instrument failed for %s" % dex_path)

    extract_classes_from_jar(jar_out, classes_root)

    result = run([jar2dex, jar_out, "-o", dex_out, "-f"], check=False)
    if result.returncode != 0:
        raise RuntimeError("jar2dex failed for %s" % dex_path)
    return dex_out


def list_dex_files(directory):
    dex_files = []
    for name in sorted(os.listdir(directory)):
        if re.match(r"classes(\d*)\.dex$", name):
            dex_files.append(os.path.join(directory, name))
    return dex_files


def next_dex_name(existing):
    indices = [1]
    for name in existing:
        match = re.match(r"classes(\d+)\.dex$", name)
        if match:
            indices.append(int(match.group(1)))
        elif name == "classes.dex":
            indices.append(1)
    return "classes%d.dex" % (max(indices) + 1)


def patch_manifest(manifest_path):
    with open(manifest_path, "r", encoding="utf-8") as handle:
        text = handle.read()

    if RECEIVER_CLASS in text:
        return

    receiver_block = (
        '    <receiver android:name="%s" android:exported="true">\n'
        '        <intent-filter>\n'
        '            <action android:name="%s"/>\n'
        '        </intent-filter>\n'
        '    </receiver>\n' % (RECEIVER_CLASS, BROADCAST_ACTION)
    )

    if "</application>" in text:
        text = text.replace("</application>", receiver_block + "    </application>", 1)
    else:
        raise RuntimeError("Could not find </application> in %s" % manifest_path)

    with open(manifest_path, "w", encoding="utf-8") as handle:
        handle.write(text)


def write_config(out_dir, package, ec_name, classes_dir):
    ec_path = "/storage/emulated/0/Android/data/%s/files" % package
    config = {
        "AppName": os.path.basename(out_dir),
        "package": package,
        "EcFilePath": ec_path,
        "EcFileName": ec_name,
        "ClassFilePath": os.path.abspath(classes_dir),
        "BroadcastAction": BROADCAST_ACTION,
        "instrumented_apk": os.path.join(out_dir, "instrumented.apk"),
        "notes": (
            "EcFilePath matches getExternalFilesDir(null) on the device. "
            "ClassFilePath is the instrumented .class tree on the host."
        ),
    }
    path = os.path.join(out_dir, "jacoco.config.json")
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(config, handle, indent=2)
        handle.write("\n")
    return path


def main(argv=None):
    args = parse_args(argv)
    tools = require_tools()
    if not tools:
        return 2
    android_home, build_tools = tools

    apk_path = os.path.abspath(args.apk)
    if not os.path.isfile(apk_path):
        sys.stderr.write("APK not found: %s\n" % apk_path)
        return 2

    stem = os.path.splitext(os.path.basename(apk_path))[0]
    out_dir = os.path.abspath(args.out or os.path.join(JOCO_ROOT, "output", stem))
    classes_dir = os.path.join(out_dir, "classes")
    os.makedirs(classes_dir, exist_ok=True)

    package = read_package(apk_path)
    ec_name = args.ec_name or ("%s_coverage.ec" % package.replace(".", "_"))

    work = tempfile.mkdtemp(prefix="jacoco-", dir=out_dir)
    decoded = os.path.join(work, "decoded")
    try:
        result = run(["apktool", "d", "-s", "-f", apk_path, "-o", decoded], check=False)
        if result.returncode != 0:
            sys.stderr.write("apktool decode failed\n")
            return 1

        dex_files = list_dex_files(decoded)
        if not dex_files:
            sys.stderr.write("No classes*.dex found in decoded APK\n")
            return 1

        for dex_path in dex_files:
            inst_dex = instrument_dex(dex_path, work, classes_dir)
            shutil.copy2(inst_dex, dex_path)

        existing = os.listdir(decoded)
        support_name = next_dex_name(existing)
        shutil.copy2(SUPPORT_DEX, os.path.join(decoded, support_name))

        manifest = os.path.join(decoded, "AndroidManifest.xml")
        if not os.path.isfile(manifest):
            sys.stderr.write("AndroidManifest.xml missing after apktool decode\n")
            return 1
        patch_manifest(manifest)

        unsigned = os.path.join(work, "unsigned.apk")
        result = run(["apktool", "b", decoded, "-o", unsigned], check=False)
        if result.returncode != 0:
            sys.stderr.write("apktool build failed\n")
            return 1

        final_apk = os.path.join(out_dir, "instrumented.apk")
        if args.skip_sign:
            shutil.copy2(unsigned, final_apk)
        else:
            ensure_debug_keystore(args.keystore)
            aligned = os.path.join(work, "aligned.apk")
            zipalign = os.path.join(build_tools, "zipalign")
            apksigner = os.path.join(build_tools, "apksigner")
            run([zipalign, "-f", "4", unsigned, aligned], check=True)
            run([
                apksigner, "sign",
                "--ks", args.keystore,
                "--ks-pass", "pass:android",
                "--key-pass", "pass:android",
                "--ks-key-alias", "androiddebugkey",
                "--out", final_apk,
                aligned,
            ], check=True)

        config_path = write_config(out_dir, package, ec_name, classes_dir)

        print("\n[✓] Instrumented APK: %s" % final_apk)
        print("    Package:        %s" % package)
        print("    Class files:    %s" % classes_dir)
        print("    EC on device:   %s/%s" % (
            "/storage/emulated/0/Android/data/%s/files" % package, ec_name,
        ))
        print("    Config:         %s" % config_path)
        print("\nInstall & test:")
        print("    adb install -r -g %s" % final_apk)
        print("    adb shell am broadcast -a %s --es coverageFile %s" % (
            BROADCAST_ACTION, ec_name,
        ))
        print("\nCollect coverage:")
        print("    python jococo_test/scripts/collect_coverage.py --config %s" % config_path)
        return 0
    finally:
        if args.keep_work:
            print("[*] Work dir kept: %s" % work)
        else:
            shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
