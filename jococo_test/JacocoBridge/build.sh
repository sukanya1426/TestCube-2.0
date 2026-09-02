#!/usr/bin/env bash
# Build JacocoBridge.jar from source (same layout as LLMDroid).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LIB="$ROOT/lib"
OUT="$ROOT/JacocoBridge/JacocoBridge.jar"
SRC="$ROOT/JacocoBridge/src/org/jacoco/examples/JacocoBridge.java"

if [[ ! -f "$LIB/org.jacoco.core-0.8.8.202204050719.jar" ]]; then
  echo "Missing JaCoCo jars in $LIB — run setup.sh first." >&2
  exit 1
fi

BUILD_DIR="$(mktemp -d)"
trap 'rm -rf "$BUILD_DIR"' EXIT

javac -cp "$LIB/org.jacoco.core-0.8.8.202204050719.jar" \
  -d "$BUILD_DIR" "$SRC"

jar cf "$OUT" -C "$BUILD_DIR" org
echo "Built $OUT"
