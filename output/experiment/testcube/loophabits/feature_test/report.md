# Feature test report: Loop Habit Tracker

- Started: 2026-09-25 00:31:21
- Finished: 2026-09-25 00:56:59
- Features: 14
- Covered: 1
- Partial: 13
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 53% (mean completion ratio; the headline number)
- Coverage: 7% (features with every guide step matched)
- Stop reason: all_features_done
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 14
- Never attempted: 0
- Blocked then recovered on retry: 0
- Blocked still: 0

## Guide vs README-extracted

- Guide features: 14
- README-extracted features: 3
- In both: 0
- Guide-only: 14
- README-only: 3
  - guide-only: G001 Create a yes/no habit
  - guide-only: G002 Set a habit frequency
  - guide-only: G003 Add notes
  - guide-only: G004 Enter a value
  - guide-only: G005 Mark a day
  - guide-only: G006 View a habit's detailed
  - guide-only: G007 View the history calendar
  - guide-only: G008 View the frequency chart
  - guide-only: G009 Archive a habit
  - guide-only: G010 Delete a habit
  - guide-only: G011 Sort the habit list
  - guide-only: G012 Change the number of
  - README-only: F001 Complete first-run setup
  - README-only: F002 Import or export data
  - README-only: F003 Change app settings

## Text-field resolution

- Filled via credential.txt: 0
- Filled via VLM/Gemini: 4
- Unresolved: 0
- Online coverage: 7% (1/14) — live journal self-report (covered / extracted features).
- Offline coverage: 0% (0 covered / 38; 8 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 7% (mean completion ratio).

## Findings

### G001 Create a yes/no habit

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the app; Tap 'create' to finalize the habit creation
- Remaining steps: Tap the '+' floating action button; Select 'yes or no' from the options; Enter the name of the habit
- Completion ratio: 0.40
- Credited from later features: G002, G007
- Actions taken: 8
  - act: CustomTouchEvent(state=177fdc7afe1dec7c3486256be79b8f5b, view=b924ba654f94f334b645265d17ba1ff3(IntroActivity/Button-Got it)) (heuristic)
  - act: CustomTouchEvent(state=6260a914091f575e85c203ddbdfea418, view=f3f56843e085f4cafbb622958acf8412(IntroActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (nav)
  - act: CustomTouchEvent(state=d1dce200cc46c04017ef45da3895c85f, view=72f33801acfb92f965c35782b66fb2bf(MainActivity/TextView-Yes or No)) (heuristic)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, view=53617e3dd633dfdab80a3ab8f4043cae(EditHabitActivity/TextView-Create hab)) (nav)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, view=53617e3dd633dfdab80a3ab8f4043cae(EditHabitActivity/TextView-Create hab)) (nav)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, view=884f9034933fbe9841e257de1f185f85(EditHabitActivity/TextView-Notes)) (llm)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, view=884f9034933fbe9841e257de1f185f85(EditHabitActivity/TextView-Notes)) (llm)

### G002 Set a habit frequency

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the habit editor; Tap the save button; Tap the frequency row
- Remaining steps: Select the desired frequency
- Completion ratio: 0.75
- Credited from later features: G001, G003
- Actions taken: 8
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=d1dce200cc46c04017ef45da3895c85f, view=c74ecdcf285b5bbb7a78397c9a4157f7(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=d8cf92080fcd6153cee0cd0269308b1b, view=4655d7f369cbc1a09d49fb711534f700(MainActivity/CheckBox-)) (rule)
  - act: CustomTouchEvent(state=765cf14783492b2d2ede396f9bf17799, view=b920068e3260d965e4b05d1130e7356f(ListHabitsActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=765cf14783492b2d2ede396f9bf17799, view=b920068e3260d965e4b05d1130e7356f(ListHabitsActivity/TextView-You have n)) (nav)

### G003 Add notes

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the habit editor; Tap the save button; Tap the notes field
- Remaining steps: Enter the note text
- Completion ratio: 0.75
- Credited from later features: G001
- Actions taken: 13
  - act: CustomTouchEvent(state=5c0f2dcb6c2ff8982d9e1a9b6ae13ff3, view=1d6bfd36a2bd7ca9bc81100cef8b2a21(ListHabitsActivity/TextView-Yes or No)) (llm)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, view=b07c0943a6f7c81e55fd95736e7a9116(EditHabitActivity/EditText-(Optional))) (nav)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, view=b07c0943a6f7c81e55fd95736e7a9116(EditHabitActivity/EditText-(Optional))) (nav)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, view=f386ee48695614925c0dabaf3fb87ec1(EditHabitActivity/TextView-Frequency)) (llm)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, view=f386ee48695614925c0dabaf3fb87ec1(EditHabitActivity/TextView-Frequency)) (llm)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, x=540, y=1800) (llm)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, x=540, y=1664) (llm)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, view=884f9034933fbe9841e257de1f185f85(EditHabitActivity/TextView-Notes)) (rule)

### G004 Enter a value

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the habit list; Tap on the measurable habit row
- Remaining steps: Scroll to the 'Enter a value' section; Tap on the 'Enter a value' field; Enter the desired value; Tap the 'Save' button to confirm the value
- Completion ratio: 0.33
- Credited from later features: G002, G007
- Actions taken: 8
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9958377056a609aa8129627129fb8100(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=765c8dca5b62f093bf403f532c6f5bac, view=4655d7f369cbc1a09d49fb711534f700(MainActivity/CheckBox-)) (heuristic)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9958377056a609aa8129627129fb8100(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=3c3f464abede0baf01c5956bc4634d22, view=9f725c1a64d195beea4cb666180560f8(MainActivity/CheckBox-)) (heuristic)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=66586bddf711e633f06e1dd276786871(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=66586bddf711e633f06e1dd276786871(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=fc7975cf5d60535de0d9f04837aa3a70(MainActivity/RecyclerView-)) (llm)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (rule)

### G005 Mark a day

- Status: **partial**
- Reason: Onboarding already finished; main screen is visible.
- Feature source: guide
- Completed steps: Tap on the day cell in the habit list.; Long-press (or repeatedly tap, depending on the settings) the day cell.
- Remaining steps: Select the 'Mark as Skipped' option from the menu.; Confirm the skip action by tapping the 'Confirm' button.; The app updates the day cell to show the skipped state.
- Completion ratio: 0.40
- Credited from later features: G006, G009

### G006 View a habit's detailed

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the habit list; Tap the habit name; Select the habit's detailed statistics; Tap the habit's detailed statistics; View the habit's detailed statistics
- Completion ratio: 1.00
- Credited from later features: G002, G007
- Actions taken: 13
  - act: CustomTouchEvent(state=765cf14783492b2d2ede396f9bf17799, view=49d2b5f2e9ed92cab05e43a5f76b7428(ListHabitsActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=5c0f2dcb6c2ff8982d9e1a9b6ae13ff3, view=2e2bdc013af549e8230434b3e58c1b08(ListHabitsActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=765cf14783492b2d2ede396f9bf17799, view=0f5bd7f1d523c5bbdd24b6f701af4bb8(ListHabitsActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=8c10b4cbeace30870e1a88693405e6c9, view=a816ac152f900595a2f5ab9c48ba88e6(ListHabitsActivity/CheckBox-)) (rule)
  - act: CustomTouchEvent(state=765cf14783492b2d2ede396f9bf17799, view=0f5bd7f1d523c5bbdd24b6f701af4bb8(ListHabitsActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=416725c266a55b7b9520f3baf779bb92, view=93fc7c80d1188310d78536d51575bf87(ListHabitsActivity/CheckBox-)) (rule)
  - act: CustomTouchEvent(state=765cf14783492b2d2ede396f9bf17799, view=f883d59479293121a29722c8afd3641f(ListHabitsActivity/View-)) (heuristic)
  - act: CustomTouchEvent(state=765cf14783492b2d2ede396f9bf17799, view=b6c620c82b8a893e6e1c90fbddcd83a6(ListHabitsActivity/Button-)) (rule)

### G007 View the history calendar

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the habit detail
- Remaining steps: Scroll to the History card; Tap on the History card; Tap on the Calendar icon; Select the desired date on the calendar
- Completion ratio: 0.20
- Actions taken: 9
  - act: CustomTouchEvent(state=d1dce200cc46c04017ef45da3895c85f, view=c74ecdcf285b5bbb7a78397c9a4157f7(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=d1dce200cc46c04017ef45da3895c85f, view=a639602b2b7ae8b94833b27b17527b34(MainActivity/LinearLayout-)) (rule)
  - act: CustomSetTextEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, view=ea6266e53fe46e96fd06981374f34d48(EditHabitActivity/EditText-e.g. Exerc), text=test) (llm)
  - act: CustomSetTextEvent(state=44f3db739c0f46a03884645f191d1c2c, view=6fcea44b38b114552c9457fab81d2fcf(EditHabitActivity/EditText-test), text=test) (rule)
  - act: CustomTouchEvent(state=44f3db739c0f46a03884645f191d1c2c, view=884f9034933fbe9841e257de1f185f85(EditHabitActivity/TextView-Notes)) (llm)
  - act: CustomTouchEvent(state=44f3db739c0f46a03884645f191d1c2c, view=53617e3dd633dfdab80a3ab8f4043cae(EditHabitActivity/TextView-Create hab)) (llm)
  - act: CustomTouchEvent(state=44f3db739c0f46a03884645f191d1c2c, view=53617e3dd633dfdab80a3ab8f4043cae(EditHabitActivity/TextView-Create hab)) (llm)

### G008 View the frequency chart

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the habit detail
- Remaining steps: Scroll to the Frequency card; Select the Frequency chart; Check the displayed frequency data
- Completion ratio: 0.25
- Actions taken: 8
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=d1dce200cc46c04017ef45da3895c85f, view=a639602b2b7ae8b94833b27b17527b34(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=4c5085db92fa4e2eec38001c1ef3e16e, view=94f5fdddde867c68a28175b7cd9b605d(EditHabitActivity/TextView-Every day)) (heuristic)
  - act: CustomTouchEvent(state=d6d1cc424096320e83ea6347aafd7160, view=b71868abf48450f305dbc411f275e379(EditHabitActivity/TextView-times in)) (nav)
  - act: CustomTouchEvent(state=d6d1cc424096320e83ea6347aafd7160, view=b71868abf48450f305dbc411f275e379(EditHabitActivity/TextView-times in)) (nav)
  - act: CustomTouchEvent(state=d6d1cc424096320e83ea6347aafd7160, view=81acd9ba843ca4713ec6a98199ea9366(EditHabitActivity/TextView-days)) (afford_search)
  - act: CustomTouchEvent(state=d6d1cc424096320e83ea6347aafd7160, view=ffd4eede60eeaeb8714073862a69f8f2(EditHabitActivity/TextView-times per )) (nav)
  - act: CustomTouchEvent(state=d6d1cc424096320e83ea6347aafd7160, view=81acd9ba843ca4713ec6a98199ea9366(EditHabitActivity/TextView-days)) (llm)

### G009 Archive a habit

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the habit list; Locate the habit you want to archive; Long-press the habit
- Remaining steps: Select the 'Archive' option from the menu; Confirm the archive action
- Completion ratio: 0.60
- Actions taken: 11
  - act: LongTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (rule)

### G010 Delete a habit

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the habit list; Scroll to find the habit you want to delete; Long-press the habit; Select the delete option
- Remaining steps: Confirm the deletion
- Completion ratio: 0.80
- Credited from later features: G007, G009, G012
- Actions taken: 9
  - act: LongTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (heuristic)
  - act: LongTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (heuristic)
  - act: LongTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (afford_search)
  - act: LongTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (heuristic)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=9107902f1e3a521eb2e60dbcdc0230ce(MainActivity/TextView-You have n)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (rule)

### G011 Sort the habit list

- Status: **partial**
- Reason: The current screen is for creating a habit, not for sorting the habit list.
- Feature source: guide
- Completed steps: Open the habit list; Tap 'Sort the habit list'; Tap the overflow menu
- Remaining steps: Select 'Sort' from the overflow menu; Select 'Reorder habits manually'; Tap 'Reorder habits manually'
- Completion ratio: 0.50
- Credited from later features: G006, G012
- Actions taken: 2
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=d1dce200cc46c04017ef45da3895c85f, view=72f33801acfb92f965c35782b66fb2bf(MainActivity/TextView-Yes or No)) (llm)

### G012 Change the number of

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Appearance' settings option in the app's main menu.; Select the 'Columns' option within the appearance settings.
- Remaining steps: Enter the desired number of day columns you want to display.; Confirm the changes by tapping the 'Save' button.; Rotate the device or resize the window to see the updated number of day columns.
- Completion ratio: 0.40
- Actions taken: 9
  - act: CustomTouchEvent(state=71178c04f9efaf3ab240753c1ead5210, view=fa0979b32c851c95dc3cb65134b17f57(MainActivity/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=68dad995bf69788300dc3a36ba02f8e7, view=27b36884e2e6467518276b9cab1ef95c(SettingsActivity/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=68dad995bf69788300dc3a36ba02f8e7, view=de67757e09e313787c1a3f5849ac9452(SettingsActivity/TextView-Differenti)) (heuristic)
  - act: CustomTouchEvent(state=856122f224d93e0ce98dacb7a625aa4e, view=de67757e09e313787c1a3f5849ac9452(SettingsActivity/TextView-Differenti)) (heuristic)
  - act: CustomTouchEvent(state=68dad995bf69788300dc3a36ba02f8e7, view=de67757e09e313787c1a3f5849ac9452(SettingsActivity/TextView-Differenti)) (heuristic)
  - act: CustomTouchEvent(state=856122f224d93e0ce98dacb7a625aa4e, view=de67757e09e313787c1a3f5849ac9452(SettingsActivity/TextView-Wait until)) (rule)
  - act: CustomTouchEvent(state=856122f224d93e0ce98dacb7a625aa4e, view=62d3b2c4fabe783bbd891f9b837a7970(SettingsActivity/TextView-Extend day)) (rule)
  - act: CustomTouchEvent(state=856122f224d93e0ce98dacb7a625aa4e, view=de67757e09e313787c1a3f5849ac9452(SettingsActivity/TextView-Replaces g)) (rule)

### G013 Enable persistent reminder notifications

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open Settings; Save the settings
- Remaining steps: Scroll to find the sticky/persistent notification option; Select the sticky/persistent notification option; Toggle the persistent reminder notification setting
- Completion ratio: 0.40
- Credited from later features: G012
- Actions taken: 10
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=71178c04f9efaf3ab240753c1ead5210, view=fa0979b32c851c95dc3cb65134b17f57(MainActivity/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=0fca48f3d02701870f89cee514b8b148, view=eae15d5f2c95d692c8cd580c8c095beb(MainActivity/Button-Close app)) (llm)
  - act: CustomTouchEvent(state=71178c04f9efaf3ab240753c1ead5210, view=8e9327bd5bcd094ea3df30723522314f(MainActivity/TextView-Dark theme)) (nav)
  - act: CustomTouchEvent(state=aa213e9cf6ade7e37dc6f839ea4444b4, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=71178c04f9efaf3ab240753c1ead5210, view=8e9327bd5bcd094ea3df30723522314f(MainActivity/TextView-Dark theme)) (nav)
  - act: CustomTouchEvent(state=765cf14783492b2d2ede396f9bf17799, view=b6c620c82b8a893e6e1c90fbddcd83a6(ListHabitsActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=10f9118ddefcff969a34cb49e3401dd6, view=93fc7c80d1188310d78536d51575bf87(ListHabitsActivity/CheckBox-)) (heuristic)

### G014 Check off a habit

- Status: **partial**
- Reason: Already on the home screen.
- Feature source: guide
- Completed steps: Tap the home screen widget for the habit you want to check off.; Tap the checkmark area to record the habit for today without opening the app.
- Remaining steps: Locate the checkmark area on the widget.
- Completion ratio: 0.67
- Credited from later features: G007
- Actions taken: 1
  - act: (screen already shows this destination) (rule)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
