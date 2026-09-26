# Feature test report: Money Manager Ex

- Started: 2026-08-26 23:36:42
- Finished: 2026-08-27 00:21:44
- Features: 28
- Covered: 3
- Partial: 19
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 42% (mean completion ratio; the headline number)
- Coverage: 11% (features with every guide step matched)
- Stop reason: budget_time
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 22
- Never attempted: 6
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

- Filled via credential.txt: 5
- Filled via VLM/Gemini: 11
- Unresolved: 0
- Online coverage: 11% (3/28) — live journal self-report (covered / extracted features).
- Offline coverage: 11% (3 covered / 28; 8 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 22% (mean completion ratio).

## Findings

### GT001 New database

- Status: **covered**
- Reason: Hit the per-feature step limit. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Create a database' option; Enter a name for the new database; Tap the 'Create' button to finalize the new database creation
- Completion ratio: 1.00
- Credited from later features: GT003
- Actions taken: 10
  - act: CustomTouchEvent(state=47be119a7326ee15d6cedb2c9f2dfff1, view=137a2809d2283a7da8e596daff8c7e19(SelectDatabaseActivity/Button-CREATE DAT)) (rule)
  - act: CustomTouchEvent(state=8f875a22c5619545f8fb0f81af80ebc7, view=cb84193f80591015faa7bf2a764ab8c3(PickActivity/Button-SAVE)) (rule)
  - act: CustomTouchEvent(state=967325bb19d8b40560a7364d0acb7f45, view=e775d76c9d80720909bf1f0537d19984(PasswordActivity/Button-OK)) (rule)
  - act: CustomTouchEvent(state=28e3b41f222ee87ee22576bc6db49aed, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomSetTextEvent(state=6afd64ac11a87a1b2293b7bff1d4b081, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=testcube.mmb) (mandatory_fill)
  - act: CustomTouchEvent(state=0a86808f543653eebbf3db7148d19aeb, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=70e35bfe537da43808c8caeaf9c64ab7, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=19fc20199e257a53c8fc08252337213f, x=55, y=1326) (llm)

### GT002 New account

- Status: **partial**
- Reason: Onboarding already finished; main screen is visible.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on the 'Account' section in the navigation drawer
- Remaining steps: Select 'New account' from the account options; Enter the account name in the text field; Tap the 'Create' button to finalize the account creation
- Completion ratio: 0.40
- Credited from later features: GT001, GT005

### GT003 Add transaction

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Tap on the 'Add a transaction' button; Select the 'Income' or 'Expense' option; Select the date of the transaction; Select the category of the transaction
- Remaining steps: Enter the amount of the transaction; Tap the 'Save' button to add the transaction
- Completion ratio: 0.67
- Credited from later features: GT005, GT006
- Actions taken: 10
  - act: CustomTouchEvent(state=28e3b41f222ee87ee22576bc6db49aed, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)
  - act: CustomSetTextEvent(state=6afd64ac11a87a1b2293b7bff1d4b081, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=1) (llm)
  - act: CustomTouchEvent(state=4786cf5cd1097b9caf5cdbaa76ff2d4e, x=1036, y=156) (llm)
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=8617b04bbc5563e3f25445a62ec47ad3(MainActivity/TextView-Income)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=0a9d730e29137793e1ffc3da5c595574, view=6afd2ddae0afe2ff010e275a4a390d1c(IncomeVsExpensesActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (heuristic)

### GT004 Edit transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the 'Save' button to update the transaction.; Select the 'Edit' option from the transaction menu.
- Remaining steps: Tap on the transaction you want to edit in the transaction list.; Enter the new details for the transaction.; Confirm the changes if prompted.
- Completion ratio: 0.40
- Credited from later features: GT003
- Actions taken: 8
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=7be5c2dd4b112ed6101a2814b06ff006, view=588e1a5a3bf1f2b4ca0d4a578f0916ca(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=44cfec823b1bddaa4fe10c58e17acb03, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=360b7c8fcd7810bc8eef9e2328ba7e8f, view=588e1a5a3bf1f2b4ca0d4a578f0916ca(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=44cfec823b1bddaa4fe10c58e17acb03, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (afford_search)
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (rule)

### GT005 Filter by date

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Tap on the 'Filter transactions by date' option in the navigation drawer.; Select the 'Date' filter option.
- Remaining steps: Enter the start date for the filter.; Enter the end date for the filter.; Tap the 'Apply' button to apply the date range filter.
- Completion ratio: 0.40
- Actions taken: 10
  - act: CustomTouchEvent(state=7d2d27564ca24e4dd1369f2dd4e674d1, view=9c588fdfa41c6bc145816eee4270a721(SearchActivity/TextView-Wed, Aug 2)) (heuristic)
  - act: CustomTouchEvent(state=7d2d27564ca24e4dd1369f2dd4e674d1, view=9c588fdfa41c6bc145816eee4270a721(SearchActivity/TextView-Wed, Aug 2)) (heuristic)
  - act: CustomTouchEvent(state=7d2d27564ca24e4dd1369f2dd4e674d1, view=a30cce194483e695fd2aa80b77cdf9b9(SearchActivity/TextView-2026)) (heuristic)
  - act: CustomTouchEvent(state=4c402bcd7d2371631a2c7da197572e90, view=9c588fdfa41c6bc145816eee4270a721(SearchActivity/TextView-Wed, Aug 2)) (heuristic)
  - act: CustomTouchEvent(state=7d2d27564ca24e4dd1369f2dd4e674d1, view=65361cf58c4eab0a92019b9b6c9b1a67(SearchActivity/View-1)) (heuristic)
  - act: CustomTouchEvent(state=d05efe82db9393d32c2e5475da48614f, view=354c500cc1feb24fd4b16148b03de8b8(SearchActivity/TextView-Sat, Aug 1)) (heuristic)
  - act: CustomTouchEvent(state=d05efe82db9393d32c2e5475da48614f, view=354c500cc1feb24fd4b16148b03de8b8(SearchActivity/TextView-Sat, Aug 1)) (heuristic)
  - act: CustomTouchEvent(state=d05efe82db9393d32c2e5475da48614f, view=a30cce194483e695fd2aa80b77cdf9b9(SearchActivity/TextView-2026)) (heuristic)

### GT006 Search transactions

- Status: **covered**
- Reason: Hit the per-feature step limit. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Tap on the 'Search transactions' option in the navigation drawer.; Enter the search term in the search bar.; Press the 'Enter' key to execute the search.; Select the desired transaction from the search results.; Tap on the 'Sort' button to sort the transactions.
- Completion ratio: 1.00
- Actions taken: 10
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=123456789) (mandatory_fill)
  - act: CustomSetTextEvent(state=5699579216d73b2fc5fa0071b0873039, view=59c45f22653c8f838c3dbdf7e5ed868b(SearchActivity/EditText-123456789), text=123456789) (mandatory_fill)
  - act: CustomTouchEvent(state=5699579216d73b2fc5fa0071b0873039, view=19ee481c4531b725329e5dd41ed6a159(SearchActivity/TextView-Search)) (heuristic)
  - act: CustomTouchEvent(state=5699579216d73b2fc5fa0071b0873039, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=5699579216d73b2fc5fa0071b0873039, view=58b2c4a62c9ae0a8c7ff9cb30218daa1(SearchActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=6bcb0633658c0a67f6f6abbb73352a8b, view=a77ab87c8cb6103cfe2c8747ad2f2a12(SearchActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=2cc65d47aaa2d183602e4845ba84f5ae, view=dfb3ee4bfbc79fd337920c5692bd781d(SearchActivity/TextView-Sort by da)) (heuristic)

### GT007 Favorite account

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Navigate to the 'Accounts' section; Tap on the 'Favorite' option
- Remaining steps: Select the account you want to mark as favorite; Confirm the favorite account selection
- Completion ratio: 0.60
- Credited from later features: GT001
- Actions taken: 9
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=0acee545b4b31b45aba42f12c040452b(MainActivity/TextView-Cash Accou)) (heuristic)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=4e675c9fc766b79ca5d7c6175102b6d9, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=4e675c9fc766b79ca5d7c6175102b6d9, view=7c128833fbdb3f8635ad6896ce727ce7(MainActivity/FloatingActionButton-)) (heuristic)
  - act: CustomTouchEvent(state=4e675c9fc766b79ca5d7c6175102b6d9, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (heuristic)

### GT008 Manage accounts

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Accounts' navigation hint to open the account list.
- Remaining steps: Select the account you want to edit from the list.; Tap on the 'Edit' button next to the selected account.; Enter the new details for the account as needed.; Tap the 'Save' button to update the account details.
- Completion ratio: 0.20
- Actions taken: 3
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=0acee545b4b31b45aba42f12c040452b(MainActivity/TextView-Cash Accou)) (heuristic)
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=0acee545b4b31b45aba42f12c040452b(MainActivity/TextView-Cash Accou)) (heuristic)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=0acee545b4b31b45aba42f12c040452b(MainActivity/TextView-Cash Accou)) (heuristic)

### GT009 Budget

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap on 'Open budgets'
- Remaining steps: Select 'Create a budget'; Enter a budget name; Select a budget category; Set a budget amount
- Completion ratio: 0.33
- Credited from later features: GT001
- Actions taken: 8
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (heuristic)
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=7d417e498af5c25e4d8d9934eb8f5c6d(MainActivity/TextView-$ 0.00)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=4ef5fc8a3f01d24bad3ebeff464fd821(IncomeVsExpensesActivity/TextView-Select Acc)) (llm)
  - act: CustomTouchEvent(state=74d297f4b2ee1680fb94cb33c6445904, view=8cb653b970fde73b22cb21785da1884b(IncomeVsExpensesActivity/CheckedTextView-1)) (llm)
  - act: CustomTouchEvent(state=e20924b6cb612529e9bf00108f0c332b, view=2928503e93598979461cdc02990dea9f(IncomeVsExpensesActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=6afd2ddae0afe2ff010e275a4a390d1c(IncomeVsExpensesActivity/RadioButton-)) (afford_search)

### GT010 Budget amount

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Select the 'Edit a budget amount' option.; Tap on the 'Budget' section in the navigation drawer.
- Remaining steps: Enter the desired budget amount in the input field.; Tap the 'Save' button to confirm the budget amount.; Verify that the budget amount is correctly updated in the app.
- Completion ratio: 0.40
- Credited from later features: GT003, GT005
- Actions taken: 6
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=7d417e498af5c25e4d8d9934eb8f5c6d(MainActivity/TextView-$ 0.00)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=3595bed292719997b56701ac18983666(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=3595bed292719997b56701ac18983666(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=f6be69f1bc8fb274bb63218fb5ccd872(IncomeVsExpensesActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=4f61b90b9ad5a17caeab5941fbc2d161, view=6afd2ddae0afe2ff010e275a4a390d1c(IncomeVsExpensesActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=f6be69f1bc8fb274bb63218fb5ccd872(IncomeVsExpensesActivity/Button-)) (heuristic)

### GT011 Budget details

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Select the 'View Budget Details' option.; Tap on the 'Budget Details' section in the main menu.
- Remaining steps: Tap on the 'Transactions' tab within the budget details section.; Select the specific transaction you want to view details for.; Review the budget details and related transactions.
- Completion ratio: 0.40
- Credited from later features: GT003, GT020
- Actions taken: 10
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, x=356, y=374) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=585bdacf181cdeba8bf9bd3ddbd4f16f(IncomeVsExpensesActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=3f2f6952e5e27c18a8bf24e8f9482673(MainActivity/FrameLayout-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=3595bed292719997b56701ac18983666(IncomeVsExpensesActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=f6be69f1bc8fb274bb63218fb5ccd872(IncomeVsExpensesActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=4f61b90b9ad5a17caeab5941fbc2d161, view=6afd2ddae0afe2ff010e275a4a390d1c(IncomeVsExpensesActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, x=356, y=374) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (rule)

### GT012 Delete budget

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Open the Money Manager Ex app; Tap the 'Delete' option
- Remaining steps: Select the 'Budgets' section; Locate and select the budget you want to delete; Confirm the deletion by tapping 'Yes'
- Completion ratio: 0.40
- Credited from later features: GT001
- Actions taken: 10
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=605a5f744a665795c78d1d4dc74be1ae(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (heuristic)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=123456789) (rule)
  - act: CustomTouchEvent(state=5699579216d73b2fc5fa0071b0873039, view=19ee481c4531b725329e5dd41ed6a159(SearchActivity/TextView-Search)) (llm)
  - act: CustomTouchEvent(state=5699579216d73b2fc5fa0071b0873039, view=eda4a15aef715ab56b24b363d052bfe3(SearchActivity/TextView-ACCOUNT)) (llm)
  - act: CustomTouchEvent(state=5699579216d73b2fc5fa0071b0873039, view=cf9c59b2dba2fdc728e5a0cf98d33e90(SearchActivity/Button-)) (afford_search)
  - act: ScrollEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=6b32a6505c84a61088998105d4308241(SearchActivity/Spinner-), direction=up) (afford_search)

### GT013 Budget view options

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the desired budget view option from the dropdown menu; Tap on the 'Budget' navigation hint
- Remaining steps: Select 'Change budget view options'; Tap on the 'Done' or 'Save' button to confirm the selection
- Completion ratio: 0.50
- Credited from later features: GT003, GT008
- Actions taken: 8
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (llm)
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=fca1078a818c9552164713d61129ec94(SearchActivity/EditText-Notes), text=no) (rule)
  - act: CustomSetTextEvent(state=2429031d465921f9da7bf8489031807b, view=e77bab3f2311825eb5ce47c9122e85e6(SearchActivity/EditText-Transactio), text=123456789) (rule)
  - act: CustomTouchEvent(state=98440666045fc319e869be86ba668eb0, view=dd2bcd15394dac037430b506c64f9720(SearchActivity/CheckBox-Transfer)) (llm)
  - act: CustomSetTextEvent(state=e72962a201cd8e04a77239bfb46faca5, view=59c45f22653c8f838c3dbdf7e5ed868b(SearchActivity/EditText-123456789), text=123456789) (llm)
  - act: CustomSetTextEvent(state=e72962a201cd8e04a77239bfb46faca5, view=59c45f22653c8f838c3dbdf7e5ed868b(SearchActivity/EditText-123456789), text=123456789) (llm)
  - act: CustomTouchEvent(state=e72962a201cd8e04a77239bfb46faca5, view=cf9c59b2dba2fdc728e5a0cf98d33e90(SearchActivity/Button-)) (afford_search)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=e9675520ae190f6731e929bc617799f1(SearchActivity/TextView-Select Pay)) (rule)

### GT014 Scheduled transaction

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select 'Add Transaction' from the dropdown menu.; Select the frequency of the transaction from the dropdown menu.; Tap on the 'Transactions' section in the main menu.
- Remaining steps: Tap on 'Recurring Transaction' to start creating a recurring transaction.; Enter the amount for the transaction.; Enter the date and time for the transaction.
- Completion ratio: 0.50
- Credited from later features: GT003, GT006, GT020
- Actions taken: 9
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, x=162, y=351) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=585bdacf181cdeba8bf9bd3ddbd4f16f(IncomeVsExpensesActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=7d417e498af5c25e4d8d9934eb8f5c6d(MainActivity/TextView-$ 0.00)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=3595bed292719997b56701ac18983666(IncomeVsExpensesActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=f6be69f1bc8fb274bb63218fb5ccd872(IncomeVsExpensesActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=4f61b90b9ad5a17caeab5941fbc2d161, view=5b074d74e3c3559c49729448dd1f8277(IncomeVsExpensesActivity/RadioButton-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=b0bd32912435a8aa0e2e5e760aaf218e(IncomeVsExpensesActivity/TextView-Income Vs )) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (afford_search)

### GT015 Recurring prompt

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Tap the 'Confirm' button to finalize the transaction.; Select the recurring transaction prompt.
- Remaining steps: Tap on the 'Recurring' badge in the navigation bar.; Enter the required details to confirm the due transaction.; Verify the updated transaction list to ensure the transaction is correctly added.
- Completion ratio: 0.40
- Credited from later features: GT003, GT006
- Actions taken: 7
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=94b2097fafbdfb15c14cc546a69a50fb, view=9e278810123d6fc7d5b1b145c0345498(MainActivity/CheckedTextView-o)) (heuristic)
  - act: CustomTouchEvent(state=a0a87fdf87d3df8cbe3eb4b416bae45a, view=588e1a5a3bf1f2b4ca0d4a578f0916ca(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=a0b750086e9d50154a98aa27e9a70d6d(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=605a5f744a665795c78d1d4dc74be1ae(MainActivity/ImageView-)) (rule)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=3f2f6952e5e27c18a8bf24e8f9482673(MainActivity/FrameLayout-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (heuristic)

### GT016 Payees

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Payees' section in the Money Manager Ex app.; Select the 'Add' button to add a new payee or the 'Edit' button to modify an existing one.
- Remaining steps: Enter the name of the payee you wish to add or edit.; Enter the payee's bank account details.; Select the 'Save' button to save the new or updated payee information.; Verify the payee's details in the app to ensure they are correctly added or edited.
- Completion ratio: 0.33
- Credited from later features: GT003
- Actions taken: 9
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, x=882, y=1944) (llm)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=3f2f6952e5e27c18a8bf24e8f9482673(MainActivity/FrameLayout-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=6afd2ddae0afe2ff010e275a4a390d1c(IncomeVsExpensesActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=e20924b6cb612529e9bf00108f0c332b, view=2928503e93598979461cdc02990dea9f(IncomeVsExpensesActivity/Button-OK)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=5b074d74e3c3559c49729448dd1f8277(IncomeVsExpensesActivity/RadioButton-)) (afford_search)
  - act: CustomTouchEvent(state=e20924b6cb612529e9bf00108f0c332b, view=df28ab0296f35d7f4d74d07eef94d1f0(IncomeVsExpensesActivity/TextView-Select Acc)) (rule)

### GT017 Categories

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Categories' section in the Money Manager Ex app.; Tap the 'Save' button to add the new category.; Select the 'Add New Category' option.; Select the 'Edit' option for an existing category.
- Remaining steps: Enter the name of the new category in the input field.; Enter the updated name for the category in the input field.
- Completion ratio: 0.67
- Credited from later features: GT001, GT003, GT005
- Actions taken: 6
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=f24fa459fe616c8712d49e4555d64545(MainActivity/TextView-your_data_)) (rule)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=f24fa459fe616c8712d49e4555d64545(MainActivity/TextView-your_data_)) (rule)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=8c2d858e5b2e2fc7655f8e4a91d7a69f(MainActivity/TextView-Difference)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=0a9d730e29137793e1ffc3da5c595574, view=5b074d74e3c3559c49729448dd1f8277(IncomeVsExpensesActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (heuristic)

### GT018 Built-in report

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open reports
- Completion ratio: 1.00
- Credited from later features: GT001
- Actions taken: 4
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=8c2d858e5b2e2fc7655f8e4a91d7a69f(MainActivity/TextView-Difference)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=0a9d730e29137793e1ffc3da5c595574, view=5b074d74e3c3559c49729448dd1f8277(IncomeVsExpensesActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (heuristic)

### GT019 General report

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Select the 'General report' option from the report menu.; Tap on the 'report' navigation hint.
- Remaining steps: Tap on the 'Run a general report' button.
- Completion ratio: 0.67
- Credited from later features: GT003, GT008
- Actions taken: 8
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=f4b5dd2c402eedfc100f5180913483c9(MainActivity/ProgressBar-)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=0d371dbba95a822912e793bda0f3505c(IncomeVsExpensesActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=ea914432cf0e48a901a378ee0f0e64da, view=4ef5fc8a3f01d24bad3ebeff464fd821(IncomeVsExpensesActivity/TextView-Select Acc)) (llm)
  - act: CustomTouchEvent(state=e20924b6cb612529e9bf00108f0c332b, view=b96ef268502e0ab7f6a634754c43d2ba(IncomeVsExpensesActivity/View-)) (llm)
  - act: CustomTouchEvent(state=e20924b6cb612529e9bf00108f0c332b, view=b96ef268502e0ab7f6a634754c43d2ba(IncomeVsExpensesActivity/View-)) (llm)
  - act: CustomTouchEvent(state=e20924b6cb612529e9bf00108f0c332b, view=df28ab0296f35d7f4d74d07eef94d1f0(IncomeVsExpensesActivity/TextView-Select Acc)) (llm)
  - act: CustomTouchEvent(state=e20924b6cb612529e9bf00108f0c332b, view=4fd61811c07371062bc2a68a2ed2df5d(IncomeVsExpensesActivity/CheckedTextView-1)) (llm)
  - act: CustomTouchEvent(state=74d297f4b2ee1680fb94cb33c6445904, view=2928503e93598979461cdc02990dea9f(IncomeVsExpensesActivity/Button-OK)) (rule)

### GT020 Investments

- Status: **partial**
- Reason: Hit the per-feature step limit.
- Feature source: guide
- Completed steps: Tap on the 'Investments' section in the main menu.; Tap on the 'Add' button to save the new investment.; Select the 'Track a stock or fund' option.
- Remaining steps: Enter the name or ticker of the stock or fund you want to track.; Verify the investment is listed in the 'Investments' section.
- Completion ratio: 0.60
- Credited from later features: GT003
- Actions taken: 11
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=44cfec823b1bddaa4fe10c58e17acb03, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)
  - act: CustomSetTextEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=fca1078a818c9552164713d61129ec94(SearchActivity/EditText-Notes), text=no) (llm)
  - act: CustomTouchEvent(state=2429031d465921f9da7bf8489031807b, view=070ef00ba28323861f05979a924d99f9(SearchActivity/TextView-Select Tag)) (llm)
  - act: CustomTouchEvent(state=02888c0f4cc2d525464b94d09d2590c2, x=918, y=2223) (llm)
  - act: CustomTouchEvent(state=02888c0f4cc2d525464b94d09d2590c2, x=918, y=2223) (llm)
  - act: CustomTouchEvent(state=02888c0f4cc2d525464b94d09d2590c2, view=e9912daba18070a8344abac8585b66c5(TagActivity/FloatingActionButton-)) (afford_search)
  - act: CustomTouchEvent(state=a305ec2fc8b86b3dfdf3a8e7963b793c, view=c4f0995ee6b9a30e3efe2869541cd1f0(TagActivity/EditText-Tag name)) (llm)

### GT021 Stock transaction

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Select 'Add a stock transaction'; Select the date of the transaction; Tap on the 'Stock' navigation hint
- Remaining steps: Enter the stock symbol; Enter the number of shares; Select the type of transaction (e.g., Buy, Sell)
- Completion ratio: 0.50
- Credited from later features: GT003, GT005, GT008
- Actions taken: 5
  - act: CustomTouchEvent(state=0d69100c2598c65fd26f6c529e12b8fa, view=a0b750086e9d50154a98aa27e9a70d6d(MainActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=f4b5dd2c402eedfc100f5180913483c9(MainActivity/ProgressBar-)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=0a9d730e29137793e1ffc3da5c595574, view=6afd2ddae0afe2ff010e275a4a390d1c(IncomeVsExpensesActivity/RadioButton-)) (heuristic)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (heuristic)

### GT022 Fixed assets

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Tap on the 'Assets' section in the Money Manager Ex app.; Select the 'Fixed Assets' option.
- Remaining steps: Enter the name of the fixed asset.; Input the initial value of the asset.; Tap the 'Save' button to track the fixed asset.
- Completion ratio: 0.40
- Credited from later features: GT001, GT003
- Actions taken: 4
  - act: CustomTouchEvent(state=3efcbdebf0d100e67b3cba80347eb333, view=9d067e10ccae0644a798da808b815f3b(MainActivity/TextView-$ 0.00)) (llm)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=0a9d730e29137793e1ffc3da5c595574, view=230ed5d1fa7f11b431becaf010ed6a0a(IncomeVsExpensesActivity/LinearLayout-)) (rule)
  - act: CustomTouchEvent(state=877b32272a35b611c8203da50adb92fc, view=7c156d5dd434bb3bdf3a347a0cac78d7(IncomeVsExpensesActivity/Button-)) (heuristic)

### GT023 Currencies

- Status: **pending**
- Feature source: guide
- Remaining steps: Open the Money Manager Ex app; Tap on the 'Currencies' section; Select the currency you want to manage; Enter the currency rate; Tap on the 'Save' button to update the currency rate
- Completion ratio: 0.00

### GT024 Sync

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Sync' option in the navigation drawer; Select 'Open sync settings' from the sync settings menu; Enter the necessary credentials or confirm the sync settings; Select the desired sync frequency or toggle; Confirm the settings and close the sync settings menu
- Completion ratio: 0.00

### GT025 Database password

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Settings' menu item in the main navigation drawer.; Select 'Database Settings' from the settings menu.; Tap on 'Database Password' to proceed to the password setting screen.; Enter the new database password in the password field.; Confirm the new password by re-entering it in the confirmation field.; Tap the 'Save' button to set the new database password.
- Completion ratio: 0.00

### GT026 Fingerprint lock

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Settings' icon in the main menu.; Select 'Security' from the settings menu.; Tap on 'Fingerprint Lock' in the security settings.; Enter your fingerprint to enable the fingerprint lock.; Confirm the fingerprint lock setup by tapping 'Done'.
- Completion ratio: 0.00

### GT027 Import export

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap on the 'Import or export a file' option in the main menu.; Select 'Import' from the navigation hints.; Enter the path to the QIF or CSV file you want to import.; Select the file type (QIF or CSV) from the dropdown menu.; Tap the 'Import' button to start the import process.
- Completion ratio: 0.00

### GT028 Settings

- Status: **pending**
- Feature source: guide
- Remaining steps: Tap the app icon to open the Money Manager Ex app.; Select the 'Settings' option from the menu.; Enter the settings page where you can manage app configurations.
- Completion ratio: 0.00

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
