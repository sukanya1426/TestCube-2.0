# Feature test report: Fossify Clock

- Started: 2026-09-25 04:59:13
- Finished: 2026-09-25 05:26:30
- Features: 16
- Covered: 13
- Partial: 3
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 94% (mean completion ratio; the headline number)
- Coverage: 81% (features with every guide step matched)
- Stop reason: all_features_done
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 14
- Never attempted: 0
- Blocked then recovered on retry: 0
- Blocked still: 0

## Guide vs README-extracted

- Guide features: 14
- README-extracted features: 6
- In both: 0
- Guide-only: 14
- README-only: 6
  - guide-only: G001 View the current time
  - guide-only: G002 Add a time zone
  - guide-only: G003 Remove
  - guide-only: G004 Open the full-screen clock
  - guide-only: G005 Create an alarm
  - guide-only: G006 Enable
  - guide-only: G007 Edit an alarm
  - guide-only: G008 Delete an alarm
  - guide-only: G009 Set the alarm sound
  - guide-only: G010 Snooze
  - guide-only: G011 Configure the snooze duration
  - guide-only: G012 Make the alarm volume
  - README-only: F001 Close or skip the tutorial
  - README-only: F002 Leave any first-run analytics or settings screen
  - README-only: F003 Tap Create Database or Open Database if shown
  - README-only: F004 Enter a file name if asked and confirm Save
  - README-only: F005 Reach the home or main screen
  - README-only: F006 Change app settings

## Text-field resolution

- Filled via credential.txt: 0
- Filled via VLM/Gemini: 2
- Unresolved: 0
- Online coverage: 81% (13/16) — live journal self-report (covered / extracted features).
- Offline coverage: 19% (5 covered / 26; 5 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 30% (mean completion ratio).

## Findings

### G001 View the current time

- Status: **partial**
- Reason: The current time and date are already displayed, indicating that the feature to view the current time has been successfully completed.
- Feature source: guide
- Completed steps: Tap on the Clock tab; Open the app
- Remaining steps: Verify the current time and date are displayed
- Completion ratio: 0.67
- Credited from later features: G002, G003

### G002 Add a time zone

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Clock tab
- Remaining steps: tap the "+" floating action button
- Completion ratio: 0.50
- Credited from later features: G003
- Actions taken: 8
  - act: CustomTouchEvent(state=612761bcc1a708e5f1b844047e25b1df, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (llm)
  - act: CustomTouchEvent(state=e5eb16c38d1a0e6f9398ce90ad72ab8d, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (llm)
  - act: CustomTouchEvent(state=1e124f4bc56feeb2df042c819aa739c8, x=821, y=1786) (visual_ground)
  - act: CustomTouchEvent(state=87522b0c688f612702018c63cc6972e6, view=332908b0d475e1adef729c449414baed(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=2d8e10f3d4580c1c1324da0d023219de, view=bf58c74d9bea16c477b15152543d37dd(MainActivity/RadioButton-Timer dura)) (nav)
  - act: CustomTouchEvent(state=1b1da5afbc7ff065866e3ef5cc0bfdac, view=9a84ab5926ca74996de79db9ea6b4f9b(MainActivity/RadioButton-Timer dura)) (nav)
  - act: CustomTouchEvent(state=1b1da5afbc7ff065866e3ef5cc0bfdac, view=9a84ab5926ca74996de79db9ea6b4f9b(MainActivity/RadioButton-Timer dura)) (nav)
  - act: CustomTouchEvent(state=1b1da5afbc7ff065866e3ef5cc0bfdac, view=d4f2e2e7923ba38f0c040c37a41af3d2(MainActivity/Button-OK)) (rule)

### G003 Remove

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the Clock tab; tap the "+" button and untick a zone to remove it, or open Settings
- Completion ratio: 1.00
- Actions taken: 13
  - act: CustomTouchEvent(state=1c0e2eb573fd3edfb441522532070a34, x=612, y=1795) (llm)
  - act: CustomTouchEvent(state=fd8281209cf6ab4916cad8519d8a3084, view=c218252482c6405139d501cb8a08b181(MainActivity/ImageView-)) (visual_ground)
  - act: CustomTouchEvent(state=534855ef1cea6063f7f6635d82735b93, view=a3cb79f6caf1077f593994a021034f30(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=cc784a7f13062cc182d3cd06d1f46b49, view=a3cb79f6caf1077f593994a021034f30(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=d9301e6060a0707766d3a3b10df8eded, view=a3cb79f6caf1077f593994a021034f30(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=91c5b8fe6c7049bd8eca75a623f59b73, view=4ba0a41a3fb049580d8c7fe6d889dbf7(MainActivity/TextView-Stopwatch)) (heuristic)
  - act: CustomTouchEvent(state=35e53a6f817d4d4fd6079c910f34acfc, view=b5a1e7e663bf1689ac9cc12e0c83d348(MainActivity/ImageView-)) (rule)
  - act: (screen already shows this destination) (rule)

### G004 Open the full-screen clock

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the Clock tab; Tap the clock face; Select the full-screen option; Confirm the transition to the full-screen clock
- Completion ratio: 1.00
- Actions taken: 9
  - act: CustomTouchEvent(state=e14f7ae38e014dcefb4e2454bb0afcf8, x=78, y=1097) (visual_ground)
  - act: CustomTouchEvent(state=f40e46163ae94a41f494750e3cd9a23d, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (visual_ground)
  - act: CustomTouchEvent(state=6480850a32fb56307b03dd78e40bd839, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (visual_ground)
  - act: CustomTouchEvent(state=b1da767e1a75595e8cf45e030dc34077, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (visual_ground)
  - act: CustomTouchEvent(state=f5eb8c0b8874b1cdd614ae1b629de7e2, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (visual_ground)
  - act: CustomTouchEvent(state=e0c51a766de8c8b9b721f94f6fa283b1, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (visual_ground)
  - act: CustomTouchEvent(state=9ac815ceabd13f12c6542215062cef76, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (visual_ground)
  - act: CustomTouchEvent(state=101165e6733e0e2eb6e5f3c18df0a909, view=4425087dbe3f5a9552c3749da8d2a869(MainActivity/TextView-Fri, 25 Se)) (heuristic)

### G005 Create an alarm

- Status: **covered**
- Reason: Covered by shared-flow reuse of C002.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the Alarm tab; tap the "+" button
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=ace9ba9d6433ab7181388b0c08c7626f, x=255, y=1102) (visual_ground)
  - act: CustomTouchEvent(state=2f216a45c98ddefdd261b22f214d9a66, x=256, y=1108) (visual_ground)
  - act: CustomTouchEvent(state=211eae9bea558c1ebaf8efb6af11cc9c, x=255, y=1101) (visual_ground)

### G006 Enable

- Status: **covered**
- Reason: Covered by shared-flow reuse of C002.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the Alarm tab; tap the toggle switch beside the alarm row
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=196582e425c7b0690f563ab55374b31c, x=259, y=1112) (visual_ground)
  - act: CustomTouchEvent(state=bd5cecb40c77d56bbcfe3146e27a42a4, x=256, y=1116) (visual_ground)
  - act: CustomTouchEvent(state=b1c18345b881cae12608c0eb34f07e39, x=250, y=1097) (visual_ground)

### G007 Edit an alarm

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the Alarm tab; Tap the alarm row; Tap the 'Edit' option; Select the alarm you want to edit; Enter the new time for the alarm; Tap the 'Save' button
- Completion ratio: 1.00
- Credited from later features: G002
- Actions taken: 18
  - act: CustomSetTextEvent(state=11f931f9193e3444daabba5d9cbb5d01, view=98d66b392be1cfea8d28c1e4bf36adb7(MainActivity/EditText-Label), text=TestCube Label) (mandatory_fill)
  - act: CustomTouchEvent(state=338fc3eedada97cc1178b9e7e2f9dcee, view=cab92d78689ec2ae36df4aed4eed7d3a(MainActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=338fc3eedada97cc1178b9e7e2f9dcee, view=cab92d78689ec2ae36df4aed4eed7d3a(MainActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=338fc3eedada97cc1178b9e7e2f9dcee, view=16417b5afd0cb399f9649cd3d4b7b1ac(MainActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=002525ce9c22275a9e434fa17eaeda0e, view=ee0486985041b70e3a9ad02a6af9b0e6(MainActivity/TextView-Clock isn')) (heuristic)
  - act: CustomTouchEvent(state=002525ce9c22275a9e434fa17eaeda0e, view=ee0486985041b70e3a9ad02a6af9b0e6(MainActivity/TextView-Clock isn')) (heuristic)
  - act: CustomTouchEvent(state=002525ce9c22275a9e434fa17eaeda0e, view=6eca7260af81443d8baa2b4d642c45e2(MainActivity/Button-Wait)) (heuristic)
  - act: CustomTouchEvent(state=338fc3eedada97cc1178b9e7e2f9dcee, view=16417b5afd0cb399f9649cd3d4b7b1ac(MainActivity/ImageView-)) (nav)

### G008 Delete an alarm

- Status: **covered**
- Reason: Covered by shared-flow reuse of C002.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Tap on the 'Alarm' tab in the Clock app.; Long-press the alarm you want to delete.; Select the 'Delete' option from the context menu.; Confirm the deletion of the alarm by tapping 'Delete' again.; The alarm is now removed from the list.
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=c0dd16bdbb40a4a840c3c4325a306166, x=255, y=1110) (visual_ground)
  - act: CustomTouchEvent(state=a36e59140ccf15c609dc7c3450a93505, x=258, y=1099) (visual_ground)
  - act: CustomTouchEvent(state=b388770d67f7a40737f5f1a0c6915a2d, x=255, y=1110) (visual_ground)

### G009 Set the alarm sound

- Status: **covered**
- Reason: Covered by shared-flow reuse of C002.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Navigate to the 'Alarm' section; Open the Clock app; Tap on the alarm you want to edit; Tap on the 'Sound' option; Select a tone or file from storage; Confirm the selection and save the changes
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=e00047082696536654bd502880f312f3, x=255, y=1110) (visual_ground)
  - act: CustomTouchEvent(state=12f6e28fd5bbb2421ce1cf84d769059b, x=261, y=1104) (visual_ground)
  - act: CustomTouchEvent(state=0eb131bb71ef7355a1fe4d1d4f268fac, x=255, y=1096) (visual_ground)

### G010 Snooze

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the 'Snooze' option from the notification.; Tap on the alarm notification when it rings.; Select the 'Snooze' option again if you wish to extend the snooze duration.; The alarm will sound again after the snooze duration.
- Remaining steps: Wait for the configured interval to elapse.
- Completion ratio: 0.80
- Credited from later features: G004, G007
- Actions taken: 14
  - act: CustomTouchEvent(state=fa0b3d5b6783ff141d94a6a26de0d49a, view=0ea26831962d44ba6b3546dac3e8b893(MainActivity/TextView-Alarm)) (heuristic)
  - act: CustomTouchEvent(state=8ee3b322ee6baaa6196088d56222fbec, view=0ea26831962d44ba6b3546dac3e8b893(MainActivity/TextView-Alarm)) (heuristic)
  - act: CustomTouchEvent(state=fd7f47ed4a24a73f1c78600611ae3fbd, view=0ea26831962d44ba6b3546dac3e8b893(MainActivity/TextView-Alarm)) (heuristic)
  - act: CustomTouchEvent(state=caac60772d37a2266ad0ad44345e0af7, view=43c238be0d6f0796162a7ebb114ab433(MainActivity/TextView-Sun, Sat)) (heuristic)
  - act: CustomTouchEvent(state=afa3afeca60ed711274096327c667d64, view=d4f2e2e7923ba38f0c040c37a41af3d2(MainActivity/Button-OK)) (heuristic)
  - act: CustomTouchEvent(state=e08263d086997e1fe6527a03ab39aa1c, view=d4f2e2e7923ba38f0c040c37a41af3d2(MainActivity/Button-OK)) (heuristic)
  - act: CustomTouchEvent(state=e3c8f1f03ada66fe0bbf739ca92b88e0, view=43c238be0d6f0796162a7ebb114ab433(MainActivity/TextView-Sun, Sat)) (heuristic)
  - act: CustomTouchEvent(state=afa3afeca60ed711274096327c667d64, view=76a984ef8ced554d4a52fd5242198968(MainActivity/TextView-Default (C)) (rule)

### G011 Configure the snooze duration

- Status: **covered**
- Reason: Covered by shared-flow reuse of C002.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Tap on the 'Settings' icon in the top right corner of the Clock app.; Scroll down to find the 'Alarms' section and tap on it.; Tap on the 'Snooze' option within the 'Alarms' section.; Select the 'Snooze Duration' option.; Enter the desired snooze duration in the input field.; Tap on the 'Done' or 'Save' button to confirm the snooze duration setting.
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=a1a21e8964c03799bb8b5b8680d9f2f9, x=960, y=1772) (llm)
  - act: CustomTouchEvent(state=35c00afe2c9bf614ab2cdcb0b67bf96a, x=737, y=1795) (llm)
  - act: CustomTouchEvent(state=c7d7ef2c50b4a2e0e43f50c416c32119, x=778, y=1843) (visual_ground)

### G012 Make the alarm volume

- Status: **covered**
- Reason: Covered by shared-flow reuse of C002.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open Settings; Select the alarm you want to adjust; Select 'Alarms' from the settings menu; Scroll to the 'Volume' setting; Select 'Increase volume gradually' option; Save the changes
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=1cf68ffb28d968f753228406c03507f3, x=255, y=1114) (visual_ground)
  - act: CustomTouchEvent(state=229c7c11bb3be3759867ef25f2802eb1, x=262, y=1101) (visual_ground)
  - act: CustomTouchEvent(state=836e26015b1e381206af98fbc2bcc9ce, x=256, y=1110) (visual_ground)

### G013 Use the stopwatch

- Status: **covered**
- Reason: Covered by shared-flow reuse of C002.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the Stopwatch tab; Tap Start; Tap Stop; Tap Reset
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=61db1d91852528c3460874d30f6d0295, x=420, y=1100) (visual_ground)
  - act: CustomTouchEvent(state=fb7f3c158297e2cd8694bb6f0906119a, x=370, y=1795) (llm)
  - act: CustomTouchEvent(state=69586f8a90f58499a74b8ae196719850, x=420, y=1095) (visual_ground)

### G014 Sort the recorded stopwatch

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: tap the sort/overflow control; Open the Stopwatch tab with laps recorded
- Completion ratio: 1.00
- Actions taken: 7
  - act: CustomTouchEvent(state=bb0bcbf91d955ddab9e4455827d0010f, x=480, y=1839) (visual_ground)
  - act: CustomTouchEvent(state=55c09428bf4237b78cf94c10dca5ea61, view=4ba0a41a3fb049580d8c7fe6d889dbf7(MainActivity/TextView-Stopwatch)) (llm)
  - act: CustomTouchEvent(state=d7bed2d95afaf8fcf24ed2a93207c2cf, x=419, y=1130) (visual_ground)
  - act: CustomTouchEvent(state=6b97f0ff53ef522486e44ce6ef67ff5b, x=480, y=1812) (visual_ground)
  - act: CustomTouchEvent(state=f6b0d7c856c212d9744737f8789af093, view=4ba0a41a3fb049580d8c7fe6d889dbf7(MainActivity/TextView-Stopwatch)) (llm)
  - act: CustomTouchEvent(state=3d0bbde8e4c65f7687ee31843d2b0941, x=480, y=1812) (visual_ground)
  - act: CustomTouchEvent(state=b652ce5e4d19572516558bf8e3107b25, view=4ba0a41a3fb049580d8c7fe6d889dbf7(MainActivity/TextView-Stopwatch)) (heuristic)

### F015 Set the timer duration

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: action_inferred
- Completed steps: New Timer timer_add; Timer duration sorting_dialog_radio_timer_duration; OK button1
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=f551b0c9564714c166b04f3a9979b5dc, x=690, y=1800) (visual_ground)
  - act: CustomTouchEvent(state=3af22e6178ff7b4052b375d23f5709cd, x=690, y=1813) (visual_ground)
  - act: CustomTouchEvent(state=ccd1e24ff5c4b562c6e23344cd1ffe2a, view=b6c76dbed698474001fba4398df36138(MainActivity/TextView-Timer)) (visual_ground)

### F016 Custom sort the recorded stopwatch

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: action_inferred
- Completed steps: OK button1; Sort by sort; Custom sorting_dialog_radio_custom
- Completion ratio: 1.00
- Credited from later features: G002, G014, F015
- Actions taken: 8
  - act: CustomTouchEvent(state=0afb8e1b9e895c673ce8dbe95f840736, x=975, y=83) (llm)
  - act: CustomTouchEvent(state=0d7761251b6b33f6de10dabbf7ef4201, view=ee64280861297de3bbde2eefd32736a7(MainActivity/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=c1470f0a2abc6837303cb9cfd4a64b6d, view=d9e4619b537ac6ab61d00317a85f748d(SettingsActivity/TextView-Look & fee)) (heuristic)
  - act: CustomTouchEvent(state=c1470f0a2abc6837303cb9cfd4a64b6d, view=d9e4619b537ac6ab61d00317a85f748d(SettingsActivity/TextView-Look & fee)) (heuristic)
  - act: CustomTouchEvent(state=c1470f0a2abc6837303cb9cfd4a64b6d, view=f64c9ab28ad9ce26363e600fd1ea0d38(SettingsActivity/TextView-Alarm tab)) (heuristic)
  - act: CustomTouchEvent(state=c1470f0a2abc6837303cb9cfd4a64b6d, view=f64c9ab28ad9ce26363e600fd1ea0d38(SettingsActivity/TextView-Alarm tab)) (heuristic)
  - act: CustomTouchEvent(state=c1470f0a2abc6837303cb9cfd4a64b6d, view=a79af8e887dc82e5a451619f29cce92b(SettingsActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=5f4a9e1b67ed2c8b129420f2ee48dca3, view=b5a1e7e663bf1689ac9cc12e0c83d348(MainActivity/ImageView-)) (rule)

## Shared flows detected

7 reuse(s); 27 action(s) skipped by not re-executing a known terminal flow.

- `G005` reused `C002` (from G003), skipped 2 action(s)
- `G006` reused `C002` (from G003), skipped 2 action(s)
- `G008` reused `C002` (from G003), skipped 4 action(s)
- `G009` reused `C002` (from G003), skipped 5 action(s)
- `G011` reused `C002` (from G003), skipped 6 action(s)
- `G012` reused `C002` (from G003), skipped 4 action(s)
- `G013` reused `C002` (from G003), skipped 4 action(s)

See `session.json` and `log.md` in this folder for the full trace.
