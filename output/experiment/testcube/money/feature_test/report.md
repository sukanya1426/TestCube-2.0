# Feature test report: Money Manager Ex

- Started: 2026-10-25 20:37:23
- Finished: 2026-10-25 21:32:31
- Features: 28
- Covered: 2
- Partial: 26
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 61% (mean completion ratio; the headline number)
- Coverage: 7% (features with every guide step matched)
- Stop reason: all_features_done
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 28
- Never attempted: 0
- Blocked then recovered on retry: 0
- Blocked still: 0

## Guide vs README-extracted

- Guide features: 28
- README-extracted features: 7
- In both: 1
- Guide-only: 27
- README-only: 6
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
  - README-only: F001 Close or skip the tutorial
  - README-only: F002 Leave any first-run analytics or settings screen
  - README-only: F003 Tap Create Database or Open Database if shown
  - README-only: F004 Enter a file name if asked and confirm Save
  - README-only: F005 Reach the home or main screen
  - README-only: F006 Create or open a database

## Independent ground-truth addendum

- Features not in the guide list: 6
- Matched in this run: 2
- Missed: 4
- Independent features not in the guide list. matched = live journal features with name similarity >= 0.3 (hybrid discovery is the expected source).

## Text-field resolution

- Filled via credential.txt: 23
- Filled via VLM/Gemini: 28
- Unresolved: 0
- Online coverage: 7% (2/28) — live journal self-report (covered / extracted features).
- Offline coverage: not computed (no ground-truth JSON).

## Findings

### GT001 New database

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Create a database' option; Tap the 'Create' button to finalize the new database creation
- Remaining steps: Select 'New database' to start creating a new database; Enter a name for the new database
- Completion ratio: 0.60
- Credited from later features: GT003
- Actions taken: 15
  - act: CustomTouchEvent(state=4fc069f43b4658dcf0a2d2647e4c412b, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na)) (llm)
  - act: CustomTouchEvent(state=4fc069f43b4658dcf0a2d2647e4c412b, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na)) (llm)
  - act: ScrollEvent(state=4fc069f43b4658dcf0a2d2647e4c412b, view=19f9c4b484370144fb4bac21c98e5e1b(AccountEditActivity/ScrollView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=8df8e220ff60f4cd5119531be05cd3b2, view=37362f0c98e81a88235637356c0038f7(AccountEditActivity/CheckedTextView-Closed)) (llm)
  - act: CustomSetTextEvent(state=8a28eb14a61d90b2b728d345641feb57, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=testcube.mmb) (llm)
  - act: CustomSetTextEvent(state=d5ce98565520c9b6de370129e4bee29f, view=624b5b32f5baf3cdfd8f063c867d4d5d(AccountEditActivity/EditText-testcube.m), text=testcube.mmb) (llm)
  - act: CustomTouchEvent(state=d5ce98565520c9b6de370129e4bee29f, view=624b5b32f5baf3cdfd8f063c867d4d5d(AccountEditActivity/EditText-testcube.m)) (llm)
  - act: CustomTouchEvent(state=d5ce98565520c9b6de370129e4bee29f, view=44e793bd4cb64fb1c3cc43b013194efd(AccountEditActivity/TextView-SELECT CUR)) (rule)

### GT002 New account

- Status: **partial**
- Reason: Onboarding already finished; main screen is visible.
- Feature source: guide
- Completed steps: Tap the 'Save' button; Select 'Create an account'; Tap on the 'Account' navigation hint
- Remaining steps: Enter the account name; Select the account type; Enter the account number
- Completion ratio: 0.50
- Credited from later features: GT001, GT007, GT013

### GT003 Add transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Add a transaction' button.; Tap the 'Save' button to add the transaction.
- Remaining steps: Enter the amount of the transaction.; Select the category of the transaction (e.g., Income or Expense).; Enter the description of the transaction.
- Completion ratio: 0.40
- Credited from later features: GT014
- Actions taken: 9
  - act: CustomTouchEvent(state=45fe028e5c478995e6d24e1b8592ea4a, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (nav)
  - act: CustomTouchEvent(state=45fe028e5c478995e6d24e1b8592ea4a, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomTouchEvent(state=10afe4e5562f1d18155e5c266544a8e0, view=2505535216838ca77a3290df1560d18d(AccountEditActivity/DrawerLayout-)) (rule)
  - act: CustomTouchEvent(state=c4e00280d29fb07fa819d4f2e8ae8ba9, view=4f0b63328683a15416e1c0d118625bef(AccountEditActivity/View-31)) (heuristic)
  - act: CustomTouchEvent(state=a5d490d63720a75515afcf71c43ff4d2, view=7f1670d4dc12f9feace2c3a9b2abbbba(AccountEditActivity/View-31)) (heuristic)
  - act: CustomTouchEvent(state=a5d490d63720a75515afcf71c43ff4d2, view=7f1670d4dc12f9feace2c3a9b2abbbba(AccountEditActivity/View-31)) (heuristic)
  - act: CustomTouchEvent(state=a5d490d63720a75515afcf71c43ff4d2, view=bb3c42cdf9d96ce8bff566108129c8e0(AccountEditActivity/View-15)) (afford_search)
  - act: CustomTouchEvent(state=50abfab48d157399305df3460cb9c8f5, view=ebf4e2ce6ee624b2eaf2a1f4e9f22634(AccountEditActivity/Button-OK)) (rule)

### GT004 Edit transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the transaction you want to edit in the transaction list.; Select the 'Edit' option from the transaction details.; Tap the 'Save' button to update the transaction.
- Remaining steps: Enter the new amount or description as needed.; Confirm the changes if prompted.
- Completion ratio: 0.60
- Credited from later features: GT005, GT014
- Actions taken: 10
  - act: CustomTouchEvent(state=89af6d41a7ccada4adeee133d6ffe251, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (llm)
  - act: CustomTouchEvent(state=89af6d41a7ccada4adeee133d6ffe251, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: CustomTouchEvent(state=fd192034ad91317d936158c61d7fca30, view=5e0e3a0235dea8d658d02e16f5a0fe11(AccountEditActivity/TextView-/storage/e)) (llm)
  - act: CustomTouchEvent(state=4fc069f43b4658dcf0a2d2647e4c412b, view=bb7c7972e5c4d268205937de196dc0ee(AccountEditActivity/EditText-Notes)) (nav)
  - act: CustomTouchEvent(state=4fc069f43b4658dcf0a2d2647e4c412b, view=bb7c7972e5c4d268205937de196dc0ee(AccountEditActivity/EditText-Notes)) (nav)
  - act: ScrollEvent(state=4fc069f43b4658dcf0a2d2647e4c412b, view=19f9c4b484370144fb4bac21c98e5e1b(AccountEditActivity/ScrollView-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=8df8e220ff60f4cd5119531be05cd3b2, view=37362f0c98e81a88235637356c0038f7(AccountEditActivity/CheckedTextView-Closed)) (llm)
  - act: CustomTouchEvent(state=8a28eb14a61d90b2b728d345641feb57, view=74a93b20fe872e1ae9ec33afdd0c5493(AccountEditActivity/Button-)) (rule)

### GT005 Filter by date

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Filter transactions by date' option in the navigation menu.; Select the 'Date' filter option.
- Remaining steps: Enter the start date for the filter.; Enter the end date for the filter.; Tap the 'Apply' button to apply the date range filter.
- Completion ratio: 0.40
- Actions taken: 9
  - act: CustomTouchEvent(state=c07558a39898e3b0daca22f53e676eb4, view=526203752573a94a403ad7d34812cbf8(SearchActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=4face5bc51ba763eefa5343ddeffdd23, view=bc4c474afc2227ad411559bdb1a926ed(CalculatorActivity/TextView-Enter Amou)) (heuristic)
  - act: CustomTouchEvent(state=4face5bc51ba763eefa5343ddeffdd23, view=bc4c474afc2227ad411559bdb1a926ed(CalculatorActivity/TextView-Enter Amou)) (heuristic)
  - act: CustomTouchEvent(state=4face5bc51ba763eefa5343ddeffdd23, view=0943e936a9b135c923b968086ae0335f(CalculatorActivity/Button-+)) (heuristic)
  - act: CustomTouchEvent(state=8e9aad7dd3d3d86a2660bd187309f1e1, view=bc4c474afc2227ad411559bdb1a926ed(CalculatorActivity/TextView-Enter Amou)) (heuristic)
  - act: CustomTouchEvent(state=8e9aad7dd3d3d86a2660bd187309f1e1, view=bc4c474afc2227ad411559bdb1a926ed(CalculatorActivity/TextView-Enter Amou)) (heuristic)
  - act: CustomTouchEvent(state=8e9aad7dd3d3d86a2660bd187309f1e1, view=0943e936a9b135c923b968086ae0335f(CalculatorActivity/Button-+)) (heuristic)
  - act: CustomTouchEvent(state=736de65779cc5b3152e764c404626edd, view=bc4c474afc2227ad411559bdb1a926ed(CalculatorActivity/TextView-Enter Amou)) (heuristic)

### GT006 Search transactions

- Status: **covered**
- Reason: Hit the per-feature step limit. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap on the 'Search transactions' option in the navigation drawer.; Enter the search term in the search bar.; Press the 'Enter' key to execute the search.; Select the desired transaction from the search results.; Tap on the 'Sort' option to sort the transactions.; Select the desired sorting option from the dropdown menu.
- Completion ratio: 1.00
- Credited from later features: GT005
- Actions taken: 18
  - act: CustomTouchEvent(state=cdfc3f9684068fba58cbfb67f0038cc6, view=836d6ceefdbb966f35964db24ebd17e0(SearchActivity/CheckedTextView-Duplicate)) (llm)
  - act: CustomTouchEvent(state=9f4c9eb0cd5a351ea53a347fffac6a64, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=9f4c9eb0cd5a351ea53a347fffac6a64, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=a77ab87c8cb6103cfe2c8747ad2f2a12(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=2cc65d47aaa2d183602e4845ba84f5ae, view=dfb3ee4bfbc79fd337920c5692bd781d(SearchActivity/TextView-Sort by da)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=9f4c9eb0cd5a351ea53a347fffac6a64, view=19ee481c4531b725329e5dd41ed6a159(SearchActivity/TextView-Search)) (heuristic)

### GT007 Favorite account

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Select the account you want to mark as favorite; Tap on the 'Favorite' option
- Remaining steps: Confirm the favorite status by tapping the confirmation button
- Completion ratio: 0.75
- Credited from later features: GT001
- Actions taken: 10
  - act: CustomTouchEvent(state=89af6d41a7ccada4adeee133d6ffe251, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: KeyEvent(state=207569270f5ff30a425070c7afe649e2, name=BACK) (llm)
  - act: CustomTouchEvent(state=e8e73b6763009503ac34a2d41ac73f5a, view=04484c2988ce055b6513c74b0c472471(AccountEditActivity/Button-Close app)) (llm)
  - act: CustomTouchEvent(state=89af6d41a7ccada4adeee133d6ffe251, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=45fe028e5c478995e6d24e1b8592ea4a, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=ce9f8bae7c1a3d996903712060ff7906(SearchActivity/TextView-STATUS)) (llm)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=ce9f8bae7c1a3d996903712060ff7906(SearchActivity/TextView-STATUS)) (llm)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=eda4a15aef715ab56b24b363d052bfe3(SearchActivity/TextView-ACCOUNT)) (llm)

### GT008 Manage accounts

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Accounts' option in the navigation drawer.; Select the account you wish to edit from the account list.
- Remaining steps: Tap on the 'Edit' button next to the account you selected.; Make the necessary changes to the account details.; Tap on the 'Save' button to update the account details.
- Completion ratio: 0.40
- Credited from later features: GT004
- Actions taken: 10
  - act: ScrollEvent(state=3b7f294b09c821f020a16db3d817a8b1, view=3d0da6020df9c26a32aa108fcb4464bd(MainActivity/ExpandableListView-), direction=left) (rule)
  - act: CustomTouchEvent(state=878dad5a22919e5ee516f44c3956487e, view=c2105826f90b3378092fd0438d21caea(MainActivity/TextView-Homeneeds)) (heuristic)
  - act: CustomTouchEvent(state=5537ba717d0bddd4d3dfaba519eaa74a, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomSetTextEvent(state=2f77687863312998838a7d801cd171e3, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor), text=no) (rule)
  - act: CustomSetTextEvent(state=a6ef0c5b39d8412fc7976dfda003cf8b, view=61ac53568a1b845675ac5cd5df9c84e5(MainActivity/EditText-no), text=your_email@gmail.com) (rule)
  - act: CustomSetTextEvent(state=631e172ff71a4ca5a0f13b8b0d5c3ff4, view=8b489210db6b50834e6b403e9c1ede24(MainActivity/EditText-your_email), text=your_email@gmail.com) (rule)
  - act: CustomSetTextEvent(state=631e172ff71a4ca5a0f13b8b0d5c3ff4, view=8b489210db6b50834e6b403e9c1ede24(MainActivity/EditText-your_email), text=your_email@gmail.com) (rule)
  - act: ScrollEvent(state=631e172ff71a4ca5a0f13b8b0d5c3ff4, view=16a1c69f3bf35250267e3567b796aa52(MainActivity/Spinner-), direction=up) (afford_search)

### GT009 Budget

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Create a budget' button.; Tap on the 'Budgets' section in the navigation drawer.; Select the category for the budget.; Tap on the 'Save' button to finalize the budget.
- Remaining steps: Enter the name of the budget.; Set the budget amount.
- Completion ratio: 0.67
- Credited from later features: GT001, GT006, GT013, GT017
- Actions taken: 4
  - act: CustomTouchEvent(state=bfa93369fafcb6c2036f53b5b7fdd7d8, view=4855c3535ba0a0549bcd86b83a41ccc2(MainActivity/CheckedTextView-<root>)) (heuristic)
  - act: CustomTouchEvent(state=631e172ff71a4ca5a0f13b8b0d5c3ff4, view=8d2f772d21b7b12c4f92c8bf23f57045(MainActivity/TextView-<root>)) (llm)
  - act: CustomTouchEvent(state=bfa93369fafcb6c2036f53b5b7fdd7d8, view=4855c3535ba0a0549bcd86b83a41ccc2(MainActivity/CheckedTextView-<root>)) (heuristic)
  - act: CustomTouchEvent(state=631e172ff71a4ca5a0f13b8b0d5c3ff4, view=8d2f772d21b7b12c4f92c8bf23f57045(MainActivity/TextView-<root>)) (llm)

### GT010 Budget amount

- Status: **partial**
- Reason: The current screen is not related to setting a budget amount, and the action history indicates that the feature has been completed.
- Feature source: guide
- Completed steps: Select the 'Edit Budget Amount' option.; Tap on the 'Budget' section in the navigation drawer.
- Remaining steps: Enter the desired budget amount in the input field.; Tap the 'Save' button to apply the budget amount.; Verify that the budget amount has been successfully updated in the app.
- Completion ratio: 0.40
- Credited from later features: GT005, GT006
- Actions taken: 1
  - act: CustomTouchEvent(state=bfa93369fafcb6c2036f53b5b7fdd7d8, view=8bb7b3404939ddebe18285905eca8c7d(MainActivity/CheckedTextView-Automobile)) (heuristic)

### GT011 Budget details

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Locate and tap on the specific transaction you want to view.; Select the 'View Budget Details and Related Transactions' option.; Tap on the 'Budget Details' section in the main menu.
- Remaining steps: Enter the budget details screen.; Review the transaction details and related budget information.
- Completion ratio: 0.60
- Credited from later features: GT004, GT005, GT023
- Actions taken: 5
  - act: CustomSetTextEvent(state=af674742604c17ceca474189dca7724d, view=8b489210db6b50834e6b403e9c1ede24(MainActivity/EditText-your_email), text=your_email@gmail.com) (rule)
  - act: CustomSetTextEvent(state=af674742604c17ceca474189dca7724d, view=8b489210db6b50834e6b403e9c1ede24(MainActivity/EditText-your_email), text=your_email@gmail.com) (rule)
  - act: CustomTouchEvent(state=af674742604c17ceca474189dca7724d, view=eadd8f7add6da2b2d5e33fc11f12b3a2(MainActivity/Spinner-)) (rule)
  - act: CustomTouchEvent(state=3fed27ac64143e76aece27f7ce124a2a, view=a1c25b739895255ca07cd5134cf7e34c(MainActivity/CheckedTextView-Automobile)) (heuristic)
  - act: CustomTouchEvent(state=af674742604c17ceca474189dca7724d, view=eadd8f7add6da2b2d5e33fc11f12b3a2(MainActivity/Spinner-)) (rule)

### GT012 Delete budget

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Delete' option; Locate and select the budget you want to delete
- Remaining steps: Select the 'Budgets' section; Confirm the deletion by tapping 'Yes' on the confirmation dialog
- Completion ratio: 0.60
- Credited from later features: GT001, GT007
- Actions taken: 8
  - act: CustomTouchEvent(state=3fed27ac64143e76aece27f7ce124a2a, view=a1c25b739895255ca07cd5134cf7e34c(MainActivity/CheckedTextView-Automobile)) (heuristic)
  - act: CustomTouchEvent(state=af674742604c17ceca474189dca7724d, view=66504947211b0967f5afa26e28736a47(MainActivity/Button-CANCEL)) (rule)
  - act: CustomTouchEvent(state=5537ba717d0bddd4d3dfaba519eaa74a, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomSetTextEvent(state=2f77687863312998838a7d801cd171e3, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor), text=no) (rule)
  - act: CustomSetTextEvent(state=a6ef0c5b39d8412fc7976dfda003cf8b, view=61ac53568a1b845675ac5cd5df9c84e5(MainActivity/EditText-no), text=your_email@gmail.com) (rule)
  - act: CustomTouchEvent(state=631e172ff71a4ca5a0f13b8b0d5c3ff4, view=16a1c69f3bf35250267e3567b796aa52(MainActivity/Spinner-)) (rule)
  - act: CustomTouchEvent(state=bfa93369fafcb6c2036f53b5b7fdd7d8, view=8bb7b3404939ddebe18285905eca8c7d(MainActivity/CheckedTextView-Automobile)) (heuristic)
  - act: CustomTouchEvent(state=af674742604c17ceca474189dca7724d, view=66504947211b0967f5afa26e28736a47(MainActivity/Button-CANCEL)) (rule)

### GT013 Budget view options

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Budget' navigation hint.; Select 'Change budget view options' from the dropdown menu.; Select the desired budget view option from the list.
- Remaining steps: Confirm the selection by tapping the 'Save' button.
- Completion ratio: 0.75
- Credited from later features: GT005
- Actions taken: 13
  - act: CustomTouchEvent(state=1f44459f13db293ed2b9e271253adad5, view=c85dd6998ec3837b1ab625eca0c2c12f(MainActivity/AutoCompleteTextView-budgets)) (heuristic)
  - act: CustomTouchEvent(state=1f44459f13db293ed2b9e271253adad5, view=c85dd6998ec3837b1ab625eca0c2c12f(MainActivity/AutoCompleteTextView-budgets)) (heuristic)
  - act: CustomTouchEvent(state=1f44459f13db293ed2b9e271253adad5, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (afford_search)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=66504947211b0967f5afa26e28736a47(MainActivity/Button-CANCEL)) (llm)
  - act: CustomTouchEvent(state=1f44459f13db293ed2b9e271253adad5, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (rule)
  - act: CustomSetTextEvent(state=1f44459f13db293ed2b9e271253adad5, view=c85dd6998ec3837b1ab625eca0c2c12f(MainActivity/AutoCompleteTextView-budgets), text=budgets) (rule)
  - act: CustomTouchEvent(state=1f44459f13db293ed2b9e271253adad5, view=56dd1af828df95f4e4137c8b37400107(MainActivity/TextView-No categor)) (rule)

### GT014 Scheduled transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Add a recurring transaction' button.; Enter the name of the transaction in the text field.; Select the frequency of the transaction from the dropdown menu.
- Remaining steps: Set the date and time for the transaction to occur.; Tap on the 'Save' button to create the recurring transaction.
- Completion ratio: 0.60
- Actions taken: 11
  - act: CustomTouchEvent(state=5fe6b60bf7a36833492c1ac0704b98a0, view=55653a2494343602e9c16941ead6ba0c(MainActivity/CheckBox-)) (heuristic)
  - act: CustomTouchEvent(state=54764f65caae197011a70753c944988e, view=864b370ff8ec8efd165831636a4d69c8(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=54764f65caae197011a70753c944988e, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (afford_search)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=16a1c69f3bf35250267e3567b796aa52(MainActivity/Spinner-)) (rule)
  - act: CustomTouchEvent(state=bfa93369fafcb6c2036f53b5b7fdd7d8, view=5f7c9f4784cfcfaad3e4fd3ef350639f(MainActivity/CheckedTextView-Automobile)) (heuristic)
  - act: CustomSetTextEvent(state=0f27a70be223b137f16283d679af8bb9, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor), text=no) (llm)
  - act: CustomSetTextEvent(state=fb60bcff2b6affa628d376ca653d66ac, view=61ac53568a1b845675ac5cd5df9c84e5(MainActivity/EditText-no), text=your_email@gmail.com) (rule)
  - act: CustomTouchEvent(state=7dd2c20d5951a865a6ed61574ffdb91e, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (rule)

### GT015 Recurring prompt

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Recurring' badge or section in the Money Manager Ex app.; Select the recurring transaction prompt that appears.; Tap the 'Accept' button to confirm the due recurring transaction.
- Remaining steps: Review the details of the transaction to ensure it is correct.; Verify that the transaction is now marked as accepted in the app's main view.
- Completion ratio: 0.60
- Credited from later features: GT001, GT014
- Actions taken: 8
  - act: CustomTouchEvent(state=54764f65caae197011a70753c944988e, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=54764f65caae197011a70753c944988e, view=56dd1af828df95f4e4137c8b37400107(MainActivity/TextView-No categor)) (heuristic)
  - act: CustomTouchEvent(state=54764f65caae197011a70753c944988e, view=56dd1af828df95f4e4137c8b37400107(MainActivity/TextView-No categor)) (heuristic)
  - act: CustomTouchEvent(state=54764f65caae197011a70753c944988e, view=2daaffb870b823a5cbdae22e1dcb0673(MainActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=a049219663ea6b7ecce0efdb02b70f0f, view=70d66a1dadce077c8e0c676fd6e7c915(MainActivity/CheckedTextView-j)) (heuristic)
  - act: CustomTouchEvent(state=2cf37ad03c31c57077f91ed2914fbb2c, view=bc002c12a1c3799d66d0e07976d4f0f2(MainActivity/TextView-Switch Act)) (llm)
  - act: CustomTouchEvent(state=1ab369f1e5c70f59d4d85cdf9237c1c8, view=859ace8f29d6fcc73e014bbc94552271(MainActivity/CheckedTextView-j)) (heuristic)

### GT016 Payees

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Payees' section in the Money Manager Ex app.; Tap the 'Save' button to add the payee.
- Remaining steps: Enter the name of the payee in the input field.; Select the payee type from the dropdown menu.; Enter the payee's bank account details.; Verify the payee has been added by checking the list of payees.
- Completion ratio: 0.33
- Credited from later features: GT001, GT014
- Actions taken: 9
  - act: CustomTouchEvent(state=6c5514ca43b8a0c0eb19b4b0e510696c, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor)) (llm)
  - act: CustomTouchEvent(state=6c5514ca43b8a0c0eb19b4b0e510696c, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor)) (llm)
  - act: ScrollEvent(state=6c5514ca43b8a0c0eb19b4b0e510696c, view=f52604802f79ceb83ffc91ca6a6be771(MainActivity/Spinner-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=e1c83449a4bd409e74d88b5beb3b5fd1, view=d69138c769fff3c74c16bbbea5c92b0c(MainActivity/CheckedTextView-Bills:Gas)) (llm)
  - act: CustomTouchEvent(state=6c5514ca43b8a0c0eb19b4b0e510696c, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (llm)
  - act: CustomSetTextEvent(state=3b3e5806dd1bbaece988d0e729dd52dd, view=f791beeb9799f0db39d52cdc9466fc11(MainActivity/AutoCompleteTextView-   ), text=Saimon) (llm)
  - act: CustomSetTextEvent(state=f1588063d7a10c5c6ae92cd8f9e53c69, view=599efc091c720ca54b53ecb598ac1477(MainActivity/AutoCompleteTextView-Saimon), text=Saimon) (llm)
  - act: CustomTouchEvent(state=f1588063d7a10c5c6ae92cd8f9e53c69, view=136d64e49e0c174b7cecd0cea5c3de55(MainActivity/Button-)) (rule)

### GT017 Categories

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Categories' option in the navigation drawer.; Enter the name of the new category in the text field.; Select the category type from the dropdown menu.; Tap the 'Save' button to add the new category.
- Remaining steps: Select an existing category to edit.; Enter the updated name for the category.
- Completion ratio: 0.67
- Actions taken: 12
  - act: CustomTouchEvent(state=4d7190b24045bb35508de8516c39660d, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (afford_search)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=49cbc33a715ac90beb22faa32a4eb997(MainActivity/TextView-Add Subcat)) (nav)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=49cbc33a715ac90beb22faa32a4eb997(MainActivity/TextView-Add Subcat)) (nav)
  - act: ScrollEvent(state=2f77687863312998838a7d801cd171e3, view=16a1c69f3bf35250267e3567b796aa52(MainActivity/Spinner-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=375dd1d795beda99e8ced3cebabece91, view=4855c3535ba0a0549bcd86b83a41ccc2(MainActivity/CheckedTextView-<root>)) (heuristic)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=66504947211b0967f5afa26e28736a47(MainActivity/Button-CANCEL)) (nav)
  - act: CustomTouchEvent(state=4d7190b24045bb35508de8516c39660d, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (afford_search)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (rule)

### GT018 Built-in report

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open reports
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=4d7190b24045bb35508de8516c39660d, view=56dd1af828df95f4e4137c8b37400107(MainActivity/TextView-No categor)) (heuristic)
  - act: CustomSetTextEvent(state=4d7190b24045bb35508de8516c39660d, view=611e3d5f464be1922a153e37c4f6092a(MainActivity/AutoCompleteTextView-no), text=reports) (heuristic)
  - act: CustomTouchEvent(state=fbc0b4ed5c732dcde763ea218c52e05b, view=f5e861c44530368969180e9301987e2f(MainActivity/AutoCompleteTextView-reports)) (heuristic)

### GT019 General report

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Close the report view; Tap on the 'report' navigation hint; Select 'Run a general report' from the menu
- Remaining steps: Wait for the general report to load and display; Review the report details
- Completion ratio: 0.60
- Credited from later features: GT001, GT013
- Actions taken: 7
  - act: CustomTouchEvent(state=fbc0b4ed5c732dcde763ea218c52e05b, view=f5e861c44530368969180e9301987e2f(MainActivity/AutoCompleteTextView-reports)) (nav)
  - act: CustomTouchEvent(state=fbc0b4ed5c732dcde763ea218c52e05b, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (nav)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=6018028bf369cefd455aeef77551e706(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=6018028bf369cefd455aeef77551e706(MainActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=8d2f772d21b7b12c4f92c8bf23f57045(MainActivity/TextView-<root>)) (llm)
  - act: CustomTouchEvent(state=375dd1d795beda99e8ced3cebabece91, view=4855c3535ba0a0549bcd86b83a41ccc2(MainActivity/CheckedTextView-<root>)) (heuristic)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=8d2f772d21b7b12c4f92c8bf23f57045(MainActivity/TextView-<root>)) (llm)

### GT020 Investments

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Investments' section in the Money Manager Ex app.; Select the 'Track a stock or fund' option.; Tap on the 'Add' button to save the new investment.
- Remaining steps: Enter the name or ticker of the stock or fund you want to track.; Verify the investment is listed in the 'Investments' section.
- Completion ratio: 0.60
- Credited from later features: GT001, GT005, GT014
- Actions taken: 8
  - act: CustomTouchEvent(state=375dd1d795beda99e8ced3cebabece91, view=8bb7b3404939ddebe18285905eca8c7d(MainActivity/CheckedTextView-Automobile)) (heuristic)
  - act: CustomSetTextEvent(state=c4ef29dbb9d2088fec27b96d6698dff1, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor), text=no) (rule)
  - act: CustomSetTextEvent(state=554d1a3d6e82169196ebd25cc1695856, view=61ac53568a1b845675ac5cd5df9c84e5(MainActivity/EditText-no), text=AAPL) (rule)
  - act: CustomTouchEvent(state=28b054a207a1430cf7773259cb6714c2, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=fbc0b4ed5c732dcde763ea218c52e05b, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor)) (llm)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=8d2f772d21b7b12c4f92c8bf23f57045(MainActivity/TextView-<root>)) (llm)
  - act: CustomTouchEvent(state=301035bfd5b9b2e45dcc8739f9553a0b, view=4855c3535ba0a0549bcd86b83a41ccc2(MainActivity/CheckedTextView-<root>)) (heuristic)

### GT021 Stock transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the date of the transaction.; Select 'Add a stock transaction' from the menu.; Tap on the 'Stock' navigation hint.
- Remaining steps: Enter the stock symbol.; Enter the number of shares.; Select the price per share.
- Completion ratio: 0.50
- Credited from later features: GT005, GT006, GT013
- Actions taken: 9
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor)) (llm)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor)) (llm)
  - act: ScrollEvent(state=2f77687863312998838a7d801cd171e3, view=16a1c69f3bf35250267e3567b796aa52(MainActivity/Spinner-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=301035bfd5b9b2e45dcc8739f9553a0b, view=4855c3535ba0a0549bcd86b83a41ccc2(MainActivity/CheckedTextView-<root>)) (heuristic)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor)) (llm)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor)) (llm)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor)) (llm)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (rule)

### GT022 Fixed assets

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Select the 'Fixed Assets' option; Tap on the 'Assets' section in the navigation drawer; Tap on the 'Add' button to save the new fixed asset
- Remaining steps: Enter the name of the fixed asset; Verify the fixed asset is listed in the assets section
- Completion ratio: 0.67
- Credited from later features: GT001, GT005, GT006, GT014
- Actions taken: 9
  - act: CustomTouchEvent(state=fbc0b4ed5c732dcde763ea218c52e05b, view=56dd1af828df95f4e4137c8b37400107(MainActivity/TextView-No categor)) (heuristic)
  - act: CustomTouchEvent(state=fbc0b4ed5c732dcde763ea218c52e05b, view=2daaffb870b823a5cbdae22e1dcb0673(MainActivity/ImageView-)) (heuristic)
  - act: CustomSetTextEvent(state=878dad5a22919e5ee516f44c3956487e, view=f791beeb9799f0db39d52cdc9466fc11(MainActivity/AutoCompleteTextView-   ), text=Saimon Bhuiyan) (llm)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=abcfc45bff2a0c402a7d6300bc56a713(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor)) (llm)
  - act: CustomTouchEvent(state=2f77687863312998838a7d801cd171e3, view=8d2f772d21b7b12c4f92c8bf23f57045(MainActivity/TextView-<root>)) (llm)
  - act: CustomTouchEvent(state=301035bfd5b9b2e45dcc8739f9553a0b, view=8bb7b3404939ddebe18285905eca8c7d(MainActivity/CheckedTextView-Automobile)) (heuristic)
  - act: CustomTouchEvent(state=c4ef29dbb9d2088fec27b96d6698dff1, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (rule)

### GT023 Currencies

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Currencies' option in the main menu.; Select the currency you want to manage.; Tap the 'Save' button to confirm the changes.
- Remaining steps: Enter the name of the currency you wish to add or edit.; Enter the exchange rate for the selected currency.; Verify that the currency and its rate are now visible in the currency list.
- Completion ratio: 0.50
- Credited from later features: GT007, GT017
- Actions taken: 9
  - act: CustomTouchEvent(state=7e72fb35420dfd44b347de75e08974ff, view=7cf1071646a4bb66f5199c5e1592ef24(MainActivity/TextView-Sort by na)) (llm)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=56dd1af828df95f4e4137c8b37400107(MainActivity/TextView-No categor)) (heuristic)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=56dd1af828df95f4e4137c8b37400107(MainActivity/TextView-No categor)) (heuristic)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=2daaffb870b823a5cbdae22e1dcb0673(MainActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=878dad5a22919e5ee516f44c3956487e, view=ae04332ec32374863a64bef9904707f0(MainActivity/ViewGroup-)) (llm)
  - act: CustomTouchEvent(state=a1116d2ff924d02ad758f84227effc15, view=70d66a1dadce077c8e0c676fd6e7c915(MainActivity/CheckedTextView-j)) (heuristic)
  - act: CustomTouchEvent(state=27198fc7af8546076653ad7c445bcc91, view=d1628afcc7ae6dfc6bf1ce01298470a8(MainActivity/TextView-Edit)) (llm)
  - act: CustomTouchEvent(state=ab8c7d4b33c0bfac2af3a9a4c20705e9, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (rule)

### GT024 Sync

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the desired sync frequency; Tap on the 'Sync' navigation hint; Select 'Open sync settings'
- Remaining steps: Enter the required credentials if prompted; Confirm the sync settings; Wait for the sync to complete
- Completion ratio: 0.50
- Credited from later features: GT006, GT013, GT018
- Actions taken: 9
  - act: CustomTouchEvent(state=27198fc7af8546076653ad7c445bcc91, view=b3085cdb81d758be1c286e40f8ed0ba6(MainActivity/TextView-Leisure:Mo)) (rule)
  - act: CustomTouchEvent(state=27198fc7af8546076653ad7c445bcc91, view=b3085cdb81d758be1c286e40f8ed0ba6(MainActivity/TextView-Leisure:Mo)) (rule)
  - act: CustomTouchEvent(state=27198fc7af8546076653ad7c445bcc91, view=fe56a52c8e60ef7173de78fd65b4ccff(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=27198fc7af8546076653ad7c445bcc91, view=fe56a52c8e60ef7173de78fd65b4ccff(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=27198fc7af8546076653ad7c445bcc91, view=32e7fa55069bfd5828b54dd39ded136e(MainActivity/TextView-Add Subcat)) (rule)
  - act: CustomTouchEvent(state=44a60f24f437001ee4c6f158235c8357, view=c21fe6081f494ceabb198e9912677542(MainActivity/TextView-Leisure:Mo)) (llm)
  - act: CustomTouchEvent(state=4719b99bac2c3dbdb6966165c771b07f, view=0531c62234835ad1b98e61152c2a2942(MainActivity/CheckedTextView-Leisure:Mo)) (heuristic)
  - act: CustomTouchEvent(state=44a60f24f437001ee4c6f158235c8357, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (rule)

### GT025 Database password

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap the 'Save' button to set the new password; Navigate to the settings menu; Select 'Database password' from the settings
- Remaining steps: Enter the new database password; Confirm the new password by re-entering it
- Completion ratio: 0.67
- Credited from later features: GT001, GT017, GT028
- Actions taken: 9
  - act: CustomTouchEvent(state=8476e9bdb38cdd1f9d910daecd316efe, view=c39271cdbdebd0fb93d3bc066b8bb84e(MainActivity/TextView-Leisure:Vi)) (rule)
  - act: CustomTouchEvent(state=8476e9bdb38cdd1f9d910daecd316efe, view=c39271cdbdebd0fb93d3bc066b8bb84e(MainActivity/TextView-Leisure:Vi)) (rule)
  - act: CustomTouchEvent(state=8476e9bdb38cdd1f9d910daecd316efe, view=fe56a52c8e60ef7173de78fd65b4ccff(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=8476e9bdb38cdd1f9d910daecd316efe, view=fe56a52c8e60ef7173de78fd65b4ccff(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=8476e9bdb38cdd1f9d910daecd316efe, view=32e7fa55069bfd5828b54dd39ded136e(MainActivity/TextView-Add Subcat)) (rule)
  - act: CustomSetTextEvent(state=67fd4917d1f325254833c5572d6eff1a, view=3a264312b512883540c4e27a39ae1fda(MainActivity/EditText-Subcategor), text=your_password) (rule)
  - act: CustomTouchEvent(state=2e27c77b3f73689e48d97ff3a24ff100, view=88d7346783afedac74c750e7fac56cbd(MainActivity/EditText-your_passw)) (nav)
  - act: CustomTouchEvent(state=2e27c77b3f73689e48d97ff3a24ff100, view=b0b5177950a3ee7dad8ad9e9a75ded8f(MainActivity/Button-OK)) (rule)

### GT026 Fingerprint lock

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Select the 'Security' option; Navigate to the settings menu
- Remaining steps: Tap on 'Fingerprint lock'; Enable the fingerprint lock; Confirm the lock settings
- Completion ratio: 0.50
- Credited from later features: GT001, GT005, GT028
- Actions taken: 11
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=2daaffb870b823a5cbdae22e1dcb0673(MainActivity/ImageView-)) (afford_search)
  - act: CustomSetTextEvent(state=0c73cc065dc4c2407c7585913cf2afb8, view=f791beeb9799f0db39d52cdc9466fc11(MainActivity/AutoCompleteTextView-   ), text=Saimon Bhuiyan) (llm)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (rule)
  - act: ScrollEvent(state=58884ef3be1c749742c68ff4f338f92d, view=3d0da6020df9c26a32aa108fcb4464bd(MainActivity/ExpandableListView-), direction=left) (rule)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (rule)
  - act: ScrollEvent(state=58884ef3be1c749742c68ff4f338f92d, view=3d0da6020df9c26a32aa108fcb4464bd(MainActivity/ExpandableListView-), direction=left) (rule)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=136d64e49e0c174b7cecd0cea5c3de55(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=7e72fb35420dfd44b347de75e08974ff, view=193690f5f9169553ff37dcfdad9e2711(MainActivity/CheckBox-)) (heuristic)

### GT027 Import export

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Wait for the import to complete and verify the new data in the app's main screen.; Tap on the 'Import or export a file' option in the navigation drawer.; Select the 'Import' option from the dropdown menu.; Enter the path to the QIF or CSV file you want to import.; Select the file type from the dropdown menu (QIF or CSV).
- Remaining steps: Tap the 'Import' button to start the import process.
- Completion ratio: 0.83
- Actions taken: 9
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=136d64e49e0c174b7cecd0cea5c3de55(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=fbb1519ab6730488fc1c585985710979, view=f2afaa9517e74f37f98576758140b978(MainActivity/TextView-Navigation)) (heuristic)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=136d64e49e0c174b7cecd0cea5c3de55(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=5fe6b60bf7a36833492c1ac0704b98a0, view=2ed9c23b1c526354498294c6550aae86(MainActivity/TextView-Sort by re)) (heuristic)
  - act: CustomSetTextEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=43b71a6e44f22650d96a72325cba1683(MainActivity/AutoCompleteTextView-Saimon Bhu), text=Saimon Bhuiyan) (mandatory_fill)
  - act: CustomSetTextEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=43b71a6e44f22650d96a72325cba1683(MainActivity/AutoCompleteTextView-Saimon Bhu), text=Saimon Bhuiyan) (mandatory_fill)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=136d64e49e0c174b7cecd0cea5c3de55(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=5fe6b60bf7a36833492c1ac0704b98a0, view=7cf1071646a4bb66f5199c5e1592ef24(MainActivity/TextView-Sort by na)) (rule)

### GT028 Settings

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap the settings icon in the app's navigation bar.; Select the 'Settings' option from the menu.; Enter the settings page.
- Remaining steps: Tap the 'General' option to access the app settings.
- Completion ratio: 0.75
- Actions taken: 7
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=136d64e49e0c174b7cecd0cea5c3de55(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=5fe6b60bf7a36833492c1ac0704b98a0, view=f2afaa9517e74f37f98576758140b978(MainActivity/TextView-Navigation)) (heuristic)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=136d64e49e0c174b7cecd0cea5c3de55(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=fbb1519ab6730488fc1c585985710979, view=2ed9c23b1c526354498294c6550aae86(MainActivity/TextView-Sort by re)) (heuristic)
  - act: CustomSetTextEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=43b71a6e44f22650d96a72325cba1683(MainActivity/AutoCompleteTextView-Saimon Bhu), text=Saimon Bhuiyan) (mandatory_fill)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=136d64e49e0c174b7cecd0cea5c3de55(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=fbb1519ab6730488fc1c585985710979, view=7cf1071646a4bb66f5199c5e1592ef24(MainActivity/TextView-Sort by na)) (rule)

### F029 Set default account

- Status: **pending**
- Feature source: action_inferred
- Remaining steps: click; select; save
- Completion ratio: 0.00

### F030 Select currency

- Status: **pending**
- Feature source: action_inferred
- Remaining steps: click; select; save
- Completion ratio: 0.00

### F031 Set initial balance

- Status: **pending**
- Feature source: action_inferred
- Remaining steps: click; select; save
- Completion ratio: 0.00

### F032 Set account status

- Status: **pending**
- Feature source: action_inferred
- Remaining steps: click; select; save
- Completion ratio: 0.00

### F033 Set account type

- Status: **pending**
- Feature source: action_inferred
- Remaining steps: click; select; save
- Completion ratio: 0.00

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
