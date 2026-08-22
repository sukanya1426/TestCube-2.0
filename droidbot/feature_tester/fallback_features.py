"""Build a testable feature list from a README or spec text without an LLM.

A feature is a finite ordered sequence of user operations where (a) each
operation is necessary — removing it changes or breaks the outcome, and
(b) the sequence ends in a visibly different, checkable app state.
Do not bundle multiple distinct outcomes or toggles into one feature just
because they live on the same screen.
"""

import re

from .specs import parse_numbered_features


NON_UI_PATTERNS = (
    "telemetry",
    "diagnostics",
    "open source",
    "libre software",
    "cross-platform",
    "small size",
    "less data",
    "native performance",
    "copyright",
    "license",
    "building from source",
    "installation guide",
    "nightly",
    "electron",
    "hackernews",
)


# Phrase → GUI walk. Matched against the README/spec, not a specific APK.
CAPABILITIES = (
    (
        ("create database", "first-time setup", ".mmb", "open database", "same database", "database used"),
        "Create or open a database",
        [
            "Tap Create Database or Open Database",
            "Enter a file name if asked",
            "Skip or set a password if asked",
            "Tap Next or Create",
        ],
        ["database", "create", "setup"],
        ["create database", "next"],
    ),
    (
        ("continue as guest", "skip login", "guest"),
        "Continue as guest or skip login",
        [
            "Tap Skip, Continue as Guest, or an equivalent first-run skip",
            "Reach the main app screen",
        ],
        ["guest", "skip"],
        ["skip", "guest"],
    ),
    (
        ("log in", "login", "sign in", "oauth", "spotify login"),
        "Log in",
        [
            "Tap Log in or Sign in",
            "Enter username or email",
            "Enter password",
            "Tap Log In and grant permission if asked",
        ],
        ["login", "password", "email"],
        ["log in", "sign in"],
    ),
    (
        ("search", "find music", "find transaction"),
        "Search",
        [
            "Tap Search",
            "Type a query",
            "Open a result",
        ],
        ["search", "query"],
        ["search"],
    ),
    (
        ("add account", "create account", "new account"),
        "Create an account",
        [
            "Tap Add Account or plus",
            "Enter a name",
            "Select type or currency if shown",
            "Tap Save",
        ],
        ["account", "add"],
        ["account", "add"],
    ),
    (
        ("add a transaction", "add transaction", "new transaction"),
        "Add a transaction",
        [
            "Tap Add Transaction or plus",
            "Enter an amount",
            "Select payee or category if shown",
            "Tap Ok or Save",
        ],
        ["transaction", "amount"],
        ["add", "transaction"],
    ),
    (
        ("budget",),
        "Set up a budget",
        [
            "Open Budget",
            "Tap plus or Add Budget",
            "Enter year or month if asked",
            "Tap Save",
        ],
        ["budget"],
        ["budget"],
    ),
    (
        ("playlist",),
        "Create or open a playlist",
        [
            "Open Library or Playlists",
            "Create or open a playlist",
            "Add or view a track",
        ],
        ["playlist"],
        ["library", "playlist"],
    ),
    (
        ("download", "offline"),
        "Download for offline use",
        [
            "Find an item",
            "Tap Download",
            "Confirm download UI or progress",
        ],
        ["download", "offline"],
        ["download"],
    ),
    (
        ("lyric", "lyrics"),
        "View lyrics",
        [
            "Play an item",
            "Open the now-playing screen",
            "Open lyrics",
        ],
        ["lyrics"],
        ["lyrics", "player"],
    ),
    (
        ("playback", "play a track", "play/pause"),
        "Playback controls",
        [
            "Select a playable item",
            "Tap play",
            "Use pause, next, or previous",
        ],
        ["play", "pause"],
        ["play", "player"],
    ),
    (
        ("plugin", "metadata provider"),
        "Install or browse plugins",
        [
            "Open Settings or Plugins",
            "Open the plugin list",
            "Select or inspect a plugin",
        ],
        ["plugin"],
        ["settings", "plugin"],
    ),
    (
        ("payee",),
        "Manage payees",
        [
            "Open Payees or the payee field",
            "Add or select a payee",
            "Save if creating one",
        ],
        ["payee"],
        ["payee"],
    ),
    (
        ("categor",),
        "Manage categories",
        [
            "Open Categories or the category field",
            "Add or select a category",
            "Save if creating one",
        ],
        ["category"],
        ["category"],
    ),
    (
        ("report", "reports", "cash-flow"),
        "View a report",
        [
            "Open Reports",
            "Tap a report type",
            "Confirm the report is visible",
        ],
        ["report"],
        ["report"],
    ),
    (
        ("import", "export", "qif", "csv"),
        "Import or export data",
        [
            "Open Settings or account options",
            "Tap Import or Export",
            "Confirm the picker or result",
        ],
        ["import", "export"],
        ["settings", "import"],
    ),
    (
        ("settings", "theme", "language"),
        "Change app settings",
        [
            "Open Settings",
            "Open a settings category",
            "Toggle or select an option",
        ],
        ["settings"],
        ["settings"],
    ),
)


def extract_features_locally(readme_text, app_name=None, allow_numbered_spec=True):
    """Turn a README or exploration notes into a GUI feature list."""
    if allow_numbered_spec:
        numbered = parse_numbered_features(readme_text, app_name=app_name)
        if numbered and numbered.get("features"):
            return numbered

    app = app_name or _guess_app_name(readme_text) or "unknown"
    blob = _capability_blob(readme_text)
    features = []
    seen = set()

    def _add(item, topic=None):
        key = topic or item["name"].lower()
        if key in seen:
            return
        seen.add(key)
        record = dict(item)
        record["id"] = "F%03d" % (len(features) + 1)
        features.append(record)

    _add({
        "name": "Complete first-run setup",
        "description": "Pass welcome, skip/login, or create-database screens and reach the main UI.",
        "actions": [
            "Close or skip the tutorial",
            "Leave any first-run analytics or settings screen",
            "Tap Create Database or Open Database if shown",
            "Enter a file name if asked and confirm Save",
            "Reach the home or main screen",
        ],
        "valid_paths": [],
        "keywords": ["onboarding", "get started", "skip", "database", "home"],
        "nav_hints": ["skip", "create database", "next"],
    }, topic="onboarding")

    for needles, name, actions, keywords, hints in CAPABILITIES:
        if any(_phrase_in(blob, needle) for needle in needles):
            _add({
                "name": name,
                "description": "Exercise the '%s' capability described in the app documentation." % name,
                "actions": list(actions),
                "valid_paths": [],
                "keywords": list(keywords),
                "nav_hints": list(hints),
            }, topic=name.lower())

    for name, description in _bullets_from_features_section(readme_text):
        if _looks_non_ui(name, description) or name.lstrip().startswith("["):
            continue
        topic = name.lower()[:40]
        _add(_feature_from_bullet(name, description), topic=topic)

    names = " ".join(item["name"].lower() for item in features)
    if any(token in names for token in ("playlist", "download for offline", "transaction", "account")):
        _add({
            "name": "Search",
            "description": "Open search, type a query, and open a result.",
            "actions": [
                "Tap Search",
                "Type a query",
                "Open a result",
            ],
            "valid_paths": [],
            "keywords": ["search", "query"],
            "nav_hints": ["search"],
        }, topic="search")

    return {"app": app, "source": "local_readme", "features": features[:20]}


def _phrase_in(blob, needle):
    if " " in needle or len(needle) >= 8:
        return needle in (blob or "")
    return re.search(r"\b%s\b" % re.escape(needle), blob or "") is not None


def _capability_blob(readme_text):
    text = readme_text or ""
    skip_headings = (
        "build", "contributing", "continuous integration", "license",
        "badges", "star history", "translate", "documentation", "download",
    )
    kept = []
    skipping = False
    for line in text.splitlines():
        heading = re.match(r"^#{1,6}\s+(.+)$", line)
        if heading:
            title = heading.group(1).strip().lower()
            skipping = any(title.startswith(name) for name in skip_headings)
        if skipping:
            continue
        kept.append(line)
    blob = "\n".join(kept).lower()
    section = re.search(
        r"^#{1,3}\s*.*feature.*$",
        text,
        re.IGNORECASE | re.MULTILINE,
    )
    body = ""
    if section:
        rest = text[section.end():]
        nxt = re.search(r"^#{1,3}\s+\S+", rest, re.MULTILINE)
        body = rest[: nxt.start()] if nxt else rest[:2000]
    return ("%s\n%s" % (blob, body)).lower()


def _guess_app_name(readme_text):
    for line in (readme_text or "").splitlines()[:40]:
        stripped = line.strip().lstrip("#").strip()
        if stripped and len(stripped.split()) <= 4 and "http" not in stripped.lower():
            if stripped.lower() not in ("features", "about", "installation"):
                return stripped
    return None


def _bullets_from_features_section(readme_text):
    text = readme_text or ""
    section = re.search(
        r"^#{1,6}\s*.*\bfeatures?\b.*$",
        text,
        re.IGNORECASE | re.MULTILINE,
    )
    if not section:
        return []
    body = text[section.end():]
    next_heading = re.search(r"^#{1,6}\s+\S+", body, re.MULTILINE)
    if next_heading:
        body = body[: next_heading.start()]
    bullets = []
    for raw in re.findall(r"^[\-\*]\s+(.+)$", body, re.MULTILINE):
        cleaned = re.sub(r"<[^>]+>", "", raw)
        cleaned = re.sub(r"[^\w\s/&.,'+-]", "", cleaned)
        cleaned = " ".join(cleaned.split()).strip()
        if len(cleaned) < 8:
            continue
        bullets.append((cleaned.split(".")[0][:80], cleaned))
        if len(bullets) >= 16:
            break
    return bullets


def _looks_non_ui(name, description):
    blob = ("%s %s" % (name, description)).lower()
    return any(token in blob for token in NON_UI_PATTERNS)


def _feature_from_bullet(name, description):
    keywords = [word for word in re.findall(r"[a-zA-Z]{3,}", name.lower())][:8]
    return {
        "name": name,
        "description": description,
        "actions": _actions_for(name, description),
        "valid_paths": [],
        "keywords": keywords,
        "nav_hints": _hints_for(name, description),
    }


def _actions_for(name, description):
    blob = ("%s %s" % (name, description)).lower()
    for needles, _title, actions, _keys, _hints in CAPABILITIES:
        if any(needle in blob for needle in needles):
            return list(actions)
    return [
        "Navigate to the relevant screen",
        "Perform the primary action for: %s" % name,
        "Confirm the feature produced a visible result",
    ]


def _hints_for(name, description):
    blob = ("%s %s" % (name, description)).lower()
    for needles, _title, _actions, _keys, hints in CAPABILITIES:
        if any(needle in blob for needle in needles):
            return list(hints)
    return []
