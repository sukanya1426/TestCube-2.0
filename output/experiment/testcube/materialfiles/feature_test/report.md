# Feature test report: Material Files

- Started: 2026-09-25 01:43:57
- Finished: 2026-09-25 01:46:35
- Features: 14
- Covered: 0
- Partial: 0
- Dropped (blocked / stuck): 2
- Not present in the app: 0
- Weighted coverage: 0% (mean completion ratio; the headline number)
- Coverage: 0% (features with every guide step matched)
- Stop reason: restart_loop
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 1
- Never attempted: 13
- Blocked then recovered on retry: 0
- Blocked still: 0

## Guide vs README-extracted

- Guide features: 14
- README-extracted features: 3
- In both: 0
- Guide-only: 14
- README-only: 3
  - guide-only: G001 Browse local storage
  - guide-only: G002 Copy files
  - guide-only: G003 Delete items
  - guide-only: G004 Sort the file list
  - guide-only: G005 Show
  - guide-only: G006 Create an archive
  - guide-only: G007 Copy the path of
  - guide-only: G008 View an image
  - guide-only: G009 Bookmark a directory
  - guide-only: G010 Connect
  - guide-only: G011 Connect
  - guide-only: G012 Configure the FTP server
  - README-only: F001 Complete first-run setup
  - README-only: F002 Search
  - README-only: F003 Change app settings

## Text-field resolution

- Filled via credential.txt: 0
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 0% (0/14) — live journal self-report (covered / extracted features).
- Offline coverage: 0% (0 covered / 42; 0 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 0% (mean completion ratio).

## Findings

### G001 Browse local storage

- Status: **dropped**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Remaining steps: Open the app; Tap the hamburger icon to open the navigation drawer; Select 'Browse' from the navigation drawer; Select 'Local' from the navigation drawer; Select 'Storage' from the navigation drawer
- Completion ratio: 0.00
- Actions taken: 6
  - act: CustomTouchEvent(state=b8779817c6843ac06e121dd55959391c, view=90e000b992fa2cbe1fcbe7914822932e(FileListActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=6fb9964ba7b151c9953e45f27d1f59c2, view=c4f394b95c30e536f4a34343146d81ed(SpaActivity/TextView-Allow this)) (heuristic)
  - act: CustomTouchEvent(state=6fb9964ba7b151c9953e45f27d1f59c2, view=f645993944622276fec39ccf90b3005f(SpaActivity/View-)) (heuristic)
  - act: CustomTouchEvent(state=9de87d11a2efe4600a9d47d4db5725ca, view=85f6502dd64da8f20b0cfcfac384e43d(SpaActivity/View-)) (heuristic)
  - act: CustomTouchEvent(state=6fb9964ba7b151c9953e45f27d1f59c2, view=f645993944622276fec39ccf90b3005f(SpaActivity/View-)) (heuristic)
  - act: CustomTouchEvent(state=9de87d11a2efe4600a9d47d4db5725ca, view=e536926440a2b96e7035d03c513fb032(SpaActivity/TextView-Allow acce)) (rule)

### G002 Copy files

- Status: **dropped**
- Reason: Could not restart the app for this feature.
- Feature source: guide
- Remaining steps: Long-press the item(s) you want to copy; Tap the copy icon in the contextual toolbar; Select the destination folder where you want to copy the files; Tap the paste icon in the contextual toolbar to complete the copy operation
- Completion ratio: 0.00

### G003 Delete items

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Material Files app; Navigate to the folder containing the items you want to delete; Long-press the item(s) you want to delete; Tap the delete icon; Confirm the deletion if prompted
- Completion ratio: 0.00

### G004 Sort the file list

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap the overflow menu (three dots); Select 'Sort by'; Select 'Directories first'; Tap the overflow menu (three dots); Select 'Sort by'; Select 'Name'
- Completion ratio: 0.00

### G005 Show

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap the overflow menu; Scroll to the 'Show' option; Select 'Show'
- Completion ratio: 0.00

### G006 Create an archive

- Status: **pending**
- Feature source: guide
- Remaining steps: Long-press the item(s) to include; Tap the overflow menu; Select 'Create'; Select 'Archive'; Tap 'Create Archive'
- Completion ratio: 0.00

### G007 Copy the path of

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Material Files app; Navigate to the folder containing the file you want to copy the path of; Long-press the item; Tap the overflow menu; Select 'Copy Path'; The app will display the path of the selected file
- Completion ratio: 0.00

### G008 View an image

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap an image file; The image viewer opens; Select the image; The image viewer displays the image
- Completion ratio: 0.00

### G009 Bookmark a directory

- Status: **pending**
- Feature source: guide
- Remaining steps: Navigate to the folder; Tap the overflow menu; Select 'Bookmark'; Confirm the bookmark action
- Completion ratio: 0.00

### G010 Connect

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap the navigation drawer icon in the top left corner of the Material Files app.; Select 'Add server' from the navigation drawer menu.; Enter the server details and tap 'Connect' to establish the connection.
- Completion ratio: 0.00

### G011 Connect

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the drawer; Tap 'Add server'; Select 'WebDAV'; Enter server details; Tap 'Connect'
- Completion ratio: 0.00

### G012 Configure the FTP server

- Status: **pending**
- Feature source: guide
- Remaining steps: Open Settings; Tap the FTP server section; Enter FTP server details; Tap the 'Save' button; Verify the FTP server configuration
- Completion ratio: 0.00

### G013 Change the theme

- Status: **pending**
- Feature source: guide
- Remaining steps: Open Settings; Tap 'Appearance'; Select 'Theme'; Tap 'Dark Theme'; Tap 'Done'
- Completion ratio: 0.00

### G014 Configure the standard directories

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Settings' icon; Scroll down to find and select 'Standard directories'; Tap on 'Standard directories' to open the configuration screen; Enter the desired path for the standard directories; Tap on 'Save' to confirm the changes
- Completion ratio: 0.00

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
