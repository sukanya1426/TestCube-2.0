#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate feature/<stem>/ specs for the experiment from APK_DATASET.md.

One app in the dataset becomes the four files a guided TestCube run reads
(droidbot/feature_tester/specs.py), plus the LLMDroid config that the same app
needs on the other side:

    feature/<stem>/README.md            app description, LLM context only
    feature/<stem>/ground_truth.json    offline EVAL yardstick (full list)
    feature/<stem>/guide_features.json  drives LIVE exploration (short hints)
    feature/<stem>/credential.txt       values to type
    compare/LLMDroid/LLMDroid-Droidbot/config.json.<stem>

The guide and the ground truth must stay INDEPENDENT. guide.classify_ground_truth_source()
compares the two files' feature-name sets, and if they match it flags the run
`same_as_guide_list` — the score is then guided-execution coverage, not coverage,
because the run is being graded against the list that drove it. So the guide here
is a strided subset with its own shortened phrasing, never a copy.

Usage:
    python scripts/make_feature_specs.py                     # docs/APK_DATASET.md
    python scripts/make_feature_specs.py --only markor,aegis
    python scripts/make_feature_specs.py --force            # overwrite existing
"""

from __future__ import print_function

import argparse
import io
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LLMDROID = os.path.join(REPO, "compare", "LLMDroid", "LLMDroid-Droidbot")
CATALOGUE = os.path.join(REPO, "experiment", "apps.json")

# Hand-authored specs. --force must not reach these: they were written and tuned
# against real runs, and the generator would replace them with dataset boilerplate.
PROTECTED = frozenset(["money", "newpipe"])

# How many features the guide offers. The guide is a hint list, not the yardstick;
# a long one just spends the run's budget re-reading it.
GUIDE_MAX = 14

STOPWORDS = set("""
a an the and or of to in on at for with from by into it its this that these those
is are was were be been being do does did use used using open tap press select
choose enter type set your you can will if when then than as but not no yes
app screen button icon menu option options item items list view tap' -> also
""".split())

# Quoted fragments that name a control type rather than a tappable label.
_GENERIC_LABELS = frozenset([
    "button", "tap", "icon", "menu", "the", "and", "or", "it", "a", "an",
    "button tap", "tap the", "three dots", "+",
])

# Words that make a good short imperative hint stop being short.
_CUT = re.compile(
    r"\s+(?:for|with|from|into|using|via|through|by|as|in|on|to|and|or|that|which)\s+.*$",
    re.I,
)
_PAREN = re.compile(r"\s*\([^)]*\)")


def unescape(text):
    """The dataset is escaped Markdown: \\-\\> for arrows, \\. after numbers, etc."""
    text = text.replace("\\-\\>", "->")
    text = re.sub(r"\\([-.#+*_\[\]()>])", r"\1", text)
    return text.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')


def parse_dataset(path):
    """{dataset app name: {package, version, note, features:[{name, actions:[...]}]}}"""
    raw = io.open(path, encoding="utf-8").read()
    apps = {}
    blocks = re.split(r"^### \*\*App Name: (.+?)\*\*\s*$", raw, flags=re.M)
    for i in range(1, len(blocks), 2):
        name = blocks[i].strip()
        body = blocks[i + 1]
        meta = re.search(
            r"^\*Package: (\S+)\s+\|\s+Version documented: (.+?)\s+\|\s+Reference: (.+?)\*\s*$",
            body, flags=re.M,
        )
        note = re.search(r"^\*Note: (.+?)\*\s*$", body, flags=re.M)
        features = []
        for match in re.finditer(
            r"^\*\*\d+\\\.\s+(.+?)\*\*\s*\n+\*\*Actions:\*\*\s*(.+?)(?=\n\*\*|\n###|\Z)",
            body, flags=re.M | re.S,
        ):
            title = unescape(match.group(1)).strip()
            steps = [
                step.strip(" .").strip()
                for step in unescape(match.group(2)).replace("\n", " ").split("->")
            ]
            steps = [re.sub(r"\s+", " ", s) for s in steps if s.strip()]
            if title and steps:
                features.append({"name": title, "actions": steps})
        apps[name] = {
            "package": meta.group(1) if meta else "",
            "version": meta.group(2).strip() if meta else "",
            "reference": meta.group(3).strip() if meta else "",
            "note": unescape(note.group(1)).strip() if note else "",
            "features": features,
        }
    return apps


def tokens(text):
    words = re.findall(r"[a-z][a-z0-9'\-]{2,}", (text or "").lower())
    return [w for w in words if w not in STOPWORDS]


def keywords_for(feature, limit=6):
    seen, out = set(), []
    for word in tokens(feature["name"]) + tokens(" ".join(feature["actions"][:2])):
        if word not in seen:
            seen.add(word)
            out.append(word)
        if len(out) >= limit:
            break
    return out


def nav_hints_for(feature, limit=4):
    """Literal on-screen labels: quoted strings in the steps, else the first words.

    Only short, arrow-free quotes count. The dataset writes steps as
    `tap the "+" ... -> tap "File"`, so a naive pair-up spans the arrow and
    yields a sentence fragment where a tappable label was wanted.
    """
    hints, seen = [], set()
    for step in feature["actions"]:
        # Per step, never across the joined list: `tap the "+" button` followed by
        # `tap "Folder"` would otherwise pair the closing quote of one step with
        # the opening quote of the next and yield "button tap".
        for quoted in re.findall(r'"([^"\n]{2,30})"', step):
            key = quoted.lower().strip(" .,")
            if not key or len(key.split()) > 3 or key in _GENERIC_LABELS:
                continue
            if key not in seen:
                seen.add(key)
                hints.append(key)
    for word in tokens(feature["name"]):
        if len(hints) >= limit:
            break
        if word not in seen:
            seen.add(word)
            hints.append(word)
    return hints[:limit]


def short_name(name):
    """A hint-sized restatement, deliberately not the ground-truth wording."""
    text = _PAREN.sub("", name).strip()
    text = _CUT.sub("", text).strip(" .,")
    words = text.split()
    if len(words) > 4:
        text = " ".join(words[:4])
    return text[0].upper() + text[1:] if text else name


def build_ground_truth(stem, app_name, meta):
    features = []
    for index, feature in enumerate(meta["features"], start=1):
        features.append({
            "id": "GT%03d" % index,
            "name": feature["name"],
            "description": "%s %s" % (feature["name"][0].upper() + feature["name"][1:],
                                      "as documented for %s." % app_name),
            "actions": feature["actions"],
            "keywords": keywords_for(feature),
            "nav_hints": nav_hints_for(feature),
        })
    return {
        "app": app_name,
        "platform": "Android",
        "source": "apk_dataset_inventory",
        "url": meta.get("reference", ""),
        "description": "Hand-verified capability inventory for %s (%s), version %s."
                       % (app_name, meta.get("package", ""), meta.get("version", "")),
        "features": features,
        "id_scheme": "GT### - independent of live README extraction IDs (F###)",
        "note": (
            "Generated by scripts/make_feature_specs.py from APK_DATASET.md. Evaluation "
            "only: never pass this file to a live run. The evaluator matches by "
            "name/description similarity, so IDs are not a join key."
        ),
    }


def build_guide(stem, app_name, meta, max_features=GUIDE_MAX):
    """A strided subset in its own words, so the two name sets cannot coincide."""
    source = meta["features"]
    if not source:
        return None
    stride = max(1, len(source) // max_features)
    picked = source[::stride][:max_features]
    features = []
    for index, feature in enumerate(picked, start=1):
        features.append({
            "id": "G%03d" % index,
            "name": short_name(feature["name"]),
            "description": feature["actions"][0][:140],
            # One or two steps only: the guide points at the feature, the run
            # is what discovers how to reach it.
            "actions": feature["actions"][:2],
            "keywords": keywords_for(feature, limit=4),
            "nav_hints": nav_hints_for(feature, limit=3),
            "source": "guide",
        })
    return {
        "app": app_name,
        "source": "guide",
        "url": meta.get("reference", ""),
        "note": (
            "Short hints that drive live exploration. Deliberately a %d-of-%d subset in "
            "different wording from ground_truth.json - if the two name sets matched, "
            "the run would be graded against the list that drove it."
            % (len(features), len(source))
        ),
        "features": features,
    }


README_TEMPLATE = u"""# {app}

Package: `{package}`
Version documented: {version}
Source: {reference}

{note}This app is explored automatically by TestCube and by LLMDroid. The list
below is the documented, user-facing capability set; it is context for the
tester, not a script to follow.

## What the app does

{summary}

## Capabilities

{bullets}
"""


def build_readme(app_name, meta):
    names = [f["name"] for f in meta["features"]]
    summary = "%s exposes %d documented user-facing features, including %s." % (
        app_name, len(names), ", ".join(n[0].lower() + n[1:] for n in names[:6]),
    )
    bullets = "\n".join("- %s" % name for name in names)
    note = ("> Note from the dataset: %s\n\n" % meta["note"]) if meta.get("note") else ""
    return README_TEMPLATE.format(
        app=app_name, package=meta.get("package", ""), version=meta.get("version", ""),
        reference=meta.get("reference", ""), note=note, summary=summary, bullets=bullets,
    )


# Values the tester types. Neutral placeholders; edit per app as needed.
CREDENTIAL_TEMPLATE = u"""email: testcube.bench@example.com
pwd: TestCube!2026
uid: testcube
f_name: Alex
l_name: Rivera
phone: 01701111111
search_query: test
playlist_name: TestCube List
note_title: TestCube Note
note_body: Created by the automated tester.
file_name: testcube
folder_name: TestCube
account_name: TestCube Account
amount: 100
title: TestCube Entry
label: TestCube
tag: testcube
url: https://example.com/feed.xml
city: Dhaka
country: Bangladesh
comment: no
rating: 1
"""

LLMDROID_CONFIG = {
    "ApiKey": "ollama",
    "Model": "qwen2.5vl:7b",
    "BaseUrl": "http://127.0.0.1:11434/v1",
}


def build_llmdroid_config(app_name, meta, tag):
    names = [f["name"] for f in meta["features"]]
    description = (
        "%s (%s). %s The app supports %s."
        % (app_name, meta.get("package", ""),
           meta.get("note", "").strip(),
           ", ".join(n[0].lower() + n[1:] for n in names[:18]))
    ).replace("  ", " ").strip()
    config = {"AppName": app_name, "Description": description}
    config.update(LLMDROID_CONFIG)
    config["Tag"] = tag
    # Filled in by scripts/run_experiment.py from the real instrumentation run.
    # 0 means "not measured yet"; LLMDroid refuses to start an androlog run on it.
    config["TotalMethod"] = 0
    return config


def write_json(path, payload, force):
    if os.path.exists(path) and not force:
        return False
    with io.open(path, "w", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, indent=2, ensure_ascii=False))
        handle.write(u"\n")
    return True


def write_text(path, text, force):
    if os.path.exists(path) and not force:
        return False
    with io.open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset", default=os.path.join(REPO, "docs", "APK_DATASET.md"),
                        help="Path to APK_DATASET.md")
    parser.add_argument("--catalogue", default=CATALOGUE)
    parser.add_argument("--only", default="", help="Comma-separated stems to generate")
    parser.add_argument("--pool", default="selected",
                        choices=["selected", "reserve", "all"])
    parser.add_argument("--force", action="store_true",
                        help="Overwrite files that already exist (default: keep them)")
    parser.add_argument("--allow-protected", action="store_true",
                        help="Also regenerate the hand-authored specs (%s). Rarely what you want."
                             % ", ".join(sorted(PROTECTED)))
    args = parser.parse_args(argv)

    if not os.path.isfile(args.dataset):
        sys.stderr.write("Dataset not found: %s\n" % args.dataset)
        return 2
    dataset = parse_dataset(args.dataset)
    catalogue = json.load(io.open(args.catalogue, encoding="utf-8"))

    only = set(s.strip() for s in args.only.split(",") if s.strip())
    written, skipped, missing = 0, 0, []
    for app in catalogue["apps"]:
        if args.pool != "all" and app["pool"] != args.pool:
            continue
        if only and app["stem"] not in only:
            continue
        meta = dataset.get(app["dataset_name"])
        if not meta or not meta["features"]:
            missing.append(app["dataset_name"])
            continue
        stem = app["stem"]
        # Covers the LLMDroid config too: its Description is the only context
        # LLMDroid gets, so replacing a hand-written one with generated prose
        # would quietly change what the comparison is measuring.
        if stem in PROTECTED and not args.allow_protected:
            skipped += 1
            print("[~] %-22s hand-authored, left alone (--allow-protected to override)" % stem)
            continue
        folder = os.path.join(REPO, "feature", stem)
        if not os.path.isdir(folder):
            os.makedirs(folder)
        made = []
        if write_text(os.path.join(folder, "README.md"),
                      build_readme(app["dataset_name"], meta), args.force):
            made.append("README.md")
        if write_json(os.path.join(folder, "ground_truth.json"),
                      build_ground_truth(stem, app["dataset_name"], meta), args.force):
            made.append("ground_truth.json")
        if write_json(os.path.join(folder, "guide_features.json"),
                      build_guide(stem, app["dataset_name"], meta), args.force):
            made.append("guide_features.json")
        if write_text(os.path.join(folder, "credential.txt"), CREDENTIAL_TEMPLATE, args.force):
            made.append("credential.txt")
        config_path = os.path.join(LLMDROID, "config.json.%s" % stem)
        if write_json(config_path,
                      build_llmdroid_config(app["dataset_name"], meta, app["coverage_tag"]),
                      args.force):
            made.append("config.json.%s" % stem)
        if made:
            written += 1
            print("[+] %-22s %d features  ->  %s" % (stem, len(meta["features"]), ", ".join(made)))
        else:
            skipped += 1
            print("[=] %-22s already present (use --force to overwrite)" % stem)

    if missing:
        sys.stderr.write("[!] not found in dataset: %s\n" % ", ".join(missing))
    print("\n%d app(s) written, %d left alone." % (written, skipped))
    return 0


if __name__ == "__main__":
    sys.exit(main())
