#!/usr/bin/env python
"""Instrument an APK with AndroLog so runtime code coverage can be measured.

Both TestCube and LLMDroid read coverage from the same AndroLog probes, so the
same instrumented APK must be used for both sides of a comparison — otherwise
the denominators differ and the numbers are not comparable.

    python scripts/instrument_apk.py apks/newpipe.apk --tag PIPE_SUPER_LOG

Prints the log tag and total method count, which are the two values LLMDroid
needs in its config.json (Tag / TotalMethod).
"""

import argparse
import os
import struct
import subprocess
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from droidbot.coverage.androlog_monitor import total_methods_from_apk

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_JAR = os.path.join(
    REPO, "tools", "AndroLog", "target", "androlog-0.1-jar-with-dependencies.jar"
)
DEFAULT_PLATFORMS = os.path.join(REPO, "tools", "android-platforms")


# --- minSdk patching ---------------------------------------------------
# Soot refuses to split dex files for pre-Lollipop targets ("Dex file overflow.
# Splitting not support for pre Lollipop (Api 22)"), so an app declaring
# minSdk < 21 cannot be instrumented even though it runs fine on a modern
# device. Raising the floor only affects which devices would accept the APK;
# it changes no application code, and the instrumented APK is for measurement
# on an emulator, never for distribution.

INT_DEC = 0x10000008
ANDROID_NS = 130
ATTR_LEN = 20
MIN_SDK_FLOOR = 21


def _find_uses_sdk(raw):
    """Offset of the minSdkVersion value field in a binary AndroidManifest.

    minSdk and targetSdk are the two *adjacent* android-namespace INT_DEC
    attributes of <uses-sdk>. Matching that pair is what makes this reliable —
    picking by value alone hits unrelated integer attributes.
    """
    candidates = []
    for i in range(0, len(raw) - ATTR_LEN - 8):
        typ, data = struct.unpack_from("<II", raw, i)
        if typ != INT_DEC or not (1 <= data <= 40):
            continue
        ns, name, rawv = struct.unpack_from("<III", raw, i - 12)
        if ns != ANDROID_NS or rawv != 0xFFFFFFFF:
            continue
        ntyp, ndata = struct.unpack_from("<II", raw, i + ATTR_LEN)
        nns, nname, nrawv = struct.unpack_from("<III", raw, i + ATTR_LEN - 12)
        if ntyp != INT_DEC or nns != ANDROID_NS or nrawv != 0xFFFFFFFF or ndata < data:
            continue
        candidates.append((i + 4, data, ndata, name, nname))
    if not candidates:
        return None
    if len(candidates) > 1:
        # Ambiguous: prefer the pair whose two name indices differ by 4, the
        # spacing of minSdkVersion/targetSdkVersion in the resource map.
        exact = [c for c in candidates if c[4] - c[3] == 4]
        if len(exact) == 1:
            candidates = exact
        else:
            print("[!] %d <uses-sdk> candidates; refusing to guess" % len(candidates))
            return None
    off, current, target, _n, _nn = candidates[0]
    return off, current, target


def bump_min_sdk(src, dst, new_min=MIN_SDK_FLOOR):
    """Rewrite minSdkVersion. Returns True when a new APK was written."""
    with zipfile.ZipFile(src) as archive:
        raw = bytearray(archive.read("AndroidManifest.xml"))
    found = _find_uses_sdk(raw)
    if not found:
        print("[!] could not locate <uses-sdk> minSdkVersion; leaving APK as is")
        return False
    off, current, target = found
    if current >= new_min:
        return False
    struct.pack_into("<I", raw, off, new_min)
    print("[*] minSdk %d -> %d (targetSdk %d untouched)" % (current, new_min, target))
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "AndroidManifest.xml":
                data = bytes(raw)
            zout.writestr(item, data)
    return True


def default_tag(apk_path):
    stem = os.path.splitext(os.path.basename(apk_path))[0]
    return "%s_SUPER_LOG" % stem.upper().replace("-", "_")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="AndroLog-instrument an APK.")
    parser.add_argument("apk", help="Path to the original (uninstrumented) APK")
    parser.add_argument("--tag", default=None, help="Logcat tag (default: <STEM>_SUPER_LOG)")
    parser.add_argument("--out", default=None, help="Output dir (default: apks/instrumented)")
    parser.add_argument("--jar", default=DEFAULT_JAR, help="AndroLog jar")
    parser.add_argument("--platforms", default=DEFAULT_PLATFORMS, help="Android platforms dir")
    parser.add_argument("--heap", default="8g", help="JVM heap for Soot (default: 8g)")
    parser.add_argument(
        "--no-bump-min-sdk", dest="bump_min_sdk", action="store_false",
        help="Do not raise minSdk to 21 before instrumenting (Soot needs >= 21).",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    tag = args.tag or default_tag(args.apk)
    out_dir = args.out or os.path.join(REPO, "apks", "instrumented")

    for path, what in ((args.jar, "AndroLog jar"), (args.platforms, "platforms dir")):
        if not os.path.exists(path):
            sys.stderr.write(
                "%s not found: %s\nSee docs/CODE_COVERAGE.md for the one-time setup.\n"
                % (what, path)
            )
            return 2

    os.makedirs(out_dir, exist_ok=True)

    source_apk = args.apk
    staged = None
    if args.bump_min_sdk:
        staged = os.path.join(out_dir, ".minsdk-" + os.path.basename(args.apk))
        if bump_min_sdk(args.apk, staged):
            source_apk = staged
        else:
            staged = None

    command = [
        "java", "-Xmx%s" % args.heap, "-jar", args.jar,
        "-p", args.platforms,
        "-l", tag,
        "-o", out_dir,
        "-a", source_apk,
        "-c", "-m", "-cp",
    ]
    print("[*] %s" % " ".join(command))
    result = subprocess.run(command)
    if result.returncode != 0:
        sys.stderr.write("AndroLog failed (exit %d)\n" % result.returncode)
        return result.returncode

    produced = os.path.join(out_dir, os.path.basename(source_apk))
    if not os.path.exists(produced):
        sys.stderr.write("AndroLog reported success but no APK at %s\n" % produced)
        return 1
    if staged:
        # Name the result after the original APK, and drop the staging copy.
        final = os.path.join(out_dir, os.path.basename(args.apk))
        os.replace(produced, final)
        produced = final
        if os.path.exists(staged):
            os.remove(staged)

    total = total_methods_from_apk(produced)
    print("\n[✓] Instrumented APK: %s" % produced)
    print("    Tag:           %s" % tag)
    print("    Total methods: %d" % total)
    print("\nTestCube:")
    print("    droidbot -a %s -o output/<run> --code-coverage androlog \\" % produced)
    print("        --coverage-tag %s" % tag)
    print("\nLLMDroid (config.json):")
    print('    "Tag": "%s", "TotalMethod": %d' % (tag, total))
    print("    ...then run with -code_coverage androlog")
    return 0


if __name__ == "__main__":
    sys.exit(main())
