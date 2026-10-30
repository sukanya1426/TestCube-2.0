# Feature test report: RadioDroid

- Started: 2026-10-26 02:41:51
- Finished: 2026-10-26 03:40:26
- Features: 14
- Covered: 3
- Partial: 4
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 58% (mean completion ratio; the headline number)
- Coverage: 21% (features with every guide step matched)
- Stop reason: budget_time
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

- Filled via credential.txt: 13
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 21% (3/14) — live journal self-report (covered / extracted features).
- Offline coverage: not computed (no ground-truth JSON).

## Findings

### G001 Browse popular radio stations

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Tap on the 'Browse popular radio stations' feature; Tap on a radio station to play
- Remaining steps: Select the 'Browse' option; Select the 'Popular' option
- Completion ratio: 0.50
- Credited from later features: G005
- Actions taken: 26
  - act: CustomTouchEvent(state=6b4ccbff9b35a08dafe0097097070eb1, view=175a8a86e5904cbf72aa7355c4533f47(ActivityMain/FrameLayout-)) (nav)
  - act: CustomTouchEvent(state=6b4ccbff9b35a08dafe0097097070eb1, view=175a8a86e5904cbf72aa7355c4533f47(ActivityMain/FrameLayout-)) (nav)
  - act: CustomTouchEvent(state=6b4ccbff9b35a08dafe0097097070eb1, view=3614a2689ab85fb8533f6497e2c1def0(ActivityMain/ImageView-)) (llm)
  - act: CustomTouchEvent(state=ce5ab14e2562ad7505d59359211e20e4, view=175a8a86e5904cbf72aa7355c4533f47(ActivityMain/FrameLayout-)) (nav)
  - act: CustomTouchEvent(state=22eb68afe8c99b42f16a87cca774c399, view=8e2ad2dda0972386d54e3e3b39789ea6(ActivityMain/TextView-Stations)) (nav)
  - act: CustomTouchEvent(state=09aecc4203de26d250179f93d9fd495b, view=7ec93f7c8e3f657f3957b27fb2f7ff78(ActivityMain/TextView-Stations)) (nav)
  - act: CustomTouchEvent(state=131fef7ed431bddfa9533899ed9e284f, view=7ec93f7c8e3f657f3957b27fb2f7ff78(ActivityMain/TextView-Stations)) (nav)
  - act: CustomTouchEvent(state=09aecc4203de26d250179f93d9fd495b, view=7ec93f7c8e3f657f3957b27fb2f7ff78(ActivityMain/TextView-Stations)) (nav)

### G002 Search stations

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the search icon; Enter the station name or tag; Select the search result
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=e979302c02547a9c6ad1bc8249bfa763, view=2c99a68025f7a9740d20944a72b6a0c5(ActivityMain/ImageView-)) (heuristic)
  - act: CustomSetTextEvent(state=1d7a343892066261794d37e7bbe8b997, view=7ce7e11cbcb86fd33860ead61f4ba498(ActivityMain/AutoCompleteTextView-Search…), text=test) (mandatory_fill)
  - act: CustomTouchEvent(state=68659c61e077c9b3bbecdfdfc2278bd8, view=4bb0a63233ea7940483e2a83767353af(ActivityMain/ImageView-)) (heuristic)

### G003 Stop playback

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap the stop control in the player bar; Tap the stop control in the expanded player
- Remaining steps: Tap the stop control in the notification
- Completion ratio: 0.67
- Actions taken: 24
  - act: CustomTouchEvent(state=5526429f41421c13ccbe93423b891375, view=d9dfb0c6c11da5fdf0c58a9641598e3b(ActivityMain/TextView-Music Play)) (rule)
  - act: CustomTouchEvent(state=09aecc4203de26d250179f93d9fd495b, view=0cc9a49a8a94336a52eda1c773863023(ActivityMain/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=09aecc4203de26d250179f93d9fd495b, view=0cc9a49a8a94336a52eda1c773863023(ActivityMain/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=9667424eb17c26afcfd97ed959f8b9c2, view=0cc9a49a8a94336a52eda1c773863023(ActivityMain/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=09aecc4203de26d250179f93d9fd495b, view=aa273f88d117fbe0792ab3fcd5954e1b(ActivityMain/Button-)) (heuristic)
  - act: CustomTouchEvent(state=0cba75da585c783abdf609dfb547ae0b, view=cb83393487370e15b0e98408d7f862fe(ActivityMain/Button-CLEAR)) (llm)
  - act: CustomTouchEvent(state=09aecc4203de26d250179f93d9fd495b, view=aa273f88d117fbe0792ab3fcd5954e1b(ActivityMain/Button-)) (heuristic)
  - act: CustomTouchEvent(state=0cba75da585c783abdf609dfb547ae0b, view=08e5d77ca7e7986e16b5156885b3e4d8(ActivityMain/TextView-Stop playi)) (rule)

### G004 Remove a station

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Long-press the station you want to remove; Tap on the 'Favourites' screen
- Remaining steps: Select 'Remove' from the context menu; Confirm the removal by selecting 'Yes'
- Completion ratio: 0.50
- Credited from later features: G005, G010
- Actions taken: 21
  - act: LongTouchEvent(state=5526429f41421c13ccbe93423b891375, view=7eef29165e9f7b76152295e447261a68(ActivityMain/TextView-Your serve)) (heuristic)
  - act: LongTouchEvent(state=1011ab338d789cbd6ce11d2fc65d8a87, view=b68eb2991bac2407314854a0b4dda01e(ActivityMain/RecyclerView-)) (heuristic)
  - act: LongTouchEvent(state=1011ab338d789cbd6ce11d2fc65d8a87, view=b68eb2991bac2407314854a0b4dda01e(ActivityMain/RecyclerView-)) (heuristic)
  - act: LongTouchEvent(state=fc8a28ad223b3a6efa86e4fbb5b7fd1c, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: LongTouchEvent(state=1ebbcdce082af602a454c4d28f0b1a9b, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: LongTouchEvent(state=37762872a8603a7e2a31ddc571b3185a, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: LongTouchEvent(state=1ebbcdce082af602a454c4d28f0b1a9b, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=37762872a8603a7e2a31ddc571b3185a, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (rule)

### G005 View station details

- Status: **covered**
- Reason: The current screen shows the track details for 'Thanks for the Memory' by Ray Conniff, which aligns with the goal of viewing station details. The presence of album art and track history indicates that the feature is complete. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap a station; open its detail page
- Completion ratio: 1.00
- Credited from later features: G006
- Actions taken: 3
  - act: CustomTouchEvent(state=b5cad94046dae045e407cde2af4d304d, view=21b7bfcea49d2396f7157624af45dff4(ActivityMain/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=b5cad94046dae045e407cde2af4d304d, view=feabd995e1cdf00f679306c546dfc83c(ActivityMain/TextView-Classic Vi)) (nav)
  - act: CustomTouchEvent(state=a5b4e324df7c48c547d391b15f104bf5, view=4edfb0eb3e4587b8e856fd285b43fd78(ActivityMain/ImageView-)) (nav)

### G006 Open a station's homepage

- Status: **partial**
- Reason: The 'APPLY' button is tapped, indicating the feature is complete and no further action is needed.
- Feature source: guide
- Completed steps: Open the station detail page
- Remaining steps: tap the homepage/website link
- Completion ratio: 0.50
- Actions taken: 22
  - act: CustomTouchEvent(state=e3cf4d9aaf73f55e9be66cb3e7f7729a, view=7ce7e11cbcb86fd33860ead61f4ba498(ActivityMain/AutoCompleteTextView-Search…)) (llm)
  - act: CustomTouchEvent(state=e3cf4d9aaf73f55e9be66cb3e7f7729a, view=5a033df61af2aaf9abc30cd97eb5430a(ActivityMain/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=37762872a8603a7e2a31ddc571b3185a, view=303abcff6c7a82815d5fee64640b03e1(ActivityMain/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=5c1d8f29fb90832f1bb8bcd38d8d036e, view=aa273f88d117fbe0792ab3fcd5954e1b(ActivityMain/Button-)) (llm)
  - act: CustomTouchEvent(state=0cba75da585c783abdf609dfb547ae0b, view=5361209944cbf53e6da3d3fe313ca8a5(ActivityMain/TextView-10)) (llm)
  - act: CustomTouchEvent(state=0cba75da585c783abdf609dfb547ae0b, view=151168cfc7e21e1e9268c616deb0a19f(ActivityMain/SeekBar-)) (llm)
  - act: CustomTouchEvent(state=8cc6d6eda63671aa195a153bb67571e4, view=c6d035783b4bc6864272ab90dc71a6fc(ActivityMain/TextView-120)) (llm)
  - act: CustomTouchEvent(state=8cc6d6eda63671aa195a153bb67571e4, view=c6d035783b4bc6864272ab90dc71a6fc(ActivityMain/TextView-120)) (llm)

### G007 Record the stream

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Tap on the station you want to play; Tap the record button in the player
- Remaining steps: Select the recording duration; Tap the record button again to stop recording; Tap the save button to save the recording to a file; Navigate to the recorded files section to view the saved recording
- Completion ratio: 0.33
- Actions taken: 23
  - act: CustomTouchEvent(state=e3cf4d9aaf73f55e9be66cb3e7f7729a, view=cafd6095650258c54057858bc95f3e34(ActivityMain/TextView-avant-gard)) (nav)
  - act: CustomTouchEvent(state=fc0f1a3e5797b6f8382c3d0692515e84, view=cafd6095650258c54057858bc95f3e34(ActivityMain/TextView-avant-gard)) (nav)
  - act: CustomTouchEvent(state=924a243ef4727f2cd897c9052e0fe046, view=cafd6095650258c54057858bc95f3e34(ActivityMain/TextView-avant-gard)) (nav)
  - act: CustomTouchEvent(state=924a243ef4727f2cd897c9052e0fe046, view=cafd6095650258c54057858bc95f3e34(ActivityMain/TextView-avant-gard)) (nav)
  - act: CustomTouchEvent(state=fc0f1a3e5797b6f8382c3d0692515e84, view=d22d320a1daf4c28cf90c87fc4d76b75(ActivityMain/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=95c9b2d67d6a48681e2df25633fc2db0, view=cafd6095650258c54057858bc95f3e34(ActivityMain/TextView-avant-gard)) (nav)
  - act: CustomTouchEvent(state=95c9b2d67d6a48681e2df25633fc2db0, view=cafd6095650258c54057858bc95f3e34(ActivityMain/TextView-avant-gard)) (nav)
  - act: CustomTouchEvent(state=6bb742006ce45b2451a45fcb736de4f1, view=af96777d7e797973210acfd3eb4e9824(ActivityMain/TextView-Spinnin Th)) (nav)

### G008 View the played-track history

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Open the navigation drawer; Tap 'History' to view the played-track history
- Remaining steps: Scroll to find and tap 'History'
- Completion ratio: 0.67
- Credited from later features: G006
- Actions taken: 14
  - act: CustomTouchEvent(state=5f9a783dff7cd2f202cf1a4e082d2bd8, view=f212b2a898d3820b69bfea445395a23c(ActivityMain/Button-NO)) (heuristic)
  - act: CustomTouchEvent(state=951b9f9e35ccb98e96b9740c0b5887d0, view=97baf4a0a94819fa9b43129690e5df43(ActivityMain/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=e800de8550382e4ed81644434c983fa7, view=6af336b689da5a8b4e9a70ed7dafca51(ActivityMain/Button-)) (rule)
  - act: CustomTouchEvent(state=fc8a28ad223b3a6efa86e4fbb5b7fd1c, view=13b23cfdfc2aa8c49f91e20d81fbe8d3(ActivityMain/TextView-History)) (heuristic)
  - act: CustomTouchEvent(state=fc8a28ad223b3a6efa86e4fbb5b7fd1c, view=13b23cfdfc2aa8c49f91e20d81fbe8d3(ActivityMain/TextView-History)) (heuristic)
  - act: CustomTouchEvent(state=fc8a28ad223b3a6efa86e4fbb5b7fd1c, view=d7faaabca7500718b78ab0e97d0d9bb8(ActivityMain/TextView-History)) (heuristic)
  - act: CustomTouchEvent(state=fc8a28ad223b3a6efa86e4fbb5b7fd1c, view=d7faaabca7500718b78ab0e97d0d9bb8(ActivityMain/TextView-History)) (heuristic)
  - act: CustomTouchEvent(state=fc8a28ad223b3a6efa86e4fbb5b7fd1c, view=aa273f88d117fbe0792ab3fcd5954e1b(ActivityMain/Button-)) (heuristic)

### G009 Set a radio alarm

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the navigation drawer icon; Select the desired radio station; Select 'Alarm' from the navigation drawer; Tap on 'Set Alarm'; Enter the desired time for the alarm; Tap on 'Save' to set the alarm
- Completion ratio: 1.00
- Credited from later features: G002, G005, G008
- Actions taken: 19
  - act: CustomTouchEvent(state=fe2f27987763f79662b4e182ae53f665, view=082f757be8effe1d1f297c28924040fd(ActivityMain/TextView-Alarm)) (heuristic)
  - act: CustomTouchEvent(state=fe2f27987763f79662b4e182ae53f665, view=545c769801eb1d139ed6cac025189185(ActivityMain/TextView-Alarm)) (heuristic)
  - act: CustomTouchEvent(state=fe2f27987763f79662b4e182ae53f665, view=545c769801eb1d139ed6cac025189185(ActivityMain/TextView-Alarm)) (heuristic)
  - act: CustomTouchEvent(state=fe2f27987763f79662b4e182ae53f665, view=bc9a64a2a57f1bb7eceae9b8e9746f24(ActivityMain/Button-)) (llm)
  - act: CustomTouchEvent(state=fe2f27987763f79662b4e182ae53f665, view=bc9a64a2a57f1bb7eceae9b8e9746f24(ActivityMain/Button-)) (llm)
  - act: CustomTouchEvent(state=fe2f27987763f79662b4e182ae53f665, view=4648941591b4c682c2c26d04fa670980(ActivityMain/ViewGroup-)) (llm)
  - act: CustomSetTextEvent(state=a392b77ed49e82ef3c7d6b5df4b1eb9a, view=b014bc2bcf669a4a683f2ffad7f1781d(ActivityMain/EditText-Search…), text=test) (mandatory_fill)
  - act: CustomTouchEvent(state=57faa872e495b67d6c63fbd1f144d450, view=8a8c4997d348ef212c2d60c0952fb0e0(ActivityMain/TextView-Alarm)) (heuristic)

### G010 Import favourite stations

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Open the navigation drawer or the Favourites overflow menu
- Remaining steps: Tap the import option; Select the M3U file to import; Confirm the import action; Verify the imported stations in the Favourites menu
- Completion ratio: 0.20
- Actions taken: 18
  - act: CustomTouchEvent(state=4ccff107a6bb21199c49b4e399afe059, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=4ccff107a6bb21199c49b4e399afe059, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=4ccff107a6bb21199c49b4e399afe059, view=1f6cabbf994952fdbe65e406c8db357e(ActivityMain/ImageButton-)) (afford_search)
  - act: ScrollEvent(state=4ccff107a6bb21199c49b4e399afe059, view=47a6be0c27b0d9c14fc1879a1451aec8(ActivityMain/ScrollView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=933aacd971aff188178a3ddc03f95d81, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (heuristic)
  - act: CustomSetTextEvent(state=4ccff107a6bb21199c49b4e399afe059, view=b014bc2bcf669a4a683f2ffad7f1781d(ActivityMain/EditText-Search…), text=test) (heuristic)
  - act: CustomTouchEvent(state=57faa872e495b67d6c63fbd1f144d450, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=57faa872e495b67d6c63fbd1f144d450, view=04a4c890ec9b59a0e359b92e946f044c(ActivityMain/ImageView-)) (rule)

### G011 Cast a station

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Tap the 'Cast' icon in the toolbar; Select the 'Cast a station' feature; Tap the 'Cast' button to start streaming the station; Verify the station is playing on the Chromecast
- Remaining steps: Ensure the phone and the Chromecast are on the same network
- Completion ratio: 0.80
- Credited from later features: G002, G005
- Actions taken: 17
  - act: CustomTouchEvent(state=fc8a28ad223b3a6efa86e4fbb5b7fd1c, view=e54c3715a9ab422b185dd0271df2ab20(ActivityMain/TextView-Adroit Jaz)) (nav)
  - act: CustomTouchEvent(state=fc8a28ad223b3a6efa86e4fbb5b7fd1c, view=e54c3715a9ab422b185dd0271df2ab20(ActivityMain/TextView-Adroit Jaz)) (nav)
  - act: CustomTouchEvent(state=fe1419ae62d3dc504801650f3b9e7ed3, view=4edfb0eb3e4587b8e856fd285b43fd78(ActivityMain/ImageView-)) (nav)
  - act: CustomTouchEvent(state=01e209f882823f5d984228e875bc2928, view=c750590e12804fcea5d2a245ebbe78f2(ActivityMain/View-)) (rule)
  - act: CustomTouchEvent(state=01e209f882823f5d984228e875bc2928, view=c750590e12804fcea5d2a245ebbe78f2(ActivityMain/View-)) (rule)
  - act: CustomTouchEvent(state=0c029a8eef905601496d82cb0448b693, view=4edfb0eb3e4587b8e856fd285b43fd78(ActivityMain/ImageView-)) (nav)
  - act: CustomTouchEvent(state=01e209f882823f5d984228e875bc2928, view=de968d2009090bcc4d892ce7802716df(ActivityMain/Button-LYRICS)) (rule)
  - act: CustomTouchEvent(state=8df3f56a5a0c710504944d85ca7986ac, view=493d90d2761d60bead7cf954222583ea(ActivityMain/Button-YES)) (rule)

### G012 Control playback

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Select 'Start a station' from the menu; Tap on the 'control' option in the navigation menu
- Remaining steps: Open the RadioDroid app; Select 'playback' from the dropdown menu; Pull down the notification shade
- Completion ratio: 0.40
- Credited from later features: G005, G010
- Actions taken: 15
  - act: CustomTouchEvent(state=860a47f20b1e5537d25f1455e033745c, view=03191ceea54161417a87e685766097ea(ActivityMain/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=48f73db676eb3bf25e7d6e7f4ea05c72, view=4ba7260ef15b4c0c92714e3b0e2155df(ActivityMain/RadialTimePickerView$RadialPickerTouchHelper-)) (llm)
  - act: CustomTouchEvent(state=4f8174230f56fa0fe3d4be0a0dbe20e8, view=b64833f06c04165e061b2a9b38d0820d(ActivityMain/Button-OK)) (rule)
  - act: CustomTouchEvent(state=fc8a28ad223b3a6efa86e4fbb5b7fd1c, view=1f6cabbf994952fdbe65e406c8db357e(ActivityMain/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=e359359af6a9f4dc27ad1c8ff717304e, view=303abcff6c7a82815d5fee64640b03e1(ActivityMain/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=5c1d8f29fb90832f1bb8bcd38d8d036e, view=1f6cabbf994952fdbe65e406c8db357e(ActivityMain/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=1ebbcdce082af602a454c4d28f0b1a9b, view=303abcff6c7a82815d5fee64640b03e1(ActivityMain/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=5c1d8f29fb90832f1bb8bcd38d8d036e, view=1f6cabbf994952fdbe65e406c8db357e(ActivityMain/ImageButton-)) (heuristic)

### G013 Adjust the streaming buffer

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Open Settings; Tap 'Save'
- Remaining steps: Scroll to 'Playback'; Select 'Adjust the streaming buffer'; Enter the desired buffer size
- Completion ratio: 0.40
- Credited from later features: G006, G009
- Actions taken: 17
  - act: CustomTouchEvent(state=1ebbcdce082af602a454c4d28f0b1a9b, view=97616a1d8d237baedbd9f524edfe991c(ActivityMain/FrameLayout-)) (nav)
  - act: CustomTouchEvent(state=71fd447bda81e202f07cff44c6f9d43c, view=9d66accf53a321d4d029df3d0b20b9bb(ActivityMain/TextView-Player)) (llm)
  - act: CustomTouchEvent(state=35072e2b429569c268a00dd71661c482, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (nav)
  - act: CustomTouchEvent(state=59fcec123abc49817e3f38262c499d4f, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (nav)
  - act: CustomTouchEvent(state=59fcec123abc49817e3f38262c499d4f, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (nav)
  - act: CustomTouchEvent(state=59fcec123abc49817e3f38262c499d4f, view=303abcff6c7a82815d5fee64640b03e1(ActivityMain/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=e797ffea457612a451f5286492b703a5, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (nav)
  - act: CustomTouchEvent(state=e797ffea457612a451f5286492b703a5, view=e57823816b20ba6494f92a1dfcb2c24e(ActivityMain/TextView-Settings)) (nav)

### G014 Restrict playback

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Tap on the 'Settings' icon in the app's main menu.
- Remaining steps: Scroll down until you find the 'Network/Metered Connection' option.; Tap on the 'Network/Metered Connection' option.; Scroll down and select the 'Restrict Playback' option.; Tap on the 'Restrict Playback' option to enable or configure playback restrictions.
- Completion ratio: 0.20
- Actions taken: 16
  - act: CustomSetTextEvent(state=e797ffea457612a451f5286492b703a5, view=b014bc2bcf669a4a683f2ffad7f1781d(ActivityMain/EditText-Search…), text=test) (nav)
  - act: CustomSetTextEvent(state=6b4ccbff9b35a08dafe0097097070eb1, view=0c3251c7973006d6aa20903d7b4a9807(ActivityMain/EditText-test), text=test) (nav)
  - act: CustomSetTextEvent(state=6b4ccbff9b35a08dafe0097097070eb1, view=0c3251c7973006d6aa20903d7b4a9807(ActivityMain/EditText-test), text=test) (nav)
  - act: CustomTouchEvent(state=6b4ccbff9b35a08dafe0097097070eb1, view=1f6cabbf994952fdbe65e406c8db357e(ActivityMain/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=6b4ccbff9b35a08dafe0097097070eb1, view=04a4c890ec9b59a0e359b92e946f044c(ActivityMain/ImageView-)) (afford_search)
  - act: ScrollEvent(state=6b4ccbff9b35a08dafe0097097070eb1, view=47a6be0c27b0d9c14fc1879a1451aec8(ActivityMain/ScrollView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=6b4ccbff9b35a08dafe0097097070eb1, view=9e2adc813054de53e386b66c27529365(ActivityMain/TextView-Settings)) (llm)
  - act: CustomTouchEvent(state=6b4ccbff9b35a08dafe0097097070eb1, view=9e2adc813054de53e386b66c27529365(ActivityMain/TextView-Settings)) (llm)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
