# Feature test report: Money Manager Ex

- Started: 2026-08-22 00:52:00
- Finished: 2026-08-22 02:16:48
- Features: 28
- Covered: 13
- Partial: 0
- Dropped (blocked / stuck): 9
- Not present in the app: 0
- Coverage: 46% (fully covered / total)
- Weighted coverage: 46% (mean completion ratio, includes partials)
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 22
- Never attempted: 6
- Blocked then recovered on retry: 0
- Blocked still: 2

## Guide vs README-extracted

- Guide features: 28
- README-extracted features: 5
- In both: 2
- Guide-only: 26
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
  - guide-only: GT013 Budget view options
  - guide-only: GT014 Scheduled transaction
  - README-only: F001 Complete first-run setup
  - README-only: F003 View and edit transactions
  - README-only: F005 View and edit categories

## Independent ground-truth addendum

- Features not in the guide list: 6
- Matched in this run: 2
- Missed: 4
- Independent features not in the guide list. matched = live journal features with name similarity >= 0.3 (hybrid discovery is the expected source).

## Text-field resolution

- Filled via credential.txt: 2
- Filled via VLM/Gemini: 5
- Unresolved: 0
- Online coverage: 46% (13/28) — live journal self-report (covered / extracted features).
- Offline coverage: 7% (2 covered / 28; 0 partial) — LLM judge vs ground-truth JSON, not the live journal.
- Offline weighted coverage: 7% (mean completion ratio).

## Findings

### GT001 New database

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Create a database
- Completion ratio: 1.00
- Actions taken: 5
  - act: CustomTouchEvent(state=f76546fea06bf63a5005018b967ba56c, view=8128f880d82f0f3d0deac64ec4ce2db8(TutorialActivity/TextView-CLOSE)) (rule)
  - act: CustomTouchEvent(state=c6a27efb5e0bd6a96dce76e8ab21bb42, view=e10f8a3f37f86db158a570e15a2f2674(GeneralSettingsActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=47be119a7326ee15d6cedb2c9f2dfff1, view=137a2809d2283a7da8e596daff8c7e19(SelectDatabaseActivity/Button-CREATE DAT)) (rule)
  - act: CustomTouchEvent(state=0dfd8ef9927ea2e605d8f16137dd370e, view=cb84193f80591015faa7bf2a764ab8c3(PickActivity/Button-SAVE)) (rule)
  - act: CustomTouchEvent(state=967325bb19d8b40560a7364d0acb7f45, view=e775d76c9d80720909bf1f0537d19984(PasswordActivity/Button-OK)) (rule)

### GT002 New account

- Status: **covered**
- Reason: Onboarding already finished; main screen is visible.
- Feature source: guide
- Remaining steps: Create an account
- Completion ratio: 1.00

### GT003 Add transaction

- Status: **dropped**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Remaining steps: Add a transaction
- Completion ratio: 0.00
- Actions taken: 9
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=1bc77b2100105e9d823d2672d4dbcaa9(MainActivity/TextView-Current da)) (llm)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=a5c16f91402335e0962f848591660472, view=9e278810123d6fc7d5b1b145c0345498(MainActivity/CheckedTextView-o)) (heuristic)
  - act: CustomTouchEvent(state=5d4a3a0465d33b5388762b64363c7374, view=588e1a5a3bf1f2b4ca0d4a578f0916ca(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=1a5ff8a0998bfbba023432c46fbad99b, view=588e1a5a3bf1f2b4ca0d4a578f0916ca(MainActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=56093e4f89e8ecaca6bdcad38145fe9f(MainActivity/ImageButton-)) (llm)

### GT004 Edit transaction

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open a transaction and edit it
- Completion ratio: 1.00
- Actions taken: 4
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=5685205ee588408fe535752b5b572219(SearchActivity/TextView-TRANSACTIO)) (heuristic)

### GT005 Filter by date

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Filter transactions by date
- Completion ratio: 1.00
- Actions taken: 1
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)

### GT006 Search transactions

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Search transactions
- Completion ratio: 1.00
- Actions taken: 1
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (heuristic)

### GT007 Favorite account

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Favorite an account
- Completion ratio: 1.00
- Actions taken: 1
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (heuristic)

### GT008 Manage accounts

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open accounts
- Completion ratio: 1.00
- Actions taken: 1
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)

### GT009 Budget

- Status: **dropped**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Remaining steps: Open budgets; Create a budget
- Completion ratio: 0.00
- Actions taken: 42
  - act: CustomTouchEvent(state=67b5c59ca9d18ea2c246396cd611dd5b, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=2e3d5fc0b62f6ad882ee8d90e02a1d19, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=84f4b8fa344afcdb25d76e538366b114, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=488b141246f0795c0e24bfb05137a840, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=93a5efadeed76a8e980818396841f462, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=e6a777c03c750cf0414b17fbcd55a1e0, view=bb86e327742730bf5b70c64b26b767ad(AccountEditActivity/Spinner-)) (llm)
  - act: CustomTouchEvent(state=bca8df489aae4d3086ef3b64b8e319e9, view=fbb40af8f27338c49b8f6301d3d130a3(AccountEditActivity/CheckedTextView-Closed)) (llm)
  - act: CustomTouchEvent(state=e6a777c03c750cf0414b17fbcd55a1e0, view=bb86e327742730bf5b70c64b26b767ad(AccountEditActivity/Spinner-)) (llm)

### GT010 Budget amount

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Edit a budget amount
- Completion ratio: 1.00
- Actions taken: 2
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=206b3bb71772a92bb536e53f25173c50(MainActivity/Button-SETTINGS)) (llm)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=d44405fcb405adc05ad761463a792339(SettingsActivity/TextView-Budget)) (heuristic)

### GT011 Budget details

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open budget details
- Completion ratio: 1.00
- Actions taken: 2
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=206b3bb71772a92bb536e53f25173c50(MainActivity/Button-SETTINGS)) (rule)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=d44405fcb405adc05ad761463a792339(SettingsActivity/TextView-Budget)) (heuristic)

### GT012 Delete budget

- Status: **dropped**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Remaining steps: Delete a budget
- Completion ratio: 0.00
- Actions taken: 7
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (rule)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (rule)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=c09292b6556242cddf098f2c6c657558(MainActivity/TextView-your_data_)) (rule)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=c09292b6556242cddf098f2c6c657558(MainActivity/TextView-your_data_)) (rule)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (rule)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (rule)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=72faf18250cd3c6df446eb3e21594e45(MainActivity/TextView-/storage/e)) (rule)

### GT013 Budget view options

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Change budget view options
- Completion ratio: 1.00
- Actions taken: 4
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=72faf18250cd3c6df446eb3e21594e45(MainActivity/TextView-/storage/e)) (rule)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=edc7fb7fe1766dc6d0be605a14690c32(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=edc7fb7fe1766dc6d0be605a14690c32(MainActivity/View-)) (rule)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (heuristic)

### GT014 Scheduled transaction

- Status: **covered**
- Reason: Stuck in a repeating screen loop. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Add a recurring transaction
- Completion ratio: 1.00
- Credited from later features: GT015
- Actions taken: 3
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=4a211b51679e00bbf4b9d97ad507b318(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)

### GT015 Recurring prompt

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Accept a recurring transaction prompt
- Completion ratio: 1.00
- Actions taken: 3
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=4c5be2b19e11edc29c55cb86570ed65a(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=68765b32bba10fd5c6bfbd691ac91e39, view=5685205ee588408fe535752b5b572219(SearchActivity/TextView-TRANSACTIO)) (heuristic)

### GT016 Payees

- Status: **dropped**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Remaining steps: Open payees
- Completion ratio: 0.00
- Actions taken: 46
  - act: CustomSetTextEvent(state=fbb4ba5e09b4fc69186d20896163b097, view=e1fd37ddbe145a1cf9c60cd6c5a37ae3(SearchActivity/EditText-test), text=) (heuristic)
  - act: CustomSetTextEvent(state=fbb4ba5e09b4fc69186d20896163b097, view=4e754d16f6fec35f1052285da8257509(SearchActivity/EditText-choose a c), text=) (llm)
  - act: CustomTouchEvent(state=bf2a07cfd347b0ca37481199468f6506, view=f609371ab6240393d060fcb22a6cb8c6(SearchActivity/Button-NO COLOR)) (llm)
  - act: CustomTouchEvent(state=914cfa39083da08e9aa629377dc00ca7, view=0e41ae9eeb62189094df2250521e2155(SearchActivity/TextView-Insurance:)) (heuristic)
  - act: CustomTouchEvent(state=f29a8b5dfade9ae54e020d97155c954e, x=110, y=1379) (llm)
  - act: CustomTouchEvent(state=89086d5a2ed3006852d8fa8081325114, x=110, y=569) (llm)
  - act: CustomTouchEvent(state=914cfa39083da08e9aa629377dc00ca7, view=0e41ae9eeb62189094df2250521e2155(SearchActivity/TextView-Insurance:)) (heuristic)
  - act: CustomTouchEvent(state=f29a8b5dfade9ae54e020d97155c954e, view=b97ab9296c94f94aa2f6c099829b599c(CategoryListActivity/ViewGroup-)) (llm)

### GT017 Categories

- Status: **dropped**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Remaining steps: Open categories
- Completion ratio: 0.00
- Actions taken: 47
  - act: CustomTouchEvent(state=9cbd0038b744dd43cc227cd90e2b8e92, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=4b563214bfc11833425e524fa415495f, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=8a226c1096d5e740a18f013cfc5c62ce, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=a9e0835678161ffc657032c4c9ff45e0, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=3fee8587086daced3e6358f34b2170ad, view=bfbb0b4138326affebd1613dc0270049(AccountEditActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=4e24ffc4ae595174af9c9b42b94b9a9a, x=44, y=1248) (llm)
  - act: CustomTouchEvent(state=8df8e220ff60f4cd5119531be05cd3b2, view=0843e091ec41665abeeed5507a9c3b40(AccountEditActivity/CheckedTextView-Open)) (llm)
  - act: CustomTouchEvent(state=4e24ffc4ae595174af9c9b42b94b9a9a, x=44, y=1248) (llm)

### GT018 Built-in report

- Status: **dropped**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Remaining steps: Open reports
- Completion ratio: 0.00
- Actions taken: 6
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=102b50a5ced55aeaa1fd01022ce0a1c1(MainActivity/Button-CREATE NEW)) (rule)
  - act: CustomSetTextEvent(state=eb3e8f0a7444ce47fc973ff179417aa3, view=79740c2fa1c6361f0e70fef7f2f2c302(AccountEditActivity/EditText-Account na), text=) (llm)
  - act: CustomTouchEvent(state=3477282304f285ff8e5427fe21aa0b20, x=55, y=1267) (llm)
  - act: CustomTouchEvent(state=8df8e220ff60f4cd5119531be05cd3b2, view=0843e091ec41665abeeed5507a9c3b40(AccountEditActivity/CheckedTextView-Open)) (llm)
  - act: CustomTouchEvent(state=3477282304f285ff8e5427fe21aa0b20, x=55, y=1267) (llm)

### GT019 General report

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Run a general report
- Completion ratio: 1.00
- Actions taken: 4
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=206b3bb71772a92bb536e53f25173c50(MainActivity/Button-SETTINGS)) (llm)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=78c738d8402e11945f32d0b47afd7ac9(SettingsActivity/TextView-General)) (heuristic)
  - act: CustomTouchEvent(state=c6a27efb5e0bd6a96dce76e8ab21bb42, view=e10f8a3f37f86db158a570e15a2f2674(GeneralSettingsActivity/ImageButton-)) (rule)

### GT020 Investments

- Status: **dropped**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Remaining steps: Open investments
- Completion ratio: 0.00
- Actions taken: 5
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=206b3bb71772a92bb536e53f25173c50(MainActivity/Button-SETTINGS)) (llm)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=c94216264d43ba3d85fa80d471b69dae(SettingsActivity/TextView-Info)) (llm)
  - act: CustomTouchEvent(state=d4cca4edf7aebd73360efe1805952df4, view=9057821023ceb097964990fcc95c5854(AboutActivity/ImageButton-)) (rule)
  - act: CustomTouchEvent(state=03b69a366c752b207fe07186c8bea9ad, view=c94216264d43ba3d85fa80d471b69dae(SettingsActivity/TextView-Info)) (llm)

### GT021 Stock transaction

- Status: **dropped**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Remaining steps: Add a stock transaction
- Completion ratio: 0.00
- Actions taken: 8
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (llm)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=3e50a1a3c41b9700c7097f818c90a401(MainActivity/TextView-Money Mana)) (rule)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=c09292b6556242cddf098f2c6c657558(MainActivity/TextView-your_data_)) (llm)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=c09292b6556242cddf098f2c6c657558(MainActivity/TextView-your_data_)) (llm)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (llm)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=d43f24065b5900eeff6de7b629e067df(MainActivity/TextView-Welcome to)) (rule)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (rule)

### GT022 Fixed assets

- Status: **dropped**
- Reason: Run ended before the feature completed.
- Feature source: guide
- Remaining steps: Open assets
- Completion ratio: 0.00
- Actions taken: 2
  - act: CustomTouchEvent(state=7313598d9c90ebe6140bb6aa97e45a52, view=32d4b16f087dcbcf349b535ed4bb83b9(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=894e19f8fdb64a19a427811ee87efe0f, view=1d9c989699ab02325b1a654c912fb0d1(MainActivity/TextView-All transa)) (rule)

### GT023 Currencies

- Status: **pending**
- Feature source: guide
- Remaining steps: Open currencies
- Completion ratio: 0.00

### GT024 Sync

- Status: **pending**
- Feature source: guide
- Remaining steps: Open sync settings
- Completion ratio: 0.00

### GT025 Database password

- Status: **pending**
- Feature source: guide
- Remaining steps: Set a database password
- Completion ratio: 0.00

### GT026 Fingerprint lock

- Status: **pending**
- Feature source: guide
- Remaining steps: Enable fingerprint lock
- Completion ratio: 0.00

### GT027 Import export

- Status: **pending**
- Feature source: guide
- Remaining steps: Import or export a file
- Completion ratio: 0.00

### GT028 Settings

- Status: **pending**
- Feature source: guide
- Remaining steps: Open settings
- Completion ratio: 0.00

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
