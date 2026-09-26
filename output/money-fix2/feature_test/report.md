# Feature test report: Money Manager Ex

- Started: 2026-08-23 13:02:36
- Finished: 2026-08-23 13:50:59
- Features: 28
- Covered: 11
- Partial: 17
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 75% (mean completion ratio; the headline number)
- Coverage: 39% (features with every guide step matched)
- Stop reason: all_features_done
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 28
- Never attempted: 0
- Blocked then recovered on retry: 0
- Blocked still: 0

## Guide vs README-extracted

- Guide features: 28
- README-extracted features: 3
- In both: 1
- Guide-only: 27
- README-only: 2
  - guide-only: GT001 New database
  - guide-only: GT002 New account
  - guide-only: GT003 Add transaction
  - guide-only: GT004 Edit transaction
  - guide-only: GT005 Filter by date
  - guide-only: GT006 Search transactions
  - guide-only: GT007 Favorite account
  - guide-only: GT008 Manage accounts
  - guide-only: GT009 Budget
  - guide-only: GT010 Budget amount
  - guide-only: GT011 Budget details
  - guide-only: GT012 Delete budget
  - README-only: F001 Complete first-run setup
  - README-only: F002 Create or open a database

## Independent ground-truth addendum

- Features not in the guide list: 6
- Matched in this run: 2
- Missed: 4
- Independent features not in the guide list. matched = live journal features with name similarity >= 0.3 (hybrid discovery is the expected source).

## Text-field resolution

- Filled via credential.txt: 16
- Filled via VLM/Gemini: 18
- Unresolved: 0
- Online coverage: 39% (11/28) — live journal self-report (covered / extracted features).
- Offline coverage: 29% (8 covered / 28; 8 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 39% (mean completion ratio).

## Findings

### GT001 New database

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap on the 'Create a database' option; Select the 'New database' feature; Enter a name for the new database; Tap the 'Create' button to finalize the new database creation
- Completion ratio: 1.00
- Credited from later features: GT004
- Actions taken: 14
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomSetTextEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=testcube.mmb) (mandatory_fill)
  - act: CustomSetTextEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=testcube.mmb) (mandatory_fill)
  - act: CustomTouchEvent(state=7453afb580064421700926acfa451d2c, x=55, y=1326) (llm)
  - act: CustomTouchEvent(state=8df8e220ff60f4cd5119531be05cd3b2, view=37362f0c98e81a88235637356c0038f7(AccountEditActivity/CheckedTextView-Closed)) (llm)
  - act: CustomTouchEvent(state=4443d9f96ebd7d55798308a79db46cf5, x=55, y=1267) (llm)
  - act: CustomTouchEvent(state=bca8df489aae4d3086ef3b64b8e319e9, view=fbb40af8f27338c49b8f6301d3d130a3(AccountEditActivity/CheckedTextView-Closed)) (llm)
  - act: CustomTouchEvent(state=4443d9f96ebd7d55798308a79db46cf5, x=55, y=1267) (llm)

### GT002 New account

- Status: **partial**
- Reason: Onboarding already finished; main screen is visible.
- Feature source: guide
- Completed steps: Select 'New account' from the account options; Open the Money Manager Ex app; Tap on the 'Account' section in the navigation drawer
- Remaining steps: Enter the account name in the input field; Tap on the 'Create' button to finalize the account creation
- Completion ratio: 0.60
- Credited from later features: GT001, GT004, GT005

### GT003 Add transaction

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the 'Add a transaction' option in the main menu.; Enter the amount of the transaction in the 'Amount' field.; Select the type of transaction (Income or Expense) from the dropdown.; Enter the description of the transaction in the 'Description' field.; Tap on the 'Save' button to add the transaction.; Verify the transaction is added to the list of transactions.
- Completion ratio: 1.00
- Actions taken: 6
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=1) (mandatory_fill)
  - act: CustomSetTextEvent(state=8b9e49f1d3e5df3e323c655f20d225d7, view=20f6bef3daf0779850c91d4714ded36c(SearchActivity/EditText-1), text=test) (mandatory_fill)
  - act: CustomSetTextEvent(state=99d5704a83d0dec9c9b70f7a91a5179b, view=fd5cbb3cc4538582826fa73daa51c2f6(SearchActivity/EditText-test), text=Saimon Bhuiyan's salary payment) (mandatory_fill)
  - act: CustomTouchEvent(state=4abc0729c74df71d97cfef5e786514c3, view=5685205ee588408fe535752b5b572219(SearchActivity/TextView-TRANSACTIO)) (heuristic)
  - act: CustomTouchEvent(state=4abc0729c74df71d97cfef5e786514c3, view=5685205ee588408fe535752b5b572219(SearchActivity/TextView-TRANSACTIO)) (heuristic)

### GT004 Edit transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Navigate to the Transactions section; Select the transaction you want to edit; Tap on the 'Edit' option
- Remaining steps: Make the necessary changes to the transaction; Confirm the changes and save
- Completion ratio: 0.67
- Credited from later features: GT001
- Actions taken: 11
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=bb7c7972e5c4d268205937de196dc0ee(AccountEditActivity/EditText-Notes)) (nav)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=bb7c7972e5c4d268205937de196dc0ee(AccountEditActivity/EditText-Notes)) (nav)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=79b4842b3f7fa17e6fae046cda8602bd(AccountEditActivity/EditText-Access inf)) (nav)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=79b4842b3f7fa17e6fae046cda8602bd(AccountEditActivity/EditText-Access inf)) (nav)
  - act: CustomSetTextEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=a05dca21723f161e9bb0cb7a5c0c274a(AccountEditActivity/EditText-Website), text=https://www.example.com) (llm)
  - act: CustomTouchEvent(state=8cb1d538d801cf12551e1ae18861550d, view=bb7c7972e5c4d268205937de196dc0ee(AccountEditActivity/EditText-Notes)) (nav)
  - act: CustomTouchEvent(state=8cb1d538d801cf12551e1ae18861550d, view=74a93b20fe872e1ae9ec33afdd0c5493(AccountEditActivity/Button-)) (rule)

### GT005 Filter by date

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Transactions' section; Select 'Filter transactions by date'; Enter the start date in the date range field; Enter the end date in the date range field; Tap the 'Apply' button to filter the transaction list
- Completion ratio: 1.00
- Actions taken: 8
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (heuristic)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=508d1e40ea5181d3f1de495cbdcb0021, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=508d1e40ea5181d3f1de495cbdcb0021, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=508d1e40ea5181d3f1de495cbdcb0021, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=1234567890) (mandatory_fill)
  - act: CustomSetTextEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=94e39d333c036b9c6fa7e13c52afa8d4(SearchActivity/EditText-1234567890), text=1234567890) (mandatory_fill)
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=5685205ee588408fe535752b5b572219(SearchActivity/TextView-TRANSACTIO)) (heuristic)

### GT006 Search transactions

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the 'Search transactions' option in the navigation drawer.; Enter the search term in the search bar.; Press the 'Enter' key to execute the search.; Select the desired transaction from the search results.; Tap on the 'Sort' option to arrange the transactions as needed.
- Completion ratio: 1.00
- Actions taken: 9
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=123456) (mandatory_fill)
  - act: CustomSetTextEvent(state=2710028214d1f891b43f7e200926c58c, view=7d271f8c77848c2163f5ea057f0887f7(SearchActivity/EditText-123456), text=123456) (mandatory_fill)
  - act: CustomTouchEvent(state=2710028214d1f891b43f7e200926c58c, view=19ee481c4531b725329e5dd41ed6a159(SearchActivity/TextView-Search)) (heuristic)
  - act: CustomTouchEvent(state=2710028214d1f891b43f7e200926c58c, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=2710028214d1f891b43f7e200926c58c, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=a77ab87c8cb6103cfe2c8747ad2f2a12(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=2cc65d47aaa2d183602e4845ba84f5ae, view=dfb3ee4bfbc79fd337920c5692bd781d(SearchActivity/TextView-Sort by da)) (heuristic)

### GT007 Favorite account

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Navigate to the Accounts section; Tap on the 'Favorite' option; Select the account you want to mark as favorite
- Remaining steps: Confirm the favorite status by tapping the confirmation button
- Completion ratio: 0.80
- Credited from later features: GT001, GT004
- Actions taken: 13
  - act: CustomTouchEvent(state=878dad5a22919e5ee516f44c3956487e, view=70d66a1dadce077c8e0c676fd6e7c915(MainActivity/CheckedTextView-j)) (heuristic)
  - act: CustomTouchEvent(state=543b7238bd83027faadc89f15014a436, view=fda3873467a3163a8e0074918cc2cda5(MainActivity/TextView-Investment)) (rule)
  - act: CustomTouchEvent(state=543b7238bd83027faadc89f15014a436, view=fda3873467a3163a8e0074918cc2cda5(MainActivity/TextView-Investment)) (rule)
  - act: CustomTouchEvent(state=543b7238bd83027faadc89f15014a436, view=fe56a52c8e60ef7173de78fd65b4ccff(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=543b7238bd83027faadc89f15014a436, view=fe56a52c8e60ef7173de78fd65b4ccff(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=543b7238bd83027faadc89f15014a436, view=32e7fa55069bfd5828b54dd39ded136e(MainActivity/TextView-Add Subcat)) (rule)
  - act: CustomSetTextEvent(state=4121c51452ce2f20b26a4a6e841a156e, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor), text=no) (rule)
  - act: CustomTouchEvent(state=926d079f4bc496f10abe6952edfe7475, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (rule)

### GT008 Manage accounts

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Accounts' option in the navigation drawer.; Tap the 'Save' button to update the account details.; Select the account you wish to edit from the account list.
- Remaining steps: Tap on the 'Edit' button next to the selected account.; Enter the new details for the account as required.
- Completion ratio: 0.60
- Credited from later features: GT003, GT004
- Actions taken: 11
  - act: CustomTouchEvent(state=878dad5a22919e5ee516f44c3956487e, view=c2105826f90b3378092fd0438d21caea(MainActivity/TextView-Homeneeds)) (heuristic)
  - act: CustomTouchEvent(state=5537ba717d0bddd4d3dfaba519eaa74a, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor)) (llm)
  - act: CustomSetTextEvent(state=2f77687863312998838a7d801cd171e3, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor), text=no) (rule)
  - act: CustomSetTextEvent(state=a6ef0c5b39d8412fc7976dfda003cf8b, view=61ac53568a1b845675ac5cd5df9c84e5(MainActivity/EditText-no), text=your_email@gmail.com) (rule)
  - act: CustomSetTextEvent(state=631e172ff71a4ca5a0f13b8b0d5c3ff4, view=8b489210db6b50834e6b403e9c1ede24(MainActivity/EditText-your_email), text=your_email@gmail.com) (rule)
  - act: CustomSetTextEvent(state=631e172ff71a4ca5a0f13b8b0d5c3ff4, view=8b489210db6b50834e6b403e9c1ede24(MainActivity/EditText-your_email), text=your_email@gmail.com) (llm)
  - act: CustomTouchEvent(state=631e172ff71a4ca5a0f13b8b0d5c3ff4, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (rule)

### GT009 Budget

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Budgets' section in the navigation drawer.; Tap on the 'Create a budget' option.; Tap on the 'Save' button to finalize the budget setup.; Select the category for the budget.; Set the budget amount.
- Remaining steps: Enter the budget name in the input field.
- Completion ratio: 0.83
- Credited from later features: GT003, GT010
- Actions taken: 9
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=d44405fcb405adc05ad761463a792339(SettingsActivity/TextView-Budget)) (heuristic)
  - act: CustomTouchEvent(state=1d2c8d0e99369d19862285baf984115d, view=e763328a8146b453f52a744eba4a137c(BudgetSettingsActivity/TextView-If checked)) (heuristic)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=7bdd1bd4f5746666becd8bac2d52096e(BudgetSettingsActivity/TextView-Use financ)) (heuristic)
  - act: CustomTouchEvent(state=1d2c8d0e99369d19862285baf984115d, view=7bdd1bd4f5746666becd8bac2d52096e(BudgetSettingsActivity/TextView-Use financ)) (heuristic)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=b57e34fd16cbc40f969d64aeb6cc580d(BudgetSettingsActivity/TextView-Budget)) (rule)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=1bce12574a887f35292c5a2a2fca3c6d(BudgetSettingsActivity/TextView-Show simpl)) (rule)
  - act: CustomTouchEvent(state=c0b0bfbb809294eb235852e73709bb73, view=7bdd1bd4f5746666becd8bac2d52096e(BudgetSettingsActivity/TextView-Use financ)) (heuristic)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=7bdd1bd4f5746666becd8bac2d52096e(BudgetSettingsActivity/TextView-Use financ)) (heuristic)

### GT010 Budget amount

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the 'Budget' section in the navigation drawer.; Select the 'Edit a budget amount' option.; Enter the desired budget amount in the input field.; Tap the 'Save' button to apply the budget amount.; Verify that the budget amount has been updated in the app's main budget view.
- Completion ratio: 1.00
- Actions taken: 14
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=e763328a8146b453f52a744eba4a137c(BudgetSettingsActivity/TextView-If checked)) (nav)
  - act: CustomTouchEvent(state=c0b0bfbb809294eb235852e73709bb73, view=1bce12574a887f35292c5a2a2fca3c6d(BudgetSettingsActivity/TextView-Show simpl)) (heuristic)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=e763328a8146b453f52a744eba4a137c(BudgetSettingsActivity/TextView-If checked)) (llm)
  - act: CustomTouchEvent(state=1d2c8d0e99369d19862285baf984115d, view=1bce12574a887f35292c5a2a2fca3c6d(BudgetSettingsActivity/TextView-Show simpl)) (llm)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (rule)
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=1) (mandatory_fill)
  - act: CustomTouchEvent(state=8b9e49f1d3e5df3e323c655f20d225d7, view=c9d57e046379535a646644ec78b8d8f6(SearchActivity/TextView-Amount to)) (heuristic)
  - act: CustomTouchEvent(state=4face5bc51ba763eefa5343ddeffdd23, view=bc4c474afc2227ad411559bdb1a926ed(CalculatorActivity/TextView-Enter Amou)) (heuristic)

### GT011 Budget details

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap on the 'Budget details' section in the navigation drawer.; Select the 'Budget details' option.; Tap on the 'View budget details and related transactions' button.; Wait for the budget details and related transactions to load.; Review the budget details and related transactions displayed on the screen.
- Completion ratio: 1.00
- Credited from later features: GT005, GT009
- Actions taken: 8
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=93a7be61735d7b212d10498b3371a25c(MainActivity/TextView-your_data_)) (rule)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=93a7be61735d7b212d10498b3371a25c(MainActivity/TextView-your_data_)) (rule)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (llm)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (llm)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=1bc77b2100105e9d823d2672d4dbcaa9(MainActivity/TextView-Current da)) (rule)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=1bc77b2100105e9d823d2672d4dbcaa9(MainActivity/TextView-Current da)) (rule)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=edc7fb7fe1766dc6d0be605a14690c32(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (rule)

### GT012 Delete budget

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the 'Delete' option; Open the Money Manager Ex app; Select the 'Budgets' section
- Remaining steps: Locate and select the budget you wish to delete; Confirm the deletion by tapping 'Yes' on the confirmation dialog
- Completion ratio: 0.60
- Credited from later features: GT001, GT004, GT005
- Actions taken: 7
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=72faf18250cd3c6df446eb3e21594e45(MainActivity/TextView-/storage/e)) (rule)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=72faf18250cd3c6df446eb3e21594e45(MainActivity/TextView-/storage/e)) (rule)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=edc7fb7fe1766dc6d0be605a14690c32(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=44e793bd4cb64fb1c3cc43b013194efd(AccountEditActivity/TextView-SELECT CUR)) (llm)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=44e793bd4cb64fb1c3cc43b013194efd(AccountEditActivity/TextView-SELECT CUR)) (llm)
  - act: ScrollEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=19f9c4b484370144fb4bac21c98e5e1b(AccountEditActivity/ScrollView-), direction=up) (afford_search)

### GT013 Budget view options

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Confirm the selection by tapping the 'Save' button.; Choose the desired budget view option from the available list.; Tap on the 'Budget' navigation hint.; Select 'Change budget view options' from the dropdown menu.
- Completion ratio: 1.00
- Credited from later features: GT003, GT009, GT010, GT018
- Actions taken: 9
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (llm)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=508d1e40ea5181d3f1de495cbdcb0021, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=508d1e40ea5181d3f1de495cbdcb0021, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=4e754d16f6fec35f1052285da8257509(SearchActivity/EditText-choose a c)) (llm)
  - act: CustomTouchEvent(state=bf2a07cfd347b0ca37481199468f6506, view=f609371ab6240393d060fcb22a6cb8c6(SearchActivity/Button-NO COLOR)) (rule)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e9675520ae190f6731e929bc617799f1(SearchActivity/TextView-Select Pay)) (rule)

### GT014 Scheduled transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Transactions' section; Select 'Add a transaction'; Tap 'Save'; Tap on 'Recurring'
- Remaining steps: Enter the details for the recurring transaction
- Completion ratio: 0.83
- Credited from later features: GT003, GT015
- Actions taken: 9
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=508d1e40ea5181d3f1de495cbdcb0021, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomSetTextEvent(state=88645f319627bbafb85e73871c078cb8, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=testcube.mmb) (llm)
  - act: CustomSetTextEvent(state=6c502ec9a4e496de4d1dc53421d0c03c, view=624b5b32f5baf3cdfd8f063c867d4d5d(AccountEditActivity/EditText-testcube.m), text=testcube.mmb) (llm)
  - act: CustomSetTextEvent(state=6c502ec9a4e496de4d1dc53421d0c03c, view=624b5b32f5baf3cdfd8f063c867d4d5d(AccountEditActivity/EditText-testcube.m), text=testcube.mmb) (llm)
  - act: ScrollEvent(state=6c502ec9a4e496de4d1dc53421d0c03c, view=19f9c4b484370144fb4bac21c98e5e1b(AccountEditActivity/ScrollView-), direction=up) (afford_search)

### GT015 Recurring prompt

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Navigate to the Transactions section; Select the Recurring Transactions tab
- Remaining steps: Locate the due recurring transaction prompt; Tap on the prompt to confirm the transaction; Review the transaction details
- Completion ratio: 0.50
- Actions taken: 10
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomTouchEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=88645f319627bbafb85e73871c078cb8, x=55, y=1267) (llm)
  - act: CustomTouchEvent(state=8df8e220ff60f4cd5119531be05cd3b2, view=37362f0c98e81a88235637356c0038f7(AccountEditActivity/CheckedTextView-Closed)) (llm)
  - act: CustomTouchEvent(state=e0d939b689efde4eefc36e74b2cbadef, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=f3803e0eb64c3e61891bb12cfa320aa3, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=92417842f5b54a8855b1e40e88199d3f, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)

### GT016 Payees

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the 'Payees' section in the Money Manager Ex app.; Select the 'Add New Payee' option.; Enter the name of the payee in the 'Name' field.; Enter the bank account number in the 'Account Number' field.; Enter the routing number in the 'Routing Number' field.; Tap the 'Save' button to add the new payee.
- Completion ratio: 1.00
- Actions taken: 8
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (heuristic)
  - act: CustomTouchEvent(state=86e04ef895e4aa026e7fb198e5684c32, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomSetTextEvent(state=44a7521f7310b4ac46aad4c8117d279b, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=Saimon) (mandatory_fill)
  - act: CustomSetTextEvent(state=e64fb481edf96658297f44638006fae6, view=fd4375654e8987b305d7a5a061da7271(AccountEditActivity/EditText-Saimon), text=Saimon) (mandatory_fill)
  - act: CustomSetTextEvent(state=e64fb481edf96658297f44638006fae6, view=fd4375654e8987b305d7a5a061da7271(AccountEditActivity/EditText-Saimon), text=Saimon) (mandatory_fill)
  - act: ScrollEvent(state=e64fb481edf96658297f44638006fae6, view=19f9c4b484370144fb4bac21c98e5e1b(AccountEditActivity/ScrollView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=8df8e220ff60f4cd5119531be05cd3b2, view=0843e091ec41665abeeed5507a9c3b40(AccountEditActivity/CheckedTextView-Open)) (llm)
  - act: CustomTouchEvent(state=e64fb481edf96658297f44638006fae6, view=74a93b20fe872e1ae9ec33afdd0c5493(AccountEditActivity/Button-)) (heuristic)

### GT017 Categories

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Categories' option in the navigation menu; Select the 'Add New Category' option; Enter the name of the new category; Tap the 'Save' button to add the category; Select the 'Edit' option for an existing category
- Remaining steps: Enter the new name for the category
- Completion ratio: 0.83
- Credited from later features: GT010
- Actions taken: 9
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=962542abca5cd365d724b78f8e342bf1(SearchActivity/TextView-Select Cat)) (heuristic)
  - act: CustomSetTextEvent(state=f29a8b5dfade9ae54e020d97155c954e, view=a2cb3f6bdaa1bbc3228397d725b6f792(CategoryListActivity/AutoCompleteTextView-   ), text=no) (mandatory_fill)
  - act: CustomTouchEvent(state=d8926dbcd50938340359b8a9592633c3, view=53dc65340553202195e21449874ed810(CategoryListActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=75bde426399c9167c035d22ae9ba0c7c, view=b5e13c806cad1442e89e49f44925ac16(CategoryListActivity/TextView-Add Subcat)) (nav)
  - act: CustomTouchEvent(state=75bde426399c9167c035d22ae9ba0c7c, view=b5e13c806cad1442e89e49f44925ac16(CategoryListActivity/TextView-Add Subcat)) (nav)
  - act: ScrollEvent(state=75bde426399c9167c035d22ae9ba0c7c, view=9d9f0693d866dff3f51651a4d77599ec(CategoryListActivity/Spinner-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=f785c2c7e6bd99e8ce6cdf4f89fb956f, view=a978a3f0ea9d9ddae6e0fd5dc4781ffb(CategoryListActivity/CheckedTextView-<root>)) (heuristic)
  - act: CustomTouchEvent(state=75bde426399c9167c035d22ae9ba0c7c, view=89d32d0cdc6b1419334dad12fef8b450(CategoryListActivity/TextView-<root>)) (nav)

### GT018 Built-in report

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Menu' icon in the top left corner of the screen.; Select 'Reports' from the menu.
- Remaining steps: Tap on the 'Built-in Report' option.; Wait for the report to load and verify the data displayed.
- Completion ratio: 0.50
- Actions taken: 14
  - act: CustomTouchEvent(state=02888c0f4cc2d525464b94d09d2590c2, view=13621b78aa600090e88b02a954aa0cd5(TagActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=7209b198637cf1ef87466bf4569ff91b, view=0dff78898eee2927d9f768fbec7b7993(TagActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=02888c0f4cc2d525464b94d09d2590c2, view=e9912daba18070a8344abac8585b66c5(TagActivity/FloatingActionButton-)) (heuristic)
  - act: CustomSetTextEvent(state=a305ec2fc8b86b3dfdf3a8e7963b793c, view=c4f0995ee6b9a30e3efe2869541cd1f0(TagActivity/EditText-Tag name), text=testcube.mmb) (rule)
  - act: CustomTouchEvent(state=553675a79e078c5fa8a1d151a6fda738, x=841, y=1171) (llm)
  - act: CustomTouchEvent(state=553675a79e078c5fa8a1d151a6fda738, x=841, y=895) (llm)
  - act: CustomTouchEvent(state=553675a79e078c5fa8a1d151a6fda738, view=3c7129e47e4799cf7a91a2a4f4a1d27b(TagActivity/Button-OK)) (heuristic)
  - act: CustomTouchEvent(state=5854a8ddcc7ca78224b4a4b56eaf4c17, view=cf9c59b2dba2fdc728e5a0cf98d33e90(SearchActivity/Button-)) (heuristic)

### GT019 General report

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Select the 'General report' option.
- Remaining steps: Tap on the 'report' navigation hint.; Tap on the 'Run a general report' button.
- Completion ratio: 0.33
- Credited from later features: GT010
- Actions taken: 7
  - act: CustomTouchEvent(state=8b18ca9e4c635c37b2ca1c065856157f, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=8b18ca9e4c635c37b2ca1c065856157f, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=8b18ca9e4c635c37b2ca1c065856157f, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=7e35ad76e7988aac4e16ba6730f8ecb6, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=7e35ad76e7988aac4e16ba6730f8ecb6, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=7e35ad76e7988aac4e16ba6730f8ecb6, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=8b18ca9e4c635c37b2ca1c065856157f, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (heuristic)

### GT020 Investments

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Investments' section in the Money Manager Ex app.; Tap the 'Add' button to save the new investment.; Verify that the investment is now listed in the 'Investments' section.
- Remaining steps: Select the 'Track a stock or fund' option.; Enter the name or ticker symbol of the stock or fund you wish to track.
- Completion ratio: 0.60
- Credited from later features: GT003, GT005
- Actions taken: 5
  - act: CustomTouchEvent(state=8b18ca9e4c635c37b2ca1c065856157f, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (heuristic)
  - act: CustomTouchEvent(state=8b18ca9e4c635c37b2ca1c065856157f, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=18d0ffcd9ec774c598e8dc8a55203b38, view=9e278810123d6fc7d5b1b145c0345498(MainActivity/CheckedTextView-o)) (heuristic)
  - act: CustomTouchEvent(state=da72e66e59890e787da483c05bbd41de, x=286, y=903) (llm)
  - act: CustomTouchEvent(state=18d0ffcd9ec774c598e8dc8a55203b38, view=9e278810123d6fc7d5b1b145c0345498(MainActivity/CheckedTextView-o)) (heuristic)

### GT021 Stock transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select 'Add a stock transaction' from the menu.; Select the date of the transaction.
- Remaining steps: Tap on the 'Stock' navigation hint.; Enter the stock symbol.; Enter the number of shares.; Enter the price per share.
- Completion ratio: 0.33
- Credited from later features: GT003, GT004
- Actions taken: 9
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=585bdacf181cdeba8bf9bd3ddbd4f16f(IncomeVsExpensesActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=8b18ca9e4c635c37b2ca1c065856157f, view=3f2f6952e5e27c18a8bf24e8f9482673(MainActivity/FrameLayout-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=3595bed292719997b56701ac18983666(IncomeVsExpensesActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=f6be69f1bc8fb274bb63218fb5ccd872(IncomeVsExpensesActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=4f61b90b9ad5a17caeab5941fbc2d161, view=6afd2ddae0afe2ff010e275a4a390d1c(IncomeVsExpensesActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=585bdacf181cdeba8bf9bd3ddbd4f16f(IncomeVsExpensesActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=8b18ca9e4c635c37b2ca1c065856157f, view=7d417e498af5c25e4d8d9934eb8f5c6d(MainActivity/TextView-$ 0.00)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (afford_search)

### GT022 Fixed assets

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap on the 'Assets' section in the Money Manager Ex app.; Select the 'Fixed Assets' option from the assets menu.; Enter the name of the fixed asset in the input field.; Tap on the 'Add' button to save the fixed asset.; Verify the fixed asset is listed in the assets section.
- Completion ratio: 1.00
- Credited from later features: GT003, GT005
- Actions taken: 9
  - act: CustomTouchEvent(state=8b18ca9e4c635c37b2ca1c065856157f, view=93a7be61735d7b212d10498b3371a25c(MainActivity/TextView-your_data_)) (rule)
  - act: CustomTouchEvent(state=8b18ca9e4c635c37b2ca1c065856157f, view=93a7be61735d7b212d10498b3371a25c(MainActivity/TextView-your_data_)) (rule)
  - act: CustomTouchEvent(state=8b18ca9e4c635c37b2ca1c065856157f, view=605a5f744a665795c78d1d4dc74be1ae(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=8ff2002877c7a119299a68cfac9d9913, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=1234567890) (mandatory_fill)
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=f146b558de4d3eb646628fe5552110fe(SearchActivity/CheckBox-Deposit)) (llm)
  - act: CustomTouchEvent(state=2446b73b6a11f65f709302aad3cb95a1, view=b4050a1552fb56f8c649bd47e4ed76f6(SearchActivity/CheckBox-Deposit)) (llm)
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=f146b558de4d3eb646628fe5552110fe(SearchActivity/CheckBox-Deposit)) (llm)

### GT023 Currencies

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap the 'Save' button to confirm the changes.; Tap on the 'Currencies' option in the navigation drawer.; Select the 'Manage Currencies' option.
- Remaining steps: Enter the name of the currency you want to add or edit.; Select the currency type (e.g., base, quote, etc.); Enter the currency rate.
- Completion ratio: 0.50
- Credited from later features: GT003, GT006, GT010
- Actions taken: 7
  - act: CustomTouchEvent(state=8ff2002877c7a119299a68cfac9d9913, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=8ff2002877c7a119299a68cfac9d9913, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=8ff2002877c7a119299a68cfac9d9913, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=e62cc63dffd7625f76671ba50e2251bd, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=e62cc63dffd7625f76671ba50e2251bd, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=e62cc63dffd7625f76671ba50e2251bd, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=8ff2002877c7a119299a68cfac9d9913, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (heuristic)

### GT024 Sync

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select 'Open sync settings' from the navigation menu
- Remaining steps: Tap on the 'Sync' navigation hint; Enter the sync settings page; Select the option to set up data sync; Follow the prompts to complete the setup
- Completion ratio: 0.20
- Credited from later features: GT017
- Actions taken: 8
  - act: CustomTouchEvent(state=8ff2002877c7a119299a68cfac9d9913, view=7c77d5e9d33904a1db7e01727c86a8a0(MainActivity/ProgressBar-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=6afd2ddae0afe2ff010e275a4a390d1c(IncomeVsExpensesActivity/RadioButton-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=4ef5fc8a3f01d24bad3ebeff464fd821(IncomeVsExpensesActivity/TextView-Select Acc)) (rule)
  - act: CustomTouchEvent(state=18f9869abde604381fd51f053a2e269a, view=b96ef268502e0ab7f6a634754c43d2ba(IncomeVsExpensesActivity/View-)) (llm)
  - act: CustomTouchEvent(state=18f9869abde604381fd51f053a2e269a, view=2928503e93598979461cdc02990dea9f(IncomeVsExpensesActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=f6be69f1bc8fb274bb63218fb5ccd872(IncomeVsExpensesActivity/Button-)) (afford_search)

### GT025 Database password

- Status: **covered**
- Reason: Covered by shared-flow reuse of C005.
- Completion source: shared_flow_reuse
- Feature source: guide
- Completed steps: Tap on the 'Settings' menu; Select 'Database' from the settings menu; Select 'Database Password' from the database settings; Enter the new database password; Confirm the new database password; Tap on the 'Save' button to set the database password
- Completion ratio: 1.00
- Actions taken: 4
  - act: CustomTouchEvent(state=8ff2002877c7a119299a68cfac9d9913, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)

### GT026 Fingerprint lock

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Select 'Security' from the settings menu; Navigate to the settings menu
- Remaining steps: Tap on 'Fingerprint lock'; Enable fingerprint lock; Confirm the fingerprint lock setup
- Completion ratio: 0.50
- Credited from later features: GT004, GT018, GT025
- Actions taken: 7
  - act: CustomTouchEvent(state=8ff2002877c7a119299a68cfac9d9913, view=7c77d5e9d33904a1db7e01727c86a8a0(MainActivity/ProgressBar-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=3595bed292719997b56701ac18983666(IncomeVsExpensesActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=0a9d730e29137793e1ffc3da5c595574, view=78374ff278a2c4fcebfc80ef817a6550(IncomeVsExpensesActivity/TextView-All Time)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=b0bd32912435a8aa0e2e5e760aaf218e(IncomeVsExpensesActivity/TextView-Income Vs )) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=b0bd32912435a8aa0e2e5e760aaf218e(IncomeVsExpensesActivity/TextView-Income Vs )) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (afford_search)

### GT027 Import export

- Status: **partial**
- Reason: blocked_no_progress: stayed in the same state cluster after 10 actions.
- Feature source: guide
- Completed steps: Tap on the 'Import or export a file' option in the main menu.; Locate and select the file you want to import from your device.; Verify the imported data in the app's main view.; Select 'Import' from the navigation hints.
- Remaining steps: Tap on the 'QIF' or 'CSV' file type you want to import.; Tap 'Open' to confirm the file selection and import it.
- Completion ratio: 0.67
- Credited from later features: GT004, GT010, GT018
- Actions taken: 10
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=4ef5fc8a3f01d24bad3ebeff464fd821(IncomeVsExpensesActivity/TextView-Select Acc)) (llm)
  - act: CustomTouchEvent(state=18f9869abde604381fd51f053a2e269a, view=2928503e93598979461cdc02990dea9f(IncomeVsExpensesActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=6afd2ddae0afe2ff010e275a4a390d1c(IncomeVsExpensesActivity/RadioButton-)) (afford_search)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=3595bed292719997b56701ac18983666(IncomeVsExpensesActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=585bdacf181cdeba8bf9bd3ddbd4f16f(IncomeVsExpensesActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=8ff2002877c7a119299a68cfac9d9913, view=7d417e498af5c25e4d8d9934eb8f5c6d(MainActivity/TextView-$ 0.00)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=f6be69f1bc8fb274bb63218fb5ccd872(IncomeVsExpensesActivity/Button-)) (rule)

### GT028 Settings

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap the 'Open settings' button.; Tap the 'Settings' option in the app's main menu.; Select the 'Settings' option from the menu.; Navigate to the 'Settings' section within the app.
- Completion ratio: 1.00
- Credited from later features: GT004
- Actions taken: 5
  - act: CustomTouchEvent(state=8ff2002877c7a119299a68cfac9d9913, view=887e9137d7bd09876b9e833aec135cbf(MainActivity/TextView-$ 0.00)) (heuristic)
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=5b074d74e3c3559c49729448dd1f8277(IncomeVsExpensesActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (heuristic)

## Shared flows detected

1 reuse(s); 5 action(s) skipped by not re-executing a known terminal flow.

- `GT025` reused `C005` (from GT006), skipped 5 action(s)

See `session.json` and `log.md` in this folder for the full trace.
