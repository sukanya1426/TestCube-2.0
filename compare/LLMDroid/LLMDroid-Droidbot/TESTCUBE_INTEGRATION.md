# TestCube feature-coverage bolt-on for LLMDroid-Droidbot

This adds two things on top of raw, unmodified LLMDroid-Droidbot so we can
measure **feature coverage** (TestCube's definition — user-facing
capabilities actually exercised, not code coverage) for a baseline
comparison. Nothing under `droidbot/policy/`, `droidbot/desc/`,
`droidbot/coverage/`, `droidbot/input_*`, `droidbot/device.py`, or
`start.py` was touched — LLMDroid explores exactly as it did before this
was added.

## What was added

| Path | What it is |
| --- | --- |
| `droidbot/feature_eval/` | TestCube's offline coverage judge, ported as-is (see below for the one compatibility patch). |
| `droidbot/local_vlm.py` | TestCube's Ollama client, ported unmodified. |
| `droidbot/GeminiAI.py` | TestCube's LLM-backend chooser (Ollama first, Gemini fallback), ported with the Gemini import made optional so nothing needs to be installed for the Ollama-only path. |
| `evaluate_features.py` | CLI entry point, mirrors TestCube's `scripts/evaluate_features.py`. Read-only: it never re-drives the device, it only reads an existing output directory. |
| `config.ollama.example.json` | Example `config.json` that points LLMDroid's own guidance LLM at a local Ollama server instead of OpenAI. |

Everything above is new files, except one small, isolated patch inside the
ported `droidbot/feature_eval/trace_loader.py::_visible_texts`: LLMDroid's
`DeviceState.to_dict()` stores widget text as one HTML-ish string (see
`droidbot/desc/device_state.py:65-74`) instead of vanilla droidbot's list
of view dicts. The patch pulls quoted attribute values and inner-tag text
out of that string with a couple of regexes so the coverage judge still
gets on-screen labels as evidence. Everything else in `feature_eval` is
byte-for-byte what TestCube uses, because LLMDroid's `states/`, `events/`,
and `utg.js` on-disk schemas otherwise match vanilla droidbot's (confirmed
against `droidbot/desc/utg.py:211-314`, `droidbot/input_event.py`, and
`droidbot/desc/device_state.py:save2dir`).

## 1. Running raw LLMDroid (unchanged)

```bash
cd compare/LLMDroid/LLMDroid-Droidbot
# config.json needs AppName/Description/ApiKey at minimum — see below
python start.py -a /path/to/app.apk -o output/app -code_coverage time
```

`-code_coverage time` is an existing LLMDroid flag (`start.py:92`) that
switches EXPLORE→ASK_GUIDANCE on elapsed time instead of Jacoco/AndroLog
code-coverage growth. Use it unless the APK has already been instrumented
with AndroLog or Jacoco — otherwise LLMDroid requires `TotalMethod`/`Tag`
or `ClassFilePath`/`EcFilePath` in `config.json` and a rebuilt APK, which
is out of scope for an out-of-the-box baseline run.

Output lands in `output/app/` in vanilla droidbot layout: `states/`,
`events/`, `utg.js`, plus LLMDroid's own `LLM_QA.txt`,
`LLM-Interaction.txt`, `codecoverage.txt`.

## 2. Pointing LLMDroid's guidance LLM at Ollama (no API key)

LLMDroid already supports any OpenAI-API-compatible endpoint via
`Model`/`BaseUrl` in `config.json` (`droidbot/policy/llm_agent.py:77-84`,
documented in the LLMDroid root `README.md`). Ollama serves an
OpenAI-compatible `/v1/chat/completions` route, and LLMDroid only ever
sends plain text prompts (HTML-serialized UI state), never images, so no
vision model or code change is required — just config:

```bash
ollama serve                      # or: brew services start ollama
ollama pull qwen2.5:7b            # any instruction-following text model works
cp config.ollama.example.json config.json
# edit AppName / Description in config.json for the app under test
```

`ApiKey` can be any non-empty placeholder string ("ollama") — Ollama does
not check it. This is unrelated to the coverage judge's own Ollama usage
described below; LLMDroid's guidance LLM and TestCube's coverage judge
are two independent local Ollama calls, both to whatever model you have
pulled.

## 3. Measuring feature coverage after a run

```bash
python evaluate_features.py \
  --results output/app \
  --features /path/to/TestCube-2.0/feature/<stem>/ground_truth.json \
  --readme   /path/to/TestCube-2.0/feature/<stem>/README.md
```

This is the same offline judge TestCube uses on its own runs
(`droidbot/feature_eval/evaluator.py`): it loads the ground-truth feature
list, reconstructs the executed trace from `output/app/events` +
`output/app/states` + `output/app/utg.js`, and asks a VLM/LLM judge
(local Ollama by default, `LLM_BACKEND=auto`, falls back to Gemini only if
`GEMINI_API_KEY`/`GOOGLE_API_KEY` is set) whether each ground-truth
feature was covered, partial, or not covered. It does not know LLMDroid's
own explore/guide/test-function state machine — it purely reads what
LLMDroid already wrote to disk, the same way it reads a TestCube run.

There is no `feature_test/report.json` journal (that only exists for
TestCube's own live guided policy), so the report will not have
`exploration_bank` cross-feature credit or online-coverage numbers — only
the offline `feature_coverage/report.json` / `report.txt`, which is the
number that matters for an out-of-the-box baseline comparison.

Output: `output/app/feature_coverage/report.json` and `report.txt`
(Feature Coverage = covered / total, Weighted Coverage = mean completion
ratio — see `../../../docs/PROJECT.md` in the main TestCube repo for the
full metric definitions).
