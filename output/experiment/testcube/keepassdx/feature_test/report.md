# Feature test report: KeePassDX

- Started: 2026-09-25 03:53:37
- Finished: 2026-09-25 04:15:41
- Features: 14
- Covered: 0
- Partial: 3
- Dropped (blocked / stuck): 1
- Not present in the app: 0
- Weighted coverage: 4% (mean completion ratio; the headline number)
- Coverage: 0% (features with every guide step matched)
- Stop reason: restart_loop
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 14
- Never attempted: 0
- Blocked then recovered on retry: 0
- Blocked still: 1

## Guide vs README-extracted

- Guide features: 14
- README-extracted features: 8
- In both: 2
- Guide-only: 12
- README-only: 6
  - guide-only: G002 Unlock a database
  - guide-only: G003 Generate a password
  - guide-only: G004 Download
  - guide-only: G005 Copy a username
  - guide-only: G006 Edit an entry
  - guide-only: G007 Move an entry
  - guide-only: G008 Edit, move
  - guide-only: G010 Use the KeePassDX autofill
  - guide-only: G011 Open a database
  - guide-only: G012 Configure clipboard timeout
  - guide-only: G013 Change the database encryption
  - guide-only: G014 Use entry templates
  - README-only: F001 Close or skip the tutorial
  - README-only: F002 Leave any first-run analytics or settings screen
  - README-only: F004 Enter a file name if asked and confirm Save
  - README-only: F005 Reach the home or main screen
  - README-only: F007 Download for offline use
  - README-only: F008 Change app settings

## Text-field resolution

- Filled via credential.txt: 0
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 0% (0/14) — live journal self-report (covered / extracted features).
- Offline coverage: 0% (0 covered / 47; 2 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 1% (mean completion ratio).

## Findings

### G001 Create a database

- Status: **dropped**
- Reason: Could not restart the app for this feature.
- Feature source: guide
- Remaining steps: Open the app; tap the "+" icon (Create new database)
- Completion ratio: 0.00
- Actions taken: 7
  - act: CustomTouchEvent(state=d13778582cf683060d9c33252d33010b, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)

### G002 Unlock a database

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Unlock' button
- Remaining steps: Select 'Hardware Key' from the unlock options; Enter the hardware key PIN; Confirm the hardware key PIN; Wait for the database to unlock; Verify the database is unlocked and accessible
- Completion ratio: 0.17
- Credited from later features: G014
- Actions taken: 7
  - act: CustomTouchEvent(state=d13778582cf683060d9c33252d33010b, view=010bc58101a4dcdbdb2c40d898466beb(FileDatabaseSelectActivity/View-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)

### G003 Generate a password

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Remaining steps: Open the entry editor; tap the generate (dice/refresh) icon beside the password field
- Completion ratio: 0.00
- Actions taken: 7
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)

### G004 Download

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the attachment name
- Remaining steps: Open the app; Navigate to the entry list; Select the entry; Select the download option; Confirm the download
- Completion ratio: 0.17
- Credited from later features: G014
- Actions taken: 7
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)

### G005 Copy a username

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Remaining steps: Open the entry; Tap the username field; Tap the copy icon beside the username or password field; Select the copied username; Paste the copied username into the clipboard
- Completion ratio: 0.00
- Actions taken: 7
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (rule)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)

### G006 Edit an entry

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Remaining steps: Tap the entry you want to edit.; Tap the edit (pencil) icon next to the entry.; Enter the new information you wish to add or modify in the edit fields.; Tap the save icon to save the changes.; Verify the updated entry by checking the app state.
- Completion ratio: 0.00
- Actions taken: 7
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)

### G007 Move an entry

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Remaining steps: Open the KeePassDX app; Navigate to the database containing the entry you want to move; Locate the entry you want to move and long-press it; Tap the 'Move' action; Select the destination database or folder where you want to move the entry; Confirm the move operation
- Completion ratio: 0.00
- Actions taken: 7
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)

### G008 Edit, move

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Remaining steps: Long-press the group; tap Edit to rename it or change its icon and notes, tap the move action to relocate it, or tap Delete and confirm
- Completion ratio: 0.00
- Actions taken: 7
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (heuristic)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: LongTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)

### G009 Search the database

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Remaining steps: Tap the 'Open the unlocked database' option in the main menu.; Enter the search term in the search field.; Tap the search icon in the toolbar to execute the search.; Review the search results to find the desired entry.
- Completion ratio: 0.00
- Actions taken: 7
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)

### G010 Use the KeePassDX autofill

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Remaining steps: Tap on the 'Settings' icon in the app drawer; Scroll down to find 'Passwords and accounts'; Tap on 'Passwords and accounts'; Select 'Autofill service'; Ensure 'Autofill service' is enabled
- Completion ratio: 0.00
- Actions taken: 7
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (rule)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (rule)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (rule)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (rule)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (rule)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (rule)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (rule)

### G011 Open a database

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Remaining steps: Tap on the 'Open an existing database' option; Enter the password for the database; Select the 'Unlock' option; Tap on the 'Read-only' toggle; Unlock the database; Verify the database is open and in read-only mode
- Completion ratio: 0.00
- Actions taken: 7
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)

### G012 Configure clipboard timeout

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap the 'Save' button to apply the changes.
- Remaining steps: Tap on the 'Settings' option in the main menu.; Scroll down and select the 'Security' section.; Tap on 'Clipboard' settings.; Scroll down and select 'Clipboard Timeout'.; Enter the desired timeout duration for the clipboard.
- Completion ratio: 0.17
- Credited from later features: G014
- Actions taken: 6
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, x=540, y=1728) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, x=540, y=1728) (llm)

### G013 Change the database encryption

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Remaining steps: Tap on the 'Settings' icon in the navigation bar.; Select 'Database' from the settings menu.; Select 'Encryption' from the database settings.; Enter the current encryption password if prompted.; Select the option to change the encryption method.; Choose a new encryption method and confirm the change.
- Completion ratio: 0.00
- Actions taken: 7
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)

### G014 Use entry templates

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Remaining steps: Tap on the menu icon in the top left corner of the app.; Select 'Settings' from the menu.; Navigate to the 'General' settings section.; Tap on 'Entry Templates' to open the templates group.; Select the desired template group from the list.; Tap on the '+' button to add a new entry using the selected template.
- Completion ratio: 0.00
- Actions taken: 8
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, x=54, y=1824) (llm)
  - act: KeyEvent(state=422e98814df9bf4ad9217b389957657c, name=BACK) (rule)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, x=54, y=1824) (llm)
  - act: CustomTouchEvent(state=70c8cceb989bfea05fb044ccb49d70c7, view=39e7b74713137d2b8eab25b3dfb3b5ce(PickActivity/Button-SAVE)) (rule)
  - act: CustomTouchEvent(state=9a9780999b5c65a5be5108ab472bce6e, view=6c93380437107f398778748a75a92696(FileDatabaseSelectActivity/Button-Cancel)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, view=a92be79e706578f152afadd53e146a25(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=3cd1a267ff7f6cd3b1472c30deaf459c, x=108, y=1728) (llm)
  - act: CustomTouchEvent(state=74044f668b540e6bb9ce65c992cd26d1, view=b80fb0d996542a29fddbd3edbf6a3208(PickActivity/Button-)) (rule)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
