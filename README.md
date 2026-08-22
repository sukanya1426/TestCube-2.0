![DroidBot UTG](droidbot/resources/dummy_documents/droidbot_utg.png)

# TestCube 2.0

## News

:fire: Check out our recent work on integrating LLM with DroidBot to support intelligent task automation on smartphones! [AutoDroid](https://github.com/MobileLLM/AutoDroid)

## About
DroidBot is a lightweight test input generator for Android.
It can send random or scripted input events to an Android app, achieve higher test coverage more quickly, and generate a UI transition graph (UTG) after testing.

A sample UTG is shown [here](http://honeynet.github.io/droidbot/report_com.yelp.android/).

DroidBot has the following advantages as compared with other input generators:

1. It does not require system modification or app instrumentation;
2. Events are based on a GUI model (instead of random);
3. It is programmable (can customize input for certain UI);
4. It can produce UI structures and method traces for analysis.

**Reference**

[Li, Yuanchun, et al. "DroidBot: a lightweight UI-guided test input generator for Android." In Proceedings of the 39th International Conference on Software Engineering Companion (ICSE-C '17). Buenos Aires, Argentina, 2017.](http://dl.acm.org/citation.cfm?id=3098352)

## Prerequisite

1. `Python` (both 2 and 3 are supported)
2. `Java`
3. `Android SDK`
4. Add `platform_tools` directory in Android SDK to `PATH`
5. (Optional) `OpenCV-Python` if you want to run DroidBot in cv mode.

## How to install

Clone this repo and install with `pip`:

```shell
git clone https://github.com/honeynet/droidbot.git
cd droidbot/
pip install -e .
```

If successfully installed, you should be able to execute `droidbot -h`.

## How to use

1. Make sure you have:

    + `.apk` file path of the app you want to analyze.
    + A device or an emulator connected to your host machine via `adb`.

2. Start DroidBot:

    ```
    droidbot -a <path_to_apk> -o output_dir
    ```
    That's it! You will find much useful information, including the UTG, generated in the output dir.

    + If you are using multiple devices, you may need to use `-d <device_serial>` to specify the target device. The easiest way to determine a device's serial number is calling `adb devices`.
    + On some devices, you may need to manually turn on accessibility service for DroidBot (required by DroidBot to get current view hierarchy).
    + If you want to test a large scale of apps, you may want to add `-keep_env` option to avoid re-installing the test environment every time.
    + You can also use a json-format script to customize input for certain states. Here are some [script samples](script_samples/). Simply use `-script <path_to_script.json>` to use DroidBot with a script.
    + If your apps do not support getting views through Accessibility (e.g., most games based on Cocos2d, Unity3d), you may find `-cv` option helpful.
    + You can use `-humanoid` option to let DroidBot communicate with [Humanoid](https://github.com/yzygitzh/Humanoid) in order to generate human-like test inputs.
    + You may find other useful features in `droidbot -h`.

## Evaluation

We have conducted several experiments to evaluate DroidBot by testing apps with DroidBot and Monkey.
The results can be found at [DroidBot Posts](http://honeynet.github.io/droidbot/).
A sample evaluation report can be found [here](http://honeynet.github.io/droidbot/2015/07/30/Evaluation_Report_2015-07-30_1501.html).

## Acknowledgement

1. [AndroidViewClient](https://github.com/dtmilano/AndroidViewClient)
2. [Androguard](http://code.google.com/p/androguard/)
3. [The Honeynet project](https://www.honeynet.org/)
4. [Google Summer of Code](https://summerofcode.withgoogle.com/)

## Useful links

- [DroidBot Blog Posts](http://honeynet.github.io/droidbot/)
- [droidbotApp Source Code](https://github.com/ylimit/droidbotApp)
- [How to contact the author](http://ylimit.github.io)



## TestCube 2.0 layout

Keep inputs sorted by app. Generated runs go under `output/` (gitignored). Helper CLIs live in `scripts/`. For a full description of inputs, outputs, and how feature coverage is computed, see [docs/PROJECT.md](docs/PROJECT.md).

```
apks/<stem>.apk                 # the app binary
feature/<stem>/README.md        # app README or numbered GUI list
feature/<stem>/guide_features.json  # human-authored live exploration list (preferred)
feature/<stem>/ground_truth.json    # offline scoring list (may match the guide)
feature/<stem>/ground_truth_addendum.json  # 5–10 extra features not in the guide
feature/<stem>/credential.txt   # values to type (email, password, …)
feature/<stem>/notes.txt        # optional extra notes (same folder only)
scripts/                        # setup_local_vlm.sh, extract_features.py, …
output/<stem>/                  # pass this as -o
```

The APK **stem** is the file name without `.apk`. Example: `apks/spotube.apk` uses `feature/spotube/`.

### Full run: Spotube + Money (live test, then metrics)

Use a **new** `-o` folder each time. Reusing a finished folder resumes the old journal instead of starting over.

**Terminal 1 — emulator**

```bash
cd ~/Library/Android/sdk/emulator
./emulator -avd Pixel_5
```

Wait until the home screen is up.

**Terminal 2 — tester + metrics**

```bash
cd /Users/mahdiya/TestCube-2.0
source .venv/bin/activate

# device must show "device", not "offline"
adb devices

# optional local VLM (otherwise Gemini is used)
brew services start ollama
python -m droidbot.local_vlm --check
python -m droidbot.local_vlm --warmup

# --- live feature-guided runs (these take a long time) ---
droidbot -a apks/spotube.apk -o output/spotube -is_emulator
droidbot -a apks/money.apk   -o output/money   -is_emulator
droidbot -a apks/vinyl.apk   -o output/vinyl   -is_emulator

# --- offline coverage vs ground truth (VLM/Gemini judge; does not re-drive the device) ---
python scripts/evaluate_features.py \
  --results output/spotube \
  --features feature/spotube/ground_truth.json

python scripts/evaluate_features.py \
  --results output/money \
  --features feature/money/ground_truth.json

python scripts/evaluate_features.py \
  --results output/vinyl \
  --features feature/vinyl/ground_truth.json

# --- paper table across both apps ---
python scripts/aggregate_metrics.py \
  output/spotube output/money \
  --ground-truth feature/spotube/ground_truth.json \
  --ground-truth feature/money/ground_truth.json \
  --out output/metrics
```

Where to read the results:

| What | Path |
| --- | --- |
| Online coverage (self-report) | `output/<run>/feature_test/report.md` and `report.json` |
| Action log | `output/<run>/feature_test/log.md` |
| Replayable test cases | `output/<run>/feature_test/test_cases/*.json` |
| Offline coverage + confusion table | `output/<run>/feature_coverage/report.json` |
| UTG / screenshots | `output/<run>/index.html`, `states/`, `events/` |
| Aggregated paper table | `output/metrics/metrics.md` and `metrics.json` |
| Text fields to label by hand | `output/metrics/*_text_inputs.tsv` |

Optional after a covered feature: replay a saved test case (no LLM):

```bash
droidbot -a apks/spotube.apk -o output/spotube-replay \
  --replay output/spotube/feature_test/test_cases/F003.json \
  -is_emulator
```

Ablation (turn mechanisms off for a comparison run):

```bash
droidbot -a apks/spotube.apk -o output/spotube-nosf \
  --disable shared_flow,hybrid_discovery -is_emulator
```

`-a spotube` also works (resolved under `apks/`). Live steps are inferred from `feature/<stem>/README.md`. Gold lists (`ground_truth.json`) only count coverage after the run. Progress is written to `output/<run>/feature_test/`.

### Add a new APK

1. Copy the binary to `apks/<stem>.apk` (pick a short stem, e.g. `newpipe`).
2. Create `feature/<stem>/` and add:
   - `README.md` — the app README (what the tester may infer from). Put the detailed GUI gold list in `ground_truth.json`, not here.
   - `credential.txt` — `email:`, `pwd:`, `search_query:`, and any other field values the app needs.
3. Run:

```bash
droidbot -a apks/<stem>.apk -o output/<stem> -is_emulator
```

Overrides if you need them: `-readme path`, `-credential path`. Do **not** pass a gold `features.json` / `ground_truth.json` to live `droidbot` to steer taps — those files are for `evaluate_features.py` only.

### Optional flags

- `-features path/to/ground_truth.json` evaluation-only (coverage counting). Live steps are always inferred from the README.
- `-policy dfs_greedy` for random UI exploration
- `-llm auto|local|gemini` (`auto` prefers the local VLM)
- `-ollama-model qwen2.5vl:7b` / `-ollama-host http://127.0.0.1:11434`
- `GEMINI_MIN_INTERVAL=25` to space cloud LLM calls so you stay under quota

Helper scripts (from repo root):

```bash
python scripts/extract_features.py --readme feature/spotube/README.md --out /tmp/features.json
python scripts/evaluate_features.py --results output/spotube --features feature/spotube/ground_truth.json
python scripts/aggregate_metrics.py output/spotube output/money --out output/metrics
bash scripts/setup_local_vlm.sh
```

### Local VLM (Ollama, Apple Silicon)

The tester uses a local vision model for screenshots when Ollama is running, and falls back to Gemini otherwise.

```bash
bash scripts/setup_local_vlm.sh
python -m droidbot.local_vlm --check
python -m droidbot.local_vlm --warmup
```

Then run as usual. Force the local model with `-llm local`.

**Start the local VLM**

```bash
brew services start ollama
# first time only:
bash scripts/setup_local_vlm.sh
python -m droidbot.local_vlm --check
python -m droidbot.local_vlm --warmup
```

If `brew services` is not used:

```bash
ollama serve
```

**Stop the local VLM**

```bash
brew services stop ollama
```

Or if you started it with `ollama serve`, press Ctrl+C in that terminal (or `killall ollama`).