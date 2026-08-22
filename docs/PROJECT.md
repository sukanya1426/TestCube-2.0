# TestCube 2.0 — system overview

TestCube 2.0 is a **feature-guided Android GUI tester** built on [DroidBot](https://github.com/honeynet/droidbot). It does not tap the UI at random. It:

1. Reads what the app can do from a README and/or a short human **guide list**.
2. Tests **one feature at a time** on a real device or emulator.
3. **Restarts the app** before the next feature so leftover screens do not poison the next attempt.
4. Remembers every executed step so a later feature can finish an earlier partial one.
5. Writes a journal plus two coverage numbers: **fully covered / total**, and a **weighted** score that includes partials.

No per-app activity names are hardcoded. Spotube, Money Manager Ex, Vinyl, or a new APK all go through the same pipeline.

---

## What “feature coverage” means

The question is: **which user-facing capabilities did the tester actually exercise?**

That is not line coverage. Opening a related screen, or seeing a button in a UI dump, is not coverage. A feature is covered only when the GUI actions that carry out that capability happened (or an equivalent path did).

Two scoreboards exist on purpose. Do not mix them.

| Number | Written where | What it is allowed to claim |
| --- | --- | --- |
| **Online coverage** | Live journal `feature_test/report.md` | Did the guided policy finish the *list that drove exploration* (guide / extracted features)? |
| **Offline coverage** | `feature_coverage/` via `scripts/evaluate_features.py` | Did the recorded event trace match a *hand-authored* `ground_truth.json`? |

Live IDs (`F001`) and gold IDs often name **different** features. Matching is by **name**, not by ID.

Gold JSON is **eval-only**. It is never loaded as live `remaining_actions`. If you pass `ground_truth.json` as `-features` to `droidbot`, the tester warns and still drives from the guide / README.

---

## How we find coverage

### Live (online)

Code: `droidbot/feature_tester/policy.py`, `journal.py`, `step_bank.py`.

The policy keeps a **current feature** and a `remaining_actions` list. Each injected event is recorded. A remaining step completes only when the event type and visible label fit that step (typing steps need `set_text`; “Select X” needs a widget whose text overlaps X).

Statuses:

| Status | Meaning |
| --- | --- |
| **covered** | Remaining steps are empty, or a skip rule proved the capability already done (e.g. onboarding already finished, hub visible). `completion_ratio = 1.0` |
| **partial** | Some listed steps completed, then the tester got stuck, hit a loop, or hit the per-feature step cap. Ratio = completed / listed |
| **dropped** | Left without useful completed steps (loop, stagnation, crash-restart budget) |
| **not_present** | Conservative: the capability is judged not in the APK. Not used just because the current screen is the home hub |

**Feature Coverage (classic)** stays:

```
fully_covered / total_features
```

If 10 features are listed and 5 are fully covered, that is **50%**. Partials do **not** count as a full cover here.

**Weighted Feature Coverage** is the new metric:

```
mean(completion_ratio)
```

A feature that finished 3 of 5 gold/guide steps contributes `0.6`, not `1.0` and not `0`. Covered contributes `1.0`. Untouched contributes `0`. This is how partial work shows up without pretending it is full coverage.

Both numbers appear in `feature_test/report.md` and `feature_coverage/report.txt`.

### Offline (after the run)

```bash
python scripts/evaluate_features.py \
  --results output/vinyl-4 \
  --features feature/vinyl/ground_truth.json \
  --readme feature/vinyl/README.md \
  --matcher ai
```

This does **not** re-drive the device. Default `--matcher ai` is a local VLM / Gemini **semantic judge** (`droidbot/feature_eval/llm_matcher.py`). It scores intent from taps, typed text, and destination screens. Token overlap is ablation-only (`--matcher deterministic`).

Rules for the judge:

- Gold step **order is not required** (a→c→b can still cover).
- **PARTIAL is kept.** An incomplete path is not discarded just because later gold steps are missing.
- Covered features always get `completion_ratio = 1.0` for the weighted metric.
- Later exploration can complete an earlier partial: if the journal marked a feature `completion_source=cross_feature`, offline scoring can upgrade it to covered.

Deterministic ablation still exists. Weak token matches below confidence **0.5** are skipped so “Tap Add Account” vs `CREATE DATABASE` at 0.11 does not inflate partials.

---

## What we did to increase coverage (this iteration)

These changes are the context for later work. They were added after the first Spotube/Money runs showed 0% offline coverage and testers stuck on leftover screens from the previous feature.

### 1. Restart the app between features

When feature A is **done or stuck**, the tester does **not** start feature B on A’s last screen.

Sequence (`policy.py`):

1. Finish A (`_drop_current`).
2. If at least one feature has already been finished, set a feature-switch restart.
3. `am force-stop <package>`
4. `am start` the launch activity
5. Only then `_begin_feature(B)`

The first feature of a run is **not** force-stopped (the app was just installed). Later switches always cold-start. Feature-switch restarts do **not** increment the crash-restart counter, so a 9-feature Vinyl list does not trip `MAX_RESTARTS`.

Why: leftover search boxes, empty-state lists, and now-playing panels from A made B look “stuck in a loop” or complete the wrong step. Vinyl logs show `Restart before testing F002` … `F009` on every switch.

### 2. Break loops without lying about coverage

Existing recovery (still on):

| Situation | What happens |
| --- | --- |
| Same screens repeating (A-B-A-B) | Try an **untried** widget (max 3 backtracks), then leave as **partial** (or dropped if nothing completed) |
| Novelty stuck | Escalate once, then terminate the feature |
| Per-feature step cap (`MAX_STEPS_PER_FEATURE = 60`) | Stop that feature, restart, move on |
| App not in the stack | Start intent (no BACK/HOME loop on the launcher) |
| Permission / first-run dialog | Grant or dismiss, then continue |

The **new** piece is: after that leave, **restart** so the next feature does not inherit the loop.

### 3. Cross-feature step memory (exploration bank)

Code: `droidbot/feature_tester/step_bank.py`, `journal.apply_bank_credit`.

If feature A explored a→b→c and got stuck on d and e, A is **partial**. If later feature P actually performs d and e, A is upgraded:

- remaining steps of A are matched against later events from **other** feature IDs
- A can become **partial** (some leftover steps found) or **covered** (`completion_source=cross_feature`)
- `credited_from` / `credited_steps` are stored on the feature and in `session.json` as `exploration_bank`

Credit runs after every recorded tap, when a feature finishes, and again at `finalize`. Offline eval re-applies the bank so the LLM judge can see credited steps.

Vinyl-4 example: F005 (Next) was credited from F004 (Pause); several hybrid features were credited from F012.

### 4. Honest metrics (do not count partial as full)

Earlier offline reports used `(covered + partial) / total`, so 2 covered + 2 partial out of 28 looked like 14%. That hid how little was fully done.

Now:

- **Feature Coverage** = `covered / total` only
- **Weighted Coverage** = `mean(completion_ratio)` so partials still contribute a fraction

Schema fields on existing reports were **kept**; the new fields are additive (`weighted_coverage`, `completion_ratio`, `exploration_bank`).

### 5. LLM judge instead of string matching (offline)

String/token matching called many wrong-screen taps “covered” or dropped real partials. The coverage judge is now a VLM/Gemini verdict. Batch scoring (chunks of 7) is used so 28 Money features do not take one LLM call each.

Local VLM (`qwen2.5vl:7b` via Ollama) is preferred (`LLM_BACKEND=auto` / `local`).

### 6. Guide list vs gold list

| File | Role |
| --- | --- |
| `feature/<stem>/guide_features.json` | Short human hints that **drive** live taps |
| `feature/<stem>/ground_truth.json` | Longer gold list used **only** to score after the run |
| `feature/<stem>/README.md` | Fallback extraction + LLM context |
| `feature/<stem>/credential.txt` | Values to type |

Live exploration must not load gold JSON as `remaining_actions`.

---

## Layout

```
apks/<stem>.apk                 # local binary (gitignored; keep apks/.gitkeep)
feature/<stem>/README.md
feature/<stem>/guide_features.json
feature/<stem>/ground_truth.json
feature/<stem>/ground_truth_addendum.json
feature/<stem>/credential.txt
scripts/                        # evaluate_features.py, extract_features.py, …
output/<run>/                   # gitignored run artifacts
droidbot/feature_tester/        # live policy, journal, step bank, restart
droidbot/feature_eval/          # offline judge, weighted coverage, reports
tests/
```

The **stem** is the APK file name without `.apk`. `apks/vinyl.apk` uses `feature/vinyl/`. Reusing a finished `-o` folder **resumes** the journal. Use a new folder (`output/vinyl-4`, `output/money-2`) for a clean run.

---

## Outputs

| Path | Meaning |
| --- | --- |
| `feature_test/report.md` | Live covered / partial / dropped + **Coverage** + **Weighted coverage** |
| `feature_test/report.json` | Same, plus `exploration_bank`, `online_coverage`, `offline_coverage` |
| `feature_test/session.json` | Resume state, remaining/completed steps, bank |
| `feature_test/log.md` | Decisions, restarts, `chain C00x finalized`, VLM fallback |
| `feature_test/test_cases/*.json` | Replayable traces |
| `events/`, `states/` | Injected events and screenshots |
| `feature_coverage/report.txt` | Offline Feature Coverage + Weighted Coverage |

---

## End-to-end pipeline

```
APK + guide/README + credentials + device
        │
        ▼
 Install & launch (permissions, first-run)
        │
        ▼
 For each feature:
   [if not the first] force-stop → start
   dump UI → score widgets → (VLM if unsure) → tap/type
   match remaining steps → record in journal + exploration bank
   if stuck / done → credit bank onto earlier partials → next feature
        │
        ▼
 Finalize journal (re-credit bank, write report.md)
        │
        ▼
 Offline LLM judge vs ground_truth.json
   Feature Coverage = covered / total
   Weighted Coverage = mean(completion_ratio)
```

Typical commands:

```bash
source .venv/bin/activate
adb devices
droidbot -a apks/vinyl.apk -o output/vinyl-4 -is_emulator

python scripts/evaluate_features.py \
  --results output/vinyl-4 \
  --features feature/vinyl/ground_truth.json \
  --readme feature/vinyl/README.md \
  --matcher ai
```

---

## Older mechanisms (still on)

All can be turned off with `--disable name,name` or `TESTCUBE_DISABLE=…`. None hardcode app names.

| Mechanism | What it does |
| --- | --- |
| **shared_flow** | Skip a known completed prefix when a later feature shares a chain. |
| **hybrid_discovery** | After the hub, infer extra features from labeled widgets. Stops on `(state, widget)` repeat. |
| **backtrack** | On a loop, pick a widget not already tried in this feature (max 3). |
| **afford_search** | Before dropping add/create, try FAB / plus / menu / scroll. |
| **stagnation** | Low novelty + remaining steps not shrinking → terminate. |
| **context_functions** | Typed values from `credential.txt` / named helpers. |
| **non_idempotent** | Do not tap pay/delete/confirm twice. |

---

## First baseline vs later runs

### First pipeline (2026-08-18) — diagnostic

Spotube online **0/10**. Money online **2/3** vs a 3-feature extract, offline **0/28** once weak token matches were dropped. Bugs found then (now fixed): ID collision, chains never finalized, backtrack re-selected tried widgets, hybrid discovery had no repeat-exit, LLM call counter was stale.

### Vinyl-4 (2026-08-20) — after restart + bank + weighted metric

Live: 16 features (9 guide + hybrid). **4/16 fully covered (25%)**, weighted **52%**. Cross-feature credit fired (F005 from F004, several hybrid features from F012). Restart ran before every later feature.

Offline vs 9 gold features: **2/9 covered (22%)**, 4 partial, weighted **34%**. Judge: local VLM, not token overlap.

Treat 2026-08-18 P/R/F1 as diagnostic. Cite later `output/<run>/` reports for the current method.

---

## How to run

```bash
cd ~/Library/Android/sdk/emulator
./emulator -avd Pixel_5

cd /Users/mahdiya/TestCube-2.0
source .venv/bin/activate
adb devices          # must say "device", not offline
brew services start ollama   # optional local VLM

droidbot -a apks/spotube.apk -o output/spotube -is_emulator
droidbot -a apks/money.apk   -o output/money-2 -is_emulator
droidbot -a apks/vinyl.apk   -o output/vinyl-4 -is_emulator
```

Emulator `Unable to connect to adb daemon on port: 5037` or `Failed to find ColorBuffer` at boot is usually startup noise after a snapshot load. Do not restart the AVD while a `droidbot` run is pulling screenshots.

Add a new app: `apks/<stem>.apk` (local only), `feature/<stem>/README.md` + `guide_features.json` + `credential.txt`. For offline scoring add `ground_truth.json` with IDs that do not collide by accident with the live list.

---

## Main code map

| Module | Responsibility |
| --- | --- |
| `droidbot/feature_tester/policy.py` | One-feature loop, **restart between features**, emit + bank |
| `droidbot/feature_tester/step_bank.py` | Global executed-step store |
| `droidbot/feature_tester/journal.py` | Step matching, `apply_bank_credit`, both coverage numbers |
| `droidbot/feature_tester/advisor.py` | Heuristic + VLM next widget |
| `droidbot/feature_eval/coverage.py` | `covered / total` and `mean(completion_ratio)` |
| `droidbot/feature_eval/llm_matcher.py` | Batch semantic judge |
| `droidbot/feature_eval/evaluator.py` | Re-apply bank, write `feature_coverage/` |
| `droidbot/local_vlm.py` | Ollama vision model |
| `tests/test_feature_eval.py` | Classic vs weighted coverage |
| `tests/test_feature_upgrade.py` | Bank credit + restart-before-next-feature |

---

## What “success” looks like

1. Guide/README features a human would recognize; hybrid discovery may add more after the hub.
2. Each new feature starts from a **fresh app process**, not the previous feature’s last screen.
3. A step completes only when the GUI action really did that step.
4. If A was partial and P later does A’s leftover steps, A is upgraded — not left stale.
5. Reports show **Feature Coverage** (full only) and **Weighted Coverage** (partials as fractions).
6. `log.md` shows `Restart before testing …` and any `Cross-feature credit`.

Coverage will not be 100% for every app (file pickers, empty libraries, unlabeled Flutter views). The tester’s job is to **reach** those screens, **leave loops** by restarting, **credit** work done later, and **not count a partial as a full cover**.
