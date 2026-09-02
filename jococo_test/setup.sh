#!/usr/bin/env bash
# One-time setup for jococo_test.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
COMPARE_LIB="$ROOT/../compare/LLMDroid/JacocoBridge/lib"
COMPARE_JAR="$ROOT/../compare/LLMDroid/JacocoBridge/JacocoBridge.jar"

mkdir -p "$ROOT/lib" "$ROOT/output"

if [[ ! -f "$ROOT/lib/jacococli.jar" && -d "$COMPARE_LIB" ]]; then
  echo "[*] Copying JaCoCo jars from compare/LLMDroid/JacocoBridge/lib"
  cp "$COMPARE_LIB"/*.jar "$ROOT/lib/"
fi

if [[ ! -f "$ROOT/JacocoBridge/JacocoBridge.jar" && -f "$COMPARE_JAR" ]]; then
  echo "[*] Copying prebuilt JacocoBridge.jar"
  cp "$COMPARE_JAR" "$ROOT/JacocoBridge/JacocoBridge.jar"
fi

for jar in jacococli.jar org.jacoco.core-0.8.8.202204050719.jar jacocoagent.jar; do
  if [[ ! -f "$ROOT/lib/$jar" ]]; then
    echo "[!] Missing $ROOT/lib/$jar" >&2
    echo "    Copy from compare/LLMDroid/JacocoBridge/lib or download JaCoCo 0.8.8." >&2
    exit 1
  fi
done

chmod +x "$ROOT/JacocoBridge/build.sh" "$ROOT/scripts/build_receiver.sh" 2>/dev/null || true

echo "[*] Building CoverageReceiver.dex (needs ANDROID_HOME)..."
if [[ -n "${ANDROID_HOME:-}" ]]; then
  "$ROOT/scripts/build_receiver.sh" || echo "[!] build_receiver.sh failed — install Android SDK build-tools"
else
  echo "[!] ANDROID_HOME not set; skip receiver build until SDK is available."
fi

echo
echo "Setup complete. Next:"
echo "  python jococo_test/scripts/instrument_apk.py apks/your.apk"
echo "  python jococo_test/scripts/collect_coverage.py --config jococo_test/output/your/jacoco.config.json"
