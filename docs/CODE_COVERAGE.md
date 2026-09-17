# Code coverage

TestCube measures **method coverage** and **activity coverage** at runtime using
AndroLog probes — the same mechanism LLMDroid uses, so the two are comparable.

## One-time setup

```bash
brew install maven                       # JDK 17+ also required
git clone https://github.com/JordanSamhi/AndroLog.git tools/AndroLog
cat > tools/AndroLog/src/main/resources/config.properties <<EOF
apksignerPath=$ANDROID_HOME/build-tools/36.0.0/apksigner
zipalignPath=$ANDROID_HOME/build-tools/36.0.0/zipalign
EOF
(cd tools/AndroLog && mvn -q clean install -DskipTests)
git clone --depth 1 https://github.com/Sable/android-platforms.git tools/android-platforms

pip install openai jpype1                # only needed to run LLMDroid
```

## Measuring any APK

**1. Instrument** (once per APK):

```bash
python scripts/instrument_apk.py apks/<app>.apk --tag <APP>_SUPER_LOG
```

Writes `apks/instrumented/<app>.apk` and prints the tag and total method count.
Apps with `minSdk < 21` are patched to 21 automatically (Soot cannot split dex
below that).

**Verify it did not break the app** — instrumentation is bytecode rewriting and
does not always produce verifiable dex:

```bash
adb install -r -g apks/instrumented/<app>.apk
adb logcat -c && adb shell monkey -p <package> -c android.intent.category.LAUNCHER 1
sleep 12 && adb logcat -d | grep -c "VerifyError\|FATAL EXCEPTION"   # must be 0
```

**2. Run TestCube:**

```bash
adb logcat -G 64M                        # AndroLog floods the default buffer
python start.py -a apks/instrumented/<app>.apk -o output/<app> \
  -is_emulator -policy feature_guided \
  --code-coverage androlog --coverage-tag <APP>_SUPER_LOG \
  -keep_env -grant_perm
```

**3. Run LLMDroid** on the same APK (needs `config.json.<app>` with `Tag` and
`TotalMethod`; see below):

```bash
python scripts/run_llmdroid.py --app <app>
```

Both commands stop after **one hour** and write their reports; nothing else has
to be passed. See [The one-hour budget](#the-one-hour-budget) to change it.

**4. Compare:**

```bash
python scripts/compare_coverage.py \
  --testcube output/<app> --llmdroid output/llmdroid/<app> \
  --out output/coverage-compare
```

## Where reports are saved

| What | Path |
| --- | --- |
| Coverage series (live) | `output/<app>/codecoverage.txt` |
| Coverage summary | `output/<app>/code_coverage.json` |
| Feature coverage | `output/<app>/feature_coverage/report.{txt,json}` |
| LLMDroid run | `output/llmdroid/<app>/` (same file names) |
| Comparison | `output/coverage-compare/coverage_comparison.{md,json}` |

`scripts/run_llmdroid.py` exists so LLMDroid's output lands under `output/llmdroid/`
instead of inside `compare/LLMDroid/LLMDroid-Droidbot/output/`, where it is easy to lose.
It also swaps in the right `config.json` and restores the old one afterwards.

## The one-hour budget

A run used to end when the explorer decided it had finished, which makes a batch
of APKs take an unpredictable amount of time — and makes the two tools
incomparable, because whichever keeps going longer wins on coverage by default.
Both tools now stop after a fixed hour of wall clock and save their reports.

| | TestCube | LLMDroid |
| --- | --- | --- |
| Budget | `--max-run-seconds 3600` | `--timeout 3600` |
| Also settable as | `TESTCUBE_MAX_RUN_SECONDS` | — |
| Hard-stop grace | `--run-grace-seconds 300` | — (fixed at 300) |
| Disable | `--max-run-seconds 0` | `-timeout -1` |

An explicit flag beats an exported `TESTCUBE_*` variable. **Change the budget on
both sides or the comparison is void** — `compare_coverage.py` cannot detect an
unequal time budget the way it detects mismatched tags and denominators.

The hour is now the **only** budget that binds. The action caps
(`--max-run-events`, `--count`) are backstops set high enough that they do not
fire; TestCube paces itself against whichever of the two is further along, so
features late in the list are not starved when the clock is what runs out.

How it stops, in two layers:

1. **Soft deadline** at 3600s, checked at the top of the policy loop and again
   in `InputManager.add_event` — the chokepoint every policy routes through, so
   `dfs_greedy` is cut off on the same terms as `feature_guided`. The run
   unwinds normally and every report is written. Overrun is one action, the
   ~40s observed on money.
2. **Hard stop** at 3600 + 300s, from a watchdog thread, for a model call that
   never returns or an adb command that hangs. It writes what it can and exits
   `3`, so one wedged app cannot stall an overnight batch. Seeing exit 3 means
   that run's reports are partial.

`stop_reason` in the feature report says which fired: `budget_time` for the soft
deadline, `budget_time_hard` for the watchdog.

## Useful flags

- `--coverage-interval N` — sample every N actions (default 10).
- `--coverage-total-methods N` — override the denominator (read from the APK otherwise).
- `--no-restart-between-features` — skip the stop/start between features. Those
  restarts re-run already-covered startup code; on a 28-feature app they were 21%
  of every action issued.

## Reading the numbers

- **Launch cost dominates.** A cold launch alone reaches ~10% on these apps.
  Only the increment above that reflects exploration.
- **Check saturation, not just totals.** `compare_coverage.py` reports how far
  into each run the coverage flattened. A run that plateaued early was not cut
  short by its budget — which matters more now that every run is truncated at
  one hour rather than allowed to finish.
- **Compare actions, not only percentages.** The table's `Actions` column is the
  effort each tool spent to get there.
- **Average ≥3 seeds.** Both tools are stochastic.
- **Activity coverage is measured differently by each tool.** TestCube uses
  AndroLog `ACTIVITY=` probes intersected with manifest-declared activities;
  LLMDroid's monitor tracks methods only, so its activity number is recovered
  from `utg.js` and marked `*` in the table.

## LLMDroid notes

Its `config.json` needs `Tag` and `TotalMethod` (from step 1), plus `ApiKey` /
`Model` / `BaseUrl` — a local Ollama endpoint works and needs **no code change**.
Store one per app as `config.json.<app>`; `run_llmdroid.py` picks it up.
Run with `-code_coverage androlog`; `time` measures nothing.

## Which APKs work

| APK | Classes | Obfuscated | Status |
| --- | ---: | ---: | --- |
| `money.apk` | 21,939 | 2.5% | ✅ 147,371 methods / 51 activities |
| `newpipe.apk` (0.27.0) | 12,418 | 2.0% | ✅ 74,478 methods |
| `newpipe-0.29.1.apk` | — | — | ❌ Soot `[0..1]` |
| `vinyl.apk` | — | — | ❌ `VerifyError` in `MusicUtil.getSongInfoString` — app dies on startup while still *appearing* to run |
| `spotube.apk` | 6,749 | 71.6% | ❌ Soot `[0..1]` |
| `renpho.apk` | 90,405 | 3.0% | ❌ Soot `[0..1]` |
| `tasks.apk` | 24,146 | 0.2% | ❌ Soot `[0..1]` |
| `antennapod.apk` | 11,992 | 5.4% | ❌ Soot `[0..1]` |

### The `[0..1]` failure

Five of the six failures are one Soot 4.6.0 bug, not six app problems. Soot leaks its
1-bit integer type (`Integer1Type`, printed `[0..1]`) out of the type assigner and then
dies at whichever stage sees it first:

- while jimplifying — `InternalTypingException: Unexpected type [0..1] (Integer1Type)`
  in `integer.ClassHierarchy.typeNode` (tasks)
- while writing dex — `RuntimeException: not found: [0..1]` in
  `toDex.PrimitiveType.getByName`, via `ExprVisitor.castPrimitive`
  (renpho, antennapod, spotube, newpipe 0.29.1)

**App selection does not avoid it.** Neither obfuscation nor dex format predicts it:
tasks.apk is the cleanest APK measured (0.2% renamed classes) and still fails, while
money.apk passes at dex 039 and newpipe 0.29.1 fails at dex 035.

Things that do NOT work, all verified here rather than assumed:

- **`-n` / `-pkg`** — `SummaryBuilder` uses these only to decide whether to insert a
  probe. DexPrinter still writes every class, so the crash is untouched.
- **`-p jb.tr use-older-type-assigner:true`** — strictly worse. It fails earlier and on
  a JDK class (`java.lang.ThreadGroup.uncaughtException`), with runaway recursion in
  `TypeVariable.fixAncestors`.

Patching `PrimitiveType.getByName` to map `[0..1]` to boolean would silence the crash,
but it is not safe for a measurement tool: coercing a type Soot failed to infer can emit
subtly wrong bytecode, which is exactly the vinyl failure mode — an APK that installs and
launches but is quietly broken. Prefer an APK that instruments cleanly.
