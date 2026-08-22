# Running LLMDroid from scratch (with TestCube feature coverage)

This is a from-scratch setup guide for `compare/LLMDroid/LLMDroid-Droidbot/` —
the state-of-the-art baseline TestCube is compared against. It covers:
installing raw LLMDroid, pointing its guidance LLM at a local Ollama model
(no API key needed), running it against an APK, and then measuring
**feature coverage** with the bolt-on described in
[`compare/LLMDroid/LLMDroid-Droidbot/TESTCUBE_INTEGRATION.md`](compare/LLMDroid/LLMDroid-Droidbot/TESTCUBE_INTEGRATION.md).

Nothing about LLMDroid's own testing logic is changed by any of this — see
that file for exactly what was added and why.

---

## 0. What you need before starting

| Tool | Why | Check |
| --- | --- | --- |
| macOS with Homebrew | commands below assume it (matches the rest of this repo) | `brew --version` |
| Python **3.9+** | LLMDroid-Droidbot requirement | `python3 --version` |
| Java JDK | Android SDK tooling (`aapt`, `adb`) needs it | `java -version` |
| Android SDK + `platform-tools` on `PATH` | `adb`, emulator | `adb version` |
| An Android emulator (AVD) or a physical device | something to test against | — |
| Ollama | local LLM for both LLMDroid's guidance and TestCube's coverage judge | `ollama --version` |
| An APK to test | e.g. reuse one from `apks/` in this repo | — |

If `adb` is not found, add platform-tools to your shell profile:

```bash
export PATH="$HOME/Library/Android/sdk/platform-tools:$PATH"
```

---

## 1. Get a Python environment

LLMDroid-Droidbot has its own small dependency set, separate from the main
TestCube `droidbot`. Use a **separate virtualenv** so nothing clashes with
this repo's own `.venv`:

```bash
cd /Users/saimon4u/Projects/TestCube-2.0/compare/LLMDroid/LLMDroid-Droidbot
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies (this is the exact command from LLMDroid's own
README):

```bash
pip install openai androguard networkx Pillow
```

- `openai` — the SDK LLMDroid uses to call its guidance LLM. It also works
  against Ollama's OpenAI-compatible endpoint (step 4), so you do **not**
  need an OpenAI account or API key.
- `androguard`, `networkx`, `Pillow` — droidbot's own core dependencies
  (APK static analysis, UTG graph, image handling).

You do **not** need `google-generativeai` unless you intend to use Gemini
as a fallback for the coverage judge (step 6) — the ported `GeminiAI.py`
in this checkout was patched to import it lazily so its absence never
breaks anything.

No package needs to be installed for the TestCube feature-coverage bolt-on
itself (`droidbot/feature_eval/`, `droidbot/local_vlm.py`) — it's pure
standard library.

---

## 2. Set up the Android side

### Option A — Emulator (recommended, matches the rest of this repo)

```bash
cd ~/Library/Android/sdk/emulator
./emulator -avd <your_avd_name>
```

List AVDs if you don't remember the name: `~/Library/Android/sdk/emulator/emulator -list-avds`.

Wait for the home screen, then in another terminal:

```bash
adb devices
```

It must print `device`, not `offline` or empty. If it prints nothing, the
emulator is still booting — wait and retry.

### Option B — Physical device

Enable Developer Options → USB debugging, plug it in, accept the RSA
prompt, confirm with `adb devices`.

### Accessibility service

Both droidbot and LLMDroid read the UI hierarchy through Android's
Accessibility API. The first run on a fresh AVD/device may need you to
manually enable it once (droidbot will prompt / try to enable it via
`adb shell settings put secure enabled_accessibility_services ...`; if
that silently fails, enable **DroidBot Accessibility Service** by hand
under Settings → Accessibility on the device).

---

## 3. Install Ollama and pull models

You need **two** local models, used for two independent purposes:

| Model role | Used by | Sends images? | Suggested model |
| --- | --- | --- | --- |
| LLMDroid's own guidance LLM (picks which widget to explore/click) | `droidbot/policy/llm_agent.py` | No — text only (HTML-serialized UI) | `qwen2.5:7b` (or any decent instruction-following text model you already have) |
| TestCube's offline coverage judge (did the trace cover this feature?) | `droidbot/feature_eval/llm_matcher.py` via `droidbot/local_vlm.py` | No — it also reasons over the text trace, not images, in this integration | `qwen2.5vl:7b` (matches the main TestCube repo's default so results are comparable) |

Install and start Ollama:

```bash
brew install ollama
brew services start ollama
```

Pull both models:

```bash
ollama pull qwen2.5:7b
ollama pull qwen2.5vl:7b
```

Sanity check:

```bash
curl -s http://127.0.0.1:11434/api/tags
```

You should see both models listed. If you'd rather reuse a single model
for both roles, just point `config.json`'s `Model` (step 4) at whichever
one you pulled — LLMDroid never sends screenshots, so a text-only model
works fine for its side.

---

## 4. Configure LLMDroid to use Ollama (no API key)

From `compare/LLMDroid/LLMDroid-Droidbot/`:

```bash
cp config.ollama.example.json config.json
```

Edit `config.json`:

```json
{
  "AppName": "Spotube",
  "Description": "One paragraph describing what the app does — copy it from feature/<stem>/README.md in the main repo. This gets fed into every LLM prompt as context.",
  "ApiKey": "ollama",
  "Model": "qwen2.5:7b",
  "BaseUrl": "http://127.0.0.1:11434/v1"
}
```

- `ApiKey` can be any non-empty placeholder string — Ollama does not check
  it, and the OpenAI SDK only refuses a `None`/missing key, not a fake
  one.
- `Model` / `BaseUrl` are officially supported LLMDroid config fields
  (see `LLMDroid-Droidbot/droidbot/policy/llm_agent.py:77-84`) — this is
  config, not a code change.
- Leave out `TotalMethod`, `Tag`, `ClassFilePath`, `EcFilePath` — they are
  only read when `--code_coverage` is `androlog` or `jacoco` (both require
  a recompiled, instrumented APK). We use `--code_coverage time` below,
  which needs none of that.

`JacocoBridge.jar` must also be present at the LLMDroid-Droidbot root —
it already is in this checkout (`compare/LLMDroid/LLMDroid-Droidbot/JacocoBridge.jar`),
untouched from the clone. It is only actually loaded if you pick
`--code_coverage jacoco`, which we don't.

---

## 5. Run LLMDroid

From `compare/LLMDroid/LLMDroid-Droidbot/` (venv active, emulator/device
connected, Ollama running):

```bash
python start.py \
  -a /path/to/app.apk \
  -o output/app-run1 \
  -is_emulator \
  -policy dfs_greedy \
  -code_coverage time \
  -timeout 3600 \
  -interval 3 \
  -count 100000 \
  -keep_app \
  -keep_env \
  -grant_perm
```

Flag notes:

- `-policy dfs_greedy` is the default anyway (`DEFAULT_POLICY` in
  `droidbot/input_manager.py:17`) and is the policy class that actually
  wires up the LLM agent (`UtgGreedySearchPolicy` → `UtgBasedInputPolicy`
  → `LLMAgent`, `droidbot/policy/utg_greedy_search_policy.py:7`,
  `utg_based_policy.py:50-51`). Passing it explicitly is just belt-and-
  braces.
- `-code_coverage time` is required for a non-instrumented APK — it makes
  LLMDroid switch from EXPLORE to LLM-guidance mode on elapsed time
  instead of watching Jacoco/AndroLog code coverage growth (`start.py:92`,
  `utg_based_policy.py:82`).
- `-timeout 3600 -interval 3 -count 100000` are the values from LLMDroid's
  own README example — adjust `-timeout` down for a quick smoke test
  (e.g. `600` for 10 minutes) before committing to a full run.
- `-d <serial>` is only needed if `adb devices` lists more than one
  device.
- Drop `-is_emulator` if you're on a physical device.

While it runs, `output/app-run1/` fills up with `states/`, `events/`,
`utg.js` (same layout as plain droidbot), plus LLMDroid's own
`LLM_QA.txt` (every prompt/response pair), `LLM-Interaction.txt` (timing),
and `codecoverage.txt`.

**Use a fresh `-o` folder for each run.** Nothing in this integration
resumes a previous run.

---

## 6. Measure feature coverage after the run

Still in `compare/LLMDroid/LLMDroid-Droidbot/`, with the same venv:

```bash
python evaluate_features.py \
  --results output/app-run1 \
  --features /Users/saimon4u/Projects/TestCube-2.0/feature/<stem>/ground_truth.json \
  --readme   /Users/saimon4u/Projects/TestCube-2.0/feature/<stem>/README.md
```

Replace `<stem>` with the app's folder name under the main repo's
`feature/` directory (e.g. `spotube`, `money`, `vinyl`) — this reuses the
**same hand-authored ground truth** the main TestCube pipeline scores
itself against, so the two numbers are directly comparable.

This does not touch the device — it only reads
`output/app-run1/{states,events,utg.js}` and asks the coverage judge (Ollama
`qwen2.5vl:7b` by default, matching the main repo; falls back to Gemini
only if `GEMINI_API_KEY`/`GOOGLE_API_KEY` is set in your shell) whether
each ground-truth feature was covered.

Output:

```
output/app-run1/feature_coverage/report.json
output/app-run1/feature_coverage/report.txt
```

`report.txt` prints **Feature Coverage** (`covered / total`) and
**Weighted Coverage** (`mean(completion_ratio)`) — the same two numbers
`docs/PROJECT.md` in the main repo defines for TestCube's own runs.

There is no `feature_test/report.json` journal in an LLMDroid run (that
only exists for TestCube's own live guided policy), so you won't see
`exploration_bank` cross-feature credit or an "online coverage" number —
only the offline number, which is the one that matters for a baseline
comparison.

---

## 7. Troubleshooting

| Symptom | Likely cause / fix |
| --- | --- |
| `adb devices` shows `offline` or nothing | Emulator still booting, or USB cable/driver issue on a physical device. Wait / reconnect. |
| LLMDroid hangs retrying `__get_response` ("Exception: ..., try to ask again in 3 seconds") | Ollama isn't reachable at `BaseUrl`, or the model in `config.json`'s `Model` field isn't pulled. Check `curl http://127.0.0.1:11434/api/tags` and `ollama list`. |
| `Must specify Tag and TotalMethod in config.json when using androlog!` | You forgot `-code_coverage time` (or omitted it — its default is `androlog`, which needs an instrumented APK). |
| `evaluate_features.py` prints "Coverage VLM/Gemini judge failed" | The `qwen2.5vl:7b` model isn't pulled/running, or Ollama stopped. Run `python -m droidbot.local_vlm --check` from `compare/LLMDroid/LLMDroid-Droidbot/` (with the venv active) to diagnose. |
| Permission dialogs / first-run popups block progress | Add `-grant_perm`; some first-run dialogs still need the accessibility service enabled (step 2). |
| Emulator `Unable to connect to adb daemon on port: 5037` right after boot | Startup noise after a snapshot load — wait it out, don't restart the AVD mid-run. |
| Want a quick smoke test before a full run | Use `-timeout 300 -count 500` to see LLMDroid produce a few states/events fast, then check `output/<run>/LLM_QA.txt` to confirm the guidance LLM is actually responding, before doing a full run. |

---

## 8. Where things live (quick reference)

```
compare/LLMDroid/LLMDroid-Droidbot/
├── config.json                    # you create this (step 4)
├── config.ollama.example.json     # template — points Model/BaseUrl at Ollama
├── start.py                       # unmodified LLMDroid entry point (step 5)
├── evaluate_features.py           # TestCube bolt-on entry point (step 6)
├── TESTCUBE_INTEGRATION.md        # what was added and why, in detail
├── droidbot/feature_eval/         # TestCube's offline coverage judge (ported)
├── droidbot/local_vlm.py          # TestCube's Ollama client (ported)
├── droidbot/GeminiAI.py           # TestCube's backend chooser (ported, Gemini import optional)
└── droidbot/policy/, droidbot/desc/, droidbot/coverage/   # LLMDroid's own logic — untouched
```
