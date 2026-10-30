# Feature test report: Aegis Authenticator

- Started: 2026-10-12 16:34:43
- Finished: 2026-10-12 16:42:22
- Features: 14
- Covered: 0
- Partial: 6
- Dropped (blocked / stuck): 5
- Not present in the app: 0
- Weighted coverage: 13% (mean completion ratio; the headline number)
- Coverage: 0% (features with every guide step matched)
- Stop reason: restart_loop
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 10
- Never attempted: 4
- Blocked then recovered on retry: 0
- Blocked still: 1

## Guide vs README-extracted

- Guide features: 14
- README-extracted features: 8
- In both: 1
- Guide-only: 13
- README-only: 7
  - guide-only: G001 Create
  - guide-only: G002 Unlock the vault
  - guide-only: G003 Add an entry
  - guide-only: G004 Edit an entry
  - guide-only: G005 Import an icon pack
  - guide-only: G006 Reveal a hidden code
  - guide-only: G008 Reorder entries manually
  - guide-only: G009 Assign an entry
  - guide-only: G010 Rename
  - guide-only: G011 Select
  - guide-only: G012 Export the vault
  - guide-only: G013 Import entries
  - README-only: F001 Close or skip the tutorial
  - README-only: F002 Leave any first-run analytics or settings screen
  - README-only: F003 Tap Create Database or Open Database if shown
  - README-only: F004 Enter a file name if asked and confirm Save
  - README-only: F005 Reach the home or main screen
  - README-only: F007 Import or export data
  - README-only: F008 Change app settings

## Text-field resolution

- Filled via credential.txt: 0
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 0% (0/14) — live journal self-report (covered / extracted features).
- Offline coverage: 0% (0 covered / 40; 3 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 2% (mean completion ratio).

## Findings

### G001 Create

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Install and open the app
- Remaining steps: Tap through the welcome screens; Select 'Create' from the navigation hints; Enter a name for the vault; Tap 'Encrypt' to secure the vault; Tap 'Done' to finalize vault creation
- Completion ratio: 0.17
- Credited from later features: G005
- Actions taken: 16
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=83ac976539dbeb7dce82a0ba1527b518(IntroActivity/Button-Import Aeg)) (llm)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=83ac976539dbeb7dce82a0ba1527b518(IntroActivity/Button-Import Aeg)) (nav)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=5137e7fa52c6a1266c62228ccf950a6e(IntroActivity/Button-)) (nav)
  - act: ScrollEvent(state=e74b49bb238a63caaee2d3ad4737b881, view=3596372bf56a107fa6f4cc86f8ef84f0(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=e74b49bb238a63caaee2d3ad4737b881, view=3596372bf56a107fa6f4cc86f8ef84f0(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=e74b49bb238a63caaee2d3ad4737b881, view=3596372bf56a107fa6f4cc86f8ef84f0(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=e74b49bb238a63caaee2d3ad4737b881, view=3596372bf56a107fa6f4cc86f8ef84f0(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: CustomTouchEvent(state=e74b49bb238a63caaee2d3ad4737b881, view=57789aa8569fc95345f56e7ced7ae485(IntroActivity/TextView-Aegis is a)) (rule)

### G002 Unlock the vault

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on 'Settings' in the navigation drawer; Select 'Security' from the settings menu
- Remaining steps: Enter the correct password or biometric to unlock the vault
- Completion ratio: 0.67
- Credited from later features: G005
- Actions taken: 12
  - act: CustomTouchEvent(state=e74b49bb238a63caaee2d3ad4737b881, view=5137e7fa52c6a1266c62228ccf950a6e(IntroActivity/Button-)) (heuristic)
  - act: ScrollEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: CustomTouchEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=2d015328b167f450dea493e57a8d1fdd(IntroActivity/View-)) (llm)
  - act: CustomTouchEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=2d015328b167f450dea493e57a8d1fdd(IntroActivity/View-)) (llm)
  - act: CustomTouchEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=719dc762ca17f4be0a22646765d5159f(IntroActivity/TextView-Warning: I)) (rule)

### G003 Add an entry

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the '+' button
- Remaining steps: Tap 'Scan an image'/Scan image from gallery'; Select the image to scan; Tap 'Add' to confirm the entry; Enter the necessary details for the entry; Tap 'Save' to add the entry
- Completion ratio: 0.17
- Credited from later features: G001
- Actions taken: 7
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=13d6575d07268296a7e155b264cfe72f(IntroActivity/TextView-Aegis is a)) (rule)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=13d6575d07268296a7e155b264cfe72f(IntroActivity/TextView-Aegis is a)) (rule)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=cf580c6cad60354bc9387fc9fc17e2cb(IntroActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=cf580c6cad60354bc9387fc9fc17e2cb(IntroActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=2d015328b167f450dea493e57a8d1fdd(IntroActivity/View-)) (llm)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=2d015328b167f450dea493e57a8d1fdd(IntroActivity/View-)) (rule)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=b88212f30494f2dbe103a308f389f102(IntroActivity/TextView-Want to im)) (afford_search)

### G004 Edit an entry

- Status: **dropped**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Remaining steps: Tap the entry in the list (or long-press it); Tap the edit action; Enter the new information for the entry; Tap the save or update button; Verify the updated entry in the list
- Completion ratio: 0.00
- Actions taken: 8
  - act: LongTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=5137e7fa52c6a1266c62228ccf950a6e(IntroActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=e74b49bb238a63caaee2d3ad4737b881, view=5137e7fa52c6a1266c62228ccf950a6e(IntroActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=06ad702751d733bb1db8d54e9bdf524b(IntroActivity/EditText-Please ent)) (heuristic)
  - act: LongTouchEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=06ad702751d733bb1db8d54e9bdf524b(IntroActivity/EditText-Please ent)) (heuristic)
  - act: LongTouchEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=719dc762ca17f4be0a22646765d5159f(IntroActivity/TextView-Warning: I)) (heuristic)
  - act: LongTouchEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=5137e7fa52c6a1266c62228ccf950a6e(IntroActivity/Button-)) (heuristic)
  - act: LongTouchEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=68c4f462a2739d86d4b5db06712796ec(IntroActivity/EditText-Please con)) (rule)
  - act: CustomTouchEvent(state=d17c4ee5ac2414e13c9ad38af8c757c0, view=719dc762ca17f4be0a22646765d5159f(IntroActivity/TextView-Warning: I)) (rule)

### G005 Import an icon pack

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open Settings; Tap 'Import'
- Remaining steps: Scroll to 'Icon packs'; Tap 'Icon packs'; Select 'Import icon pack'; Enter the path to the icon pack
- Completion ratio: 0.33
- Credited from later features: G001
- Actions taken: 9
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=b88212f30494f2dbe103a308f389f102(IntroActivity/TextView-Want to im)) (heuristic)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=b88212f30494f2dbe103a308f389f102(IntroActivity/TextView-Want to im)) (heuristic)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=b88212f30494f2dbe103a308f389f102(IntroActivity/TextView-Want to im)) (afford_search)
  - act: ScrollEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=2d015328b167f450dea493e57a8d1fdd(IntroActivity/View-)) (llm)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=2d015328b167f450dea493e57a8d1fdd(IntroActivity/View-)) (llm)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=2d015328b167f450dea493e57a8d1fdd(IntroActivity/View-)) (llm)
  - act: CustomTouchEvent(state=37ae339380914fd06c4e21a0dd48f22d, view=83ac976539dbeb7dce82a0ba1527b518(IntroActivity/Button-Import Aeg)) (rule)

### G006 Reveal a hidden code

- Status: **partial**
- Reason: Could not restart the app for this feature.
- Feature source: guide
- Completed steps: Tap on the 'Reveal a hidden code' option in the settings menu.
- Remaining steps: Select the entry in the list that you want to reveal.; Tap the 'Tap to reveal' option next to the entry.; The hidden code will be displayed in the app state.
- Completion ratio: 0.25
- Credited from later features: G005

### G007 Search entries

- Status: **dropped**
- Reason: App would not stay in the foreground.
- Feature source: guide
- Remaining steps: Tap the search icon in the toolbar; Type part of the issuer or account name; Press the Enter key to execute the search; Review the search results; Select an entry from the search results; Tap the back button to return to the main screen
- Completion ratio: 0.00

### G008 Reorder entries manually

- Status: **dropped**
- Reason: App would not stay in the foreground.
- Feature source: guide
- Remaining steps: Tap on the 'Entries' section in the navigation drawer.; Select 'Sort' from the menu.; Choose 'Custom' from the sort options.; Long-press an entry to start reordering.; Drag the entry to a new position in the list.
- Completion ratio: 0.00

### G009 Assign an entry

- Status: **partial**
- Reason: App would not stay in the foreground.
- Feature source: guide
- Completed steps: Open the entry editor
- Remaining steps: Tap the group selector; Select the group to assign the entry to; Tap the 'Assign' button to confirm the group assignment
- Completion ratio: 0.25
- Credited from later features: G005

### G010 Rename

- Status: **dropped**
- Reason: App would not stay in the foreground.
- Feature source: guide
- Remaining steps: Tap on the overflow menu; Scroll down to find the 'Manage groups' option; Tap on 'Manage groups'; Tap on the group you want to rename; Enter the new name for the group; Tap on the 'Rename' button to confirm the change
- Completion ratio: 0.00

### G011 Select

- Status: **partial**
- Reason: Run ended before the feature completed.
- Feature source: guide
- Completed steps: Open the Aegis Authenticator app
- Remaining steps: Navigate to the entry list; Long-press the first entry; Tap the further entries to add them
- Completion ratio: 0.25
- Credited from later features: G005

### G012 Export the vault

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on 'Settings' in the main menu.; Scroll down to find the 'Import and export' option.; Select 'Export the vault' from the 'Import and export' menu.; Follow the prompts to confirm the export of the vault.; Wait for the export process to complete and confirm the successful export.
- Completion ratio: 0.00

### G013 Import entries

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap the "+" button; tap "Scan a QR code"
- Completion ratio: 0.00

### G014 Add a second unlock

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on 'Settings'; Select 'Security'; Select 'Add second unlock'; Enter a name for the second unlock; Confirm the second unlock
- Completion ratio: 0.00

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
