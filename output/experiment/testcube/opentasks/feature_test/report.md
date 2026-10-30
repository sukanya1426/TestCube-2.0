# Feature test report: OpenTasks

- Started: 2026-10-26 01:39:24
- Finished: 2026-10-26 02:38:22
- Features: 14
- Covered: 4
- Partial: 4
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 69% (mean completion ratio; the headline number)
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
- README-extracted features: 3
- In both: 0
- Guide-only: 14
- README-only: 3
  - guide-only: G001 Create a task
  - guide-only: G002 Set a due date
  - guide-only: G003 Set the task priority
  - guide-only: G004 Set the task status
  - guide-only: G005 Add a location
  - guide-only: G006 Add a checklist
  - guide-only: G007 Create a recurring task
  - guide-only: G008 Edit an existing task
  - guide-only: G009 Browse tasks grouped
  - guide-only: G010 Browse tasks grouped
  - guide-only: G011 Browse tasks grouped
  - guide-only: G012 Show
  - README-only: F001 Complete first-run setup
  - README-only: F002 Search
  - README-only: F003 Change app settings

## Text-field resolution

- Filled via credential.txt: 5
- Filled via VLM/Gemini: 8
- Unresolved: 0
- Online coverage: 29% (4/14) — live journal self-report (covered / extracted features).
- Offline coverage: not computed (no ground-truth JSON).

## Findings

### G001 Create a task

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the app; Tap the 'Create' button; Tap the '+' floating action button; Enter the task title; Enter the task description
- Completion ratio: 1.00
- Credited from later features: G003, G007
- Actions taken: 13
  - act: CustomTouchEvent(state=3fbad5be3b8845f70450c0ed3e384adc, view=b8c62ffc97ad19b67a4baf546eb1e362(EditTaskActivity/TextView-Create)) (nav)
  - act: CustomTouchEvent(state=3fbad5be3b8845f70450c0ed3e384adc, view=4023960839e67ca18dc36091a2c1fdfa(EditTaskActivity/TextView-Add item)) (afford_search)
  - act: CustomTouchEvent(state=5abd90fcb33e4ecc83a05f133e1b7253, view=b8c62ffc97ad19b67a4baf546eb1e362(EditTaskActivity/TextView-Create)) (nav)
  - act: CustomTouchEvent(state=5abd90fcb33e4ecc83a05f133e1b7253, view=cea5154ac7526c54f710df81101cccae(EditTaskActivity/Spinner-)) (rule)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=fb8aaa5d056017170a30c6fbf8f99119(TaskListActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=c98bd5a4ac537b8af631508e8b7427e3, view=f36b90ffe131be6fd18f4e08e5573ddf(EditTaskActivity/TextView-My tasks)) (heuristic)
  - act: CustomSetTextEvent(state=3fbad5be3b8845f70450c0ed3e384adc, view=ff72569ddd3bd58620eb67ebd4b7b8da(EditTaskActivity/EditText-Title), text=Create a task entry) (mandatory_fill)
  - act: CustomSetTextEvent(state=d5f869b67a0895d8c9c3846c9d1f2116, view=bff6d69cd42c5290eb35ecd39f86d31c(EditTaskActivity/EditText-Create a t), text=Complete the project by next week.) (mandatory_fill)

### G002 Set a due date

- Status: **covered**
- Reason: Hit the per-feature step limit. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap on the task you want to set a due date for; Tap on the 'Due' field; Select the date from the date picker; Select the time from the time picker; Tap on the 'Save' button to confirm the due date
- Completion ratio: 1.00
- Credited from later features: G007, G005
- Actions taken: 17
  - act: CustomTouchEvent(state=cead913e664a6c7388403e0cd07d1aba, view=fb8aaa5d056017170a30c6fbf8f99119(TaskListActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=53bf0a82e01ec4f7b2df5d98d587c246, view=9cad0af31adadac925cf81d98bf1cae6(EditTaskActivity/TextView-Local)) (llm)
  - act: CustomTouchEvent(state=3cc15677daefabfd5ecb882927783377, view=d479e4e8c2b34e4708ea59e43daf15b0(EditTaskActivity/TextView-Local)) (llm)
  - act: CustomTouchEvent(state=3fbad5be3b8845f70450c0ed3e384adc, view=672ed14d2344e018700bfe80f9581654(EditTaskActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6c0a390490145aadb89a2cd0828a7771, view=04163724d4ad3abd23afd1d68ce702c1(EditTaskActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=447921dd9f774d07532a10f912663bd0, view=292a9aadd6062c149649d43c75ecf4b0(EditTaskActivity/TextView-Set time)) (heuristic)
  - act: CustomTouchEvent(state=447921dd9f774d07532a10f912663bd0, view=0021cae21fa870bc5bccefefb6ef2d6a(EditTaskActivity/TextView-Type in ti)) (nav)
  - act: CustomTouchEvent(state=447921dd9f774d07532a10f912663bd0, view=0021cae21fa870bc5bccefefb6ef2d6a(EditTaskActivity/TextView-Type in ti)) (nav)

### G003 Set the task priority

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the task editor
- Remaining steps: Tap the priority selector; Select the desired priority level
- Completion ratio: 0.33
- Actions taken: 17
  - act: CustomTouchEvent(state=3fbad5be3b8845f70450c0ed3e384adc, view=cea5154ac7526c54f710df81101cccae(EditTaskActivity/Spinner-)) (rule)
  - act: CustomSetTextEvent(state=447921dd9f774d07532a10f912663bd0, view=3dbb6e348956e1873441201b24b9b966(EditTaskActivity/EditText-3), text=test) (llm)
  - act: CustomSetTextEvent(state=447921dd9f774d07532a10f912663bd0, view=3dbb6e348956e1873441201b24b9b966(EditTaskActivity/EditText-3), text=test) (llm)
  - act: CustomTouchEvent(state=447921dd9f774d07532a10f912663bd0, view=993ab8c26cf153ac58a3f87eb8412fbc(EditTaskActivity/TextView-minute)) (llm)
  - act: CustomTouchEvent(state=447921dd9f774d07532a10f912663bd0, view=ba1c423d7995af6fa59206e9d2f3b290(EditTaskActivity/CheckedTextView-AM)) (afford_search)
  - act: CustomTouchEvent(state=b15f2446937fc73d610c18e5412c3c49, view=41d690c36e5304c5e1b4926774a4099e(EditTaskActivity/CheckedTextView-AM)) (heuristic)
  - act: CustomTouchEvent(state=447921dd9f774d07532a10f912663bd0, view=993ab8c26cf153ac58a3f87eb8412fbc(EditTaskActivity/TextView-minute)) (llm)
  - act: ScrollEvent(state=447921dd9f774d07532a10f912663bd0, view=594c57580b77adc4be7db5e12cf9a076(EditTaskActivity/Spinner-), direction=up) (afford_search)

### G004 Set the task status

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the task editor; Tap the status field; Select the desired status from the dropdown
- Remaining steps: Confirm the status change
- Completion ratio: 0.75
- Credited from later features: G003, G007, G002
- Actions taken: 9
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=62b6976b3faeed2bbf1d8d959fd09046(TaskListActivity/TextView-My tasks)) (nav)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=eecbf65a8d849b474c73bc022b006880(TaskListActivity/TextView-Local)) (nav)
  - act: CustomTouchEvent(state=cead913e664a6c7388403e0cd07d1aba, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=b9bd3499ada8fcda67d53da65da2aad2, view=7452df90f418ba6334f9ebab9bb5de0c(TaskListActivity/CheckBox-)) (heuristic)
  - act: CustomTouchEvent(state=cead913e664a6c7388403e0cd07d1aba, view=633924ed01f5e3a334f108accc99fa7f(TaskListActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=b9bd3499ada8fcda67d53da65da2aad2, view=119f617b3a18633f172562f0b35a53e7(TaskListActivity/TextView-Refresh)) (llm)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (afford_search)

### G005 Add a location

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the task editor; Tap the location field; Enter the desired location; Tap the save button
- Completion ratio: 1.00
- Credited from later features: G003, G007
- Actions taken: 12
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=b9bd3499ada8fcda67d53da65da2aad2, view=07203c6cf6f90ffee6acdd14aeb5ba96(TaskListActivity/TextView-Show compl)) (nav)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (llm)
  - act: CustomSetTextEvent(state=cead913e664a6c7388403e0cd07d1aba, view=eeed3a6f9e72df5f160cbf875183e4bd(TaskListActivity/AutoCompleteTextView-   Search), text=test) (mandatory_fill)
  - act: CustomTouchEvent(state=2e462b5b35dbf920f79423a40d97832c, view=6d8b7d30f2b1ebaf845f7c08e875abb6(TaskListActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=d61e439ec88202614e19374a93cffc38, view=b010a42480d0d3d87a2e8e3e8edc8f83(TaskListActivity/ExpandableListView-)) (llm)
  - act: CustomTouchEvent(state=d61e439ec88202614e19374a93cffc38, view=fb8aaa5d056017170a30c6fbf8f99119(TaskListActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=3fbad5be3b8845f70450c0ed3e384adc, view=3a1ba8c3ba5e963b93ca55311ad3aa1b(EditTaskActivity/TextView-SAVE)) (heuristic)

### G006 Add a checklist

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the add item button; Open the task editor; Tap the checklist section; Enter the checklist item; Enter the second checklist item
- Completion ratio: 1.00
- Credited from later features: G001, G003
- Actions taken: 14
  - act: ScrollEvent(state=cead913e664a6c7388403e0cd07d1aba, view=02404317ae5caf0a8349e579471b71a9(TaskListActivity/ViewPager-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=cead913e664a6c7388403e0cd07d1aba, view=c7b43e8c725f12bc03c927e9cabefbab(TaskListActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=cead913e664a6c7388403e0cd07d1aba, view=c7b43e8c725f12bc03c927e9cabefbab(TaskListActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=cead913e664a6c7388403e0cd07d1aba, view=fb8aaa5d056017170a30c6fbf8f99119(TaskListActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=d742d631e1807240f8297654cd09e770, view=4023960839e67ca18dc36091a2c1fdfa(EditTaskActivity/TextView-Add item)) (nav)
  - act: CustomTouchEvent(state=5abd90fcb33e4ecc83a05f133e1b7253, view=c4cee20ec9aa5441d1c0196721077049(EditTaskActivity/TextView-Checklist)) (heuristic)
  - act: CustomSetTextEvent(state=14f42180b01bdd5823fc988e1f8cb9f4, view=ff72569ddd3bd58620eb67ebd4b7b8da(EditTaskActivity/EditText-Title), text=test) (mandatory_fill)
  - act: CustomSetTextEvent(state=fbf3badc8fd43bfa164df5e87eec01f4, view=b3c8514deee5df9e4d5360ce70c1a80e(EditTaskActivity/EditText-test), text=test) (mandatory_fill)

### G007 Create a recurring task

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open the task editor; Tap the recurrence field; Select the recurrence type; Enter the recurrence interval; Save the task
- Remaining steps: Select the recurrence frequency
- Completion ratio: 0.83
- Credited from later features: G002
- Actions taken: 25
  - act: CustomTouchEvent(state=cead913e664a6c7388403e0cd07d1aba, view=8e1924bab4772f00bae4cc4ebafc58d3(TaskListActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=4a605044334d07df09baa4559220abc7, view=f07df933405e979adc3a686376fbfc19(TaskListActivity/TextView-0 tasks)) (nav)
  - act: CustomTouchEvent(state=4a605044334d07df09baa4559220abc7, view=f07df933405e979adc3a686376fbfc19(TaskListActivity/TextView-0 tasks)) (nav)
  - act: CustomTouchEvent(state=4a605044334d07df09baa4559220abc7, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=b9bd3499ada8fcda67d53da65da2aad2, view=95c05bb76616bd28846d1c9fba2ba26d(TaskListActivity/TextView-Displayed )) (rule)
  - act: CustomTouchEvent(state=85a7b9d1bd51b13ca0c8714ec88445a2, view=a5ec41ff613a0fa83b030f128f14e008(SyncSettingsActivity/TextView-My tasks)) (nav)
  - act: CustomTouchEvent(state=424db67dfa4adb97b994d5a4c0c8a3c1, view=a5ec41ff613a0fa83b030f128f14e008(SyncSettingsActivity/TextView-My tasks)) (nav)
  - act: CustomTouchEvent(state=85a7b9d1bd51b13ca0c8714ec88445a2, view=efefa9d1c8c95f1b6d75cd34ffb182ad(SyncSettingsActivity/Button-SYNCHRONIZ)) (rule)

### G008 Edit an existing task

- Status: **partial**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Tap the task in the list to open the detail view
- Remaining steps: Tap the edit (pencil) icon; Enter the new title for the task; Enter the new description for the task; Tap the save icon to update the task
- Completion ratio: 0.20
- Credited from later features: G003
- Actions taken: 11
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=b9bd3499ada8fcda67d53da65da2aad2, view=07203c6cf6f90ffee6acdd14aeb5ba96(TaskListActivity/TextView-Show compl)) (nav)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=68c3488f3043b2ab82a4d54a0f0bdad3, view=07203c6cf6f90ffee6acdd14aeb5ba96(TaskListActivity/TextView-Show compl)) (nav)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=4d37dc853f7a65fb57609b24ddd0e72a(TaskListActivity/TextView-Next days)) (rule)
  - act: CustomTouchEvent(state=4a605044334d07df09baa4559220abc7, view=263245fb174ed0807ea645b0f75d063b(TaskListActivity/TextView-Task progr)) (nav)
  - act: CustomTouchEvent(state=4a605044334d07df09baa4559220abc7, view=263245fb174ed0807ea645b0f75d063b(TaskListActivity/TextView-Task progr)) (nav)
  - act: CustomTouchEvent(state=4a605044334d07df09baa4559220abc7, view=e4e76dd38bdb17b889cf86d417fa7a26(TaskListActivity/TextView-Done)) (llm)

### G009 Browse tasks grouped

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the app; Select the 'Browse' option; Select the 'Tasks' option; Select the 'Grouped' option
- Remaining steps: Select the 'Due' tab
- Completion ratio: 0.80
- Credited from later features: G003, G012
- Actions taken: 8
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=633924ed01f5e3a334f108accc99fa7f(TaskListActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=6ab3e6aead58bb7b6cda879092ec7d34(TaskListActivity/TextView-Tasks due)) (nav)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=6ab3e6aead58bb7b6cda879092ec7d34(TaskListActivity/TextView-Tasks due)) (nav)
  - act: ScrollEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=491dad72e299315c0666429e84832797(TaskListActivity/ViewPager-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=4d37dc853f7a65fb57609b24ddd0e72a(TaskListActivity/TextView-Next days)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=633924ed01f5e3a334f108accc99fa7f(TaskListActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=08c7b54a5880668987e85a75202a107e(TaskListActivity/RelativeLayout-)) (rule)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=3f02d4bed9ccdb09f6b1d04ec4a4e63e(TaskListActivity/TextView-Tasks)) (rule)

### G010 Browse tasks grouped

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the app; Select the 'Browse' option; Select the 'Tasks' option
- Remaining steps: Select the 'Lists' tab; Select the 'Grouped' view
- Completion ratio: 0.60
- Credited from later features: G003, G012
- Actions taken: 7
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=8e1924bab4772f00bae4cc4ebafc58d3(TaskListActivity/ImageView-)) (llm)
  - act: CustomSetTextEvent(state=cead913e664a6c7388403e0cd07d1aba, view=eeed3a6f9e72df5f160cbf875183e4bd(TaskListActivity/AutoCompleteTextView-   Search), text=test) (llm)
  - act: CustomTouchEvent(state=2e462b5b35dbf920f79423a40d97832c, view=a7d100655593c70d5ad4b26f9a71cb0e(TaskListActivity/TextView-test)) (llm)
  - act: CustomTouchEvent(state=5d0fff9d5d7d94180b51569029760ca8, view=4d728c3a8a61672f74ae75e6180dabe9(TaskListActivity/TextView-0 tasks)) (nav)
  - act: CustomSetTextEvent(state=2e462b5b35dbf920f79423a40d97832c, view=f0eb811075ecfd89ca55e8914b864a96(TaskListActivity/AutoCompleteTextView-test), text=test) (llm)
  - act: CustomTouchEvent(state=2e462b5b35dbf920f79423a40d97832c, view=6d8b7d30f2b1ebaf845f7c08e875abb6(TaskListActivity/ImageView-)) (afford_search)
  - act: CustomSetTextEvent(state=d61e439ec88202614e19374a93cffc38, view=f0eb811075ecfd89ca55e8914b864a96(TaskListActivity/AutoCompleteTextView-test), text=test) (llm)

### G011 Browse tasks grouped

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the app; Select the 'Browse' option; Select the 'Tasks' option; Select the 'Grouped' option
- Remaining steps: Select the 'Progress' tab
- Completion ratio: 0.80
- Credited from later features: G003, G012
- Actions taken: 8
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=08c7b54a5880668987e85a75202a107e(TaskListActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=3f02d4bed9ccdb09f6b1d04ec4a4e63e(TaskListActivity/TextView-Tasks)) (nav)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=62b6976b3faeed2bbf1d8d959fd09046(TaskListActivity/TextView-My tasks)) (llm)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=1e6c12ceefc24680555839d18f4315fa(TaskListActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=3f02d4bed9ccdb09f6b1d04ec4a4e63e(TaskListActivity/TextView-Tasks)) (llm)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=1e6c12ceefc24680555839d18f4315fa(TaskListActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=6d8b7d30f2b1ebaf845f7c08e875abb6(TaskListActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=269c6a34f11e3a288aac56f6fabd01b7, view=58af100f594aab1ea7f59a561b464ff3(TaskListActivity/TextView-My tasks)) (rule)

### G012 Show

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Tap the overflow menu (three dots) in the task list; Select the 'Show completed tasks' option
- Remaining steps: Tap the 'Show' option in the overflow menu
- Completion ratio: 0.67
- Actions taken: 5
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=6d8b7d30f2b1ebaf845f7c08e875abb6(TaskListActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=269c6a34f11e3a288aac56f6fabd01b7, view=1ac7f477236a29379d0ba6509c2acd1d(TaskListActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=3fbad5be3b8845f70450c0ed3e384adc, view=dd79489014f43689e4bdce27209d8f34(EditTaskActivity/TextView-My tasks)) (heuristic)
  - act: CustomTouchEvent(state=3cc15677daefabfd5ecb882927783377, view=c468e2c0f75323c1d3e219d5355761ca(EditTaskActivity/TextView-My tasks)) (rule)
  - act: CustomTouchEvent(state=3fbad5be3b8845f70450c0ed3e384adc, view=dd79489014f43689e4bdce27209d8f34(EditTaskActivity/TextView-My tasks)) (llm)

### G013 Create a local task

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Tap on the overflow menu
- Remaining steps: Select 'Create' from the overflow menu; Select 'Local' from the navigation hints; Enter a title for the task; Enter a description for the task; Tap on the 'Create' button to save the task
- Completion ratio: 0.17
- Credited from later features: G012
- Actions taken: 3
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=eecbf65a8d849b474c73bc022b006880(TaskListActivity/TextView-Local)) (nav)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=eecbf65a8d849b474c73bc022b006880(TaskListActivity/TextView-Local)) (llm)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=eecbf65a8d849b474c73bc022b006880(TaskListActivity/TextView-Local)) (nav)

### G014 Share a task

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the task detail view
- Remaining steps: tap the share icon
- Completion ratio: 0.50
- Actions taken: 8
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=6d8b7d30f2b1ebaf845f7c08e875abb6(TaskListActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=269c6a34f11e3a288aac56f6fabd01b7, view=7b8b1045e948214f0f1d4fea3f27b2c6(TaskListActivity/Spinner-)) (nav)
  - act: CustomTouchEvent(state=5a31730de00024ff3c00560136a520d4, view=62dc5b1d4ddae3468d0832a51baa12c1(TaskListActivity/TextView-Local)) (nav)
  - act: CustomTouchEvent(state=269c6a34f11e3a288aac56f6fabd01b7, view=ba7a5dd51e4717e36e6e698d03574557(TaskListActivity/EditText-Title)) (llm)
  - act: CustomTouchEvent(state=269c6a34f11e3a288aac56f6fabd01b7, view=ba7a5dd51e4717e36e6e698d03574557(TaskListActivity/EditText-Title)) (llm)
  - act: CustomTouchEvent(state=269c6a34f11e3a288aac56f6fabd01b7, view=58af100f594aab1ea7f59a561b464ff3(TaskListActivity/TextView-My tasks)) (nav)
  - act: CustomTouchEvent(state=5a31730de00024ff3c00560136a520d4, view=e380bb28286de2903837a163fbe204c8(TaskListActivity/View-)) (rule)
  - act: CustomTouchEvent(state=269c6a34f11e3a288aac56f6fabd01b7, view=7f539ba09e952b7178162c5cf90d3528(TaskListActivity/TextView-Add task)) (rule)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
