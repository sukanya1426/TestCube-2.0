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
import shutil
import struct
import tempfile
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


# Binary AXML chunk types and layout. Resolving the attribute by NAME out of the
# string pool is exact; the byte-pattern search below it is only a fallback.
_RES_STRING_POOL = 0x001C0001
_RES_START_TAG = 0x00100102          # type 0x0102 | headerSize 0x0010 << 16
_UTF8_FLAG = 0x00000100
_ATTR_SIZE = 20
_ATTR_DATA_OFF = 16


def _axml_strings(raw):
    """Every string in the manifest's string pool, in index order."""
    offset = 8                                   # past the file header
    while offset + 8 <= len(raw):
        chunk_type, chunk_size = struct.unpack_from("<II", raw, offset)
        if chunk_type == _RES_STRING_POOL:
            count, _styles, flags, strings_start = struct.unpack_from("<IIII", raw, offset + 8)
            offsets_at = offset + 28
            data_at = offset + strings_start
            utf8 = bool(flags & _UTF8_FLAG)
            out = []
            for i in range(count):
                try:
                    rel, = struct.unpack_from("<I", raw, offsets_at + 4 * i)
                    at = data_at + rel
                    if utf8:
                        n = raw[at + 1]
                        if n & 0x80:             # two-byte length
                            n = ((n & 0x7F) << 8) | raw[at + 2]
                            at += 1
                        out.append(bytes(raw[at + 2:at + 2 + n]).decode("utf-8", "replace"))
                    else:
                        n, = struct.unpack_from("<H", raw, at)
                        if n & 0x8000:
                            n = ((n & 0x7FFF) << 16) | struct.unpack_from("<H", raw, at + 2)[0]
                            at += 2
                        out.append(bytes(raw[at + 2:at + 2 + n * 2]).decode("utf-16-le", "replace"))
                except Exception:
                    out.append("")
            return out
        if chunk_size <= 0:
            break
        offset += chunk_size
    return []


def _find_min_sdk_by_name(raw):
    """(offset, minSdk, targetSdk) found by resolving attribute names.

    Walks the START_TAG chunks and matches the attribute literally called
    minSdkVersion, rather than guessing from the shape of the bytes. Manifests
    order and space their attributes freely, which is what defeats a pattern
    match: markor declares minSdk 18 and was skipped entirely.
    """
    strings = _axml_strings(raw)
    if not strings:
        return None
    offset, found = 8, {}
    while offset + 8 <= len(raw):
        chunk_type, chunk_size = struct.unpack_from("<II", raw, offset)
        if chunk_type == _RES_START_TAG:
            attr_start, _attr_size, attr_count = struct.unpack_from("<HHH", raw, offset + 24)
            base = offset + 16 + attr_start
            for i in range(attr_count):
                at = base + i * _ATTR_SIZE
                if at + _ATTR_SIZE > len(raw):
                    break
                _ns, name_idx = struct.unpack_from("<II", raw, at)
                name = strings[name_idx] if 0 <= name_idx < len(strings) else ""
                if name in ("minSdkVersion", "targetSdkVersion"):
                    data_at = at + _ATTR_DATA_OFF
                    value, = struct.unpack_from("<I", raw, data_at)
                    found.setdefault(name, (data_at, value))
        if chunk_size <= 0:
            break
        offset += chunk_size
    if "minSdkVersion" not in found:
        return None
    data_at, value = found["minSdkVersion"]
    target = found.get("targetSdkVersion", (0, 0))[1]
    return data_at, value, target


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
    found = _find_min_sdk_by_name(raw)
    if not found:
        # Fall back to the old byte-pattern search before giving up.
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
    staged_dir = None
    if args.bump_min_sdk:
        # NOT in out_dir: AndroLog writes its result to <out_dir>/<basename of
        # input>, so staging there makes the output path equal the input path.
        # It truncates the file it is about to read and dies with "zip file is
        # empty", which is why raising minSdk never actually worked.
        staged_dir = tempfile.mkdtemp(prefix="testcube-minsdk-")
        staged = os.path.join(staged_dir, os.path.basename(args.apk))
        if bump_min_sdk(args.apk, staged):
            source_apk = staged
            print("[*] staged patched APK at %s" % staged)
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
        if staged_dir:
            shutil.rmtree(staged_dir, ignore_errors=True)
        return 1
    if staged:
        # Name the result after the original APK, and drop the staging copy.
        final = os.path.join(out_dir, os.path.basename(args.apk))
        if os.path.abspath(produced) != os.path.abspath(final):
            os.replace(produced, final)
        produced = final
    if staged_dir:
        shutil.rmtree(staged_dir, ignore_errors=True)

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
