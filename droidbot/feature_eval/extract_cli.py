"""CLI: README -> features.json via Gemini."""

import argparse
import os
import sys


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Detect application features from a README using Gemini."
    )
    parser.add_argument("--readme", required=True, help="Application README / specification")
    parser.add_argument("--out", required=True, help="Where to write features.json")
    parser.add_argument("--app", default=None, help="Application name (optional)")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    from droidbot.feature_eval.feature_extractor import FeatureExtractor
    payload = FeatureExtractor().extract(
        readme_path=os.path.abspath(args.readme),
        app_name=args.app,
        output_path=os.path.abspath(args.out),
    )
    features = payload.get("features") or []
    sys.stdout.write("Wrote %s (%d features)\n" % (os.path.abspath(args.out), len(features)))
    for item in features:
        sys.stdout.write("  [%s] %s\n" % (item.get("id"), item.get("name")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
