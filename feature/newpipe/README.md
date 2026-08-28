# NewPipe

A libre lightweight streaming front-end for Android. NewPipe plays YouTube and
other services without the official app, without ads, and without requiring a
Google account or any sign-in. Content is fetched by parsing the site directly,
so every feature below is reachable immediately on first launch.

- Package: `org.schabi.newpipe`
- F-Droid: https://f-droid.org/en/packages/org.schabi.newpipe/
- Source: https://github.com/TeamNewPipe/NewPipe

## User-facing capabilities

Scoped to what works on the version under test (see the limitation below).

- Browse the What's New feed on the main page
- Search for videos, channels and playlists; clear a query; re-run one from history
- Filter search results by type (videos, channels, playlists)
- Open Subscriptions and Bookmarked Playlists from the navigation drawer
- Review watch history, and the Downloads list
- Change settings: Appearance/theme, Video and audio, Download, Content,
  History and cache, Notifications, Backup and restore
- Read the About & FAQ screen

## Version limitation (important)

`apks/newpipe.apk` is **0.27.0**, and its bundled YouTube extractor is now out of
date. Two endpoints fail with `Could not parse website`:

- **Trending kiosk** (`youtube.com/feed/trending`) — the tab never loads
- **Stream resolution** (`youtube.com/watch?v=...`) — video pages fail to open

Search still parses correctly, so search, the drawer destinations and all settings
screens are exercisable. **Every video-playback feature is excluded from both
`guide_features.json` and `ground_truth.json`** — including playback controls,
background/popup players, the play queue, downloads of a stream, channels,
subscribing, comments, related videos and sharing. Scoring them would have
produced false negatives that say nothing about either tool.

NewPipe **0.29.1** (kept at `apks/newpipe-0.29.1.apk`) fixes all of this — Trending
and playback both work — but it **cannot be instrumented**: AndroLog/Soot dies with
`DexPrinterException ... castPrimitive` on it, the same failure spotube hits. So the
instrumentable version and the fully-working version are unfortunately disjoint.

## Notes for testing

- No login is required. There is no account, so `credential.txt` only supplies a
  search query and a playlist name.
- Search needs network access. Without it the results screen shows "Sorry,
  something went wrong" and most remaining features cannot be exercised either.
- Subscriptions and Bookmarked Playlists start empty and stay empty, since
  subscribing requires a channel page (which needs stream resolution).
