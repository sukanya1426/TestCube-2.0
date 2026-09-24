#!/usr/bin/env bash
# One-time setup of the instrumentation toolchain.
#
# tools/ is gitignored (the AndroLog jar alone is 26 MB and android-platforms is
# a separate repo), so a fresh clone has neither. Without them EVERY APK fails
# to instrument, which looks like an APK problem and is not.
#
#   bash scripts/setup_tools.sh
#
set -euo pipefail
cd "$(dirname "$0")/.."
REPO="$PWD"
JAR="$REPO/tools/AndroLog/target/androlog-0.1-jar-with-dependencies.jar"
PLATFORMS="$REPO/tools/android-platforms"

step() { printf "\n\033[1m==> %s\033[0m\n" "$1"; }
have() { command -v "$1" >/dev/null 2>&1; }

step "Checking prerequisites"
missing=0
for c in git java mvn; do
  if have "$c"; then echo "  ok      $c ($($c --version 2>&1 | head -1))"
  else echo "  MISSING $c"; missing=1; fi
done
if [ "$missing" = 1 ]; then
  echo
  echo "Install what is missing first:"
  echo "  brew install maven          # brings a JDK if you have none"
  echo "  java -version              # needs 17 or newer"
  exit 1
fi
if [ -z "${ANDROID_HOME:-}" ]; then
  for guess in "$HOME/Library/Android/sdk" "$HOME/Android/Sdk"; do
    [ -d "$guess" ] && export ANDROID_HOME="$guess" && break
  done
fi
if [ -z "${ANDROID_HOME:-}" ] || [ ! -d "$ANDROID_HOME" ]; then
  echo "  MISSING ANDROID_HOME (set it to your Android SDK path)"; exit 1
fi
echo "  ok      ANDROID_HOME=$ANDROID_HOME"

BUILD_TOOLS="$(ls -1d "$ANDROID_HOME"/build-tools/* 2>/dev/null | sort -V | tail -1 || true)"
if [ -z "$BUILD_TOOLS" ]; then
  echo "  MISSING $ANDROID_HOME/build-tools/* (install build-tools via sdkmanager)"; exit 1
fi
echo "  ok      build-tools $(basename "$BUILD_TOOLS")"

step "AndroLog"
if [ -f "$JAR" ]; then
  echo "  already built: $(du -h "$JAR" | cut -f1)"
else
  [ -d "$REPO/tools/AndroLog/.git" ] || \
    git clone --depth 1 https://github.com/JordanSamhi/AndroLog.git "$REPO/tools/AndroLog"
  mkdir -p "$REPO/tools/AndroLog/src/main/resources"
  cat > "$REPO/tools/AndroLog/src/main/resources/config.properties" <<EOF
apksignerPath=$BUILD_TOOLS/apksigner
zipalignPath=$BUILD_TOOLS/zipalign
EOF
  echo "  wrote config.properties pointing at $(basename "$BUILD_TOOLS")"
  echo "  building (a few minutes the first time)..."
  ( cd "$REPO/tools/AndroLog" && mvn -q clean install -DskipTests )
  [ -f "$JAR" ] || { echo "  BUILD FAILED: $JAR was not produced"; exit 1; }
  echo "  built: $(du -h "$JAR" | cut -f1)"
fi

step "Android platforms (Soot needs these stubs)"
if [ -d "$PLATFORMS" ] && [ "$(ls -1 "$PLATFORMS" | wc -l | tr -d ' ')" -gt 0 ]; then
  echo "  already present: $(ls -1 "$PLATFORMS" | wc -l | tr -d ' ') entries"
else
  git clone --depth 1 https://github.com/Sable/android-platforms.git "$PLATFORMS"
  echo "  cloned: $(ls -1 "$PLATFORMS" | wc -l | tr -d ' ') entries"
fi

step "LLMDroid python deps"
python -c "import openai" 2>/dev/null && echo "  ok      openai" || pip install -q openai
python -c "import jpype" 2>/dev/null && echo "  ok      jpype1" || pip install -q jpype1

step "Verifying with a real instrumentation"
TESTAPK="$(ls -1S apks/*.apk 2>/dev/null | tail -1 || true)"
if [ -z "$TESTAPK" ]; then
  echo "  no APK to test with yet; run: python scripts/fetch_apks.py --only fossifyclock"
else
  STEM="$(basename "$TESTAPK" .apk)"
  echo "  instrumenting the smallest APK ($STEM) as a smoke test..."
  if python scripts/instrument_apk.py "$TESTAPK" --tag SETUP_CHECK_LOG >/tmp/setup-check.log 2>&1; then
    grep -E "Total methods" /tmp/setup-check.log | sed 's/^/  /'
    echo "  toolchain works."
  else
    echo "  FAILED. Last lines of /tmp/setup-check.log:"
    tail -5 /tmp/setup-check.log | sed 's/^/    /'
    exit 1
  fi
fi

printf "\n\033[1mSetup complete.\033[0m Next:\n"
echo "  python scripts/check_experiment_setup.py"
echo "  python scripts/run_experiment.py --dry-run --all --usable-only"
