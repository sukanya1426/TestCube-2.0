# Feature test report: Fossify Notes

- Started: 2026-10-25 13:10:41
- Finished: 2026-10-25 14:09:14
- Features: 14
- Covered: 9
- Partial: 5
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 85% (mean completion ratio; the headline number)
- Coverage: 64% (features with every guide step matched)
- Stop reason: all_features_done
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 14
- Never attempted: 0
- Blocked then recovered on retry: 0
- Blocked still: 0

## Guide vs README-extracted

- Guide features: 14
- README-extracted features: 8
- In both: 1
- Guide-only: 13
- README-only: 7
  - guide-only: G001 Create a text note
  - guide-only: G002 Tick
  - guide-only: G003 Switch between notes
  - guide-only: G004 Delete a note
  - guide-only: G006 Unlock a protected note
  - guide-only: G007 Export all notes at
  - guide-only: G008 Keep a note synchronised
  - guide-only: G009 Print a note
  - guide-only: G010 Change the editor font
  - guide-only: G011 Set where the cursor
  - guide-only: G012 Show a word
  - guide-only: G013 Enable automatic saving
  - README-only: F001 Close or skip the tutorial
  - README-only: F002 Leave any first-run analytics or settings screen
  - README-only: F003 Tap Create Database or Open Database if shown
  - README-only: F004 Enter a file name if asked and confirm Save
  - README-only: F005 Reach the home or main screen
  - README-only: F007 Import or export data
  - README-only: F008 Change app settings

## Text-field resolution

- Filled via credential.txt: 73
- Filled via VLM/Gemini: 0
- Unresolved: 0
- Online coverage: 64% (9/14) — live journal self-report (covered / extracted features).
- Offline coverage: not computed (no ground-truth JSON).

## Findings

### G001 Create a text note

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the app; Tap the overflow menu (three dots); Select 'new note'; Tap 'Save'; Enter the note text
- Completion ratio: 1.00
- Credited from later features: G002, G003, G008
- Actions taken: 10
  - act: CustomTouchEvent(state=7f21d5b825e9d9aec679e8ec26fe7eac, view=19d95f88d8a892a79c7bb5982ec7e1a6(MainActivity/TextView-New note t)) (nav)
  - act: CustomTouchEvent(state=7f21d5b825e9d9aec679e8ec26fe7eac, view=86952d5d609c23711522f0682316cafc(MainActivity/TextView-Add a new )) (nav)
  - act: CustomTouchEvent(state=7f21d5b825e9d9aec679e8ec26fe7eac, view=86952d5d609c23711522f0682316cafc(MainActivity/TextView-Add a new )) (nav)
  - act: CustomSetTextEvent(state=7f21d5b825e9d9aec679e8ec26fe7eac, view=6e3217e85d9ea23f15fb75de55be8f27(MainActivity/EditText-Label), text=no) (llm)
  - act: CustomTouchEvent(state=4e95cfc48dfacbc9059ee6a4db637399, view=19d95f88d8a892a79c7bb5982ec7e1a6(MainActivity/TextView-New note t)) (nav)
  - act: CustomTouchEvent(state=4e95cfc48dfacbc9059ee6a4db637399, view=b524df81f1e29847e0a8bf3e1a4c1119(MainActivity/RadioButton-Text note)) (rule)
  - act: CustomTouchEvent(state=cc43185bc2fcf1d28fcb931f1a83fd07, view=4dca066dccb2a3c4095bbb5d50ea8f9f(MainActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=c371045ef289011b26c40c2d587f01e1, view=6e3217e85d9ea23f15fb75de55be8f27(MainActivity/EditText-Label), text=no) (mandatory_fill)

### G002 Tick

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the checklist note; Tap the checkbox beside an item to mark it done; Verify the item is now marked as done in the checklist
- Completion ratio: 1.00
- Actions taken: 15
  - act: CustomSetTextEvent(state=4e95cfc48dfacbc9059ee6a4db637399, view=da426ae52907f06d0bffa2e7cb739ea8(MainActivity/EditText-no), text=no) (llm)
  - act: CustomTouchEvent(state=4e95cfc48dfacbc9059ee6a4db637399, view=d92eb8bb92de362453999e32491af063(MainActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=6180233b8fb7e1bec0b3b3c6493b14a2(MainActivity/RadioButton-Text note)) (nav)
  - act: CustomTouchEvent(state=4e95cfc48dfacbc9059ee6a4db637399, view=19d95f88d8a892a79c7bb5982ec7e1a6(MainActivity/TextView-New note t)) (nav)
  - act: CustomTouchEvent(state=4e95cfc48dfacbc9059ee6a4db637399, view=9aadbc45f5053ef6bfc9f2e76038bb93(MainActivity/RadioButton-Checklist)) (nav)
  - act: CustomTouchEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=f6b3265e242d8021a895a2ef9edf83e0(MainActivity/Button-Cancel)) (nav)
  - act: CustomTouchEvent(state=cc43185bc2fcf1d28fcb931f1a83fd07, view=e5256d390ab6bfd17a98f2d950b0df01(MainActivity/CheckBox-)) (heuristic)
  - act: CustomTouchEvent(state=e0d1f8e97bcd450a233631063db8af47, view=c2dbe1a0533a0858306d17703a0f3479(MainActivity/TextView-no)) (heuristic)

### G003 Switch between notes

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the note title in the toolbar (or open the overflow menu; Select the note you want to switch to; Tap 'Open note'
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=f024b0f4a3dcb5d1d4901e61eca51734, view=ef2bd5a42f90253118719d0c2c8ce227(MainActivity/EditText-Insert tex)) (heuristic)
  - act: CustomTouchEvent(state=f024b0f4a3dcb5d1d4901e61eca51734, view=ef2bd5a42f90253118719d0c2c8ce227(MainActivity/EditText-Insert tex)) (heuristic)
  - act: CustomTouchEvent(state=f024b0f4a3dcb5d1d4901e61eca51734, view=9e241f9ef8017e8e3e09d6fc125d9e2e(MainActivity/TextView-General no)) (heuristic)

### G004 Delete a note

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the note; Tap the overflow menu; Select 'Delete note'; Confirm the deletion
- Completion ratio: 1.00
- Credited from later features: G003, G007
- Actions taken: 27
  - act: CustomTouchEvent(state=fff1cca1fbc74950ec43c32f16d1ac2d, view=f7535c9acc0952447a5c6c7b61acb18d(MainActivity/Button-)) (nav)
  - act: CustomTouchEvent(state=3a3c5bf873db4f57bd7690a6b657bd95, view=8f53de1abe777291a64c5ae42b6171a1(MainActivity/TextView-0)) (nav)
  - act: CustomTouchEvent(state=3a3c5bf873db4f57bd7690a6b657bd95, view=8f53de1abe777291a64c5ae42b6171a1(MainActivity/TextView-0)) (nav)
  - act: CustomTouchEvent(state=3a3c5bf873db4f57bd7690a6b657bd95, view=9e241f9ef8017e8e3e09d6fc125d9e2e(MainActivity/TextView-General no)) (nav)
  - act: CustomTouchEvent(state=3a3c5bf873db4f57bd7690a6b657bd95, view=9e241f9ef8017e8e3e09d6fc125d9e2e(MainActivity/TextView-General no)) (nav)
  - act: CustomTouchEvent(state=3a3c5bf873db4f57bd7690a6b657bd95, view=8f02a6729a054adbb09f7967364d876b(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=643d7d72d69e4f35176755987fe6c586, view=73116cc5ba008b2c97d204df7674c47f(MainActivity/TextView-no)) (nav)
  - act: CustomTouchEvent(state=32e23464e67661b7daa9371829a5b3e7, view=4dca066dccb2a3c4095bbb5d50ea8f9f(MainActivity/Button-)) (rule)

### G005 Search inside a note

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the note you want to search inside; Review the search results within the note; Tap the search icon in the toolbar; Enter the search term in the search bar; Press the Enter key to execute the search
- Completion ratio: 1.00
- Credited from later features: G003
- Actions taken: 16
  - act: CustomTouchEvent(state=c371045ef289011b26c40c2d587f01e1, view=c163f4ec027a828fc6c78cebf6e23235(MainActivity/RadioButton-Checklist)) (llm)
  - act: CustomTouchEvent(state=c371045ef289011b26c40c2d587f01e1, view=c163f4ec027a828fc6c78cebf6e23235(MainActivity/RadioButton-Checklist)) (llm)
  - act: CustomTouchEvent(state=c371045ef289011b26c40c2d587f01e1, view=f6b3265e242d8021a895a2ef9edf83e0(MainActivity/Button-Cancel)) (llm)
  - act: CustomTouchEvent(state=cc43185bc2fcf1d28fcb931f1a83fd07, view=8f02a6729a054adbb09f7967364d876b(MainActivity/Button-)) (nav)
  - act: CustomTouchEvent(state=643d7d72d69e4f35176755987fe6c586, view=1a2e9b60a184d41135e51a668f2f34c4(MainActivity/TextView-no)) (nav)
  - act: CustomTouchEvent(state=cb34aff85bccd7093427fcac30cfcfaa, view=f7535c9acc0952447a5c6c7b61acb18d(MainActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=e4e87e5e3c65bad96423a7a868bc3a69, view=c8ec54d6ce4d74505ada267e98c552b1(MainActivity/EditText-Search), text=test) (mandatory_fill)
  - act: CustomSetTextEvent(state=032cb6a80bb64c8789e5018a1012878d, view=7edcfb99affc6ea5331861e35e0abcd3(MainActivity/EditText-test), text=test) (mandatory_fill)

### G006 Unlock a protected note

- Status: **partial**
- Reason: Could not reach the feature from this screen.
- Feature source: guide
- Completed steps: Tap on the locked note; Enter the PIN or pattern; Select the unlock option; Confirm the unlock action
- Remaining steps: Present the fingerprint
- Completion ratio: 0.80
- Credited from later features: G012, G007
- Actions taken: 36
  - act: CustomTouchEvent(state=fff1cca1fbc74950ec43c32f16d1ac2d, view=4dca066dccb2a3c4095bbb5d50ea8f9f(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=c371045ef289011b26c40c2d587f01e1, view=6e3217e85d9ea23f15fb75de55be8f27(MainActivity/EditText-Label)) (nav)
  - act: CustomTouchEvent(state=c371045ef289011b26c40c2d587f01e1, view=6e3217e85d9ea23f15fb75de55be8f27(MainActivity/EditText-Label)) (nav)
  - act: CustomTouchEvent(state=c371045ef289011b26c40c2d587f01e1, view=6e3217e85d9ea23f15fb75de55be8f27(MainActivity/EditText-Label)) (nav)
  - act: CustomTouchEvent(state=c371045ef289011b26c40c2d587f01e1, view=6e3217e85d9ea23f15fb75de55be8f27(MainActivity/EditText-Label)) (nav)
  - act: CustomTouchEvent(state=c371045ef289011b26c40c2d587f01e1, view=6e3217e85d9ea23f15fb75de55be8f27(MainActivity/EditText-Label)) (nav)
  - act: CustomTouchEvent(state=c371045ef289011b26c40c2d587f01e1, view=6e3217e85d9ea23f15fb75de55be8f27(MainActivity/EditText-Label)) (nav)
  - act: CustomSetTextEvent(state=c371045ef289011b26c40c2d587f01e1, view=6e3217e85d9ea23f15fb75de55be8f27(MainActivity/EditText-Label), text=no) (nav)

### G007 Export all notes at

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open the overflow menu; Tap 'Export all notes'; Select 'Export all notes'; Confirm export
- Remaining steps: Wait for export completion
- Completion ratio: 0.80
- Credited from later features: G003
- Actions taken: 39
  - act: CustomTouchEvent(state=87f1e0a79f5709f9733bc1e1718ff420, view=c0b2e7961dac1e5354b8d94df32a08a3(MainActivity/RadioButton-Only expor)) (heuristic)
  - act: CustomTouchEvent(state=32e23464e67661b7daa9371829a5b3e7, view=f7535c9acc0952447a5c6c7b61acb18d(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=c2fc2ac581cdc8941dfd92a032deba37, view=714ff92a3b1b448845367fcdeaa59c6c(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=d5b33841f845937e784f5b6b8e93c998, view=5a147532e006c1b1d4eb02cf5722c698(MainActivity/TextView-Rename not)) (llm)
  - act: CustomTouchEvent(state=b6cfd17a3c87f014b3347ce5c22493f1, view=e528811d12670d1e9b95ecd05100697c(MainActivity/TextView-Rename not)) (llm)
  - act: CustomTouchEvent(state=b6cfd17a3c87f014b3347ce5c22493f1, view=e528811d12670d1e9b95ecd05100697c(MainActivity/TextView-Rename not)) (llm)
  - act: CustomTouchEvent(state=b6cfd17a3c87f014b3347ce5c22493f1, view=e528811d12670d1e9b95ecd05100697c(MainActivity/TextView-Rename not)) (llm)
  - act: CustomTouchEvent(state=b6cfd17a3c87f014b3347ce5c22493f1, view=e528811d12670d1e9b95ecd05100697c(MainActivity/TextView-Rename not)) (rule)

### G008 Keep a note synchronised

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the 'Keep a note synchronised' feature; Select 'Import or create a note'; Enter the note content; Tap the 'Save' button to synchronize the note
- Completion ratio: 1.00
- Actions taken: 4
  - act: CustomTouchEvent(state=f024b0f4a3dcb5d1d4901e61eca51734, view=8f02a6729a054adbb09f7967364d876b(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=77ea54c5e0d5b8c55667ac0dc92bd0a7, view=73116cc5ba008b2c97d204df7674c47f(MainActivity/TextView-no)) (heuristic)
  - act: CustomSetTextEvent(state=f024b0f4a3dcb5d1d4901e61eca51734, view=ef2bd5a42f90253118719d0c2c8ce227(MainActivity/EditText-Insert tex), text=no) (mandatory_fill)
  - act: CustomTouchEvent(state=bc439bafa95fda5d462609b9808108c5, view=27ebc70ce2a020218add1a3f5db51ac4(MainActivity/EditText-no)) (heuristic)

### G009 Print a note

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the note; Tap the overflow menu; Choose 'Print' to print the note; Select 'Print' from the menu
- Completion ratio: 1.00
- Credited from later features: G003
- Actions taken: 10
  - act: CustomTouchEvent(state=2c555232f748c5bce08f0bd466f14a58, view=9e241f9ef8017e8e3e09d6fc125d9e2e(MainActivity/TextView-General no)) (nav)
  - act: CustomTouchEvent(state=2c555232f748c5bce08f0bd466f14a58, view=9e241f9ef8017e8e3e09d6fc125d9e2e(MainActivity/TextView-General no)) (nav)
  - act: CustomTouchEvent(state=2c555232f748c5bce08f0bd466f14a58, view=714ff92a3b1b448845367fcdeaa59c6c(MainActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=d5b33841f845937e784f5b6b8e93c998, view=07091861938c2fa44a210db4e6ce2ae8(MainActivity/TextView-Delete not)) (nav)
  - act: CustomTouchEvent(state=5c12e052ab5d75da5bf4d0d02b17c686, view=c61b3ab65e33ab1b964db34a8954cec9(MainActivity/TextView-Are you su)) (nav)
  - act: CustomTouchEvent(state=5c12e052ab5d75da5bf4d0d02b17c686, view=f6b3265e242d8021a895a2ef9edf83e0(MainActivity/Button-Cancel)) (nav)
  - act: CustomTouchEvent(state=2c555232f748c5bce08f0bd466f14a58, view=8f02a6729a054adbb09f7967364d876b(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=d5b33841f845937e784f5b6b8e93c998, view=af8ccdba9505ea4067dfca49cb0062e5(MainActivity/TextView-Print)) (heuristic)

### G010 Change the editor font

- Status: **partial**
- Reason: Could not reach the feature from this screen.
- Feature source: guide
- Completed steps: Open Settings; Select 'Font'
- Remaining steps: Scroll to the 'Editor' section; Tap the font size entry and choose the size; Tap outside the font size entry to save changes
- Completion ratio: 0.40
- Credited from later features: G002, G003
- Actions taken: 29
  - act: CustomSetTextEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=da426ae52907f06d0bffa2e7cb739ea8(MainActivity/EditText-no), text=no) (rule)
  - act: CustomSetTextEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=da426ae52907f06d0bffa2e7cb739ea8(MainActivity/EditText-no), text=no) (rule)
  - act: CustomTouchEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=da426ae52907f06d0bffa2e7cb739ea8(MainActivity/EditText-no)) (llm)
  - act: CustomTouchEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=d92eb8bb92de362453999e32491af063(MainActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=b6cfd17a3c87f014b3347ce5c22493f1, view=e528811d12670d1e9b95ecd05100697c(MainActivity/TextView-Rename not)) (rule)
  - act: CustomTouchEvent(state=b6cfd17a3c87f014b3347ce5c22493f1, view=e528811d12670d1e9b95ecd05100697c(MainActivity/TextView-Rename not)) (rule)
  - act: CustomTouchEvent(state=b6cfd17a3c87f014b3347ce5c22493f1, view=e528811d12670d1e9b95ecd05100697c(MainActivity/TextView-Rename not)) (rule)
  - act: CustomTouchEvent(state=b6cfd17a3c87f014b3347ce5c22493f1, view=e528811d12670d1e9b95ecd05100697c(MainActivity/TextView-Rename not)) (rule)

### G011 Set where the cursor

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open Settings; Tap on 'General'
- Remaining steps: Select 'Cursor Placement'; Enter 'where' in the search bar; Tap on 'cursor' in the search results; Select 'placed' to set the cursor placement
- Completion ratio: 0.33
- Credited from later features: G002, G009
- Actions taken: 37
  - act: KeyEvent(state=b6cfd17a3c87f014b3347ce5c22493f1, name=BACK) (llm)
  - act: CustomTouchEvent(state=c2fc2ac581cdc8941dfd92a032deba37, view=ca10227827d1ed3be6c48ba8ba81525e(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=c2fc2ac581cdc8941dfd92a032deba37, view=ca10227827d1ed3be6c48ba8ba81525e(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=c2fc2ac581cdc8941dfd92a032deba37, view=714ff92a3b1b448845367fcdeaa59c6c(MainActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=d5b33841f845937e784f5b6b8e93c998, view=5a147532e006c1b1d4eb02cf5722c698(MainActivity/TextView-Rename not)) (llm)
  - act: KeyEvent(state=b6cfd17a3c87f014b3347ce5c22493f1, name=BACK) (llm)
  - act: KeyEvent(state=b6cfd17a3c87f014b3347ce5c22493f1, name=BACK) (llm)
  - act: CustomTouchEvent(state=c2fc2ac581cdc8941dfd92a032deba37, view=f7535c9acc0952447a5c6c7b61acb18d(MainActivity/Button-)) (rule)

### G012 Show a word

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the Notes app; Navigate to the Settings menu; Select the 'Show word count' option; Enable the 'Show word count' feature; Return to the main notes screen
- Completion ratio: 1.00
- Credited from later features: G003
- Actions taken: 25
  - act: CustomTouchEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=c163f4ec027a828fc6c78cebf6e23235(MainActivity/RadioButton-Checklist)) (rule)
  - act: CustomTouchEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=c163f4ec027a828fc6c78cebf6e23235(MainActivity/RadioButton-Checklist)) (rule)
  - act: CustomTouchEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=c163f4ec027a828fc6c78cebf6e23235(MainActivity/RadioButton-Checklist)) (rule)
  - act: CustomTouchEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=c163f4ec027a828fc6c78cebf6e23235(MainActivity/RadioButton-Checklist)) (rule)
  - act: CustomTouchEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=c163f4ec027a828fc6c78cebf6e23235(MainActivity/RadioButton-Checklist)) (rule)
  - act: CustomTouchEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=d92eb8bb92de362453999e32491af063(MainActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=eb7a9d0e981ee7d9fd49929c9f03b43a, view=d92eb8bb92de362453999e32491af063(MainActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=c2fc2ac581cdc8941dfd92a032deba37, view=38fd0afc4a3601593d907923954596ab(MainActivity/TextView-1)) (heuristic)

### G013 Enable automatic saving

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open Settings; Save the settings; Scroll to 'General'
- Remaining steps: Select 'Automatic Save'; Toggle the automatic save option
- Completion ratio: 0.60
- Credited from later features: G008, G009
- Actions taken: 43
  - act: CustomTouchEvent(state=d5b33841f845937e784f5b6b8e93c998, view=7b5bacb2fc3f93c5f67d13b990d79186(MainActivity/TextView-Share)) (llm)
  - act: CustomTouchEvent(state=de293b19b5295753a56f935b7464477a, view=714ff92a3b1b448845367fcdeaa59c6c(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=d5b33841f845937e784f5b6b8e93c998, view=73a41b8440452927281da573dcbd6e94(MainActivity/TextView-Settings)) (rule)
  - act: CustomTouchEvent(state=5074233d9fcf28fae39d2888f2a15172, view=f81a43b1b183ccbb649bbb3c9c43deb3(SettingsActivity/Switch-Enable lin)) (heuristic)
  - act: CustomTouchEvent(state=50162c96b0668e3896db6c7434dbdcfb, view=6ebd050a66249c6be6fdd3530344ef33(SettingsActivity/TextView-Look & fee)) (heuristic)
  - act: CustomTouchEvent(state=50162c96b0668e3896db6c7434dbdcfb, view=d463c3f8c8c6087dc9192604eef116aa(SettingsActivity/Switch-Enable lin)) (heuristic)
  - act: ScrollEvent(state=5074233d9fcf28fae39d2888f2a15172, view=4f3b17fe2380997322125545525b06a3(SettingsActivity/ScrollView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=b00693d0f9b068bce7577ca896c99b26, view=39fe0c74fc64e56bae09daf00e654cf3(SettingsActivity/RelativeLayout-)) (rule)

### G014 Customise the app colours

- Status: **covered**
- Reason: Covered by shared-flow reuse of C018.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open Settings; Tap 'Done'; Tap 'Customise colours'; Select 'Primary Color'; Enter '#FF0000'
- Completion ratio: 1.00
- Credited from later features: G002
- Actions taken: 32
  - act: CustomTouchEvent(state=d5b33841f845937e784f5b6b8e93c998, view=48cf3541123df69f7f11b9a545ab4adf(MainActivity/TextView-About)) (llm)
  - act: CustomSetTextEvent(state=581194cb05f2cc799224cd82133e06e9, view=ed2fc1732a0ca798880b78136736c71c(MainActivity/EditText-no), text=no) (heuristic)
  - act: CustomSetTextEvent(state=c14daaeae45b0cca6843e56dde369b7e, view=ed2fc1732a0ca798880b78136736c71c(MainActivity/EditText-no), text=no) (heuristic)
  - act: CustomSetTextEvent(state=c14daaeae45b0cca6843e56dde369b7e, view=ed2fc1732a0ca798880b78136736c71c(MainActivity/EditText-no), text=no) (heuristic)
  - act: ScrollEvent(state=c14daaeae45b0cca6843e56dde369b7e, view=df729f230753b5a34fa4b27c4cc0506d(MainActivity/o-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=c14daaeae45b0cca6843e56dde369b7e, view=f7535c9acc0952447a5c6c7b61acb18d(MainActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=d91da2ecb939732b14f6ad2bb43f62b2, view=c8ec54d6ce4d74505ada267e98c552b1(MainActivity/EditText-Search), text=test) (llm)
  - act: CustomSetTextEvent(state=59ae406059824c9f3f72247f9f5fee5b, view=7edcfb99affc6ea5331861e35e0abcd3(MainActivity/EditText-test), text=test) (llm)

## Shared flows detected

1 reuse(s); 3 action(s) skipped by not re-executing a known terminal flow.

- `G014` reused `C018` (from G005), skipped 3 action(s)

See `session.json` and `log.md` in this folder for the full trace.
