# Feature test report: Fossify Contacts

- Started: 2026-10-25 15:29:51
- Finished: 2026-10-25 16:28:22
- Features: 14
- Covered: 8
- Partial: 6
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 80% (mean completion ratio; the headline number)
- Coverage: 57% (features with every guide step matched)
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

- Filled via credential.txt: 26
- Filled via VLM/Gemini: 12
- Unresolved: 0
- Online coverage: 57% (8/14) — live journal self-report (covered / extracted features).
- Offline coverage: not computed (no ground-truth JSON).

## Findings

### G001 Create a contact

- Status: **covered**
- Reason: Covered by shared-flow reuse of C008.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the app; Tap the save button; Tap the '+' floating action button; Enter the contact's name; Select the contact type; Enter the contact's phone number
- Completion ratio: 1.00
- Credited from later features: G002
- Actions taken: 28
  - act: CustomTouchEvent(state=6435f185c932644e3e6a2448c8ab358a, view=289499ba1851752845c94824c20917d8(MainActivity/RadioButton-First name)) (llm)
  - act: CustomTouchEvent(state=3feb8dfabc83629c39d3c28a171014bc, view=cbb2ddf22c92d5aa94fd326a6c19ac10(MainActivity/RadioButton-Date creat)) (nav)
  - act: CustomTouchEvent(state=6435f185c932644e3e6a2448c8ab358a, view=3364249f5a9e0dae0741e232cfdb386b(MainActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=461fb4b6332ac3f67dc293ce64f48fe8, view=ab689a902fec3d95f9ad72e4b66dd63c(MainActivity/Button-)) (nav)
  - act: CustomTouchEvent(state=6435f185c932644e3e6a2448c8ab358a, view=5d99c0ffcc14882ba299cbf43ecab3ea(MainActivity/RadioButton-Middle nam)) (rule)
  - act: CustomTouchEvent(state=461fb4b6332ac3f67dc293ce64f48fe8, view=b38643bbd52666344ca4763082de0450(MainActivity/TextView-Favorites)) (nav)
  - act: CustomTouchEvent(state=cf99d3def7e49cb054165ce46e746722, view=114fb90cbcbe4063e5c7e02607de3596(MainActivity/TextView-Contacts)) (nav)
  - act: CustomTouchEvent(state=ade4b4701e17927d2d164eb6f092fc3f, view=2747ef025fbfbdd3fc2d42a2f5cc2414(MainActivity/FloatingActionButton-)) (nav)

### G002 Add multiple phone numbers

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the contact editor; Tap the '+' beside the phone section; Enter the first phone number; Enter the second phone number
- Completion ratio: 1.00
- Credited from later features: G003
- Actions taken: 11
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=e5a8065e1f9e8a606019f3f9b9eec818(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=e5a8065e1f9e8a606019f3f9b9eec818(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=7cf851b94ba0f40ad1f207b351e45617(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=550c1ff8967998d1201f9e51306906df(EditContactActivity/TextView-Unknown)) (nav)
  - act: CustomTouchEvent(state=906718ee03778018e11f8abae4727896, view=f2f76e78750fa76296ecef034e813051(EditContactActivity/TextView-2026)) (llm)
  - act: CustomTouchEvent(state=b98464ad0eba83b14296ae84fbeb4f4a, view=02a8107b7a8a1266b0f5a032d52b979e(EditContactActivity/Button-OK)) (rule)
  - act: CustomSetTextEvent(state=461fb4b6332ac3f67dc293ce64f48fe8, view=2c55da7dcd1fc911bc404a63c177cf74(MainActivity/EditText-Search), text=test) (mandatory_fill)
  - act: CustomSetTextEvent(state=2218f642a88b894407c02fe704761ff8, view=5bd992f8737cef6c5f354f39d4ae6ed2(MainActivity/EditText-test), text=test) (mandatory_fill)

### G003 Add postal addresses

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the contact editor; tap the "+" beside the address section
- Completion ratio: 1.00
- Actions taken: 4
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=6336e7794cca3231ba87a804e4b6c694(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=5c7429df2d1ae0c32b72a5fed686dac8, view=5a82e84abe3d2c67037dfe982cbaab75(MainActivity/TextView-Settings)) (rule)
  - act: CustomTouchEvent(state=69ef2d4147e1c19e0a7dcbe13f8a6e98, view=43a83a665340ca3aabc29387dcb34c96(SettingsActivity/TextView-On contact)) (heuristic)
  - act: CustomTouchEvent(state=69ef2d4147e1c19e0a7dcbe13f8a6e98, view=78edb9b5da7db3e4c3fc3c9f4a646582(SettingsActivity/TextView-Look & fee)) (heuristic)

### G004 Add the organisation

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Tap on the 'Add' button to initiate the contact creation process.; Tap on the 'Save' button to add the organisation to the contact.; Verify that the organisation is now listed under the contact's details.
- Remaining steps: Select the 'organisation' option from the dropdown menu.; Enter the name of the organisation in the provided field.; Scroll to the 'job' section and select the appropriate job title.
- Completion ratio: 0.50
- Credited from later features: G006
- Actions taken: 35
  - act: CustomTouchEvent(state=461fb4b6332ac3f67dc293ce64f48fe8, view=137ceb59ccd8fb47c3449fadcf978468(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=cf99d3def7e49cb054165ce46e746722, view=4ff71f874aaeb6fa487625dafd7e241b(MainActivity/FloatingActionButton-)) (nav)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=93652991c50dc5e9b7b2cb71377719ab(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=93652991c50dc5e9b7b2cb71377719ab(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=93652991c50dc5e9b7b2cb71377719ab(MainActivity/LinearLayout-)) (afford_search)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=93652991c50dc5e9b7b2cb71377719ab(MainActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=9ea21e9cca0613387829726eef61c7b5(MainActivity/TextView-No contact)) (llm)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=3364249f5a9e0dae0741e232cfdb386b(MainActivity/Button-OK)) (rule)

### G005 Add notes

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Tap on the contact you want to add notes to; Tap the save button to add the notes
- Remaining steps: Scroll to the notes field; Enter the notes you want to add
- Completion ratio: 0.50
- Credited from later features: G004
- Actions taken: 35
  - act: CustomTouchEvent(state=cf99d3def7e49cb054165ce46e746722, view=7c5da58f4266a7605d93216019981812(MainActivity/TextView-No contact)) (nav)
  - act: CustomTouchEvent(state=cf99d3def7e49cb054165ce46e746722, view=7c5da58f4266a7605d93216019981812(MainActivity/TextView-No contact)) (nav)
  - act: CustomTouchEvent(state=cf99d3def7e49cb054165ce46e746722, view=4ff71f874aaeb6fa487625dafd7e241b(MainActivity/FloatingActionButton-)) (nav)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=9ea21e9cca0613387829726eef61c7b5(MainActivity/TextView-No contact)) (nav)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=9ea21e9cca0613387829726eef61c7b5(MainActivity/TextView-No contact)) (nav)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=93652991c50dc5e9b7b2cb71377719ab(MainActivity/LinearLayout-)) (afford_search)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=9ea21e9cca0613387829726eef61c7b5(MainActivity/TextView-No contact)) (nav)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=3364249f5a9e0dae0741e232cfdb386b(MainActivity/Button-OK)) (rule)

### G006 Edit a contact

- Status: **covered**
- Reason: Covered by shared-flow reuse of C003.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Open the contact; Tap the edit (pencil) icon; Enter the new name in the name field; Tap the save icon to update the contact; Verify the contact details are updated
- Completion ratio: 1.00
- Actions taken: 6
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=203db9b1ad82b0290b795a4b7ec28789(MainActivity/TextView-Contacts)) (nav)
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=203db9b1ad82b0290b795a4b7ec28789(MainActivity/TextView-Contacts)) (nav)
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=fc16bc34cec818e1f77e7118e60d0d49(MainActivity/TextView-No contact)) (nav)
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=6336e7794cca3231ba87a804e4b6c694(MainActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=5c7429df2d1ae0c32b72a5fed686dac8, view=5a82e84abe3d2c67037dfe982cbaab75(MainActivity/TextView-Settings)) (rule)
  - act: CustomTouchEvent(state=69ef2d4147e1c19e0a7dcbe13f8a6e98, view=43a83a665340ca3aabc29387dcb34c96(SettingsActivity/TextView-On contact)) (heuristic)

### G007 Mark a contact

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open the contact; Tap the star icon in the toolbar; or long-press the contact in the list; The contact is now marked as a favourite
- Remaining steps: Select the 'Mark' option from the context menu; Confirm the marking by tapping the 'Mark' button
- Completion ratio: 0.60
- Credited from later features: G006
- Actions taken: 42
  - act: CustomTouchEvent(state=cf99d3def7e49cb054165ce46e746722, view=9185a9708d43b473f0de85026d1b9c1b(MainActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=c47755aa129a5056a41f210d8d23c095, view=114fb90cbcbe4063e5c7e02607de3596(MainActivity/TextView-Contacts)) (nav)
  - act: CustomTouchEvent(state=3e91ae9593917acf22e85234a95a35ce, view=203db9b1ad82b0290b795a4b7ec28789(MainActivity/TextView-Contacts)) (nav)
  - act: CustomTouchEvent(state=3e91ae9593917acf22e85234a95a35ce, view=203db9b1ad82b0290b795a4b7ec28789(MainActivity/TextView-Contacts)) (nav)
  - act: CustomTouchEvent(state=3e91ae9593917acf22e85234a95a35ce, view=2747ef025fbfbdd3fc2d42a2f5cc2414(MainActivity/FloatingActionButton-)) (afford_search)
  - act: CustomSetTextEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=439dfdb3cc0765cabed5de0aceb14508(EditContactActivity/AutoCompleteTextView-Surname), text=Rivera) (nav)
  - act: CustomTouchEvent(state=4ad5a1fe54a80f8cd9f6b950b4a7d6ff, view=7435c31b0dbb7c0bfce14ee81fb92d11(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=4ad5a1fe54a80f8cd9f6b950b4a7d6ff, view=3d8fdc89e3bfbd8646c68fd796db1288(EditContactActivity/ImageView-)) (rule)

### G008 Call a contact

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the contact; tap the phone number (or the call icon beside it); the dialler is opened with the number
- Completion ratio: 1.00
- Actions taken: 6
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=fc16bc34cec818e1f77e7118e60d0d49(MainActivity/TextView-No contact)) (nav)
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=0ec021ed99663aeba9a76bffb0421895(MainActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=46ac1cbd5e80666829184c5238ef3854, view=b38643bbd52666344ca4763082de0450(MainActivity/TextView-Favorites)) (llm)
  - act: CustomTouchEvent(state=79db178435d1e6475f5f9db31917be3b, view=114fb90cbcbe4063e5c7e02607de3596(MainActivity/TextView-Contacts)) (nav)
  - act: CustomTouchEvent(state=040bcab3c57b1c751287031675bf6e7e, view=2747ef025fbfbdd3fc2d42a2f5cc2414(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=fe04346708d5a97887f1944fd76ad6c3(EditContactActivity/TextView-Mobile)) (heuristic)

### G009 Send an email

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the contact; Tap the email address; Select the email icon; Enter the recipient's email address; Tap the send button
- Completion ratio: 1.00
- Credited from later features: G001
- Actions taken: 18
  - act: CustomTouchEvent(state=169de02ec2e5df210b1fb7360094a688, view=02a8107b7a8a1266b0f5a032d52b979e(EditContactActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=95c6791349e42de1b3d0c5fd7a19db21, view=7cf851b94ba0f40ad1f207b351e45617(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=95c6791349e42de1b3d0c5fd7a19db21, view=7cf851b94ba0f40ad1f207b351e45617(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=95c6791349e42de1b3d0c5fd7a19db21, view=dcc3eda97ce46cce32acfa4fe029ed0b(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=3736b7985bbbccebc0a3c5e3408cb1df, view=7cf851b94ba0f40ad1f207b351e45617(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=3736b7985bbbccebc0a3c5e3408cb1df, view=7cf851b94ba0f40ad1f207b351e45617(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=3736b7985bbbccebc0a3c5e3408cb1df, view=dcc3eda97ce46cce32acfa4fe029ed0b(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=3736b7985bbbccebc0a3c5e3408cb1df, view=6ab01751f5d9aa94f0c6f5b163ef6e7a(EditContactActivity/EditText-Email)) (rule)

### G010 Add contacts

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the 'Add' button; Tap the 'Save' button; Open the Groups tab; Select the contact group; Tap the group; Enter the contact information
- Completion ratio: 1.00
- Credited from later features: G001, G002, G006, G007, G011
- Actions taken: 10
  - act: CustomTouchEvent(state=3736b7985bbbccebc0a3c5e3408cb1df, view=f10ac85c6c34624f12b2a26354c29bfc(EditContactActivity/ImageView-)) (nav)
  - act: CustomTouchEvent(state=3736b7985bbbccebc0a3c5e3408cb1df, view=36fc3fe99d31afc5c5a845a5d7c5230b(EditContactActivity/TextView-Home)) (afford_search)
  - act: CustomTouchEvent(state=8eb8e9d488975bfa2b14490db6ea91d9, view=821ba764bb08809cb26c2e874378a388(EditContactActivity/RadioButton-Custom)) (llm)
  - act: CustomTouchEvent(state=d41b80a6def74cf235c0b66930315bb2, view=192b65f5e8d17adf1617a50886a0a692(EditContactActivity/Button-Cancel)) (llm)
  - act: CustomTouchEvent(state=3736b7985bbbccebc0a3c5e3408cb1df, view=8bdb67e0e302dce8526b361e43b8bafa(EditContactActivity/TextView-Home)) (nav)
  - act: CustomTouchEvent(state=abebb97be07570c9158f8c943d62c85a, view=6032da0eef076ee9d2937a78388d0cd2(EditContactActivity/RadioButton-Work)) (llm)
  - act: CustomTouchEvent(state=de19d6abd61edc34d00cc9573832876f, view=3d8fdc89e3bfbd8646c68fd796db1288(EditContactActivity/ImageView-)) (rule)
  - act: CustomSetTextEvent(state=461fb4b6332ac3f67dc293ce64f48fe8, view=2c55da7dcd1fc911bc404a63c177cf74(MainActivity/EditText-Search), text=test) (mandatory_fill)

### G011 Send a message

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the Groups tab; Tap the group; Tap the send icon; Enter the message; Tap the send button
- Completion ratio: 1.00
- Credited from later features: G001
- Actions taken: 16
  - act: CustomTouchEvent(state=e7df9d4b09821fdcd86cf93644c064fd, view=0494671ae40dc88c46784adeb673e604(MainActivity/TextView-Groups)) (llm)
  - act: CustomTouchEvent(state=e7df9d4b09821fdcd86cf93644c064fd, view=0494671ae40dc88c46784adeb673e604(MainActivity/TextView-Groups)) (llm)
  - act: CustomSetTextEvent(state=e7df9d4b09821fdcd86cf93644c064fd, view=5bd992f8737cef6c5f354f39d4ae6ed2(MainActivity/EditText-test), text=test) (llm)
  - act: CustomSetTextEvent(state=e7df9d4b09821fdcd86cf93644c064fd, view=5bd992f8737cef6c5f354f39d4ae6ed2(MainActivity/EditText-test), text=test) (llm)
  - act: CustomTouchEvent(state=e7df9d4b09821fdcd86cf93644c064fd, view=0ec021ed99663aeba9a76bffb0421895(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=e7df9d4b09821fdcd86cf93644c064fd, view=0ec021ed99663aeba9a76bffb0421895(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=e7df9d4b09821fdcd86cf93644c064fd, view=b38643bbd52666344ca4763082de0450(MainActivity/TextView-Favorites)) (llm)
  - act: CustomTouchEvent(state=971dbda460ecc70d971180289be11541, view=0d6fe26769ad0fc2e451fe198db8dfbc(MainActivity/ImageView-)) (rule)

### G012 Sort the contact list

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Select 'Name'; Confirm the contact list is sorted by name
- Remaining steps: Tap the overflow menu; Select 'Sort by'
- Completion ratio: 0.50
- Credited from later features: G004, G006
- Actions taken: 34
  - act: CustomTouchEvent(state=461fb4b6332ac3f67dc293ce64f48fe8, view=0ec021ed99663aeba9a76bffb0421895(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=461fb4b6332ac3f67dc293ce64f48fe8, view=0ec021ed99663aeba9a76bffb0421895(MainActivity/ImageView-)) (heuristic)
  - act: ScrollEvent(state=461fb4b6332ac3f67dc293ce64f48fe8, view=1583de512dd84d6832f9fe22a1641968(MainActivity/b-), direction=up) (heuristic)
  - act: CustomTouchEvent(state=461fb4b6332ac3f67dc293ce64f48fe8, view=3b7cd269ac3d3a0567f9e8252e2aeaa4(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=cf99d3def7e49cb054165ce46e746722, view=1a0ad0c481a20c5cbe8270999d234b16(MainActivity/TextView-Add favori)) (nav)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=9ea21e9cca0613387829726eef61c7b5(MainActivity/TextView-No contact)) (nav)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=9ea21e9cca0613387829726eef61c7b5(MainActivity/TextView-No contact)) (nav)
  - act: CustomTouchEvent(state=f075a194e79d03edaae07b1d8425f0ad, view=3364249f5a9e0dae0741e232cfdb386b(MainActivity/Button-OK)) (rule)

### G013 Choose

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open the app; Tap on the 'Settings' icon; Select 'Manage shown contact fields'
- Remaining steps: Tap on the 'Visible' option; Select the desired field to change its visibility; Tap on 'Save' to apply changes
- Completion ratio: 0.50
- Credited from later features: G002, G003, G006
- Actions taken: 35
  - act: CustomTouchEvent(state=cf99d3def7e49cb054165ce46e746722, view=ab689a902fec3d95f9ad72e4b66dd63c(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=231088c6487c42608f9f2968e6d6a968, view=c981bfc211f759477fde9ecfbf9486d8(MainActivity/RadioButton-First name)) (llm)
  - act: CustomTouchEvent(state=231088c6487c42608f9f2968e6d6a968, view=5f28da944055c9f56e71f8cdfddac927(MainActivity/RadioButton-Surname)) (heuristic)
  - act: CustomTouchEvent(state=d747964a8496fa6735b4ccb2e805a028, view=f910e58b243f9cf7444d36a3a2f7654a(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=d747964a8496fa6735b4ccb2e805a028, view=f910e58b243f9cf7444d36a3a2f7654a(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=d747964a8496fa6735b4ccb2e805a028, view=289499ba1851752845c94824c20917d8(MainActivity/RadioButton-First name)) (llm)
  - act: CustomTouchEvent(state=231088c6487c42608f9f2968e6d6a968, view=5d99c0ffcc14882ba299cbf43ecab3ea(MainActivity/RadioButton-Middle nam)) (llm)
  - act: CustomTouchEvent(state=ca3420d975b8d46b0cd867f92761a80f, view=3364249f5a9e0dae0741e232cfdb386b(MainActivity/Button-OK)) (rule)

### G014 Merge duplicate contacts

- Status: **partial**
- Reason: Retry round 3; budget remains.
- Feature source: guide
- Completed steps: Open the contact list; Scroll down to find the contact you want to merge; Long-press the contact you want to merge; Select the contact you want to merge with
- Remaining steps: Select the 'Merge' option from the menu; Confirm the merge action
- Completion ratio: 0.67
- Credited from later features: G005, G006, G007
- Actions taken: 30
  - act: CustomTouchEvent(state=ee3ca20a8920e34f795fa2586d9ed759, view=203db9b1ad82b0290b795a4b7ec28789(MainActivity/TextView-Contacts)) (nav)
  - act: CustomTouchEvent(state=ee3ca20a8920e34f795fa2586d9ed759, view=2747ef025fbfbdd3fc2d42a2f5cc2414(MainActivity/FloatingActionButton-)) (afford_search)
  - act: CustomSetTextEvent(state=58de5a58f9d31ff23ef9267595b0ce44, view=e9d85afb583e0d70699ab56ac16ba404(EditContactActivity/AutoCompleteTextView-First name), text=TestCube List) (llm)
  - act: CustomSetTextEvent(state=798a4f408c98c947709c0532f91f72bf, view=439dfdb3cc0765cabed5de0aceb14508(EditContactActivity/AutoCompleteTextView-Surname), text=Rivera) (llm)
  - act: CustomSetTextEvent(state=2600697c108ec094583b5ef2284e46bf, view=e6b1c6022b26c6027183ac192897e784(EditContactActivity/AutoCompleteTextView-TestCube L), text=TestCube List) (llm)
  - act: CustomSetTextEvent(state=2600697c108ec094583b5ef2284e46bf, view=e6b1c6022b26c6027183ac192897e784(EditContactActivity/AutoCompleteTextView-TestCube L), text=TestCube List) (llm)
  - act: CustomTouchEvent(state=2600697c108ec094583b5ef2284e46bf, view=776cb7ac2b9f9326ca2278f1ba0b3aeb(EditContactActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=cf99d3def7e49cb054165ce46e746722, view=6336e7794cca3231ba87a804e4b6c694(MainActivity/ImageView-)) (heuristic)

## Shared flows detected

2 reuse(s); 8 action(s) skipped by not re-executing a known terminal flow.

- `G006` reused `C003` (from G003), skipped 4 action(s)
- `G001` reused `C008` (from G008), skipped 4 action(s)

See `session.json` and `log.md` in this folder for the full trace.
