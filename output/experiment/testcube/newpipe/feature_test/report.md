# Feature test report: NewPipe

- Started: 2026-10-26 13:57:24
- Finished: 2026-10-26 14:54:31
- Features: 18
- Covered: 13
- Partial: 5
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 82% (mean completion ratio; the headline number)
- Coverage: 72% (features with every guide step matched)
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

- Filled via credential.txt: 22
- Filled via VLM/Gemini: 2
- Unresolved: 0
- Online coverage: 72% (13/18) — live journal self-report (covered / extracted features).
- Offline coverage: not computed (no ground-truth JSON).

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
  - act: CustomTouchEvent(state=dca01089ff41fa943b32d2624fc2292a, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=278c7ffcf1444b33d7d05b5cebcd167c, view=9f1e9d5955e6cba81431ba8fd2921d11(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (rule)
  - act: CustomSetTextEvent(state=278c7ffcf1444b33d7d05b5cebcd167c, view=932c754fd3b9b0a75419c3854d74dbf5(MainActivity/EditText-Search), text=lofi hip hop) (mandatory_fill)
  - act: CustomTouchEvent(state=77bf81142f59cde90f52c4430a67c9c9, view=9f1e9d5955e6cba81431ba8fd2921d11(MainActivity/ImageView-)) (heuristic)

### F003 Filter search results

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Run a search; Open the filter menu; Pick a filter
- Completion ratio: 1.00
- Credited from later features: F004, F009
- Actions taken: 9
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=3a40574addde41666bcfe896b181a3c9(MainActivity/TextView-Bookmarked)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=3a40574addde41666bcfe896b181a3c9(MainActivity/TextView-Bookmarked)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=ca369ec4c0dfac50311c0a48f202ff64, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=6aeff1ca8b95ca69329d6fd581f47b2e, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=ca369ec4c0dfac50311c0a48f202ff64, view=a6d843570d3936b62cacc812c4e09337(MainActivity/CheckedTextView-Bookmarked)) (rule)
  - act: CustomTouchEvent(state=45db9105e4e016b3f99ab31ba3076d7e, view=3a40574addde41666bcfe896b181a3c9(MainActivity/TextView-Bookmarked)) (rule)
  - act: CustomTouchEvent(state=45db9105e4e016b3f99ab31ba3076d7e, view=3a40574addde41666bcfe896b181a3c9(MainActivity/TextView-Bookmarked)) (rule)

### F004 Downloads list

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the drawer
- Remaining steps: Tap Downloads
- Completion ratio: 0.50
- Actions taken: 33
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=0ad19e889ec0c0419cc8036b2e159ce2(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=dca01089ff41fa943b32d2624fc2292a, view=4ff54950de0ba6aba599e29fdc0f4007(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=2b88735a97c692937b8a484580921fd9, view=65f79c13fe16a6d568dae7cdb92d7fcf(MainActivity/Button-ENABLE FAS)) (rule)
  - act: CustomTouchEvent(state=dca01089ff41fa943b32d2624fc2292a, view=4ff54950de0ba6aba599e29fdc0f4007(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=be2d284e5fda1a7a10058efd7ba79f23, view=3358bb717297cb6e3ebd3fc0d7ed947e(MainActivity/Button-DISABLE FA)) (llm)
  - act: CustomTouchEvent(state=dca01089ff41fa943b32d2624fc2292a, view=d78a50973dd2bd95a8b8caac2c8ac3d1(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=0ad19e889ec0c0419cc8036b2e159ce2(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=dca01089ff41fa943b32d2624fc2292a, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)

### F005 Subscriptions tab

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the drawer; Tap Subscriptions
- Completion ratio: 1.00
- Actions taken: 8
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=86a81684bc351334383b55d29a587293, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=f5f0c9a422a963c0cc6da5d08c55b8f5, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=2477ab7465e65dbc141797b7866b316c, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=f5f0c9a422a963c0cc6da5d08c55b8f5, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=2477ab7465e65dbc141797b7866b316c, view=1b2316909654001a5a84ae7acccc3c81(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=f5f0c9a422a963c0cc6da5d08c55b8f5, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=1b2316909654001a5a84ae7acccc3c81(MainActivity/LinearLayout-)) (heuristic)

### F006 Bookmarked playlists

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap Bookmarked Playlists; Open the drawer
- Completion ratio: 1.00
- Credited from later features: F003, F004
- Actions taken: 4
  - act: CustomTouchEvent(state=17f41017c3c70346c6ee7cfdef983366, view=68428886113891027a7af430bc9d0761(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=278c7ffcf1444b33d7d05b5cebcd167c, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=7c3e1d89d6bbc71e3a91da9924602656, view=ce40e8ecbef01fa0d51d1d35551461e8(MainActivity/TextView-Playlists)) (heuristic)
  - act: CustomTouchEvent(state=278c7ffcf1444b33d7d05b5cebcd167c, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)

### F007 Watch history

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the drawer; Tap the 'Watch History' option in the drawer; Tap History; Review the list of watched videos; End in a visibly different, checkable app state
- Completion ratio: 1.00
- Credited from later features: F004, F005, F014
- Actions taken: 24
  - act: CustomSetTextEvent(state=ad7c87a2b8022f0f95413a8fed222acd, view=2ebf56eaccd57a6e345d7fcf99de6427(MainActivity/EditText-lofi hip h), text=lofi hip hop) (heuristic)
  - act: CustomSetTextEvent(state=5f40c9104d0918ea48e8e86990b6d05e, view=f300f7aeffae8382d529412cf737b7f1(MainActivity/EditText-lofi hip h), text=lofi hip hop) (heuristic)
  - act: CustomSetTextEvent(state=5f40c9104d0918ea48e8e86990b6d05e, view=f300f7aeffae8382d529412cf737b7f1(MainActivity/EditText-lofi hip h), text=lofi hip hop) (heuristic)
  - act: CustomTouchEvent(state=5f40c9104d0918ea48e8e86990b6d05e, view=6be1c49af532e2ee6c52c86938bd05af(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=f6a4cec8fd8b978f24267c0a007c28e6, view=4bc3c6ab2f87358d7ce050b82690790b(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=c3df37a3ab59ac3b9007add8c7259ff4, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=2db22b39cdb13efbf8421bd36afcf557, view=c6aa7b91700fa655cd445c7332c92ae1(MainActivity/CheckedTextView-History)) (nav)
  - act: CustomTouchEvent(state=cc847f5181bd76d21dc23632c419453a, view=f3fec16ddcb0afe7bb46bb3c49c67def(MainActivity/TextView-No videos)) (heuristic)

### F008 Open settings

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the drawer; Tap Settings
- Completion ratio: 1.00
- Credited from later features: F004, F009
- Actions taken: 8
  - act: CustomTouchEvent(state=7c3e1d89d6bbc71e3a91da9924602656, view=ce40e8ecbef01fa0d51d1d35551461e8(MainActivity/TextView-Playlists)) (heuristic)
  - act: CustomSetTextEvent(state=ca4850595df15df5a24072653738ed6a, view=d278d3fe19dc8e4e64d476dbf766e024(MainActivity/EditText-lofi hip h), text=lofi hip hop) (rule)
  - act: CustomTouchEvent(state=393fec2174cf139883f15e605f6b6120, view=0581105da2de033ae915b9603b193735(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=bac789dda0f772cca5a64b33705d3497, view=0581105da2de033ae915b9603b193735(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=ca4850595df15df5a24072653738ed6a, view=34cbe537d3b6062ad9414307e5d85435(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=f20ee4313a178c4099358afb18d4361f, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=7c3e1d89d6bbc71e3a91da9924602656, view=62f7d846e8d95c86743749bc7a63d1c5(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=f20ee4313a178c4099358afb18d4361f, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)

### F009 Change appearance

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open Settings; Tap Appearance; Pick a theme
- Completion ratio: 1.00
- Actions taken: 11
  - act: CustomTouchEvent(state=d9f9ee8f887311afda8ccc1c663a9a35, view=ad5d92bb7669106d8774cf29419d6e74(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=840273895d859248c8bd3e70f2314783, view=913403674234b3b9b0b0fadfe0a32b22(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=d9f9ee8f887311afda8ccc1c663a9a35, view=4e03f1ad9dcc7466d7087eab3df54bcb(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=d9f9ee8f887311afda8ccc1c663a9a35, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (rule)
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=ed63c398314c72a338dfd42f9839ba7f, view=e8d16081a3ba98a216b9fe92563aed8a(MainActivity/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=20fde93363107ef32c2ad029cb5afc45, view=61009159bff45b44a7ae0930d9962f7b(SettingsActivity/TextView-Appearance)) (heuristic)
  - act: CustomTouchEvent(state=d411640927d7a09ba9daf75dde53ded6, view=1b2ef187ce51ab5ca2354ed2084c0207(SettingsActivity/TextView-Select you)) (heuristic)

### F010 Video and audio settings

- Status: **covered**
- Reason: Covered by shared-flow reuse of C001.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open Settings; Tap Video and audio; Change a preference
- Completion ratio: 1.00
- Actions taken: 6
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (heuristic)
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=86a81684bc351334383b55d29a587293, view=1f892bc1c62f41e8d42173c79300e8b6(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=f5f0c9a422a963c0cc6da5d08c55b8f5, view=831be133abb43ba384e7e7b9b3457508(MainActivity/Button-RETRY)) (rule)
  - act: CustomTouchEvent(state=f5f0c9a422a963c0cc6da5d08c55b8f5, view=831be133abb43ba384e7e7b9b3457508(MainActivity/Button-RETRY)) (rule)
  - act: CustomTouchEvent(state=f5f0c9a422a963c0cc6da5d08c55b8f5, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)

### F011 About NewPipe

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the drawer
- Remaining steps: Scroll; Tap About; Tap FAQ
- Completion ratio: 0.25
- Credited from later features: F004
- Actions taken: 35
  - act: CustomTouchEvent(state=152f3bd2d280cd0f391767b09271251a, view=4e03f1ad9dcc7466d7087eab3df54bcb(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=152f3bd2d280cd0f391767b09271251a, view=4e03f1ad9dcc7466d7087eab3df54bcb(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=152f3bd2d280cd0f391767b09271251a, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=ed63c398314c72a338dfd42f9839ba7f, view=644750bdf90b720e7e27d5431fc22d84(MainActivity/TextView-Add to pla)) (rule)
  - act: CustomTouchEvent(state=50c7eb8eb62a9f4d71765cfcb9c91e75, view=4059bedf2b124a34f90878700d1e7d28(MainActivity/EditText-Name)) (llm)
  - act: CustomSetTextEvent(state=50c7eb8eb62a9f4d71765cfcb9c91e75, view=4059bedf2b124a34f90878700d1e7d28(MainActivity/EditText-Name), text=your_email@gmail.com) (rule)
  - act: CustomTouchEvent(state=f6210d5e119c26dbf9475ba629ca4865, view=2c6cbc2b164d4f7924a9407ac5ff16b0(MainActivity/Button-CREATE)) (llm)
  - act: CustomTouchEvent(state=152f3bd2d280cd0f391767b09271251a, view=ad5d92bb7669106d8774cf29419d6e74(MainActivity/Button-)) (rule)

### F012 Content settings

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open Settings
- Remaining steps: Tap Content; Change a preference
- Completion ratio: 0.33
- Credited from later features: F004
- Actions taken: 45
  - act: CustomTouchEvent(state=a9cde6fcab505b391de9e169f350c32b, view=4e03f1ad9dcc7466d7087eab3df54bcb(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=a9cde6fcab505b391de9e169f350c32b, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=ed63c398314c72a338dfd42f9839ba7f, view=644750bdf90b720e7e27d5431fc22d84(MainActivity/TextView-Add to pla)) (llm)
  - act: CustomTouchEvent(state=50c7eb8eb62a9f4d71765cfcb9c91e75, view=2c6cbc2b164d4f7924a9407ac5ff16b0(MainActivity/Button-CREATE)) (llm)
  - act: CustomTouchEvent(state=a9cde6fcab505b391de9e169f350c32b, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=ed63c398314c72a338dfd42f9839ba7f, view=62f7d846e8d95c86743749bc7a63d1c5(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=20fde93363107ef32c2ad029cb5afc45, view=31d7885a65828e4522a9bb66dc720399(SettingsActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=205b1f769e705d47e8759a861773de33, view=84660c3e7b9ca3632a51a85cc441f04c(SettingsActivity/TextView-Content)) (rule)

### F013 Download settings

- Status: **covered**
- Reason: Covered by shared-flow reuse of C009.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open Settings; Tap Download; Change a preference
- Completion ratio: 1.00
- Actions taken: 5
  - act: CustomTouchEvent(state=7c3e1d89d6bbc71e3a91da9924602656, view=8f77f5eb1ae17ce7473bd1e3ed8fc42f(MainActivity/TextView-Albums)) (llm)
  - act: CustomTouchEvent(state=46a31cdffe8512b3e1d509e640ec3c3e, view=13315cf023ddfb97a8c962b9650f790c(MainActivity/TextView-)) (heuristic)
  - act: CustomTouchEvent(state=7a08d7515035c3853537db3a07296142, view=913403674234b3b9b0b0fadfe0a32b22(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=152f3bd2d280cd0f391767b09271251a, view=ad5d92bb7669106d8774cf29419d6e74(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=a9cde6fcab505b391de9e169f350c32b, view=913403674234b3b9b0b0fadfe0a32b22(MainActivity/Button-)) (heuristic)

### F014 History and cache settings

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open Settings; Tap History and cache; Clear a cache or history entry
- Completion ratio: 1.00
- Actions taken: 8
  - act: CustomTouchEvent(state=152f3bd2d280cd0f391767b09271251a, view=ad5d92bb7669106d8774cf29419d6e74(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=a9cde6fcab505b391de9e169f350c32b, view=913403674234b3b9b0b0fadfe0a32b22(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=152f3bd2d280cd0f391767b09271251a, view=219c4bbedbbdf1d3941d0453cbda55c0(MainActivity/ImageView-)) (heuristic)
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=ed63c398314c72a338dfd42f9839ba7f, view=e8d16081a3ba98a216b9fe92563aed8a(MainActivity/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=20fde93363107ef32c2ad029cb5afc45, view=cc735fc21d6ca49f827fa2089269fe14(SettingsActivity/TextView-Backup and)) (heuristic)
  - act: CustomTouchEvent(state=296a33080c8113ad9be5c80b619b935a, view=d3d859214b3b249fd48a3e764543f901(SettingsActivity/TextView-Export his)) (heuristic)
  - act: CustomTouchEvent(state=296a33080c8113ad9be5c80b619b935a, view=d3d859214b3b249fd48a3e764543f901(SettingsActivity/TextView-Export his)) (heuristic)

### F015 Notification settings

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open Settings
- Remaining steps: Tap Notifications; Toggle a notification preference
- Completion ratio: 0.33
- Actions taken: 40
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=78113e45284d57e6a58eba3d82085017(MainActivity/Button-OPEN IN BR)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=6bac928563da9b08f96c2afcc4835f7f(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=6bac928563da9b08f96c2afcc4835f7f(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=d50c52c1df46ceea6e2656296d1e6a5b, view=b1e54895cbffa2637b437130ced3faff(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=8cb6ab5624a7c7146264f7a1bce26125, view=f03a4827af5407f9487e4bb799b6a030(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=8cb6ab5624a7c7146264f7a1bce26125, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=ee76c4ba989f015bea818298310e3421, view=faaf41fd65fa8aabec9bcc262656ded8(MainActivity/CheckedTextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=20fde93363107ef32c2ad029cb5afc45, view=53d9f141b79c4b83d9370dbf0db39d83(SettingsActivity/TextView-Settings)) (rule)

### F016 Backup and restore

- Status: **covered**
- Reason: Covered by shared-flow reuse of C001.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Tap 'Settings' in the navigation drawer; Tap 'Backup and restore' in the settings menu; Select 'Backup and restore' from the settings menu; Tap 'Backup' to initiate the backup process; Tap 'Restore' to initiate the restore process; Select the backup file to restore
- Completion ratio: 1.00
- Actions taken: 9
  - act: CustomTouchEvent(state=8d7fdf4cd81f71e9b8df5d1cd25473f0, view=faaf41fd65fa8aabec9bcc262656ded8(MainActivity/CheckedTextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=20fde93363107ef32c2ad029cb5afc45, view=cc735fc21d6ca49f827fa2089269fe14(SettingsActivity/TextView-Backup and)) (heuristic)
  - act: CustomTouchEvent(state=296a33080c8113ad9be5c80b619b935a, view=5757009dc8cd4258c6e8a8a9dacf1166(SettingsActivity/TextView-Reset sett)) (heuristic)
  - act: CustomTouchEvent(state=f6c033765c3f0cc8467ad00f6e01836e, view=7ce56ecd51af100af378d81a88b387d4(SettingsActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=0a98cdff5dc94eddd39ae4aeaa324287, view=6ea2423181dc9e61b8d5d6e7c67a602c(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=86a81684bc351334383b55d29a587293, view=831be133abb43ba384e7e7b9b3457508(MainActivity/Button-RETRY)) (rule)
  - act: CustomTouchEvent(state=86a81684bc351334383b55d29a587293, view=831be133abb43ba384e7e7b9b3457508(MainActivity/Button-RETRY)) (rule)
  - act: CustomTouchEvent(state=86a81684bc351334383b55d29a587293, view=cc00d1e7d8180062b3afba1b6216c7a5(MainActivity/LinearLayout-)) (rule)

### F017 Search suggestion reuse

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open Search
- Remaining steps: Observe previous queries; Tap a stored query
- Completion ratio: 0.33
- Actions taken: 48
  - act: CustomTouchEvent(state=296a33080c8113ad9be5c80b619b935a, view=5f1349f5162690f6ac9e86cc7d2b1a02(SettingsActivity/TextView-Backup and)) (rule)
  - act: CustomTouchEvent(state=296a33080c8113ad9be5c80b619b935a, view=3b58a08d31ec595083974736537f4f57(SettingsActivity/TextView-Import dat)) (rule)
  - act: CustomTouchEvent(state=296a33080c8113ad9be5c80b619b935a, view=3b58a08d31ec595083974736537f4f57(SettingsActivity/TextView-Import dat)) (rule)
  - act: CustomTouchEvent(state=296a33080c8113ad9be5c80b619b935a, view=d3d859214b3b249fd48a3e764543f901(SettingsActivity/TextView-Overrides )) (rule)
  - act: CustomTouchEvent(state=296a33080c8113ad9be5c80b619b935a, view=d3d859214b3b249fd48a3e764543f901(SettingsActivity/TextView-Export his)) (rule)
  - act: CustomTouchEvent(state=296a33080c8113ad9be5c80b619b935a, view=33f5bffde1ec9512346f78035c731825(SettingsActivity/TextView-Export dat)) (rule)
  - act: CustomTouchEvent(state=296a33080c8113ad9be5c80b619b935a, view=33f5bffde1ec9512346f78035c731825(SettingsActivity/TextView-Export dat)) (rule)
  - act: CustomTouchEvent(state=296a33080c8113ad9be5c80b619b935a, view=b1d5303a98e4be3e8b931d76ecbbaaf8(SettingsActivity/LinearLayout-)) (rule)

### F018 Clear a search

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open Search; Type a query; Tap the clear button
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=344ce514e4af626e54ad7cc0347561b1, view=9f1e9d5955e6cba81431ba8fd2921d11(MainActivity/ImageView-)) (heuristic)
  - act: CustomSetTextEvent(state=5578ed41c10e62f8125e1a3082273427, view=932c754fd3b9b0a75419c3854d74dbf5(MainActivity/EditText-Search), text=lofi hip hop) (mandatory_fill)
  - act: CustomTouchEvent(state=344ce514e4af626e54ad7cc0347561b1, view=9f1e9d5955e6cba81431ba8fd2921d11(MainActivity/ImageView-)) (heuristic)

## Shared flows detected

3 reuse(s); 8 action(s) skipped by not re-executing a known terminal flow.

- `F010` reused `C001` (from F001), skipped 2 action(s)
- `F013` reused `C009` (from F009), skipped 3 action(s)
- `F016` reused `C001` (from F001), skipped 3 action(s)

See `session.json` and `log.md` in this folder for the full trace.
