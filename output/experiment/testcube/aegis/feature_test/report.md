# Feature test report: Aegis Authenticator

- Started: 2026-09-25 03:35:29
- Finished: 2026-09-25 03:49:50
- Features: 14
- Covered: 0
- Partial: 6
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 13% (mean completion ratio; the headline number)
- Coverage: 0% (features with every guide step matched)
- Stop reason: restart_loop
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 5
- Never attempted: 9
- Blocked then recovered on retry: 0
- Blocked still: 0

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

- Filled via credential.txt: 8
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 0% (0/14) — live journal self-report (covered / extracted features).
- Offline coverage: 2% (1 covered / 40; 2 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 3% (mean completion ratio).

## Findings

### G001 Create

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Install and open the app
- Remaining steps: Tap through the welcome screens; Select 'Create' from the navigation menu; Enter a name for the vault; Tap 'Encrypt' to secure the vault; Enter a password to encrypt the vault
- Completion ratio: 0.17
- Credited from later features: G005
- Actions taken: 8
  - act: ScrollEvent(state=44fb7984198392ecbe123dc1d95acb34, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=44fb7984198392ecbe123dc1d95acb34, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=44fb7984198392ecbe123dc1d95acb34, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=44fb7984198392ecbe123dc1d95acb34, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: CustomTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=b88212f30494f2dbe103a308f389f102(IntroActivity/TextView-Want to im)) (afford_search)
  - act: CustomTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=83ac976539dbeb7dce82a0ba1527b518(IntroActivity/Button-Import Aeg)) (llm)
  - act: CustomTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=83ac976539dbeb7dce82a0ba1527b518(IntroActivity/Button-Import Aeg)) (nav)
  - act: CustomTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=689dfd14036420ff77e6af19d0ae3c77(IntroActivity/TextView-Welcome)) (rule)

### G002 Unlock the vault

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Settings' icon
- Remaining steps: Select 'Security'; Tap on 'Unlock the vault' option; Enter the required password; Select 'Unlock vault with password' option; Tap on 'Unlock vault with biometrics' option
- Completion ratio: 0.17
- Actions taken: 17
  - act: ScrollEvent(state=c3d2bd3e4df4de975093506555d86ba1, view=3596372bf56a107fa6f4cc86f8ef84f0(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=c3d2bd3e4df4de975093506555d86ba1, view=3596372bf56a107fa6f4cc86f8ef84f0(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=c3d2bd3e4df4de975093506555d86ba1, view=3596372bf56a107fa6f4cc86f8ef84f0(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: CustomTouchEvent(state=c3d2bd3e4df4de975093506555d86ba1, view=e5695bcf4cd2a6e2094dd6dc677a6960(IntroActivity/RadioButton-None)) (llm)
  - act: CustomTouchEvent(state=c3d2bd3e4df4de975093506555d86ba1, view=57789aa8569fc95345f56e7ced7ae485(IntroActivity/TextView-Aegis is a)) (llm)
  - act: CustomTouchEvent(state=c3d2bd3e4df4de975093506555d86ba1, view=57789aa8569fc95345f56e7ced7ae485(IntroActivity/TextView-Aegis is a)) (llm)
  - act: CustomTouchEvent(state=c3d2bd3e4df4de975093506555d86ba1, view=d1edef213a9c2677de4cb0e78d0cc1fe(IntroActivity/TextView-No passwor)) (llm)
  - act: CustomTouchEvent(state=c3d2bd3e4df4de975093506555d86ba1, view=6959e350e2ab61a6af705e3e341e7890(IntroActivity/TextView-Security)) (rule)

### G003 Add an entry

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the '+' button
- Remaining steps: Tap 'Scan an image'/Scan image from gallery'; Select the image to scan; Tap 'Add Entry'; Enter the necessary details for the entry; Tap 'Save'
- Completion ratio: 0.17
- Credited from later features: G001
- Actions taken: 20
  - act: CustomSetTextEvent(state=ba53d20f46f4075f8c342807fa4e54fa, view=b73815771c4c5a5f87759443c44ba2b3(IntroActivity/EditText-TestCube!2), text=TestCube!2026) (rule)
  - act: CustomSetTextEvent(state=ba53d20f46f4075f8c342807fa4e54fa, view=b73815771c4c5a5f87759443c44ba2b3(IntroActivity/EditText-TestCube!2), text=TestCube!2026) (rule)
  - act: CustomSetTextEvent(state=ba53d20f46f4075f8c342807fa4e54fa, view=68c4f462a2739d86d4b5db06712796ec(IntroActivity/EditText-Please con), text=TestCube!2026) (rule)
  - act: ScrollEvent(state=249655217f3df850489e87f2d9e9f349, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=249655217f3df850489e87f2d9e9f349, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=249655217f3df850489e87f2d9e9f349, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: ScrollEvent(state=249655217f3df850489e87f2d9e9f349, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=left) (rule)
  - act: CustomTouchEvent(state=249655217f3df850489e87f2d9e9f349, view=719dc762ca17f4be0a22646765d5159f(IntroActivity/TextView-Warning: I)) (rule)

### G004 Edit an entry

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the save button
- Remaining steps: Tap the entry in the list (or long-press it); Tap the edit action; Enter the new information; Verify the updated entry in the list
- Completion ratio: 0.20
- Credited from later features: G001
- Actions taken: 7
  - act: LongTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=2d015328b167f450dea493e57a8d1fdd(IntroActivity/View-)) (heuristic)
  - act: LongTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=2d015328b167f450dea493e57a8d1fdd(IntroActivity/View-)) (heuristic)
  - act: LongTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=cf580c6cad60354bc9387fc9fc17e2cb(IntroActivity/ImageView-)) (heuristic)
  - act: LongTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=cf580c6cad60354bc9387fc9fc17e2cb(IntroActivity/ImageView-)) (heuristic)
  - act: LongTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=13d6575d07268296a7e155b264cfe72f(IntroActivity/TextView-Aegis is a)) (heuristic)
  - act: LongTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=689dfd14036420ff77e6af19d0ae3c77(IntroActivity/TextView-Welcome)) (rule)
  - act: LongTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=13d6575d07268296a7e155b264cfe72f(IntroActivity/TextView-Aegis is a)) (rule)

### G005 Import an icon pack

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open Settings; Tap on 'Import'; Confirm the import; Scroll down to find 'Icon packs'; Tap on 'Icon packs'; Select a desired icon pack
- Completion ratio: 1.00
- Credited from later features: G001, G002
- Actions taken: 9
  - act: CustomTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=b88212f30494f2dbe103a308f389f102(IntroActivity/TextView-Want to im)) (heuristic)
  - act: CustomTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=b88212f30494f2dbe103a308f389f102(IntroActivity/TextView-Want to im)) (heuristic)
  - act: CustomTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=b88212f30494f2dbe103a308f389f102(IntroActivity/TextView-Want to im)) (afford_search)
  - act: ScrollEvent(state=44fb7984198392ecbe123dc1d95acb34, view=464cf92bd53ed9c58b6d2126b6117fb7(IntroActivity/RecyclerView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=2d015328b167f450dea493e57a8d1fdd(IntroActivity/View-)) (llm)
  - act: CustomTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=b88212f30494f2dbe103a308f389f102(IntroActivity/TextView-Want to im)) (llm)
  - act: CustomTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=2d015328b167f450dea493e57a8d1fdd(IntroActivity/View-)) (llm)
  - act: CustomTouchEvent(state=44fb7984198392ecbe123dc1d95acb34, view=83ac976539dbeb7dce82a0ba1527b518(IntroActivity/Button-Import Aeg)) (rule)

### G006 Reveal a hidden code

- Status: **partial**
- Reason: Could not restart the app for this feature.
- Feature source: guide
- Completed steps: Tap on the 'Reveal a hidden code' option in the settings menu.
- Remaining steps: Select the entry in the list that you want to reveal the hidden code for.; Tap the 'Tap to reveal' option next to the selected entry.; The hidden code will be displayed in the app's interface.
- Completion ratio: 0.25
- Credited from later features: G002

### G007 Search entries

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap the search icon in the toolbar; Type part of the issuer or account name; Press the Enter key to execute the search
- Completion ratio: 0.00

### G008 Reorder entries manually

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Aegis Authenticator app; Navigate to the entries list; Select the 'Sort' option; Choose 'Custom' from the sort options; Long-press an entry to start reordering; Drag the entry to a new position in the list
- Completion ratio: 0.00

### G009 Assign an entry

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the entry editor; Tap the group selector; Select the group to assign the entry to; Tap the 'Assign' button; Confirm the assignment
- Completion ratio: 0.00

### G010 Rename

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the overflow menu; Select 'Manage groups'; Tap on the group you want to rename; Enter the new name for the group; Tap the 'Rename' button to save the changes
- Completion ratio: 0.00

### G011 Select

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Aegis Authenticator app; Navigate to the entry list; Long-press the first entry; Tap the further entries to add them; Verify the app state changes
- Completion ratio: 0.00

### G012 Export the vault

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Settings' option in the main menu.; Scroll down to find the 'Import and export' option and tap on it.; Select 'Export the vault' from the export options.; Wait for the export process to complete and confirm the export.; Check the exported vault file to ensure it is in the desired format.
- Completion ratio: 0.00

### G013 Import entries

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap the "+" button; tap "Scan a QR code"
- Completion ratio: 0.00

### G014 Add a second unlock

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on 'Settings'; Select 'Security'; Select 'Add second unlock'; Enter a name for the second unlock; Confirm the addition of the second unlock
- Completion ratio: 0.00

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
