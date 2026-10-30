# Feature test report: Fossify Clock

- Started: 2026-10-12 18:51:24
- Finished: 2026-10-12 19:49:58
- Features: 14
- Covered: 4
- Partial: 9
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 73% (mean completion ratio; the headline number)
- Coverage: 29% (features with every guide step matched)
- Stop reason: budget_time
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
- Filled via VLM/Gemini: 9
- Unresolved: 0
- Online coverage: 29% (4/14) — live journal self-report (covered / extracted features).
- Offline coverage: 12% (3 covered / 26; 4 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 18% (mean completion ratio).

## Findings

### G001 View the current time

- Status: **covered**
- Reason: The current time and date are displayed, indicating that the feature is complete. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the app; the Clock tab shows the current time and date for the device time zone
- Completion ratio: 1.00
- Credited from later features: G003
- Actions taken: 1
  - act: CustomTouchEvent(state=56976e68e9e5be59af34a7f2fda405e7, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (llm)

### G002 Add a time zone

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Clock tab
- Remaining steps: tap the "+" floating action button
- Completion ratio: 0.50
- Credited from later features: G003
- Actions taken: 15
  - act: CustomTouchEvent(state=77c35e78318d0f5bad6a847c4c2696c6, view=aa080e7b0b8dc403ea29a8045ff1697d(ContributorsActivity/TextView-Contributo)) (llm)
  - act: CustomTouchEvent(state=86c920051d373ef84f86f55d34e64403, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=fc48b00c2f80b45b1d1aebf3d74a7735, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=231f7938dfb2b7283a75d98f2001764e, view=ecb42936b57b9c8feeb73116ec228641(MainActivity/TextView-Clock)) (visual_ground)
  - act: CustomTouchEvent(state=261020d7beea7c77818c5b3500ab89c9, view=c218252482c6405139d501cb8a08b181(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=ab1470b8003d63706cacc7c8ee3409e0, view=ecb42936b57b9c8feeb73116ec228641(MainActivity/TextView-Clock)) (visual_ground)
  - act: CustomTouchEvent(state=e839e72fb9a0dbe4af71085f2ccafda4, view=b5a1e7e663bf1689ac9cc12e0c83d348(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=0d7761251b6b33f6de10dabbf7ef4201, view=60c3c22253e848fcd237438bae735d2f(MainActivity/LinearLayout-)) (heuristic)

### G003 Remove

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Clock tab
- Remaining steps: tap the "+" button and untick a zone to remove it, or open Settings
- Completion ratio: 0.50
- Actions taken: 18
  - act: CustomTouchEvent(state=c57200715848a043d8efda4dcc460b4d, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=134e6ea67f4b8e69e223313dcfef5dc7, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (llm)
  - act: CustomTouchEvent(state=c3b7c06390e6f865a5ed3a3be12a951a, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (llm)
  - act: CustomTouchEvent(state=78349ff05c88bd1bbe81c5aecbfcddf5, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=bab75e5e210371e68bf29220b43e4ff6, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (llm)
  - act: CustomTouchEvent(state=d6fd94c3417a62de086d835a2b25a51d, view=c218252482c6405139d501cb8a08b181(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=f1bec2aea521a7fa57539775f1c0434d, view=a3cb79f6caf1077f593994a021034f30(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=63d93e4d82f5629fb047e802b32ccfe3, view=332908b0d475e1adef729c449414baed(MainActivity/Button-)) (rule)

### G004 Open the full-screen clock

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Clock tab; Tap the clock face; Select the full-screen option
- Remaining steps: Confirm the transition to the full-screen clock
- Completion ratio: 0.75
- Credited from later features: G010
- Actions taken: 25
  - act: CustomTouchEvent(state=2d8e10f3d4580c1c1324da0d023219de, view=bf58c74d9bea16c477b15152543d37dd(MainActivity/RadioButton-Timer dura)) (llm)
  - act: CustomTouchEvent(state=1b1da5afbc7ff065866e3ef5cc0bfdac, view=65bb7cf0711d37ad306f92585aeed317(MainActivity/RadioButton-Creation o)) (llm)
  - act: CustomTouchEvent(state=2d8e10f3d4580c1c1324da0d023219de, view=d4f2e2e7923ba38f0c040c37a41af3d2(MainActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=570165d7e3ad2868509fbb10054ed782, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=3adee8fa8d5d50b3b610590fe2d7aca3, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=25186c223da4eb3efad6443056fc6c65, view=ecb42936b57b9c8feeb73116ec228641(MainActivity/TextView-Clock)) (visual_ground)
  - act: CustomTouchEvent(state=b9cfebd59c73de276204fed5d9a21936, view=9c98f47a0506a0ff2552b84018cca005(MainActivity/TextView-Clock)) (visual_ground)
  - act: CustomTouchEvent(state=a1316e0df74b252ead0e5d95e462da61, view=7a87e8c5bf0f71881b97a66675ae9853(MainActivity/FloatingActionButton-)) (rule)

### G005 Create an alarm

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the Alarm tab; tap the "+" button
- Completion ratio: 1.00
- Credited from later features: G003
- Actions taken: 10
  - act: CustomTouchEvent(state=dd25c29d030345d3fbb62515f4725fac, view=e2275266a34e514f63dae65dcd82b626(MainActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=dd828cc153a8c73b877fe2306f832cae, view=9cc37bdb808aafbf1cee9878865b9467(MainActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=dd25c29d030345d3fbb62515f4725fac, view=d4f2e2e7923ba38f0c040c37a41af3d2(MainActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=4913a8e1a7b64742e4a8681ac53bc6af, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=085e4ffd2acb92e6e233bd87138a26e1, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=623e3c21f8aa14bab225b0bc3ada9da8, view=2436abd86d9b8c3262b1b5d9334b253e(MainActivity/TextView-Alarm)) (visual_ground)
  - act: CustomTouchEvent(state=b86aa0b1fc8cda1b99566c65e3008a1a, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=534cfbc46910292c7f65167330f9a87d, view=35af8c0e9d6cd4f41b3fdea7b3c33ca2(MainActivity/ViewGroup-)) (rule)

### G006 Enable

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the Alarm tab; tap the toggle switch beside the alarm row
- Completion ratio: 1.00
- Actions taken: 2
  - act: CustomTouchEvent(state=8f906d0b66140607af29bf6dcff3aa33, view=cab92d78689ec2ae36df4aed4eed7d3a(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=8f906d0b66140607af29bf6dcff3aa33, view=cab92d78689ec2ae36df4aed4eed7d3a(MainActivity/ImageView-)) (heuristic)

### G007 Edit an alarm

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Alarm tab; Tap the alarm row; Tap the edit icon; Select the alarm to edit; Enter the new alarm time
- Remaining steps: Tap the save icon
- Completion ratio: 0.83
- Actions taken: 23
  - act: CustomTouchEvent(state=dd828cc153a8c73b877fe2306f832cae, view=d4f2e2e7923ba38f0c040c37a41af3d2(MainActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=3d54340744f82bb43a923bb67d48dbbb, view=fd36fb42f3039a362b237f1988383aed(MainActivity/RecyclerView-)) (visual_ground)
  - act: CustomTouchEvent(state=7434a4e78d201f339a3e3f13f3ab0d75, view=fd36fb42f3039a362b237f1988383aed(MainActivity/RecyclerView-)) (visual_ground)
  - act: CustomTouchEvent(state=5d211c82a596929ed3cefc9db80d5761, view=fd36fb42f3039a362b237f1988383aed(MainActivity/RecyclerView-)) (visual_ground)
  - act: CustomTouchEvent(state=cff77552139da9a456c5ead286199461, view=c218252482c6405139d501cb8a08b181(MainActivity/ImageView-)) (visual_ground)
  - act: CustomTouchEvent(state=f374a44e1832cd2b312eaea091961a6f, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=e29e3ca6d4733fed564daff40393e921, view=a3cb79f6caf1077f593994a021034f30(MainActivity/ImageView-)) (visual_ground)
  - act: CustomTouchEvent(state=f86caee877af0a4f1ddea2a7039cc615, view=2436abd86d9b8c3262b1b5d9334b253e(MainActivity/TextView-Alarm)) (rule)

### G008 Delete an alarm

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Alarm' tab; Long-press the alarm you want to delete; Confirm the deletion of the alarm by tapping 'Delete'
- Remaining steps: Select 'Delete' from the options that appear
- Completion ratio: 0.75
- Credited from later features: G007
- Actions taken: 19
  - act: CustomTouchEvent(state=6a5d45d0c9ec7d49b07eaf10caf0b76b, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=a9e6defff1b6344a55b34c3a98895471, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=8c7cfd1179042475cec87ee01cf1c99f, view=b5a1e7e663bf1689ac9cc12e0c83d348(MainActivity/ImageView-)) (visual_ground)
  - act: CustomTouchEvent(state=0d7761251b6b33f6de10dabbf7ef4201, x=526, y=146) (llm)
  - act: CustomTouchEvent(state=dcfd000a296020071aea80e5399900a5, view=b5a1e7e663bf1689ac9cc12e0c83d348(MainActivity/ImageView-)) (visual_ground)
  - act: CustomTouchEvent(state=0d7761251b6b33f6de10dabbf7ef4201, view=60c3c22253e848fcd237438bae735d2f(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=47233bb584088c26045999f4062e48c6, view=f7ad3cefb7208755007935fb370e6f9d(AboutActivity/TextView-About)) (heuristic)
  - act: CustomTouchEvent(state=47233bb584088c26045999f4062e48c6, view=f7ad3cefb7208755007935fb370e6f9d(AboutActivity/TextView-About)) (heuristic)

### G009 Set the alarm sound

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Clock app; Navigate to the alarm settings; Tap on the alarm you want to edit; Select the alarm sound entry and choose a tone
- Remaining steps: Save the changes
- Completion ratio: 0.80
- Credited from later features: G003, G007
- Actions taken: 17
  - act: CustomTouchEvent(state=c4fef421ea40e6bd45bee9b407ff18cd, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=1e0f69b37dfe97d445f1be4207a7a2ad, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=a6a847c71d24129618fc8fd475ded37c, view=95ca51b068ab8f1cb7da19a6bafe2b94(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=5fb7030f5cfd5e0fa1ff63bad4cfd8f1, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=f6b052169f8369a316b1ecdd58ad926a, view=0ea26831962d44ba6b3546dac3e8b893(MainActivity/TextView-Alarm)) (llm)
  - act: CustomTouchEvent(state=f305a70c4a99028c53db6a57a0785e0b, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=adba01746a78ed2957387c1245c17f9b, view=0ea26831962d44ba6b3546dac3e8b893(MainActivity/TextView-Alarm)) (nav)
  - act: CustomTouchEvent(state=d06c610158fe6f72d9ec25eec1b20ebf, view=8a2ca2319c05640eeb8393d34d6bef60(MainActivity/ViewGroup-)) (rule)

### G010 Snooze

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the alarm notification to open the Clock app; Select the 'Snooze' option to postpone the alarm by the configured interval; Confirm the snooze duration by selecting the desired time; The alarm will now ring again after the configured snooze duration; To stop the alarm, select the 'Dismiss' option
- Completion ratio: 1.00
- Actions taken: 10
  - act: CustomTouchEvent(state=d3f33efdb8ec420d25379ced1e814e33, view=2436abd86d9b8c3262b1b5d9334b253e(MainActivity/TextView-Alarm)) (llm)
  - act: CustomTouchEvent(state=d9f7cd78fee3c1b302e0ac0fb8011a17, view=b6c76dbed698474001fba4398df36138(MainActivity/TextView-Timer)) (llm)
  - act: CustomTouchEvent(state=33644aab446d4b435b39c7931a54b150, view=2436abd86d9b8c3262b1b5d9334b253e(MainActivity/TextView-Alarm)) (heuristic)
  - act: CustomTouchEvent(state=b5e4833c12b48508015b5c3604fe5172, view=dfea5ce9b4721aa554bf8f2c27fdf2b1(MainActivity/TextView-9:00 am)) (heuristic)
  - act: CustomTouchEvent(state=afa3afeca60ed711274096327c667d64, view=a20062ae7adb810f1fc3b39952341a70(MainActivity/TextView-9:00 am)) (heuristic)
  - act: CustomTouchEvent(state=bce772a9e7c9e941e15e56141af2663c, view=34d697f8b50243c13440f36f50de6a40(MainActivity/Button-OK)) (heuristic)
  - act: CustomTouchEvent(state=afa3afeca60ed711274096327c667d64, view=cab92d78689ec2ae36df4aed4eed7d3a(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=afa3afeca60ed711274096327c667d64, view=cab92d78689ec2ae36df4aed4eed7d3a(MainActivity/ImageView-)) (heuristic)

### G011 Configure the snooze duration

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the specific alarm you want to configure.; Tap on the 'Settings' icon in the app's main menu.; Tap on the 'Snooze' option within the alarm settings.
- Remaining steps: Scroll down to find the 'Alarms' section and tap on it.; Select the desired snooze duration from the available options.
- Completion ratio: 0.60
- Credited from later features: G007, G008
- Actions taken: 18
  - act: CustomSetTextEvent(state=dbc0fdb0926fc0afaa82f8012fb15593, view=8668101ed5d8385b121600e409604750(MainActivity/EditText-TestCube A), text=TestCube Alarm Label) (nav)
  - act: CustomTouchEvent(state=dbc0fdb0926fc0afaa82f8012fb15593, view=562070ed6fc38f95cfeef98837a8c7f8(MainActivity/TextView-7:00 am)) (rule)
  - act: CustomTouchEvent(state=3442e9b15ab685ea9d77829be171349f, view=34d697f8b50243c13440f36f50de6a40(MainActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=dbc0fdb0926fc0afaa82f8012fb15593, view=316c3e0f703d350db2840e8961584272(MainActivity/TextView-S)) (rule)
  - act: CustomTouchEvent(state=dbc0fdb0926fc0afaa82f8012fb15593, view=316c3e0f703d350db2840e8961584272(MainActivity/TextView-S)) (llm)
  - act: CustomTouchEvent(state=dbc0fdb0926fc0afaa82f8012fb15593, view=4b670f65c586cddfb5e0abc526937514(MainActivity/TextView-M)) (llm)
  - act: CustomTouchEvent(state=dbc0fdb0926fc0afaa82f8012fb15593, view=4b670f65c586cddfb5e0abc526937514(MainActivity/TextView-M)) (rule)
  - act: CustomTouchEvent(state=dbc0fdb0926fc0afaa82f8012fb15593, view=d4f2e2e7923ba38f0c040c37a41af3d2(MainActivity/Button-OK)) (rule)

### G012 Make the alarm volume

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open Settings; Select 'Edit Alarm'; Scroll to 'Alarm Volume' settings
- Remaining steps: Scroll to 'Alarms' section; Select 'Increase volume gradually' option
- Completion ratio: 0.60
- Credited from later features: G003, G007, G008
- Actions taken: 17
  - act: CustomTouchEvent(state=f93262f92a13929ccd1f585add74f557, view=0ea26831962d44ba6b3546dac3e8b893(MainActivity/TextView-Alarm)) (llm)
  - act: CustomTouchEvent(state=b8ca6e785d6c64319610cb729b4e5b5c, view=0ea26831962d44ba6b3546dac3e8b893(MainActivity/TextView-Alarm)) (llm)
  - act: CustomTouchEvent(state=a24a6759bf132f54872db41bfb826356, view=0ea26831962d44ba6b3546dac3e8b893(MainActivity/TextView-Alarm)) (llm)
  - act: CustomTouchEvent(state=edfeea3864dbfcbeba6e62ef648939e1, view=95ca51b068ab8f1cb7da19a6bafe2b94(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=a51a2c3623d240c9c4c48b3dd7b5f613, view=0ea26831962d44ba6b3546dac3e8b893(MainActivity/TextView-Alarm)) (nav)
  - act: CustomTouchEvent(state=0c4f4b44eff5b3e15760dfb804f0554c, view=0ea26831962d44ba6b3546dac3e8b893(MainActivity/TextView-Alarm)) (nav)
  - act: CustomTouchEvent(state=3a058aa240aeda5103aa6015e067d2d3, view=0ea26831962d44ba6b3546dac3e8b893(MainActivity/TextView-Alarm)) (nav)
  - act: CustomTouchEvent(state=70a3aba1a967820b40b461a09710a040, view=43d47f313fa0b9116c5085cb3b2037b1(MainActivity/TextView-test)) (nav)

### G013 Use the stopwatch

- Status: **partial**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the Stopwatch tab; Tap Start; Tap Stop
- Remaining steps: Tap Reset
- Completion ratio: 0.75
- Credited from later features: G010
- Actions taken: 17
  - act: CustomTouchEvent(state=d55fe904918c4c60f1177123978d4f96, view=305f90429aa259791b92f7b9f86f624f(MainActivity/TextView-Stopwatch)) (nav)
  - act: CustomTouchEvent(state=02a40c1ac8b45559a194972797f1168a, view=305f90429aa259791b92f7b9f86f624f(MainActivity/TextView-Stopwatch)) (nav)
  - act: CustomTouchEvent(state=1168b1bb4f232ba340fdf1c5e1d4bd13, view=168d0e4555feed92e2809fd64baf90b3(MainActivity/TextView-0.0)) (rule)
  - act: CustomTouchEvent(state=52649e9a9ea628a724782a972361aa5b, view=d4f2e2e7923ba38f0c040c37a41af3d2(MainActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=dde431a5acf0f41cbc947b415fdc14fc, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=78e6600c257cf451ba5411d0ed878bd8, view=ea0f6ea56bdffbd3fe94ef776feaddc8(MainActivity/j-)) (visual_ground)
  - act: CustomTouchEvent(state=c51a5358add340e06a1ca56c448d165c, view=4ba0a41a3fb049580d8c7fe6d889dbf7(MainActivity/TextView-Stopwatch)) (visual_ground)
  - act: CustomTouchEvent(state=83988b1b0df34321e6fee585f4df0830, view=305f90429aa259791b92f7b9f86f624f(MainActivity/TextView-Stopwatch)) (visual_ground)

### G014 Sort the recorded stopwatch

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Tap on the Stopwatch tab with laps recorded
- Remaining steps: Tap the sort/overflow control; Select the 'Sort' option from the menu; Choose 'Sort by Lap Time' from the sort options; Confirm the sorting of the recorded stopwatch laps
- Completion ratio: 0.20
- Actions taken: 13
  - act: CustomTouchEvent(state=2744fb5472db7e9bb0c552b2f1f6be5e, view=305f90429aa259791b92f7b9f86f624f(MainActivity/TextView-Stopwatch)) (heuristic)
  - act: CustomTouchEvent(state=bbca243331062aed3a4788b929ab78f0, view=b5a1e7e663bf1689ac9cc12e0c83d348(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=0d7761251b6b33f6de10dabbf7ef4201, view=ee64280861297de3bbde2eefd32736a7(MainActivity/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=96da222815edc1d45e300daf6a214ce4, view=636327018998f4b42fbf8adbcb1f9e77(SettingsActivity/Switch-Always use)) (heuristic)
  - act: CustomTouchEvent(state=9f7ca7819680fa27d5fe5c17ad0d139e, view=b5a1e7e663bf1689ac9cc12e0c83d348(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=0d7761251b6b33f6de10dabbf7ef4201, view=0358e0bf5cf25adc267cbce3aaf591e1(MainActivity/TextView-About)) (heuristic)
  - act: ScrollEvent(state=47233bb584088c26045999f4062e48c6, view=efe99da9bdeedc29e21f8083cedf0c3a(AboutActivity/ScrollView-), direction=up) (heuristic)
  - act: CustomTouchEvent(state=77c35e78318d0f5bad6a847c4c2696c6, view=f9ff74eeb7d57d78e329bb357112a456(ContributorsActivity/View-)) (heuristic)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
