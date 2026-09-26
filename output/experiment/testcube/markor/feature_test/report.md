# Feature test report: Markor

- Started: 2026-09-24 22:51:11
- Finished: 2026-09-24 22:58:09
- Features: 14
- Covered: 0
- Partial: 2
- Dropped (blocked / stuck): 1
- Not present in the app: 0
- Weighted coverage: 5% (mean completion ratio; the headline number)
- Coverage: 0% (features with every guide step matched)
- Stop reason: restart_loop
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 2
- Never attempted: 12
- Blocked then recovered on retry: 0
- Blocked still: 0

## Guide vs README-extracted

- Guide features: 14
- README-extracted features: 4
- In both: 0
- Guide-only: 14
- README-only: 4
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
  - README-only: F001 Complete first-run setup
  - README-only: F002 Search
  - README-only: F003 Import or export data
  - README-only: F004 Change app settings

## Text-field resolution

- Filled via credential.txt: 0
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 0% (0/14) — live journal self-report (covered / extracted features).
- Offline coverage: 0% (0 covered / 46; 1 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 0% (mean completion ratio).

## Findings

### G001 Browse the notebook folder

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the app; Tap on the 'Files' tab
- Remaining steps: Select the 'Browse' option; Select the 'notebook' folder; Select the 'folder' option
- Completion ratio: 0.40
- Credited from later features: G002
- Actions taken: 12
  - act: CustomTouchEvent(state=c5a3411e94d5b81924d5a7b23537f604, view=02b1944a6ed43f71450736cac5b0bcd3(IntroActivity/Button-DONE)) (rule)
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=9e4029fc05acebd1bbe1e21767619dbf(StoragePermissionActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=9e4029fc05acebd1bbe1e21767619dbf(StoragePermissionActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=f20577cd148b856cb5d4408db7195e2c(StoragePermissionActivity/View-)) (llm)
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=bde25c2ada76bb47743cf500dd884367(StoragePermissionActivity/Button-EXIT)) (llm)
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=f20577cd148b856cb5d4408db7195e2c(StoragePermissionActivity/View-)) (llm)
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=bde25c2ada76bb47743cf500dd884367(StoragePermissionActivity/Button-EXIT)) (llm)
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=7fd7d5a9c7b89971d15935f536b0caf2(StoragePermissionActivity/TextView-Storage pe)) (llm)

### G002 Create a folder

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Files tab; Tap the '+' button
- Remaining steps: Select 'Create'; Select 'Folder'; Enter the folder name; Tap 'Create'
- Completion ratio: 0.33
- Credited from later features: G001
- Actions taken: 9
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=bde25c2ada76bb47743cf500dd884367(StoragePermissionActivity/Button-EXIT)) (rule)
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=bde25c2ada76bb47743cf500dd884367(StoragePermissionActivity/Button-EXIT)) (llm)
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=bde25c2ada76bb47743cf500dd884367(StoragePermissionActivity/Button-EXIT)) (llm)
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=bde25c2ada76bb47743cf500dd884367(StoragePermissionActivity/Button-EXIT)) (llm)
  - act: CustomTouchEvent(state=b132829a1d080b8cfc5587906635feec, view=9e4029fc05acebd1bbe1e21767619dbf(StoragePermissionActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=8c223f2b0df51825229aee69d3d4041d, view=c4f394b95c30e536f4a34343146d81ed(SpaActivity/TextView-Allow this)) (heuristic)
  - act: CustomTouchEvent(state=8c223f2b0df51825229aee69d3d4041d, view=f645993944622276fec39ccf90b3005f(SpaActivity/View-)) (heuristic)
  - act: CustomTouchEvent(state=e3604b710debb0b1885eaff8f574a7fe, view=e536926440a2b96e7035d03c513fb032(SpaActivity/TextView-Allow acce)) (rule)

### G003 Apply Markdown formatting

- Status: **dropped**
- Reason: Could not restart the app for this feature.
- Feature source: guide
- Remaining steps: Open a Markdown document; Select the text you want to format; Tap the 'Apply Markdown formatting' option in the action toolbar; Choose the desired Markdown formatting from the dropdown menu; The document will now display the formatted text
- Completion ratio: 0.00

### G004 Insert an image

- Status: **pending**
- Feature source: guide
- Remaining steps: Open a document; Tap the image/attachment action in the action bar; Select 'pick from gallery'; Choose an image from the gallery; Tap 'Insert' to add the image to the document
- Completion ratio: 0.00

### G005 Insert a table

- Status: **pending**
- Feature source: guide
- Remaining steps: Open a Markdown document; Tap the table action in the action bar; Select the table option from the dropdown menu; Enter the number of rows and columns for the table; Tap the 'Insert' button to confirm the table insertion
- Completion ratio: 0.00

### G006 Search across all files

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Files tab; Tap the search icon in the toolbar; Enter 'search' in the search bar; Tap the 'across' button; Tap the 'all' button; Tap the search result to view the file content
- Completion ratio: 0.00

### G007 Manage a todo.txt file

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Markor app; Tap on the 'todo' option in the navigation drawer; Enter the path to the todo.txt file or tap 'Create' to create a new file; Tap on the 'todo.txt' action bar to view and manage the todo.txt file; Perform the necessary operations to manage the todo.txt file
- Completion ratio: 0.00

### G008 Preview a CSV file

- Status: **pending**
- Feature source: guide
- Remaining steps: Open a .csv file; tap the preview/eye icon
- Completion ratio: 0.00

### G009 Share the document

- Status: **pending**
- Feature source: guide
- Remaining steps: Open a document; Tap the overflow menu; Select 'Share' from the overflow menu; Enter the desired sharing method (e.g., 'Email', 'Message', 'Social Media'); Tap the 'Send' button to share the document
- Completion ratio: 0.00

### G010 Delete files

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Files' tab; Long-press the items to select them; Select the 'delete' option; Confirm the deletion; The app state changes to reflect the deleted files
- Completion ratio: 0.00

### G011 Sort the file list

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Files tab; Tap the sort icon (or the overflow menu); Select 'folders first'; Select 'sort'; Select 'file'
- Completion ratio: 0.00

### G012 View recent

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap the 'Files' tab; Select 'Go to' menu; Select 'recent documents'
- Completion ratio: 0.00

### G013 Open a file

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap the navigation drawer icon to open the navigation drawer; Select the 'Files' tab from the navigation drawer; Tap on the file you want to open
- Completion ratio: 0.00

### G014 Change the notebook directory

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Settings' option in the main menu.; Scroll down to find and select the 'Notebook' / root folder entry.; Tap on the 'Notebook' / root folder entry to open the directory settings.; Tap on the 'Change' option to modify the notebook directory.; Enter the new directory path in the input field.; Tap the 'Save' button to apply the changes.
- Completion ratio: 0.00

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
