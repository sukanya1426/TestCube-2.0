# Feature test report: Amaze File Manager

- Started: 2026-09-25 01:03:47
- Finished: 2026-09-25 01:41:05
- Features: 14
- Covered: 6
- Partial: 8
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 68% (mean completion ratio; the headline number)
- Coverage: 43% (features with every guide step matched)
- Stop reason: all_features_done
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 14
- Never attempted: 0
- Blocked then recovered on retry: 1
- Blocked still: 0

## Guide vs README-extracted

- Guide features: 14
- README-extracted features: 7
- In both: 1
- Guide-only: 13
- README-only: 6
  - guide-only: G001 Browse internal storage
  - guide-only: G002 Copy files
  - guide-only: G003 Delete files
  - guide-only: G005 Show
  - guide-only: G006 View file properties
  - guide-only: G007 Extract an archive
  - guide-only: G008 Decrypt a file
  - guide-only: G009 Edit
  - guide-only: G010 Open the app manager
  - guide-only: G011 Start the built-in FTP
  - guide-only: G012 Connect over SFTP/SSH
  - guide-only: G013 View recent files
  - README-only: F001 Close or skip the tutorial
  - README-only: F002 Leave any first-run analytics or settings screen
  - README-only: F003 Tap Create Database or Open Database if shown
  - README-only: F004 Enter a file name if asked and confirm Save
  - README-only: F005 Reach the home or main screen
  - README-only: F007 Change app settings

## Text-field resolution

- Filled via credential.txt: 1
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 43% (6/14) — live journal self-report (covered / extracted features).
- Offline coverage: 0% (0 covered / 46; 4 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 3% (mean completion ratio).

## Findings

### G001 Browse internal storage

- Status: **covered**
- Reason: Covered by shared-flow reuse of C005.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Tap on the hamburger icon to open the navigation drawer; Select 'Browse internal storage' from the navigation drawer; Tap on the 'Internal' option to proceed; Tap on the 'Storage' option to view the internal storage; Select the desired folder or file to browse
- Completion ratio: 1.00
- Actions taken: 12
  - act: CustomTouchEvent(state=94f9d35a78ccb0f0e1ced765a2a359ca, view=36cfa181152ca2154847775a5521915e(MainActivity/Button-STORAGE)) (nav)
  - act: CustomTouchEvent(state=631d592916e49847558388d3137679c7, view=36cfa181152ca2154847775a5521915e(MainActivity/Button-STORAGE)) (nav)
  - act: CustomTouchEvent(state=94f9d35a78ccb0f0e1ced765a2a359ca, view=36cfa181152ca2154847775a5521915e(MainActivity/Button-STORAGE)) (nav)
  - act: CustomTouchEvent(state=94f9d35a78ccb0f0e1ced765a2a359ca, view=68f580ac62bb490a55df52c0529eb2c5(MainActivity/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=cc8f815ac46d8b61b81e978d57a8ba10, view=bb0c1abd67c596897d61ac29ce07762e(MainActivity/TextView-Add to Boo)) (rule)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=d587dc1dba2812a31709ae99de8b62cd(MainActivity/TextView-GRANT)) (llm)

### G002 Copy files

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Amaze File Manager app; Navigate to the folder containing the files you want to copy; Select the destination folder where you want to copy the files; Tap the 'Copy' option in the contextual menu; Long-press the item(s) to select them
- Remaining steps: Tap the copy icon in the contextual toolbar
- Completion ratio: 0.83
- Credited from later features: G003, G005, G006
- Actions taken: 18
  - act: LongTouchEvent(state=f29f94935c8a045be93b0c36b5022c11, view=4ef3ee600f8a8ea799a6fbe84f1839b6(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=1b480031391fe79a8f301b545daa8333, view=d67ebb6714e1f9e73c7887fffac9245a(MainActivity/TextView-Copy: 1 fo)) (rule)
  - act: CustomTouchEvent(state=1b480031391fe79a8f301b545daa8333, view=ce98d57f79c1c2b076ddcfb6141ba19c(MainActivity/TextView-1)) (rule)
  - act: LongTouchEvent(state=6c715418f2f74ecd335fb1d8fed7438e, view=50e4b5b5266dec312e87955234db9de8(MainActivity/TextView-Select sim)) (heuristic)
  - act: LongTouchEvent(state=1b480031391fe79a8f301b545daa8333, view=d9c1b797d9a13de6eb79c96bfbdd2f5b(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=f29f94935c8a045be93b0c36b5022c11, view=cacb05e9418ec61b441a5cbd82c9a394(MainActivity/LinearLayout-)) (afford_search)
  - act: CustomTouchEvent(state=e25a9d0110e85b2f8840d405feb708ff, view=d67ebb6714e1f9e73c7887fffac9245a(MainActivity/TextView-Copy: 1 fo)) (heuristic)
  - act: CustomTouchEvent(state=e25a9d0110e85b2f8840d405feb708ff, view=f9b9d652a7bf7d9907fa29ff7da7bf1b(MainActivity/TextView-13 folders)) (rule)

### G003 Delete files

- Status: **partial**
- Reason: Stuck on the same screen.
- Feature source: guide
- Completed steps: Open the Amaze File Manager app; Navigate to the folder containing the files you want to delete; Long-press the item(s) you want to delete
- Remaining steps: Tap the delete (bin) icon; Confirm the deletion by tapping 'Delete'
- Completion ratio: 0.60
- Credited from later features: G006
- Actions taken: 12
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (llm)
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (llm)
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (nav)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (nav)

### G004 Run a deep search

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the search icon; Enter the query text; Press the search button
- Completion ratio: 1.00
- Actions taken: 11
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=d587dc1dba2812a31709ae99de8b62cd(MainActivity/TextView-GRANT)) (llm)
  - act: CustomTouchEvent(state=80a9b0ab88b639cc7fbbd84a89c4f4cd, view=97ae4cf458ac3a810c02db7a22761792(MainActivity/Button-)) (rule)
  - act: (screen already shows this destination) (rule)
  - act: CustomSetTextEvent(state=356bdf1993df271b89d5748ae3e86bb5, view=b91c8dbbacf4c0f0210263729f7959e3(MainActivity/EditText-Type to se), text=test) (mandatory_fill)
  - act: CustomTouchEvent(state=d227a4741a88f758ef621a958b44a23b, view=26f9c764c00f2f02c1ac7c0ec18d64d5(MainActivity/Button-Try Indexe)) (heuristic)

### G005 Show

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the overflow menu; toggle "Show hidden files"
- Completion ratio: 1.00
- Actions taken: 5
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=d587dc1dba2812a31709ae99de8b62cd(MainActivity/TextView-GRANT)) (llm)
  - act: CustomTouchEvent(state=80a9b0ab88b639cc7fbbd84a89c4f4cd, view=cacb05e9418ec61b441a5cbd82c9a394(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=7dd612af591dd5be774072d13f734433, view=f9b9d652a7bf7d9907fa29ff7da7bf1b(MainActivity/TextView-13 folders)) (heuristic)

### G006 View file properties

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Long-press the file; Tap the overflow menu; Select 'Properties' from the overflow menu
- Remaining steps: Review the file properties in the dialog; Close the properties dialog
- Completion ratio: 0.60
- Credited from later features: G005
- Actions taken: 8
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)

### G007 Extract an archive

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap an archive file (ZIP, RAR, TAR, TAR.GZ, 7Z); Select the 'Extract' option from the menu
- Remaining steps: The archive viewer opens; Choose the desired extraction location; Confirm the extraction process
- Completion ratio: 0.40
- Credited from later features: G005
- Actions taken: 8
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)

### G008 Decrypt a file

- Status: **covered**
- Reason: Covered by shared-flow reuse of C005.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Tap the encrypted (.aze) file; Enter the password or authenticate with the fingerprint; Tap the 'Decrypt' button; Wait for the decryption process to complete; Verify the decrypted file by opening it
- Completion ratio: 1.00
- Actions taken: 7
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (nav)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (nav)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (nav)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (nav)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=d587dc1dba2812a31709ae99de8b62cd(MainActivity/TextView-GRANT)) (llm)

### G009 Edit

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the 'edit' option from the dropdown menu.; Long-press the bookmark to edit it.
- Remaining steps: Tap the drawer icon in the top left corner of the screen.; Enter the desired changes to the bookmark.; Tap the checkmark or save icon to confirm the changes.
- Completion ratio: 0.40
- Credited from later features: G005, G006
- Actions taken: 9
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: LongTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (heuristic)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=d587dc1dba2812a31709ae99de8b62cd(MainActivity/TextView-GRANT)) (llm)
  - act: LongTouchEvent(state=80a9b0ab88b639cc7fbbd84a89c4f4cd, view=4ef3ee600f8a8ea799a6fbe84f1839b6(MainActivity/ImageView-)) (heuristic)
  - act: LongTouchEvent(state=47fe2bacd730b81a1badf7243fcab769, view=d9c1b797d9a13de6eb79c96bfbdd2f5b(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=80a9b0ab88b639cc7fbbd84a89c4f4cd, view=e67f62bd459061deaf0c875089c6f340(MainActivity/TextView-Audiobooks)) (rule)

### G010 Open the app manager

- Status: **covered**
- Reason: Covered by shared-flow reuse of C008.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Tap the navigation drawer icon to open the navigation drawer; Scroll to the 'Apps' section in the navigation drawer; Tap 'Apps' to open the app manager
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (nav)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (nav)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (nav)

### G011 Start the built-in FTP

- Status: **covered**
- Reason: Covered by shared-flow reuse of C004.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the navigation drawer; Tap on 'FTP' in the navigation drawer; Tap 'Start' to begin the built-in FTP
- Completion ratio: 1.00
- Actions taken: 5
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)

### G012 Connect over SFTP/SSH

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the drawer
- Remaining steps: Tap the '+' beside the network section; Select 'SCP/SFTP connection'; Enter the SFTP/SSH server address; Enter the username; Enter the password
- Completion ratio: 0.17
- Credited from later features: G002
- Actions taken: 7
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=bf364e9e02ac00b098a77b359d1562f6(MainActivity/TextView-CANCEL)) (llm)
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=6777e80a63ef098ef8ee723768003574(MainActivity/TextView-Since Andr)) (llm)

### G013 View recent files

- Status: **partial**
- Reason: Already on the home screen.
- Feature source: guide
- Completed steps: Tap 'Recent files' on the home screen
- Remaining steps: Open the navigation drawer; Select the desired file from the recent files list
- Completion ratio: 0.33
- Actions taken: 1
  - act: (screen already shows this destination) (rule)

### G014 Change the accent

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open Settings
- Remaining steps: Scroll down to find 'Appearance'; Tap 'Appearance'; Tap 'Accent'; Select a new accent color; Tap 'Done'
- Completion ratio: 0.17
- Credited from later features: G002
- Actions taken: 6
  - act: CustomTouchEvent(state=58ff11f37a9cac3066f593473b3f808b, view=d587dc1dba2812a31709ae99de8b62cd(MainActivity/TextView-GRANT)) (llm)
  - act: CustomTouchEvent(state=322082437899eed059aea04305a45969, view=cacb05e9418ec61b441a5cbd82c9a394(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=f0f35e5d5565408fd7f4f647a356057a, view=b452f116e61c5fd5d5bf2b07a427a90f(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=8b8f55ec3be2374ab67bd3c417aa3598, view=082de8b63af70192f2a0627ea527439f(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=322082437899eed059aea04305a45969, view=cacb05e9418ec61b441a5cbd82c9a394(MainActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=f0f35e5d5565408fd7f4f647a356057a, view=b452f116e61c5fd5d5bf2b07a427a90f(MainActivity/LinearLayout-)) (heuristic)

## Shared flows detected

4 reuse(s); 15 action(s) skipped by not re-executing a known terminal flow.

- `G008` reused `C005` (from G005), skipped 4 action(s)
- `G010` reused `C008` (from G008), skipped 3 action(s)
- `G011` reused `C004` (from G004), skipped 3 action(s)
- `G001` reused `C005` (from G005), skipped 5 action(s)

See `session.json` and `log.md` in this folder for the full trace.
