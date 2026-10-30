# Feature test report: KeePassDX

- Started: 2026-10-12 16:48:29
- Finished: 2026-10-12 17:37:17
- Features: 14
- Covered: 3
- Partial: 3
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 62% (mean completion ratio; the headline number)
- Coverage: 21% (features with every guide step matched)
- Stop reason: restart_loop
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 13
- Never attempted: 1
- Blocked then recovered on retry: 0
- Blocked still: 0

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

- Filled via credential.txt: 10
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 21% (3/14) — live journal self-report (covered / extracted features).
- Offline coverage: 4% (2 covered / 47; 4 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 7% (mean completion ratio).

## Findings

### G001 Create a database

- Status: **partial**
- Reason: App would not stay in the foreground.
- Feature source: guide
- Completed steps: Open the app
- Remaining steps: tap the "+" icon (Create new database)
- Completion ratio: 0.50
- Actions taken: 11
  - act: CustomTouchEvent(state=a105c87febe329c7ab07e049f763aa58, view=8538f57947935e7ae9395e4f6391ff08(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=9f3c38f2e1e63430fa133563b0ba6707, view=c762892e7253388b7ad5f68579af54e1(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=a105c87febe329c7ab07e049f763aa58, view=c7b775f415a91ebe659332e51f845069(FileDatabaseSelectActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=6ae9f44aa199db282495e1464c6e94c6, view=c762892e7253388b7ad5f68579af54e1(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=2ebb106d88d65ef2bf7b5f7748fb683b, view=8538f57947935e7ae9395e4f6391ff08(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=6ae9f44aa199db282495e1464c6e94c6, view=c762892e7253388b7ad5f68579af54e1(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=2ebb106d88d65ef2bf7b5f7748fb683b, view=bb97d88cb5f3840ff64894e709042797(FileDatabaseSelectActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=78336156090439cb41d2e05f9903dfcb, view=e5facd6c8c846aabcaa3e8fb8833eed2(FileDatabaseSelectActivity/TextView-Driver for)) (llm)

### G002 Unlock a database

- Status: **partial**
- Reason: App would not stay in the foreground.
- Feature source: guide
- Completed steps: Tap on the 'Unlock' button; Select 'Hardware Key' from the unlock options; Select the correct hardware key from the list; Tap 'Unlock' to proceed; Confirm the hardware key PIN
- Remaining steps: Enter the hardware key PIN
- Completion ratio: 0.83
- Credited from later features: G001, G004, G009
- Actions taken: 10
  - act: CustomTouchEvent(state=78336156090439cb41d2e05f9903dfcb, view=f3b6298c8f0a2f300c7ca96734eedb6e(FileDatabaseSelectActivity/Switch-Hardware k)) (nav)
  - act: CustomTouchEvent(state=19af741df1de8cd2494828099870c81f, view=b886386010fbb8633954fb7efe711216(FileDatabaseSelectActivity/Switch-Hardware k)) (nav)
  - act: CustomTouchEvent(state=78336156090439cb41d2e05f9903dfcb, view=f2230eee89c2f180d0d130ed53b51c9b(FileDatabaseSelectActivity/Spinner-Yubikey ch)) (rule)
  - act: CustomTouchEvent(state=d30e2455d84c2c602c710b49533a01bc, view=f3b6298c8f0a2f300c7ca96734eedb6e(FileDatabaseSelectActivity/Switch-Hardware k)) (nav)
  - act: CustomTouchEvent(state=19af741df1de8cd2494828099870c81f, view=58665a50c5376e4645516866dfaa084b(FileDatabaseSelectActivity/TextView-Assign a m)) (nav)
  - act: CustomTouchEvent(state=19af741df1de8cd2494828099870c81f, view=c762892e7253388b7ad5f68579af54e1(FileDatabaseSelectActivity/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=61b1812aa5fc8b82c1dceb292ec76c63, view=b886386010fbb8633954fb7efe711216(FileDatabaseSelectActivity/Switch-Hardware k)) (nav)
  - act: CustomTouchEvent(state=78336156090439cb41d2e05f9903dfcb, view=c7b775f415a91ebe659332e51f845069(FileDatabaseSelectActivity/Button-OK)) (rule)

### G003 Generate a password

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the entry editor; tap the generate (dice/refresh) icon beside the password field
- Completion ratio: 1.00
- Actions taken: 2
  - act: CustomTouchEvent(state=78336156090439cb41d2e05f9903dfcb, view=f2230eee89c2f180d0d130ed53b51c9b(FileDatabaseSelectActivity/Spinner-Yubikey ch)) (heuristic)
  - act: CustomTouchEvent(state=d30e2455d84c2c602c710b49533a01bc, view=658f2f0a83e0ea4598f7e04fd5cb93c1(FileDatabaseSelectActivity/ImageButton-)) (heuristic)

### G004 Download

- Status: **partial**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the KeePassDX app; Navigate to the database containing the entry; Select the entry; Tap the attachment name
- Remaining steps: Select the download option; Wait for the download to complete
- Completion ratio: 0.67
- Actions taken: 17
  - act: CustomTouchEvent(state=94eff40d0b36c1f6e73046416cf2aba5, view=08cb02fb26098205332e856d1a3543a3(PickActivity/TextView-your_data_)) (rule)
  - act: CustomTouchEvent(state=eebbec042b9766b14b983bc4a6d8a098, view=6c93380437107f398778748a75a92696(FileDatabaseSelectActivity/Button-Cancel)) (llm)
  - act: CustomTouchEvent(state=78336156090439cb41d2e05f9903dfcb, view=c46c42db3988f98e3c1caee78c4c02b7(FileDatabaseSelectActivity/ProgressBar-)) (llm)
  - act: ScrollEvent(state=78336156090439cb41d2e05f9903dfcb, view=632ed9735d7251fd85b047d4b7ef9a4d(FileDatabaseSelectActivity/ScrollView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=149eed3386bd4968054ed345667796ad, view=f2230eee89c2f180d0d130ed53b51c9b(FileDatabaseSelectActivity/Spinner-Yubikey ch)) (heuristic)
  - act: CustomTouchEvent(state=31fbe327af90d0e7b5b921d530625462, view=f2230eee89c2f180d0d130ed53b51c9b(FileDatabaseSelectActivity/Spinner-Yubikey ch)) (heuristic)
  - act: CustomTouchEvent(state=149eed3386bd4968054ed345667796ad, view=79ec796495607a3ca94194ebfac52e97(FileDatabaseSelectActivity/EditText-Keyfile)) (heuristic)
  - act: CustomTouchEvent(state=149eed3386bd4968054ed345667796ad, view=c7b775f415a91ebe659332e51f845069(FileDatabaseSelectActivity/Button-OK)) (llm)

### G005 Copy a username

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the entry; Tap the username field; Select the username field; Tap the copy icon beside the username field
- Remaining steps: Wait for the username to be copied to the clipboard
- Completion ratio: 0.80
- Credited from later features: G003, G004
- Actions taken: 11
  - act: CustomTouchEvent(state=8d9553d5c8e8c3e31da36be7f0f63e1b, view=1343c34ecaad31d91656ba984756e158(FileDatabaseSelectActivity/TextView-Entropy: 0)) (nav)
  - act: CustomTouchEvent(state=4750d049dd62d9c9c730ca1989758960, view=1343c34ecaad31d91656ba984756e158(FileDatabaseSelectActivity/TextView-Entropy: 0)) (nav)
  - act: CustomTouchEvent(state=8d9553d5c8e8c3e31da36be7f0f63e1b, view=99a101afc090f8a35ca5b1d11d8e9d3f(FileDatabaseSelectActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=4750d049dd62d9c9c730ca1989758960, view=c7b775f415a91ebe659332e51f845069(FileDatabaseSelectActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=4750d049dd62d9c9c730ca1989758960, view=1ae6cfa6f7845d5d3fb39a69249f9aee(FileDatabaseSelectActivity/Switch-Password)) (rule)
  - act: CustomTouchEvent(state=a8d7a3d1f078f903e595b9a48029ae6d, view=1343c34ecaad31d91656ba984756e158(FileDatabaseSelectActivity/TextView-Entropy: 0)) (nav)
  - act: CustomTouchEvent(state=8d9553d5c8e8c3e31da36be7f0f63e1b, view=1343c34ecaad31d91656ba984756e158(FileDatabaseSelectActivity/TextView-Entropy: 0)) (nav)
  - act: CustomTouchEvent(state=4750d049dd62d9c9c730ca1989758960, view=c762892e7253388b7ad5f68579af54e1(FileDatabaseSelectActivity/ImageButton-)) (afford_search)

### G006 Edit an entry

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Tap on the entry you want to edit.; Tap the edit (pencil) icon next to the entry.; Enter the new information you wish to add or modify in the edit fields.; Verify the updated entry in the list to ensure the changes were applied correctly.
- Remaining steps: Tap the save icon to save the changes.
- Completion ratio: 0.80
- Credited from later features: G004
- Actions taken: 12
  - act: CustomTouchEvent(state=ca0d6cc578f0c85fcc32484e2ed1ce00, view=7f3827f29315c74eb3bce4511b59f4e3(FileDatabaseSelectActivity/TextView-Entropy: 3)) (nav)
  - act: CustomTouchEvent(state=276573aec3f5c388b3670a312c4c6d7b, view=7f3827f29315c74eb3bce4511b59f4e3(FileDatabaseSelectActivity/TextView-Entropy: 3)) (nav)
  - act: CustomTouchEvent(state=ca0d6cc578f0c85fcc32484e2ed1ce00, view=c7b775f415a91ebe659332e51f845069(FileDatabaseSelectActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=a646ab727dcc80616aeace7f328a93df, view=7f3827f29315c74eb3bce4511b59f4e3(FileDatabaseSelectActivity/TextView-Entropy: 3)) (nav)
  - act: CustomTouchEvent(state=6bb344207ee6e3965a4de23bcac2c157, view=7f3827f29315c74eb3bce4511b59f4e3(FileDatabaseSelectActivity/TextView-Entropy: 3)) (nav)
  - act: CustomTouchEvent(state=a646ab727dcc80616aeace7f328a93df, view=7f3827f29315c74eb3bce4511b59f4e3(FileDatabaseSelectActivity/TextView-Entropy: 3)) (nav)
  - act: CustomTouchEvent(state=6bb344207ee6e3965a4de23bcac2c157, view=c96fe53982540ce8a6802ee105bf1a7b(FileDatabaseSelectActivity/EditText-TestCube!2)) (rule)
  - act: CustomTouchEvent(state=6bb344207ee6e3965a4de23bcac2c157, view=99a101afc090f8a35ca5b1d11d8e9d3f(FileDatabaseSelectActivity/ImageButton-)) (rule)

### G007 Move an entry

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the KeePassDX app; Navigate to the database containing the entry you want to move; Long-press the entry you want to move; Select the desired destination for the entry
- Remaining steps: Tap the 'Move' action; Confirm the move action
- Completion ratio: 0.67
- Credited from later features: G004, G005
- Actions taken: 18
  - act: CustomTouchEvent(state=99378cf3f487c7a19cb4caa33d0d8a96, view=f2230eee89c2f180d0d130ed53b51c9b(FileDatabaseSelectActivity/Spinner-Yubikey ch)) (heuristic)
  - act: CustomTouchEvent(state=5d1cf047ac6a6f8b527c1c5a7e4fcf74, view=f2230eee89c2f180d0d130ed53b51c9b(FileDatabaseSelectActivity/Spinner-Yubikey ch)) (heuristic)
  - act: CustomTouchEvent(state=5d1cf047ac6a6f8b527c1c5a7e4fcf74, view=4099bc0e5c3dacf426ecc6ba292cb783(FileDatabaseSelectActivity/ImageButton-)) (afford_search)
  - act: CustomTouchEvent(state=cd4593e3e684f392b65435f443adf58b, view=f2230eee89c2f180d0d130ed53b51c9b(FileDatabaseSelectActivity/Spinner-Yubikey ch)) (heuristic)
  - act: CustomTouchEvent(state=83e13fb999576243d668abc7e35ba8bf, view=f2230eee89c2f180d0d130ed53b51c9b(FileDatabaseSelectActivity/Spinner-Yubikey ch)) (heuristic)
  - act: LongTouchEvent(state=cd4593e3e684f392b65435f443adf58b, view=7ef6b9bf7ab8671d53a54275b69eeba4(FileDatabaseSelectActivity/ImageView-)) (heuristic)
  - act: LongTouchEvent(state=cd4593e3e684f392b65435f443adf58b, view=7ef6b9bf7ab8671d53a54275b69eeba4(FileDatabaseSelectActivity/ImageView-)) (heuristic)
  - act: CustomSetTextEvent(state=cd4593e3e684f392b65435f443adf58b, view=f2230eee89c2f180d0d130ed53b51c9b(FileDatabaseSelectActivity/Spinner-Yubikey ch), text=TestCube!2026) (rule)

### G008 Edit, move

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Remaining steps: Long-press the group; Tap Edit to rename it or change its icon and notes; Tap the move action to relocate it; Tap the move action to relocate it; Tap the move action to relocate it; Tap Delete and confirm
- Completion ratio: 0.00
- Actions taken: 7
  - act: LongTouchEvent(state=83e13fb999576243d668abc7e35ba8bf, view=bb97d88cb5f3840ff64894e709042797(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: LongTouchEvent(state=5d1cf047ac6a6f8b527c1c5a7e4fcf74, view=99a101afc090f8a35ca5b1d11d8e9d3f(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: LongTouchEvent(state=cd4593e3e684f392b65435f443adf58b, view=bb97d88cb5f3840ff64894e709042797(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: LongTouchEvent(state=5d1cf047ac6a6f8b527c1c5a7e4fcf74, view=99a101afc090f8a35ca5b1d11d8e9d3f(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=cd4593e3e684f392b65435f443adf58b, view=c7b775f415a91ebe659332e51f845069(FileDatabaseSelectActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=cd4593e3e684f392b65435f443adf58b, view=c96fe53982540ce8a6802ee105bf1a7b(FileDatabaseSelectActivity/EditText-TestCube!2)) (rule)
  - act: CustomTouchEvent(state=cd4593e3e684f392b65435f443adf58b, view=bb97d88cb5f3840ff64894e709042797(FileDatabaseSelectActivity/ImageButton-)) (rule)

### G009 Search the database

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the KeePassDX app; Tap the 'Unlock' button; Tap the search icon in the toolbar; Enter the unlock method (e.g., key file, hardware key, biometrics, device credential); Enter the search query in the search bar; Press the search button to execute the search
- Completion ratio: 1.00
- Credited from later features: G011
- Actions taken: 16
  - act: CustomTouchEvent(state=b3dc3534178172d7d2f6a9ffded701ae, view=1526e15fcab91676e4be9f59c43ba888(PickActivity/CompoundButton-Documents)) (rule)
  - act: CustomTouchEvent(state=3c7b7aa05d3704a917b087756e751583, view=21edf07cd915c8aca9d064c7b9f0346b(PickActivity/CompoundButton-Documents)) (rule)
  - act: CustomTouchEvent(state=b3dc3534178172d7d2f6a9ffded701ae, view=1526e15fcab91676e4be9f59c43ba888(PickActivity/CompoundButton-Documents)) (rule)
  - act: CustomTouchEvent(state=3c7b7aa05d3704a917b087756e751583, view=f8969899c89bfb39627199a96ceb4f9c(PickActivity/AutoCompleteTextView-test)) (rule)
  - act: CustomTouchEvent(state=3c7b7aa05d3704a917b087756e751583, view=bf70cb41e57c0e75ef65780a02592d52(PickActivity/ImageView-)) (rule)
  - act: CustomSetTextEvent(state=beb42635bdfa6d1d252bc134322c4034, view=dea7f5ccb3e2cb7957da9d5e15694af5(PickActivity/AutoCompleteTextView-Search…), text=test) (rule)
  - act: CustomTouchEvent(state=3c7b7aa05d3704a917b087756e751583, view=65171f21eb5ef41f17324cdcde84ae25(PickActivity/TextView-Files in D)) (rule)
  - act: CustomSetTextEvent(state=c8c74b3e982c66a1082f125eb5c4d039, view=f2230eee89c2f180d0d130ed53b51c9b(FileDatabaseSelectActivity/Spinner-Yubikey ch), text=test) (nav)

### G010 Use the KeePassDX autofill

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the Android system settings; Select 'Passwords and accounts'; Select 'Autofill service'
- Remaining steps: Scroll to find 'Passwords and accounts'; Scroll to find 'Autofill service'; Tap on 'KeePassDX' to enable autofill
- Completion ratio: 0.50
- Credited from later features: G001, G004
- Actions taken: 6
  - act: CustomTouchEvent(state=a2441c1741023541e9934216b2add54b, view=8538f57947935e7ae9395e4f6391ff08(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=c8c74b3e982c66a1082f125eb5c4d039, view=c762892e7253388b7ad5f68579af54e1(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=a2441c1741023541e9934216b2add54b, view=8538f57947935e7ae9395e4f6391ff08(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=c8c74b3e982c66a1082f125eb5c4d039, view=c762892e7253388b7ad5f68579af54e1(FileDatabaseSelectActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=a2441c1741023541e9934216b2add54b, view=c7b775f415a91ebe659332e51f845069(FileDatabaseSelectActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=c8c74b3e982c66a1082f125eb5c4d039, view=afc241c312a535a7c5fcafd66d264e1d(FileDatabaseSelectActivity/TextView-The passwo)) (rule)

### G011 Open a database

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the 'Unlock' button; Unlock the database; Enter the unlock code; Select the 'Read-only' toggle; Verify the database is open in read-only mode
- Completion ratio: 1.00
- Actions taken: 15
  - act: CustomTouchEvent(state=2705a2ef4388dad9bb214f26fca11804, view=21edf07cd915c8aca9d064c7b9f0346b(PickActivity/CompoundButton-Documents)) (rule)
  - act: CustomTouchEvent(state=21be495e9b36bfa9004ae4dc56d984d4, view=1526e15fcab91676e4be9f59c43ba888(PickActivity/CompoundButton-Documents)) (rule)
  - act: CustomSetTextEvent(state=c8c74b3e982c66a1082f125eb5c4d039, view=dd0c160e62e3fa985fdba08c28e91a15(FileDatabaseSelectActivity/EditText-test), text=TestCube!2026) (mandatory_fill)
  - act: CustomSetTextEvent(state=5d1cf047ac6a6f8b527c1c5a7e4fcf74, view=c96fe53982540ce8a6802ee105bf1a7b(FileDatabaseSelectActivity/EditText-TestCube!2), text=TestCube!2026) (llm)
  - act: CustomTouchEvent(state=5d1cf047ac6a6f8b527c1c5a7e4fcf74, view=c762892e7253388b7ad5f68579af54e1(FileDatabaseSelectActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=99378cf3f487c7a19cb4caa33d0d8a96, view=2474d3792592d294b21b59f11d2c34b5(FileDatabaseSelectActivity/FrameLayout-)) (llm)
  - act: CustomTouchEvent(state=8ea55625a38258fbb36432d6e9c4621f, view=21edf07cd915c8aca9d064c7b9f0346b(PickActivity/CompoundButton-Documents)) (rule)
  - act: CustomTouchEvent(state=bbb65e2e5e0f924ac6b8ed7056801e3b, view=65171f21eb5ef41f17324cdcde84ae25(PickActivity/TextView-Files in D)) (rule)

### G012 Configure clipboard timeout

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Tap the 'Save' button to apply the changes.
- Remaining steps: Tap on the 'Settings' option in the main menu.; Scroll down to the 'Security' section.; Tap on the 'Clipboard' option.; Tap on 'Clipboard Timeout' to configure it.; Enter the desired timeout duration in the input field.
- Completion ratio: 0.17
- Credited from later features: G009

### G013 Change the database encryption

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Select 'Database' from the settings menu.; Select 'Change' to modify the current encryption settings.
- Remaining steps: Tap on the 'Settings' icon in the top right corner of the main screen.; Tap on 'Encryption' to access the encryption settings.; Enter the new encryption settings as required by the app.; Confirm the changes by tapping 'OK' or 'Apply'.
- Completion ratio: 0.33
- Credited from later features: G004

### G014 Use entry templates

- Status: **pending**
- Reason: Retry after later features discovered new states.
- Feature source: guide
- Completed steps: Open the database settings and set the templates group (KDBX 4); Tap on the '+' icon to add a new entry
- Remaining steps: Select 'Templates' from the navigation hints; Enter the name of the template group; Tap on the template group to confirm and save the settings
- Completion ratio: 0.40
- Credited from later features: G001, G004

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
