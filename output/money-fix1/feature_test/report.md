# Feature test report: Money Manager Ex

- Started: 2026-08-23 11:21:01
- Finished: 2026-08-23 12:46:22
- Features: 28
- Covered: 4
- Partial: 12
- Dropped (blocked / stuck): 1
- Not present in the app: 0
- Weighted coverage: 45% (mean completion ratio; the headline number)
- Coverage: 14% (features with every guide step matched)
- Stop reason: not recorded
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 17
- Never attempted: 11
- Blocked then recovered on retry: 0
- Blocked still: 0

## Guide vs README-extracted

- Guide features: 28
- README-extracted features: 8
- In both: 5
- Guide-only: 23
- README-only: 3
  - guide-only: GT001 New database
  - guide-only: GT003 Add transaction
  - guide-only: GT004 Edit transaction
  - guide-only: GT005 Filter by date
  - guide-only: GT006 Search transactions
  - guide-only: GT007 Favorite account
  - guide-only: GT008 Manage accounts
  - guide-only: GT010 Budget amount
  - guide-only: GT011 Budget details
  - guide-only: GT012 Delete budget
  - guide-only: GT014 Scheduled transaction
  - guide-only: GT015 Recurring prompt
  - README-only: F001 Complete first-run setup
  - README-only: F003 View and edit transactions
  - README-only: F008 Set up notifications

## Independent ground-truth addendum

- Features not in the guide list: 6
- Matched in this run: 2
- Missed: 4
- Independent features not in the guide list. matched = live journal features with name similarity >= 0.3 (hybrid discovery is the expected source).

## Text-field resolution

- Filled via credential.txt: 0
- Filled via VLM/Gemini: 11
- Unresolved: 0
- Online coverage: 14% (4/28) — live journal self-report (covered / extracted features).
- Offline coverage: 7% (2 covered / 28; 5 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 16% (mean completion ratio).

## Findings

### GT001 New database

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Create a database' option; Select 'New database' from the menu; Tap the 'Create' button to finalize the new database creation
- Remaining steps: Enter a name for the new database
- Completion ratio: 0.80
- Credited from later features: GT004, GT005
- Actions taken: 13
  - act: CustomTouchEvent(state=967325bb19d8b40560a7364d0acb7f45, view=e775d76c9d80720909bf1f0537d19984(PasswordActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, x=44, y=694) (llm)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na)) (llm)
  - act: ScrollEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=19f9c4b484370144fb4bac21c98e5e1b(AccountEditActivity/ScrollView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=8df8e220ff60f4cd5119531be05cd3b2, view=37362f0c98e81a88235637356c0038f7(AccountEditActivity/CheckedTextView-Closed)) (llm)
  - act: CustomTouchEvent(state=19104151282084bed73b61a898862237, x=44, y=594) (llm)
  - act: CustomTouchEvent(state=3137910ef05fcf2015d0bd5dc4a5da99, view=50833023c95487c826ea6c381b28fc69(AccountEditActivity/CheckedTextView-Shares)) (llm)

### GT002 New account

- Status: **partial**
- Reason: Onboarding already finished; main screen is visible.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Account' section in the navigation drawer; Select 'New account' from the account management options; Enter the account name
- Remaining steps: Tap the 'Create' button to finalize the account creation
- Completion ratio: 0.80
- Credited from later features: GT001, GT005, GT007, GT009

### GT003 Add transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the 'Income' or 'Expense' option; Tap on the 'Add a transaction' button; Tap the 'Save' button to add the transaction; Select the date of the transaction; Select the category of the transaction
- Remaining steps: Enter the amount of the transaction
- Completion ratio: 0.83
- Credited from later features: GT004, GT005, GT006
- Actions taken: 7
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=72faf18250cd3c6df446eb3e21594e45(MainActivity/TextView-/storage/e)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=72faf18250cd3c6df446eb3e21594e45(MainActivity/TextView-/storage/e)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=0873a2dd73b366c01020680b19604264, view=9e278810123d6fc7d5b1b145c0345498(MainActivity/CheckedTextView-o)) (heuristic)
  - act: CustomTouchEvent(state=7c2a180aabc77be16cf8bb54941c35cb, view=588e1a5a3bf1f2b4ca0d4a578f0916ca(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (llm)

### GT004 Edit transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the transaction you want to edit in the transaction list.; Select the 'Edit' option from the menu that appears.; Enter the new details for the transaction.; Tap the 'Save' button to update the transaction.
- Remaining steps: Confirm the changes if prompted.
- Completion ratio: 0.80
- Actions taken: 11
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=5685205ee588408fe535752b5b572219(SearchActivity/TextView-TRANSACTIO)) (heuristic)
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, x=32, y=32) (llm)
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=ce9f8bae7c1a3d996903712060ff7906(SearchActivity/TextView-STATUS)) (llm)
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=ce9f8bae7c1a3d996903712060ff7906(SearchActivity/TextView-STATUS)) (llm)
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, x=540, y=540) (llm)
  - act: CustomTouchEvent(state=2446b73b6a11f65f709302aad3cb95a1, view=ce9f8bae7c1a3d996903712060ff7906(SearchActivity/TextView-STATUS)) (llm)
  - act: CustomTouchEvent(state=2446b73b6a11f65f709302aad3cb95a1, view=ce9f8bae7c1a3d996903712060ff7906(SearchActivity/TextView-STATUS)) (llm)
  - act: CustomTouchEvent(state=2446b73b6a11f65f709302aad3cb95a1, view=3d99f9a62783b30bfc02b7a74366a277(SearchActivity/TextView-)) (llm)

### GT005 Filter by date

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the 'Filter by date' option in the navigation drawer.; Select the 'Date' filter option.; Enter the start date in the date picker.; Enter the end date in the date picker.; Tap the 'Apply' button to filter the transaction list by the specified date range.
- Completion ratio: 1.00
- Actions taken: 10
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=f40559004b628e3cc27dcdad85a96df1(SettingsActivity/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=f40559004b628e3cc27dcdad85a96df1(SettingsActivity/TextView-Settings)) (heuristic)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=0da48a853941316ac05626092291c120(SettingsActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=702c74bda4f2d7f4472ae6c040470403(AccountEditActivity/TextView-INITIAL DA)) (heuristic)
  - act: CustomSetTextEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=testcube.mmb) (mandatory_fill)
  - act: CustomSetTextEvent(state=7453afb580064421700926acfa451d2c, view=624b5b32f5baf3cdfd8f063c867d4d5d(AccountEditActivity/EditText-testcube.m), text=2023-01-01) (mandatory_fill)
  - act: CustomTouchEvent(state=74a98cf433e1c4051851ef39bc38be21, view=702c74bda4f2d7f4472ae6c040470403(AccountEditActivity/TextView-INITIAL DA)) (heuristic)

### GT006 Search transactions

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the 'Search transactions' option in the navigation drawer.; Enter the search term in the search bar.; Press the 'Enter' key to execute the search.; Select the desired transaction from the search results.; Tap on the 'Sort' option to sort the transactions.
- Completion ratio: 1.00
- Actions taken: 9
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=1234567890) (mandatory_fill)
  - act: CustomSetTextEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=94e39d333c036b9c6fa7e13c52afa8d4(SearchActivity/EditText-1234567890), text=1234567890) (mandatory_fill)
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=19ee481c4531b725329e5dd41ed6a159(SearchActivity/TextView-Search)) (heuristic)
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=a77ab87c8cb6103cfe2c8747ad2f2a12(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=2cc65d47aaa2d183602e4845ba84f5ae, view=dfb3ee4bfbc79fd337920c5692bd781d(SearchActivity/TextView-Sort by da)) (heuristic)

### GT007 Favorite account

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Select the 'Accounts' section; Tap on the account you want to mark as favorite; Select the 'Favorite' option from the account menu; Confirm the favorite status by tapping 'Save'
- Completion ratio: 1.00
- Actions taken: 6
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (heuristic)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=ccea967a8b318016bd7714c304944e97(AccountEditActivity/TextView-ACCOUNT ST)) (heuristic)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=ccea967a8b318016bd7714c304944e97(AccountEditActivity/TextView-ACCOUNT ST)) (heuristic)

### GT008 Manage accounts

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the account you want to edit; Tap the 'Save' button to update the account; Select the 'Manage accounts' feature; Tap on the 'Accounts' navigation hint
- Remaining steps: Enter the new account details
- Completion ratio: 0.80
- Credited from later features: GT004, GT007, GT013
- Actions taken: 8
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=206b3bb71772a92bb536e53f25173c50(MainActivity/Button-SETTINGS)) (llm)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=0da48a853941316ac05626092291c120(SettingsActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=8e5fdc0331f019f7f39faf901afdd7e3(MainActivity/TextView-your_data_)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=8e5fdc0331f019f7f39faf901afdd7e3(MainActivity/TextView-your_data_)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=edc7fb7fe1766dc6d0be605a14690c32(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (rule)

### GT009 Budget

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the 'Create a budget' option.; Tap on the 'Save' button to finalize the budget setup.; Tap on the 'Open budgets' option in the navigation drawer.; Verify the newly created budget in the 'Budgets' section.
- Remaining steps: Enter the budget name in the input field.
- Completion ratio: 0.80
- Credited from later features: GT001, GT004, GT005, GT010
- Actions taken: 8
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=edc7fb7fe1766dc6d0be605a14690c32(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=1bc77b2100105e9d823d2672d4dbcaa9(MainActivity/TextView-Current da)) (rule)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=1bc77b2100105e9d823d2672d4dbcaa9(MainActivity/TextView-Current da)) (rule)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: CustomSetTextEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=8bcd308b8146e2d2f0591bd37449b85a(AccountEditActivity/EditText-Account nu), text=test_budget_name) (llm)
  - act: CustomTouchEvent(state=326f7772b0ac5e060f5a1e81e385a990, view=b217f2a58290b0b90c1f8423cac6f204(AccountEditActivity/EditText-test_budge)) (heuristic)
  - act: CustomSetTextEvent(state=326f7772b0ac5e060f5a1e81e385a990, view=b217f2a58290b0b90c1f8423cac6f204(AccountEditActivity/EditText-test_budge), text=test_budget_name) (rule)

### GT010 Budget amount

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Navigate to the 'Budget' section; Confirm the changes; Tap on the 'Edit' button next to the budget amount
- Remaining steps: Select the category you want to set a budget for; Enter the new budget amount
- Completion ratio: 0.67
- Credited from later features: GT007, GT013
- Actions taken: 12
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: ScrollEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=19f9c4b484370144fb4bac21c98e5e1b(AccountEditActivity/ScrollView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=8df8e220ff60f4cd5119531be05cd3b2, view=37362f0c98e81a88235637356c0038f7(AccountEditActivity/CheckedTextView-Closed)) (llm)
  - act: CustomTouchEvent(state=19104151282084bed73b61a898862237, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=e0d939b689efde4eefc36e74b2cbadef, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=f3803e0eb64c3e61891bb12cfa320aa3, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=92417842f5b54a8855b1e40e88199d3f, view=44e793bd4cb64fb1c3cc43b013194efd(AccountEditActivity/TextView-SELECT CUR)) (rule)

### GT011 Budget details

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Budget' section in the navigation drawer.; Select 'Budget Details' from the dropdown menu.; Tap on the 'View' button to open the budget details.; Scroll through the budget details to view related transactions.
- Remaining steps: Tap on a specific transaction to view its details.
- Completion ratio: 0.80
- Credited from later features: GT013
- Actions taken: 13
  - act: CustomTouchEvent(state=935626e11ff4d50cf01f0b512b00aaf0, view=82bc37482dfd3c7153bf44f161d7a961(BudgetListActivity/TextView-Budgets)) (heuristic)
  - act: CustomTouchEvent(state=935626e11ff4d50cf01f0b512b00aaf0, view=82bc37482dfd3c7153bf44f161d7a961(BudgetListActivity/TextView-Budgets)) (heuristic)
  - act: CustomTouchEvent(state=935626e11ff4d50cf01f0b512b00aaf0, view=3b5249cd1e960e3fc1d1a8545c5a89a8(BudgetListActivity/ListView-)) (llm)
  - act: CustomTouchEvent(state=935626e11ff4d50cf01f0b512b00aaf0, view=93e5d3bfe3dca356af308af6f7ee822d(BudgetListActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio)) (rule)

### GT012 Delete budget

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Delete' option; Select the 'Budgets' section; Confirm the deletion by tapping 'Yes' on the confirmation dialog
- Remaining steps: Locate and select the budget you want to delete
- Completion ratio: 0.80
- Credited from later features: GT001, GT007
- Actions taken: 9
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=070ef00ba28323861f05979a924d99f9(SearchActivity/TextView-Select Tag)) (llm)
  - act: CustomTouchEvent(state=02888c0f4cc2d525464b94d09d2590c2, view=e9912daba18070a8344abac8585b66c5(TagActivity/FloatingActionButton-)) (heuristic)
  - act: CustomSetTextEvent(state=a305ec2fc8b86b3dfdf3a8e7963b793c, view=c4f0995ee6b9a30e3efe2869541cd1f0(TagActivity/EditText-Tag name), text=testcube.mmb) (rule)
  - act: CustomTouchEvent(state=553675a79e078c5fa8a1d151a6fda738, view=3c7129e47e4799cf7a91a2a4f4a1d27b(TagActivity/Button-OK)) (llm)
  - act: CustomSetTextEvent(state=011a065fc6900cf9dc0ec850cabe84f1, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=1234567890) (rule)
  - act: CustomTouchEvent(state=1712205d726bd34059b054ff7b7ac395, view=e9675520ae190f6731e929bc617799f1(SearchActivity/TextView-Select Pay)) (rule)

### GT013 Budget view options

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap on the 'Budget' navigation hint.; Select 'Change budget view options' from the dropdown menu.; Tap on the 'Budget view options' button.; Select the desired budget view option from the dropdown menu.; Tap on the 'Save' button to apply the selected budget view option.
- Completion ratio: 1.00
- Credited from later features: GT004
- Actions taken: 9
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=206b3bb71772a92bb536e53f25173c50(MainActivity/Button-SETTINGS)) (rule)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=d44405fcb405adc05ad761463a792339(SettingsActivity/TextView-Budget)) (heuristic)
  - act: CustomTouchEvent(state=1d2c8d0e99369d19862285baf984115d, view=1bce12574a887f35292c5a2a2fca3c6d(BudgetSettingsActivity/TextView-Show simpl)) (heuristic)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=1bce12574a887f35292c5a2a2fca3c6d(BudgetSettingsActivity/TextView-Show simpl)) (heuristic)
  - act: CustomTouchEvent(state=1d2c8d0e99369d19862285baf984115d, view=1bce12574a887f35292c5a2a2fca3c6d(BudgetSettingsActivity/TextView-Show simpl)) (heuristic)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=b57e34fd16cbc40f969d64aeb6cc580d(BudgetSettingsActivity/TextView-Budget)) (rule)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=62387459b3851ce330304a4b9a3d0c62(BudgetSettingsActivity/TextView-If checked)) (rule)
  - act: CustomTouchEvent(state=1d2c8d0e99369d19862285baf984115d, view=7bdd1bd4f5746666becd8bac2d52096e(BudgetSettingsActivity/TextView-Use financ)) (rule)

### GT014 Scheduled transaction

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Transactions' section in the main menu.; Tap on the 'Add Transaction' button.; Tap on the 'Save' button to create the recurring transaction.
- Remaining steps: Select 'Recurring' from the transaction type options.; Enter the details for the transaction amount, date, and description.
- Completion ratio: 0.60
- Credited from later features: GT004
- Actions taken: 8
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=206b3bb71772a92bb536e53f25173c50(MainActivity/Button-SETTINGS)) (llm)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=c45abf7e6dd72942f012d88d540bfa20(SettingsActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=d4cca4edf7aebd73360efe1805952df4, view=9057821023ceb097964990fcc95c5854(AboutActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=6648828d391955472ed9c1af01d76d50(SettingsActivity/TextView-Database)) (llm)
  - act: CustomTouchEvent(state=61f5e43370a4d4dae9c32ac580d0d3b9, view=c0de09a88bd075d9af5c2c69f0df1cbf(DatabaseSettingsActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=6648828d391955472ed9c1af01d76d50(SettingsActivity/TextView-Database)) (llm)

### GT015 Recurring prompt

- Status: **partial**
- Reason: The current screen does not provide any actionable steps related to the recurring transaction feature. The screen is an onboarding or initial setup screen for the Money Manager Ex app, and there is no indication that the feature is ready to be used or confirmed.
- Feature source: guide
- Completed steps: Select the due date if prompted; Select the recurring transaction prompt
- Remaining steps: Tap on the 'Recurring' badge; Enter the amount if prompted; Review the details of the transaction; Tap 'Accept' to confirm the due recurring transaction
- Completion ratio: 0.33
- Credited from later features: GT005, GT006

### GT016 Payees

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the 'Save' button to add the payee.; Tap on the 'Payees' option in the navigation drawer.; Select the payee from the list to edit its details.
- Remaining steps: Enter the name of the payee in the text field.; Select the payee type from the dropdown menu.; Enter the bank account details.
- Completion ratio: 0.50
- Credited from later features: GT004, GT005, GT011
- Actions taken: 8
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (rule)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (rule)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=8e5fdc0331f019f7f39faf901afdd7e3(MainActivity/TextView-your_data_)) (rule)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=8e5fdc0331f019f7f39faf901afdd7e3(MainActivity/TextView-your_data_)) (rule)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (rule)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (llm)
  - act: CustomTouchEvent(state=cf48aa7ab880d430170bd8310be910e9, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (rule)

### GT017 Categories

- Status: **partial**
- Reason: Run ended before the feature completed.
- Feature source: guide
- Completed steps: Select the 'Edit' option to modify an existing category.; Tap the 'Save' button to add the category.; Tap on the 'Categories' option in the navigation drawer.; Select the 'Add New Category' option.
- Remaining steps: Enter the name of the new category in the text field.; Enter the new name for the category in the text field.
- Completion ratio: 0.67
- Credited from later features: GT004, GT005
- Actions taken: 4
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, x=33, y=1655) (llm)
  - act: CustomTouchEvent(state=10601b2ee300481c3b0f33bdaa3ac722, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)

### GT018 Built-in report

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Reports' section in the navigation drawer.; Select the 'Built-in report' option from the reports menu.; Wait for the report to load and ensure it is displayed in a visibly different state from the previous screen.
- Completion ratio: 0.00

### GT019 General report

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'report' navigation hint.; Select the 'General report' option from the menu.; Tap on the 'Run a general report' button.; Wait for the report to generate and display the results.
- Completion ratio: 0.00

### GT020 Investments

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Investments' section in the Money Manager Ex app.; Select the 'Track a stock or fund' option.; Enter the name or ticker symbol of the stock or fund you wish to track.; Tap the 'Add' button to save the new investment.; Verify the added investment in the 'Investments' section to ensure it's correctly tracked.
- Completion ratio: 0.00

### GT021 Stock transaction

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Stock' navigation hint.; Select 'Add a stock transaction' from the menu.; Enter the stock symbol.; Enter the number of shares.; Select the date of the transaction.; Enter the price per share.
- Completion ratio: 0.00

### GT022 Fixed assets

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Assets' section in the navigation drawer.; Select the 'Fixed Assets' option from the assets menu.; Enter the name of the fixed asset in the input field.; Tap on the 'Add' button to save the new fixed asset.; Verify the fixed asset is listed in the assets section.
- Completion ratio: 0.00

### GT023 Currencies

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Currencies' option in the main menu.; Select the currency you want to manage.; Enter the new currency rate if needed.; Tap on the 'Save' button to update the currency rate.; Verify the updated currency rate in the app's currency list.
- Completion ratio: 0.00

### GT024 Sync

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Money Manager Ex app; Navigate to the main menu; Select the 'Settings' option; Scroll down to find the 'Sync' settings; Tap on 'Sync' settings; Select 'Open sync settings'
- Completion ratio: 0.00

### GT025 Database password

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Settings' menu item in the top navigation bar.; Select 'Database Settings' from the settings menu.; Tap on 'Change Database Password' to proceed.; Enter the new database password in the password field.; Re-enter the new database password in the confirmation field.; Tap on the 'Save' button to set the new database password.
- Completion ratio: 0.00

### GT026 Fingerprint lock

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Money Manager Ex app; Navigate to the settings menu; Select 'Security' from the settings menu; Select 'Fingerprint lock'; Enable fingerprint lock; Confirm the fingerprint lock setup
- Completion ratio: 0.00

### GT027 Import export

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Import or export a file' option in the navigation drawer.; Select 'Import' from the dropdown menu.; Enter the path to the QIF or CSV file you want to import.; Tap the 'Open' button to select the file.; Wait for the file to be imported and the app to update the state.; Verify the imported data by checking the transaction list.
- Completion ratio: 0.00

### GT028 Settings

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap the 'Settings' option in the app's main menu.; Select the 'Settings' option from the menu.; Open the settings menu by tapping the 'Settings' option.; Navigate to the 'Settings' section by tapping the 'Settings' option.; Access the app's settings by tapping the 'Settings' option.
- Completion ratio: 0.00

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
