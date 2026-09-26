# Feature test report: OpenTasks

- Started: 2026-09-25 00:00:14
- Finished: 2026-09-25 00:28:47
- Features: 14
- Covered: 0
- Partial: 14
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 46% (mean completion ratio; the headline number)
- Coverage: 0% (features with every guide step matched)
- Stop reason: all_features_done
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 14
- Never attempted: 0
- Blocked then recovered on retry: 1
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

- Filled via credential.txt: 3
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 0% (0/14) — live journal self-report (covered / extracted features).
- Offline coverage: 0% (0 covered / 31; 10 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 8% (mean completion ratio).

## Findings

### G001 Create a task

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the app; Tap the 'Save' button
- Remaining steps: Tap the '+' floating action button; Enter the task title; Enter the task description
- Completion ratio: 0.40
- Credited from later features: G002, G003
- Actions taken: 10
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=4d728c3a8a61672f74ae75e6180dabe9(TaskListActivity/TextView-0 tasks)) (nav)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=fb8aaa5d056017170a30c6fbf8f99119(TaskListActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=30804cfa5efd19d6102a588d28768a70, view=b8c62ffc97ad19b67a4baf546eb1e362(EditTaskActivity/TextView-Create)) (nav)
  - act: CustomTouchEvent(state=30804cfa5efd19d6102a588d28768a70, view=b8c62ffc97ad19b67a4baf546eb1e362(EditTaskActivity/TextView-Create)) (nav)
  - act: CustomTouchEvent(state=30804cfa5efd19d6102a588d28768a70, view=9cad0af31adadac925cf81d98bf1cae6(EditTaskActivity/TextView-Local)) (nav)
  - act: CustomTouchEvent(state=3cc15677daefabfd5ecb882927783377, view=d479e4e8c2b34e4708ea59e43daf15b0(EditTaskActivity/TextView-Local)) (nav)
  - act: CustomTouchEvent(state=30804cfa5efd19d6102a588d28768a70, view=cea5154ac7526c54f710df81101cccae(EditTaskActivity/Spinner-)) (rule)
  - act: CustomTouchEvent(state=3cc15677daefabfd5ecb882927783377, view=44d71c47b30e1516e3b8bdf3f76eb2f2(EditTaskActivity/View-)) (rule)

### G002 Set a due date

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the task editor; Tap the 'Due' field; Select the date; Select the time
- Remaining steps: Set the due date
- Completion ratio: 0.67
- Credited from later features: G008, G010
- Actions taken: 6
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=6d8b7d30f2b1ebaf845f7c08e875abb6(TaskListActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=269c6a34f11e3a288aac56f6fabd01b7, view=58af100f594aab1ea7f59a561b464ff3(TaskListActivity/TextView-My tasks)) (llm)
  - act: CustomTouchEvent(state=5a31730de00024ff3c00560136a520d4, view=62dc5b1d4ddae3468d0832a51baa12c1(TaskListActivity/TextView-Local)) (llm)
  - act: CustomTouchEvent(state=269c6a34f11e3a288aac56f6fabd01b7, view=58af100f594aab1ea7f59a561b464ff3(TaskListActivity/TextView-My tasks)) (llm)
  - act: CustomTouchEvent(state=5a31730de00024ff3c00560136a520d4, view=e380bb28286de2903837a163fbe204c8(TaskListActivity/View-)) (rule)
  - act: CustomTouchEvent(state=269c6a34f11e3a288aac56f6fabd01b7, view=7b8b1045e948214f0f1d4fea3f27b2c6(TaskListActivity/Spinner-)) (rule)

### G003 Set the task priority

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the task editor
- Remaining steps: Tap the priority selector; Select the desired priority level; Tap the save button to confirm changes
- Completion ratio: 0.25
- Actions taken: 9
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=62b6976b3faeed2bbf1d8d959fd09046(TaskListActivity/TextView-My tasks)) (nav)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=3f02d4bed9ccdb09f6b1d04ec4a4e63e(TaskListActivity/TextView-Tasks)) (nav)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=b9bd3499ada8fcda67d53da65da2aad2, view=07203c6cf6f90ffee6acdd14aeb5ba96(TaskListActivity/TextView-Show compl)) (nav)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=3f02d4bed9ccdb09f6b1d04ec4a4e63e(TaskListActivity/TextView-Tasks)) (nav)
  - act: ScrollEvent(state=6ba115282a4422dcce2af57319729b83, view=02404317ae5caf0a8349e579471b71a9(TaskListActivity/ViewPager-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=fb8aaa5d056017170a30c6fbf8f99119(TaskListActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=30804cfa5efd19d6102a588d28768a70, view=3a1ba8c3ba5e963b93ca55311ad3aa1b(EditTaskActivity/TextView-SAVE)) (rule)

### G004 Set the task status

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the task editor; Tap the save button
- Remaining steps: Tap the status field; Select the desired status
- Completion ratio: 0.50
- Credited from later features: G002, G003
- Actions taken: 8
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, x=450, y=1120) (llm)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, x=450, y=1120) (llm)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, x=450, y=960) (llm)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=68c3488f3043b2ab82a4d54a0f0bdad3, view=07203c6cf6f90ffee6acdd14aeb5ba96(TaskListActivity/TextView-Show compl)) (nav)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, x=450, y=960) (llm)
  - act: ScrollEvent(state=6ba115282a4422dcce2af57319729b83, view=02404317ae5caf0a8349e579471b71a9(TaskListActivity/ViewPager-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=6d8b7d30f2b1ebaf845f7c08e875abb6(TaskListActivity/ImageView-)) (rule)

### G005 Add a location

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the task editor
- Remaining steps: tap the location field
- Completion ratio: 0.50
- Credited from later features: G002
- Actions taken: 3
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=eecbf65a8d849b474c73bc022b006880(TaskListActivity/TextView-Local)) (llm)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=62b6976b3faeed2bbf1d8d959fd09046(TaskListActivity/TextView-My tasks)) (nav)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=eecbf65a8d849b474c73bc022b006880(TaskListActivity/TextView-Local)) (llm)

### G006 Add a checklist

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the task editor; Tap the 'Add' button
- Remaining steps: Tap the checklist section; Enter the checklist item; Enter the second checklist item
- Completion ratio: 0.33
- Credited from later features: G002, G008
- Actions taken: 7
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, x=1026, y=288) (llm)
  - act: CustomTouchEvent(state=cead913e664a6c7388403e0cd07d1aba, view=1e6c12ceefc24680555839d18f4315fa(TaskListActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=cead913e664a6c7388403e0cd07d1aba, view=1e6c12ceefc24680555839d18f4315fa(TaskListActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=cead913e664a6c7388403e0cd07d1aba, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=b9bd3499ada8fcda67d53da65da2aad2, view=7452df90f418ba6334f9ebab9bb5de0c(TaskListActivity/CheckBox-)) (heuristic)
  - act: CustomTouchEvent(state=cead913e664a6c7388403e0cd07d1aba, view=b010a42480d0d3d87a2e8e3e8edc8f83(TaskListActivity/ExpandableListView-)) (llm)
  - act: ScrollEvent(state=cead913e664a6c7388403e0cd07d1aba, view=02404317ae5caf0a8349e579471b71a9(TaskListActivity/ViewPager-), direction=up) (afford_search)

### G007 Create a recurring task

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the task editor; Save the task
- Remaining steps: Tap the recurrence field; Select the recurrence type; Enter the recurrence interval; Enter the recurrence duration
- Completion ratio: 0.33
- Credited from later features: G002, G003
- Actions taken: 7
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=633924ed01f5e3a334f108accc99fa7f(TaskListActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=f07df933405e979adc3a686376fbfc19(TaskListActivity/TextView-0 tasks)) (nav)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=f07df933405e979adc3a686376fbfc19(TaskListActivity/TextView-0 tasks)) (nav)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=b9bd3499ada8fcda67d53da65da2aad2, view=07203c6cf6f90ffee6acdd14aeb5ba96(TaskListActivity/TextView-Show compl)) (nav)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=68c3488f3043b2ab82a4d54a0f0bdad3, view=07203c6cf6f90ffee6acdd14aeb5ba96(TaskListActivity/TextView-Show compl)) (nav)

### G008 Edit an existing task

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the task in the list to open the detail view
- Remaining steps: Tap the edit (pencil) icon; Enter the new title for the task; Enter the new description for the task; Tap the save icon to update the task; Verify the task has been updated in the list
- Completion ratio: 0.17
- Actions taken: 15
  - act: CustomTouchEvent(state=30804cfa5efd19d6102a588d28768a70, view=dd79489014f43689e4bdce27209d8f34(EditTaskActivity/TextView-My tasks)) (nav)
  - act: CustomTouchEvent(state=3cc15677daefabfd5ecb882927783377, view=44d71c47b30e1516e3b8bdf3f76eb2f2(EditTaskActivity/View-)) (rule)
  - act: CustomTouchEvent(state=30804cfa5efd19d6102a588d28768a70, view=254080ba7b1196f37307363600210a55(EditTaskActivity/TextView-DESCRIPTIO)) (rule)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=fb8aaa5d056017170a30c6fbf8f99119(TaskListActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=30804cfa5efd19d6102a588d28768a70, view=4023960839e67ca18dc36091a2c1fdfa(EditTaskActivity/TextView-Add item)) (afford_search)
  - act: CustomTouchEvent(state=30804cfa5efd19d6102a588d28768a70, view=dd79489014f43689e4bdce27209d8f34(EditTaskActivity/TextView-My tasks)) (nav)
  - act: CustomTouchEvent(state=c5caf391542226aedbbddf91d5a87a0a, view=1030a01f5a1a352325b9afb1e850db42(EditTaskActivity/TextView-OpenTasks )) (nav)
  - act: CustomTouchEvent(state=c5caf391542226aedbbddf91d5a87a0a, view=1030a01f5a1a352325b9afb1e850db42(EditTaskActivity/TextView-OpenTasks )) (nav)

### G009 Browse tasks grouped

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the app; Select the 'Due' tab; Select the 'Tasks' option
- Remaining steps: Select the 'Browse' option; Select the 'Grouped' option
- Completion ratio: 0.60
- Credited from later features: G002, G010, G012
- Actions taken: 8
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=4d37dc853f7a65fb57609b24ddd0e72a(TaskListActivity/TextView-Next days)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=4d37dc853f7a65fb57609b24ddd0e72a(TaskListActivity/TextView-Next days)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=633924ed01f5e3a334f108accc99fa7f(TaskListActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=08c7b54a5880668987e85a75202a107e(TaskListActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=62b6976b3faeed2bbf1d8d959fd09046(TaskListActivity/TextView-My tasks)) (nav)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=08c7b54a5880668987e85a75202a107e(TaskListActivity/RelativeLayout-)) (rule)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=3f02d4bed9ccdb09f6b1d04ec4a4e63e(TaskListActivity/TextView-Tasks)) (rule)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=4d728c3a8a61672f74ae75e6180dabe9(TaskListActivity/TextView-0 tasks)) (rule)

### G010 Browse tasks grouped

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the 'Lists' tab; Open the app; Select the 'Tasks' option
- Remaining steps: Select the 'Browse' option; Select the 'Grouped' option
- Completion ratio: 0.60
- Credited from later features: G002, G012
- Actions taken: 13
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, x=54, y=173) (visual_ground)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=927d320fc4ac51103b9a8958f0bb4728(TaskListActivity/TextView-Someday)) (heuristic)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=927d320fc4ac51103b9a8958f0bb4728(TaskListActivity/TextView-Someday)) (heuristic)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=8e1924bab4772f00bae4cc4ebafc58d3(TaskListActivity/ImageView-)) (heuristic)
  - act: CustomSetTextEvent(state=cead913e664a6c7388403e0cd07d1aba, view=eeed3a6f9e72df5f160cbf875183e4bd(TaskListActivity/AutoCompleteTextView-   Search), text=test) (heuristic)
  - act: CustomSetTextEvent(state=2e462b5b35dbf920f79423a40d97832c, view=f0eb811075ecfd89ca55e8914b864a96(TaskListActivity/AutoCompleteTextView-test), text=test) (heuristic)
  - act: CustomSetTextEvent(state=2e462b5b35dbf920f79423a40d97832c, view=f0eb811075ecfd89ca55e8914b864a96(TaskListActivity/AutoCompleteTextView-test), text=test) (heuristic)
  - act: CustomTouchEvent(state=2e462b5b35dbf920f79423a40d97832c, view=6d8b7d30f2b1ebaf845f7c08e875abb6(TaskListActivity/ImageView-)) (afford_search)

### G011 Browse tasks grouped

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the app; Select the 'Progress' tab; Select the 'Tasks' option
- Remaining steps: Select the 'Browse' option; Select the 'Grouped' option
- Completion ratio: 0.60
- Credited from later features: G002, G010, G012
- Actions taken: 8
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=633924ed01f5e3a334f108accc99fa7f(TaskListActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, x=42, y=420) (llm)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=3f02d4bed9ccdb09f6b1d04ec4a4e63e(TaskListActivity/TextView-Tasks)) (nav)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=eecbf65a8d849b474c73bc022b006880(TaskListActivity/TextView-Local)) (llm)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, view=8e1924bab4772f00bae4cc4ebafc58d3(TaskListActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=4a605044334d07df09baa4559220abc7, view=f07df933405e979adc3a686376fbfc19(TaskListActivity/TextView-0 tasks)) (nav)
  - act: CustomTouchEvent(state=4a605044334d07df09baa4559220abc7, view=f07df933405e979adc3a686376fbfc19(TaskListActivity/TextView-0 tasks)) (nav)
  - act: CustomTouchEvent(state=4a605044334d07df09baa4559220abc7, view=263245fb174ed0807ea645b0f75d063b(TaskListActivity/TextView-Task progr)) (rule)

### G012 Show

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the overflow menu (three dots) in the task list; Select 'Show completed tasks' from the overflow menu
- Remaining steps: Tap the 'Show' option in the navigation bar
- Completion ratio: 0.67
- Actions taken: 20
  - act: CustomTouchEvent(state=85a7b9d1bd51b13ca0c8714ec88445a2, view=59c6320c453fcb723c7ccec9b5306178(SyncSettingsActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, x=443, y=113) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=1e6c12ceefc24680555839d18f4315fa(TaskListActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=1e6c12ceefc24680555839d18f4315fa(TaskListActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=f07df933405e979adc3a686376fbfc19(TaskListActivity/TextView-0 tasks)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=f07df933405e979adc3a686376fbfc19(TaskListActivity/TextView-0 tasks)) (heuristic)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=f07df933405e979adc3a686376fbfc19(TaskListActivity/TextView-0 tasks)) (heuristic)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=6ab3e6aead58bb7b6cda879092ec7d34(TaskListActivity/TextView-Tasks due)) (rule)

### G013 Create a local task

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the overflow menu; Select 'Create' from the overflow menu
- Remaining steps: Select 'Local' from the navigation hints; Enter a title for the task; Enter a description for the task; Tap on the 'Create' button to save the task
- Completion ratio: 0.33
- Credited from later features: G012
- Actions taken: 7
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=c51e069783f396bf30b25cc8715b3697(TaskListActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=99879acd8c9123e1bfa4c988ec9da0fb(TaskListActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=99879acd8c9123e1bfa4c988ec9da0fb(TaskListActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, x=975, y=73) (llm)
  - act: CustomTouchEvent(state=b9bd3499ada8fcda67d53da65da2aad2, view=119f617b3a18633f172562f0b35a53e7(TaskListActivity/TextView-Refresh)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=adedc08e6e1d1028253210b215416c1f(TaskListActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, x=975, y=73) (llm)

### G014 Share a task

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the task detail view
- Remaining steps: tap the share icon
- Completion ratio: 0.50
- Credited from later features: G002
- Actions taken: 7
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=adedc08e6e1d1028253210b215416c1f(TaskListActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=2fe438c12de6c3420afcbcb28523c6b3(TaskListActivity/RelativeLayout-)) (llm)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=2fe438c12de6c3420afcbcb28523c6b3(TaskListActivity/RelativeLayout-)) (rule)
  - act: CustomTouchEvent(state=0b001e45709cb306cb2ab5ab0d988ac3, view=8e1924bab4772f00bae4cc4ebafc58d3(TaskListActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=6ba115282a4422dcce2af57319729b83, x=42, y=420) (llm)
  - act: CustomTouchEvent(state=f9aa42196d6b1170c3b57cb571f08f19, view=8a78771c7be8dd206266d4babc63938c(TaskListActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=68c3488f3043b2ab82a4d54a0f0bdad3, view=77b0c908c1caf33baac9df92ae31d880(TaskListActivity/CheckBox-)) (heuristic)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
