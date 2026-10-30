# Feature test report: Omni Notes

- Started: 2026-10-26 00:37:02
- Finished: 2026-10-26 01:36:37
- Features: 14
- Covered: 1
- Partial: 5
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 61% (mean completion ratio; the headline number)
- Coverage: 7% (features with every guide step matched)
- Stop reason: budget_time
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 14
- Never attempted: 0
- Blocked then recovered on retry: 0
- Blocked still: 0

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

- Filled via credential.txt: 42
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 7% (1/14) — live journal self-report (covered / extracted features).
- Offline coverage: not computed (no ground-truth JSON).

## Findings

### G001 Create a text note

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Tap the 'Save' button; Open the app; Tap the 'Text' option in the dropdown menu
- Remaining steps: Tap the '+' floating action button; Enter a title for the note; Enter the text content of the note
- Completion ratio: 0.50
- Credited from later features: G002, G006
- Actions taken: 31
  - act: CustomSetTextEvent(state=09cbe7a6bf7af3a1b687a1856b4bb377, view=8f928e3a89af1640a068ff45fb749f34(MainActivity/TextView-Created: 1), text=no) (nav)
  - act: CustomSetTextEvent(state=09cbe7a6bf7af3a1b687a1856b4bb377, view=8f928e3a89af1640a068ff45fb749f34(MainActivity/TextView-Created: 1), text=no) (nav)
  - act: CustomSetTextEvent(state=09cbe7a6bf7af3a1b687a1856b4bb377, view=64faab37a7f1d784e630b112abbcbd1c(MainActivity/EditText-no), text=no) (llm)
  - act: CustomSetTextEvent(state=09cbe7a6bf7af3a1b687a1856b4bb377, view=64faab37a7f1d784e630b112abbcbd1c(MainActivity/EditText-no), text=no) (llm)
  - act: CustomTouchEvent(state=09cbe7a6bf7af3a1b687a1856b4bb377, view=012a7f60c6cbc0d3d19ef1f47cb700b7(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=6b6441f7fe2ba63dbb9259fc97ff0160, view=b83ae67df4c76b97d6e66ab7c11b7e53(MainActivity/LinearLayout-)) (llm)
  - act: CustomSetTextEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=8f928e3a89af1640a068ff45fb749f34(MainActivity/TextView-Created: 1), text=no) (nav)
  - act: CustomSetTextEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=8f928e3a89af1640a068ff45fb749f34(MainActivity/TextView-Created: 1), text=no) (nav)

### G002 Convert a note between

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open a note; Select 'Convert to note'; Tap the overflow menu (three dots)
- Remaining steps: Select 'Convert to checklist'
- Completion ratio: 0.60
- Credited from later features: G006
- Actions taken: 24
  - act: CustomTouchEvent(state=fa860fc85e2f516238ea464661b47863, view=e2eb90c8dc2e50e57d2ed4c2c503029c(MainActivity/TextView-3)) (heuristic)
  - act: CustomTouchEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=bdd7c83bd888f01d089d99fc4f5434d8(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6576afdad7454f2d75516922dde9cf4e, view=054b67271be9a9d84649c2a01f5c8753(MainActivity/TextView-1)) (heuristic)
  - act: CustomTouchEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=bdd7c83bd888f01d089d99fc4f5434d8(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=d0010250343f2d5627c2b1e02dbef4a0, view=bf5476d09e74efe7d278b0ce522bbf33(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=21c0ff67a35dfaade3a688d022803445(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=b9192de12c58cca98c8cef7cacbb5921(MainActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=b9192de12c58cca98c8cef7cacbb5921(MainActivity/Button-)) (heuristic)

### G003 Record

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the Omni Notes app; Navigate to the note you want to record; Tap the attachment icon to add an audio file to the note
- Remaining steps: Tap the 'Record' option in the navigation bar; Start recording by tapping the 'Record' button; Stop recording by tapping the 'Stop' button
- Completion ratio: 0.50
- Credited from later features: G006
- Actions taken: 21
  - act: CustomTouchEvent(state=6b6441f7fe2ba63dbb9259fc97ff0160, view=e6038d76d1c12d281ea8b36bad53efba(MainActivity/TextView-Pin note)) (llm)
  - act: CustomTouchEvent(state=34620fd9b60f98edaa673d2d0dfe48e8, view=d6f67a261b43ca5f6160a13c86063346(MainActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=defd8e189032ea24eee9b3dfc9fc8148, view=82f69ca1ab7ed9d2278cc0e34cf74bf4(MainActivity/Button-)) (nav)
  - act: CustomTouchEvent(state=151faf2a66da818bba8939b2a5e82521, view=1bb0388414be7e37445c7d7745fb7810(MainActivity/TextView-Record)) (rule)
  - act: CustomTouchEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=012a7f60c6cbc0d3d19ef1f47cb700b7(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=e1586e52cadca260fb5bf6c7d9013a67, view=e6038d76d1c12d281ea8b36bad53efba(MainActivity/TextView-Pin note)) (llm)
  - act: CustomTouchEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=012a7f60c6cbc0d3d19ef1f47cb700b7(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=e1586e52cadca260fb5bf6c7d9013a67, view=e6038d76d1c12d281ea8b36bad53efba(MainActivity/TextView-Pin note)) (llm)

### G004 Add a location

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open a note; Tap the overflow menu; Select 'Add location'; Enter the location name
- Remaining steps: Tap 'Save'
- Completion ratio: 0.80
- Credited from later features: G006
- Actions taken: 29
  - act: CustomSetTextEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=64faab37a7f1d784e630b112abbcbd1c(MainActivity/EditText-no), text=no) (llm)
  - act: CustomSetTextEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=64faab37a7f1d784e630b112abbcbd1c(MainActivity/EditText-no), text=no) (llm)
  - act: CustomSetTextEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=d009b69f635491380557d0b028d99be6(MainActivity/EditText-no), text=no) (llm)
  - act: CustomSetTextEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=d009b69f635491380557d0b028d99be6(MainActivity/EditText-no), text=no) (llm)
  - act: CustomSetTextEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=33f1defd8ac369d416a78fad3d18b30e(MainActivity/TextView-Updated: m), text=no) (llm)
  - act: CustomSetTextEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=33f1defd8ac369d416a78fad3d18b30e(MainActivity/TextView-Updated: m), text=no) (llm)
  - act: CustomTouchEvent(state=1ec1ee371150576bb1a8a8c377f292c0, view=5b0f835c182e8baf10567fd1f32fd5f9(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=8d4eaaaf7b36955bea5f10f30e971e03, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (heuristic)

### G005 View all notes

- Status: **partial**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Tap 'Notes'; Open the navigation drawer (hamburger icon or left-edge swipe)
- Remaining steps: Tap 'Reminders'; Tap 'All'
- Completion ratio: 0.50
- Credited from later features: G001, G006
- Actions taken: 15
  - act: CustomTouchEvent(state=fc9efb1e0679b5e676d0cdb66065155a, view=5b0f835c182e8baf10567fd1f32fd5f9(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=fc9efb1e0679b5e676d0cdb66065155a, view=3d8c9a8af0cb85c59062297c7ad922f3(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=bb75f4778e8dd96e1355e12492a25c16, view=82f69ca1ab7ed9d2278cc0e34cf74bf4(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=151faf2a66da818bba8939b2a5e82521, view=7dc510ff0b3a60dcba301a014000f9a7(MainActivity/TextView-Files)) (llm)
  - act: CustomTouchEvent(state=bb75f4778e8dd96e1355e12492a25c16, view=bdd7c83bd888f01d089d99fc4f5434d8(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=fa860fc85e2f516238ea464661b47863, view=e2eb90c8dc2e50e57d2ed4c2c503029c(MainActivity/TextView-3)) (heuristic)
  - act: CustomTouchEvent(state=bb75f4778e8dd96e1355e12492a25c16, view=bdd7c83bd888f01d089d99fc4f5434d8(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=8d4eaaaf7b36955bea5f10f30e971e03, view=c242a44ccece00449df5b669552343db(MainActivity/ImageButton-)) (heuristic)

### G006 Assign a category

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Open a note; Tap the overflow menu; Select 'Assign a category'; Enter the name of the category; Select the category from the list
- Remaining steps: Tap 'Assign'
- Completion ratio: 0.83
- Credited from later features: G007
- Actions taken: 21
  - act: CustomTouchEvent(state=38941e7e064d125fbfbcbe8c8e518bdc, view=836f08446b30fada403186f9d479969b(CategoryActivity/TextView-Edit categ)) (nav)
  - act: CustomTouchEvent(state=38941e7e064d125fbfbcbe8c8e518bdc, view=836f08446b30fada403186f9d479969b(CategoryActivity/TextView-Edit categ)) (nav)
  - act: CustomTouchEvent(state=38941e7e064d125fbfbcbe8c8e518bdc, view=836f08446b30fada403186f9d479969b(CategoryActivity/TextView-Edit categ)) (nav)
  - act: CustomTouchEvent(state=38941e7e064d125fbfbcbe8c8e518bdc, view=836f08446b30fada403186f9d479969b(CategoryActivity/TextView-Edit categ)) (nav)
  - act: CustomTouchEvent(state=38941e7e064d125fbfbcbe8c8e518bdc, view=836f08446b30fada403186f9d479969b(CategoryActivity/TextView-Edit categ)) (llm)
  - act: CustomTouchEvent(state=38941e7e064d125fbfbcbe8c8e518bdc, view=5ca3e073513c74e4f70be05a91d4522b(CategoryActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=38941e7e064d125fbfbcbe8c8e518bdc, view=5ca3e073513c74e4f70be05a91d4522b(CategoryActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=38941e7e064d125fbfbcbe8c8e518bdc, view=ced08c0383a896e757129040310431c3(CategoryActivity/EditText-Title)) (rule)

### G007 Filter notes

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Open the navigation drawer; Tap 'Tags'; Select 'Filter' from the navigation drawer; Enter the desired tag in the filter input field
- Remaining steps: Tap the 'Apply' button to apply the filter
- Completion ratio: 0.80
- Actions taken: 27
  - act: CustomTouchEvent(state=1a0bf9fe7e96de6187e1d697ae1611bd, view=9c628fa4cec4e64c167ff9b105c35d0a(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=d30b987913fc2a6fb8e432d6fc50058b, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=d30b987913fc2a6fb8e432d6fc50058b, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=d30b987913fc2a6fb8e432d6fc50058b, view=5b563b4aaa579c7f9a16ac10c77ca0f1(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=d30b987913fc2a6fb8e432d6fc50058b, view=5b563b4aaa579c7f9a16ac10c77ca0f1(MainActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=d30b987913fc2a6fb8e432d6fc50058b, view=ab1750c7fcfbac622b638a762a75d31c(MainActivity/AutoCompleteTextView-Search in ), text=test) (llm)
  - act: CustomTouchEvent(state=20da456233493f5dd5e349a4ca11fb52, view=ef6c870f89e88f0542038819fde46f6d(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=20da456233493f5dd5e349a4ca11fb52, view=08ead1f0876f9c283fa5fa6b9d55bab6(MainActivity/Button-)) (rule)

### G008 Restore a note

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Open the drawer; Select the note to restore; Select 'Restore'
- Remaining steps: Tap 'Archive'; Tap 'Restore'
- Completion ratio: 0.60
- Credited from later features: G006
- Actions taken: 14
  - act: CustomTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=bdd7c83bd888f01d089d99fc4f5434d8(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6576afdad7454f2d75516922dde9cf4e, view=054b67271be9a9d84649c2a01f5c8753(MainActivity/TextView-1)) (heuristic)
  - act: CustomTouchEvent(state=ff5256e25d8a0c780680fbaade7625a5, view=bdd7c83bd888f01d089d99fc4f5434d8(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=bb5f613518b09c683aa8c977378bdff4, view=6a4542aad60ac5aba51f5e5404c3628b(MainActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=f85edee160742a7e13ca561595eabfc5, view=5b0f835c182e8baf10567fd1f32fd5f9(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=f1eab1d94220a3278772e1611f282bf2, view=6a4542aad60ac5aba51f5e5404c3628b(MainActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=c2e360fd919d90134f85341339f053be, view=5b0f835c182e8baf10567fd1f32fd5f9(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=f1eab1d94220a3278772e1611f282bf2, view=6a4542aad60ac5aba51f5e5404c3628b(MainActivity/ImageView-)) (nav)

### G009 Pin a note

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Long-press the note in the list
- Remaining steps: Tap the pin action in the contextual toolbar; Pinned notes stay above the rest
- Completion ratio: 0.33
- Credited from later features: G006
- Actions taken: 18
  - act: LongTouchEvent(state=c2e360fd919d90134f85341339f053be, view=bdd7c83bd888f01d089d99fc4f5434d8(MainActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=c2e360fd919d90134f85341339f053be, view=21c0ff67a35dfaade3a688d022803445(MainActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=c2e360fd919d90134f85341339f053be, view=21c0ff67a35dfaade3a688d022803445(MainActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=c2e360fd919d90134f85341339f053be, view=b9192de12c58cca98c8cef7cacbb5921(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=c2e360fd919d90134f85341339f053be, view=ce00e99b2459176dea9208842c560a16(MainActivity/ViewGroup-)) (llm)
  - act: CustomTouchEvent(state=c2e360fd919d90134f85341339f053be, view=ce00e99b2459176dea9208842c560a16(MainActivity/ViewGroup-)) (llm)
  - act: CustomTouchEvent(state=c2e360fd919d90134f85341339f053be, view=816fe349bff4a856c57af87bccf7c284(MainActivity/TextView-Reminder s)) (llm)
  - act: CustomTouchEvent(state=02d4cf85c40f1891a78e5fcf9f190cc7, view=0ee96df1df8627cd6277422d97f548bb(MainActivity/Button-OK)) (rule)

### G010 Merge several notes

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Long-press the first note; Tap the 'Merge' option in the menu that appears; Tap the additional notes to add them to the selection
- Remaining steps: Select the notes to merge; Tap the 'Merge' button to complete the merge operation
- Completion ratio: 0.60
- Credited from later features: G006
- Actions taken: 13
  - act: CustomTouchEvent(state=60bac118b3d1b28e5b9ce568d9694ec0, view=44d1829028ed013abc01d393f1e97744(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=60bac118b3d1b28e5b9ce568d9694ec0, view=44d1829028ed013abc01d393f1e97744(MainActivity/View-)) (llm)
  - act: LongTouchEvent(state=60bac118b3d1b28e5b9ce568d9694ec0, view=5b0f835c182e8baf10567fd1f32fd5f9(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=60bac118b3d1b28e5b9ce568d9694ec0, view=21c0ff67a35dfaade3a688d022803445(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=c2e360fd919d90134f85341339f053be, view=b9192de12c58cca98c8cef7cacbb5921(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=c2e360fd919d90134f85341339f053be, view=012a7f60c6cbc0d3d19ef1f47cb700b7(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=6b6441f7fe2ba63dbb9259fc97ff0160, view=aec83566785ed515732b514662cd53c1(MainActivity/TextView-Add shortc)) (heuristic)
  - act: CustomTouchEvent(state=c2e360fd919d90134f85341339f053be, view=012a7f60c6cbc0d3d19ef1f47cb700b7(MainActivity/ImageView-)) (heuristic)

### G011 Add a note

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the 'Share' button; Open the Omni Notes app; Select 'Add a note' from the navigation hints; Select the text or file you want to add to a note; Tap the 'Save' button to add the note; Enter the note content
- Completion ratio: 1.00
- Credited from later features: G002, G006, G007
- Actions taken: 10
  - act: CustomTouchEvent(state=60bac118b3d1b28e5b9ce568d9694ec0, view=bdd7c83bd888f01d089d99fc4f5434d8(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=fa860fc85e2f516238ea464661b47863, view=532200316c4e070a6673fcae8ecece7b(MainActivity/TextView-ADD CATEGO)) (nav)
  - act: CustomTouchEvent(state=38941e7e064d125fbfbcbe8c8e518bdc, view=836f08446b30fada403186f9d479969b(CategoryActivity/TextView-Edit categ)) (llm)
  - act: CustomTouchEvent(state=38941e7e064d125fbfbcbe8c8e518bdc, view=836f08446b30fada403186f9d479969b(CategoryActivity/TextView-Edit categ)) (llm)
  - act: CustomTouchEvent(state=38941e7e064d125fbfbcbe8c8e518bdc, view=4f7a42c2d6bee2f1f8d6198cccfc0284(CategoryActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=1195331f37b281d806d590a187d2ea07, view=78cb6c3f85283b8d8f5a490051da9b20(CategoryActivity/TextView-CUSTOM)) (rule)
  - act: CustomTouchEvent(state=6b6441f7fe2ba63dbb9259fc97ff0160, view=e6038d76d1c12d281ea8b36bad53efba(MainActivity/TextView-Pin note)) (heuristic)
  - act: CustomSetTextEvent(state=c2e360fd919d90134f85341339f053be, view=64faab37a7f1d784e630b112abbcbd1c(MainActivity/EditText-no), text=no) (mandatory_fill)

### G012 Switch the note list

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Tap the overflow menu in the note list; Observe the note list switch to the expanded card layout; Select the 'Layout' option
- Remaining steps: Tap the 'Expanded view' toggle
- Completion ratio: 0.75
- Credited from later features: G006
- Actions taken: 16
  - act: CustomTouchEvent(state=c2e360fd919d90134f85341339f053be, view=a307f777e59b672054ec2496573e3570(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=02d4cf85c40f1891a78e5fcf9f190cc7, view=de5153b96876b1393459b2f581c6acf8(MainActivity/Button-OCT 26, 20)) (nav)
  - act: CustomTouchEvent(state=debec73eb47368b3b78646a7079e48fc, view=824fa97691ec4f975eeeac55a8f407a4(MainActivity/Button-11:55 AM)) (nav)
  - act: CustomTouchEvent(state=02d4cf85c40f1891a78e5fcf9f190cc7, view=de5153b96876b1393459b2f581c6acf8(MainActivity/Button-OCT 26, 20)) (nav)
  - act: CustomTouchEvent(state=debec73eb47368b3b78646a7079e48fc, view=0ee96df1df8627cd6277422d97f548bb(MainActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=c2e360fd919d90134f85341339f053be, view=816fe349bff4a856c57af87bccf7c284(MainActivity/TextView-Reminder s)) (llm)
  - act: CustomTouchEvent(state=02d4cf85c40f1891a78e5fcf9f190cc7, view=c0d34b1863e93f7177ebd57f324c33ff(MainActivity/Button-CANCEL)) (nav)
  - act: CustomTouchEvent(state=c2e360fd919d90134f85341339f053be, view=e204bce1f281a123fa603e09646cf453(MainActivity/ImageView-)) (llm)

### G013 Export a full backup

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Open Settings
- Remaining steps: Tap 'Data'; Tap 'Export Data'; Select 'Export Full Backup'; Tap 'Export' to confirm; Wait for the backup to complete
- Completion ratio: 0.17
- Credited from later features: G006
- Actions taken: 17
  - act: CustomTouchEvent(state=02d4cf85c40f1891a78e5fcf9f190cc7, view=e77bc9d7bce367f9be69269ca1fc1626(MainActivity/TextView-11)) (llm)
  - act: CustomTouchEvent(state=02d4cf85c40f1891a78e5fcf9f190cc7, view=5b6ce0f51590be3909aa6d24f0671aa7(MainActivity/RadialTimePickerView$RadialPickerTouchHelper-)) (llm)
  - act: CustomTouchEvent(state=b5dcef7bf793ce60d23c04082976c66b, view=430d57374263df50214bcca2cb5e5d41(MainActivity/TextView-12)) (llm)
  - act: CustomTouchEvent(state=7ec46b6ae79abffaf28dbdf19793e4d3, view=430d57374263df50214bcca2cb5e5d41(MainActivity/TextView-12)) (llm)
  - act: CustomTouchEvent(state=7ec46b6ae79abffaf28dbdf19793e4d3, view=5b6ce0f51590be3909aa6d24f0671aa7(MainActivity/RadialTimePickerView$RadialPickerTouchHelper-)) (llm)
  - act: CustomTouchEvent(state=b5dcef7bf793ce60d23c04082976c66b, view=b91363d0e94a0f8462ff25eb7b0e220e(MainActivity/RadialTimePickerView$RadialPickerTouchHelper-)) (afford_search)
  - act: CustomTouchEvent(state=f2f48476196b42ed1a25c839029bb66d, view=a8a73e1c7bccab3481519195da73f092(MainActivity/RadialTimePickerView$RadialPickerTouchHelper-)) (llm)
  - act: CustomTouchEvent(state=b5dcef7bf793ce60d23c04082976c66b, view=0ee96df1df8627cd6277422d97f548bb(MainActivity/Button-OK)) (rule)

### G014 Delete an existing backup

- Status: **pending**
- Reason: Retry round 2; budget remains.
- Feature source: guide
- Completed steps: Open Settings
- Remaining steps: tap "Data"
- Completion ratio: 0.50
- Credited from later features: G006
- Actions taken: 15
  - act: CustomTouchEvent(state=09cbe7a6bf7af3a1b687a1856b4bb377, view=bdd7c83bd888f01d089d99fc4f5434d8(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=fa860fc85e2f516238ea464661b47863, view=71336219debdf69f2d98426a466e332f(MainActivity/TextView-REMOVE CAT)) (rule)
  - act: CustomTouchEvent(state=09cbe7a6bf7af3a1b687a1856b4bb377, view=bdd7c83bd888f01d089d99fc4f5434d8(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=d0010250343f2d5627c2b1e02dbef4a0, view=71336219debdf69f2d98426a466e332f(MainActivity/TextView-REMOVE CAT)) (rule)
  - act: CustomTouchEvent(state=09cbe7a6bf7af3a1b687a1856b4bb377, view=21c0ff67a35dfaade3a688d022803445(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=09cbe7a6bf7af3a1b687a1856b4bb377, view=21c0ff67a35dfaade3a688d022803445(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=09cbe7a6bf7af3a1b687a1856b4bb377, view=b9192de12c58cca98c8cef7cacbb5921(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=09cbe7a6bf7af3a1b687a1856b4bb377, view=b9192de12c58cca98c8cef7cacbb5921(MainActivity/Button-)) (heuristic)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
