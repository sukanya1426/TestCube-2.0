# Feature test report: Fossify Contacts

- Started: 2026-09-25 01:51:50
- Finished: 2026-09-25 02:20:16
- Features: 14
- Covered: 0
- Partial: 14
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 48% (mean completion ratio; the headline number)
- Coverage: 0% (features with every guide step matched)
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
- In both: 0
- Guide-only: 14
- README-only: 8
  - guide-only: G001 Create a contact
  - guide-only: G002 Add multiple phone numbers
  - guide-only: G003 Add postal addresses
  - guide-only: G004 Add the organisation
  - guide-only: G005 Add notes
  - guide-only: G006 Edit a contact
  - guide-only: G007 Mark a contact
  - guide-only: G008 Call a contact
  - guide-only: G009 Send an email
  - guide-only: G010 Add contacts
  - guide-only: G011 Send a message
  - guide-only: G012 Sort the contact list
  - README-only: F001 Close or skip the tutorial
  - README-only: F002 Leave any first-run analytics or settings screen
  - README-only: F003 Tap Create Database or Open Database if shown
  - README-only: F004 Enter a file name if asked and confirm Save
  - README-only: F005 Reach the home or main screen
  - README-only: F006 Search
  - README-only: F007 Import or export data
  - README-only: F008 Change app settings

## Text-field resolution

- Filled via credential.txt: 9
- Filled via VLM/Gemini: 2
- Unresolved: 0
- Online coverage: 0% (0/14) — live journal self-report (covered / extracted features).
- Offline coverage: 0% (0 covered / 38; 7 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 5% (mean completion ratio).

## Findings

### G001 Create a contact

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the app; Tap the 'Save' button
- Remaining steps: Tap the '+' floating action button; Enter the contact's name; Enter the contact's phone number
- Completion ratio: 0.40
- Credited from later features: G002
- Actions taken: 8
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=2747ef025fbfbdd3fc2d42a2f5cc2414(MainActivity/FloatingActionButton-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=7435c31b0dbb7c0bfce14ee81fb92d11(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=7435c31b0dbb7c0bfce14ee81fb92d11(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=832c30cd199ec870e48a1156624651f8(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=832c30cd199ec870e48a1156624651f8(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=cda8ec7ba557104f0c1c875b1c54eafd(EditContactActivity/ImageView-)) (llm)
  - act: CustomSetTextEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=e9d85afb583e0d70699ab56ac16ba404(EditContactActivity/AutoCompleteTextView-First name), text=TestCube List) (llm)
  - act: CustomTouchEvent(state=798a4f408c98c947709c0532f91f72bf, view=e6b1c6022b26c6027183ac192897e784(EditContactActivity/AutoCompleteTextView-TestCube L)) (rule)

### G002 Add multiple phone numbers

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the contact editor
- Remaining steps: tap the "+" beside the phone section
- Completion ratio: 0.50
- Actions taken: 8
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=2747ef025fbfbdd3fc2d42a2f5cc2414(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=f10ac85c6c34624f12b2a26354c29bfc(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=8bdb67e0e302dce8526b361e43b8bafa(EditContactActivity/TextView-Home)) (nav)
  - act: CustomTouchEvent(state=abebb97be07570c9158f8c943d62c85a, view=821ba764bb08809cb26c2e874378a388(EditContactActivity/RadioButton-Custom)) (llm)
  - act: CustomTouchEvent(state=d41b80a6def74cf235c0b66930315bb2, view=e85d9456790532ed1c14ece846ea478a(EditContactActivity/TextView-Label)) (llm)
  - act: CustomTouchEvent(state=d41b80a6def74cf235c0b66930315bb2, view=02a8107b7a8a1266b0f5a032d52b979e(EditContactActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=d41b80a6def74cf235c0b66930315bb2, view=92cd00ab7c7d5d5860d2832c4ab155c2(EditContactActivity/EditText-Title)) (llm)
  - act: CustomTouchEvent(state=d41b80a6def74cf235c0b66930315bb2, x=789, y=703) (llm)

### G003 Add postal addresses

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the contact editor
- Remaining steps: tap the "+" beside the address section
- Completion ratio: 0.50
- Credited from later features: G002
- Actions taken: 3
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=6336e7794cca3231ba87a804e4b6c694(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=5c7429df2d1ae0c32b72a5fed686dac8, view=5a82e84abe3d2c67037dfe982cbaab75(MainActivity/TextView-Settings)) (rule)
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=6336e7794cca3231ba87a804e4b6c694(MainActivity/ImageView-)) (heuristic)

### G004 Add the organisation

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Add' button to start creating a new contact.; Tap on the 'Save' button to add the organisation to the contact.
- Remaining steps: Select the 'organisation' option from the dropdown menu.; Enter the name of the organisation in the text field.; Tap on the 'job' option to add the job title.; Enter the job title in the text field.
- Completion ratio: 0.33
- Credited from later features: G006
- Actions taken: 12
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=f10ac85c6c34624f12b2a26354c29bfc(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=8bdb67e0e302dce8526b361e43b8bafa(EditContactActivity/TextView-Home)) (nav)
  - act: CustomTouchEvent(state=abebb97be07570c9158f8c943d62c85a, view=821ba764bb08809cb26c2e874378a388(EditContactActivity/RadioButton-Custom)) (llm)
  - act: CustomTouchEvent(state=d41b80a6def74cf235c0b66930315bb2, view=92cd00ab7c7d5d5860d2832c4ab155c2(EditContactActivity/EditText-Title)) (llm)
  - act: CustomTouchEvent(state=d41b80a6def74cf235c0b66930315bb2, view=192b65f5e8d17adf1617a50886a0a692(EditContactActivity/Button-Cancel)) (llm)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=36fc3fe99d31afc5c5a845a5d7c5230b(EditContactActivity/TextView-Home)) (afford_search)
  - act: CustomTouchEvent(state=8eb8e9d488975bfa2b14490db6ea91d9, view=db5c1b99610106921c86bf3176503c40(EditContactActivity/RadioButton-Home)) (llm)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=e9d85afb583e0d70699ab56ac16ba404(EditContactActivity/AutoCompleteTextView-First name)) (rule)

### G005 Add notes

- Status: **partial**
- Reason: blocked_no_progress: stayed in the same state cluster after 10 actions.
- Feature source: guide
- Completed steps: Tap on the contact you want to add notes to; Tap on the 'Edit' button to open the contact editor; Tap on the 'Save' button to update the contact
- Remaining steps: Scroll to the 'Notes' field; Enter the notes you want to add
- Completion ratio: 0.60
- Credited from later features: G004
- Actions taken: 11
  - act: ScrollEvent(state=46ac1cbd5e80666829184c5238ef3854, view=1583de512dd84d6832f9fe22a1641968(MainActivity/b-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=fc16bc34cec818e1f77e7118e60d0d49(MainActivity/TextView-No contact)) (nav)
  - act: CustomSetTextEvent(state=46ac1cbd5e80666829184c5238ef3854, view=2c55da7dcd1fc911bc404a63c177cf74(MainActivity/EditText-Search), text=test) (llm)
  - act: CustomTouchEvent(state=8ac0b424f20e0107405d6cad84d0347c, view=2747ef025fbfbdd3fc2d42a2f5cc2414(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=dcc3eda97ce46cce32acfa4fe029ed0b(EditContactActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=199dd7b8130e8e515032bef32db2e6d9(EditContactActivity/EditText-Address)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=36fc3fe99d31afc5c5a845a5d7c5230b(EditContactActivity/TextView-Home)) (afford_search)
  - act: CustomTouchEvent(state=8eb8e9d488975bfa2b14490db6ea91d9, view=db5c1b99610106921c86bf3176503c40(EditContactActivity/RadioButton-Home)) (rule)

### G006 Edit a contact

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the contact; Verify the changes in the contact list
- Remaining steps: Tap the edit (pencil) icon; Enter the new information; Tap the save icon
- Completion ratio: 0.40
- Credited from later features: G007
- Actions taken: 10
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=7cf851b94ba0f40ad1f207b351e45617(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=7cf851b94ba0f40ad1f207b351e45617(EditContactActivity/ImageView-)) (nav)
  - act: CustomSetTextEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=199dd7b8130e8e515032bef32db2e6d9(EditContactActivity/EditText-Address), text=testcube.bench@example.com) (afford_search)
  - act: CustomTouchEvent(state=f7bb0f86403e7c397f4897d7edf80ee6, view=7435c31b0dbb7c0bfce14ee81fb92d11(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=f7bb0f86403e7c397f4897d7edf80ee6, view=7435c31b0dbb7c0bfce14ee81fb92d11(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=f7bb0f86403e7c397f4897d7edf80ee6, view=36fc3fe99d31afc5c5a845a5d7c5230b(EditContactActivity/TextView-Home)) (afford_search)
  - act: CustomTouchEvent(state=8eb8e9d488975bfa2b14490db6ea91d9, view=821ba764bb08809cb26c2e874378a388(EditContactActivity/RadioButton-Custom)) (llm)
  - act: CustomTouchEvent(state=d41b80a6def74cf235c0b66930315bb2, view=02a8107b7a8a1266b0f5a032d52b979e(EditContactActivity/Button-OK)) (rule)

### G007 Mark a contact

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the contact; Select the contact; Tap the star icon in the contact details
- Remaining steps: Tap the star icon in the toolbar; Confirm the marking as a favourite
- Completion ratio: 0.60
- Credited from later features: G002, G006
- Actions taken: 10
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=ae4ac57d07b6cebdaac966978dec3f76(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=ae4ac57d07b6cebdaac966978dec3f76(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=3d8fdc89e3bfbd8646c68fd796db1288(EditContactActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=2598d78e1e6067fbd234bd260eed9a6a, view=7435c31b0dbb7c0bfce14ee81fb92d11(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=2598d78e1e6067fbd234bd260eed9a6a, view=7435c31b0dbb7c0bfce14ee81fb92d11(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=2598d78e1e6067fbd234bd260eed9a6a, view=36fc3fe99d31afc5c5a845a5d7c5230b(EditContactActivity/TextView-Home)) (afford_search)
  - act: CustomTouchEvent(state=8eb8e9d488975bfa2b14490db6ea91d9, view=821ba764bb08809cb26c2e874378a388(EditContactActivity/RadioButton-Custom)) (llm)
  - act: CustomTouchEvent(state=d41b80a6def74cf235c0b66930315bb2, view=02a8107b7a8a1266b0f5a032d52b979e(EditContactActivity/Button-OK)) (rule)

### G008 Call a contact

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the contact
- Remaining steps: tap the phone number (or the call icon beside it); the dialler is opened with the number
- Completion ratio: 0.50
- Credited from later features: G002
- Actions taken: 3
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=ab689a902fec3d95f9ad72e4b66dd63c(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=beeb7a89182869582edf17385b8bd9eb, view=3364249f5a9e0dae0741e232cfdb386b(MainActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=ab689a902fec3d95f9ad72e4b66dd63c(MainActivity/Button-)) (rule)

### G009 Send an email

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the contact; Tap the send button; Tap the email address
- Remaining steps: Enter the recipient's email address; Confirm the email is sent
- Completion ratio: 0.60
- Credited from later features: G002, G005
- Actions taken: 11
  - act: CustomTouchEvent(state=30b06e104e9597fff0345f11ba4243f1, view=665edefd22b5985e862a59edd6ae3019(MainActivity/CheckBox-Phone stor)) (nav)
  - act: CustomTouchEvent(state=052cc0d5f17b77e8c8142f3ba9eb7a5a, view=3364249f5a9e0dae0741e232cfdb386b(MainActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=468302ac30db598ce8f0bb164d0f8178(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=052cc0d5f17b77e8c8142f3ba9eb7a5a, view=d19f1219669cd74406c0815bc3f36cb4(MainActivity/CheckBox-Phone stor)) (nav)
  - act: CustomTouchEvent(state=30b06e104e9597fff0345f11ba4243f1, view=fd1ec86574f45ef0e1c4a5217499bbe0(MainActivity/CheckBox-Phone stor)) (nav)
  - act: CustomTouchEvent(state=bf97b509b7181a71f04c13ae3b706f1f, view=665edefd22b5985e862a59edd6ae3019(MainActivity/CheckBox-Phone stor)) (nav)
  - act: CustomTouchEvent(state=242b184202f638a5a0b6f4ee855a1af2, view=d19f1219669cd74406c0815bc3f36cb4(MainActivity/CheckBox-Phone stor)) (nav)
  - act: CustomTouchEvent(state=bf97b509b7181a71f04c13ae3b706f1f, view=1efabe49519dc4665b6dbbffb4a4c6ea(MainActivity/RelativeLayout-)) (rule)

### G010 Add contacts

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Groups tab; Tap the group; Enter contact details; Save the contact
- Remaining steps: Tap the '+' icon; Select the contact type
- Completion ratio: 0.67
- Credited from later features: G002
- Actions taken: 11
  - act: CustomTouchEvent(state=35eae45e63b52ed620d88eb960a41d6f, view=337e55c894d75d221a2fac09db0f60fb(MainActivity/TextView-Create a n)) (nav)
  - act: CustomTouchEvent(state=35eae45e63b52ed620d88eb960a41d6f, view=337e55c894d75d221a2fac09db0f60fb(MainActivity/TextView-Create a n)) (nav)
  - act: CustomTouchEvent(state=35eae45e63b52ed620d88eb960a41d6f, view=db1023a1c4b40a99bde98d0d934e225d(MainActivity/EditText-TestCube G)) (nav)
  - act: CustomTouchEvent(state=35eae45e63b52ed620d88eb960a41d6f, view=db1023a1c4b40a99bde98d0d934e225d(MainActivity/EditText-TestCube G)) (nav)
  - act: CustomTouchEvent(state=35eae45e63b52ed620d88eb960a41d6f, view=aa4208af11b5242897595f1fd12dcece(MainActivity/Button-Cancel)) (llm)
  - act: CustomTouchEvent(state=94c3b98556c7429630affa412eaf70f2, view=58eb2ded2fde573e3de29308c0863913(MainActivity/FloatingActionButton-)) (afford_search)
  - act: CustomTouchEvent(state=0cc13438d528e7b70c378c54443cd4ae, view=3364249f5a9e0dae0741e232cfdb386b(MainActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=0cc13438d528e7b70c378c54443cd4ae, view=7e1fb65cd3b0e856988143916a857fd9(MainActivity/EditText-Title)) (rule)

### G011 Send a message

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Contacts app; Navigate to the Groups tab; Tap the group to which you want to send a message; Tap the 'Send' button
- Remaining steps: Enter the message content; Tap the 'Send' button to send the message
- Completion ratio: 0.67
- Credited from later features: G002
- Actions taken: 12
  - act: CustomTouchEvent(state=94c3b98556c7429630affa412eaf70f2, x=858, y=1795) (llm)
  - act: CustomTouchEvent(state=94c3b98556c7429630affa412eaf70f2, x=858, y=1795) (llm)
  - act: CustomTouchEvent(state=94c3b98556c7429630affa412eaf70f2, view=0494671ae40dc88c46784adeb673e604(MainActivity/TextView-Groups)) (llm)
  - act: CustomTouchEvent(state=94c3b98556c7429630affa412eaf70f2, view=0494671ae40dc88c46784adeb673e604(MainActivity/TextView-Groups)) (llm)
  - act: CustomSetTextEvent(state=94c3b98556c7429630affa412eaf70f2, view=2c55da7dcd1fc911bc404a63c177cf74(MainActivity/EditText-Search), text=test) (llm)
  - act: CustomTouchEvent(state=20e26d540c39e6abca13c756cc3be3eb, x=858, y=1732) (llm)
  - act: CustomTouchEvent(state=20e26d540c39e6abca13c756cc3be3eb, x=858, y=1732) (llm)
  - act: CustomTouchEvent(state=20e26d540c39e6abca13c756cc3be3eb, view=0d6fe26769ad0fc2e451fe198db8dfbc(MainActivity/ImageView-)) (rule)

### G012 Sort the contact list

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select 'Name'
- Remaining steps: Tap the overflow menu; Select 'Sort by'; Tap 'Done'
- Completion ratio: 0.25
- Credited from later features: G004
- Actions taken: 8
  - act: CustomTouchEvent(state=e47dc04b4e08f47b17e43a603d88679c, view=114fb90cbcbe4063e5c7e02607de3596(MainActivity/TextView-Contacts)) (nav)
  - act: CustomSetTextEvent(state=14d074f06b4288856fe7e963322f54dd, view=2c55da7dcd1fc911bc404a63c177cf74(MainActivity/EditText-Search), text=test) (rule)
  - act: CustomTouchEvent(state=64868d311dab23db28b6c9e8e8f7b5e5, view=ab689a902fec3d95f9ad72e4b66dd63c(MainActivity/Button-)) (nav)
  - act: CustomTouchEvent(state=beeb7a89182869582edf17385b8bd9eb, view=d350ce93289ba6d4baa2118db6de16d7(MainActivity/TextView-Sort by)) (nav)
  - act: CustomTouchEvent(state=beeb7a89182869582edf17385b8bd9eb, view=d350ce93289ba6d4baa2118db6de16d7(MainActivity/TextView-Sort by)) (nav)
  - act: CustomTouchEvent(state=beeb7a89182869582edf17385b8bd9eb, view=2e03984a91439f80baa2d1d008f17432(MainActivity/RadioButton-Descending)) (nav)
  - act: CustomTouchEvent(state=3feb8dfabc83629c39d3c28a171014bc, view=d350ce93289ba6d4baa2118db6de16d7(MainActivity/TextView-Sort by)) (nav)
  - act: CustomTouchEvent(state=3feb8dfabc83629c39d3c28a171014bc, view=3364249f5a9e0dae0741e232cfdb386b(MainActivity/Button-OK)) (rule)

### G013 Choose

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open Settings; Scroll to 'Manage shown contact fields'; Tap 'Manage shown contact fields'
- Remaining steps: Select 'Visible' from the dropdown; Tap 'Done' to save changes
- Completion ratio: 0.60
- Credited from later features: G002, G006, G007
- Actions taken: 8
  - act: CustomTouchEvent(state=e47dc04b4e08f47b17e43a603d88679c, x=593, y=1133) (llm)
  - act: CustomTouchEvent(state=e47dc04b4e08f47b17e43a603d88679c, x=593, y=1133) (llm)
  - act: CustomTouchEvent(state=e47dc04b4e08f47b17e43a603d88679c, x=586, y=1100) (llm)
  - act: CustomTouchEvent(state=e47dc04b4e08f47b17e43a603d88679c, view=58eb2ded2fde573e3de29308c0863913(MainActivity/FloatingActionButton-)) (afford_search)
  - act: CustomTouchEvent(state=0cc13438d528e7b70c378c54443cd4ae, view=aa4208af11b5242897595f1fd12dcece(MainActivity/Button-Cancel)) (rule)
  - act: CustomTouchEvent(state=e47dc04b4e08f47b17e43a603d88679c, x=586, y=1100) (llm)
  - act: CustomTouchEvent(state=e47dc04b4e08f47b17e43a603d88679c, view=58eb2ded2fde573e3de29308c0863913(MainActivity/FloatingActionButton-)) (afford_search)
  - act: CustomTouchEvent(state=0cc13438d528e7b70c378c54443cd4ae, view=3364249f5a9e0dae0741e232cfdb386b(MainActivity/Button-OK)) (rule)

### G014 Merge duplicate contacts

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the contact list
- Remaining steps: Long-press the contacts to select them; Select the contacts to be merged; Navigate to the 'Merge' option; Select the contacts to merge; Confirm the merge action
- Completion ratio: 0.17
- Actions taken: 9
  - act: CustomTouchEvent(state=e47dc04b4e08f47b17e43a603d88679c, view=114fb90cbcbe4063e5c7e02607de3596(MainActivity/TextView-Contacts)) (heuristic)
  - act: CustomTouchEvent(state=14d074f06b4288856fe7e963322f54dd, view=203db9b1ad82b0290b795a4b7ec28789(MainActivity/TextView-Contacts)) (heuristic)
  - act: CustomTouchEvent(state=14d074f06b4288856fe7e963322f54dd, view=203db9b1ad82b0290b795a4b7ec28789(MainActivity/TextView-Contacts)) (heuristic)
  - act: CustomTouchEvent(state=14d074f06b4288856fe7e963322f54dd, view=2747ef025fbfbdd3fc2d42a2f5cc2414(MainActivity/FloatingActionButton-)) (afford_search)
  - act: LongTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=fe04346708d5a97887f1944fd76ad6c3(EditContactActivity/TextView-Mobile)) (heuristic)
  - act: LongTouchEvent(state=120bbe854b0efd00965ecb4d9f3d70bb, view=fb812fca22b68886dd15bc729744fad3(EditContactActivity/RadioButton-Home Fax)) (heuristic)
  - act: LongTouchEvent(state=a9772a31246c3fe39a9691927a349b14, view=85f91a9b0332e27dfc11133559270814(EditContactActivity/EditText-Number)) (heuristic)
  - act: CustomTouchEvent(state=a9772a31246c3fe39a9691927a349b14, view=776cb7ac2b9f9326ca2278f1ba0b3aeb(EditContactActivity/ImageView-)) (rule)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
