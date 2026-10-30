# Feature test report: Odyssey

- Started: 2026-10-26 14:59:10
- Finished: 2026-10-26 15:54:10
- Features: 14
- Covered: 8
- Partial: 6
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 72% (mean completion ratio; the headline number)
- Coverage: 57% (features with every guide step matched)
- Stop reason: all_features_done
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 14
- Never attempted: 0
- Blocked then recovered on retry: 1
- Blocked still: 1

## Guide vs README-extracted

- Guide features: 14
- README-extracted features: 10
- In both: 1
- Guide-only: 13
- README-only: 9
  - guide-only: G001 Browse the music library
  - guide-only: G002 Browse all tracks
  - guide-only: G003 Browse the file system
  - guide-only: G005 View
  - guide-only: G006 Clear the play queue
  - guide-only: G007 Browse
  - guide-only: G008 Create a bookmark
  - guide-only: G009 Delete a bookmark
  - guide-only: G010 Jump
  - guide-only: G011 Download artwork
  - guide-only: G012 Restrict artwork downloads
  - guide-only: G013 Add the Odyssey home
  - README-only: F001 Close or skip the tutorial
  - README-only: F002 Leave any first-run analytics or settings screen
  - README-only: F003 Tap Create Database or Open Database if shown
  - README-only: F004 Enter a file name if asked and confirm Save
  - README-only: F005 Reach the home or main screen
  - README-only: F006 Search
  - README-only: F007 Create or open a playlist
  - README-only: F008 Download for offline use
  - README-only: F010 Change app settings

## Text-field resolution

- Filled via credential.txt: 8
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 57% (8/14) — live journal self-report (covered / extracted features).
- Offline coverage: not computed (no ground-truth JSON).

## Findings

### G001 Browse the music library

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the 'Browse' option in the navigation menu.; Select 'Browse the music library' from the available options.; Tap on 'Browse by album' to view the music library by album.; Select an album to view its tracks.; Tap on a track to play it.
- Completion ratio: 1.00
- Actions taken: 10
  - act: CustomTouchEvent(state=00344d5a2c7460cfb817970534aa9600, view=b75288efb333fd60c4e75b29fcd825b4(OdysseyMainActivity/Button-)) (rule)
  - act: CustomSetTextEvent(state=7dd47d20c3d17df6d7f413d35da26705, view=15090521c2ce4d07e8d57d7704c5466f(OdysseyMainActivity/AutoCompleteTextView-   ), text=test) (rule)
  - act: ScrollEvent(state=313912d65e543dae4f3ee1dcfecb70a2, view=d319be7695eb593819dc249a7bc1df8a(OdysseyMainActivity/ViewPager-), direction=right) (heuristic)
  - act: CustomTouchEvent(state=313912d65e543dae4f3ee1dcfecb70a2, view=96de5988b7c1182693472a3b0e1601bc(OdysseyMainActivity/TextView-No albums )) (heuristic)
  - act: CustomTouchEvent(state=313912d65e543dae4f3ee1dcfecb70a2, view=19a6838ecf315ef7254e795fd9c9943d(OdysseyMainActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=a1742a0ed0ada3fe67257d4f89d92bf5, view=3b1444000aa4f1a2e84f8d8a0e2808a5(OdysseyMainActivity/TextView-Recent alb)) (nav)
  - act: CustomTouchEvent(state=fe92c43e091e6b7bcd8f6625ca1e5094, view=98909b06d11a45521ae327867a6bae2d(OdysseyMainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=d6f7475f13f7be6a4038031c60261822, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (heuristic)

### G002 Browse all tracks

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the "All tracks"/Tracks tab
- Remaining steps: scroll the alphabetical list
- Completion ratio: 0.50
- Actions taken: 34
  - act: CustomTouchEvent(state=3c1072197bec47f78f2a7bc5e5792c89, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (llm)
  - act: CustomTouchEvent(state=3c1072197bec47f78f2a7bc5e5792c89, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (llm)
  - act: CustomTouchEvent(state=3c1072197bec47f78f2a7bc5e5792c89, view=ea04a51ae96f207e259d0bebcb48e440(OdysseyMainActivity/TextView-Classic_Vi)) (llm)
  - act: CustomTouchEvent(state=3c1072197bec47f78f2a7bc5e5792c89, view=f9df95ac969a149a1a8ebd9525ad8b2f(OdysseyMainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=3c1072197bec47f78f2a7bc5e5792c89, view=ea04a51ae96f207e259d0bebcb48e440(OdysseyMainActivity/TextView-Classic_Vi)) (llm)
  - act: CustomTouchEvent(state=3c1072197bec47f78f2a7bc5e5792c89, view=f9df95ac969a149a1a8ebd9525ad8b2f(OdysseyMainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=3c1072197bec47f78f2a7bc5e5792c89, view=cd537eb97a3e74b9e9d9b30b78c8ed74(OdysseyMainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=3c1072197bec47f78f2a7bc5e5792c89, view=d5f6a9c8be1f26d734fdee4e91ba81bb(OdysseyMainActivity/LinearLayoutCompat-)) (rule)

### G003 Browse the file system

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the navigation drawer; tap "Files"/the file browser
- Completion ratio: 1.00
- Actions taken: 2
  - act: CustomTouchEvent(state=3c63a7f80b4fd90da55166b7fb475052, view=70bd59546c7fe154893baf8e52673220(OdysseyMainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=087bb1ba1f69dd531fc776cf891bf929, view=f39d9d23ed426a6607297a191e43e4b0(OdysseyMainActivity/CheckedTextView-Files)) (heuristic)

### G004 Control playback

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the now-playing bar at the bottom of the screen; Drag up the now-playing bar to adjust the playback controls; Release the now-playing bar to apply the new playback settings
- Completion ratio: 1.00
- Actions taken: 9
  - act: CustomTouchEvent(state=85be389a808c1c0ae350141c28dd2bdd, view=f9df95ac969a149a1a8ebd9525ad8b2f(OdysseyMainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=491b581a810efdab1c6c5d5d4b73e276, view=f9df95ac969a149a1a8ebd9525ad8b2f(OdysseyMainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=f221005a1eb555c1e54ed079638a19e1, view=f9df95ac969a149a1a8ebd9525ad8b2f(OdysseyMainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=f38ca4cf531e25b08c2a1aafe16ff7bb, view=f9df95ac969a149a1a8ebd9525ad8b2f(OdysseyMainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=44b14d4bdc7560b942d6f1b7d4c102c5, view=f9df95ac969a149a1a8ebd9525ad8b2f(OdysseyMainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=e4a8c6e0279d87340e2ec335f620a400, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (heuristic)
  - act: CustomTouchEvent(state=abc663b53e31063f6f679e59276e4d76, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (heuristic)
  - act: CustomTouchEvent(state=179c576c0f8a5ad83fcfe8475f7e364f, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (heuristic)

### G005 View

- Status: **covered**
- Reason: Covered by shared-flow reuse of C004.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the full player; switch to the queue/playlist view
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=f71549512b79c96539e2b180c90a05ba, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (heuristic)
  - act: CustomTouchEvent(state=7423e2afa0b021d4b41299ded4595b1e, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (heuristic)
  - act: CustomTouchEvent(state=877e4c40e8e1a2f61dd34e2a5a0b1580, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (heuristic)

### G006 Clear the play queue

- Status: **covered**
- Reason: Covered by shared-flow reuse of C004.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the full player or the queue view; Tap the overflow menu; Select 'Clear playlist'
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=fa410855093a35c234250786e001facf, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (heuristic)
  - act: CustomTouchEvent(state=74bdfa55146f3d2a974b1efdf3e15092, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (heuristic)
  - act: CustomTouchEvent(state=f5c31496c39339ad1dc33ee258b9f69d, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (heuristic)

### G007 Browse

- Status: **covered**
- Reason: Covered by shared-flow reuse of C004.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the 'Playlists' tab; Tap on the 'Browse' option; Select the 'Playlists' tab
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=5d0598115ce963bca526be79efced556, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (nav)
  - act: CustomTouchEvent(state=4b49da0f91d92d8e937f44fbf70ac8a3, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (nav)
  - act: CustomTouchEvent(state=3b98c72bde3b8e337f29cec84ece6e01, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (nav)

### G008 Create a bookmark

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the overflow menu
- Remaining steps: Select 'Create bookmark'; Enter the bookmark name; Tap 'Save'
- Completion ratio: 0.25
- Credited from later features: G001
- Actions taken: 31
  - act: CustomTouchEvent(state=558a74a63c1335d887c5fe5305a74c75, view=2fe7478528e8f02a4382aceed6e77b1d(OdysseyMainActivity/TextView-No bookmar)) (nav)
  - act: CustomTouchEvent(state=558a74a63c1335d887c5fe5305a74c75, view=7bb176d1140bfbd14e0d454201e93345(OdysseyMainActivity/TextView-Bookmarks)) (nav)
  - act: CustomTouchEvent(state=558a74a63c1335d887c5fe5305a74c75, view=7bb176d1140bfbd14e0d454201e93345(OdysseyMainActivity/TextView-Bookmarks)) (nav)
  - act: CustomTouchEvent(state=558a74a63c1335d887c5fe5305a74c75, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (llm)
  - act: CustomTouchEvent(state=558a74a63c1335d887c5fe5305a74c75, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (llm)
  - act: CustomTouchEvent(state=558a74a63c1335d887c5fe5305a74c75, view=ea04a51ae96f207e259d0bebcb48e440(OdysseyMainActivity/TextView-Classic_Vi)) (llm)
  - act: CustomTouchEvent(state=558a74a63c1335d887c5fe5305a74c75, view=70bd59546c7fe154893baf8e52673220(OdysseyMainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=3c1072197bec47f78f2a7bc5e5792c89, view=d5f6a9c8be1f26d734fdee4e91ba81bb(OdysseyMainActivity/LinearLayoutCompat-)) (rule)

### G009 Delete a bookmark

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Bookmarks view; long-press the bookmark
- Remaining steps: Select the delete option; Confirm the deletion; Verify the bookmark is removed
- Completion ratio: 0.40
- Credited from later features: G014, G010
- Actions taken: 26
  - act: LongTouchEvent(state=558a74a63c1335d887c5fe5305a74c75, view=62b89b63db370201ff887fea5ab0e8bf(OdysseyMainActivity/ImageButton-)) (rule)
  - act: LongTouchEvent(state=558a74a63c1335d887c5fe5305a74c75, view=62b89b63db370201ff887fea5ab0e8bf(OdysseyMainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=bd4736593178f252a9a4cf9bbeb19f1b, view=2fe7478528e8f02a4382aceed6e77b1d(OdysseyMainActivity/TextView-No bookmar)) (heuristic)
  - act: CustomTouchEvent(state=bd4736593178f252a9a4cf9bbeb19f1b, view=7bb176d1140bfbd14e0d454201e93345(OdysseyMainActivity/TextView-Bookmarks)) (heuristic)
  - act: LongTouchEvent(state=bd4736593178f252a9a4cf9bbeb19f1b, view=70bd59546c7fe154893baf8e52673220(OdysseyMainActivity/ImageButton-)) (rule)
  - act: LongTouchEvent(state=bd4736593178f252a9a4cf9bbeb19f1b, view=70bd59546c7fe154893baf8e52673220(OdysseyMainActivity/ImageButton-)) (rule)
  - act: LongTouchEvent(state=bd4736593178f252a9a4cf9bbeb19f1b, view=62b89b63db370201ff887fea5ab0e8bf(OdysseyMainActivity/ImageButton-)) (llm)
  - act: LongTouchEvent(state=bd4736593178f252a9a4cf9bbeb19f1b, view=62b89b63db370201ff887fea5ab0e8bf(OdysseyMainActivity/ImageButton-)) (rule)

### G010 Jump

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap 'Show album' in the player overflow menu; Long-press a track in the music library; Select the desired album from the list; Tap the 'Jump' button to play the album
- Completion ratio: 1.00
- Credited from later features: G014
- Actions taken: 16
  - act: CustomTouchEvent(state=7ba8dc7aab851ebd75a8f344b859f197, view=78b88b8bbe9e2e78ae28c0e8f5b4d9f1(OdysseyMainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=7ba8dc7aab851ebd75a8f344b859f197, view=764c8208bb1b685acc5a2cbc6f2aa057(OdysseyMainActivity/CheckedTextView-My Music)) (afford_search)
  - act: CustomTouchEvent(state=553bd30bf3e2223f9a3d3460a6c4407b, view=b75288efb333fd60c4e75b29fcd825b4(OdysseyMainActivity/Button-)) (rule)
  - act: CustomSetTextEvent(state=ccee6d4702a45aa0deb2fd1d104c6864, view=15090521c2ce4d07e8d57d7704c5466f(OdysseyMainActivity/AutoCompleteTextView-   ), text=test) (rule)
  - act: CustomTouchEvent(state=f5e817fed9c2294ad89bef409ac9fb26, view=ee153424de416e696e403bc2c97c940a(OdysseyMainActivity/TextView-TestCube T)) (rule)
  - act: CustomTouchEvent(state=fc72e280ff737f167baaf08ec3fac7b1, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (llm)
  - act: CustomTouchEvent(state=a1f0195bcb49edf6ca5f921d761745cf, view=51774ad88ce65fa35fbb67ac1026448b(OdysseyMainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=eb822659d8089cf551140dd0e2cbdc83, view=ef1b7346937a553aad3cfd7e98290ed3(OdysseyMainActivity/ImageButton-)) (heuristic)

### G011 Download artwork

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open Settings; the artwork section
- Completion ratio: 1.00
- Credited from later features: G002, G012
- Actions taken: 30
  - act: CustomTouchEvent(state=810aa1d0277f0d619fbd2d0cae3efd8d, view=ea04a51ae96f207e259d0bebcb48e440(OdysseyMainActivity/TextView-Classic_Vi)) (nav)
  - act: CustomTouchEvent(state=47988faabb2faf7ac7d0d889e6e7b013, view=ea04a51ae96f207e259d0bebcb48e440(OdysseyMainActivity/TextView-Classic_Vi)) (nav)
  - act: CustomTouchEvent(state=863f5427eaa2bb0b20553593129df2de, view=70bd59546c7fe154893baf8e52673220(OdysseyMainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=d59c2a2b0f8ddb88726b7b1bd73664ba, view=9e13b93d9a7f8ab32b0bf9cd1bad09ac(OdysseyMainActivity/CheckedTextView-Settings)) (nav)
  - act: CustomTouchEvent(state=2796bc865e162c146d1f6c93be1944bb, view=60e589d14ab1b7f86d9709bed7739aa1(OdysseyMainActivity/TextView-Only show )) (nav)
  - act: CustomTouchEvent(state=f655b7c5bac886983730a943418a9e7e, view=60e589d14ab1b7f86d9709bed7739aa1(OdysseyMainActivity/TextView-Only show )) (nav)
  - act: CustomTouchEvent(state=2796bc865e162c146d1f6c93be1944bb, view=60e589d14ab1b7f86d9709bed7739aa1(OdysseyMainActivity/TextView-Only show )) (nav)
  - act: CustomTouchEvent(state=f655b7c5bac886983730a943418a9e7e, view=648b16c3c530289791aa3310a273c69e(OdysseyMainActivity/TextView-Only show )) (rule)

### G012 Restrict artwork downloads

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on 'Settings' in the main menu; Select 'Artwork' from the settings menu
- Remaining steps: Select 'Downloads' from the artwork settings; Tap on 'Restrict' to enable artwork download restrictions; Confirm the restriction settings by tapping 'Save'
- Completion ratio: 0.40
- Actions taken: 46
  - act: CustomTouchEvent(state=2796bc865e162c146d1f6c93be1944bb, view=ea04a51ae96f207e259d0bebcb48e440(OdysseyMainActivity/TextView-Classic_Vi)) (heuristic)
  - act: CustomTouchEvent(state=2796bc865e162c146d1f6c93be1944bb, view=851cca6e3e6caf969d2da7b86082f11e(OdysseyMainActivity/Switch-)) (afford_search)
  - act: ScrollEvent(state=2796bc865e162c146d1f6c93be1944bb, view=c23974f4c42abbfef8a726bffdc22d6a(OdysseyMainActivity/RecyclerView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=2796bc865e162c146d1f6c93be1944bb, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (llm)
  - act: CustomTouchEvent(state=2796bc865e162c146d1f6c93be1944bb, view=ea04a51ae96f207e259d0bebcb48e440(OdysseyMainActivity/TextView-Classic_Vi)) (llm)
  - act: CustomTouchEvent(state=2796bc865e162c146d1f6c93be1944bb, view=6c6b60a90fa85a0fcb2aa91129d8b172(OdysseyMainActivity/TextView-<unknown> )) (llm)
  - act: CustomTouchEvent(state=2796bc865e162c146d1f6c93be1944bb, view=f9df95ac969a149a1a8ebd9525ad8b2f(OdysseyMainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=2796bc865e162c146d1f6c93be1944bb, view=831a7afb14aba844677a5963030aac86(OdysseyMainActivity/TextView-Select a d)) (rule)

### G013 Add the Odyssey home

- Status: **partial**
- Reason: Already on the home screen.
- Feature source: guide
- Completed steps: Select Odyssey
- Remaining steps: Long-press an empty area of the Android home screen; Tap Widgets; Scroll down to find Odyssey; Tap Add the Odyssey home
- Completion ratio: 0.20
- Credited from later features: G001

### G014 Open the system equaliser

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the navigation drawer or the player overflow menu
- Remaining steps: Scroll down until you find the equaliser entry; Tap the equaliser entry
- Completion ratio: 0.33
- Actions taken: 36
  - act: CustomTouchEvent(state=9565eabd42338100e8e9b96321080723, view=68aa487333b6759732c2499fc7230056(OdysseyMainActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=9565eabd42338100e8e9b96321080723, view=68aa487333b6759732c2499fc7230056(OdysseyMainActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=9565eabd42338100e8e9b96321080723, view=601a30b86821c8805b80b380683070e8(OdysseyMainActivity/TextView-Theme)) (llm)
  - act: CustomTouchEvent(state=9565eabd42338100e8e9b96321080723, view=013c8b740c693b25b749bcf31efe6905(OdysseyMainActivity/TextView-Library)) (rule)
  - act: CustomTouchEvent(state=9565eabd42338100e8e9b96321080723, view=70bd59546c7fe154893baf8e52673220(OdysseyMainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=e7f757622d52e79477fa36ee8abf6a6f, view=ea59986f5197d38dc4f7ef5440392e78(OdysseyMainActivity/TextView-Dark theme)) (llm)
  - act: CustomTouchEvent(state=f10d9acfcbd51f31a94dbc011d2cc183, view=68aa487333b6759732c2499fc7230056(OdysseyMainActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=f10d9acfcbd51f31a94dbc011d2cc183, view=7bb176d1140bfbd14e0d454201e93345(OdysseyMainActivity/TextView-Bookmarks)) (rule)

## Shared flows detected

3 reuse(s); 8 action(s) skipped by not re-executing a known terminal flow.

- `G005` reused `C004` (from G004), skipped 2 action(s)
- `G006` reused `C004` (from G004), skipped 3 action(s)
- `G007` reused `C004` (from G004), skipped 3 action(s)

See `session.json` and `log.md` in this folder for the full trace.
