# Feature test report: Loop Habit Tracker

- Started: 2026-10-25 17:31:44
- Finished: 2026-10-25 18:30:10
- Features: 14
- Covered: 5
- Partial: 6
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 75% (mean completion ratio; the headline number)
- Coverage: 36% (features with every guide step matched)
- Stop reason: budget_time
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

- Filled via credential.txt: 4
- Filled via VLM/Gemini: 8
- Unresolved: 0
- Online coverage: 36% (5/14) — live journal self-report (covered / extracted features).
- Offline coverage: not computed (no ground-truth JSON).

## Findings

### G001 Create a yes/no habit

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open the app; Select 'yes' or 'no' for the habit; Tap the '+' floating action button; Tap 'create'
- Remaining steps: Select 'yes or no' from the menu; Enter a habit name
- Completion ratio: 0.67
- Credited from later features: G002, G003, G006
- Actions taken: 32
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=56404a350ae7410dd9eaf4ee119a24fb(SettingsActivity/Switch-)) (heuristic)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=27b36884e2e6467518276b9cab1ef95c(SettingsActivity/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=06b160693cdf92f6c10423c62c0c5a43(SettingsActivity/Switch-)) (heuristic)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=493e5d92f7087b5cb0741cf81d73b302(SettingsActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=27b36884e2e6467518276b9cab1ef95c(SettingsActivity/TextView-Settings)) (rule)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=65ab674d113117f090ebad4edb42a54b(SettingsActivity/TextView-Interface)) (rule)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=65ab674d113117f090ebad4edb42a54b(SettingsActivity/TextView-Interface)) (rule)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=2f0ec387b1cbe562295479b38cb0d4ea(SettingsActivity/TextView-Toggle wit)) (llm)

### G002 Set a habit frequency

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the habit editor; Tap the save button; Tap the frequency row
- Remaining steps: Select the desired frequency
- Completion ratio: 0.75
- Credited from later features: G001, G004
- Actions taken: 29
  - act: CustomTouchEvent(state=d11e6d2add90502b25177533c45c1763, view=0f5bd7f1d523c5bbdd24b6f701af4bb8(ListHabitsActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=90ef907c08014d07a34d2c34b0e7e75d(SettingsActivity/TextView-Disable an)) (llm)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=2f0ec387b1cbe562295479b38cb0d4ea(SettingsActivity/TextView-Toggle wit)) (llm)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=62d3b2c4fabe783bbd891f9b837a7970(SettingsActivity/TextView-Extend day)) (rule)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=62d3b2c4fabe783bbd891f9b837a7970(SettingsActivity/TextView-Extend day)) (llm)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=0d6c33216cfe01ef8bc6eb421aecd396(SettingsActivity/TextView-Show quest)) (llm)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=0d6c33216cfe01ef8bc6eb421aecd396(SettingsActivity/TextView-Show quest)) (llm)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=9d5dd97a7868a95a9d1131df37dec4d7(SettingsActivity/TextView-Reverse or)) (llm)

### G003 Add notes

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the habit editor; Tap the notes field; Enter the note text; Tap the save button
- Completion ratio: 1.00
- Actions taken: 9
  - act: CustomTouchEvent(state=76be00baa046a4f81e67fa69f889e186, view=2e32984a29613ab5eb4c6223bd8631e6(MainActivity/TextView-Habits)) (nav)
  - act: CustomTouchEvent(state=76be00baa046a4f81e67fa69f889e186, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=d8cf92080fcd6153cee0cd0269308b1b, view=4655d7f369cbc1a09d49fb711534f700(MainActivity/CheckBox-)) (rule)
  - act: CustomTouchEvent(state=208c54ae66e941f2eefaf63593b649ea, view=49d2b5f2e9ed92cab05e43a5f76b7428(ListHabitsActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=d78a148fd1b9a6a33449addab0a1e21d, view=1d6bfd36a2bd7ca9bc81100cef8b2a21(ListHabitsActivity/TextView-Yes or No)) (llm)
  - act: CustomTouchEvent(state=eb50c2909d7c962e520fa93417a5c059, view=884f9034933fbe9841e257de1f185f85(EditHabitActivity/TextView-Notes)) (heuristic)
  - act: CustomSetTextEvent(state=eb50c2909d7c962e520fa93417a5c059, view=ea6266e53fe46e96fd06981374f34d48(EditHabitActivity/EditText-e.g. Exerc), text=no) (mandatory_fill)
  - act: CustomTouchEvent(state=a325d80dd607ffccb92dda861da1ac23, view=cd8ef146b98b2518ac0e44ca228ec490(EditHabitActivity/Button-SAVE)) (heuristic)

### G004 Enter a value

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the habit list; Tap on the habit row for the measurable habit; Tap on the 'Enter a value' option; Enter the value for the habit; Tap the 'Save' button to confirm the value entry
- Completion ratio: 1.00
- Actions taken: 5
  - act: CustomTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=a479532c1e93ed50ea941120081f658b, view=5b585e813c4a74cd955dcb950364c79c(MainActivity/TextView-Measurable)) (heuristic)
  - act: CustomSetTextEvent(state=a94d51032704fb36f22c97cb0f8e0d4f, view=26594f1a25b9e1ded85cfda11ca239f8(EditHabitActivity/EditText-e.g. Run), text=100) (mandatory_fill)
  - act: CustomSetTextEvent(state=127abecc70e0f2b5b23403c6dcfdc1a2, view=fdac9958ad7817e625c72595e939dc53(EditHabitActivity/EditText-100), text=100) (mandatory_fill)
  - act: CustomTouchEvent(state=127abecc70e0f2b5b23403c6dcfdc1a2, view=cd8ef146b98b2518ac0e44ca228ec490(EditHabitActivity/Button-SAVE)) (heuristic)

### G005 Mark a day

- Status: **partial**
- Reason: Onboarding already finished; main screen is visible.
- Feature source: guide
- Completed steps: Open the Loop Habit Tracker app; Navigate to the habit list; Navigate back to the habit list; Long-press (or repeatedly tap, depending on the settings) the day cell
- Remaining steps: Choose the 'skip' state; Confirm the skip action
- Completion ratio: 0.67
- Credited from later features: G002, G004, G009

### G006 View a habit's detailed

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open the habit list; Tap the habit name; Select the habit's detailed statistics; Tap the 'Detailed' option
- Remaining steps: Scroll to the detailed statistics section; Check the visibly different app state
- Completion ratio: 0.67
- Credited from later features: G009, G012
- Actions taken: 29
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=ba8b36c35b51108bd503e1b971b119b2(SettingsActivity/TextView-Show days )) (llm)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=8034ef4485546f3524244301da75449e(SettingsActivity/TextView-Use pure b)) (llm)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=de67757e09e313787c1a3f5849ac9452(SettingsActivity/TextView-Disable co)) (llm)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=de67757e09e313787c1a3f5849ac9452(SettingsActivity/TextView-Disable co)) (llm)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=152f7016dbbe929505ec714b67e9f51d(SettingsActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=d8cf92080fcd6153cee0cd0269308b1b, view=8e9327bd5bcd094ea3df30723522314f(MainActivity/TextView-Dark theme)) (rule)
  - act: CustomTouchEvent(state=bff6a8782d239f6440f8b090cd6f4711, view=08fb153294f1a0f5896ef5ee51114226(ListHabitsActivity/TextView-no)) (llm)

### G007 View the history calendar

- Status: **covered**
- Reason: Covered by shared-flow reuse of C003.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the habit detail; Scroll to the History card; Tap on the History card; Select the calendar view; Confirm the calendar view is selected; Check the app state for the history calendar
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=71178c04f9efaf3ab240753c1ead5210, view=9f725c1a64d195beea4cb666180560f8(MainActivity/CheckBox-)) (rule)
  - act: CustomTouchEvent(state=bff6a8782d239f6440f8b090cd6f4711, view=49d2b5f2e9ed92cab05e43a5f76b7428(ListHabitsActivity/Button-)) (heuristic)

### G008 View the frequency chart

- Status: **covered**
- Reason: Covered by shared-flow reuse of C003.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the habit detail; Scroll to the Frequency card; Select the Frequency chart; Check the chart for the desired frequency; End the feature interaction
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=d8cf92080fcd6153cee0cd0269308b1b, view=4655d7f369cbc1a09d49fb711534f700(MainActivity/CheckBox-)) (rule)
  - act: CustomTouchEvent(state=bff6a8782d239f6440f8b090cd6f4711, view=49d2b5f2e9ed92cab05e43a5f76b7428(ListHabitsActivity/Button-)) (heuristic)

### G009 Archive a habit

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Tap on the 'Habits' section in the navigation drawer; Select the habit you want to archive; Long-press the habit
- Remaining steps: Select 'Archive' from the context menu; Confirm the archive action
- Completion ratio: 0.60
- Actions taken: 37
  - act: LongTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=9958377056a609aa8129627129fb8100(MainActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=9958377056a609aa8129627129fb8100(MainActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=9958377056a609aa8129627129fb8100(MainActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (afford_search)
  - act: LongTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=9958377056a609aa8129627129fb8100(MainActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=7026a0e89ba3e74382f66161421920aa(MainActivity/TextView-no)) (llm)
  - act: LongTouchEvent(state=dd40287197d595c265537f6a327e7a85, view=2b77c1f7d8099bec932f11436186dadf(MainActivity/TextView-1)) (heuristic)
  - act: CustomTouchEvent(state=dd40287197d595c265537f6a327e7a85, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (rule)

### G010 Delete a habit

- Status: **partial**
- Reason: Retry round 3; budget remains.
- Feature source: guide
- Completed steps: Open the habit list; Confirm the deletion; Scroll down to find the habit you want to delete; Long-press the habit you want to delete
- Remaining steps: Select the delete option
- Completion ratio: 0.80
- Credited from later features: G002, G004, G006, G009
- Actions taken: 33
  - act: CustomTouchEvent(state=79f3a193d92fa3ed24146d0d2bba1679, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (rule)
  - act: LongTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (nav)
  - act: LongTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (nav)
  - act: LongTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (nav)
  - act: LongTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (afford_search)
  - act: LongTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (nav)
  - act: CustomTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=86dda9cf49b1cc84f1157a5c09bd2c02(MainActivity/Button-)) (llm)
  - act: LongTouchEvent(state=a479532c1e93ed50ea941120081f658b, view=db267a17579c53282bfe6785142fc587(MainActivity/LinearLayout-)) (rule)

### G011 Sort the habit list

- Status: **pending**
- Reason: Retry round 3; budget remains.
- Feature source: guide
- Completed steps: Open the habit list; Choose 'Sort by Name'; Select 'Sort'
- Remaining steps: Tap the overflow menu; Confirm the sort action
- Completion ratio: 0.60
- Credited from later features: G002, G006, G009
- Actions taken: 24
  - act: CustomTouchEvent(state=a479532c1e93ed50ea941120081f658b, view=db267a17579c53282bfe6785142fc587(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=a94d51032704fb36f22c97cb0f8e0d4f, view=667b0a6ac743a1b4d3c6ae175ce13bf9(EditHabitActivity/TextView-Color)) (nav)
  - act: CustomTouchEvent(state=a94d51032704fb36f22c97cb0f8e0d4f, view=667b0a6ac743a1b4d3c6ae175ce13bf9(EditHabitActivity/TextView-Color)) (nav)
  - act: CustomTouchEvent(state=a94d51032704fb36f22c97cb0f8e0d4f, view=cd8ef146b98b2518ac0e44ca228ec490(EditHabitActivity/Button-SAVE)) (llm)
  - act: CustomSetTextEvent(state=a94d51032704fb36f22c97cb0f8e0d4f, view=26594f1a25b9e1ded85cfda11ca239f8(EditHabitActivity/EditText-e.g. Run), text=test) (llm)
  - act: CustomTouchEvent(state=182ae9b10036622141ba605f4eb5347f, view=53617e3dd633dfdab80a3ab8f4043cae(EditHabitActivity/TextView-Create hab)) (nav)
  - act: CustomTouchEvent(state=182ae9b10036622141ba605f4eb5347f, view=53617e3dd633dfdab80a3ab8f4043cae(EditHabitActivity/TextView-Create hab)) (nav)
  - act: CustomTouchEvent(state=182ae9b10036622141ba605f4eb5347f, view=884f9034933fbe9841e257de1f185f85(EditHabitActivity/TextView-Notes)) (llm)

### G012 Change the number of

- Status: **pending**
- Reason: Retry round 3; budget remains.
- Feature source: guide
- Completed steps: Confirm the changes by tapping the 'Done' or 'Save' button.; Tap on the 'Appearance' settings option in the app.
- Remaining steps: Scroll down to find the 'Number of Days' setting.; Select the 'Number of Days' setting.; Enter the desired number of days you want to display.
- Completion ratio: 0.40
- Credited from later features: G003
- Actions taken: 24
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=ba8b36c35b51108bd503e1b971b119b2(SettingsActivity/TextView-Show days )) (rule)
  - act: CustomTouchEvent(state=79f3a193d92fa3ed24146d0d2bba1679, view=66586bddf711e633f06e1dd276786871(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=79f3a193d92fa3ed24146d0d2bba1679, view=fc7975cf5d60535de0d9f04837aa3a70(MainActivity/RecyclerView-)) (rule)
  - act: CustomTouchEvent(state=79f3a193d92fa3ed24146d0d2bba1679, view=fc7975cf5d60535de0d9f04837aa3a70(MainActivity/RecyclerView-)) (rule)
  - act: CustomTouchEvent(state=79f3a193d92fa3ed24146d0d2bba1679, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=79f3a193d92fa3ed24146d0d2bba1679, view=9958377056a609aa8129627129fb8100(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=d11e6d2add90502b25177533c45c1763, view=b6c620c82b8a893e6e1c90fbddcd83a6(ListHabitsActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=c1c9d962f1374a441f1c673fe5e9d8af, view=a816ac152f900595a2f5ab9c48ba88e6(ListHabitsActivity/CheckBox-)) (heuristic)

### G013 Enable persistent reminder notifications

- Status: **pending**
- Reason: Retry round 3; budget remains.
- Feature source: guide
- Completed steps: Open Settings; Save the settings
- Remaining steps: Scroll to find the sticky/persistent notification option; Select the sticky/persistent notification option; Enable the sticky/persistent notification
- Completion ratio: 0.40
- Credited from later features: G002, G003
- Actions taken: 24
  - act: CustomTouchEvent(state=f76bedeec35f6cb3592dd40f42494fc7, view=434ac7c8c71405ad45422218e9a814fe(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=d8cf92080fcd6153cee0cd0269308b1b, view=fa0979b32c851c95dc3cb65134b17f57(MainActivity/TextView-Settings)) (nav)
  - act: CustomTouchEvent(state=66a1e832b01929ec8292d183fa0a6580, x=54, y=96) (llm)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=493e5d92f7087b5cb0741cf81d73b302(SettingsActivity/LinearLayout-)) (nav)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=90ef907c08014d07a34d2c34b0e7e75d(SettingsActivity/TextView-Disable an)) (nav)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=06b160693cdf92f6c10423c62c0c5a43(SettingsActivity/Switch-)) (afford_search)
  - act: ScrollEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=e4c2d2c3dd9ba496328c325cfc8d0ded(SettingsActivity/RecyclerView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=dea033550c5b4da805d1fe17eb50b9e3, view=b02de247df48695451e28c457dcf203d(SettingsActivity/TextView-Enable ski)) (rule)

### G014 Check off a habit

- Status: **covered**
- Reason: Already on the home screen. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap the checkmark area on the placed home screen widget; the habit is recorded for today without opening the app
- Completion ratio: 1.00
- Credited from later features: G006

## Shared flows detected

2 reuse(s); 9 action(s) skipped by not re-executing a known terminal flow.

- `G007` reused `C003` (from G003), skipped 5 action(s)
- `G008` reused `C003` (from G003), skipped 4 action(s)

See `session.json` and `log.md` in this folder for the full trace.
