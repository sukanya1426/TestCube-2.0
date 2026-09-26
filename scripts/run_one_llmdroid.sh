#!/usr/bin/env bash
# =============================================================================
#  Run ONE app through LLMDroid ONLY, for 1 hour. One click.
#
#      bash scripts/run_one_llmdroid.sh
#
#  Use this to confirm LLMDroid works before committing to a long batch: it is
#  the half that silently failed on every app when `openai`/`jpype` were absent.
#  For both tools on one app, use scripts/run_one_app.sh instead.
# =============================================================================

# ---- EDIT THESE TWO ---------------------------------------------------------
APP="aegis"              # app to test (stem from experiment/apps.json)
BUDGET_SECONDS=3600      # 1 hour. Use 600 for a quick 10-minute check.
# -----------------------------------------------------------------------------

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1
FAIL=0
ok()   { printf "  \033[32mok\033[0m      %s\n" "$1"; }
bad()  { printf "  \033[31mMISSING\033[0m %s\n" "$1"; FAIL=1; }
step() { printf "\n\033[1m==> %s\033[0m\n" "$1"; }

step "1/5  App and budget"
echo "  app:    $APP  (LLMDroid only)"
echo "  budget: ${BUDGET_SECONDS}s  (~$((BUDGET_SECONDS/60)) minutes)"
python -c "
import io,json,sys
c=json.load(io.open('experiment/apps.json',encoding='utf-8'))
sys.exit(0 if any(a['stem']=='$APP' for a in c['apps']) else 1)" 2>/dev/null || {
  echo "  '$APP' is not in experiment/apps.json. Valid stems:"
  python -c "
import io,json
c=json.load(io.open('experiment/apps.json',encoding='utf-8'))
print('   ', ', '.join(a['stem'] for a in c['apps'] if a['pool']=='selected'))"
  exit 1; }

step "2/5  LLMDroid's python deps"
# LLMDroid imports both at module load, so a missing one makes it exit 1 for
# every app while TestCube keeps working - a batch that yields no comparison.
# 'openai' is only an HTTP client here: it talks to your local Ollama, never to
# OpenAI. 'jpype' is needed because utg_based_policy imports JacocoCVMonitor
# unconditionally, even though we measure with AndroLog.
for M in openai jpype; do
  python -c "import $M" 2>/dev/null && ok "$M" || bad "$M  ->  pip install openai jpype1"
done

step "3/5  Ollama (LLMDroid's model)"
if curl -s -m 5 http://127.0.0.1:11434/api/tags >/dev/null 2>&1; then
  ok "ollama reachable on 127.0.0.1:11434"
  curl -s -m 5 http://127.0.0.1:11434/api/tags | grep -q "qwen2.5vl" \
    && ok "model qwen2.5vl present" \
    || bad "model qwen2.5vl  ->  ollama pull qwen2.5vl:7b"
else
  bad "ollama not running  ->  brew services start ollama   (or: ollama serve)"
fi

step "4/5  Instrumentation toolchain (only needed if $APP is not instrumented yet)"
if [ -f "apks/instrumented/$APP.apk" ]; then
  ok "apks/instrumented/$APP.apk already built"
else
  echo "  $APP is not instrumented yet, so the toolchain is required:"
  [ -f tools/AndroLog/target/androlog-0.1-jar-with-dependencies.jar ] \
    && ok "AndroLog jar" || bad "AndroLog jar  ->  bash scripts/setup_tools.sh"
  [ -d tools/android-platforms ] && [ -n "$(ls -A tools/android-platforms 2>/dev/null)" ] \
    && ok "android-platforms" || bad "android-platforms  ->  bash scripts/setup_tools.sh"
  MAJOR="$(java -version 2>&1 | head -1 | sed -E 's/.*"([0-9]+).*/\1/' 2>/dev/null || echo 0)"
  if [ "${MAJOR:-0}" -lt 21 ] 2>/dev/null; then
    printf "  \033[33mnote\033[0m    Java %s instruments fewer apps than Java 21.\n" "$MAJOR"
  fi
fi

step "5/5  Emulator"
if [ -n "$(adb devices 2>/dev/null | sed -n '2p' | grep -w device)" ]; then
  ok "device: $(adb devices | sed -n '2p' | awk '{print $1}')"
else
  echo "  no device; starting the emulator..."
  EMU="$(command -v emulator || echo "$HOME/Library/Android/sdk/emulator/emulator")"
  if [ ! -x "$EMU" ]; then bad "emulator binary not found (set ANDROID_HOME)"; else
    AVD="$("$EMU" -list-avds 2>/dev/null | head -1)"
    if [ -z "$AVD" ]; then bad "no AVD exists (create one in Android Studio)"; else
      "$EMU" -avd "$AVD" -no-boot-anim >/tmp/emulator-llmdroid.log 2>&1 &
      echo "  booting AVD '$AVD' (up to 3 min)..."
      adb wait-for-device
      for _ in $(seq 1 36); do
        [ "$(adb shell getprop sys.boot_completed 2>/dev/null | tr -d '\r')" = "1" ] && break
        sleep 5
      done
      [ "$(adb shell getprop sys.boot_completed 2>/dev/null | tr -d '\r')" = "1" ] \
        && ok "booted: $(adb devices | sed -n '2p' | awk '{print $1}')" \
        || bad "emulator did not finish booting (see /tmp/emulator-llmdroid.log)"
    fi
  fi
fi

if [ "$FAIL" -ne 0 ]; then
  printf "\n\033[31mNot starting:\033[0m fix the MISSING items above, then re-run.\n"
  exit 1
fi

step "Running LLMDroid on $APP"
echo "  started $(date '+%H:%M:%S'); fetches and instruments first if needed."
echo "  live log: run-llmdroid-$APP.log"
adb logcat -G 64M >/dev/null 2>&1     # AndroLog floods the default buffer

CAFF=""; command -v caffeinate >/dev/null 2>&1 && CAFF="caffeinate -i"
$CAFF python scripts/run_experiment.py \
      --apps "$APP" --no-testcube --budget-seconds "$BUDGET_SECONDS" \
      2>&1 | tee "run-llmdroid-$APP.log"

step "Result"
python - "$APP" <<'PYEOF'
import io, json, os, sys
app = sys.argv[1]
f = "output/experiment/llmdroid/%s/codecoverage.txt" % app
if os.path.isfile(f):
    rows = [l.strip() for l in io.open(f, encoding="utf-8") if "%" in l]
    if rows:
        print("LLMDroid code coverage : %s" % rows[-1])
        print("  %d samples recorded, so LLMDroid ran." % len(rows))
    else:
        print("LLMDroid wrote codecoverage.txt but no samples: it started and died early.")
else:
    print("LLMDroid produced NO output.")
    print("  Reason: run-llmdroid-%s.log, and llmdroid_error in" % app)
    print("  output/experiment/compare/experiment_results.json")
PYEOF
echo
echo "Outputs: output/experiment/llmdroid/$APP/   run-llmdroid-$APP.log"
