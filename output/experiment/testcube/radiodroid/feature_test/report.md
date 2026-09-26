# Feature test report: RadioDroid

- Started: 2026-09-25 03:06:50
- Finished: 2026-09-25 03:33:04
- Features: 14
- Covered: 3
- Partial: 11
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 56% (mean completion ratio; the headline number)
- Coverage: 21% (features with every guide step matched)
- Stop reason: all_features_done
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 14
- Never attempted: 0
- Blocked then recovered on retry: 0
- Blocked still: 0

## Guide vs README-extracted

- Guide features: 14
- README-extracted features: 10
- In both: 2
- Guide-only: 12
- README-only: 8
  - guide-only: G001 Browse popular radio stations
  - guide-only: G004 Remove a station
  - guide-only: G005 View station details
  - guide-only: G006 Open a station's homepage
  - guide-only: G007 Record the stream
  - guide-only: G008 View the played-track history
  - guide-only: G009 Set a radio alarm
  - guide-only: G010 Import favourite stations
  - guide-only: G011 Cast a station
  - guide-only: G012 Control playback
  - guide-only: G013 Adjust the streaming buffer
  - guide-only: G014 Restrict playback
  - README-only: F001 Close or skip the tutorial
  - README-only: F002 Leave any first-run analytics or settings screen
  - README-only: F003 Tap Create Database or Open Database if shown
  - README-only: F004 Enter a file name if asked and confirm Save
  - README-only: F005 Reach the home or main screen
  - README-only: F007 Download for offline use
  - README-only: F009 Import or export data
  - README-only: F010 Change app settings

## Text-field resolution

- Filled via credential.txt: 2
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 21% (3/14) — live journal self-report (covered / extracted features).
- Offline coverage: 3% (1 covered / 32; 7 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 9% (mean completion ratio).

## Findings

### G001 Browse popular radio stations

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select a popular radio station from the list; Open the app
- Remaining steps: Tap on the 'Stations' screen; Scroll down to find the 'Browse popular radio stations' section; Tap on the 'Browse popular radio stations' option
- Completion ratio: 0.40
- Credited from later features: G002, G008
- Actions taken: 10
  - act: CustomTouchEvent(state=949c40d94ef119c218f5de3011f3f639, view=f37a50b43d6bdf4a3a9d830130e513dc(ActivityMain/ImageView-)) (nav)
  - act: CustomTouchEvent(state=f1f594b0d991f72256445873f41489bf, view=7ec93f7c8e3f657f3957b27fb2f7ff78(ActivityMain/TextView-Stations)) (nav)
  - act: CustomTouchEvent(state=949c40d94ef119c218f5de3011f3f639, view=f37a50b43d6bdf4a3a9d830130e513dc(ActivityMain/ImageView-)) (nav)
  - act: CustomTouchEvent(state=f1f594b0d991f72256445873f41489bf, view=8e2ad2dda0972386d54e3e3b39789ea6(ActivityMain/TextView-Stations)) (rule)
  - act: CustomTouchEvent(state=f1f594b0d991f72256445873f41489bf, view=596321735a93d75f9c125217d1780772(ActivityMain/TextView-Radio Para)) (rule)
  - act: CustomTouchEvent(state=183db57ffec1ba439dacca731c87ce50, view=7ec93f7c8e3f657f3957b27fb2f7ff78(ActivityMain/TextView-Stations)) (nav)
  - act: CustomTouchEvent(state=7a95e3bd0ce0b09b66fc190a6bd2d078, view=7ec93f7c8e3f657f3957b27fb2f7ff78(ActivityMain/TextView-Stations)) (nav)
  - act: CustomTouchEvent(state=7a95e3bd0ce0b09b66fc190a6bd2d078, view=cafd6095650258c54057858bc95f3e34(ActivityMain/TextView-california)) (rule)

### G002 Search stations

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap on the search icon in the navigation bar; Enter the name of the station in the search bar; Press the search button to execute the search; Select the desired station from the search results; Tap on the station to open its details
- Completion ratio: 1.00
- Credited from later features: G005
- Actions taken: 12
  - act: CustomTouchEvent(state=295a9021806f9725356f2c3f1b41457f, view=bc1f2fe2fb0faecfec1156a0f3fc74ea(ActivityMain/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=295a9021806f9725356f2c3f1b41457f, view=bc1f2fe2fb0faecfec1156a0f3fc74ea(ActivityMain/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=295a9021806f9725356f2c3f1b41457f, view=d556c765e6351ccc41fd479a43f0e0ac(ActivityMain/EditText-Search…)) (llm)
  - act: CustomTouchEvent(state=295a9021806f9725356f2c3f1b41457f, view=9e2adc813054de53e386b66c27529365(ActivityMain/TextView-Settings)) (llm)
  - act: CustomTouchEvent(state=295a9021806f9725356f2c3f1b41457f, view=d556c765e6351ccc41fd479a43f0e0ac(ActivityMain/EditText-Search…)) (llm)
  - act: CustomTouchEvent(state=295a9021806f9725356f2c3f1b41457f, view=b014bc2bcf669a4a683f2ffad7f1781d(ActivityMain/EditText-Search…)) (llm)
  - act: CustomTouchEvent(state=295a9021806f9725356f2c3f1b41457f, view=b014bc2bcf669a4a683f2ffad7f1781d(ActivityMain/EditText-Search…)) (llm)
  - act: CustomTouchEvent(state=295a9021806f9725356f2c3f1b41457f, view=0838a53581aec3a6ddc5085984f0c046(ActivityMain/FrameLayout-)) (rule)

### G003 Stop playback

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the stop control in the player bar; Tap the stop control in the expanded player
- Remaining steps: Tap the stop control in the notification
- Completion ratio: 0.67
- Actions taken: 9
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=62523d54dbc2bf005566bafbdbe763d0(ActivityMain/TextView-Music Play)) (heuristic)
  - act: CustomTouchEvent(state=cccdc5a74973f0e369d02792a56c321e, view=d9dfb0c6c11da5fdf0c58a9641598e3b(ActivityMain/TextView-Music Play)) (heuristic)
  - act: CustomTouchEvent(state=cccdc5a74973f0e369d02792a56c321e, view=d9dfb0c6c11da5fdf0c58a9641598e3b(ActivityMain/TextView-Music Play)) (heuristic)
  - act: CustomTouchEvent(state=cccdc5a74973f0e369d02792a56c321e, view=0cc9a49a8a94336a52eda1c773863023(ActivityMain/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=fa0b70159602af95176c18be34c0ebf1, view=d9dfb0c6c11da5fdf0c58a9641598e3b(ActivityMain/TextView-Music Play)) (heuristic)
  - act: CustomTouchEvent(state=fa0b70159602af95176c18be34c0ebf1, view=d9dfb0c6c11da5fdf0c58a9641598e3b(ActivityMain/TextView-Music Play)) (heuristic)
  - act: CustomTouchEvent(state=fa0b70159602af95176c18be34c0ebf1, view=0cc9a49a8a94336a52eda1c773863023(ActivityMain/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=fa0b70159602af95176c18be34c0ebf1, view=0cc9a49a8a94336a52eda1c773863023(ActivityMain/ImageView-)) (heuristic)

### G004 Remove a station

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Long-press the station you want to remove; Tap on the 'Favourites' screen
- Remaining steps: Select 'Remove' from the context menu; Confirm the removal by selecting 'Yes' if prompted
- Completion ratio: 0.50
- Credited from later features: G005, G010
- Actions taken: 8
  - act: LongTouchEvent(state=352bffe189166a6a65689d898758e4b8, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: LongTouchEvent(state=aad61832051f26acbd10d0f24cb759c9, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: LongTouchEvent(state=aad61832051f26acbd10d0f24cb759c9, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: LongTouchEvent(state=aad61832051f26acbd10d0f24cb759c9, view=303abcff6c7a82815d5fee64640b03e1(ActivityMain/ImageButton-)) (afford_search)
  - act: LongTouchEvent(state=d392eb84ada05c6c5beac23b08d0615c, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: LongTouchEvent(state=aad61832051f26acbd10d0f24cb759c9, view=d73976b4ec33a7cb181639c302d4bcff(ActivityMain/ImageView-)) (heuristic)
  - act: LongTouchEvent(state=46b9a67333c84edef3f3de7f784d41e5, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=46b9a67333c84edef3f3de7f784d41e5, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (rule)

### G005 View station details

- Status: **covered**
- Reason: The current screen is already showing the station details, which matches the goal of viewing station details. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap a station; open its detail page
- Completion ratio: 1.00
- Credited from later features: G006
- Actions taken: 6
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=46b9a67333c84edef3f3de7f784d41e5, view=5700b8558847a3d721a3ef36c3b05329(ActivityMain/TextView-Radio Para)) (nav)
  - act: CustomTouchEvent(state=4d80fc6d948ec5d4d61ad87d71151981, view=4edfb0eb3e4587b8e856fd285b43fd78(ActivityMain/ImageView-)) (nav)
  - act: CustomTouchEvent(state=446fab6a49f6e9bfe40b67966279e3f2, view=c750590e12804fcea5d2a245ebbe78f2(ActivityMain/View-)) (rule)
  - act: CustomTouchEvent(state=4d80fc6d948ec5d4d61ad87d71151981, view=4edfb0eb3e4587b8e856fd285b43fd78(ActivityMain/ImageView-)) (nav)
  - act: CustomTouchEvent(state=77a08c1d40e9dcfee5877084f0c0ce59, view=2d13236dfad4e8c4ff5ce8a965545f7b(ActivityMain/TextView-03:00)) (llm)

### G006 Open a station's homepage

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the station detail page; Select the station's homepage link
- Remaining steps: Tap on the homepage/website link
- Completion ratio: 0.67
- Credited from later features: G002
- Actions taken: 7
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=702e68d753622b80bc7c8121f46abe77, view=cdf7bacd8203e0efaf7228c3bcd86ef8(ActivityMain/ViewGroup-)) (llm)
  - act: CustomTouchEvent(state=b37a0d2905f90069b6647cee4936fe65, view=5d620d8a7e1477aeeb6e6190352e59dd(ActivityMain/ImageView-)) (llm)
  - act: CustomTouchEvent(state=b37a0d2905f90069b6647cee4936fe65, view=05c365b3c3ef027f8572676a4975fef1(ActivityMain/ViewGroup-)) (llm)
  - act: CustomTouchEvent(state=c3d7317547672c9507302a07c2557fdf, view=303abcff6c7a82815d5fee64640b03e1(ActivityMain/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=c0936940ff492ffe84ce1ac751f4273f, view=1f6cabbf994952fdbe65e406c8db357e(ActivityMain/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=c3d7317547672c9507302a07c2557fdf, view=303abcff6c7a82815d5fee64640b03e1(ActivityMain/ImageButton-)) (heuristic)

### G007 Record the stream

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the 'Stream' button in the navigation bar.; Tap the 'Start playing a station' button to begin playing a station.
- Remaining steps: Select the 'Record the stream' feature from the menu.; Tap the record button in the player interface to start recording the stream.; Wait for the recording to complete and then stop the recording by tapping the stop button.
- Completion ratio: 0.40
- Credited from later features: G005
- Actions taken: 9
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=62523d54dbc2bf005566bafbdbe763d0(ActivityMain/TextView-Music Play)) (heuristic)
  - act: CustomTouchEvent(state=cccdc5a74973f0e369d02792a56c321e, view=0cc9a49a8a94336a52eda1c773863023(ActivityMain/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=fa0b70159602af95176c18be34c0ebf1, view=1f6cabbf994952fdbe65e406c8db357e(ActivityMain/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=459495ee80fa3804f7041bb5696e0185, view=d9dfb0c6c11da5fdf0c58a9641598e3b(ActivityMain/TextView-Music Play)) (heuristic)
  - act: CustomTouchEvent(state=459495ee80fa3804f7041bb5696e0185, view=d9dfb0c6c11da5fdf0c58a9641598e3b(ActivityMain/TextView-Music Play)) (heuristic)
  - act: CustomTouchEvent(state=459495ee80fa3804f7041bb5696e0185, view=303abcff6c7a82815d5fee64640b03e1(ActivityMain/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=659f398a11cfc4073f433d65c3883953, view=d9dfb0c6c11da5fdf0c58a9641598e3b(ActivityMain/TextView-Music Play)) (heuristic)
  - act: CustomTouchEvent(state=6390d976a4ed6f68192165b2e03b517b, view=9d66accf53a321d4d029df3d0b20b9bb(ActivityMain/TextView-Player)) (rule)

### G008 View the played-track history

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the navigation drawer
- Remaining steps: Scroll down to find 'History'; Tap on 'History'; Wait for the track history to load; Verify the track history is displayed
- Completion ratio: 0.20
- Actions taken: 9
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=13b23cfdfc2aa8c49f91e20d81fbe8d3(ActivityMain/TextView-History)) (heuristic)
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=d7faaabca7500718b78ab0e97d0d9bb8(ActivityMain/TextView-History)) (heuristic)
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=d7faaabca7500718b78ab0e97d0d9bb8(ActivityMain/TextView-History)) (heuristic)
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=25d3402e7d19290a2113aca169f2045d(ActivityMain/Button-)) (heuristic)
  - act: CustomTouchEvent(state=5f9a783dff7cd2f202cf1a4e082d2bd8, view=9f12e4257bbab64e944a6e267d8b6fc0(ActivityMain/TextView-Do you rea)) (heuristic)
  - act: CustomTouchEvent(state=5f9a783dff7cd2f202cf1a4e082d2bd8, view=f212b2a898d3820b69bfea445395a23c(ActivityMain/Button-NO)) (heuristic)
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=97baf4a0a94819fa9b43129690e5df43(ActivityMain/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=fc7f0602feaa76139be98d52d5f67471, view=6af336b689da5a8b4e9a70ed7dafca51(ActivityMain/Button-)) (rule)

### G009 Set a radio alarm

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the navigation drawer; Tap 'Alarm'; Select the desired radio station
- Remaining steps: Enter the desired time for the alarm; Tap 'Set' to confirm the alarm
- Completion ratio: 0.60
- Credited from later features: G002
- Actions taken: 10
  - act: CustomTouchEvent(state=7b73395ea9e28c7112e5ce43f1d9e0df, view=76d5db6c2477dd3f186d5b22e98800b7(ActivityMain/TextView-Open the a)) (heuristic)
  - act: CustomTouchEvent(state=bf9eb9f979f9c8e0a454449eb81635dd, view=32c041c322ec3e27717a3cb9d300769a(ActivityMain/View-)) (llm)
  - act: CustomTouchEvent(state=bf9eb9f979f9c8e0a454449eb81635dd, view=32c041c322ec3e27717a3cb9d300769a(ActivityMain/View-)) (llm)
  - act: CustomTouchEvent(state=bf9eb9f979f9c8e0a454449eb81635dd, view=ca28a2dbb278ba868779927b959407e7(ActivityMain/CheckedTextView-YouTube Mu)) (llm)
  - act: CustomTouchEvent(state=ce0b747ed3e28e00248339cef5043e03, view=fbd70529e92e0400df874d5a9adb0518(ActivityMain/TextView-Open the a)) (heuristic)
  - act: CustomTouchEvent(state=e7084d4e345f8d32c5f0d4ebba36fff4, view=76d5db6c2477dd3f186d5b22e98800b7(ActivityMain/TextView-Open the a)) (heuristic)
  - act: CustomTouchEvent(state=bf9eb9f979f9c8e0a454449eb81635dd, view=ca28a2dbb278ba868779927b959407e7(ActivityMain/CheckedTextView-YouTube Mu)) (llm)
  - act: CustomTouchEvent(state=ce0b747ed3e28e00248339cef5043e03, view=b7fe8c21f7740880e3f16555519b3439(ActivityMain/FrameLayout-)) (rule)

### G010 Import favourite stations

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the navigation drawer or the Favourites overflow menu; tap the import option
- Completion ratio: 1.00
- Credited from later features: G012
- Actions taken: 9
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=9e2adc813054de53e386b66c27529365(ActivityMain/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=9e2adc813054de53e386b66c27529365(ActivityMain/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=175a8a86e5904cbf72aa7355c4533f47(ActivityMain/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=8874368c035e50968236cd7d23ed3075, view=97616a1d8d237baedbd9f524edfe991c(ActivityMain/FrameLayout-)) (heuristic)
  - act: CustomSetTextEvent(state=d02480851f7703ce409483c0ff0f4943, view=b014bc2bcf669a4a683f2ffad7f1781d(ActivityMain/EditText-Search…), text=test) (heuristic)
  - act: CustomTouchEvent(state=3c6c3d3448aa5e507dd2bc55da94aa1a, view=04a4c890ec9b59a0e359b92e946f044c(ActivityMain/ImageView-)) (rule)

### G011 Cast a station

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Select the 'Cast' option from the station menu; Tap on the 'Station' option in the navigation drawer; Tap the cast icon in the toolbar to confirm the station is cast
- Remaining steps: Open the RadioDroid app; Tap the cast icon in the toolbar; Ensure the phone and the Chromecast are on the same network
- Completion ratio: 0.50
- Credited from later features: G002, G005
- Actions taken: 4
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=5700b8558847a3d721a3ef36c3b05329(ActivityMain/TextView-Radio Para)) (nav)
  - act: CustomTouchEvent(state=f1619c7df46ef7638dded37855f341e3, view=4edfb0eb3e4587b8e856fd285b43fd78(ActivityMain/ImageView-)) (nav)
  - act: CustomTouchEvent(state=446fab6a49f6e9bfe40b67966279e3f2, view=c750590e12804fcea5d2a245ebbe78f2(ActivityMain/View-)) (rule)
  - act: CustomTouchEvent(state=f1619c7df46ef7638dded37855f341e3, view=4edfb0eb3e4587b8e856fd285b43fd78(ActivityMain/ImageView-)) (nav)

### G012 Control playback

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'control' option in the navigation menu.; Select the desired station from the list.; Tap on the 'Start a station' option.
- Remaining steps: Select 'playback' from the dropdown menu.; Pull down the notification shade to reveal the control panel.
- Completion ratio: 0.60
- Credited from later features: G002, G005
- Actions taken: 8
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=4648941591b4c682c2c26d04fa670980(ActivityMain/ViewGroup-)) (heuristic)
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=3614a2689ab85fb8533f6497e2c1def0(ActivityMain/ImageView-)) (llm)
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=936aa16d7b801189398fba4d4663cbd3(ActivityMain/TextView-Connectivi)) (llm)
  - act: CustomTouchEvent(state=76f717c4f3b8ca0d1520bf7d7fdeae42, view=0e383d4df9fa8b38aacb91f01c292319(ActivityMain/TextView-Retry time)) (rule)
  - act: CustomTouchEvent(state=f9727af3e157ece361505d951beeed32, view=93e187ee747bcce06e9a7d841fe37ff9(ActivityMain/TextView-Retry time)) (rule)
  - act: CustomTouchEvent(state=f9727af3e157ece361505d951beeed32, view=93e187ee747bcce06e9a7d841fe37ff9(ActivityMain/TextView-Retry time)) (rule)
  - act: CustomTouchEvent(state=f9727af3e157ece361505d951beeed32, view=64829a1a6eb14119182b8a5000e9b666(ActivityMain/Button-OK)) (rule)
  - act: CustomTouchEvent(state=76f717c4f3b8ca0d1520bf7d7fdeae42, view=0e383d4df9fa8b38aacb91f01c292319(ActivityMain/TextView-Retry time)) (rule)

### G013 Adjust the streaming buffer

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on 'Settings'
- Remaining steps: Scroll to 'Playback'; Select 'Adjust the streaming buffer'; Enter the desired buffer size; Tap on 'Save' to apply changes
- Completion ratio: 0.20
- Actions taken: 8
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=97616a1d8d237baedbd9f524edfe991c(ActivityMain/FrameLayout-)) (heuristic)
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=936aa16d7b801189398fba4d4663cbd3(ActivityMain/TextView-Connectivi)) (llm)
  - act: CustomTouchEvent(state=76f717c4f3b8ca0d1520bf7d7fdeae42, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (nav)
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=3614a2689ab85fb8533f6497e2c1def0(ActivityMain/ImageView-)) (llm)
  - act: CustomTouchEvent(state=6ce2d5dc6c64622b4849ed709da804b1, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (nav)
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=44f19fc14506e26a1e24370e01860701(ActivityMain/ViewGroup-)) (llm)
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=97616a1d8d237baedbd9f524edfe991c(ActivityMain/FrameLayout-)) (nav)
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=44f19fc14506e26a1e24370e01860701(ActivityMain/ViewGroup-)) (llm)

### G014 Restrict playback

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open Settings
- Remaining steps: Scroll down to find the network/metered connection option; Select the network/metered connection option; Scroll down to find the playback restrictions; Select the playback restrictions; Confirm the changes
- Completion ratio: 0.17
- Actions taken: 6
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=941278d31a2c82787d9f28dc40811dd4(ActivityMain/ImageView-)) (llm)
  - act: CustomTouchEvent(state=cc2e80a05347f02256a751d7c827184c, view=97616a1d8d237baedbd9f524edfe991c(ActivityMain/FrameLayout-)) (nav)
  - act: CustomTouchEvent(state=d02480851f7703ce409483c0ff0f4943, view=e63a1de6d2b95fe14dfd083098320725(ActivityMain/ImageView-)) (llm)
  - act: CustomTouchEvent(state=79c35b5a530101fd7ae2b1849ff87c22, view=941278d31a2c82787d9f28dc40811dd4(ActivityMain/ImageView-)) (llm)
  - act: CustomTouchEvent(state=cc2e80a05347f02256a751d7c827184c, view=97616a1d8d237baedbd9f524edfe991c(ActivityMain/FrameLayout-)) (nav)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
