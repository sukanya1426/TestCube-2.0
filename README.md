![DroidBot UTG](droidbot/resources/dummy_documents/droidbot_utg.png)

# TestCube 2.0

An LLM-driven Android GUI explorer built on [DroidBot](https://github.com/honeynet/droidbot),
used to measure **code coverage** and **feature coverage**, and to compare those
numbers against [LLMDroid](compare/LLMDroid/LLMDroid-Droidbot/) on the same APK
under the same budget.

- [Quick start](#quick-start) · [The APK dataset](#the-apk-dataset) ·
  [One-click experiment](#one-click-experiment) ·
  [Choosing which APKs run](#choosing-which-apks-run) · [Layout](#layout)
- Deeper detail: [docs/CODE_COVERAGE.md](docs/CODE_COVERAGE.md) ·
  [docs/PROJECT.md](docs/PROJECT.md) · [experiment/README.md](experiment/README.md)

---

## Quick start

**Prerequisites**

1. `Python` 3, `Java`, `Android SDK`, with `platform-tools` on `PATH`
2. An emulator or device on `adb`
3. Ollama running the local VLM (both tools use it)

```bash
# terminal 1 - emulator
cd ~/Library/Android/sdk/emulator && ./emulator -avd Pixel_5

# terminal 2 - repo
cd /Users/mahdiya/TestCube-2.0
source .venv/bin/activate
adb devices                      # must show "device", not "offline"

brew services start ollama
python -m droidbot.local_vlm --check
python -m droidbot.local_vlm --warmup
```

**A single guided run**

```bash
python start.py -a apks/money.apk -o output/money -is_emulator
```

`-a money` also works; the APK is resolved under `apks/`. Everything the run
needs is discovered from `feature/<stem>/` — no flags.

---

## The APK dataset

**The dataset lives in the repo at [`docs/APK_DATASET.md`](docs/APK_DATASET.md).**
(It was compiled outside the repo and has been copied in, so nothing depends on
`~/Downloads` any more.)

It is a structured, user-facing feature inventory covering **42 Android
applications** and **1,589 documented features**. Each app is recorded as:

```
### **App Name: Markor**
*Package: net.gsantner.markor  |  Version documented: 2.16.1  |  Reference: ...*

**1\. Create a new plain text or Markdown document**
**Actions:** Open the Files tab -> tap the "+" button -> tap "File" -> ...
```

Every entry is a control, screen, menu item or setting documented for that app;
nothing was invented, and unverifiable items are marked "Unable to verify".

### From the dataset to a runnable app

`scripts/make_feature_specs.py` parses the dataset and writes, per app:

| File | Role |
| --- | --- |
| `feature/<stem>/README.md` | App description. LLM context only. |
| `feature/<stem>/guide_features.json` | Drives **live** exploration. Short hints. |
| `feature/<stem>/ground_truth.json` | Offline **evaluation** yardstick. |
| `feature/<stem>/credential.txt` | `key: value` lines the tester types. |
| `compare/.../config.json.<stem>` | LLMDroid's side: `AppName`, `Description`, `Tag`, `TotalMethod`. |

```bash
python scripts/make_feature_specs.py --dataset docs/APK_DATASET.md
python scripts/make_feature_specs.py --dataset docs/APK_DATASET.md --only markor,aegis
```

The guide is a strided subset written in its own wording, never a copy of the
ground truth. If the two name sets matched, `guide.classify_ground_truth_source()`
would flag `same_as_guide_list` and the score would be guided-execution coverage
— the run graded against the list that drove it. The hand-authored `money` and
`newpipe` specs are protected from regeneration.

### Which apps are selected

[`experiment/apps.json`](experiment/apps.json) holds **30 selected** candidates
and a **12-app reserve** pool, each with the reason it was chosen or excluded.
Selection criteria: open source (so the documented version is obtainable), no
account required, no root, no special hardware, enough GUI-reachable features.

**Compatibility is measured, not predicted.** An APK is only usable if it
survives Soot/AndroLog instrumentation *and* the rewritten dex verifies.
`docs/CODE_COVERAGE.md` records six of eight APKs failing — including the
*least* obfuscated one measured — so `scripts/run_experiment.py` decides it at a
preflight gate and writes the verdict back into `apps.json`.

Check the current state at any time:

```bash
python scripts/check_experiment_setup.py          # files + compatibility, all 30
```

---

## One-click experiment

One command runs everything, per app in order:
**instrument → verify → TestCube → LLMDroid → compare → feature eval.**

```bash
python scripts/run_experiment.py
```

### Running 5 APKs

Open [`scripts/run_experiment.py`](scripts/run_experiment.py) and set the two
variables at the top (around line 61):

```python
APK_NAMES = []        # empty  -> auto-pick
NUM_APKS  = 5         # ...the first 5 apps that have a binary in apks/
```

then:

```bash
python scripts/run_experiment.py
```

Or without editing the file at all:

```bash
python scripts/run_experiment.py --apps money,newpipe,markor,aegis,fossifyclock
```

The script prints which rule it used before doing anything, so you never have to
guess:

```
Selecting the first 5 app(s) with a binary (NUM_APKS in scripts/run_experiment.py); 2 of 30 have one.
```

Always dry-run first — it prints the plan and the worst-case runtime, and runs nothing:

```bash
python scripts/run_experiment.py --dry-run
```

---

## Choosing which APKs run

This lives in **exactly one place**: the top of
[`scripts/run_experiment.py`](scripts/run_experiment.py).

```python
APK_NAMES = ["money", "newpipe"]   # which APKs
NUM_APKS  = 5                      # how many
```

**The one rule that matters: `APK_NAMES` wins. `NUM_APKS` is only used when
`APK_NAMES` is empty.**

| What you want | `APK_NAMES` | `NUM_APKS` | Result |
| --- | --- | --- | --- |
| These exact apps | `["money", "newpipe"]` | *(ignored)* | runs those two, in order |
| Any 5 that are ready | `[]` | `5` | first 5 with a binary in `apks/` |
| Any 10 that are ready | `[]` | `10` | first 10 with a binary |
| All that are ready | `[]` | `99` | every app with a binary |

Names are the **stem**: the APK filename without `.apk`, matching the `stem`
column in `experiment/apps.json`. `apks/money.apk` → `"money"`.

For one run only, without editing anything:

```bash
python scripts/run_experiment.py --apps markor,aegis     # overrides APK_NAMES
python scripts/run_experiment.py --count 5               # overrides NUM_APKS
```

Everything **else** — budget, output folders, policy, LLM backend — is in
[`experiment/config.json`](experiment/config.json). The app list is deliberately
not duplicated there.

| Setting | Default |
| --- | --- |
| `budget_seconds` / `grace_seconds` | `3600` / `300` |
| `testcube_output` / `llmdroid_output` / `compare_output` / `log_dir` | `output/experiment/...` |
| `policy` / `llmdroid_policy` | `feature_guided` / `dfs_greedy` |
| `verify_instrumentation`, `run_llmdroid`, `run_compare`, `run_feature_eval` | `true` |

Other flags: `--budget-seconds N`, `--resume` (skip finished apps),
`--no-llmdroid`, `--dry-run`.

### Where output lands

```
output/experiment/testcube/<stem>/   code_coverage.json, codecoverage.txt,
                                     feature_coverage/report.{json,txt}, .droidbot/utg.js
output/experiment/llmdroid/<stem>/   codecoverage.txt, utg.js, LLM_QA.txt
output/experiment/compare/<stem>/    coverage_comparison.{md,json}
output/experiment/compare/experiment_summary.md    one table for the whole batch
output/experiment/logs/<stem>.log    full stdout for that app
```

The summary is rewritten after **every** app, so a batch interrupted at app 17
still leaves 16 apps of usable results. One app failing never stops the run, and
a single-instance lock stops two runners colliding on one emulator.

---

## Adding a new APK

1. Put the binary at `apks/<stem>.apk` (short stem, e.g. `newpipe`).
2. If the app is in the dataset, generate its specs:
   `python scripts/make_feature_specs.py --dataset docs/APK_DATASET.md --only <stem>`
   Otherwise write `feature/<stem>/` by hand (four files, table above).
3. Add it to `experiment/apps.json`, or just name it in `APK_NAMES`.
4. `python scripts/check_experiment_setup.py` to confirm nothing is missing.

---

## Layout

```
apks/<stem>.apk                     the app binary
apks/instrumented/<stem>.apk        AndroLog-instrumented build
docs/APK_DATASET.md                 the 42-app / 1,589-feature inventory
feature/<stem>/                     README.md, guide_features.json,
                                    ground_truth.json, credential.txt
experiment/apps.json                30 selected + 12 reserve, with reasons
experiment/config.json              budget, paths, policy (NOT the app list)
scripts/run_experiment.py           the one-click runner  <- APK_NAMES / NUM_APKS
scripts/make_feature_specs.py       dataset -> feature specs
scripts/check_experiment_setup.py   verify every app is ready
scripts/instrument_apk.py           AndroLog instrumentation
scripts/compare_coverage.py         TestCube vs LLMDroid table
output/<stem>/, output/experiment/  generated runs (gitignored)
```

---

## Reading the numbers

- **Launch cost dominates.** A cold launch alone reaches ~10% on these apps; only
  the increment above that reflects exploration.
- **Check saturation, not just totals.** `compare_coverage.py` reports how far
  into each run coverage flattened.
- **Average ≥3 seeds.** Both tools are stochastic and coverage rises with time.
- **Known confound:** TestCube reads a per-app `guide_features.json`; LLMDroid
  gets only a prose `Description`. Part of any gap is *guided vs unguided*, not
  *better algorithm*. Add TestCube's own `dfs_greedy` as a third arm before
  claiming otherwise.
- **Activity coverage is measured differently by each tool** — TestCube uses
  AndroLog `ACTIVITY=` probes; LLMDroid's number comes from `utg.js` and is
  marked `*` in the table.

---

## Ablation and replay

```bash
# turn mechanisms off for a comparison run
python start.py -a apks/money.apk -o output/money-nosf \
  --disable shared_flow,hybrid_discovery -is_emulator

# replay a saved test case, no LLM
python start.py -a apks/money.apk -o output/money-replay \
  --replay output/money/feature_test/test_cases/F003.json -is_emulator
```

## Local VLM (Ollama, Apple Silicon)

```bash
bash scripts/setup_local_vlm.sh
python -m droidbot.local_vlm --check
python -m droidbot.local_vlm --warmup
```

Force it with `-llm local`; `brew services stop ollama` to stop it.

## Acknowledgement

Built on [DroidBot](https://github.com/honeynet/droidbot) —
[Li, Yuanchun, et al. "DroidBot: a lightweight UI-guided test input generator for
Android." ICSE-C '17](http://dl.acm.org/citation.cfm?id=3098352). Also
[AndroidViewClient](https://github.com/dtmilano/AndroidViewClient),
[Androguard](http://code.google.com/p/androguard/), and
[The Honeynet Project](https://www.honeynet.org/).
