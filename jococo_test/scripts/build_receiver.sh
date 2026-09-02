#!/usr/bin/env bash
# Compile CoverageReceiver + merge JaCoCo runtime into one dex for APK injection.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LIB="$ROOT/lib"
ANDROID_SRC="$ROOT/android/com/testcube/jacoco/CoverageReceiver.java"
OUT_DIR="$ROOT/templates"
OUT_DEX="$OUT_DIR/jacoco_support.dex"

if [[ -z "${ANDROID_HOME:-}" ]]; then
  echo "ANDROID_HOME is required" >&2
  exit 1
fi

API="${ANDROID_API:-34}"
PLATFORM="$ANDROID_HOME/platforms/android-$API/android.jar"
if [[ ! -f "$PLATFORM" ]]; then
  echo "Platform jar not found: $PLATFORM" >&2
  exit 1
fi

BUILD="$(mktemp -d)"
trap 'rm -rf "$BUILD"' EXIT

javac -source 1.8 -target 1.8 \
  -bootclasspath "$PLATFORM" \
  -classpath "$LIB/org.jacoco.agent-0.8.8.202204050719.jar" \
  -d "$BUILD" "$ANDROID_SRC"

D8="$(command -v d8 || true)"
if [[ -z "$D8" ]]; then
  BT="$(ls -d "$ANDROID_HOME"/build-tools/*/d8 2>/dev/null | sort -V | tail -1)"
  D8="$BT"
fi
if [[ ! -x "$D8" ]]; then
  echo "d8 not found under ANDROID_HOME/build-tools" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"
"$D8" --lib "$PLATFORM" --min-api 21 --output "$BUILD/dex" \
  "$LIB/org.jacoco.agent-0.8.8.202204050719.jar" \
  "$BUILD/com/testcube/jacoco/CoverageReceiver.class"

cp "$BUILD/dex/classes.dex" "$OUT_DEX"
echo "Wrote $OUT_DEX"
