# Feature test report: Markor

- Started: 2026-10-25 18:32:38
- Finished: 2026-10-25 19:31:33
- Features: 14
- Covered: 1
- Partial: 11
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 49% (mean completion ratio; the headline number)
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
- README-extracted features: 8
- In both: 0
- Guide-only: 14
- README-only: 8
  - guide-only: G001 Browse the notebook folder
  - guide-only: G002 Create a folder
  - guide-only: G003 Apply Markdown formatting
  - guide-only: G004 Insert an image
  - guide-only: G005 Insert a table
  - guide-only: G006 Search across all files
  - guide-only: G007 Manage a todo.txt file
  - guide-only: G008 Preview a CSV file
  - guide-only: G009 Share the document
  - guide-only: G010 Delete files
  - guide-only: G011 Sort the file list
  - guide-only: G012 View recent
  - README-only: F001 Close or skip the tutorial
  - README-only: F002 Leave any first-run analytics or settings screen
  - README-only: F003 Tap Create Database or Open Database if shown
  - README-only: F004 Enter a file name if asked and confirm Save
  - README-only: F005 Reach the home or main screen
  - README-only: F006 Search
  - README-only: F007 Import or export data
  - README-only: F008 Change app settings

## Text-field resolution

- Filled via credential.txt: 16
- Filled via VLM/Gemini: 34
- Unresolved: 2
- Online coverage: 7% (1/14) — live journal self-report (covered / extracted features).
- Offline coverage: not computed (no ground-truth JSON).

## Findings

### G001 Browse the notebook folder

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Files' tab; Open the app; Observe the notebook folder structure
- Remaining steps: Select 'Browse' from the navigation hints; Select 'notebook' from the navigation hints; Select 'folder' from the navigation hints
- Completion ratio: 0.50
- Credited from later features: G002, G005, G014
- Actions taken: 22
  - act: CustomTouchEvent(state=e1b8dd09e0ce27e87863f46479f4946e, view=379e3d41b18d167029424e435ef55269(DocumentActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=8f26b3bda107783586ed639eac7ac574, view=0036d7df67c5f0968be798f56f31b9b4(DocumentActivity/CheckBox-)) (heuristic)
  - act: CustomSetTextEvent(state=1409a4975334be0addbb1df14fcfbf32, view=11ca652d84dfe544611d5df6806faeec(DocumentActivity/EditText-), text=no) (llm)
  - act: CustomSetTextEvent(state=c90254b2a6c4497ff03b7bd1bee756d2, view=b4fcb83a90ff104589fb0cb4c25fdc58(DocumentActivity/EditText-no), text=no) (llm)
  - act: CustomSetTextEvent(state=c90254b2a6c4497ff03b7bd1bee756d2, view=b4fcb83a90ff104589fb0cb4c25fdc58(DocumentActivity/EditText-no), text=no) (llm)
  - act: CustomTouchEvent(state=c90254b2a6c4497ff03b7bd1bee756d2, view=116397ad79d4405dba16e3988ff65937(DocumentActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=e1b8dd09e0ce27e87863f46479f4946e, view=cd4d49b2c10e77d6d325871fe9773870(DocumentActivity/LinearLayout-)) (nav)
  - act: CustomTouchEvent(state=8f26b3bda107783586ed639eac7ac574, view=253cd79028cc1b708ff388553ae41105(DocumentActivity/ImageView-)) (heuristic)

### G002 Create a folder

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Files' tab; Tap the '+' button; Select 'Create' from the menu
- Remaining steps: Select 'Folder' from the sub-menu; Enter a name for the new folder; Tap 'Create' to finalize the folder creation
- Completion ratio: 0.50
- Credited from later features: G001, G006
- Actions taken: 17
  - act: CustomTouchEvent(state=dd077f391cfe8c7eb02d8ffad01ab609, view=bec2b31d8c332d86c10d746a0083a899(DocumentActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=ba3eb1d3e2ef76b932897c60e815e2cc, view=116397ad79d4405dba16e3988ff65937(DocumentActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=e1b8dd09e0ce27e87863f46479f4946e, view=4c80e1716737c1f50cbc063ddb319ff2(DocumentActivity/TextView-Reload)) (llm)
  - act: CustomTouchEvent(state=d33bfb7e26007d6e6674c2102faf70d5, view=116397ad79d4405dba16e3988ff65937(DocumentActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=e1b8dd09e0ce27e87863f46479f4946e, view=13cf2611138b0c7b55ea98bc6ad9bfcb(DocumentActivity/TextView-Info)) (llm)
  - act: CustomTouchEvent(state=1a699f5c8b3772660044089f55f71da0, view=80c2dbeb5d536d2055114c63b272e21f(DocumentActivity/CheckBox-List in re)) (llm)
  - act: CustomTouchEvent(state=a2ff24481aca086cf8afecc4900f0851, view=4a4b203e755175bf12d5bf0a36f32658(DocumentActivity/CheckBox-List in re)) (llm)
  - act: CustomTouchEvent(state=1a699f5c8b3772660044089f55f71da0, view=76245354bb05f05079a4d989e48bd0e1(DocumentActivity/Button-OK)) (llm)

### G003 Apply Markdown formatting

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the 'Apply' button; Open a Markdown document; Tap the action toolbar; Place the cursor or select text
- Remaining steps: Select the 'Markdown' option; Choose the desired formatting option
- Completion ratio: 0.67
- Credited from later features: G001, G005, G006
- Actions taken: 16
  - act: CustomTouchEvent(state=c9c58379dcbd26eb5bf8a4b490a264a9, view=62bfc1505b2bd1eb0adf75e3618e090d(DocumentActivity/TextView-Text Case)) (heuristic)
  - act: CustomTouchEvent(state=c9c58379dcbd26eb5bf8a4b490a264a9, view=15b1ff0aace9a683a494a16cf7b94209(DocumentActivity/TextView-Toggle Cas)) (rule)
  - act: CustomSetTextEvent(state=d33bfb7e26007d6e6674c2102faf70d5, view=11ca652d84dfe544611d5df6806faeec(DocumentActivity/EditText-), text=test) (heuristic)
  - act: CustomSetTextEvent(state=aa9373c3256940c529c461efe5462260, view=3790f6cb9c2b15742ba71ae1ea9a9a8e(DocumentActivity/EditText-test), text=test) (heuristic)
  - act: CustomSetTextEvent(state=aa9373c3256940c529c461efe5462260, view=3790f6cb9c2b15742ba71ae1ea9a9a8e(DocumentActivity/EditText-test), text=test) (heuristic)
  - act: ScrollEvent(state=aa9373c3256940c529c461efe5462260, view=84776a42d19353a793a6c89dc6a15a42(DocumentActivity/HorizontalScrollView-), direction=up) (afford_search)
  - act: CustomSetTextEvent(state=9b6b2e375b030225c21ab156aacd4c5e, view=3790f6cb9c2b15742ba71ae1ea9a9a8e(DocumentActivity/EditText-test), text=test) (heuristic)
  - act: CustomSetTextEvent(state=9b6b2e375b030225c21ab156aacd4c5e, view=3790f6cb9c2b15742ba71ae1ea9a9a8e(DocumentActivity/EditText-test), text=test) (heuristic)

### G004 Insert an image

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open a document; Select 'pick from gallery'; Tap the 'Insert' button to add the image to the document
- Remaining steps: Tap the image/attachment action in the action bar; Choose an image from the gallery
- Completion ratio: 0.60
- Credited from later features: G005, G006, G009
- Actions taken: 10
  - act: CustomTouchEvent(state=97ea3ad0cbf00e458186943445e0539a, view=7c8dd4b032ea320f39817b788cf3e790(MainActivity/ImageView-)) (heuristic)
  - act: CustomSetTextEvent(state=fbb04da3627db249a1d300a080468717, view=1c1812a2651e76ac4baccdba97acbf37(MainActivity/EditText-Search), text=test) (llm)
  - act: CustomTouchEvent(state=97ea3ad0cbf00e458186943445e0539a, view=7c8dd4b032ea320f39817b788cf3e790(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=9b6b2e375b030225c21ab156aacd4c5e, view=8a62deca55a31cef51123601db0596aa(DocumentActivity/ViewGroup-)) (heuristic)
  - act: CustomTouchEvent(state=9b6b2e375b030225c21ab156aacd4c5e, view=8a62deca55a31cef51123601db0596aa(DocumentActivity/ViewGroup-)) (heuristic)
  - act: CustomTouchEvent(state=9b6b2e375b030225c21ab156aacd4c5e, view=a4b5212b4a38a940616d0c04c32f3f1f(DocumentActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=21be4b900c20bb3fea3ba714fa1e7947, view=11ca652d84dfe544611d5df6806faeec(DocumentActivity/EditText-), text=test) (heuristic)
  - act: CustomTouchEvent(state=9b6b2e375b030225c21ab156aacd4c5e, view=a4b5212b4a38a940616d0c04c32f3f1f(DocumentActivity/Button-)) (heuristic)

### G005 Insert a table

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open a Markdown document
- Remaining steps: Tap the table action in the action bar; Select the table option from the dropdown menu; Enter the number of rows and columns for the table; Tap the 'Insert' button to confirm and insert the table
- Completion ratio: 0.20
- Actions taken: 18
  - act: CustomTouchEvent(state=21be4b900c20bb3fea3ba714fa1e7947, view=f4681fea0788a1c1728da0bf59118540(DocumentActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=83f7ffff61adcb41d804d89120dfb60b, view=aee9b5dd19570ac246f20ee77ffc8cc5(DocumentActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=256a2f81641d1a7731007e9d8a9ebfc7, view=ede26c1c97471184d258f5baf404753c(DocumentActivity/TextView-Insert lin)) (nav)
  - act: CustomTouchEvent(state=256a2f81641d1a7731007e9d8a9ebfc7, view=ede26c1c97471184d258f5baf404753c(DocumentActivity/TextView-Insert lin)) (nav)
  - act: CustomTouchEvent(state=256a2f81641d1a7731007e9d8a9ebfc7, view=6e826bf637b8aa1d2142236970d4ec5a(DocumentActivity/Button-CANCEL)) (afford_search)
  - act: CustomSetTextEvent(state=256a2f81641d1a7731007e9d8a9ebfc7, view=84db14bcbedab5c9923a0f7d288bcc38(DocumentActivity/EditText-Descriptio), text=test) (llm)
  - act: CustomTouchEvent(state=e4acc0e399c7dcb4d60416e452c5e6ef, view=ede26c1c97471184d258f5baf404753c(DocumentActivity/TextView-Insert lin)) (nav)
  - act: CustomTouchEvent(state=e4acc0e399c7dcb4d60416e452c5e6ef, view=76245354bb05f05079a4d989e48bd0e1(DocumentActivity/Button-OK)) (rule)

### G006 Search across all files

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the search icon in the toolbar; Enter 'search' in the search bar; Tap the search icon in the search bar; Select 'across all' from the search options; Select the desired file from the search results
- Completion ratio: 1.00
- Actions taken: 7
  - act: CustomTouchEvent(state=8f26b3bda107783586ed639eac7ac574, view=379e3d41b18d167029424e435ef55269(DocumentActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=dd077f391cfe8c7eb02d8ffad01ab609, view=cd4d49b2c10e77d6d325871fe9773870(DocumentActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=7e1fa6b6a83234c0d09b8729053884e4, view=12fcdec1ccd508ac28e22b2aa8186343(DocumentActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=7e1fa6b6a83234c0d09b8729053884e4, view=11ca652d84dfe544611d5df6806faeec(DocumentActivity/EditText-), text=test) (mandatory_fill)
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=fb911fe14f9609420d660d30e145f8dc, view=877b7331735c4e2cc5824bb969a2a414(DocumentActivity/EditText-Search)) (heuristic)
  - act: CustomTouchEvent(state=fb911fe14f9609420d660d30e145f8dc, view=877b7331735c4e2cc5824bb969a2a414(DocumentActivity/EditText-Search)) (heuristic)

### G007 Manage a todo.txt file

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select 'todo.txt' from the list of files; Open the Markor app
- Remaining steps: Navigate to the 'todo' section in the navigation drawer; Enter the text editor mode; Type a todo item and press Enter to add it to the list
- Completion ratio: 0.40
- Credited from later features: G002, G009
- Actions taken: 17
  - act: CustomSetTextEvent(state=e4acc0e399c7dcb4d60416e452c5e6ef, view=b2910e7cec248651627bdfae15770fcd(DocumentActivity/EditText-test), text=test) (rule)
  - act: CustomSetTextEvent(state=e4acc0e399c7dcb4d60416e452c5e6ef, view=1022a3323758a30ebf5eed5935f581e3(DocumentActivity/EditText-URL / Path), text=https://example.com/feed.xml) (llm)
  - act: CustomSetTextEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=6c079893b41acf4c6eac4a0faa964851(DocumentActivity/EditText-https://ex), text=https://example.com/feed.xml) (rule)
  - act: CustomSetTextEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=6c079893b41acf4c6eac4a0faa964851(DocumentActivity/EditText-https://ex), text=https://example.com/feed.xml) (rule)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=6e826bf637b8aa1d2142236970d4ec5a(DocumentActivity/Button-CANCEL)) (afford_search)
  - act: CustomSetTextEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=1022a3323758a30ebf5eed5935f581e3(DocumentActivity/EditText-URL / Path), text=https://example.com/feed.xml) (rule)
  - act: CustomSetTextEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=1022a3323758a30ebf5eed5935f581e3(DocumentActivity/EditText-URL / Path), text=https://example.com/feed.xml) (rule)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=76245354bb05f05079a4d989e48bd0e1(DocumentActivity/Button-OK)) (rule)

### G008 Preview a CSV file

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open a .csv file
- Remaining steps: tap the preview/eye icon
- Completion ratio: 0.50
- Credited from later features: G009
- Actions taken: 16
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=a9a9f4053ed1503a45872d8b11415b8a(DocumentActivity/Button-BROWSE FIL)) (nav)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=a9a9f4053ed1503a45872d8b11415b8a(DocumentActivity/Button-BROWSE FIL)) (nav)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=251c5e5bc43155f20cb13301017912f3(DocumentActivity/Button-SEARCH DOC)) (rule)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=251c5e5bc43155f20cb13301017912f3(DocumentActivity/Button-SEARCH DOC)) (rule)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=6e826bf637b8aa1d2142236970d4ec5a(DocumentActivity/Button-CANCEL)) (rule)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=76245354bb05f05079a4d989e48bd0e1(DocumentActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=ede26c1c97471184d258f5baf404753c(DocumentActivity/TextView-Insert lin)) (rule)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=ede26c1c97471184d258f5baf404753c(DocumentActivity/TextView-Insert lin)) (rule)

### G009 Share the document

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open a document; Select 'Share' from the menu
- Remaining steps: Tap the overflow menu; Enter the desired sharing method (e.g., email, file sharing, etc.); Tap the 'Share' button to complete the action
- Completion ratio: 0.40
- Credited from later features: G006
- Actions taken: 21
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=251c5e5bc43155f20cb13301017912f3(DocumentActivity/Button-SEARCH DOC)) (nav)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=251c5e5bc43155f20cb13301017912f3(DocumentActivity/Button-SEARCH DOC)) (nav)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=251c5e5bc43155f20cb13301017912f3(DocumentActivity/Button-SEARCH DOC)) (nav)
  - act: CustomTouchEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=251c5e5bc43155f20cb13301017912f3(DocumentActivity/Button-SEARCH DOC)) (nav)
  - act: CustomSetTextEvent(state=4eff9a62b40d4b5b0145f87de95a5f1f, view=6c079893b41acf4c6eac4a0faa964851(DocumentActivity/EditText-https://ex), text=testcube.bench@example.com) (llm)
  - act: CustomTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=251c5e5bc43155f20cb13301017912f3(DocumentActivity/Button-SEARCH DOC)) (nav)
  - act: CustomSetTextEvent(state=9785f84d68898c366c72fe086a3daa34, view=1450335372f050502f857794a8aa024e(DocumentActivity/EditText-testcube.b), text=testcube.bench@example.com) (llm)
  - act: CustomTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=76245354bb05f05079a4d989e48bd0e1(DocumentActivity/Button-OK)) (rule)

### G010 Delete files

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Files' tab in the navigation bar.; Verify that the file or folder is no longer present in the 'Files' tab.
- Remaining steps: Long-press on the file or folder you wish to delete.; Select the 'Delete' option from the context menu.; Confirm the deletion by tapping 'Delete' on the confirmation dialog.
- Completion ratio: 0.40
- Credited from later features: G002
- Actions taken: 18
  - act: LongTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=ede26c1c97471184d258f5baf404753c(DocumentActivity/TextView-Insert lin)) (heuristic)
  - act: LongTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=251c5e5bc43155f20cb13301017912f3(DocumentActivity/Button-SEARCH DOC)) (heuristic)
  - act: LongTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=6e826bf637b8aa1d2142236970d4ec5a(DocumentActivity/Button-CANCEL)) (afford_search)
  - act: LongTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=a9a9f4053ed1503a45872d8b11415b8a(DocumentActivity/Button-BROWSE FIL)) (heuristic)
  - act: LongTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=1450335372f050502f857794a8aa024e(DocumentActivity/EditText-testcube.b)) (llm)
  - act: LongTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=1022a3323758a30ebf5eed5935f581e3(DocumentActivity/EditText-URL / Path)) (llm)
  - act: LongTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=1022a3323758a30ebf5eed5935f581e3(DocumentActivity/EditText-URL / Path)) (llm)
  - act: CustomTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=1450335372f050502f857794a8aa024e(DocumentActivity/EditText-testcube.b)) (rule)

### G011 Sort the file list

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open the Files tab; Select the desired sorting option
- Remaining steps: Tap the sort icon (or the overflow menu); Select 'folders first'; Tap 'sort'
- Completion ratio: 0.40
- Credited from later features: G002, G006
- Actions taken: 14
  - act: CustomTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=a9a9f4053ed1503a45872d8b11415b8a(DocumentActivity/Button-BROWSE FIL)) (nav)
  - act: CustomTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=6e826bf637b8aa1d2142236970d4ec5a(DocumentActivity/Button-CANCEL)) (nav)
  - act: CustomTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=ede26c1c97471184d258f5baf404753c(DocumentActivity/TextView-Insert lin)) (rule)
  - act: CustomTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=6e826bf637b8aa1d2142236970d4ec5a(DocumentActivity/Button-CANCEL)) (afford_search)
  - act: CustomTouchEvent(state=9785f84d68898c366c72fe086a3daa34, view=a9a9f4053ed1503a45872d8b11415b8a(DocumentActivity/Button-BROWSE FIL)) (nav)
  - act: CustomSetTextEvent(state=9785f84d68898c366c72fe086a3daa34, view=1450335372f050502f857794a8aa024e(DocumentActivity/EditText-testcube.b), text=testcube.bench@example.com) (llm)
  - act: CustomSetTextEvent(state=9785f84d68898c366c72fe086a3daa34, view=1450335372f050502f857794a8aa024e(DocumentActivity/EditText-testcube.b), text=testcube.bench@example.com) (llm)
  - act: CustomSetTextEvent(state=9785f84d68898c366c72fe086a3daa34, view=1450335372f050502f857794a8aa024e(DocumentActivity/EditText-testcube.b), text=testcube.bench@example.com) (llm)

### G012 View recent

- Status: **partial**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the Files tab
- Remaining steps: Tap the 'Go to' menu; Select 'recent documents'
- Completion ratio: 0.33
- Credited from later features: G002
- Actions taken: 11
  - act: CustomTouchEvent(state=e1b8dd09e0ce27e87863f46479f4946e, view=4c80e1716737c1f50cbc063ddb319ff2(DocumentActivity/TextView-Reload)) (llm)
  - act: CustomTouchEvent(state=ee617577afbf18203edd3294ae47695b, view=f6b41ddc192faff14431a71e2f30b140(DocumentActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=ee617577afbf18203edd3294ae47695b, view=b9260d3e4f8b656b3d45dbd89ed6df0b(DocumentActivity/TextView-2026-10-12)) (llm)
  - act: CustomTouchEvent(state=a6c8d7ddf742b4f42699a92522b7f792, view=f24bf9812cb6e05161fb06842f695bea(DocumentActivity/TextView-Priority)) (llm)
  - act: CustomTouchEvent(state=62445f96ec79a06ea1747fef6e63eea2, view=904049515121ea2e8fb25cd5083d4ed8(DocumentActivity/Button-OK (0))) (llm)
  - act: CustomTouchEvent(state=53b6c7eef0f74f9c19c0522b00bfe38a, view=72940d34e8a8dc749374a7484386a96d(DocumentActivity/CheckedTextView-)) (rule)
  - act: CustomSetTextEvent(state=9785f84d68898c366c72fe086a3daa34, view=1450335372f050502f857794a8aa024e(DocumentActivity/EditText-testcube.b), text=testcube.bench@example.com) (llm)
  - act: CustomSetTextEvent(state=9785f84d68898c366c72fe086a3daa34, view=1450335372f050502f857794a8aa024e(DocumentActivity/EditText-testcube.b), text=testcube.bench@example.com) (llm)

### G013 Open a file

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the Files tab
- Remaining steps: long-press a file
- Completion ratio: 0.50
- Credited from later features: G002
- Actions taken: 8
  - act: LongTouchEvent(state=53b6c7eef0f74f9c19c0522b00bfe38a, view=904049515121ea2e8fb25cd5083d4ed8(DocumentActivity/Button-OK (0))) (heuristic)
  - act: LongTouchEvent(state=01aed7d780f4d89dd72a9f1ef30fe252, view=acb316b218f0b0ee74689d969c515cc3(DocumentActivity/ImageView-)) (heuristic)
  - act: LongTouchEvent(state=01aed7d780f4d89dd72a9f1ef30fe252, view=acb316b218f0b0ee74689d969c515cc3(DocumentActivity/ImageView-)) (heuristic)
  - act: LongTouchEvent(state=01aed7d780f4d89dd72a9f1ef30fe252, view=b34d1ba50d4c7b7b4e789d7e532666c8(DocumentActivity/ImageView-)) (heuristic)
  - act: LongTouchEvent(state=01aed7d780f4d89dd72a9f1ef30fe252, view=b34d1ba50d4c7b7b4e789d7e532666c8(DocumentActivity/ImageView-)) (heuristic)
  - act: LongTouchEvent(state=01aed7d780f4d89dd72a9f1ef30fe252, view=b9260d3e4f8b656b3d45dbd89ed6df0b(DocumentActivity/TextView-2026-10-12)) (llm)
  - act: LongTouchEvent(state=01aed7d780f4d89dd72a9f1ef30fe252, view=0acba5155222837b52332537ec99c84e(DocumentActivity/ViewGroup-)) (llm)
  - act: LongTouchEvent(state=01aed7d780f4d89dd72a9f1ef30fe252, view=0acba5155222837b52332537ec99c84e(DocumentActivity/ViewGroup-)) (llm)

### G014 Change the notebook directory

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open Settings; Tap on the 'Notebook' / root folder entry; Tap on the 'Save' button
- Remaining steps: Select the 'Change' option; Enter the new directory path; Confirm the new directory path
- Completion ratio: 0.50
- Credited from later features: G001
- Actions taken: 12
  - act: CustomTouchEvent(state=0d08fd2acd79b218102393690653ba15, view=14829e2e94031d5f34f96f1f943a2578(MainActivity/FrameLayout-)) (heuristic)
  - act: CustomTouchEvent(state=47d2090818fde8df2831424fe4bcef8a, view=b8b45b32366e7f41fcd4527438c0af22(MainActivity/LinearLayout-)) (nav)
  - act: CustomTouchEvent(state=1409a4975334be0addbb1df14fcfbf32, view=116397ad79d4405dba16e3988ff65937(DocumentActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=e1b8dd09e0ce27e87863f46479f4946e, view=672314a723fa2b7ea023f63ff76e97f3(DocumentActivity/TextView-File Setti)) (nav)
  - act: CustomTouchEvent(state=8f26b3bda107783586ed639eac7ac574, view=02f9628d3bdbe72728f00d36bc481eb7(DocumentActivity/TextView-File Setti)) (nav)
  - act: CustomTouchEvent(state=8f26b3bda107783586ed639eac7ac574, view=02f9628d3bdbe72728f00d36bc481eb7(DocumentActivity/TextView-File Setti)) (nav)
  - act: CustomTouchEvent(state=8f26b3bda107783586ed639eac7ac574, view=29cb9d8624e4e960bec3313a3b30f720(DocumentActivity/CheckBox-)) (afford_search)
  - act: CustomTouchEvent(state=1409a4975334be0addbb1df14fcfbf32, view=116397ad79d4405dba16e3988ff65937(DocumentActivity/ImageView-)) (afford_search)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
