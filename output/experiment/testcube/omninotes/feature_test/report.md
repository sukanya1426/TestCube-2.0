# Feature test report: Omni Notes

- Started: 2026-09-24 23:00:41
- Finished: 2026-09-24 23:27:13
- Features: 14
- Covered: 1
- Partial: 12
- Dropped (blocked / stuck): 1
- Not present in the app: 0
- Weighted coverage: 44% (mean completion ratio; the headline number)
- Coverage: 7% (features with every guide step matched)
- Stop reason: restart_loop
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 13
- Never attempted: 1
- Blocked then recovered on retry: 0
- Blocked still: 1

## Guide vs README-extracted

- Guide features: 14
- README-extracted features: 4
- In both: 0
- Guide-only: 14
- README-only: 4
  - guide-only: G001 Create a text note
  - guide-only: G002 Convert a note between
  - guide-only: G003 Record
  - guide-only: G004 Add a location
  - guide-only: G005 View all notes
  - guide-only: G006 Assign a category
  - guide-only: G007 Filter notes
  - guide-only: G008 Restore a note
  - guide-only: G009 Pin a note
  - guide-only: G010 Merge several notes
  - guide-only: G011 Add a note
  - guide-only: G012 Switch the note list
  - README-only: F001 Complete first-run setup
  - README-only: F002 Search
  - README-only: F003 Import or export data
  - README-only: F004 Change app settings

## Text-field resolution

- Filled via credential.txt: 0
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 7% (1/14) — live journal self-report (covered / extracted features).
- Offline coverage: 0% (0 covered / 48; 8 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 6% (mean completion ratio).

## Findings

### G001 Create a text note

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the app
- Remaining steps: tap the "+" floating action button
- Completion ratio: 0.50
- Credited from later features: G003
- Actions taken: 13
  - act: CustomTouchEvent(state=835be08c1742c7560927a043a40c995b, view=a6ac4dba46ee35e935902122ee17a05e(IntroActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=5db0af0f6310ce3ad8f712fe5b611ae1(MainActivity/TextView-Notes)) (nav)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=5db0af0f6310ce3ad8f712fe5b611ae1(MainActivity/TextView-Notes)) (nav)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=5b0f835c182e8baf10567fd1f32fd5f9(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, x=625, y=1495) (llm)
  - act: CustomTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=82f69ca1ab7ed9d2278cc0e34cf74bf4(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=151faf2a66da818bba8939b2a5e82521, view=76da8433a47703ba775a906bbc6f78a1(MainActivity/TextView-Pushbullet)) (llm)

### G002 Convert a note between

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the overflow menu (three dots) on the note.; Select 'convert' from the overflow menu options.
- Remaining steps: Tap on the note you want to convert.; Choose 'convert to checklist' from the conversion options.; Tap 'Done' to save the changes.
- Completion ratio: 0.40
- Credited from later features: G004
- Actions taken: 8
  - act: CustomTouchEvent(state=b8f554585e400d6451fbea45bfca6f83, view=6e8e6e396dddb4bba618a9493f38bd8b(MainActivity/TextView-OK)) (rule)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=5b0f835c182e8baf10567fd1f32fd5f9(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=b0c8bbb5f7e566813c2f7adb4f966c0a, view=65f93f6f850aeccc753595ab221096b4(MainActivity/ListView-)) (llm)
  - act: CustomTouchEvent(state=b0c8bbb5f7e566813c2f7adb4f966c0a, view=65f93f6f850aeccc753595ab221096b4(MainActivity/ListView-)) (llm)
  - act: CustomTouchEvent(state=b0c8bbb5f7e566813c2f7adb4f966c0a, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=9c628fa4cec4e64c167ff9b105c35d0a(MainActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=cef0cb6e9c9291b34913f73eb2b5bbc6, view=e7374f2577cd697e119ef3ff1d504da3(MainActivity/TextView-Text note)) (rule)

### G003 Record

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the Omni Notes app; Navigate to the 'Record' feature; Tap the 'Record' option; Tap the 'Open a note' option
- Remaining steps: Tap the 'Attachment' icon; Select the 'Record' option
- Completion ratio: 0.67
- Credited from later features: G008
- Actions taken: 13
  - act: CustomTouchEvent(state=151faf2a66da818bba8939b2a5e82521, view=1bb0388414be7e37445c7d7745fb7810(MainActivity/TextView-Record)) (heuristic)
  - act: CustomTouchEvent(state=d3cd0e6d09eab67a8fa8d6f7ccebf8ce, view=4b37abdece5bb79c48ecae7bd895a5f8(MainActivity/TextView-Stop)) (nav)
  - act: CustomTouchEvent(state=4f850bb511b50fc81390bb93bbca2c30, view=82f69ca1ab7ed9d2278cc0e34cf74bf4(MainActivity/Button-)) (nav)
  - act: CustomTouchEvent(state=151faf2a66da818bba8939b2a5e82521, view=1bb0388414be7e37445c7d7745fb7810(MainActivity/TextView-Record)) (heuristic)
  - act: CustomTouchEvent(state=d3cd0e6d09eab67a8fa8d6f7ccebf8ce, view=4b37abdece5bb79c48ecae7bd895a5f8(MainActivity/TextView-Stop)) (nav)
  - act: CustomTouchEvent(state=69bbea10778801345409e3623aa47ef7, view=82f69ca1ab7ed9d2278cc0e34cf74bf4(MainActivity/Button-)) (nav)
  - act: CustomTouchEvent(state=151faf2a66da818bba8939b2a5e82521, view=76da8433a47703ba775a906bbc6f78a1(MainActivity/TextView-Pushbullet)) (llm)
  - act: CustomTouchEvent(state=69bbea10778801345409e3623aa47ef7, view=82f69ca1ab7ed9d2278cc0e34cf74bf4(MainActivity/Button-)) (afford_search)

### G004 Add a location

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the overflow menu; Tap to save the note
- Remaining steps: Select 'Add location'; Enter the location name; Tap to confirm the location
- Completion ratio: 0.40
- Credited from later features: G002
- Actions taken: 3
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=604a4707d5fae42e68968e1165eaa576(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=acef88737734a30f878024eb76cd84f6, view=1f3898069d4b3cb5c516721fbd112779(MainActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=604a4707d5fae42e68968e1165eaa576(MainActivity/Button-)) (heuristic)

### G005 View all notes

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the navigation drawer (hamburger icon or left-edge swipe)
- Remaining steps: Tap 'Reminders'; Tap 'All'
- Completion ratio: 0.33
- Credited from later features: G007
- Actions taken: 8
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=012a7f60c6cbc0d3d19ef1f47cb700b7(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=a7079a5f5cb704d939918a87bb174402, view=b83ae67df4c76b97d6e66ab7c11b7e53(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=012a7f60c6cbc0d3d19ef1f47cb700b7(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=c06c74e36ef057d0a9676a96c63f0e36, x=54, y=36) (llm)
  - act: CustomTouchEvent(state=c06c74e36ef057d0a9676a96c63f0e36, x=54, y=36) (llm)
  - act: CustomTouchEvent(state=c06c74e36ef057d0a9676a96c63f0e36, view=b83ae67df4c76b97d6e66ab7c11b7e53(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, x=151, y=154) (llm)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=5b0f835c182e8baf10567fd1f32fd5f9(MainActivity/ImageButton-)) (rule)

### G006 Assign a category

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open a note; Tap the overflow menu
- Remaining steps: Select 'Assign category'; Enter a category name; Tap 'Assign'; Confirm the category assignment
- Completion ratio: 0.33
- Credited from later features: G002, G004
- Actions taken: 8
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=81dfa562b5fd28ef88bb675e7f2978ba(MainActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=81dfa562b5fd28ef88bb675e7f2978ba(MainActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=de4ada5f877b9da35d7d83558525ec78(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=de4ada5f877b9da35d7d83558525ec78(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=2e442d5e93dbaedb83454f9f4f056701(MainActivity/ViewGroup-)) (rule)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=2e442d5e93dbaedb83454f9f4f056701(MainActivity/ViewGroup-)) (rule)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, x=54, y=192) (llm)
  - act: CustomTouchEvent(state=b0c8bbb5f7e566813c2f7adb4f966c0a, view=9c628fa4cec4e64c167ff9b105c35d0a(MainActivity/Button-)) (rule)

### G007 Filter notes

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the navigation drawer; Tap on the 'Tags' option
- Remaining steps: Select the desired tag to filter notes
- Completion ratio: 0.67
- Credited from later features: G003
- Actions taken: 11
  - act: CustomTouchEvent(state=b0c8bbb5f7e566813c2f7adb4f966c0a, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, x=54, y=96) (visual_ground)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=44d1829028ed013abc01d393f1e97744(MainActivity/View-)) (visual_ground)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, x=44, y=87) (visual_ground)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=44d1829028ed013abc01d393f1e97744(MainActivity/View-)) (visual_ground)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=c242a44ccece00449df5b669552343db(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=5db0af0f6310ce3ad8f712fe5b611ae1(MainActivity/TextView-Notes)) (rule)

### G008 Restore a note

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the drawer; Select the 'Restore' option
- Remaining steps: Tap on the note you want to restore; Confirm the restoration; Verify the note is restored to its original state
- Completion ratio: 0.40
- Credited from later features: G003
- Actions taken: 8
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=5b0f835c182e8baf10567fd1f32fd5f9(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=b0c8bbb5f7e566813c2f7adb4f966c0a, view=323544fa8f17f7e628b8dfa997991a6b(MainActivity/TextView-Notes)) (nav)
  - act: CustomTouchEvent(state=b0c8bbb5f7e566813c2f7adb4f966c0a, view=323544fa8f17f7e628b8dfa997991a6b(MainActivity/TextView-Notes)) (nav)
  - act: CustomTouchEvent(state=b0c8bbb5f7e566813c2f7adb4f966c0a, view=604a4707d5fae42e68968e1165eaa576(MainActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=5db0af0f6310ce3ad8f712fe5b611ae1(MainActivity/TextView-Notes)) (nav)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=5db0af0f6310ce3ad8f712fe5b611ae1(MainActivity/TextView-Notes)) (nav)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=c242a44ccece00449df5b669552343db(MainActivity/ImageButton-)) (afford_search)

### G009 Pin a note

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Long-press the note in the list; Verify that the note is now pinned at the top of the list
- Remaining steps: Tap the pin action in the contextual toolbar; Confirm the pin action by tapping the confirmation button
- Completion ratio: 0.50
- Credited from later features: G012
- Actions taken: 7
  - act: LongTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (heuristic)
  - act: LongTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=3129b904c1e4deaaa09ec65e278a57c2(MainActivity/EditText-Title)) (heuristic)
  - act: LongTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=3129b904c1e4deaaa09ec65e278a57c2(MainActivity/EditText-Title)) (heuristic)
  - act: LongTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=4298255ac4bd57ba350a09eb9ca88da7(MainActivity/EditText-Content)) (heuristic)
  - act: LongTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=4298255ac4bd57ba350a09eb9ca88da7(MainActivity/EditText-Content)) (heuristic)
  - act: CustomTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=44d1829028ed013abc01d393f1e97744(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=012a7f60c6cbc0d3d19ef1f47cb700b7(MainActivity/ImageView-)) (llm)

### G010 Merge several notes

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the 'Merge' button; Tap the 'Merge' option
- Remaining steps: Long-press the first note; Tap the additional notes to add them to the selection; Select the notes to merge; Confirm the merge operation
- Completion ratio: 0.33
- Credited from later features: G001, G003
- Actions taken: 8
  - act: LongTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=81dfa562b5fd28ef88bb675e7f2978ba(MainActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=81dfa562b5fd28ef88bb675e7f2978ba(MainActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=81dfa562b5fd28ef88bb675e7f2978ba(MainActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (afford_search)
  - act: LongTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=21c0ff67a35dfaade3a688d022803445(MainActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=21c0ff67a35dfaade3a688d022803445(MainActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=bdd7c83bd888f01d089d99fc4f5434d8(MainActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=21c0ff67a35dfaade3a688d022803445(MainActivity/Button-)) (rule)

### G011 Add a note

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Omni Notes app; Tap on the 'Share' button
- Remaining steps: Select text or a file in any app; Select 'Add' from the navigation hints; Select 'Note' from the navigation hints; Enter the note content
- Completion ratio: 0.33
- Credited from later features: G001
- Actions taken: 9
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=5db0af0f6310ce3ad8f712fe5b611ae1(MainActivity/TextView-Notes)) (nav)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=5db0af0f6310ce3ad8f712fe5b611ae1(MainActivity/TextView-Notes)) (nav)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=15d69a476e7fac088b2b6abe33ef7346(MainActivity/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=241e971698193bf6e54dca910bab8be6, view=eee31f86d4f83c18514746ba88e358c0(MainActivity/TextView-Add remind)) (nav)
  - act: CustomTouchEvent(state=a5d939a6d82687ae2d4c1d72b7263631, view=e77bc9d7bce367f9be69269ca1fc1626(MainActivity/TextView-11)) (llm)
  - act: CustomTouchEvent(state=a5d939a6d82687ae2d4c1d72b7263631, view=e77bc9d7bce367f9be69269ca1fc1626(MainActivity/TextView-11)) (llm)
  - act: CustomTouchEvent(state=a5d939a6d82687ae2d4c1d72b7263631, view=0ee96df1df8627cd6277422d97f548bb(MainActivity/Button-OK)) (rule)

### G012 Switch the note list

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the overflow menu in the note list; Select 'Layout' from the overflow menu; Tap the 'Expanded view' option in the layout menu; The note list now displays in the expanded card layout
- Completion ratio: 1.00
- Actions taken: 11
  - act: CustomTouchEvent(state=2f231c7e33af82273e92a3501c9bf667, view=5551fda752739e00a219dac4b5637279(MainActivity/Button-SEP 24, 20)) (nav)
  - act: CustomTouchEvent(state=7d2a369a7739e254b9a602859cb7412b, view=7dbdd94a0f6739c87042bb42b14a8ca8(MainActivity/TextView-2026)) (heuristic)
  - act: CustomTouchEvent(state=56f86e1368c9b4a1ce849826ee9c6a3d, view=4c536dc8685f932b4c8d6fccc42c2a6e(MainActivity/TextView-2029)) (heuristic)
  - act: CustomTouchEvent(state=62b69804daf90d38026bd4663ab616d3, view=00da5627b2d291070bc4424d865aaf9c(MainActivity/Button-11:23 PM)) (nav)
  - act: CustomTouchEvent(state=4c02d39f14e380139670035120cb7f18, view=1854dab4d0cad8ad6a6d3ef9192fc9c5(MainActivity/Button-SEP 24, 20)) (nav)
  - act: CustomTouchEvent(state=62b69804daf90d38026bd4663ab616d3, view=00da5627b2d291070bc4424d865aaf9c(MainActivity/Button-11:23 PM)) (nav)
  - act: CustomTouchEvent(state=4c02d39f14e380139670035120cb7f18, view=0ee96df1df8627cd6277422d97f548bb(MainActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=907fe07594f65d8c637546fcfe6076b9, view=dbe06a2f7d081095c9a4b87f3c71df8e(MainActivity/LinearLayout-)) (heuristic)

### G013 Export a full backup

- Status: **dropped**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Remaining steps: Tap 'Settings'; Scroll to 'Data'; Tap 'Export data'; Select 'Export full backup'; Confirm export; Wait for backup completion
- Completion ratio: 0.00
- Actions taken: 7
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=0db419bcb7fecd31acf4c3bc0aa8ccdb, view=e7374f2577cd697e119ef3ff1d504da3(MainActivity/TextView-Text note)) (heuristic)
  - act: CustomTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=012a7f60c6cbc0d3d19ef1f47cb700b7(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=eb1a2732ea48bd24d189167b61515050, view=717efb83ad9fec36d2f59fdf65bf532b(MainActivity/TextView-Enable che)) (rule)
  - act: CustomTouchEvent(state=241e971698193bf6e54dca910bab8be6, view=012a7f60c6cbc0d3d19ef1f47cb700b7(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=e1d7c6f4af18aa4814b7019d87ea1c4d, view=29ed44c0c7128f11e75f6df76b750eae(MainActivity/TextView-Disable ch)) (rule)
  - act: CustomTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=b9192de12c58cca98c8cef7cacbb5921(MainActivity/Button-)) (heuristic)

### G014 Delete an existing backup

- Status: **partial**
- Reason: Could not restart the app for this feature.
- Feature source: guide
- Completed steps: Open Settings; Select 'Backups'
- Remaining steps: Tap 'Data'; Tap 'Existing Backups'; Select the backup to delete; Tap 'Delete'
- Completion ratio: 0.33
- Credited from later features: G003, G012

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
