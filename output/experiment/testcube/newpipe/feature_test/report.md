# Feature test report: NewPipe

- Started: 2026-09-24 22:22:03
- Finished: 2026-09-24 22:48:46
- Features: 18
- Covered: 10
- Partial: 8
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 71% (mean completion ratio; the headline number)
- Coverage: 56% (features with every guide step matched)
- Stop reason: all_features_done
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 18
- Never attempted: 0
- Blocked then recovered on retry: 0
- Blocked still: 0

## Guide vs README-extracted

- Guide features: 18
- README-extracted features: 7
- In both: 1
- Guide-only: 17
- README-only: 6
  - guide-only: F001 Browse What's New
  - guide-only: F003 Filter search results
  - guide-only: F004 Downloads list
  - guide-only: F005 Subscriptions tab
  - guide-only: F006 Bookmarked playlists
  - guide-only: F007 Watch history
  - guide-only: F008 Open settings
  - guide-only: F009 Change appearance
  - guide-only: F010 Video and audio settings
  - guide-only: F011 About NewPipe
  - guide-only: F012 Content settings
  - guide-only: F013 Download settings
  - README-only: F001 Complete first-run setup
  - README-only: F002 Log in
  - README-only: F004 Create or open a playlist
  - README-only: F005 Download for offline use
  - README-only: F006 Playback controls
  - README-only: F007 Change app settings

## Text-field resolution

- Filled via credential.txt: 5
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 56% (10/18) — live journal self-report (covered / extracted features).
- Offline coverage: 18% (3 covered / 17; 4 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 24% (mean completion ratio).

## Findings

### F001 Browse What's New

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the What's New tab
- Completion ratio: 1.00
- Actions taken: 4
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=831be133abb43ba384e7e7b9b3457508(MainActivity/Button-RETRY)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=831be133abb43ba384e7e7b9b3457508(MainActivity/Button-RETRY)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=abc35bf55e3357bfd219f8ddffb67cdd(MainActivity/LinearLayout-)) (heuristic)

### F002 Search

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap Search; Type a query; Submit the search
- Completion ratio: 1.00
- Actions taken: 6
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=278c7ffcf1444b33d7d05b5cebcd167c, view=9f1e9d5955e6cba81431ba8fd2921d11(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (rule)
  - act: CustomSetTextEvent(state=278c7ffcf1444b33d7d05b5cebcd167c, view=932c754fd3b9b0a75419c3854d74dbf5(MainActivity/EditText-Search), text=lofi hip hop) (mandatory_fill)
  - act: CustomTouchEvent(state=0c509ffe810951ef99b3bc348b6634ba, view=9f1e9d5955e6cba81431ba8fd2921d11(MainActivity/ImageView-)) (heuristic)

### F003 Filter search results

- Status: **covered**
- Reason: Covered by shared-flow reuse of C002.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Run a search; Open the filter menu; Pick a filter
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=278c7ffcf1444b33d7d05b5cebcd167c, view=9f1e9d5955e6cba81431ba8fd2921d11(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (heuristic)

### F004 Downloads list

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the drawer; Tap Downloads
- Completion ratio: 1.00
- Actions taken: 7
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=86a81684bc351334383b55d29a587293, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=f5f0c9a422a963c0cc6da5d08c55b8f5, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=2477ab7465e65dbc141797b7866b316c, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=f5f0c9a422a963c0cc6da5d08c55b8f5, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=2477ab7465e65dbc141797b7866b316c, view=fa5e57f1d26e38afed22ce601730bd4c(MainActivity/CheckedTextView-Downloads)) (rule)
  - act: CustomTouchEvent(state=e4bcd6fd202fbb01d060f0469307473f, view=b44ccbf1cc7e200ed4f94d1acb6b29bb(DownloadActivity/TextView-Downloads)) (heuristic)

### F005 Subscriptions tab

- Status: **covered**
- Reason: Covered by shared-flow reuse of C001.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the drawer; Tap Subscriptions
- Completion ratio: 1.00
- Actions taken: 5
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=86a81684bc351334383b55d29a587293, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=f5f0c9a422a963c0cc6da5d08c55b8f5, view=831be133abb43ba384e7e7b9b3457508(MainActivity/Button-RETRY)) (rule)
  - act: CustomTouchEvent(state=f5f0c9a422a963c0cc6da5d08c55b8f5, view=831be133abb43ba384e7e7b9b3457508(MainActivity/Button-RETRY)) (rule)
  - act: CustomTouchEvent(state=f5f0c9a422a963c0cc6da5d08c55b8f5, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)

### F006 Bookmarked playlists

- Status: **covered**
- Reason: The current screen shows the 'Bookmarked Playlists' section, which is the final step in the feature completion. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the drawer; Tap Bookmarked Playlists
- Completion ratio: 1.00
- Credited from later features: F008
- Actions taken: 8
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=f03a4827af5407f9487e4bb799b6a030(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=f03a4827af5407f9487e4bb799b6a030(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=abc35bf55e3357bfd219f8ddffb67cdd(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=dca01089ff41fa943b32d2624fc2292a, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=3a40574addde41666bcfe896b181a3c9(MainActivity/TextView-Bookmarked)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=3a40574addde41666bcfe896b181a3c9(MainActivity/TextView-Bookmarked)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=ca369ec4c0dfac50311c0a48f202ff64, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (rule)

### F007 Watch history

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the back button to return to the main screen; Tap the drawer icon in the top-left corner of the screen; Scroll down to find and tap the 'History' option in the drawer
- Remaining steps: Wait for the watch history to load and verify the list of watched videos; Tap on a video in the watch history to play it
- Completion ratio: 0.60
- Credited from later features: F004
- Actions taken: 12
  - act: CustomTouchEvent(state=ca369ec4c0dfac50311c0a48f202ff64, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=d78a50973dd2bd95a8b8caac2c8ac3d1(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=1b2316909654001a5a84ae7acccc3c81(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=17f41017c3c70346c6ee7cfdef983366, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (rule)
  - act: CustomSetTextEvent(state=278c7ffcf1444b33d7d05b5cebcd167c, view=932c754fd3b9b0a75419c3854d74dbf5(MainActivity/EditText-Search), text=lofi hip hop) (nav)
  - act: CustomSetTextEvent(state=0c509ffe810951ef99b3bc348b6634ba, view=f300f7aeffae8382d529412cf737b7f1(MainActivity/EditText-lofi hip h), text=lofi hip hop) (nav)
  - act: CustomSetTextEvent(state=0c509ffe810951ef99b3bc348b6634ba, view=f300f7aeffae8382d529412cf737b7f1(MainActivity/EditText-lofi hip h), text=lofi hip hop) (nav)
  - act: CustomTouchEvent(state=0c509ffe810951ef99b3bc348b6634ba, view=01e4c4fe03d90501923c5beaa3c501fd(MainActivity/RecyclerView-)) (rule)

### F008 Open settings

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the drawer; Tap Settings
- Completion ratio: 1.00
- Credited from later features: F004, F016
- Actions taken: 5
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=1b2316909654001a5a84ae7acccc3c81(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=17f41017c3c70346c6ee7cfdef983366, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=1ce4c3cd0f1456a83ca943667cf9fdb4, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=7c3e1d89d6bbc71e3a91da9924602656, view=ce40e8ecbef01fa0d51d1d35551461e8(MainActivity/TextView-Playlists)) (heuristic)
  - act: CustomTouchEvent(state=1ce4c3cd0f1456a83ca943667cf9fdb4, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)

### F009 Change appearance

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open Settings
- Remaining steps: Tap Appearance; Pick a theme
- Completion ratio: 0.33
- Credited from later features: F004
- Actions taken: 3
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=99adbef69a7899a08ac9a93c840d9480(MainActivity/Button-REPORT)) (heuristic)
  - act: CustomTouchEvent(state=35e4b8f5c1e329f84a73330a397b20d3, view=46ee0284c8b6b00b08c5650affd829b4(ErrorActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=99adbef69a7899a08ac9a93c840d9480(MainActivity/Button-REPORT)) (heuristic)

### F010 Video and audio settings

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open Settings
- Remaining steps: Tap Video and audio; Change a preference
- Completion ratio: 0.33
- Credited from later features: F004
- Actions taken: 8
  - act: ScrollEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=b282ac7adceb918287824e22061035c4(MainActivity/ViewPager-), direction=up) (heuristic)
  - act: ScrollEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=b282ac7adceb918287824e22061035c4(MainActivity/ViewPager-), direction=up) (heuristic)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=5125b0ef3fc97b7a8ccc5331fb40c56a(MainActivity/TextView-Trending)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=5125b0ef3fc97b7a8ccc5331fb40c56a(MainActivity/TextView-Trending)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=78113e45284d57e6a58eba3d82085017(MainActivity/Button-OPEN IN BR)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=78113e45284d57e6a58eba3d82085017(MainActivity/Button-OPEN IN BR)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=6bac928563da9b08f96c2afcc4835f7f(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)

### F011 About NewPipe

- Status: **covered**
- Reason: Covered by shared-flow reuse of C004.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the drawer; Scroll down to the 'About & FAQ' section; Tap 'About & FAQ'; Read the About & FAQ screen
- Completion ratio: 1.00
- Actions taken: 5
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=6bac928563da9b08f96c2afcc4835f7f(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=0ad19e889ec0c0419cc8036b2e159ce2(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=dca01089ff41fa943b32d2624fc2292a, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=262e7591a8865c5911c9505e3d59bc32, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=c1fa35ba52b8e915e8e7d3e6e4d96666, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)

### F012 Content settings

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open Settings
- Remaining steps: Tap Content; Change a preference
- Completion ratio: 0.33
- Actions taken: 10
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=2b88735a97c692937b8a484580921fd9, view=66cf5b867ce5c2ac3ecca7c87da649ec(MainActivity/TextView-Do you thi)) (heuristic)
  - act: CustomTouchEvent(state=2b88735a97c692937b8a484580921fd9, view=66cf5b867ce5c2ac3ecca7c87da649ec(MainActivity/TextView-Do you thi)) (heuristic)
  - act: CustomTouchEvent(state=2b88735a97c692937b8a484580921fd9, view=6337a738be96648f84bb3dfecd4bb6ba(MainActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=dca01089ff41fa943b32d2624fc2292a, view=d52076366ad91b49823bc125bf5d3f05(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=4492094f04df051be30763eedb33f8d4, x=789, y=665) (llm)
  - act: CustomTouchEvent(state=4492094f04df051be30763eedb33f8d4, view=6337a738be96648f84bb3dfecd4bb6ba(MainActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=dca01089ff41fa943b32d2624fc2292a, view=d52076366ad91b49823bc125bf5d3f05(MainActivity/Button-)) (heuristic)

### F013 Download settings

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open Settings
- Remaining steps: Tap Download; Change a preference
- Completion ratio: 0.33
- Credited from later features: F004
- Actions taken: 6
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=b1e54895cbffa2637b437130ced3faff(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=17f41017c3c70346c6ee7cfdef983366, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=d78a50973dd2bd95a8b8caac2c8ac3d1(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=b1e54895cbffa2637b437130ced3faff(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=17f41017c3c70346c6ee7cfdef983366, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=3a40574addde41666bcfe896b181a3c9(MainActivity/TextView-Bookmarked)) (rule)

### F014 History and cache settings

- Status: **covered**
- Reason: Covered by shared-flow reuse of C004.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open Settings; Tap History and cache; Clear a cache or history entry
- Completion ratio: 1.00
- Actions taken: 8
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=91871fc58012e93f54d2579d02fc1f38(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=abc35bf55e3357bfd219f8ddffb67cdd(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=dca01089ff41fa943b32d2624fc2292a, view=4ff54950de0ba6aba599e29fdc0f4007(MainActivity/Button-)) (heuristic)
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=2b88735a97c692937b8a484580921fd9, view=6337a738be96648f84bb3dfecd4bb6ba(MainActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=dca01089ff41fa943b32d2624fc2292a, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=262e7591a8865c5911c9505e3d59bc32, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=c1fa35ba52b8e915e8e7d3e6e4d96666, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)

### F015 Notification settings

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open Settings
- Remaining steps: Tap Notifications; Toggle a notification preference
- Completion ratio: 0.33
- Credited from later features: F004
- Actions taken: 7
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=91871fc58012e93f54d2579d02fc1f38(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=1b2316909654001a5a84ae7acccc3c81(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=17f41017c3c70346c6ee7cfdef983366, view=03176d03917e62f97206269e73b1f4b7(MainActivity/TextView-Import or )) (heuristic)
  - act: CustomTouchEvent(state=17f41017c3c70346c6ee7cfdef983366, view=03176d03917e62f97206269e73b1f4b7(MainActivity/TextView-Import or )) (heuristic)
  - act: CustomTouchEvent(state=17f41017c3c70346c6ee7cfdef983366, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=d3b5c196133d40a1a37d676f1bd24acb, view=3471e198a4262fb5b94e3380feb60edf(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=93788b5f5c3da16e06213194e41cb4bb, view=043dc24c365e850dbb9db2c24e2f61fb(MainActivity/TextView-Export to)) (rule)

### F016 Backup and restore

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Settings' option in the navigation drawer
- Remaining steps: Scroll down to find the 'Backup and restore' section; Tap on the 'Backup and restore' option; Select the 'Backup' option to initiate the backup process; Wait for the backup to complete; Tap on the 'Restore' option to initiate the restore process
- Completion ratio: 0.17
- Actions taken: 7
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=86a81684bc351334383b55d29a587293, view=831be133abb43ba384e7e7b9b3457508(MainActivity/Button-RETRY)) (rule)
  - act: CustomTouchEvent(state=cc847f5181bd76d21dc23632c419453a, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=26ca6aff39b48bf546e1bc68e2b8c956, view=5010b83fded74da4550484f401da1e41(MainActivity/TextView-Clear watc)) (rule)
  - act: CustomTouchEvent(state=be40985ce2010a47a72b7e38cf284926, view=5386f38edbc95dcaab75e0806af7b358(MainActivity/Button-CANCEL)) (llm)
  - act: CustomTouchEvent(state=cc847f5181bd76d21dc23632c419453a, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=26ca6aff39b48bf546e1bc68e2b8c956, view=5010b83fded74da4550484f401da1e41(MainActivity/TextView-Clear watc)) (rule)

### F017 Search suggestion reuse

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open Search
- Remaining steps: Observe previous queries; Tap a stored query
- Completion ratio: 0.33
- Actions taken: 9
  - act: CustomTouchEvent(state=1ce4c3cd0f1456a83ca943667cf9fdb4, view=20c293b1bd0711ed263c9cf871fb97d3(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=827820f865529fb757436e015629d25d, view=9f1e9d5955e6cba81431ba8fd2921d11(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=b52c19d799a924383c013e88ecfecb1b, view=20c293b1bd0711ed263c9cf871fb97d3(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=8ba23b5a79932f692a5a79eb3e3f6d3c, view=9f1e9d5955e6cba81431ba8fd2921d11(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=d69abaf8af6c2e2547d5d62fdafbbbd9, view=20c293b1bd0711ed263c9cf871fb97d3(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=e2db7e7219387c2c00b3025a1990af06, view=9f1e9d5955e6cba81431ba8fd2921d11(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=61dda20922c8e2972ada7ce49137b4da, view=20c293b1bd0711ed263c9cf871fb97d3(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=326c64ac365f601e0661603b3b4206a7, view=702d5077aad675be22f45a8017f0bf14(MainActivity/EditText-lofi hip h)) (rule)

### F018 Clear a search

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open Search; Type a query; Tap the clear button
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=1ce4c3cd0f1456a83ca943667cf9fdb4, view=932c754fd3b9b0a75419c3854d74dbf5(MainActivity/EditText-Search), text=lofi hip hop) (mandatory_fill)
  - act: CustomTouchEvent(state=0c509ffe810951ef99b3bc348b6634ba, view=9f1e9d5955e6cba81431ba8fd2921d11(MainActivity/ImageView-)) (heuristic)

## Shared flows detected

4 reuse(s); 8 action(s) skipped by not re-executing a known terminal flow.

- `F003` reused `C002` (from F002), skipped 2 action(s)
- `F005` reused `C001` (from F001), skipped 1 action(s)
- `F011` reused `C004` (from F004), skipped 3 action(s)
- `F014` reused `C004` (from F004), skipped 2 action(s)

See `session.json` and `log.md` in this folder for the full trace.
