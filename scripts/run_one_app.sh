#!/usr/bin/env bash
# =============================================================================
#  Run ONE app through TestCube and LLMDroid, 1 hour each. One click.
#
#      bash scripts/run_one_app.sh
#
#  Everything is checked before anything long starts, so a missing dependency
#  costs seconds instead of two hours.
# =============================================================================

# ---- EDIT THESE TWO ---------------------------------------------------------
APP="aegis"              # app to test (stem from experiment/apps.json)
BUDGET_SECONDS=3600      # per tool, so total run time is about twice this
# -----------------------------------------------------------------------------

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1
REPO="$PWD"
FAIL=0
ok()   { printf "  \033[32mok\033[0m      %s\n" "$1"; }
bad()  { printf "  \033[31mMISSING\033[0m %s\n" "$1"; FAIL=1; }
step() { printf "\n\033[1m==> %s\033[0m\n" "$1"; }

step "1/6  App and budget"
echo "  app:    $APP"
echo "  budget: ${BUDGET_SECONDS}s per tool (~$((BUDGET_SECONDS*2/3600))h total)"
if ! python -c "
import io,json,sys
c=json.load(io.open('experiment/apps.json',encoding='utf-8'))
sys.exit(0 if any(a['stem']=='$APP' for a in c['apps']) else 1)" 2>/dev/null; then
  echo "  '$APP' is not in experiment/apps.json. Valid stems:"
  python -c "
import io,json
c=json.load(io.open('experiment/apps.json',encoding='utf-8'))
print('   ', ', '.join(a['stem'] for a in c['apps'] if a['pool']=='selected'))"
  exit 1
fi

step "2/6  Java"
if command -v java >/dev/null 2>&1; then
  V="$(java -version 2>&1 | head -1)"
  MAJOR="$(java -version 2>&1 | head -1 | sed -E 's/.*"([0-9]+).*/\1/')"
  ok "$V"
  if [ "${MAJOR:-0}" -lt 21 ] 2>/dev/null; then
    printf "  \033[33mnote\033[0m    Java %s: Soot instruments FEWER apps than Java 21.\n" "$MAJOR"
    printf "          money and vlc fail on 17 but work on 21. If '%s' fails to\n" "$APP"
    printf "          instrument, try:  brew install openjdk@21 && export JAVA_HOME=\$(/usr/libexec/java_home -v 21)\n"
  fi
else
  bad "java (need 17+, 21 recommended)"
fi

step "3/6  Instrumentation toolchain"
[ -f tools/AndroLog/target/androlog-0.1-jar-with-dependencies.jar ] \
  && ok "AndroLog jar" || bad "AndroLog jar  -> run: bash scripts/setup_tools.sh"
[ -d tools/android-platforms ] && [ -n "$(ls -A tools/android-platforms 2>/dev/null)" ] \
  && ok "android-platforms" || bad "android-platforms  -> run: bash scripts/setup_tools.sh"

step "4/6  Python deps for LLMDroid"
for M in openai jpype; do
  python -c "import $M" 2>/dev/null && ok "$M" || bad "$M  -> run: pip install openai jpype1"
done
# 'openai' is only an HTTP client here; it talks to your local Ollama, not to OpenAI.

step "5/6  Ollama (both tools use the local model)"
if curl -s -m 5 http://127.0.0.1:11434/api/tags >/dev/null 2>&1; then
  ok "ollama reachable on 127.0.0.1:11434"
  if curl -s -m 5 http://127.0.0.1:11434/api/tags | grep -q "qwen2.5vl"; then
    ok "model qwen2.5vl present"
  else
    bad "model qwen2.5vl  -> run: ollama pull qwen2.5vl:7b"
  fi
else
  bad "ollama not running  -> run: brew services start ollama   (or: ollama serve)"
fi

step "6/6  Emulator"
if [ -n "$(adb devices 2>/dev/null | sed -n '2p' | grep -w device)" ]; then
  ok "device: $(adb devices | sed -n '2p' | awk '{print $1}')"
else
  echo "  no device; starting the emulator..."
  EMU="$(command -v emulator || echo "$HOME/Library/Android/sdk/emulator/emulator")"
  if [ ! -x "$EMU" ]; then bad "emulator binary not found (set ANDROID_HOME)"; else
    AVD="$("$EMU" -list-avds 2>/dev/null | head -1)"
    if [ -z "$AVD" ]; then bad "no AVD exists (create one in Android Studio)"; else
      "$EMU" -avd "$AVD" -no-boot-anim >/tmp/emulator-oneapp.log 2>&1 &
      echo "  booting AVD '$AVD' (up to 3 min)..."
      adb wait-for-device
      for _ in $(seq 1 36); do
        [ "$(adb shell getprop sys.boot_completed 2>/dev/null | tr -d '\r')" = "1" ] && break
        sleep 5
      done
      if [ "$(adb shell getprop sys.boot_completed 2>/dev/null | tr -d '\r')" = "1" ]; then
        ok "booted: $(adb devices | sed -n '2p' | awk '{print $1}')"
      else
        bad "emulator did not finish booting (see /tmp/emulator-oneapp.log)"
      fi
    fi
  fi
fi

if [ "$FAIL" -ne 0 ]; then
  printf "\n\033[31mNot starting:\033[0m fix the MISSING items above, then re-run this script.\n"
  exit 1
fi

step "Running $APP  (TestCube, then LLMDroid)"
echo "  started $(date '+%H:%M:%S'); expect about $((BUDGET_SECONDS*2/60)) minutes plus setup."
echo "  live log: run-$APP.log"
adb logcat -G 64M >/dev/null 2>&1        # AndroLog floods the default buffer

CAFF=""; command -v caffeinate >/dev/null 2>&1 && CAFF="caffeinate -i"
$CAFF python scripts/run_experiment.py \
      --apps "$APP" --budget-seconds "$BUDGET_SECONDS" 2>&1 | tee "run-$APP.log"

step "Result"
CMP="output/experiment/compare/$APP/coverage_comparison.md"
if [ -f "$CMP" ]; then cat "$CMP"; else echo "  no comparison written; see run-$APP.log"; fi
echo
python - "$APP" <<'PYEOF'
import io, json, os, sys
app = sys.argv[1]
p = "output/experiment/testcube/%s/code_coverage.json" % app
if os.path.isfile(p):
    d = json.load(io.open(p, encoding="utf-8"))
    print("TestCube code coverage : %.2f%%  (%s/%s methods, %s actions)"
          % (d.get("final_coverage") or 0, d.get("methods_hit"),
             d.get("total_methods"), d.get("total_actions")))
    if not d.get("final_coverage"):
        print("  WARNING: 0% means the app ran but emitted no probes - treat as failed.")
f = "output/experiment/llmdroid/%s/codecoverage.txt" % app
if os.path.isfile(f):
    last = [l for l in io.open(f, encoding="utf-8") if "%" in l][-1:]
    print("LLMDroid code coverage : %s" % (last[0].strip() if last else "no samples"))
else:
    print("LLMDroid code coverage : NO OUTPUT - check run-%s.log for its error" % app)
r = "output/experiment/testcube/%s/feature_coverage/report.json" % app
if os.path.isfile(r):
    d = json.load(io.open(r, encoding="utf-8"))
    print("TestCube feature cov.  : %s%% of %s features"
          % (d.get("coverage_percentage"), d.get("total_features")))
PYEOF
echo
echo "Full outputs:"
echo "  output/experiment/testcube/$APP/   output/experiment/llmdroid/$APP/"
echo "  output/experiment/compare/$APP/    run-$APP.log"
