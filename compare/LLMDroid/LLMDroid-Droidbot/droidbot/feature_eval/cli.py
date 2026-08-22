"""CLI for post-run feature coverage evaluation.

Does not change start.py or dfs_greedy behavior.
"""

import argparse
import os
import sys


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Evaluate feature coverage of an existing TestCube run."
    )
    parser.add_argument(
        "--results",
        required=True,
        help="TestCube output directory (events/, states/, utg.js)",
    )
    parser.add_argument(
        "--features",
        required=True,
        help="Manually prepared ground-truth features.json",
    )
    parser.add_argument(
        "--readme",
        default=None,
        help="Optional application README (LLM context only)",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Report directory (default: <results>/feature_coverage)",
    )
    parser.add_argument(
        "--matcher",
        choices=["ai", "deterministic", "hybrid"],
        default="ai",
        help="Coverage judge. ai (default) = VLM/Gemini semantic scoring. "
             "deterministic = token overlap ablation. hybrid = old string-first path.",
    )
    parser.add_argument(
        "--no-llm",
        action="store_true",
        help="Alias for --matcher deterministic",
    )
    parser.add_argument(
        "--min-confidence",
        type=float,
        default=None,
        help="Deterministic ablation only: skip individual step matches below this "
             "confidence (default: 0.5). Partial paths are kept. Coverage scoring "
             "uses the LLM judge, not this threshold.",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    from droidbot.feature_eval.evaluator import evaluate_feature_coverage

    matcher_mode = "deterministic" if args.no_llm else args.matcher
    report, paths = evaluate_feature_coverage(
        results_dir=os.path.abspath(args.results),
        features_path=os.path.abspath(args.features),
        readme_path=os.path.abspath(args.readme) if args.readme else None,
        output_dir=os.path.abspath(args.out) if args.out else None,
        use_llm=matcher_mode != "deterministic",
        min_confidence=args.min_confidence,
        matcher_mode=matcher_mode,
    )
    from droidbot.feature_eval.report import ReportGenerator
    sys.stdout.write(ReportGenerator().render_text(report))
    sys.stdout.write("\nWrote %s\n" % paths["json"])
    sys.stdout.write("Wrote %s\n" % paths["txt"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
