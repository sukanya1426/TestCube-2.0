"""Discover README/txt specs and turn them into GUI feature lists.

No per-app hardcoding. A numbered exploration list in a txt/md file is used
when present; otherwise the README is parsed for user-facing capabilities.

Layout (repo root):

    apks/<stem>.apk
    feature/<stem>/README.md
    feature/<stem>/guide_features.json
    feature/<stem>/ground_truth.json
    feature/<stem>/credential.txt
    scripts/                  helper CLIs
    output/<stem>/            generated runs (-o)
"""

import json
import os
import re

# Old APK filenames still resolve to the canonical stem under apks/.
APK_ALIASES = {
    "final": "spotube",
    "spotube-android-all-arch": "spotube",
}

# Old -o folder names still resolve under output/<app>/.
OUTPUT_ALIASES = {
    "outputdir-money": os.path.join("output", "money"),
    "outputdir-spotube": os.path.join("output", "spotube"),
    "outputdir-spotube2": os.path.join("output", "spotube"),
    "outputdir": os.path.join("output", "spotube"),
    "outputdir-features": os.path.join("output", "archive", "spotube-features"),
    "output_dir": os.path.join("output", "archive", "legacy"),
}

_CREDENTIAL_NAMES = ("credential.txt", "credentials.txt")
_README_NAMES = ("README.md", "readme.md", "notes.md", "notes.txt", "spec.md", "spec.txt")


def apk_stem(apk_path):
    """Canonical folder name for an APK (lowercase, aliases applied)."""
    name = os.path.splitext(os.path.basename(apk_path or ""))[0]
    if not name:
        return ""
    return APK_ALIASES.get(name.lower(), name.lower())


def resolve_apk_path(apk_path, cwd=None):
    """Resolve `-a` to a real APK file.

    Accepts a full path, `apks/<stem>.apk`, `<stem>.apk`, or just `<stem>`.
    """
    if not apk_path:
        return apk_path
    root = cwd or os.getcwd()
    if os.path.isfile(apk_path):
        return os.path.abspath(apk_path)
    joined = os.path.join(root, apk_path)
    if os.path.isfile(joined):
        return os.path.abspath(joined)
    stem = apk_stem(apk_path)
    raw_stem = os.path.splitext(os.path.basename(apk_path))[0]
    names = []
    for candidate in (stem, raw_stem, os.path.basename(apk_path)):
        if not candidate:
            continue
        names.append(candidate if candidate.lower().endswith(".apk") else candidate + ".apk")
    seen = set()
    for name in names:
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)
        for folder in (os.path.join(root, "apks"), root):
            path = os.path.join(folder, name)
            if os.path.isfile(path):
                return os.path.abspath(path)
    return os.path.abspath(joined)


def resolve_output_dir(output_dir, apk_path=None, cwd=None):
    """Map -o to output/<stem>/, including old outputDir-* names."""
    root = cwd or os.getcwd()
    if not output_dir:
        stem = apk_stem(apk_path) or "run"
        return os.path.join("output", stem)
    key = os.path.basename(str(output_dir).rstrip("/").rstrip("\\")).lower()
    alias = OUTPUT_ALIASES.get(key)
    if alias:
        return alias
    if os.path.isabs(output_dir):
        return output_dir
    joined = os.path.join(root, output_dir)
    # If the caller already passed output/money, keep the relative form.
    if os.path.isdir(joined) or output_dir.startswith("output"):
        return output_dir
    return output_dir


def feature_app_dir(apk_path=None, cwd=None):
    stem = apk_stem(apk_path)
    if not stem:
        return None
    return os.path.join(cwd or os.getcwd(), "feature", stem)


def _nonempty_file(path):
    return os.path.isfile(path) and os.path.getsize(path) > 0


def discover_readme(apk_path=None, cwd=None):
    root = cwd or os.getcwd()
    stem = apk_stem(apk_path)
    candidates = []
    if stem:
        app_dir = os.path.join(root, "feature", stem)
        for name in _README_NAMES:
            candidates.append(os.path.join(app_dir, name))
        candidates.append(os.path.join(app_dir, stem + ".md"))
        candidates.append(os.path.join(app_dir, stem + ".txt"))
        for ext in (".md", ".txt"):
            candidates.append(os.path.join(root, "feature", stem + ext))
            candidates.append(os.path.join(root, "features", stem + ext))
            candidates.append(os.path.join(root, "features", stem, "README.md"))
    for path in candidates:
        if _nonempty_file(path):
            return os.path.abspath(path)
    return None


def discover_credentials(apk_path=None, readme_path=None, cwd=None):
    """Per-app credentials under feature/<stem>/, then droidbot/credential.txt."""
    root = cwd or os.getcwd()
    stem = apk_stem(apk_path)
    if not stem and readme_path:
        parent = os.path.basename(os.path.dirname(os.path.abspath(readme_path)))
        if parent and parent.lower() not in ("feature", "features"):
            stem = parent.lower()
    candidates = []
    if stem:
        for name in _CREDENTIAL_NAMES:
            candidates.append(os.path.join(root, "feature", stem, name))
    if readme_path:
        folder = os.path.dirname(os.path.abspath(readme_path))
        for name in _CREDENTIAL_NAMES:
            candidates.append(os.path.join(folder, name))
    package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    candidates.append(os.path.join(package_dir, "credential.txt"))
    seen = set()
    for path in candidates:
        abspath = os.path.abspath(path)
        if abspath in seen:
            continue
        seen.add(abspath)
        if os.path.isfile(abspath):
            return abspath
    return None


def discover_context_module(apk_path=None, cwd=None):
    stem = apk_stem(apk_path)
    if not stem:
        return None
    path = os.path.join(cwd or os.getcwd(), "feature", stem, "context_functions.py")
    if os.path.isfile(path):
        return os.path.abspath(path)
    return None


def discover_ground_truth(apk_path=None, cwd=None):
    stem = apk_stem(apk_path)
    if not stem:
        return None
    path = os.path.join(cwd or os.getcwd(), "feature", stem, "ground_truth.json")
    if os.path.isfile(path):
        return os.path.abspath(path)
    return None


def discover_guide_features(apk_path=None, cwd=None):
    from .guide import discover_guide_features as _discover
    return _discover(apk_path=apk_path, cwd=cwd)


def extra_spec_texts(readme_path=None, cwd=None):
    """Load extra notes from the same app folder only (not every app under feature/)."""
    texts = []
    folders = []
    if readme_path:
        folders.append(os.path.dirname(os.path.abspath(readme_path)))
    seen = set()
    if readme_path:
        seen.add(os.path.abspath(readme_path))
    for folder in folders:
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            lower = name.lower()
            if not (lower.endswith(".txt") or lower.endswith(".md")):
                continue
            if lower in ("readme.md", "credential.txt", "credentials.txt"):
                continue
            if "credential" in lower:
                continue
            path = os.path.abspath(os.path.join(folder, name))
            if path in seen:
                continue
            seen.add(path)
            try:
                with open(path, "r", encoding="utf-8") as handle:
                    body = handle.read().strip()
                if body:
                    texts.append((path, body))
            except Exception:
                continue
    return texts


def apply_run_paths(opts, cwd=None):
    """Resolve apk / README / credentials on parsed CLI options.

    Returns False if the APK cannot be found.
    """
    opts.apk_path = resolve_apk_path(opts.apk_path, cwd)
    if not os.path.isfile(opts.apk_path):
        return False
    if not getattr(opts, "readme_path", None) or not os.path.isfile(
        opts.readme_path if os.path.isabs(opts.readme_path)
        else os.path.join(cwd or os.getcwd(), opts.readme_path)
    ):
        found = discover_readme(opts.apk_path, cwd)
        if found:
            if getattr(opts, "readme_path", None) and opts.readme_path != found:
                print("README not found at %s; using %s" % (opts.readme_path, found))
            opts.readme_path = found
    opts.output_dir = resolve_output_dir(
        getattr(opts, "output_dir", None),
        opts.apk_path,
        cwd,
    )
    if not getattr(opts, "credential_path", None):
        found = discover_credentials(
            opts.apk_path,
            getattr(opts, "readme_path", None),
            cwd,
        )
        if found:
            opts.credential_path = found
    if not getattr(opts, "ground_truth_path", None):
        found = discover_ground_truth(opts.apk_path, cwd)
        if found:
            opts.ground_truth_path = found
    if not getattr(opts, "guide_features_path", None):
        found = discover_guide_features(opts.apk_path, cwd)
        if found:
            opts.guide_features_path = found
    redirect_eval_only_feature_list(opts)
    if not getattr(opts, "context_module_path", None):
        found = discover_context_module(opts.apk_path, cwd)
        if found:
            opts.context_module_path = found
    return True


def is_eval_only_feature_list(path, payload=None):
    """True if this JSON is a coverage gold list, not a live exploration script.

    Hand-authored ground_truth.json / feature/<app>/features.json must never
    become remaining_actions for the live policy.
    """
    if not path:
        return False
    abspath = os.path.abspath(path)
    name = os.path.basename(abspath).lower()
    parts = [part.lower() for part in abspath.replace("\\", "/").split("/")]
    if "ground_truth.json" in name:
        return True
    if name == "guide_features.json":
        return False
    if "addendum" in name:
        return True
    if name == "features.json" and "feature" in parts and "feature_test" not in parts:
        return True
    if payload is None and os.path.isfile(abspath):
        try:
            with open(abspath, "r", encoding="utf-8") as handle:
                payload = json.load(handle)
        except Exception:
            return False
    if not isinstance(payload, dict):
        return False
    source = (payload.get("source") or "").lower()
    if source in ("manual_exploration", "ground_truth"):
        return True
    if "GT" in str(payload.get("id_scheme") or ""):
        return True
    features = payload.get("features") or []
    if features and str((features[0] or {}).get("id") or "").upper().startswith("GT"):
        return True
    return False


def redirect_eval_only_feature_list(opts):
    """If -features points at a gold list, keep it for offline eval only.

    Live exploration is driven by guide_features.json when present, then by a
    non-gold -features JSON, then by README extraction.
    """
    path = getattr(opts, "features_path", None)
    if not path:
        return opts
    resolved = path
    if os.path.isfile(resolved):
        resolved = os.path.abspath(resolved)
    if not is_eval_only_feature_list(resolved if os.path.isfile(resolved) else path):
        return opts
    print(
        "WARNING: -features %s is a coverage gold list and will not guide "
        "live exploration. Use feature/<app>/guide_features.json (or a "
        "non-gold JSON) to drive taps." % path
    )
    if not getattr(opts, "ground_truth_path", None) and os.path.isfile(resolved):
        opts.ground_truth_path = resolved
    elif not getattr(opts, "ground_truth_path", None):
        opts.ground_truth_path = path
    opts.features_path = None
    return opts


def parse_numbered_features(text, app_name=None):
    """Parse a manual exploration list (1. Title / steps) if that is what we were given."""
    if not text:
        return None
    pattern = re.compile(
        r"^\s*(?:#{1,3}\s*)?(\d{1,2})[\.\)]\s+(.+)$",
        re.MULTILINE,
    )
    matches = list(pattern.finditer(text))
    if len(matches) < 3:
        return None
    numbers = [int(match.group(1)) for match in matches]
    if numbers.count(1) > max(2, len(numbers) * 0.4):
        # Credits/dependency lists often restart at "1." on every line.
        return None
    features = []
    for index, match in enumerate(matches):
        title = re.sub(r"\s+", " ", match.group(2)).strip(" -:")
        title = re.sub(r"https?://\S+", "", title).strip()
        if len(title) < 4 or title.startswith("["):
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        actions = _actions_from_block(title, body)
        features.append({
            "id": "F%03d" % (len(features) + 1),
            "name": title[:90],
            "description": _first_sentence(body) or title,
            "actions": actions,
            "valid_paths": [],
            "keywords": _keywords(title),
            "nav_hints": _nav_hints(title, " ".join(actions)),
        })
    if len(features) < 3:
        return None
    gui = []
    for item in features:
        blob = " ".join(item.get("actions") or []).lower() + " " + (item.get("name") or "").lower()
        if any(token in blob for token in (
            "tap", "enter", "select", "open", "long-press", "long press",
            "toggle", "save", "create", "add ", "go to",
        )):
            gui.append(item)
    if len(gui) < 3:
        return None
    for index, item in enumerate(gui[:25], start=1):
        item["id"] = "F%03d" % index
    return {
        "app": app_name or "unknown",
        "source": "numbered_spec",
        "features": gui[:25],
    }


def _actions_from_block(title, body):
    lines = []
    for raw in (body or "").splitlines():
        stripped = raw.strip()
        if not stripped:
            continue
        stripped = re.sub(r"^[\-\*]+\s*", "", stripped)
        if stripped.lower().startswith("http"):
            continue
        if len(stripped) < 8:
            continue
        lines.append(stripped.rstrip("."))
        if len(lines) >= 8:
            break
    if not lines:
        return [
            "Navigate to the screen for: %s" % title,
            "Perform the primary action",
            "Confirm a visible result",
        ]
    # Prefer imperative lines (tap/enter/select/go) when present.
    imperative = [
        line for line in lines
        if re.match(
            r"^(tap|enter|select|open|go|long-press|long press|type|toggle|set|create|add|save|confirm|grant|swipe|drag)",
            line,
            re.IGNORECASE,
        )
    ]
    return (imperative or lines)[:8]


def _first_sentence(body):
    text = " ".join((body or "").split())
    if not text:
        return ""
    return text.split(". ")[0][:240]


def _keywords(title):
    words = re.findall(r"[a-zA-Z]{3,}", (title or "").lower())
    stop = {
        "the", "and", "for", "with", "from", "into", "view", "manage",
        "change", "open", "new",
    }
    return [word for word in words if word not in stop][:8]


def _nav_hints(title, blob):
    text = ("%s %s" % (title, blob)).lower()
    hints = []
    mapping = (
        ("search", "search"),
        ("library", "library"),
        ("settings", "settings"),
        ("home", "home"),
        ("login", "log in"),
        ("guest", "skip"),
        ("playlist", "playlist"),
        ("download", "download"),
        ("lyric", "lyrics"),
        ("account", "account"),
        ("budget", "budget"),
        ("report", "report"),
        ("payee", "payee"),
        ("categor", "category"),
        ("plugin", "plugin"),
        ("drawer", "menu"),
    )
    for needle, hint in mapping:
        if needle in text and hint not in hints:
            hints.append(hint)
    return hints
