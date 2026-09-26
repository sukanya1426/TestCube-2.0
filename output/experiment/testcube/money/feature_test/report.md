# Feature test report: Money Manager Ex

- Started: 2026-09-17 05:29:14
- Finished: 2026-09-17 05:35:53
- Features: 28
- Covered: 0
- Partial: 6
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 11% (mean completion ratio; the headline number)
- Coverage: 0% (features with every guide step matched)
- Stop reason: budget_time
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 6
- Never attempted: 22
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

- Filled via credential.txt: 3
- Filled via VLM/Gemini: 9
- Unresolved: 0
- Online coverage: 0% (0/28) — live journal self-report (covered / extracted features).
- Offline coverage: 0% (0 covered / 28; 3 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 5% (mean completion ratio).

## Findings

### GT001 New database

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Tap on the Money Manager Ex app icon to open it.; Select the 'Create a database' option from the main menu.; Enter a name for the new database.; Tap the 'Create' button to finalize the new database creation.
- Remaining steps: Verify the new database is listed in the database selection screen.; Close the app to complete the feature setup.
- Completion ratio: 0.67
- Credited from later features: GT003
- Actions taken: 10
  - act: CustomTouchEvent(state=47be119a7326ee15d6cedb2c9f2dfff1, view=137a2809d2283a7da8e596daff8c7e19(SelectDatabaseActivity/Button-CREATE DAT)) (rule)
  - act: CustomTouchEvent(state=db9de7889d8d1b431453c3981085d929, view=cb84193f80591015faa7bf2a764ab8c3(PickActivity/Button-SAVE)) (rule)
  - act: CustomTouchEvent(state=967325bb19d8b40560a7364d0acb7f45, view=e775d76c9d80720909bf1f0537d19984(PasswordActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=f00e04918ea3ad23ba29c76ba4864753, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomSetTextEvent(state=7fe42e2da8b25787daf620ca2edd4801, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=testcube.mmb) (mandatory_fill)
  - act: CustomSetTextEvent(state=7fe42e2da8b25787daf620ca2edd4801, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=testcube.mmb) (mandatory_fill)
  - act: CustomSetTextEvent(state=21e79083fc5c249a15a24696183e0e3c, view=624b5b32f5baf3cdfd8f063c867d4d5d(AccountEditActivity/EditText-testcube.m), text=testcube.mmb) (llm)
  - act: CustomSetTextEvent(state=21e79083fc5c249a15a24696183e0e3c, view=624b5b32f5baf3cdfd8f063c867d4d5d(AccountEditActivity/EditText-testcube.m), text=testcube.mmb) (llm)

### GT002 New account

- Status: **partial**
- Reason: Onboarding already finished; main screen is visible.
- Feature source: guide
- Completed steps: Tap on the 'Save' button to create the new account.; Tap on the 'Account' section in the navigation drawer.
- Remaining steps: Select 'New Account' from the account options.; Enter the name of the new account in the input field.; Verify the new account is listed in the account section.
- Completion ratio: 0.40
- Credited from later features: GT003, GT006

### GT003 Add transaction

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Tap the 'Save' button; Select the 'Income' or 'Expense' option; Select the category
- Remaining steps: Tap on the 'Add a transaction' button; Enter the amount; Enter the description
- Completion ratio: 0.50
- Credited from later features: GT001
- Actions taken: 8
  - act: CustomTouchEvent(state=f00e04918ea3ad23ba29c76ba4864753, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (nav)
  - act: CustomTouchEvent(state=f00e04918ea3ad23ba29c76ba4864753, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (nav)
  - act: CustomTouchEvent(state=f00e04918ea3ad23ba29c76ba4864753, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomSetTextEvent(state=7fe42e2da8b25787daf620ca2edd4801, view=8bcd308b8146e2d2f0591bd37449b85a(AccountEditActivity/EditText-Account nu), text=1) (llm)
  - act: CustomSetTextEvent(state=9bedc058f258c8f45e4b12e2c42f64b3, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=1) (llm)
  - act: CustomSetTextEvent(state=256358af08e6815432edd71b2d1df748, view=4f14a0dcaca0feb8d4b8dfec578791ba(AccountEditActivity/EditText-1), text=1) (llm)
  - act: CustomTouchEvent(state=256358af08e6815432edd71b2d1df748, view=4f14a0dcaca0feb8d4b8dfec578791ba(AccountEditActivity/EditText-1)) (llm)
  - act: CustomTouchEvent(state=256358af08e6815432edd71b2d1df748, view=44e793bd4cb64fb1c3cc43b013194efd(AccountEditActivity/TextView-SELECT CUR)) (rule)

### GT004 Edit transaction

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Tap on the transaction you want to edit in the transaction list.; Select the 'Edit' option from the menu that appears.; Enter the new details for the transaction.
- Remaining steps: Tap the 'Save' button to update the transaction.; Confirm the changes if prompted.
- Completion ratio: 0.60
- Actions taken: 8
  - act: CustomTouchEvent(state=f00e04918ea3ad23ba29c76ba4864753, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=7081635cc4d3e28f6425391f1c1a78d6, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)
  - act: ScrollEvent(state=f9c0e13417200920ea1b1c3174b0e414, view=3d0da6020df9c26a32aa108fcb4464bd(MainActivity/ExpandableListView-), direction=left) (rule)
  - act: CustomTouchEvent(state=878dad5a22919e5ee516f44c3956487e, view=136d64e49e0c174b7cecd0cea5c3de55(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=7e72fb35420dfd44b347de75e08974ff, view=193690f5f9169553ff37dcfdad9e2711(MainActivity/CheckBox-)) (heuristic)
  - act: CustomSetTextEvent(state=7f1538788b703799c2a3c2ea38d7f7a0, view=f791beeb9799f0db39d52cdc9466fc11(MainActivity/AutoCompleteTextView-   ), text=Saimon Bhuiyan) (mandatory_fill)
  - act: CustomSetTextEvent(state=2ec765d399440d7f03cebf41a2c317c3, view=43b71a6e44f22650d96a72325cba1683(MainActivity/AutoCompleteTextView-Saimon Bhu), text=Saimon Bhuiyan) (rule)
  - act: CustomTouchEvent(state=2ec765d399440d7f03cebf41a2c317c3, x=918, y=2223) (llm)

### GT005 Filter by date

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the menu icon; Select 'Filter transactions by date'
- Remaining steps: Enter the start date in the date range field; Enter the end date in the date range field; Tap the 'Apply' button to filter the transaction list by date range
- Completion ratio: 0.50
- Actions taken: 8
  - act: CustomTouchEvent(state=f00e04918ea3ad23ba29c76ba4864753, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (heuristic)
  - act: CustomTouchEvent(state=f00e04918ea3ad23ba29c76ba4864753, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=7cffa83d253e5f2a61bfa3b4bda9978e(SearchActivity/TextView-To Date)) (heuristic)
  - act: CustomTouchEvent(state=97d121fab7d7f6af3321f8c9b03f9529, view=a59db7317c0fe2974966399c62e41381(SearchActivity/TextView-Thu, Sep 1)) (heuristic)
  - act: CustomTouchEvent(state=97d121fab7d7f6af3321f8c9b03f9529, view=a59db7317c0fe2974966399c62e41381(SearchActivity/TextView-Thu, Sep 1)) (heuristic)
  - act: CustomTouchEvent(state=97d121fab7d7f6af3321f8c9b03f9529, view=a30cce194483e695fd2aa80b77cdf9b9(SearchActivity/TextView-2026)) (heuristic)
  - act: CustomTouchEvent(state=770dd326de7b40e3adbb300d52ad7488, view=a30cce194483e695fd2aa80b77cdf9b9(SearchActivity/TextView-2026)) (heuristic)
  - act: CustomTouchEvent(state=770dd326de7b40e3adbb300d52ad7488, view=a30cce194483e695fd2aa80b77cdf9b9(SearchActivity/TextView-2026)) (heuristic)

### GT006 Search transactions

- Status: **partial**
- Feature source: guide
- Completed steps: Tap on the 'Search transactions' option in the navigation drawer.; Enter the search term in the search bar.
- Remaining steps: Press the 'Enter' key to execute the search.; Select the desired transaction from the search results.; Tap on the 'Sort' button to change the sorting order of the transactions.
- Completion ratio: 0.40
- Actions taken: 3
  - act: CustomTouchEvent(state=f00e04918ea3ad23ba29c76ba4864753, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=123456789) (mandatory_fill)
  - act: CustomSetTextEvent(state=5699579216d73b2fc5fa0071b0873039, view=59c45f22653c8f838c3dbdf7e5ed868b(SearchActivity/EditText-123456789), text=123456789) (mandatory_fill)

### GT007 Favorite account

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Money Manager Ex app; Navigate to the 'Accounts' section; Select the account you want to mark as favorite; Tap on the 'Favorite' option; Confirm the favorite status by tapping the confirmation button
- Completion ratio: 0.00

### GT008 Manage accounts

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Accounts' navigation hint to open the account list.; Select the account you wish to edit from the account list.; Tap on the 'Edit' option for the selected account.; Make the necessary changes to the account details.; Tap on the 'Save' button to confirm the changes.
- Completion ratio: 0.00

### GT009 Budget

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Open budgets' option in the navigation drawer.; Select 'Create a budget' from the available options.; Enter a name for the new budget.; Set a start date for the budget.; Set an end date for the budget.; Enter a budget amount.
- Completion ratio: 0.00

### GT010 Budget amount

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Budget' section in the main menu.; Select the 'Edit a budget amount' option.; Enter the desired budget amount in the input field.; Tap the 'Save' button to confirm the budget amount.; Verify that the budget amount is correctly updated in the app.
- Completion ratio: 0.00

### GT011 Budget details

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Budget' section in the navigation drawer.; Select 'Budget Details' from the menu.; Tap on the 'View' button to display the budget details.; Scroll through the list of transactions to view related transactions.; Select a transaction to view its details.
- Completion ratio: 0.00

### GT012 Delete budget

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Money Manager Ex app; Select the 'Budgets' section; Locate and select the budget you want to delete; Tap the 'Delete' button; Confirm the deletion by tapping 'Yes' to delete the budget
- Completion ratio: 0.00

### GT013 Budget view options

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Budget' navigation hint; Select 'Change budget view options'; Tap on the 'Budget view options' menu item; Select the desired budget view option from the menu; Confirm the selection by tapping 'Done' or 'Apply'
- Completion ratio: 0.00

### GT014 Scheduled transaction

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Transactions' section in the main menu.; Select 'Add Transaction' from the dropdown menu.; Tap on 'Recurring Transaction' to start creating a recurring transaction.; Enter the details of the transaction, including the amount and description.; Set the frequency and date for the recurring transaction.; Tap on 'Save' to finalize the recurring transaction setup.
- Completion ratio: 0.00

### GT015 Recurring prompt

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Money Manager Ex app; Navigate to the Recurring Transactions section; Select the recurring transaction you want to confirm; Tap on the 'Confirm' button to proceed; Review the details of the transaction; Tap the 'Confirm' button to finalize the transaction
- Completion ratio: 0.00

### GT016 Payees

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Payees' section in the Money Manager Ex app.; Enter the name of the payee you wish to add or edit.; Select the payee from the list if you are editing an existing payee.; Tap on the 'Save' or 'Update' button to confirm the changes.; Verify that the payee has been added or updated by checking the list of payees.
- Completion ratio: 0.00

### GT017 Categories

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Categories' section in the Money Manager Ex app; Select the 'Add New Category' option; Enter the name of the new category; Tap on the 'Save' button to add the category; Select the 'Edit' option to modify an existing category; Enter the new name for the category
- Completion ratio: 0.00

### GT018 Built-in report

- Status: **pending**
- Feature source: guide
- Remaining steps: Open reports
- Completion ratio: 0.00

### GT019 General report

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'report' navigation hint.; Select the 'General report' option from the report menu.; Tap on the 'Run a general report' button to generate the report.
- Completion ratio: 0.00

### GT020 Investments

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Investments' section in the main menu.; Select the 'Track a stock or fund' option.; Enter the name or ticker symbol of the stock or fund you want to track.; Tap on the 'Add' button to save the new investment.; Verify the investment is listed in the 'Investments' section.
- Completion ratio: 0.00

### GT021 Stock transaction

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Stock' navigation hint.; Select the 'Add a stock transaction' option.; Enter the stock symbol.; Enter the number of shares.; Enter the price per share.; Select the date of the transaction.
- Completion ratio: 0.00

### GT022 Fixed assets

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Assets' section in the navigation drawer.; Select the 'Fixed Assets' option.; Enter the name of the fixed asset in the input field.; Tap on the 'Add' button to save the fixed asset.; Verify the fixed asset is listed under the 'Fixed Assets' section.
- Completion ratio: 0.00

### GT023 Currencies

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the app; Tap on 'Currencies' in the navigation drawer; Select the 'Manage currencies and rates' option; Enter the desired currency; Select the currency rate; Tap on the 'Save' button to update the currency rate
- Completion ratio: 0.00

### GT024 Sync

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Money Manager Ex app; Navigate to the main menu; Select the 'Settings' option; Scroll down to find the 'Sync' settings; Tap on the 'Sync' settings; Select 'Open sync settings'
- Completion ratio: 0.00

### GT025 Database password

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Settings' menu.; Select 'Database' from the settings menu.; Tap on 'Database Password' to proceed.; Enter the new database password.; Confirm the new database password.; Tap on 'Save' to apply the changes.
- Completion ratio: 0.00

### GT026 Fingerprint lock

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Money Manager Ex app; Navigate to the settings menu; Select 'Security' from the settings menu; Tap on 'Fingerprint lock'; Enable fingerprint lock; Confirm the fingerprint lock setup
- Completion ratio: 0.00

### GT027 Import export

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Money Manager Ex app; Navigate to the 'Import or export' feature; Select 'Import' or 'Export' based on the user's choice; Choose the file type (QIF or CSV); Locate and select the file to import or export; Confirm the import or export operation
- Completion ratio: 0.00

### GT028 Settings

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Settings' option in the app's main menu.; Select the 'Settings' option from the menu.; Open the settings menu by tapping on the 'Settings' option.
- Completion ratio: 0.00

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
