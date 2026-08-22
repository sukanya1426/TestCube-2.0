# Post-run feature coverage evaluator, ported from TestCube 2.0.
#
# Runs OFFLINE against an existing LLMDroid-Droidbot output directory
# (states/, events/, utg.js). It does not start or influence exploration
# and does not touch anything under droidbot/policy, droidbot/desc, or
# droidbot/coverage — LLMDroid's own testing/exploration logic is
# unmodified. This script only reads what LLMDroid already wrote to
# disk and scores it against a TestCube-style ground_truth.json.
#
# Usage:
#   python start.py -a app.apk -o output/app -code_coverage time   # raw LLMDroid run
#   python evaluate_features.py --results output/app \
#       --features /path/to/feature/<stem>/ground_truth.json \
#       --readme /path/to/feature/<stem>/README.md
#
# See README.md ("TestCube feature coverage" section) for details, and
# droidbot/local_vlm.py / config.ollama.example.json for the Ollama setup
# this judge uses when no API key is configured.
from droidbot.feature_eval.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
