# Feature test report: App Manager

- Started: 2026-10-25 14:32:14
- Finished: 2026-10-25 15:27:21
- Features: 13
- Covered: 9
- Partial: 4
- Dropped (blocked / stuck): 0
- Not present in the app: 0
- Weighted coverage: 83% (mean completion ratio; the headline number)
- Coverage: 69% (features with every guide step matched)
- Stop reason: all_features_done
- Scoring: **feature coverage** vs an independent labeled set (ground_truth_source=independent_labeled_set).

## Attempt summary

- Attempted: 13
- Never attempted: 0
- Blocked then recovered on retry: 1
- Blocked still: 1

## Guide vs README-extracted

- Guide features: 13
- README-extracted features: 2
- In both: 0
- Guide-only: 13
- README-only: 2
  - guide-only: G001 Browse installed apps
  - guide-only: G002 Open an app's details
  - guide-only: G003 Inspect app components
  - guide-only: G004 Review permissions
  - guide-only: G005 Scan for trackers
  - guide-only: G006 Search for an app
  - guide-only: G007 Sort or filter the list
  - guide-only: G008 Run a batch operation
  - guide-only: G009 Open running apps
  - guide-only: G010 View app usage
  - guide-only: G011 Open profiles
  - guide-only: G012 Open settings
  - README-only: F001 Complete first-run setup
  - README-only: F002 Import or export data

## Text-field resolution

- Filled via credential.txt: 8
- Filled via VLM/Gemini: 12
- Unresolved: 0
- Online coverage: 69% (9/13) — live journal self-report (covered / extracted features).
- Offline coverage: not computed (no ground-truth JSON).

## Findings

### G001 Browse installed apps

- Status: **partial**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink.
- Feature source: guide
- Completed steps: Open the app; Tap on the 'installed' option in the navigation drawer; Select the 'Browse installed apps' feature; Tap on the desired app to view its details
- Remaining steps: Scroll through the package list until the desired app is visible
- Completion ratio: 0.80
- Credited from later features: G002, G009, G003
- Actions taken: 56
  - act: CustomTouchEvent(state=97cf79740771ecd4308f93cd4e14dd40, view=e9c62f1a8c2b45f20b503652e3d1571b(MainActivity/RadioButton-Package na)) (heuristic)
  - act: CustomTouchEvent(state=7b0ca75d6d927307f1335228aea81bec, view=52203feb2fc8b8383f174b47ebb50687(MainActivity/RadioButton-Signature)) (heuristic)
  - act: CustomTouchEvent(state=38b3a7dea011789f879caf1d5597fe0a, view=2faa1c5a3f51b61155390d567b0ea835(MainActivity/RadioButton-Frozen fir)) (heuristic)
  - act: CustomTouchEvent(state=b5598275ce23cbdf12f067c52c34e697, view=f74a9ec505d866938e3078c63e33e26d(MainActivity/RadioButton-Shared use)) (heuristic)
  - act: CustomTouchEvent(state=e12d0604c1714f558272c55ce263b5af, view=d71adbdfbb7c87be853d277d4882bc84(MainActivity/RadioButton-Shared use)) (heuristic)
  - act: CustomTouchEvent(state=cc403b44cc675f6a02ef0a7eb3501bb2, view=52203feb2fc8b8383f174b47ebb50687(MainActivity/RadioButton-Signature)) (heuristic)
  - act: CustomSetTextEvent(state=38b3a7dea011789f879caf1d5597fe0a, view=d3fbfb99789c7180b262cf4654921888(MainActivity/Spinner-No profile), text=test) (nav)
  - act: CustomTouchEvent(state=38b3a7dea011789f879caf1d5597fe0a, view=897278e9d045394fad5f76084939f543(MainActivity/Button-Installed )) (rule)

### G002 Open an app's details

- Status: **covered**
- Reason: The 'Add to profile' action has been completed, and the app details are loaded. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the app; Tap on the app row; Tap on the 'details' option; Wait for the app details to load; Select the app from the list
- Completion ratio: 1.00
- Credited from later features: G006, G009, G003
- Actions taken: 15
  - act: CustomTouchEvent(state=58c3ee4a82745e4e89d2bb800fbbfc42, view=e4429e1cfbba4bef9bfd1cf981c6bd21(MainActivity/TextView-  Allow ma)) (rule)
  - act: CustomTouchEvent(state=ebf46a842abcf2a3c9d09515fd548f4c, view=812fb8f34416141c54e1bbdf776433da(AppDetailsActivity/ImageButton-)) (llm)
  - act: CustomTouchEvent(state=aec4bc392bb3bebfa82b9d1c5cd1f751, view=1a0a5818798185dc089c5dfcb25d3bfd(MainActivity/TextView-Android Se)) (heuristic)
  - act: CustomTouchEvent(state=04753d4bd61228b452ba85a22a1d1cd8, view=d289f567911835a7061bce7f7850c99f(AppDetailsActivity/TextView-Android Se)) (heuristic)
  - act: CustomTouchEvent(state=b05275455a4e520116a1801c917c5a20, view=5be910085fddbe997659e8c479be6338(AppDetailsActivity/TextView-App info)) (nav)
  - act: CustomTouchEvent(state=b05275455a4e520116a1801c917c5a20, view=5be910085fddbe997659e8c479be6338(AppDetailsActivity/TextView-App info)) (nav)
  - act: CustomTouchEvent(state=b05275455a4e520116a1801c917c5a20, view=67ba99ade153270e8a259becee77cc90(AppDetailsActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=10235b96021e56295fa9c3ba679fa049, view=4842f7716b67c655e7b5b07d313315eb(AppDetailsActivity/ImageView-)) (llm)

### G003 Inspect app components

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap on the 'Activities' tab to view the app's activities.; Select the 'Inspect app components' option from the menu that appears.; Tap on the app you want to inspect in the list of installed apps.; Tap on the 'Details' tab to view the app's manifest and components.; Scroll to the 'Permissions' tab to see the app's permissions.; Select the 'Services' tab to inspect the app's services.
- Completion ratio: 1.00
- Credited from later features: G002, G009
- Actions taken: 15
  - act: CustomTouchEvent(state=645c577615808cbc038904294d18f725, view=67ba99ade153270e8a259becee77cc90(AppDetailsActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=033aa6839dc4573499630336b79ba9a6, view=c94c9f9fa620011b025621a9e20abc1b(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=94ca07026736e0e31400548651378123, view=7ae996efa84cba63033d13ce118dc692(MainActivity/TextView-Settings)) (llm)
  - act: CustomTouchEvent(state=797e83980bf8c82bf0b0fd8924b390d4, view=c0b529334d676e5ae7633d74a88f2938(SettingsActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=aec4bc392bb3bebfa82b9d1c5cd1f751, view=fa9ef37945de2204ad6c6f1bab40a55e(MainActivity/TextView-com_google)) (heuristic)
  - act: CustomTouchEvent(state=04753d4bd61228b452ba85a22a1d1cd8, view=7465f279446e76cd3f0161ed6e8dada8(AppDetailsActivity/TextView-com_google)) (nav)
  - act: ScrollEvent(state=b05275455a4e520116a1801c917c5a20, view=a1e886a05daaab719e08386ebd5f98ba(AppDetailsActivity/HorizontalScrollView-), direction=right) (heuristic)
  - act: CustomTouchEvent(state=b05275455a4e520116a1801c917c5a20, view=527f6c43c2a38dcb3f952a378dc85a38(AppDetailsActivity/TextView-Services)) (heuristic)

### G004 Review permissions

- Status: **partial**
- Reason: Onboarding already finished; main screen is visible.
- Feature source: guide
- Completed steps: Open an app's details; Scroll to the permissions tab; Select the permissions tab
- Remaining steps: Review the permissions listed; End in a visibly different, checkable app state
- Completion ratio: 0.60
- Credited from later features: G003

### G005 Scan for trackers

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open an app's details; Tap the overflow menu (three dots); Select 'Scan for trackers'
- Completion ratio: 1.00
- Credited from later features: G003, G007
- Actions taken: 21
  - act: CustomTouchEvent(state=d2bb073151f5d96e21eb1b472b15d29d, view=3dd56d0685e395f94b6184e098c3424f(AppDetailsActivity/TextView-Refresh)) (rule)
  - act: CustomTouchEvent(state=645c577615808cbc038904294d18f725, view=a4e8c5b47546db13142a6085ed037647(AppDetailsActivity/LinearLayout-)) (heuristic)
  - act: CustomTouchEvent(state=78fcd3f95dac95820ce84b5d250e6c85, view=7663d1ec744c4465aa2006bdb8af1824(AppDetailsActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=78fcd3f95dac95820ce84b5d250e6c85, view=7663d1ec744c4465aa2006bdb8af1824(AppDetailsActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=78fcd3f95dac95820ce84b5d250e6c85, view=67ba99ade153270e8a259becee77cc90(AppDetailsActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=10235b96021e56295fa9c3ba679fa049, view=2904d4193a841e3185376a9abfab75e6(AppDetailsActivity/LinearLayout-)) (llm)
  - act: CustomTouchEvent(state=78fcd3f95dac95820ce84b5d250e6c85, view=b5ad9054f4221c514da5c328bbe1d92e(AppDetailsActivity/TextView-Android Se)) (heuristic)
  - act: CustomTouchEvent(state=d13b43b21cc2f21409051a06d529716d, view=cff7acef680dc4d27fe0b020a3c7cb81(MainActivity/RadioButton-Trackers)) (heuristic)

### G006 Search for an app

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the search icon; Tap the search icon again; Open the app; Enter 'App Manager' in the search bar; Select the search result for 'App Manager'; Enter 'Search for an app' in the search bar
- Completion ratio: 1.00
- Credited from later features: G002
- Actions taken: 17
  - act: CustomTouchEvent(state=04753d4bd61228b452ba85a22a1d1cd8, view=f25f46362048dc95d7522e519822c3c7(AppDetailsActivity/AutoCompleteTextView-   Search )) (heuristic)
  - act: CustomTouchEvent(state=bf5ea8d5247d03efd9443d432b39e5a1, view=7663d1ec744c4465aa2006bdb8af1824(AppDetailsActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=bf5ea8d5247d03efd9443d432b39e5a1, view=7663d1ec744c4465aa2006bdb8af1824(AppDetailsActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=bf5ea8d5247d03efd9443d432b39e5a1, view=67ba99ade153270e8a259becee77cc90(AppDetailsActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=10235b96021e56295fa9c3ba679fa049, view=2904d4193a841e3185376a9abfab75e6(AppDetailsActivity/LinearLayout-)) (llm)
  - act: CustomSetTextEvent(state=033aa6839dc4573499630336b79ba9a6, view=dc1d3466b64410964cccf128c91c8ac5(MainActivity/AutoCompleteTextView-   Search ), text=test) (mandatory_fill)
  - act: CustomTouchEvent(state=e3be2c079a9484509dfc5e01027e9979, view=701fdadf64f6397d17a2405afcc18e71(MainActivity/ImageView-)) (heuristic)
  - act: CustomSetTextEvent(state=aec4bc392bb3bebfa82b9d1c5cd1f751, view=dc1d3466b64410964cccf128c91c8ac5(MainActivity/AutoCompleteTextView-   Search ), text=test) (mandatory_fill)

### G007 Sort or filter the list

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the app; Select 'filter'; Tap the overflow menu (three dots); Select 'sort by'; Choose 'Name' from the sort options
- Completion ratio: 1.00
- Credited from later features: G002, G008
- Actions taken: 16
  - act: CustomTouchEvent(state=e3be2c079a9484509dfc5e01027e9979, view=9e6fd41eca27020b057eb9e2c5a3ff0e(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=e3be2c079a9484509dfc5e01027e9979, view=41bb2fc4c913863add4798bc67bf7b11(MainActivity/GridView-)) (llm)
  - act: CustomTouchEvent(state=e3be2c079a9484509dfc5e01027e9979, view=41bb2fc4c913863add4798bc67bf7b11(MainActivity/GridView-)) (llm)
  - act: CustomTouchEvent(state=e3be2c079a9484509dfc5e01027e9979, view=701fdadf64f6397d17a2405afcc18e71(MainActivity/ImageView-)) (afford_search)
  - act: CustomTouchEvent(state=aec4bc392bb3bebfa82b9d1c5cd1f751, view=9e6fd41eca27020b057eb9e2c5a3ff0e(MainActivity/Button-)) (llm)
  - act: CustomTouchEvent(state=c42ada14739ca664db7959d0ba01df08, view=9f08fca507b31ad73e13084765a6fc03(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=7eaa4f7a76d44f3946222718f93a02a2, view=9b1f8841bab47ecaa075a023c34c734a(MainActivity/TextView-Sort)) (heuristic)
  - act: CustomTouchEvent(state=c42ada14739ca664db7959d0ba01df08, view=9b1f8841bab47ecaa075a023c34c734a(MainActivity/TextView-Sort)) (heuristic)

### G008 Run a batch operation

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the app
- Remaining steps: Scroll to find the app you want to operate on; Long-press the app row; Select 'Batch' from the dropdown menu; Choose the operation you want to perform (e.g., freeze, force-stop, clear data, uninstall); Confirm the batch operation
- Completion ratio: 0.17
- Credited from later features: G002
- Actions taken: 62
  - act: LongTouchEvent(state=5bf8e4470a87854b5f2b3949408dddf2, view=fb775873333c2be39e97311e0a5a2a95(MainActivity/RadioButton-Target SDK)) (heuristic)
  - act: LongTouchEvent(state=2f76cd93e2ea30170ac3d9eed20978df, view=f74a9ec505d866938e3078c63e33e26d(MainActivity/RadioButton-Shared use)) (heuristic)
  - act: LongTouchEvent(state=5bf8e4470a87854b5f2b3949408dddf2, view=fb775873333c2be39e97311e0a5a2a95(MainActivity/RadioButton-Target SDK)) (heuristic)
  - act: CustomTouchEvent(state=2f76cd93e2ea30170ac3d9eed20978df, view=9f08fca507b31ad73e13084765a6fc03(MainActivity/ImageButton-)) (rule)
  - act: LongTouchEvent(state=964010e761fedf9cae0f3671272a93e6, view=f74a9ec505d866938e3078c63e33e26d(MainActivity/RadioButton-Shared use)) (heuristic)
  - act: LongTouchEvent(state=5bf8e4470a87854b5f2b3949408dddf2, view=52203feb2fc8b8383f174b47ebb50687(MainActivity/RadioButton-Signature)) (heuristic)
  - act: LongTouchEvent(state=2184e4a770f37e71cde66a5fe11ec496, view=f74a9ec505d866938e3078c63e33e26d(MainActivity/RadioButton-Shared use)) (heuristic)
  - act: LongTouchEvent(state=5bf8e4470a87854b5f2b3949408dddf2, view=52203feb2fc8b8383f174b47ebb50687(MainActivity/RadioButton-Signature)) (heuristic)

### G009 Open running apps

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Tap the navigation drawer icon; Select the 'Running apps' option; Verify the list of running apps
- Completion ratio: 1.00
- Actions taken: 10
  - act: CustomTouchEvent(state=12768bcf6fa6b4e6e95b17b2e576ac51, view=e47fde9814fd11fc81408541e024f560(MainActivity/TextView-Android Se)) (heuristic)
  - act: CustomTouchEvent(state=dc84b66256a60b80a9a349d404d46a82, view=1a0a5818798185dc089c5dfcb25d3bfd(MainActivity/TextView-Android Se)) (heuristic)
  - act: CustomTouchEvent(state=12768bcf6fa6b4e6e95b17b2e576ac51, view=e47fde9814fd11fc81408541e024f560(MainActivity/TextView-Android Se)) (heuristic)
  - act: ScrollEvent(state=dc84b66256a60b80a9a349d404d46a82, view=cdc03cc62a6214b8f8fdfe7a95d46ff4(MainActivity/GridView-), direction=up) (rule)
  - act: CustomTouchEvent(state=8887cf776798e3dd5029866c4cfe161a, view=e47fde9814fd11fc81408541e024f560(MainActivity/TextView-Android Se)) (heuristic)
  - act: CustomTouchEvent(state=12768bcf6fa6b4e6e95b17b2e576ac51, view=ec0a069845081e140837af52d0188058(MainActivity/CardView-)) (llm)
  - act: CustomSetTextEvent(state=dc84b66256a60b80a9a349d404d46a82, view=dc1d3466b64410964cccf128c91c8ac5(MainActivity/AutoCompleteTextView-   Search ), text=test) (llm)
  - act: CustomTouchEvent(state=c466d10cbf662b8d0cfbc32de3f02e74, view=41bb2fc4c913863add4798bc67bf7b11(MainActivity/GridView-)) (heuristic)

### G010 View app usage

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the navigation drawer; tap the app usage entry
- Completion ratio: 1.00
- Credited from later features: G009
- Actions taken: 10
  - act: CustomTouchEvent(state=94ca07026736e0e31400548651378123, view=5e8fc5c22cee0b292ba174b53bf0f54a(MainActivity/TextView-App usage)) (nav)
  - act: CustomTouchEvent(state=8f0842bbac5539d9a13f115073e17e89, x=54, y=234) (llm)
  - act: CustomTouchEvent(state=e3be2c079a9484509dfc5e01027e9979, view=c94c9f9fa620011b025621a9e20abc1b(MainActivity/ImageView-)) (heuristic)
  - act: CustomTouchEvent(state=94ca07026736e0e31400548651378123, view=5e8fc5c22cee0b292ba174b53bf0f54a(MainActivity/TextView-App usage)) (nav)
  - act: CustomTouchEvent(state=e63d546b5c5b5fb9545d19e6772c785a, view=aaeb6636f1bf63cd1536015123d612e2(AppUsageActivity/TextView-App usage)) (nav)
  - act: CustomTouchEvent(state=e63d546b5c5b5fb9545d19e6772c785a, view=aaeb6636f1bf63cd1536015123d612e2(AppUsageActivity/TextView-App usage)) (nav)
  - act: CustomTouchEvent(state=e63d546b5c5b5fb9545d19e6772c785a, view=878bb5d959ac5b0db8ef11b9ea99449b(AppUsageActivity/Button-)) (rule)
  - act: CustomTouchEvent(state=4c4f2ab616357a36e67a41ea992f21e1, view=fb589994912c4795bdfb1cadbd34c610(MainActivity/RadioButton-Data usage)) (heuristic)

### G011 Open profiles

- Status: **covered**
- Reason: Listed steps are done.
- Feature source: guide
- Completed steps: Open the navigation drawer; tap the profiles entry
- Completion ratio: 1.00
- Credited from later features: G009
- Actions taken: 9
  - act: CustomTouchEvent(state=cb610fd5904656a48971284bfec9ba10, view=35b6cfd8d6343f841cf9af98bc52d1cd(AppUsageActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=cb610fd5904656a48971284bfec9ba10, view=35b6cfd8d6343f841cf9af98bc52d1cd(AppUsageActivity/ImageButton-)) (heuristic)
  - act: CustomSetTextEvent(state=cb610fd5904656a48971284bfec9ba10, view=3c0dc50e74e816ca342611200457f951(AppUsageActivity/Spinner-Daily), text=test) (heuristic)
  - act: CustomTouchEvent(state=e63d546b5c5b5fb9545d19e6772c785a, view=726737e9b60af54d2dda7826e26f3948(AppUsageActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=cb610fd5904656a48971284bfec9ba10, view=cfa9d4ec8d11cbc084e8b2aac068e5c6(AppUsageActivity/Button-)) (heuristic)
  - act: CustomTouchEvent(state=b9f09ee3f23d19cd2155c293af67fec3, view=726737e9b60af54d2dda7826e26f3948(AppUsageActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=9844ea5c0508a65bb60885fecbc85d10, view=35b6cfd8d6343f841cf9af98bc52d1cd(AppUsageActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=dd1b3d3a1a390ab3d9416d5c61acf3c4, view=d3fbfb99789c7180b262cf4654921888(MainActivity/Spinner-No profile)) (heuristic)

### G012 Open settings

- Status: **covered**
- Reason: Stagnation: novelty below threshold and remaining steps did not shrink. Later exploration completed remaining steps.
- Completion source: cross_feature
- Feature source: guide
- Completed steps: Open the navigation drawer; tap Settings
- Completion ratio: 1.00
- Credited from later features: G009, G013
- Actions taken: 8
  - act: CustomTouchEvent(state=9844ea5c0508a65bb60885fecbc85d10, view=c0d57d75894e3d18521eaa1e2cfd9688(AppUsageActivity/TextView-  ↑ 138 B )) (heuristic)
  - act: CustomSetTextEvent(state=15db27289d8321a62fb5b47b60b03c7d, view=a4b0c42eb480c0dfb0c8cb6c40edc938(AppUsageActivity/Spinner-Weekly), text=test) (heuristic)
  - act: CustomTouchEvent(state=b9f09ee3f23d19cd2155c293af67fec3, view=c0d57d75894e3d18521eaa1e2cfd9688(AppUsageActivity/TextView-  ↑ 138 B )) (heuristic)
  - act: CustomTouchEvent(state=a0750228c07025c04f991b9c4966ac56, view=7cd79b4211dff5b422d485738693bc0d(AppUsageActivity/TextView-Data usage)) (llm)
  - act: CustomTouchEvent(state=a0750228c07025c04f991b9c4966ac56, view=7cd79b4211dff5b422d485738693bc0d(AppUsageActivity/TextView-Data usage)) (llm)
  - act: CustomTouchEvent(state=a0750228c07025c04f991b9c4966ac56, view=5b181495a255550572d3f6339ca7ca0b(AppUsageActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=a0750228c07025c04f991b9c4966ac56, view=5b181495a255550572d3f6339ca7ca0b(AppUsageActivity/ImageView-)) (llm)
  - act: CustomTouchEvent(state=a0750228c07025c04f991b9c4966ac56, view=9509c09d00dcec31750b8e9436696e55(AppUsageActivity/ImageView-)) (llm)

### G013 Read about and version

- Status: **partial**
- Reason: Stuck in a repeating screen loop.
- Feature source: guide
- Completed steps: Open the navigation drawer
- Remaining steps: Tap on 'About'; Select 'Version' from the dropdown menu; Read the version information displayed
- Completion ratio: 0.25
- Credited from later features: G009
- Actions taken: 48
  - act: CustomTouchEvent(state=38b3a7dea011789f879caf1d5597fe0a, view=9f08fca507b31ad73e13084765a6fc03(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=d30e80fe66063bc12d154d3ebece62c9, view=9b1f8841bab47ecaa075a023c34c734a(MainActivity/TextView-Sort)) (heuristic)
  - act: CustomTouchEvent(state=2184e4a770f37e71cde66a5fe11ec496, view=9f08fca507b31ad73e13084765a6fc03(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=f84336f0de748ca1e7ff8a91e04d75cb, view=bd9b9b43a7cac79785ecb0fef170ad8b(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=f84336f0de748ca1e7ff8a91e04d75cb, view=bd9b9b43a7cac79785ecb0fef170ad8b(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=f84336f0de748ca1e7ff8a91e04d75cb, view=3506d9f8f3b4b03b5b9ccce26806bbe2(MainActivity/TextView-Filter)) (heuristic)
  - act: CustomTouchEvent(state=2184e4a770f37e71cde66a5fe11ec496, view=9f08fca507b31ad73e13084765a6fc03(MainActivity/ImageButton-)) (heuristic)
  - act: CustomTouchEvent(state=f84336f0de748ca1e7ff8a91e04d75cb, view=9b1f8841bab47ecaa075a023c34c734a(MainActivity/TextView-Sort)) (heuristic)

## Shared flows detected

None this run.

See `session.json` and `log.md` in this folder for the full trace.
