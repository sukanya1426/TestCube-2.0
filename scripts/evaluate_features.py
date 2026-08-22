# Post-run feature coverage evaluator for TestCube 2.0.
# Default judge is the local VLM / Gemini (semantic), not token overlap.
# Does not start exploration.
#
#   python scripts/evaluate_features.py \
#     --results output/spotube-11 \
#     --features feature/spotube/ground_truth.json
from droidbot.feature_eval.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
