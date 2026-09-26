# Feature test report: Money Manager Ex

- Started: 2026-08-27 04:19:47
- Finished: 2026-08-27 05:14:11
- Features: 30
- Covered: 8
- Partial: 22
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 69% (mean completion ratio; the headline number)
- Coverage: 27% (features with every guide step matched)
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

- Filled via credential.txt: 12
- Filled via VLM/Gemini: 18
- Unresolved: 0
- Online coverage: 27% (8/30) — live journal self-report (covered / extracted features).
- Offline coverage: 21% (6 covered / 28; 11 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 37% (mean completion ratio).

## Findings

### GT001 New database

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Create a database' option; Enter a name for the new database; Tap the 'Create' button to finalize the new database creation
- Completion ratio: 1.00
- Credited from later features: GT003
- Actions taken: 12
  - act: CustomTouchEvent(state=967325bb19d8b40560a7364d0acb7f45, view=e775d76c9d80720909bf1f0537d19984(PasswordActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomSetTextEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=testcube.mmb) (mandatory_fill)
  - act: CustomTouchEvent(state=70e35bfe537da43808c8caeaf9c64ab7, x=55, y=1267) (llm)
  - act: CustomTouchEvent(state=8df8e220ff60f4cd5119531be05cd3b2, view=37362f0c98e81a88235637356c0038f7(AccountEditActivity/CheckedTextView-Closed)) (llm)
  - act: CustomTouchEvent(state=b0a2c58698c6131a57a9f5b29691a6e5, x=55, y=1267) (llm)
  - act: CustomTouchEvent(state=bca8df489aae4d3086ef3b64b8e319e9, view=fbb40af8f27338c49b8f6301d3d130a3(AccountEditActivity/CheckedTextView-Closed)) (llm)
  - act: CustomTouchEvent(state=b0a2c58698c6131a57a9f5b29691a6e5, view=bb86e327742730bf5b70c64b26b767ad(AccountEditActivity/Spinner-)) (llm)

### GT002 New account

- Status: **partial**
- Reason: Onboarding already finished; main screen is visible.
- Feature source: guide
- Completed steps: Tap the 'Save' button to create the new account.; Tap on the 'New account' option in the account creation section.
- Remaining steps: Enter the account name in the provided field.; Select the account type from the dropdown menu.; Enter the account number in the designated field.
- Completion ratio: 0.40
- Credited from later features: GT003, GT007

### GT003 Add transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the 'Save' button to add the transaction
- Remaining steps: Tap on the 'Add a transaction' button; Enter the amount of the transaction; Select the type of transaction (income or expense); Enter the description of the transaction
- Completion ratio: 0.20
- Credited from later features: GT025
- Actions taken: 7
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (nav)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (nav)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomSetTextEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=1) (llm)
  - act: CustomTouchEvent(state=7b98a94ff926716a5d233faf11240cf2, view=4f14a0dcaca0feb8d4b8dfec578791ba(AccountEditActivity/EditText-1)) (llm)
  - act: CustomTouchEvent(state=7b98a94ff926716a5d233faf11240cf2, view=4f14a0dcaca0feb8d4b8dfec578791ba(AccountEditActivity/EditText-1)) (llm)
  - act: ScrollEvent(state=7b98a94ff926716a5d233faf11240cf2, view=19f9c4b484370144fb4bac21c98e5e1b(AccountEditActivity/ScrollView-), direction=up) (afford_search)

### GT004 Edit transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the transaction you want to edit in the transaction list.; Select the edit option for the transaction.; Tap the save button to update the transaction.
- Remaining steps: Enter the new amount or description as needed.; Verify the updated transaction in the transaction list.
- Completion ratio: 0.60
- Credited from later features: GT005, GT025
- Actions taken: 10
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=3317d3816fa0e3c5c32288ae628299c3, x=154, y=259) (llm)
  - act: CustomTouchEvent(state=3317d3816fa0e3c5c32288ae628299c3, x=198, y=608) (llm)
  - act: CustomTouchEvent(state=86070183d449b76364b8d8c2c478edb4, x=25, y=25) (llm)
  - act: CustomTouchEvent(state=86070183d449b76364b8d8c2c478edb4, x=154, y=299) (llm)
  - act: CustomTouchEvent(state=86070183d449b76364b8d8c2c478edb4, view=9e278810123d6fc7d5b1b145c0345498(MainActivity/CheckedTextView-o)) (afford_search)
  - act: CustomTouchEvent(state=d5f7af379b2823f707868240265f6b56, view=588e1a5a3bf1f2b4ca0d4a578f0916ca(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (rule)

### GT005 Filter by date

- Status: **covered**
- Reason: Hit the per-feature step limit. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap on the 'Filter transactions by date' option in the menu.; Select the 'Date' filter option.; Enter the start date for the filter.; Enter the end date for the filter.; Tap the 'Apply' button to apply the date range filter.
- Completion ratio: 1.00
- Actions taken: 13
  - act: CustomTouchEvent(state=57331b671feb1e19c9b9c54df26f475e, view=8e13be37d3aecd28da0f36185b80b3f9(SearchActivity/TextView-Thu, Aug 2)) (heuristic)
  - act: CustomTouchEvent(state=407f9efe84e9702a4f16629e43853018, view=65361cf58c4eab0a92019b9b6c9b1a67(SearchActivity/View-1)) (heuristic)
  - act: CustomTouchEvent(state=d05efe82db9393d32c2e5475da48614f, view=354c500cc1feb24fd4b16148b03de8b8(SearchActivity/TextView-Sat, Aug 1)) (heuristic)
  - act: CustomTouchEvent(state=d05efe82db9393d32c2e5475da48614f, view=354c500cc1feb24fd4b16148b03de8b8(SearchActivity/TextView-Sat, Aug 1)) (heuristic)
  - act: CustomTouchEvent(state=d05efe82db9393d32c2e5475da48614f, view=7962440a3a2fc87e7095c9c75d07f9f6(SearchActivity/Button-OK)) (rule)
  - act: CustomSetTextEvent(state=98504b45f8f4a3557475a1a04d32e3ba, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=1234567890) (mandatory_fill)
  - act: CustomSetTextEvent(state=aef8ecd987952d69bb03e3981e209dae, view=94e39d333c036b9c6fa7e13c52afa8d4(SearchActivity/EditText-1234567890), text=1234567890) (mandatory_fill)
  - act: CustomTouchEvent(state=aef8ecd987952d69bb03e3981e209dae, view=d8a4d69ebd4e269c8847bef737282b84(SearchActivity/TextView-From Date)) (heuristic)

### GT006 Search transactions

- Status: **covered**
- Reason: Hit the per-feature step limit. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap on the 'Search' icon in the navigation bar.; Enter the search term in the search bar.; Press the 'Enter' key to execute the search.; Select the desired transaction from the search results.; Tap on the 'Sort' button to sort the transactions.; Select the sorting option from the dropdown menu.
- Completion ratio: 1.00
- Credited from later features: GT005
- Actions taken: 13
  - act: ScrollEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=94bce4df792f0ec0434d9099eec56d07(SearchActivity/Spinner-), direction=up) (afford_search)
  - act: CustomTouchEvent(state=cdfc3f9684068fba58cbfb67f0038cc6, view=836d6ceefdbb966f35964db24ebd17e0(SearchActivity/CheckedTextView-Duplicate)) (llm)
  - act: CustomTouchEvent(state=9f4c9eb0cd5a351ea53a347fffac6a64, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=9f4c9eb0cd5a351ea53a347fffac6a64, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=a77ab87c8cb6103cfe2c8747ad2f2a12(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=2cc65d47aaa2d183602e4845ba84f5ae, view=dfb3ee4bfbc79fd337920c5692bd781d(SearchActivity/TextView-Sort by da)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (rule)

### GT007 Favorite account

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Select the account you want to mark as favorite; Tap on the 'Favorite' option in the account details; Confirm the favorite status by tapping the confirmation button
- Completion ratio: 1.00
- Actions taken: 5
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomTouchEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=ccea967a8b318016bd7714c304944e97(AccountEditActivity/TextView-ACCOUNT ST)) (heuristic)

### GT008 Manage accounts

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the 'Accounts' option in the navigation drawer.; Select the account you wish to edit from the account list.; Make the necessary edits to the account details.; Tap the 'Save' button to confirm the changes.
- Remaining steps: Tap the 'Edit' button next to the account you selected.
- Completion ratio: 0.80
- Credited from later features: GT004, GT007
- Actions taken: 10
  - act: ScrollEvent(state=db5b1d197ef9cefaa4110e8cf054557c, view=3d0da6020df9c26a32aa108fcb4464bd(MainActivity/ExpandableListView-), direction=left) (rule)
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
- Completed steps: Open the app; Tap on 'Open budgets'; Select 'Create a budget'; Select a budget category; Set a budget amount
- Remaining steps: Enter a budget name
- Completion ratio: 0.83
- Credited from later features: GT001, GT007, GT010
- Actions taken: 10
  - act: CustomTouchEvent(state=1d2c8d0e99369d19862285baf984115d, view=e763328a8146b453f52a744eba4a137c(BudgetSettingsActivity/TextView-If checked)) (heuristic)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=e763328a8146b453f52a744eba4a137c(BudgetSettingsActivity/TextView-If checked)) (heuristic)
  - act: CustomTouchEvent(state=1d2c8d0e99369d19862285baf984115d, view=e763328a8146b453f52a744eba4a137c(BudgetSettingsActivity/TextView-If checked)) (heuristic)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=b57e34fd16cbc40f969d64aeb6cc580d(BudgetSettingsActivity/TextView-Budget)) (rule)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=1bce12574a887f35292c5a2a2fca3c6d(BudgetSettingsActivity/TextView-Show simpl)) (rule)
  - act: CustomTouchEvent(state=c0b0bfbb809294eb235852e73709bb73, view=e763328a8146b453f52a744eba4a137c(BudgetSettingsActivity/TextView-If checked)) (heuristic)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=e763328a8146b453f52a744eba4a137c(BudgetSettingsActivity/TextView-If checked)) (heuristic)
  - act: CustomTouchEvent(state=c0b0bfbb809294eb235852e73709bb73, view=62387459b3851ce330304a4b9a3d0c62(BudgetSettingsActivity/TextView-If checked)) (rule)

### GT010 Budget amount

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Budget' section in the navigation drawer.; Select the 'Edit a budget amount' option.; Tap the 'Save' button to confirm the budget amount.
- Remaining steps: Enter the desired budget amount in the input field.; Verify that the budget amount is correctly updated in the app.
- Completion ratio: 0.60
- Credited from later features: GT025
- Actions taken: 7
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=206b3bb71772a92bb536e53f25173c50(MainActivity/Button-SETTINGS)) (rule)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=d44405fcb405adc05ad761463a792339(SettingsActivity/TextView-Budget)) (heuristic)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=7bdd1bd4f5746666becd8bac2d52096e(BudgetSettingsActivity/TextView-Use financ)) (heuristic)
  - act: CustomTouchEvent(state=1d2c8d0e99369d19862285baf984115d, view=7bdd1bd4f5746666becd8bac2d52096e(BudgetSettingsActivity/TextView-Use financ)) (heuristic)
  - act: CustomTouchEvent(state=7c0814a4c14bf2e2ef44cd216f8b635b, view=7bdd1bd4f5746666becd8bac2d52096e(BudgetSettingsActivity/TextView-Use financ)) (heuristic)
  - act: CustomTouchEvent(state=1d2c8d0e99369d19862285baf984115d, view=b57e34fd16cbc40f969d64aeb6cc580d(BudgetSettingsActivity/TextView-Budget)) (rule)
  - act: CustomTouchEvent(state=1d2c8d0e99369d19862285baf984115d, view=1bce12574a887f35292c5a2a2fca3c6d(BudgetSettingsActivity/TextView-Show simpl)) (rule)

### GT011 Budget details

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Select the 'View Budget Details' option.; Tap on the 'Budget Details' section in the main menu.; Tap on the 'Transactions' tab to view related transactions.; Scroll down to see more budget details and related transactions.
- Completion ratio: 1.00
- Credited from later features: GT005, GT010, GT014
- Actions taken: 8
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=9c16c88499f3682493ec99ea4d30819c(MainActivity/TextView-your_data_)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=9c16c88499f3682493ec99ea4d30819c(MainActivity/TextView-your_data_)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1bc77b2100105e9d823d2672d4dbcaa9(MainActivity/TextView-Current da)) (rule)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1bc77b2100105e9d823d2672d4dbcaa9(MainActivity/TextView-Current da)) (rule)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)

### GT012 Delete budget

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the budget you want to delete; Select the 'Delete' option; Confirm the deletion by tapping 'Yes'; Select the 'Budgets' section
- Completion ratio: 1.00
- Credited from later features: GT001, GT004, GT005, GT007, GT014
- Actions taken: 8
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=72faf18250cd3c6df446eb3e21594e45(MainActivity/TextView-/storage/e)) (rule)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=72faf18250cd3c6df446eb3e21594e45(MainActivity/TextView-/storage/e)) (rule)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=edc7fb7fe1766dc6d0be605a14690c32(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=edc7fb7fe1766dc6d0be605a14690c32(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: CustomSetTextEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=8bcd308b8146e2d2f0591bd37449b85a(AccountEditActivity/EditText-Account nu), text=1234567890) (rule)
  - act: CustomSetTextEvent(state=453e913c304ec9b57cb43dc1caa2d015, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=testcube.mmb) (rule)
  - act: CustomTouchEvent(state=6f1663fd889d70d58bd788369dc591a6, view=44e793bd4cb64fb1c3cc43b013194efd(AccountEditActivity/TextView-SELECT CUR)) (rule)

### GT013 Budget view options

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the desired budget view option from the list.; Tap on the 'Save' button to apply the changes.; Tap on the 'Budget' navigation hint.; Select 'Change budget view options' from the dropdown menu.
- Remaining steps: Tap on the 'Budget view options' menu item.
- Completion ratio: 0.80
- Credited from later features: GT005, GT010, GT025
- Actions taken: 9
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (rule)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (rule)
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=1234567890) (rule)
  - act: CustomTouchEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=ce9f8bae7c1a3d996903712060ff7906(SearchActivity/TextView-STATUS)) (llm)
  - act: CustomSetTextEvent(state=b8bcdcaf393abc604d38daa72d0edef1, view=94e39d333c036b9c6fa7e13c52afa8d4(SearchActivity/EditText-1234567890), text=testcube.mmb) (rule)
  - act: CustomTouchEvent(state=2794d6d85703953b233d3d7223a9772b, view=3d99f9a62783b30bfc02b7a74366a277(SearchActivity/TextView-)) (llm)

### GT014 Scheduled transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Transactions' section; Select 'Add Transaction'; Tap on 'Recurring'; Tap on 'Save'
- Remaining steps: Enter the details for the recurring transaction
- Completion ratio: 0.83
- Credited from later features: GT006, GT015, GT025
- Actions taken: 9
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: CustomSetTextEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=8bcd308b8146e2d2f0591bd37449b85a(AccountEditActivity/EditText-Account nu), text=1234567890) (llm)
  - act: CustomSetTextEvent(state=453e913c304ec9b57cb43dc1caa2d015, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=testcube.mmb) (llm)
  - act: CustomTouchEvent(state=6f1663fd889d70d58bd788369dc591a6, x=154, y=145) (llm)
  - act: CustomSetTextEvent(state=6f1663fd889d70d58bd788369dc591a6, view=624b5b32f5baf3cdfd8f063c867d4d5d(AccountEditActivity/EditText-testcube.m), text=testcube.mmb) (llm)
  - act: ScrollEvent(state=6f1663fd889d70d58bd788369dc591a6, view=19f9c4b484370144fb4bac21c98e5e1b(AccountEditActivity/ScrollView-), direction=up) (afford_search)

### GT015 Recurring prompt

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Navigate to the Transactions section; Select the recurring transactions tab
- Remaining steps: Locate the specific recurring transaction prompt; Tap on the prompt to confirm the due transaction
- Completion ratio: 0.60
- Actions taken: 10
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomTouchEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=4618be4242a107570e85ecb13b8f0d1e, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=e4a9c793ec08772d338546370e0a106e, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=4ebf91aa9e738c367d48b43c65eec164, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=9021cc71ab9d224f2add11077c7eda12, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=d7cfc8d96924543decb85ae6be4e1955, x=55, y=1267) (llm)

### GT016 Payees

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open payees; Tap on the 'Add' button to add a new payee; Tap the 'Save' button to add the payee
- Remaining steps: Enter the payee's name in the text field; Select the payee type from the dropdown menu; Enter the payee's bank account details
- Completion ratio: 0.50
- Credited from later features: GT001, GT003, GT025
- Actions taken: 9
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (rule)
  - act: CustomTouchEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=4618be4242a107570e85ecb13b8f0d1e, x=44, y=594) (llm)
  - act: CustomTouchEvent(state=3137910ef05fcf2015d0bd5dc4a5da99, view=1060431a33ee8b34cf735afd4bbb54e7(AccountEditActivity/CheckedTextView-Cash)) (rule)
  - act: CustomTouchEvent(state=4618be4242a107570e85ecb13b8f0d1e, x=44, y=694) (llm)
  - act: CustomTouchEvent(state=4618be4242a107570e85ecb13b8f0d1e, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na)) (rule)

### GT017 Categories

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Categories' option in the navigation drawer.; Tap on the 'Save' button to confirm the category addition or edit.
- Remaining steps: Enter the name of the new category or select an existing category to edit.; Verify that the new or edited category is visible in the list of categories.
- Completion ratio: 0.50
- Credited from later features: GT008, GT025
- Actions taken: 7
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, x=33, y=1655) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, x=33, y=1655) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: CustomTouchEvent(state=2847f301b08474c846ac0b4f5f865bc4, x=44, y=1195) (llm)
  - act: CustomTouchEvent(state=2847f301b08474c846ac0b4f5f865bc4, x=44, y=1195) (llm)
  - act: ScrollEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=19f9c4b484370144fb4bac21c98e5e1b(AccountEditActivity/ScrollView-), direction=up) (afford_search)

### GT018 Built-in report

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Select the 'Built-in Report' option; Tap on the 'Reports' section in the navigation drawer
- Completion ratio: 1.00
- Credited from later features: GT005, GT008
- Actions taken: 9
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: CustomTouchEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=2b8297bbfe0f9040fa96924ca5423e59(AccountEditActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e9675520ae190f6731e929bc617799f1(SearchActivity/TextView-Select Pay)) (rule)

### GT019 General report

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the 'General report' option from the report menu.
- Remaining steps: Tap on the 'report' navigation hint.; Tap on the 'Run a general report' button.
- Completion ratio: 0.33
- Credited from later features: GT005
- Actions taken: 10
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=206b3bb71772a92bb536e53f25173c50(MainActivity/Button-SETTINGS)) (rule)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=0da48a853941316ac05626092291c120(SettingsActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=206b3bb71772a92bb536e53f25173c50(MainActivity/Button-SETTINGS)) (llm)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=b30c212038bd33508574f56ed8b2ed2f(SettingsActivity/TextView-Look & Fee)) (rule)
  - act: CustomTouchEvent(state=957e36314592b1d9bc9071e7838a5e43, view=8857a4b15de03aab06713e965cd6c4cd(LookFeelSettingsActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=78c738d8402e11945f32d0b47afd7ac9(SettingsActivity/TextView-General)) (rule)
  - act: CustomTouchEvent(state=c6a27efb5e0bd6a96dce76e8ab21bb42, view=e10f8a3f37f86db158a570e15a2f2674(GeneralSettingsActivity/ImageButton-)) (rule)

### GT020 Investments

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Investments' section; Tap on the 'Save' button to track the investment
- Remaining steps: Select the 'Track a stock or fund' feature; Enter the name or ticker of the stock or fund to track
- Completion ratio: 0.60
- Credited from later features: GT010, GT025
- Actions taken: 8
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (llm)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (rule)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=9c16c88499f3682493ec99ea4d30819c(MainActivity/TextView-your_data_)) (llm)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=9c16c88499f3682493ec99ea4d30819c(MainActivity/TextView-your_data_)) (llm)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (llm)

### GT021 Stock transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select 'Add a stock transaction' from the menu.; Tap on the 'Stock' option in the navigation drawer.; Tap the 'Save' button to add the transaction.
- Remaining steps: Enter the stock symbol.; Enter the number of shares.; Enter the price per share.
- Completion ratio: 0.50
- Credited from later features: GT006, GT008, GT025
- Actions taken: 8
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, x=33, y=1655) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, x=33, y=1655) (llm)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (rule)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=edc7fb7fe1766dc6d0be605a14690c32(MainActivity/View-)) (llm)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=1bc77b2100105e9d823d2672d4dbcaa9(MainActivity/TextView-Current da)) (rule)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=1bc77b2100105e9d823d2672d4dbcaa9(MainActivity/TextView-Current da)) (rule)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (rule)

### GT022 Fixed assets

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Assets' section in the main menu.; Select the 'Fixed Assets' option.; Tap on the 'Save' button to record the fixed asset.
- Remaining steps: Enter the name of the fixed asset.; Input the initial value of the asset.
- Completion ratio: 0.60
- Credited from later features: GT005, GT025
- Actions taken: 7
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=070ef00ba28323861f05979a924d99f9(SearchActivity/TextView-Select Tag)) (llm)
  - act: CustomTouchEvent(state=02888c0f4cc2d525464b94d09d2590c2, view=e9912daba18070a8344abac8585b66c5(TagActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=a305ec2fc8b86b3dfdf3a8e7963b793c, view=c4f0995ee6b9a30e3efe2869541cd1f0(TagActivity/EditText-Tag name)) (llm)
  - act: CustomTouchEvent(state=a305ec2fc8b86b3dfdf3a8e7963b793c, view=c4f0995ee6b9a30e3efe2869541cd1f0(TagActivity/EditText-Tag name)) (llm)
  - act: CustomTouchEvent(state=a305ec2fc8b86b3dfdf3a8e7963b793c, view=3c7129e47e4799cf7a91a2a4f4a1d27b(TagActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=02888c0f4cc2d525464b94d09d2590c2, view=e9912daba18070a8344abac8585b66c5(TagActivity/FloatingActionButton-)) (afford_search)

### GT023 Currencies

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Select the currency you want to manage; Tap on the 'Save' button to confirm the changes; Tap on the 'Currencies' section
- Remaining steps: Enter the new currency rate
- Completion ratio: 0.80
- Credited from later features: GT007, GT010
- Actions taken: 8
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=72faf18250cd3c6df446eb3e21594e45(MainActivity/TextView-/storage/e)) (rule)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=72faf18250cd3c6df446eb3e21594e45(MainActivity/TextView-/storage/e)) (rule)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=edc7fb7fe1766dc6d0be605a14690c32(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=b44b6853186518f76cb582f39dfba1a1, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: CustomTouchEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=44e793bd4cb64fb1c3cc43b013194efd(AccountEditActivity/TextView-SELECT CUR)) (nav)
  - act: CustomTouchEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=44e793bd4cb64fb1c3cc43b013194efd(AccountEditActivity/TextView-SELECT CUR)) (nav)

### GT024 Sync

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Select the 'Settings' option; Tap on the 'Sync' settings; Navigate to the main menu; Select 'Open sync settings'
- Remaining steps: Scroll down to find the 'Sync' settings
- Completion ratio: 0.83
- Credited from later features: GT001, GT005, GT009, GT022, GT025
- Actions taken: 8
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: CustomSetTextEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=bb7c7972e5c4d268205937de196dc0ee(AccountEditActivity/EditText-Notes), text=no) (nav)
  - act: CustomSetTextEvent(state=102213f1db2ebb7d7769fb3b2dc95ca6, view=e9177cd673e4455c991b98ed19ee3e2c(AccountEditActivity/EditText-no), text=no) (nav)
  - act: CustomSetTextEvent(state=102213f1db2ebb7d7769fb3b2dc95ca6, view=e9177cd673e4455c991b98ed19ee3e2c(AccountEditActivity/EditText-no), text=no) (nav)
  - act: CustomTouchEvent(state=102213f1db2ebb7d7769fb3b2dc95ca6, view=2b8297bbfe0f9040fa96924ca5423e59(AccountEditActivity/ImageButton-)) (rule)

### GT025 Database password

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the 'Settings' icon in the top right corner of the app.; Select 'Database' from the settings menu.; Tap on 'Database Password' to proceed.; Enter the new database password in the password field.; Confirm the new password by re-entering it in the confirmation field.; Tap on the 'Save' button to apply the changes.
- Completion ratio: 1.00
- Actions taken: 8
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1bc77b2100105e9d823d2672d4dbcaa9(MainActivity/TextView-Current da)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=1bc77b2100105e9d823d2672d4dbcaa9(MainActivity/TextView-Current da)) (heuristic)
  - act: CustomTouchEvent(state=b15108e6865afcce018c5b0dbed14e33, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (afford_search)
  - act: CustomSetTextEvent(state=2847f301b08474c846ac0b4f5f865bc4, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=your_password) (mandatory_fill)
  - act: CustomSetTextEvent(state=d545b097991f0bbc1929e6352c8618ab, view=f49a5222d4d191941de26049903340c7(AccountEditActivity/EditText-your_passw), text=your_password) (mandatory_fill)
  - act: CustomTouchEvent(state=d545b097991f0bbc1929e6352c8618ab, view=74a93b20fe872e1ae9ec33afdd0c5493(AccountEditActivity/Button-)) (heuristic)

### GT026 Fingerprint lock

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Select the 'Security' option; Navigate to the settings menu
- Remaining steps: Tap on 'Fingerprint lock'; Enable fingerprint lock; Confirm the fingerprint lock setup
- Completion ratio: 0.50
- Credited from later features: GT001, GT005, GT025
- Actions taken: 9
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=6afd2ddae0afe2ff010e275a4a390d1c(IncomeVsExpensesActivity/RadioButton-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=4ef5fc8a3f01d24bad3ebeff464fd821(IncomeVsExpensesActivity/TextView-Select Acc)) (rule)
  - act: CustomTouchEvent(state=d52057ba7f84942f39c06b38d872b313, view=9aa553333936f841aae6c4539a644236(IncomeVsExpensesActivity/CheckedTextView-your_passw)) (rule)
  - act: CustomTouchEvent(state=b507a32f91221300d07414f0b8c3aa7e, view=b96ef268502e0ab7f6a634754c43d2ba(IncomeVsExpensesActivity/View-)) (llm)
  - act: CustomTouchEvent(state=b507a32f91221300d07414f0b8c3aa7e, view=b96ef268502e0ab7f6a634754c43d2ba(IncomeVsExpensesActivity/View-)) (llm)
  - act: CustomTouchEvent(state=b507a32f91221300d07414f0b8c3aa7e, view=2928503e93598979461cdc02990dea9f(IncomeVsExpensesActivity/Button-OK)) (rule)

### GT027 Import export

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap on the 'Import or export a file' option in the navigation drawer.; Select 'Import' from the dropdown menu.
- Remaining steps: Tap on the 'QIF' or 'CSV' file type you want to import.; Locate and select the file you want to import from your device.; Tap on the 'Import' button to start the import process.; Wait for the import to complete and check the app state for any changes.
- Completion ratio: 0.33
- Credited from later features: GT008, GT025
- Actions taken: 8
  - act: CustomTouchEvent(state=4613f2448dfd9d979b6da01ab35707fd, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=19ee481c4531b725329e5dd41ed6a159(SearchActivity/TextView-Search)) (rule)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=19ee481c4531b725329e5dd41ed6a159(SearchActivity/TextView-Search)) (rule)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=b98f92eb6768411b3869dc288a3e1915(SearchActivity/FloatingActionButton-)) (afford_search)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=b98f92eb6768411b3869dc288a3e1915(SearchActivity/FloatingActionButton-)) (afford_search)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=48264a250017bd399f3abd5f8c3e487e(SearchActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=a77ab87c8cb6103cfe2c8747ad2f2a12(SearchActivity/Button-)) (rule)

### GT028 Settings

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Select the 'Settings' option from the app's main menu; Tap on the 'Settings' option in the navigation drawer; Tap on the app icon to open the Money Manager Ex app; Select the 'Settings' option from the main menu; Tap on the 'Settings' option in the navigation drawer to open the settings menu
- Remaining steps: Enter the settings menu by selecting the 'Settings' option
- Completion ratio: 0.83
- Credited from later features: GT001, GT005, GT008
- Actions taken: 6
  - act: CustomTouchEvent(state=4613f2448dfd9d979b6da01ab35707fd, view=7c77d5e9d33904a1db7e01727c86a8a0(MainActivity/ProgressBar-)) (heuristic)
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=0a9d730e29137793e1ffc3da5c595574, view=78374ff278a2c4fcebfc80ef817a6550(IncomeVsExpensesActivity/TextView-All Time)) (heuristic)
  - act: (screen already shows this destination) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (llm)

### F029 Set initial balance

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: action_inferred
- Completed steps: Save
- Remaining steps: editTextInitialBalance; editTextInitialBalance
- Completion ratio: 0.33
- Credited from later features: GT025
- Actions taken: 7
  - act: CustomTouchEvent(state=4613f2448dfd9d979b6da01ab35707fd, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=4613f2448dfd9d979b6da01ab35707fd, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=4613f2448dfd9d979b6da01ab35707fd, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=1e0f20e758d4dddb58ed0a07f70ab327, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=1e0f20e758d4dddb58ed0a07f70ab327, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=1e0f20e758d4dddb58ed0a07f70ab327, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=4613f2448dfd9d979b6da01ab35707fd, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (heuristic)

### F030 Set account status

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: action_inferred
- Completed steps: Save
- Remaining steps: spinnerAccountStatus; spinnerAccountStatus
- Completion ratio: 0.33
- Credited from later features: GT025
- Actions taken: 3
  - act: CustomTouchEvent(state=4613f2448dfd9d979b6da01ab35707fd, view=0acee545b4b31b45aba42f12c040452b(MainActivity/TextView-Cash Accou)) (heuristic)
  - act: CustomTouchEvent(state=b14b7f3df8d87b088392f50dd4ab3c80, view=0acee545b4b31b45aba42f12c040452b(MainActivity/TextView-Cash Accou)) (heuristic)
  - act: CustomTouchEvent(state=4613f2448dfd9d979b6da01ab35707fd, view=0acee545b4b31b45aba42f12c040452b(MainActivity/TextView-Cash Accou)) (heuristic)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
