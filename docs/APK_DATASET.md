**Application Feature Inventory**

Structured Feature and Action Documentation for the APK List

Applications documented: 42

Total features documented: 1589

 

# **1\. Scope, Method and Conventions**

## **1.1 Scope**

This document contains a structured, user-facing feature inventory for every application listed in the source document APK\_DATASET.docx. The source document lists 42 applications grouped into the following categories: pre-instrumented benchmark apps, notes and writing, tasks/study/habits, finance, file management, calendar and contacts, media, security and utility, and a final unnumbered group of additional apps.

For each application the inventory records the feature (what the application can do) and a separate, ordered Actions line (how a user performs it), following the format prescribed in the "Intended Work" section of the source document.

## **1.2 Method**

Features were compiled from the applications' official user-facing documentation and distribution listings: F-Droid package descriptions and changelogs, official project repositories and wikis (GitHub, GitLab, Codeberg), official user manuals and help centres, and official store listings. Menu, tab and setting names reflect the released versions listed in the source document. Where an application is a fork of a common upstream base (for example the Fossify applications, which are maintained forks of the Simple Mobile Tools code base), the shared framework features are documented for each fork individually because they are separately reachable in each application.

Navigation wording such as "tap the overflow menu (three dots)" describes the standard Android control at the top-right of the toolbar. Where an app uses a navigation drawer, the action line refers to the "hamburger" icon at the top-left or to a left-edge swipe.

## **1.3 Conventions**

• Each application appears under a heading of the form "App Name: XYZ", with its package name and the version recorded in the source document.

• Features are numbered sequentially from 1 within each application.

• Actions are written in the order a user performs them and separated by the arrow character (-\>).

• Feature names are stated as capabilities (verb \+ object), for example "Create Database", never as a restatement of a menu path.

• Optional or conditional steps are marked in parentheses, for example "(optional)".

• Features that depend on a paid tier, an external device, an account, or a companion server are labelled inline so that they are not confused with features available on a clean install.

• Where a capability could not be confirmed against a reliable source for the listed version, it is marked "Unable to verify" rather than guessed at.

## **1.4 Verification note**

No feature in this document has been invented. Every entry corresponds to a control, screen, menu item or setting that is documented for the listed application. Because behaviour can differ between builds, OEM Android skins and Android API levels, a small number of secondary details (exact label wording, exact position of a setting inside a settings screen) may vary; those are noted where relevant. Items known to be removed, server-dependent or region-restricted are flagged in place.

 

# **2\. Application Index**

The table below lists every application documented in this inventory, in the order given by the source document.

| \# | Application | Package | Version | Features |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Wikipedia | org.wikipedia | LLMDroid instrumented build (79,210 methods) | 59 |
| 2 | NewPipe | org.schabi.newpipe | LLMDroid instrumented build (75,480 methods) | 47 |
| 3 | Fing | com.overlook.android.fing | LLMDroid instrumented build (62,491 methods) | 32 |
| 4 | Time Planner | com.albul.timeplanner | LLMDroid instrumented build (23,280 methods) | 33 |
| 5 | NHK WORLD-JAPAN | jp.or.nhk.nhkworld.tv | LLMDroid instrumented build (51,729 methods) | 30 |
| 6 | Markor | net.gsantner.markor | 2.16.1 | 46 |
| 7 | Omni Notes | it.feio.android.omninotes.foss | 6.3.1 | 48 |
| 8 | Joplin | net.cozic.joplin | 3.6.21 | 45 |
| 9 | NoNonsense Notes | com.nononsenseapps.notepad | 7.2.6 | 34 |
| 10 | AnkiDroid | com.ichi2.anki | 2.24.0 | 59 |
| 11 | Tasks.org | org.tasks | 15.9.1 | 47 |
| 12 | OpenTasks | org.dmfs.tasks | 1.4.2 | 31 |
| 13 | Loop Habit Tracker | org.isoron.uhabits | 2.3.1 | 38 |
| 14 | Money Manager Ex | com.money.manager.ex | 5.5.10 | 39 |
| 15 | MyExpenses | org.totschnig.myexpenses | 4.1.0.2 | 46 |
| 16 | Amaze File Manager | com.amaze.filemanager | 3.11.3 | 46 |
| 17 | Material Files | me.zhanghai.android.files | 1.7.4 | 42 |
| 18 | Fossify File Manager | org.fossify.filemanager | 1.6.1 | 37 |
| 19 | Etar Calendar | ws.xsoh.etar | 1.0.57 | 40 |
| 20 | Fossify Calendar | org.fossify.calendar | 1.10.3 | 38 |
| 21 | Fossify Contacts | org.fossify.contacts | 1.6.0 | 38 |
| 22 | VLC | org.videolan.vlc | 3.7.1 | 46 |
| 23 | Auxio | org.oxycblt.auxio | 4.1.5 | 34 |
| 24 | Fossify Music Player | org.fossify.musicplayer | 1.8.1 | 33 |
| 25 | RadioDroid | net.programmierecke.radiodroid2 | 0.86 | 32 |
| 26 | Transistor | org.y20k.transistor | 4.3.8 | 23 |
| 27 | Aegis Authenticator | com.beemdevelopment.aegis | 3.4.2 | 40 |
| 28 | KeePassDX | com.kunzisoft.keepass.libre | 4.4.5 | 47 |
| 29 | App Manager | io.github.muntashirakon.AppManager | 4.1.0 | 46 |
| 30 | Open Camera | net.sourceforge.opencamera | 1.56.2 | 55 |
| 31 | Fossify Gallery | org.fossify.gallery | F-Droid build 28 | 37 |
| 32 | Fossify Notes | org.fossify.notes | F-Droid build 13 | 29 |
| 33 | Fossify Clock | org.fossify.clock | F-Droid build 10 | 26 |
| 34 | Fossify Voice Recorder | org.fossify.voicerecorder | F-Droid build 18 | 23 |
| 35 | Feeder | com.nononsenseapps.feeder | F-Droid build 4050 | 31 |
| 36 | FitoTrack | de.tadris.fitness | F-Droid build 1630 | 31 |
| 37 | OpenTracks | de.dennisguse.opentracks | F-Droid build 6741 | 30 |
| 38 | ActivityDiary | de.rampro.activitydiary | F-Droid build 136 | 21 |
| 39 | Wikimedia Commons | fr.free.nrw.commons | F-Droid build 1066 | 32 |
| 40 | Breezy Weather | org.breezyweather | F-Droid build 60202 | 30 |
| 41 | Organic Maps | app.organicmaps | F-Droid build 26072306 | 35 |
| 42 | Odyssey | org.gateshipone.odyssey | F-Droid build 42 | 33 |

 

# **3\. Feature Inventories**

## **Category: Pre-instrumented benchmark applications**

### **App Name: Wikipedia**

*Package: org.wikipedia  |  Version documented: LLMDroid instrumented build (79,210 methods)  |  Reference: Official Wikimedia Android app documentation and in-app menus*

**Features:**

**1\. Search for an article**

**Actions:** Open the app \-\> tap the search bar at the top of the Explore feed \-\> type the search term \-\> tap a result in the suggestion list to open the article.

**2\. Search by voice**

**Actions:** Tap the search bar \-\> tap the microphone icon at the right of the search field \-\> grant the microphone permission if prompted \-\> speak the query \-\> tap a result.

**3\. Browse the Explore feed**

**Actions:** Open the app \-\> the Explore tab is the default landing tab \-\> scroll vertically through the feed cards (Featured article, Top read, Picture of the day, Because you read, In the news, On this day, Places, Randomizer, Today on Wikipedia).

**4\. Customise which Explore feed cards are shown**

**Actions:** Open the Explore tab \-\> tap the overflow menu (three dots) on the feed header (or go to Settings \-\> Explore feed) \-\> toggle individual card types on or off \-\> tap the back arrow to return.

**5\. Hide a single feed card**

**Actions:** On the Explore feed \-\> tap the overflow menu (three dots) on the card \-\> choose the hide/"Don't show this card" option \-\> optionally tap Undo in the snackbar to restore it.

**6\. Read an article**

**Actions:** Open an article from search, the feed or a link \-\> scroll to read \-\> tap an internal blue link to open a preview or the linked article.

**7\. Preview a link before opening it**

**Actions:** While reading an article \-\> tap an internal wiki link \-\> the link preview sheet opens at the bottom showing the lead image and summary \-\> tap "Read article" to open it fully, or swipe the sheet down to dismiss.

**8\. Open the table of contents and jump to a section**

**Actions:** While reading an article \-\> tap the table-of-contents button (or swipe in from the right edge) \-\> tap the section name to scroll directly to that section.

**9\. Search within the current article (Find in article)**

**Actions:** Open an article \-\> tap the overflow menu (three dots) \-\> tap "Find in article" \-\> type the text \-\> use the up/down chevrons to step through matches \-\> tap the X to close.

**10\. Change the reading text size**

**Actions:** Open an article \-\> tap the "Aa" (theme/appearance) icon in the toolbar \-\> drag the text size slider or tap the smaller/larger "A" controls \-\> tap outside the panel to dismiss.

**11\. Change the reading theme (light, sepia, dark, black)**

**Actions:** Open an article \-\> tap the "Aa" (theme) icon \-\> tap Light, Sepia, Dark or Black \-\> tap outside the panel to apply and dismiss.

**12\. Change the reading font family**

**Actions:** Open an article \-\> tap the "Aa" (theme) icon \-\> select the serif or sans-serif font option in the panel.

**13\. Save an article to a reading list for offline use**

**Actions:** Open the article \-\> tap the bookmark/save icon in the bottom toolbar \-\> choose an existing reading list or tap "Create new" \-\> the article and its images are downloaded for offline reading.

**14\. Create a reading list**

**Actions:** Tap the Saved tab in the bottom navigation bar \-\> tap the "+" / "Create new list" button \-\> enter a list name \-\> enter an optional description \-\> tap OK/Create.

**15\. Rename or delete a reading list**

**Actions:** Open the Saved tab \-\> long-press a list (or open it and tap the overflow menu) \-\> choose Rename or Delete \-\> confirm.

**16\. Remove an article from a reading list**

**Actions:** Open the Saved tab \-\> open the list \-\> swipe the article row or long-press it \-\> tap Remove from list \-\> confirm.

**17\. Sync reading lists across devices**

**Actions:** Tap the Saved tab \-\> tap the sync prompt (or go to Settings \-\> "Sync reading lists") \-\> log in with a Wikipedia account \-\> toggle sync on.

**18\. Enable offline downloads of saved articles over Wi-Fi only**

**Actions:** Open Settings \-\> find the "Download only over Wi-Fi" option under the reading list/offline section \-\> toggle it on.

**19\. View browsing history**

**Actions:** Tap the History tab in the bottom navigation bar \-\> scroll the chronological list \-\> tap any entry to reopen the article.

**20\. Delete individual history entries or clear all history**

**Actions:** Open the History tab \-\> swipe an entry away to delete it, or tap the overflow menu / trash icon \-\> tap "Clear browsing history" \-\> confirm.

**21\. Search within browsing history**

**Actions:** Open the History tab \-\> tap the search icon \-\> type part of an article title \-\> tap a filtered result.

**22\. Open articles in tabs and manage them**

**Actions:** Long-press a link \-\> tap "Open in new tab" \-\> tap the tabs button in the bottom toolbar to see all open tabs \-\> tap a tab to switch, or swipe a tab away to close it.

**23\. Change the article language**

**Actions:** Open an article \-\> tap the language icon in the bottom toolbar \-\> select the target language from the list of available language versions.

**24\. Add and reorder app content languages**

**Actions:** Open Settings \-\> tap "Wikipedia languages" \-\> tap "+ Add language" \-\> search for and select the language \-\> drag the handle beside a language to reorder the preference list \-\> use the overflow menu to remove a language.

**25\. Browse nearby articles on a map (Places)**

**Actions:** Open the Explore feed and tap the Places card, or open Places from the feed \-\> grant the location permission \-\> pan or zoom the map \-\> tap a map pin \-\> tap the preview card to read the article.

**26\. Search for a location in Places**

**Actions:** Open Places \-\> tap the search field at the top \-\> type a place name \-\> select the location to recentre the map on it.

**27\. Open a random article**

**Actions:** Open the Explore feed \-\> scroll to the Randomizer card and tap it, or tap the dice/refresh control on the card to shuffle to a different random article.

**28\. View the images in an article in a full-screen gallery**

**Actions:** Open an article \-\> tap any image \-\> the gallery viewer opens \-\> swipe left or right to move between images \-\> pinch to zoom \-\> tap the info control to see the caption, licence and author.

**29\. Share an article**

**Actions:** Open an article \-\> tap the overflow menu (three dots) \-\> tap Share \-\> choose the target app from the Android share sheet.

**30\. Share a selected text snippet as a customised card**

**Actions:** Open an article \-\> long-press to select text \-\> tap the Share option in the selection toolbar \-\> choose the image/text share card \-\> pick the target app.

**31\. Open the current article in a web browser**

**Actions:** Open an article \-\> tap the overflow menu (three dots) \-\> tap "View in browser".

**32\. Log in to a Wikipedia account**

**Actions:** Open the Explore feed \-\> tap the account/profile icon in the toolbar (or open the main menu) \-\> tap "Log in" \-\> enter username and password \-\> tap Log in.

**33\. Create a Wikipedia account**

**Actions:** Tap the account icon \-\> tap "Join Wikipedia" / "Create an account" \-\> enter a username, password and optional email address \-\> complete the captcha \-\> tap Create account.

**34\. Log out of the account**

**Actions:** Tap the account/profile icon \-\> open the account menu \-\> tap "Log out" \-\> confirm.

**35\. Edit an article section**

**Actions:** Open an article \-\> tap the pencil/edit icon beside a section heading \-\> make the changes in the wikitext editor \-\> tap the next/arrow button \-\> enter an edit summary \-\> tap Publish.

**36\. Edit a full article**

**Actions:** Open an article \-\> tap the edit pencil in the toolbar \-\> select the full-article edit option \-\> modify the wikitext \-\> tap next \-\> add an edit summary \-\> tap Publish.

**37\. Preview an edit before publishing**

**Actions:** While editing \-\> tap the preview/next control in the editor toolbar \-\> review the rendered preview \-\> tap the back arrow to continue editing or Publish to save.

**38\. Use the editing toolbar for formatting and wiki syntax**

**Actions:** Open the editor \-\> use the formatting bar above the keyboard to insert bold, italics, links, headings, lists, references or templates \-\> continue typing.

**39\. Mark an edit as a minor edit or watch the page while publishing**

**Actions:** Edit an article \-\> tap next to reach the save screen \-\> toggle "Minor edit" and/or "Watch this page" \-\> tap Publish.

**40\. Add or edit a short description of an article**

**Actions:** Open an article \-\> tap the description area under the title (or use the Suggested edits entry point) \-\> type the short description \-\> tap Publish.

**41\. Complete Suggested edits tasks**

**Actions:** Open the Explore feed or the account menu \-\> tap "Suggested edits" \-\> choose a task type (add article description, translate description, add image caption, translate caption, image recommendations) \-\> complete the task on the card \-\> tap Publish, or tap Skip to move to the next item.

**42\. View your contributions and edit statistics**

**Actions:** Tap the account/profile icon \-\> tap "Contributions" \-\> browse the list of your edits and the contribution counters.

**43\. View an article's edit history and compare revisions**

**Actions:** Open an article \-\> tap the overflow menu (three dots) \-\> tap "Edit history" \-\> tap a revision to view it \-\> select two revisions to see the diff between them.

**44\. Add a page to your watchlist**

**Actions:** Open an article \-\> tap the overflow menu (three dots) \-\> tap "Watch" \-\> choose the watch duration (for example one week, one month, permanent).

**45\. View the watchlist**

**Actions:** Open the account/main menu \-\> tap "Watchlist" \-\> scroll the list of recent changes to watched pages \-\> tap an entry to see the diff.

**46\. Filter the watchlist**

**Actions:** Open the Watchlist \-\> tap the filter icon \-\> select the wikis, edit types and user types to include \-\> tap the back arrow to apply.

**47\. Read and reply on article talk pages**

**Actions:** Open an article \-\> tap the overflow menu (three dots) \-\> tap "Talk page" \-\> tap a discussion topic \-\> tap Reply \-\> type the message \-\> tap Publish.

**48\. Start a new talk page topic**

**Actions:** Open the talk page \-\> tap the "+" / new topic button \-\> enter a subject and body \-\> tap Publish.

**49\. Receive and read notifications**

**Actions:** Tap the bell/notifications icon in the toolbar \-\> scroll the notification list \-\> tap a notification to open the related page.

**50\. Configure notification types**

**Actions:** Open Settings \-\> tap "Notifications" \-\> toggle the categories (for example talk page messages, milestones, thanks, mentions) \-\> return to Settings.

**51\. Turn image loading off to save data**

**Actions:** Open Settings \-\> find "Show images" \-\> toggle it off so articles load without images.

**52\. Set the app-wide appearance/theme default**

**Actions:** Open Settings \-\> tap "App theme" (or open the "Aa" panel from any article) \-\> select the default theme and text size \-\> exit Settings.

**53\. Enable or disable link previews**

**Actions:** Open Settings \-\> find the "Show link previews" option \-\> toggle it off to make links open directly instead of showing a preview card.

**54\. Add the Wikipedia search widget to the home screen**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Wikipedia \-\> drag the search widget onto the home screen \-\> tap it to jump straight into search.

**55\. Add the Featured article widget to the home screen**

**Actions:** Long-press the home screen \-\> tap Widgets \-\> find Wikipedia \-\> drag the featured-article widget onto the home screen.

**56\. Send app feedback**

**Actions:** Open Settings or the main menu \-\> tap "About the Wikipedia app" \-\> tap "Send app feedback" \-\> write the message \-\> send.

**57\. Open the donate flow**

**Actions:** Open the main/account menu \-\> tap "Donate" \-\> the donation page opens in the browser or in-app view.

**58\. Clear cached data**

**Actions:** Open Settings \-\> scroll to the storage/cache option \-\> tap the clear cache control \-\> confirm.

**59\. View app licence and version information**

**Actions:** Open Settings \-\> tap "About the Wikipedia app" \-\> read the version number, licence and credits.

 

### **App Name: NewPipe**

*Package: org.schabi.newpipe  |  Version documented: LLMDroid instrumented build (75,480 methods)  |  Reference: Official NewPipe project documentation and in-app menus*

**Features:**

**1\. Search for content**

**Actions:** Open the app \-\> tap the search (magnifying glass) icon in the toolbar \-\> type the query \-\> tap the keyboard search key \-\> scroll the results.

**2\. Switch the service being searched (YouTube, SoundCloud, media.ccc.de, PeerTube, Bandcamp)**

**Actions:** Tap the search icon \-\> tap the service name / service selector at the top of the search screen \-\> choose the service \-\> re-run the search.

**3\. Filter and sort search results**

**Actions:** Run a search \-\> tap the filter icon in the search toolbar \-\> choose the content type (all, videos, channels, playlists) and the sort/upload-date filters \-\> tap OK to apply.

**4\. Play a video in the main player**

**Actions:** Tap a video in any list \-\> the detail page opens \-\> tap the thumbnail or the play control to start playback \-\> rotate the device or tap the fullscreen icon for fullscreen.

**5\. Play audio in the background**

**Actions:** Open a video detail page \-\> tap the headphones/background icon (or long-press the play button and choose Background) \-\> playback continues with the screen off and is controlled from the notification.

**6\. Play a video in a floating popup window**

**Actions:** Open a video detail page \-\> tap the popup icon \-\> grant the "draw over other apps" permission if prompted \-\> drag the floating window to reposition it \-\> pinch to resize \-\> drag it to the X to close.

**7\. Control playback speed and pitch**

**Actions:** Start playback \-\> tap the player to show controls \-\> tap the playback speed control (or the overflow menu in the player) \-\> adjust the tempo and pitch sliders \-\> optionally enable "unhook" to change them independently \-\> tap the back arrow.

**8\. Select the video resolution**

**Actions:** Start playback \-\> tap the player \-\> tap the quality selector (for example "720p") \-\> choose the resolution from the list.

**9\. Enable captions/subtitles**

**Actions:** Start playback \-\> tap the player \-\> tap the captions (CC) icon \-\> choose the caption track or "No captions".

**10\. Use gesture controls for volume and brightness**

**Actions:** During fullscreen playback \-\> swipe vertically on the right half of the screen to change volume \-\> swipe vertically on the left half to change brightness.

**11\. Seek and skip within a video**

**Actions:** During playback \-\> drag the seek bar, or double-tap the left or right side of the player to jump back or forward by the configured seek interval.

**12\. Enqueue a video to the play queue**

**Actions:** Long-press a video item in a list \-\> tap "Enqueue" (or "Enqueue next") \-\> open the queue from the player to see the ordered list.

**13\. Reorder or remove items in the play queue**

**Actions:** Start playback \-\> tap the queue icon in the player \-\> drag the handle beside an item to reorder it \-\> swipe an item away to remove it.

**14\. Repeat and shuffle the queue**

**Actions:** Open the player \-\> tap the queue \-\> tap the repeat icon to cycle off/one/all \-\> tap the shuffle icon to toggle shuffling.

**15\. Download a video, audio track or subtitle file**

**Actions:** Open a video detail page \-\> tap the download icon \-\> choose the Video, Audio or Subtitle tab \-\> select the format and quality \-\> confirm or edit the file name and target folder \-\> tap OK to start the download.

**16\. Manage downloads**

**Actions:** Open the navigation drawer (hamburger icon) \-\> tap "Downloads" \-\> use the Pending and Finished tabs \-\> tap the pause/resume control on a running download \-\> long-press an entry to delete it or to open the completed file.

**17\. Subscribe to a channel**

**Actions:** Open a channel page (tap the channel name on a video) \-\> tap the "Subscribe" button \-\> the channel is added to the subscription list.

**18\. Enable new-stream notifications for a channel**

**Actions:** Open a channel page \-\> subscribe \-\> tap the bell/notification icon beside the Subscribe button to enable notifications for new uploads.

**19\. View the subscription feed ("What's New")**

**Actions:** Open the navigation drawer \-\> tap "What's New" \-\> pull down to refresh \-\> tap a video to play it.

**20\. Create and use subscription feed groups**

**Actions:** Open the "What's New" feed \-\> tap the "+" beside the group carousel at the top \-\> enter a group name \-\> pick an icon \-\> select the channels to include \-\> tap the tick/save \-\> tap the group chip to filter the feed.

**21\. Import subscriptions from another service or file**

**Actions:** Open the drawer \-\> tap "Subscriptions" \-\> tap the overflow menu (three dots) \-\> tap "Import subscriptions" \-\> choose the source (for example a YouTube export, a SoundCloud profile or a previously exported JSON file) \-\> select the file or enter the profile \-\> confirm.

**22\. Export subscriptions to a file**

**Actions:** Open the drawer \-\> tap "Subscriptions" \-\> tap the overflow menu \-\> tap "Export subscriptions" \-\> choose the destination folder and file name \-\> tap Save.

**23\. Browse a channel page and its tabs**

**Actions:** Tap a channel name or avatar \-\> the channel page opens \-\> swipe between the Videos, Playlists, Channels, Shorts/Livestreams and About tabs as available for the service.

**24\. Create a local playlist**

**Actions:** Long-press a video in any list \-\> tap "Add to playlist" \-\> tap "Create a new playlist" \-\> enter the playlist name \-\> tap Create.

**25\. Add a video to an existing local playlist**

**Actions:** Long-press a video \-\> tap "Add to playlist" \-\> tap the target playlist name.

**26\. Reorder, rename or delete a local playlist**

**Actions:** Open the drawer \-\> tap "Bookmarked playlists" \-\> open the playlist \-\> drag the handles to reorder items, or tap the overflow menu \-\> tap Rename / Delete \-\> confirm.

**27\. Bookmark a remote playlist**

**Actions:** Open a playlist page from a channel or search result \-\> tap the bookmark/star icon \-\> the playlist appears under "Bookmarked playlists".

**28\. Set a playlist thumbnail**

**Actions:** Open a local playlist \-\> long-press an item \-\> tap "Set as playlist thumbnail".

**29\. Browse the kiosk/Trending page**

**Actions:** Open the drawer \-\> tap "Trending" (or the kiosk name for the selected service) \-\> scroll the list \-\> tap an item to play.

**30\. View watch history**

**Actions:** Open the drawer \-\> tap "History" \-\> use the "Watch history" tab \-\> tap an entry to replay it.

**31\. View and reuse search history**

**Actions:** Open the drawer \-\> tap "History" \-\> switch to the "Search history" tab \-\> tap an entry to re-run that search.

**32\. Clear watch or search history**

**Actions:** Open "History" \-\> tap the overflow menu (three dots) or the delete icon \-\> choose the history type to clear \-\> confirm.

**33\. Read comments on a video**

**Actions:** Open a video detail page \-\> scroll down to the Comments section (or tap the Comments tab) \-\> tap a comment to expand replies.

**34\. Browse related/recommended videos**

**Actions:** Open a video detail page \-\> scroll to the "Related items" section (or the Related tab) \-\> tap a suggestion to open it.

**35\. Share a video or channel**

**Actions:** Long-press an item (or open its detail page and use the overflow menu) \-\> tap Share \-\> pick the target app in the Android share sheet.

**36\. Open a video in an external browser or another app**

**Actions:** Open a video detail page \-\> tap the overflow menu (three dots) \-\> tap "Open in browser".

**37\. Play a video on Kodi**

**Actions:** Open a video detail page \-\> tap the overflow menu \-\> tap "Play with Kodi" \-\> install/enable the Kore companion app if prompted \-\> confirm the target device.

**38\. Mark a video as watched**

**Actions:** Long-press a video item in a feed or playlist \-\> tap "Mark as watched".

**39\. Change the app theme**

**Actions:** Open the drawer \-\> tap "Settings" \-\> tap "Appearance" \-\> select the theme (Light, Dark, Black or Automatic) \-\> return.

**40\. Configure video and audio playback defaults**

**Actions:** Open Settings \-\> tap "Video and audio" \-\> set the default resolution, the popup resolution, the preferred audio format, the default playback speed and the seek duration.

**41\. Configure player behaviour**

**Actions:** Open Settings \-\> tap "Player" / "Player behaviour" \-\> set options such as auto-play, resume on focus gain, minimise on app switch, remember popup size and background/popup defaults.

**42\. Configure download defaults**

**Actions:** Open Settings \-\> tap "Downloads" \-\> choose the video and audio download folders \-\> set the file naming character set \-\> toggle download-over-mobile behaviour and cross-network resume.

**43\. Configure history and cache options**

**Actions:** Open Settings \-\> tap "History and cache" \-\> toggle watch-history and search-history recording \-\> tap the controls to wipe cached metadata, image cache or the whole watch history.

**44\. Configure content and language options**

**Actions:** Open Settings \-\> tap "Content" \-\> set the preferred content language and country \-\> toggle showing comments, next/related videos, age-restricted content and the default kiosk/start page.

**45\. Back up and restore the application database and settings**

**Actions:** Open Settings \-\> tap "Backup and restore" (under Content) \-\> tap Export database to write a ZIP with subscriptions, playlists and history \-\> or tap Import database and select a previously exported ZIP \-\> confirm.

**46\. Enable the update check**

**Actions:** Open Settings \-\> tap "Updates" \-\> toggle the automatic update-check option (present on non-store builds).

**47\. Report an error / view the error log**

**Actions:** When an error dialog appears, tap "Report" \-\> review the generated report \-\> tap the copy or share control to send it.

 

### **App Name: Fing**

*Package: com.overlook.android.fing  |  Version documented: LLMDroid instrumented build (62,491 methods)  |  Reference: Official Fing help centre and store listing*

*Note: Fing is a proprietary application. Several capabilities require a Fing account, a paid subscription, or the separate Fingbox/Fing Agent hardware; those are labelled inline.*

**Features:**

**1\. Scan the local network for connected devices**

**Actions:** Open the app \-\> make sure the phone is joined to the Wi-Fi network to scan \-\> open the Devices/Network tab \-\> tap "Scan for devices" (or pull down to refresh) \-\> wait for the discovery to complete \-\> review the device list.

**2\. View detailed information about a discovered device**

**Actions:** Open the device list \-\> tap a device row \-\> review the details screen showing IP address, MAC address, hostname, vendor/manufacturer, device type, model, first-seen and last-seen times.

**3\. Edit a device's name, type and manufacturer**

**Actions:** Tap a device in the list \-\> tap the edit (pencil) icon \-\> change the custom name, device type, brand/model and owner \-\> tap Save.

**4\. Search and filter the device list**

**Actions:** Open the Devices tab \-\> tap the search icon at the bottom of the list \-\> type part of a name, IP or MAC address \-\> or tap the filter control to filter by state (online/offline) or type.

**5\. Delete a device from the network inventory**

**Actions:** Open the Devices tab \-\> long-press or swipe the device row (or open the device and use the overflow menu) \-\> tap Delete \-\> confirm.

**6\. Run a port scan against a device (Find open ports)**

**Actions:** Tap a device in the device list \-\> tap "Find open ports" / the port-scan action \-\> wait for the scan \-\> review the list of open TCP ports and the services detected.

**7\. Ping a device**

**Actions:** Open a device detail screen \-\> tap the Ping action \-\> observe the round-trip latency, packet loss and the running chart \-\> tap Stop to end.

**8\. Run a traceroute to a host**

**Actions:** Open the Tools tab \-\> tap "Traceroute" \-\> enter the target host name or IP address \-\> tap Start \-\> review each hop and its transit delay.

**9\. Perform a DNS lookup**

**Actions:** Open the Tools tab \-\> tap "DNS Lookup" \-\> enter the host name or IP address \-\> optionally choose a custom DNS server \-\> tap the lookup button \-\> read the forward or reverse resolution result.

**10\. Look up a MAC address vendor**

**Actions:** Open the Tools tab \-\> tap "MAC Lookup" \-\> type or paste the MAC address \-\> tap the lookup button \-\> read the recognised device brand, type and model.

**11\. Scan nearby Wi-Fi access points**

**Actions:** Open the Tools tab \-\> tap "Wi-Fi Scanner" \-\> grant the location permission if prompted \-\> review the nearby access points with their SSID, channel, signal strength and likely channel collisions.

**12\. Run DHCP discovery**

**Actions:** Open the Tools tab \-\> tap "DHCP Discovery" \-\> start the probe \-\> review the DHCP servers that answered and the offered lease parameters.

**13\. Run an internet speed test**

**Actions:** Open the Internet/Speed tab \-\> tap the start button \-\> wait while the download speed, upload speed and latency are measured \-\> review the result summary.

**14\. Run a Wi-Fi speed test between the phone and the router**

**Actions:** Open the Internet/Speed area \-\> select the Wi-Fi speed test option \-\> tap Start \-\> review the measured local link speed.

**15\. View internet connection and ISP details**

**Actions:** Open the Internet tab \-\> review the public IP address, the ISP name, the connection type and the current outage/quality status.

**16\. View current network details**

**Actions:** Tap the network selector (the circular three-dot icon at the top-right) \-\> tap "Current network" \-\> review the SSID/BSSID, gateway, subnet mask, DNS servers and network class.

**17\. Switch between networks and view scan history**

**Actions:** Tap the network selector at the top-right \-\> choose "Monitored networks" to list networks linked to the account, or "Scanned networks" to list previous scans \-\> tap a network to load it.

**18\. Unlink or delete a saved network**

**Actions:** Open the network selector \-\> open "Monitored networks" \-\> swipe left on the network entry \-\> tap the delete/unlink action \-\> confirm.

**19\. Create a Fing account**

**Actions:** Open the account/profile area \-\> tap "Sign up" \-\> enter an email address and password (or use a supported single sign-on provider) \-\> confirm the verification email.

**20\. Log in and sync data across devices**

**Actions:** Open the account area \-\> tap "Log in" \-\> enter the credentials \-\> the app syncs monitored networks and device inventories with Fing Desktop and Fing Agent.

**21\. Receive network and device alerts (account required)**

**Actions:** Log in to a Fing account \-\> open the alerts/notification settings \-\> enable alerts for new devices, device state changes and security events \-\> choose push and/or email delivery.

**22\. Review the network event timeline**

**Actions:** Open the Events/Timeline area \-\> scroll the chronological list of device join/leave events, outages and alerts \-\> tap an entry for detail.

**23\. Run a network security check**

**Actions:** Open the Security/Network protection area \-\> tap the security check action \-\> wait for the assessment \-\> review the reported vulnerabilities, open ports and recommendations.

**24\. Block or pause a device's internet access (requires Fingbox or a subscription)**

**Actions:** Open a device detail screen \-\> tap the block/pause action \-\> confirm \-\> the device is blocked or paused according to the plan and hardware in use.

**25\. Schedule screen time / parental controls (requires Fingbox)**

**Actions:** Open the device or user profile \-\> tap the parental control / screen time option \-\> set the schedule \-\> save.

**26\. Track people's presence on the network (Digital Presence, requires Fingbox)**

**Actions:** Assign devices to people in the device details \-\> open the People/Presence widget on the main dashboard \-\> review who is present based on device activity.

**27\. Detect devices near the home (Digital Fence, requires Fingbox)**

**Actions:** Pair a Fingbox \-\> open the Digital Fence area \-\> review the nearby devices detected in radio range.

**28\. Analyse bandwidth usage per device (requires Fingbox)**

**Actions:** Open the bandwidth analysis area on a paired Fingbox network \-\> select the time range \-\> review the per-device usage chart.

**29\. Wake a device with Wake-on-LAN**

**Actions:** Open the device detail screen for a device that supports Wake-on-LAN \-\> tap the "Wake on LAN" action \-\> confirm.

**30\. Share or export a network report**

**Actions:** Open the network overview \-\> tap the overflow/share control \-\> choose the export or share option \-\> pick the destination app.

**31\. Configure application settings**

**Actions:** Open the account/settings area \-\> tap Settings \-\> adjust preferences such as notifications, theme/appearance, measurement units, discovery options and account details.

**32\. Rate, get support or read the help documentation**

**Actions:** Open the settings/account area \-\> tap the Help, Support or About entry \-\> open the linked knowledge base or contact form.

 

### **App Name: Time Planner**

*Package: com.albul.timeplanner  |  Version documented: LLMDroid instrumented build (23,280 methods)  |  Reference: Official Time Planner store listing and in-app tabs*

*Note: Time Planner ships as a free version with an in-app Pro upgrade. Features that the developer lists as Pro-only are labelled inline.*

**Features:**

**1\. Create an activity category**

**Actions:** Open the Tasks/Activities tab \-\> tap the "+" (add) button \-\> choose to create a category \-\> enter the category name \-\> pick an icon \-\> pick a colour \-\> tap the save/tick button.

**2\. Create a subcategory under a category**

**Actions:** Open the Tasks tab \-\> open the parent category \-\> tap the "+" button inside it \-\> enter the subcategory name \-\> choose an icon and colour \-\> tap save.

**3\. Create a task**

**Actions:** Open the Tasks tab \-\> tap the "+" button \-\> choose task \-\> enter the task name \-\> assign it to a category \-\> set the icon, colour and priority \-\> tap save.

**4\. Create nested subtasks (Pro)**

**Actions:** Open an existing task \-\> tap the add-subtask control \-\> enter the subtask name \-\> repeat to build further nesting levels \-\> tap save.

**5\. Set a task priority mark**

**Actions:** Create or edit a task \-\> tap the priority control \-\> select the priority level \-\> tap save.

**6\. Schedule an activity on the timeline**

**Actions:** Open the Schedule tab \-\> tap the "+" button (or long-press an empty slot on the timeline) \-\> select the activity/category \-\> set the start time and duration \-\> choose the repeat pattern \-\> tap save.

**7\. Switch the schedule between timeline mode and part-of-day mode**

**Actions:** Open the Schedule tab \-\> tap the view-mode control in the toolbar \-\> choose the timeline view or the part-of-the-day view.

**8\. Move or resize a scheduled activity**

**Actions:** Open the Schedule tab \-\> long-press a scheduled block \-\> drag it to a new time to move it \-\> drag its edge handle to change its duration \-\> release to save.

**9\. Navigate the schedule by day, week or month**

**Actions:** Open the Schedule tab \-\> swipe horizontally to move between days \-\> tap the date header to open the date picker \-\> select the target date.

**10\. Start tracking time with a bubble**

**Actions:** Open the Logging tab (or the schedule) \-\> tap the activity bubble to start tracking \-\> the elapsed time runs on the bubble \-\> tap the bubble again to stop and write the log entry.

**11\. Log a completed activity manually**

**Actions:** Open the Logging tab \-\> tap the "+" button \-\> select the activity \-\> set the start time and end time (or duration) \-\> add an optional note \-\> tap save.

**12\. Edit or delete a logged entry**

**Actions:** Open the Logging tab \-\> tap a log entry \-\> change the activity, times or note \-\> tap save, or tap the delete icon and confirm.

**13\. Search log entries by text**

**Actions:** Open the Logging tab \-\> tap the search icon \-\> type the text to match \-\> review the filtered log entries.

**14\. Filter logs and schedule entries (Pro)**

**Actions:** Open the Logging or Schedule tab \-\> tap the filter icon \-\> select the categories, activities or types to include \-\> apply the filter.

**15\. View statistics of planned versus actual time**

**Actions:** Open the Statistics tab \-\> choose the period (day, week, month, or a custom range) \-\> review the charts comparing scheduled time with logged time per category. Detailed and unlimited statistics are a Pro feature.

**16\. Switch the statistics chart type and grouping**

**Actions:** Open the Statistics tab \-\> tap the chart-type/grouping control \-\> select the chart type and whether to group by category or subcategory.

**17\. Create a note with rich formatting**

**Actions:** Open the Notes tab \-\> tap the "+" button \-\> enter a title and body \-\> use the formatting controls to apply bold, italic, lists or colour \-\> tap save.

**18\. Attach a note to a task or activity**

**Actions:** Open the task or activity editor \-\> tap the note field \-\> type or select the note content \-\> tap save.

**19\. Set a reminder for a task or scheduled activity**

**Actions:** Open the task or activity editor \-\> tap the reminder section \-\> choose the reminder type and lead time \-\> select the notification sound \-\> tap save.

**20\. Set an alarm with an anti-procrastination captcha**

**Actions:** Open the reminder settings for the activity \-\> select the alarm reminder type \-\> enable the captcha option \-\> choose the captcha style \-\> save. When the alarm fires, solve the captcha to dismiss it.

**21\. Use the timer, stopwatch and countdown (Pro)**

**Actions:** Open the timer/stopwatch area from the toolbar or drawer \-\> choose Timer, Stopwatch or Countdown \-\> set the duration for a countdown \-\> tap start \-\> tap stop or reset when finished.

**22\. View the moon calendar**

**Actions:** Open the navigation drawer or the schedule toolbar \-\> tap the moon calendar entry \-\> browse the lunar phase information by date.

**23\. Import events from Google Calendar**

**Actions:** Open Settings (or the drawer) \-\> tap the import/Google Calendar option \-\> grant calendar access \-\> select the calendars to import \-\> confirm.

**24\. Back up the application data**

**Actions:** Open Settings \-\> tap Backup \-\> tap "Create backup" \-\> choose the destination folder \-\> confirm.

**25\. Restore data from a backup**

**Actions:** Open Settings \-\> tap Backup \-\> tap Restore \-\> select the backup file \-\> confirm the restore.

**26\. Customise icons and colours**

**Actions:** Open any category, task or activity editor \-\> tap the icon control to choose from the icon set \-\> tap the colour control to choose from the palette \-\> tap save.

**27\. Change the application theme and appearance**

**Actions:** Open Settings \-\> tap the appearance/theme section \-\> choose the theme, accent colour and font size \-\> return.

**28\. Configure notification sounds and vibration**

**Actions:** Open Settings \-\> tap the notifications/sound section \-\> select the default reminder sound and vibration behaviour. Additional sounds are available in the Pro version.

**29\. Add a home screen widget (Pro)**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Time Planner \-\> drag the widget onto the home screen \-\> configure what it displays.

**30\. Set the first day of the week and time format**

**Actions:** Open Settings \-\> tap the general/date-and-time section \-\> set the first day of the week and the 12/24-hour time format.

**31\. Reorder categories and tasks**

**Actions:** Open the Tasks tab \-\> enter the reorder/edit mode from the overflow menu \-\> drag the handle beside an item to its new position \-\> confirm.

**32\. Archive or delete a category, task or activity**

**Actions:** Open the Tasks tab \-\> long-press the item \-\> tap Delete (or the archive option) \-\> confirm.

**33\. Upgrade to the Pro version**

**Actions:** Open Settings or the drawer \-\> tap the Pro/upgrade entry \-\> review the feature list \-\> complete the in-app purchase.

 

### **App Name: NHK WORLD-JAPAN**

*Package: jp.or.nhk.nhkworld.tv  |  Version documented: LLMDroid instrumented build (51,729 methods)  |  Reference: Official NHK WORLD-JAPAN store listing and app documentation*

*Note: Content availability varies by region and by the language selected; some programmes are excluded from on-demand for rights reasons.*

**Features:**

**1\. Watch the 24-hour live TV stream**

**Actions:** Open the app \-\> tap the Live (TV) tab \-\> tap the play control on the live player \-\> wait for the stream to buffer \-\> tap the fullscreen icon for fullscreen playback.

**2\. Listen to the live radio stream**

**Actions:** Open the app \-\> tap the Radio/Live radio tab \-\> select the language service \-\> tap play \-\> playback continues while the notification control is shown.

**3\. Select the app content language**

**Actions:** Open Settings (or the language selector in the toolbar) \-\> tap the language option \-\> choose from the supported languages (for example English, Japanese, Chinese, Spanish, French, Arabic, Hindi, Indonesian, Korean, Portuguese, Russian, Thai, Vietnamese and others) \-\> confirm; the news, radio and programme lists reload in that language.

**4\. Read the latest news headlines**

**Actions:** Open the News tab \-\> scroll the headline list \-\> tap a headline to open the full story.

**5\. Read a news article with its video clip**

**Actions:** Open a news item from the News tab \-\> tap the embedded video to play the report \-\> scroll to read the accompanying text.

**6\. Browse news by category**

**Actions:** Open the News tab \-\> tap a category chip or the category selector (for example Latest, Japan, World, Business, Sports) \-\> scroll the filtered list.

**7\. Watch video programmes on demand**

**Actions:** Open the On Demand / Video tab \-\> browse or search the programme list \-\> tap a programme \-\> tap an episode \-\> tap play.

**8\. Listen to audio programmes on demand**

**Actions:** Open the On Demand / Audio (Radio) area \-\> select a programme \-\> tap an episode \-\> tap play.

**9\. Use the 7-day catch-up for TV and radio**

**Actions:** Open the Live or Programmes area \-\> open the schedule/catch-up view \-\> select a date within the past seven days \-\> tap the programme slot to play the recorded broadcast.

**10\. Browse programmes by genre or category**

**Actions:** Open the Programmes / On Demand tab \-\> tap a genre or category filter (for example News, Documentary, Culture, Food, Travel, Science, Learn Japanese) \-\> scroll the filtered list.

**11\. Search for a programme or news item**

**Actions:** Tap the search icon in the toolbar \-\> type the keyword \-\> tap search \-\> tap a result to open it.

**12\. View the TV programme schedule**

**Actions:** Open the Schedule / Programme guide tab \-\> select the date \-\> scroll the timetable \-\> tap an entry for the programme description.

**13\. Change the schedule display time zone**

**Actions:** Open the Schedule tab or Settings \-\> tap the time zone option \-\> select the desired time zone (for example local time or Japan Standard Time) \-\> confirm.

**14\. Add a programme or episode to My List / Favourites**

**Actions:** Open a programme or episode page \-\> tap the favourite/bookmark (star or heart) icon \-\> the item is added to the saved list.

**15\. View and manage the saved list**

**Actions:** Open the My List / Favourites tab \-\> scroll the saved items \-\> tap an item to open it \-\> tap the favourite icon again (or use the edit/delete control) to remove it.

**16\. Enable push notifications for breaking news**

**Actions:** Open Settings \-\> tap Notifications \-\> toggle breaking-news notifications on \-\> grant the Android notification permission if prompted.

**17\. Enable emergency alerts for earthquakes, tsunami and weather warnings**

**Actions:** Open Settings \-\> tap Notifications \-\> enable the emergency information alerts (available in the supported languages) \-\> save.

**18\. Control video playback**

**Actions:** Start any video \-\> tap the player to reveal the controls \-\> use play/pause, the seek bar, and the skip controls \-\> tap the fullscreen icon to toggle fullscreen \-\> rotate the device for landscape playback.

**19\. Turn subtitles or closed captions on and off**

**Actions:** Start a video \-\> tap the player \-\> tap the subtitle/CC control \-\> select the subtitle track or turn subtitles off (available where the programme provides them).

**20\. Change the streaming quality**

**Actions:** Start a video \-\> tap the player \-\> open the quality/settings control \-\> select the bitrate or the automatic option.

**21\. Restrict streaming to Wi-Fi to limit mobile data**

**Actions:** Open Settings \-\> find the data usage / playback over mobile network option \-\> toggle Wi-Fi-only streaming on.

**22\. Share a programme or news item**

**Actions:** Open the programme or article \-\> tap the share icon \-\> choose the destination app in the Android share sheet.

**23\. Study Japanese with the Easy Japanese lessons**

**Actions:** Open the Programmes / Learn Japanese area \-\> select the Easy Japanese course \-\> tap a lesson \-\> play the audio or video and follow the accompanying text.

**24\. Continue watching a partly-watched programme**

**Actions:** Reopen the app \-\> find the continue-watching entry on the home screen or in the programme page \-\> tap it to resume from the saved position.

**25\. Cast the stream to a TV**

**Actions:** Start playback \-\> tap the cast icon in the player toolbar \-\> select the target device on the same network. Availability of casting has changed between releases; confirm on the installed build. Marked "Unable to verify" for the exact instrumented build.

**26\. Read the programme description and episode details**

**Actions:** Open a programme \-\> scroll below the player to read the synopsis, broadcast date, duration and presenter information.

**27\. Open the settings screen**

**Actions:** Tap the menu (hamburger) or the settings gear icon \-\> review options such as language, notifications, time zone, data usage, text size and cache.

**28\. Clear the application cache**

**Actions:** Open Settings \-\> scroll to the storage/cache entry \-\> tap the clear cache control \-\> confirm.

**29\. View terms of use, privacy policy and app version**

**Actions:** Open Settings \-\> tap the About / Information entry \-\> read the terms of service, the privacy policy and the version number.

**30\. Send feedback or contact NHK**

**Actions:** Open Settings \-\> tap the contact/feedback entry \-\> complete the form or open the linked contact page.

 

## **Category: Notes and writing**

### **App Name: Markor**

*Package: net.gsantner.markor  |  Version documented: 2.16.1  |  Reference: Official Markor repository documentation and F-Droid listing*

**Features:**

**1\. Browse the notebook folder**

**Actions:** Open the app \-\> the Files tab opens at the configured notebook root \-\> tap a folder to enter it \-\> tap the up arrow or the breadcrumb path to move back up.

**2\. Create a new plain text or Markdown document**

**Actions:** Open the Files tab \-\> tap the "+" floating action button \-\> tap "File" \-\> enter the file name \-\> choose the file type/extension (for example .md, .txt) \-\> optionally pick a template \-\> tap OK.

**3\. Create a document from a template**

**Actions:** Tap the "+" button \-\> tap File \-\> tap the template selector \-\> choose a template (for example empty file, Markdown reference, to-do list, Zim page or a user template) \-\> enter the name \-\> tap OK.

**4\. Create a folder**

**Actions:** Open the Files tab \-\> tap the "+" button \-\> tap "Folder" \-\> enter the folder name \-\> tap OK.

**5\. Edit a document in the text editor**

**Actions:** Open the Files tab \-\> tap a file \-\> the editor opens \-\> type the content \-\> tap the back arrow or the save icon; changes are stored to the file.

**6\. Switch between edit mode and rendered preview**

**Actions:** Open a document \-\> tap the preview/eye icon in the toolbar \-\> the rendered view is shown \-\> tap the icon again (or the edit pencil) to return to editing.

**7\. Apply Markdown formatting with the action toolbar**

**Actions:** Open a Markdown document \-\> place the cursor or select text \-\> tap an icon on the format action bar below the editor (bold, italic, strikethrough, heading level, code, quote, horizontal rule) \-\> the syntax is inserted around the selection.

**8\. Insert bullet, numbered and checkbox lists**

**Actions:** Open a document \-\> position the cursor on the line \-\> tap the list, numbered list or checkbox action in the action bar \-\> continue typing; pressing Enter continues the list automatically.

**9\. Insert a link**

**Actions:** Open a document \-\> select the text to link (optional) \-\> tap the link action in the action bar \-\> enter or pick the target path or URL \-\> confirm; the Markdown link syntax is inserted.

**10\. Insert an image from the gallery or camera**

**Actions:** Open a document \-\> tap the image/attachment action in the action bar \-\> choose "Take a picture", "Pick from gallery" or "Select a file" \-\> grant the permission if prompted \-\> the image is copied into the attachment folder and the Markdown image reference is inserted.

**11\. Record and insert an audio note**

**Actions:** Open a document \-\> tap the attachment action \-\> choose the audio recording option \-\> grant the microphone permission \-\> tap record \-\> tap stop \-\> the recording is saved and linked in the document.

**12\. Insert the current date or time**

**Actions:** Open a document \-\> tap the date/time action in the action bar \-\> select the required format from the list (or long-press to configure the default format) \-\> the timestamp is inserted at the cursor.

**13\. Insert a table**

**Actions:** Open a Markdown document \-\> tap the table action in the action bar \-\> choose the number of columns \-\> the table skeleton is inserted \-\> fill in the cells.

**14\. Undo and redo edits**

**Actions:** While editing \-\> tap the undo arrow in the toolbar to revert the last change \-\> tap the redo arrow to reapply it.

**15\. Search inside the open document**

**Actions:** Open a document \-\> tap the search icon in the editor toolbar \-\> type the search term \-\> step through the highlighted matches.

**16\. Search across all files in the notebook**

**Actions:** Open the Files tab \-\> tap the search icon in the toolbar \-\> type the query \-\> choose whether to search file names only or file contents \-\> review the matching files \-\> tap a result to open it.

**17\. Open the QuickNote file**

**Actions:** Tap the QuickNote tab in the bottom navigation bar (or open it from the drawer) \-\> the dedicated QuickNote document opens directly in the editor.

**18\. Open the To-Do file**

**Actions:** Tap the To-Do tab in the bottom navigation bar \-\> the dedicated to-do document opens in the editor.

**19\. Manage a todo.txt file**

**Actions:** Open or create a .txt file in todo.txt format \-\> the todo.txt action bar appears \-\> use the actions to add a priority, a project (+), a context (@), a due date or to mark a line done \-\> tap the sort action to reorder by priority, due date, project or context.

**20\. Edit a Zim Wiki page**

**Actions:** Open a file with the Zim Wiki extension/format \-\> the Zim-specific action bar appears \-\> use the heading, bold, italic, checkbox and link actions \-\> tap the preview icon to see the rendered page.

**21\. Edit AsciiDoc, Org-Mode, CSV and plain text files**

**Actions:** Open a file with the corresponding extension \-\> Markor selects the matching syntax highlighting and action bar \-\> edit the content \-\> use the preview toggle where a renderer is available.

**22\. Preview a CSV file as a table**

**Actions:** Open a .csv file \-\> tap the preview/eye icon \-\> the delimited data is rendered as a table.

**23\. Create a Markdown presentation**

**Actions:** Create or open a Markdown file containing the presentation front-matter/slide separators \-\> tap the preview icon \-\> the slides are rendered \-\> swipe or tap to advance between slides.

**24\. Export the document as a PDF or print it**

**Actions:** Open a document \-\> tap the overflow menu (three dots) \-\> tap "Share" or the print/PDF option \-\> choose "Print / Save as PDF" \-\> select the printer or "Save as PDF" \-\> confirm.

**25\. Share the document as plain text or rendered HTML**

**Actions:** Open a document \-\> tap the overflow menu \-\> tap Share \-\> choose to share the raw text, the rendered HTML or the file itself \-\> pick the target app.

**26\. Rename a file or folder**

**Actions:** Open the Files tab \-\> long-press the item to select it \-\> tap the rename action in the contextual toolbar \-\> enter the new name \-\> tap OK.

**27\. Move or copy files and folders**

**Actions:** Open the Files tab \-\> long-press one or more items \-\> tap the move or copy action \-\> browse to the destination folder \-\> tap the confirm button.

**28\. Delete files and folders**

**Actions:** Open the Files tab \-\> long-press the items to select them \-\> tap the delete (bin) icon \-\> confirm the deletion.

**29\. Select multiple files at once**

**Actions:** Open the Files tab \-\> long-press the first item \-\> tap additional items to add them to the selection \-\> use the select-all action in the contextual toolbar if required \-\> apply the wanted bulk action.

**30\. Mark a file or folder as a favourite**

**Actions:** Open the Files tab \-\> long-press the item \-\> tap the favourite (star) action \-\> open the favourites view from the drawer or the folder shortcuts to reach it quickly.

**31\. Sort the file list**

**Actions:** Open the Files tab \-\> tap the sort icon (or the overflow menu \-\> Sort) \-\> choose the sort key (name, date modified, file size or file type) \-\> toggle ascending/descending \-\> optionally enable "folders first".

**32\. Show or hide hidden files**

**Actions:** Open the Files tab \-\> tap the overflow menu (three dots) \-\> toggle "Show hidden files".

**33\. Jump to a specific folder path**

**Actions:** Open the Files tab \-\> tap the overflow menu \-\> tap the "Go to" option \-\> choose a preset location (notebook, internal storage, SD card, app data, recent or popular documents) or type a path \-\> confirm.

**34\. View recent and popular documents**

**Actions:** Open the Files tab \-\> tap the "Go to" menu \-\> tap "Recent documents" or "Popular documents" \-\> tap a listed file to reopen it.

**35\. View file information**

**Actions:** Open the Files tab \-\> long-press a file \-\> tap the info action \-\> read the path, size, modification date and permissions.

**36\. Encrypt and open password-protected notes**

**Actions:** Open Settings \-\> set the encryption password under the encryption/security section \-\> create or open a file with the encrypted (.jenc) extension \-\> enter the password when prompted \-\> edit the decrypted content as usual.

**37\. Open a file with another application**

**Actions:** Open the Files tab \-\> long-press a file \-\> tap the "Open with" action \-\> select the external app from the chooser.

**38\. Add a launcher shortcut to a document**

**Actions:** Open the Files tab \-\> long-press a file \-\> tap the "Create launcher shortcut" action \-\> confirm the placement on the Android home screen.

**39\. Add the Markor home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Markor \-\> drag the widget onto the home screen \-\> choose the folder or file it should open.

**40\. Change the notebook (root) directory**

**Actions:** Open Settings \-\> tap the "Notebook" / root folder entry \-\> browse to the folder to use \-\> tap the select/confirm button.

**41\. Change the theme and colours**

**Actions:** Open Settings \-\> tap "Appearance"/theme \-\> choose light, dark or system default \-\> set the editor background and accent colour options.

**42\. Change the editor font family and size**

**Actions:** Open Settings \-\> open the editor section \-\> tap the font family entry to pick a font \-\> tap the font size entry and set the value.

**43\. Configure editor behaviour**

**Actions:** Open Settings \-\> open the editor section \-\> toggle options such as line numbers, syntax highlighting, word wrap, auto-format, tab width, keep screen on, and highlighting delay.

**44\. Configure the format action bar buttons**

**Actions:** Open Settings \-\> open the action-bar/format section \-\> enable, disable or reorder the individual formatting actions shown above the keyboard.

**45\. Change the app language**

**Actions:** Open Settings \-\> tap the Language entry \-\> choose the interface language from the list \-\> the app reloads in that language.

**46\. Review the changelog, help and licences**

**Actions:** Open Settings or the overflow menu \-\> tap "About"/"Help" \-\> read the changelog, the built-in help pages, the open-source licences and the version number.

 

### **App Name: Omni Notes**

*Package: it.feio.android.omninotes.foss  |  Version documented: 6.3.1  |  Reference: Official Omni Notes repository documentation and F-Droid listing*

**Features:**

**1\. Create a text note**

**Actions:** Open the app \-\> tap the "+" floating action button \-\> tap the text/note option \-\> enter a title \-\> enter the note body \-\> tap the back arrow to save.

**2\. Create a checklist note**

**Actions:** Tap the "+" button \-\> tap the checklist option (or open a note and use the overflow menu \-\> "Convert to checklist") \-\> type the first item \-\> press Enter to add the next item \-\> tap the back arrow to save.

**3\. Tick and untick checklist items**

**Actions:** Open a checklist note \-\> tap the checkbox beside an item to mark it done \-\> tap it again to clear it; completed items move or are struck through according to the settings.

**4\. Convert a note between text and checklist**

**Actions:** Open a note \-\> tap the overflow menu (three dots) \-\> tap "Convert to checklist" or "Convert to note" \-\> confirm.

**5\. Attach a photo from the camera**

**Actions:** Open a note \-\> tap the attachment (paper clip) icon \-\> tap Camera \-\> grant the camera permission if prompted \-\> take the picture \-\> confirm to attach it.

**6\. Attach an image or video from the gallery**

**Actions:** Open a note \-\> tap the attachment icon \-\> tap Gallery/Files \-\> select the media \-\> confirm.

**7\. Record and attach an audio note**

**Actions:** Open a note \-\> tap the attachment icon \-\> tap the recording option \-\> grant the microphone permission \-\> tap record \-\> tap stop \-\> the recording is attached to the note.

**8\. Create and attach a sketch**

**Actions:** Open a note \-\> tap the attachment icon \-\> tap "Sketch" \-\> draw on the canvas \-\> use the stroke size, eraser and colour controls \-\> tap the back arrow/save to attach the drawing.

**9\. Attach an arbitrary file**

**Actions:** Open a note \-\> tap the attachment icon \-\> tap Files \-\> browse and select the file \-\> confirm.

**10\. Add a location to a note**

**Actions:** Open a note \-\> tap the overflow menu \-\> tap "Add location" \-\> grant the location permission \-\> confirm the detected address or search for a place \-\> tap OK.

**11\. Set a reminder on a note**

**Actions:** Open a note \-\> tap the alarm/clock icon \-\> pick the date \-\> pick the time \-\> tap Done; the reminder fires as an Android notification.

**12\. Set a recurring reminder**

**Actions:** Open the reminder dialog on a note \-\> tap the repeat/recurrence option \-\> choose the repetition rule (for example daily, weekly, monthly, yearly or a custom rule) \-\> confirm.

**13\. View all notes that have reminders**

**Actions:** Open the navigation drawer (hamburger icon or left-edge swipe) \-\> tap "Reminders" \-\> review the notes with scheduled alarms.

**14\. Create a category**

**Actions:** Open the navigation drawer \-\> tap "Categories" (or the manage-categories entry) \-\> tap the "+" button \-\> enter the category name and description \-\> pick a colour \-\> tap Save.

**15\. Edit or delete a category**

**Actions:** Open the drawer \-\> open the categories list \-\> long-press (or tap) the category \-\> tap Edit to change the name, description or colour, or tap Delete \-\> confirm.

**16\. Assign a category to a note**

**Actions:** Open a note \-\> tap the overflow menu \-\> tap "Category" \-\> select the category from the list \-\> the note is colour-coded accordingly.

**17\. Filter notes by category**

**Actions:** Open the navigation drawer \-\> tap the category name in the drawer list \-\> the note list shows only the notes in that category.

**18\. Tag notes with hashtags**

**Actions:** Open a note \-\> type a hashtag such as "\#work" in the title or body (or tap the tag action in the overflow menu and pick a tag) \-\> save the note.

**19\. Filter notes by tag**

**Actions:** Open the navigation drawer \-\> tap "Tags" \-\> select one or more tags \-\> confirm; the list is filtered to notes carrying those tags.

**20\. Search notes**

**Actions:** Tap the search icon in the toolbar \-\> type the search text \-\> the note list filters as you type \-\> tap a result to open it.

**21\. Archive a note**

**Actions:** On the note list \-\> swipe the note (according to the configured swipe action) or open the note and tap the overflow menu \-\> tap "Archive"; the note moves to the Archive section of the drawer.

**22\. Restore a note from the archive**

**Actions:** Open the drawer \-\> tap "Archive" \-\> long-press the note \-\> tap the unarchive action \-\> confirm.

**23\. Move a note to the trash**

**Actions:** On the note list \-\> long-press the note \-\> tap the delete (bin) icon \-\> confirm; the note moves to Trash.

**24\. Restore or permanently delete notes from the trash**

**Actions:** Open the drawer \-\> tap "Trash" \-\> long-press the note \-\> tap Restore to bring it back, or tap Delete permanently \-\> confirm. Use "Empty trash" from the overflow menu to purge everything.

**25\. Pin a note to the top of the list**

**Actions:** Long-press the note in the list \-\> tap the pin action in the contextual toolbar; pinned notes stay above the rest.

**26\. Lock a note with a password**

**Actions:** Open Settings \-\> Security \-\> set a password and a recovery question \-\> open the note \-\> tap the overflow menu \-\> tap "Lock"; the note content is hidden until the password is entered.

**27\. Unlock a locked note**

**Actions:** Tap a locked note in the list \-\> enter the password in the prompt \-\> tap OK to reveal the content.

**28\. Merge several notes into one**

**Actions:** Long-press the first note \-\> tap the additional notes to add them to the selection \-\> tap the overflow menu in the contextual toolbar \-\> tap "Merge" \-\> confirm; the contents are combined into a single note.

**29\. Duplicate a note**

**Actions:** Open a note \-\> tap the overflow menu \-\> tap "Duplicate"; a copy is created in the list.

**30\. Share a note**

**Actions:** Open a note \-\> tap the share icon \-\> choose whether to include attachments if prompted \-\> select the destination app from the Android share sheet.

**31\. Add a note from another app via the share sheet**

**Actions:** In any app, select text or a file \-\> tap Share \-\> choose Omni Notes \-\> the content opens as a new note \-\> add a title \-\> tap back to save.

**32\. Sort the note list**

**Actions:** Tap the overflow menu (three dots) in the note list \-\> tap "Sort by" \-\> choose the criterion (for example creation date, last modification, reminder date, title or manual/drag order) \-\> confirm.

**33\. Reorder notes manually**

**Actions:** Set the sort order to manual/custom \-\> long-press a note \-\> drag it to the required position \-\> release.

**34\. Switch the note list between list and grid layout**

**Actions:** Tap the overflow menu in the note list \-\> tap the layout/"Expanded view" toggle to switch between the compact list and the expanded card layout.

**35\. View note details and statistics**

**Actions:** Open a note \-\> tap the overflow menu \-\> tap "Note info"/"Details" \-\> read the creation date, last modification date, word and character counts and the attachment count. The global statistics screen is reachable from Settings.

**36\. Add the Omni Notes home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Omni Notes \-\> drag the widget onto the home screen \-\> select the category or filter it should display \-\> confirm.

**37\. Export a full backup**

**Actions:** Open Settings \-\> tap "Data" \-\> tap "Export data"/Backup \-\> enter or confirm the backup name \-\> choose whether to include settings \-\> tap OK.

**38\. Import data from a backup**

**Actions:** Open Settings \-\> tap "Data" \-\> tap "Import data" \-\> select the backup from the list \-\> confirm; the notes, attachments and (optionally) the settings are restored.

**39\. Schedule automatic backups**

**Actions:** Open Settings \-\> tap "Data" \-\> enable the automatic backup option \-\> choose the interval \-\> confirm.

**40\. Delete an existing backup**

**Actions:** Open Settings \-\> tap "Data" \-\> tap the import/backup list \-\> long-press the backup entry \-\> tap Delete \-\> confirm.

**41\. Change the interface language**

**Actions:** Open Settings \-\> tap "Interface" \-\> tap "Language" \-\> select the language from the list.

**42\. Change the app colours and theme**

**Actions:** Open Settings \-\> tap "Interface" \-\> set the navigation drawer colour, the note-list colour behaviour and the dark/light theme options.

**43\. Change the text size in the note list**

**Actions:** Open Settings \-\> tap "Interface" \-\> tap the text size entry \-\> choose the size.

**44\. Configure the swipe gesture action**

**Actions:** Open Settings \-\> tap "Behaviour"/Navigation \-\> choose what a swipe on a note does (archive or delete) \-\> confirm.

**45\. Configure checklist behaviour**

**Actions:** Open Settings \-\> tap "Behaviour" \-\> set whether checked items move to the bottom, whether they are kept or removed on save, and whether unchecked items are shown first.

**46\. Configure notification behaviour for reminders**

**Actions:** Open Settings \-\> tap "Notifications" \-\> set the notification sound, vibration, LED and snooze delay \-\> confirm.

**47\. Set the password and recovery question**

**Actions:** Open Settings \-\> tap "Security" \-\> tap "Password" \-\> enter the new password twice \-\> enter the recovery question and answer \-\> tap Confirm.

**48\. View the app version, changelog and licences**

**Actions:** Open Settings \-\> scroll to the "About"/Info section \-\> tap it to read the version, the changelog, the privacy policy and the open-source licences.

 

### **App Name: Joplin**

*Package: net.cozic.joplin  |  Version documented: 3.6.21  |  Reference: Official Joplin documentation (joplinapp.org) and in-app menus*

**Features:**

**1\. Create a notebook**

**Actions:** Open the sidebar (hamburger icon) \-\> tap "New notebook" / the "+" beside Notebooks \-\> enter the notebook title \-\> tap OK.

**2\. Create a nested sub-notebook**

**Actions:** Open the sidebar \-\> long-press the parent notebook \-\> tap "Edit"/move option and set the parent, or create a new notebook and then long-press it \-\> tap "Move" \-\> select the parent notebook \-\> confirm.

**3\. Rename or delete a notebook**

**Actions:** Open the sidebar \-\> long-press the notebook \-\> tap "Edit" to rename it and tap Save, or tap "Delete" and confirm.

**4\. Create a note**

**Actions:** Open the target notebook \-\> tap the "+" floating action button \-\> tap "New note" \-\> enter the title \-\> type the body \-\> tap the back arrow or the tick to save.

**5\. Create a to-do**

**Actions:** Open a notebook \-\> tap the "+" button \-\> tap "New to-do" \-\> enter the title and body \-\> tap back to save; the item appears with a checkbox in the note list.

**6\. Mark a to-do as completed**

**Actions:** Open the note list \-\> tap the checkbox beside the to-do; completed to-dos are struck through and can be hidden through the sort/filter options.

**7\. Convert a note to a to-do and back**

**Actions:** Open the note \-\> tap the overflow menu (three dots) \-\> tap "Convert to to-do" (or "Convert to note") \-\> confirm.

**8\. Set an alarm on a to-do**

**Actions:** Open a to-do \-\> tap the overflow menu \-\> tap "Set alarm" \-\> pick the date and time \-\> tap Save; a notification fires at that time.

**9\. Write in Markdown with live syntax highlighting**

**Actions:** Open a note in the Markdown editor \-\> type Markdown syntax (headings, lists, links, code fences, tables) \-\> the editor highlights the syntax as you type.

**10\. Use the Markdown formatting toolbar**

**Actions:** Open a note in the editor \-\> use the toolbar above the keyboard to insert bold, italic, headings, lists, checkboxes, links, code and horizontal rules at the cursor.

**11\. Switch between the Markdown editor and the rich text (WYSIWYG) editor**

**Actions:** Open a note \-\> tap the editor toggle icon in the toolbar (or set the default in Settings \-\> Note) \-\> the note reopens in the other editing mode.

**12\. Switch between edit mode and the rendered viewer**

**Actions:** Open a note \-\> tap the eye/edit toggle in the toolbar \-\> the rendered Markdown is displayed \-\> tap the pencil to go back to editing.

**13\. Attach a photo taken with the camera**

**Actions:** Open a note in edit mode \-\> tap the attach (paper clip) icon \-\> tap "Take photo" \-\> grant the camera permission \-\> capture the image \-\> confirm; the image is embedded as a resource.

**14\. Attach an image or file from the device**

**Actions:** Open a note \-\> tap the attach icon \-\> tap "Attach file"/"Attach photo" \-\> select the item from the picker \-\> confirm.

**15\. Record and attach audio**

**Actions:** Open a note \-\> tap the attach icon \-\> choose the audio recorder option \-\> grant the microphone permission \-\> record \-\> stop \-\> the audio resource is embedded.

**16\. Use voice typing to dictate note text**

**Actions:** Open a note in edit mode \-\> tap the voice typing (microphone) icon in the toolbar \-\> download the language model if prompted \-\> speak \-\> tap stop; the transcription is inserted at the cursor.

**17\. Attach the current geolocation to a note**

**Actions:** Enable the geolocation option in Settings \-\> Note \-\> create or open a note \-\> tap the overflow menu \-\> tap "Attach geolocation"/"Show note location" as available \-\> grant the location permission.

**18\. Add tags to a note**

**Actions:** Open a note \-\> tap the overflow menu \-\> tap "Tags" \-\> type a new tag or select existing tags \-\> tap OK.

**19\. Browse notes by tag**

**Actions:** Open the sidebar \-\> tap "Tags" \-\> tap the tag name \-\> the note list shows all notes carrying that tag.

**20\. Search notes**

**Actions:** Tap the search icon in the toolbar \-\> type the query (supports Joplin search syntax such as tag:, notebook:, title: and created:) \-\> tap a result to open it.

**21\. Sort the note list**

**Actions:** Open a notebook \-\> tap the overflow menu (three dots) \-\> tap the sort option \-\> choose the field (updated date, created date, title or custom order) and the direction.

**22\. Reorder notes manually**

**Actions:** Set the sort order to custom \-\> long-press a note in the list \-\> drag it to the required position \-\> release.

**23\. Move a note to another notebook**

**Actions:** Open the note \-\> tap the overflow menu \-\> tap "Move" / the notebook selector \-\> choose the destination notebook \-\> confirm.

**24\. Duplicate a note**

**Actions:** Open the note list \-\> long-press the note \-\> tap "Duplicate" from the contextual menu.

**25\. Delete a note**

**Actions:** Open the note (or long-press it in the list) \-\> tap the delete/bin action \-\> confirm; the note moves to the trash.

**26\. Restore notes from the trash**

**Actions:** Open the sidebar \-\> tap "Trash" \-\> long-press the deleted note \-\> tap Restore, or tap the permanent delete action to purge it.

**27\. Configure synchronisation with a remote target**

**Actions:** Open the sidebar \-\> tap "Configuration"/Settings \-\> tap "Synchronisation" \-\> choose the sync target (Joplin Cloud, Joplin Server, Dropbox, OneDrive, Nextcloud/WebDAV, AWS S3 or the local file system) \-\> enter the credentials or complete the OAuth login \-\> tap "Check synchronisation configuration" \-\> save.

**28\. Run a synchronisation manually**

**Actions:** Open the sidebar \-\> tap "Synchronise" \-\> the sync progress is shown in the sidebar \-\> wait for completion.

**29\. Set the automatic synchronisation interval**

**Actions:** Open Configuration \-\> Synchronisation \-\> tap the "Synchronisation interval" entry \-\> select the interval (or disable it) \-\> also set whether syncing over mobile data is allowed.

**30\. Enable end-to-end encryption**

**Actions:** Open Configuration \-\> tap "Encryption" \-\> toggle end-to-end encryption on \-\> set the master password \-\> confirm; run a sync so the encrypted data is uploaded.

**31\. Enter a master key password to decrypt synced notes**

**Actions:** Open Configuration \-\> Encryption \-\> find the listed master key \-\> tap it \-\> enter the password \-\> tap Save; decryption starts automatically.

**32\. Publish/share a note (Joplin Cloud account required)**

**Actions:** Log in to Joplin Cloud in the synchronisation settings \-\> open the note \-\> tap the overflow menu \-\> tap the share/publish option \-\> confirm \-\> copy the generated public link.

**33\. Lock the app with a PIN or biometrics**

**Actions:** Open Configuration \-\> tap "Application"/security section \-\> enable the app lock \-\> set the PIN \-\> optionally enable fingerprint/biometric unlock \-\> confirm.

**34\. Change the application theme**

**Actions:** Open Configuration \-\> tap "Appearance" \-\> select the theme (light, dark, dracula, solarized, Nord, aritim dark and so on) \-\> optionally enable the automatic light/dark switch.

**35\. Change the editor and viewer font size**

**Actions:** Open Configuration \-\> Appearance \-\> set the editor font size and the note viewer font size \-\> return.

**36\. Enable Markdown rendering plugins**

**Actions:** Open Configuration \-\> tap "Markdown"/"Note" \-\> toggle the individual renderer plugins (for example KaTeX maths, Mermaid diagrams, footnotes, tables, task lists, abbreviations, sub/superscript, mark and typographer).

**37\. Install and manage Joplin plugins**

**Actions:** Open Configuration \-\> tap "Plugins" \-\> browse or search the plugin repository \-\> tap Install on a plugin \-\> restart the app if prompted \-\> use the toggle to enable or disable an installed plugin.

**38\. Configure note behaviour defaults**

**Actions:** Open Configuration \-\> tap "Note" \-\> set options such as the default editor, sort order, whether completed to-dos are shown, whether note counts are displayed and whether new notes get the geolocation.

**39\. Export a JEX/RAW backup or share note data**

**Actions:** Open Configuration \-\> tap "Tools"/Export \-\> choose the export format (for example JEX archive) \-\> pick the destination \-\> confirm.

**40\. Import notes from a file**

**Actions:** Open Configuration \-\> Tools \-\> tap the import option \-\> select the JEX or Markdown file \-\> confirm.

**41\. Send a note to another app**

**Actions:** Open a note \-\> tap the overflow menu \-\> tap "Share"/"Export" \-\> choose the target app in the Android share sheet.

**42\. Create a note from another app via the share sheet**

**Actions:** In any app, tap Share on the text, link or image \-\> choose Joplin \-\> select the destination notebook if prompted \-\> confirm; a new note is created.

**43\. View note properties**

**Actions:** Open a note \-\> tap the overflow menu \-\> tap "Properties"/"Note info" \-\> read the created and updated times, the source URL, the location and the internal ID.

**44\. View the synchronisation status and log**

**Actions:** Open Configuration \-\> tap "Synchronisation status" to see counts of items and encryption state, or open Tools \-\> "Log" to read the diagnostic log.

**45\. Check for application updates**

**Actions:** Open Configuration \-\> tap "About"/"Check for updates" \-\> follow the prompt if a newer version is available (available on non-store builds).

 

### **App Name: NoNonsense Notes**

*Package: com.nononsenseapps.notepad  |  Version documented: 7.2.6  |  Reference: Official NoNonsense Notes repository documentation and F-Droid listing*

**Features:**

**1\. Create a task list**

**Actions:** Open the navigation drawer (hamburger icon or left-edge swipe) \-\> tap "Create new list"/the "+" beside the lists \-\> enter the list name \-\> tap OK.

**2\. Rename a task list**

**Actions:** Open the list \-\> tap the overflow menu (three dots) \-\> tap "Rename list"/"Edit list" \-\> change the name \-\> tap OK.

**3\. Delete a task list**

**Actions:** Open the list \-\> tap the overflow menu \-\> tap "Delete list" \-\> confirm; the tasks in that list are removed with it.

**4\. Set the default list**

**Actions:** Open Settings \-\> tap the default list entry \-\> select the list that new tasks and the widget should use by default.

**5\. Create a task**

**Actions:** Open the target list \-\> tap the "+" floating action button \-\> enter the task title \-\> enter the optional note text \-\> tap the back arrow or the save/tick to store it.

**6\. Edit a task**

**Actions:** Open the list \-\> tap the task \-\> change the title, note, due date or reminders \-\> tap back/save.

**7\. Mark a task as completed**

**Actions:** Open the list \-\> tap the checkbox beside the task; the task is struck through and, depending on the settings, hidden from the active list.

**8\. Show or hide completed tasks**

**Actions:** Open the list \-\> tap the overflow menu \-\> toggle the "Show completed"/"Hide completed" option.

**9\. Delete all completed tasks in a list**

**Actions:** Open the list \-\> tap the overflow menu \-\> tap "Delete completed tasks" \-\> confirm.

**10\. Create sub-tasks by indenting**

**Actions:** Open a list in manual/tree sort order \-\> long-press the task \-\> drag it to the right (or use the indent control) to nest it under the task above \-\> release.

**11\. Reorder tasks manually**

**Actions:** Set the list sort order to manual \-\> long-press a task \-\> drag it up or down to the required position \-\> release.

**12\. Set a due date on a task**

**Actions:** Open the task \-\> tap the due-date field \-\> select the date in the picker \-\> tap OK.

**13\. Set a time-based reminder**

**Actions:** Open the task \-\> tap the "Add reminder" control \-\> pick the date and time \-\> tap OK; a notification fires at that moment.

**14\. Set a repeating reminder**

**Actions:** Open the task \-\> add a reminder \-\> tap the repeat control on the reminder row \-\> choose the repetition (for example daily, weekly, monthly, yearly) \-\> confirm.

**15\. Set a location-based reminder**

**Actions:** Open the task \-\> tap "Add reminder" \-\> switch to the location option \-\> grant the location permission \-\> search for or pick the place on the map \-\> confirm; the reminder fires when you arrive at that location.

**16\. Remove a reminder**

**Actions:** Open the task \-\> tap the delete (X or bin) icon on the reminder row \-\> the reminder is removed.

**17\. Move a task to a different list**

**Actions:** Open the task \-\> tap the overflow menu \-\> tap "Move to list"/change the list selector \-\> choose the target list \-\> confirm.

**18\. Delete a task**

**Actions:** Open the task \-\> tap the delete (bin) icon, or swipe the task in the list according to the configured swipe action \-\> confirm.

**19\. Sort a list**

**Actions:** Open the list \-\> tap the overflow menu \-\> tap "Sort" \-\> choose the order (manual/tree, due date, alphabetical or possible/creation order).

**20\. Switch between lists by swiping**

**Actions:** Open any list \-\> swipe horizontally left or right to move to the neighbouring list (when the swipe-between-lists option is enabled in Settings).

**21\. View all tasks from all lists together**

**Actions:** Open the navigation drawer \-\> tap the "All lists"/combined view entry \-\> the tasks from every list are shown in one screen.

**22\. Search tasks**

**Actions:** Open a list \-\> tap the search icon in the toolbar \-\> type the search text \-\> tap a matching task to open it.

**23\. Share a task**

**Actions:** Open the task \-\> tap the share icon (or the overflow menu \-\> Share) \-\> choose the destination app in the Android share sheet.

**24\. Create a task from text shared by another app**

**Actions:** In another app select text \-\> tap Share \-\> choose NoNonsense Notes \-\> pick the target list \-\> tap save.

**25\. Add the task list home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find NoNonsense Notes \-\> drag the widget onto the home screen \-\> choose the list, theme and transparency in the widget configuration \-\> tap OK.

**26\. Configure widget appearance**

**Actions:** Long-press the placed widget (or open its configuration) \-\> set the list to display, the header visibility, the background transparency and the text colour \-\> confirm.

**27\. Change the app theme**

**Actions:** Open Settings \-\> tap the theme entry \-\> choose light, dark, black or the classic theme.

**28\. Change the list and font sizes**

**Actions:** Open Settings \-\> open the appearance section \-\> set the item text size and the number of note lines shown per row.

**29\. Enable synchronisation with a storage folder (SD card sync)**

**Actions:** Open Settings \-\> tap the synchronisation section \-\> enable the file/SD card sync \-\> choose the folder that holds the plain-text task files \-\> confirm.

**30\. Configure notification behaviour**

**Actions:** Open Settings \-\> tap the notification section \-\> set the notification sound, vibration and whether persistent notifications are used for reminders.

**31\. Back up the task database**

**Actions:** Open Settings \-\> tap the backup entry \-\> tap the export/backup action \-\> choose the destination \-\> confirm.

**32\. Restore the task database from a backup**

**Actions:** Open Settings \-\> tap the backup entry \-\> tap Restore/Import \-\> select the backup file \-\> confirm.

**33\. Configure the swipe gesture on list items**

**Actions:** Open Settings \-\> open the behaviour section \-\> choose what a horizontal swipe does to a task (for example complete or delete).

**34\. View the about screen and licences**

**Actions:** Open Settings (or the drawer) \-\> tap "About" \-\> read the version number, the credits and the open-source licences.

 

## **Category: Tasks, study and habits**

### **App Name: AnkiDroid**

*Package: com.ichi2.anki  |  Version documented: 2.24.0  |  Reference: Official AnkiDroid manual and in-app menus*

**Features:**

**1\. Create a deck**

**Actions:** Open the deck list \-\> tap the "+" floating action button \-\> tap "Create deck" \-\> enter the deck name \-\> tap OK.

**2\. Create a subdeck**

**Actions:** Tap the "+" button \-\> tap "Create deck" \-\> enter the name using the "Parent::Child" notation (for example "Spanish::Verbs") \-\> tap OK; the deck is nested under the parent.

**3\. Rename a deck**

**Actions:** Open the deck list \-\> long-press the deck (or tap the gear icon on the deck row) \-\> tap "Rename" \-\> enter the new name \-\> tap OK.

**4\. Delete a deck**

**Actions:** Open the deck list \-\> long-press the deck (or tap the gear icon) \-\> tap "Delete" \-\> confirm; the deck and its cards are removed.

**5\. Reorder or re-parent decks**

**Actions:** Open the deck list \-\> long-press a deck \-\> tap "Rename" \-\> change the "::" prefix to move it under a different parent \-\> tap OK.

**6\. Study a deck**

**Actions:** Open the deck list \-\> tap the deck name \-\> tap "Study Now" \-\> read the question \-\> tap "Show Answer" \-\> tap one of the answer buttons (Again, Hard, Good, Easy) to grade the card.

**7\. Add a note (create cards)**

**Actions:** Tap the "+" button \-\> tap "Add" \-\> choose the note type \-\> choose the target deck \-\> fill in the fields (for example Front and Back) \-\> add tags if wanted \-\> tap the save/tick button.

**8\. Create a cloze deletion card**

**Actions:** Tap "+" \-\> Add \-\> set the note type to Cloze \-\> type the sentence in the Text field \-\> select the word to hide \-\> tap the cloze (\[...\]) button in the field toolbar \-\> tap Save.

**9\. Attach an image, audio clip or recording to a field**

**Actions:** Open the Add/Edit note screen \-\> tap the paper-clip/multimedia icon beside a field \-\> choose Image, Audio or Record \-\> pick or capture the media \-\> confirm; the media reference is inserted into the field.

**10\. Create an image occlusion note**

**Actions:** Tap "+" \-\> Add \-\> select the Image Occlusion note type \-\> choose the image \-\> draw the masks over the areas to hide \-\> add optional header and comment text \-\> tap Save.

**11\. Add tags to a note**

**Actions:** Open the Add or Edit note screen \-\> tap the Tags row \-\> select existing tags or type a new tag \-\> tap OK \-\> save the note.

**12\. Edit an existing card or note**

**Actions:** While reviewing, tap the edit (pencil) icon; or open the Card Browser and tap the card \-\> change the field contents \-\> tap Save.

**13\. Preview a card**

**Actions:** Open the Card Browser \-\> long-press or select the card \-\> tap the Preview action \-\> step through the question and answer sides with the navigation arrows.

**14\. Browse and search cards**

**Actions:** Open the navigation drawer \-\> tap "Card Browser" \-\> tap the search field \-\> type an Anki search query (for example "deck:Spanish tag:verb is:due") \-\> review the matching cards.

**15\. Filter the Card Browser by deck, note type, flag or tag**

**Actions:** Open the Card Browser \-\> tap the filter/sidebar icon \-\> select a deck, note type, tag, flag or saved search from the sidebar \-\> the list updates.

**16\. Save a search in the Card Browser**

**Actions:** Open the Card Browser \-\> type the search query \-\> tap the overflow menu (three dots) \-\> tap "Save current search" \-\> enter a name \-\> tap OK.

**17\. Flag cards with colours**

**Actions:** Open the Card Browser and select cards (or tap the flag icon during review) \-\> tap the flag action \-\> choose the flag colour (for example red, orange, green, blue, pink, turquoise, purple) \-\> confirm.

**18\. Suspend or unsuspend cards**

**Actions:** Open the Card Browser \-\> long-press to select the cards \-\> tap the overflow menu \-\> tap "Toggle Suspend"; suspended cards are shown greyed out and are skipped during study.

**19\. Bury a card or note**

**Actions:** During review tap the overflow menu \-\> tap "Bury card" or "Bury note"; the item is postponed to the next day.

**20\. Reposition new cards**

**Actions:** Open the Card Browser \-\> select the new cards \-\> tap the overflow menu \-\> tap "Reposition" \-\> enter the start position and step \-\> tap OK.

**21\. Set a card's due date**

**Actions:** Open the Card Browser \-\> select the cards \-\> tap the overflow menu \-\> tap "Set due date" \-\> enter the number of days or a range \-\> choose whether to change the interval \-\> tap OK.

**22\. Reset/forget cards**

**Actions:** Open the Card Browser \-\> select the cards \-\> tap the overflow menu \-\> tap "Reset"/"Forget" \-\> choose whether to restore the original position \-\> confirm.

**23\. Change the deck of selected cards**

**Actions:** Open the Card Browser \-\> select the cards \-\> tap the overflow menu \-\> tap "Change deck" \-\> choose the target deck \-\> confirm.

**24\. Change the note type of selected notes**

**Actions:** Open the Card Browser \-\> select the notes \-\> tap the overflow menu \-\> tap "Change note type" \-\> map the old fields and templates to the new ones \-\> confirm.

**25\. Delete cards or notes**

**Actions:** Open the Card Browser \-\> select the items \-\> tap the delete (bin) icon \-\> confirm.

**26\. Undo the last action**

**Actions:** Tap the undo arrow in the toolbar (available on the reviewer, the Card Browser and the deck list) \-\> the previous action is reverted.

**27\. Configure deck options (scheduling)**

**Actions:** Open the deck list \-\> tap the gear icon on the deck row \-\> tap "Options" \-\> set the new cards/day limit, the maximum reviews/day, the learning steps, the graduating and easy intervals, the lapse steps, the leech threshold and action, the burying options and the display order \-\> tap Save.

**28\. Enable and configure FSRS scheduling**

**Actions:** Open deck options \-\> open the FSRS section \-\> toggle FSRS on \-\> set the desired retention \-\> optionally tap "Optimize" to compute parameters from your review history \-\> tap Save.

**29\. Create a filtered/custom study deck**

**Actions:** Open the deck list \-\> tap the deck \-\> tap "Custom Study" (or use the "+" button \-\> "Create filtered deck") \-\> choose the option (for example increase today's new card limit, review forgotten cards, study by card state or tag) \-\> set the search, limit and order \-\> tap Build.

**30\. Rebuild or empty a filtered deck**

**Actions:** Open the filtered deck \-\> tap "Rebuild" to refill it with matching cards, or tap "Empty" to return the cards to their home decks.

**31\. View study statistics**

**Actions:** Open the navigation drawer \-\> tap "Statistics" \-\> select the scope (deck or collection) and the period (for example 1 month, 1 year, all history) \-\> scroll the graphs (Future Due, Calendar, Reviews, Card Counts, Card Ease/Difficulty, Hourly Breakdown, Answer Buttons, True Retention).

**32\. Synchronise with AnkiWeb**

**Actions:** Open the navigation drawer \-\> tap the sync icon in the toolbar \-\> enter the AnkiWeb email address and password on first use \-\> tap Log in \-\> the collection syncs; tap sync again later to sync manually.

**33\. Synchronise media**

**Actions:** Ensure the AnkiWeb account is configured \-\> run a sync \-\> media files are uploaded and downloaded as part of the sync; check progress in the sync notification.

**34\. Enable automatic synchronisation**

**Actions:** Open Settings \-\> tap "Sync" \-\> toggle "Automatic synchronisation" on \-\> optionally restrict syncing to unmetered networks \-\> return.

**35\. Download shared decks**

**Actions:** Open the deck list \-\> tap the "+" button \-\> tap "Get shared decks" \-\> browse or search the AnkiWeb shared deck site in the opened view \-\> download the .apkg \-\> confirm the import.

**36\. Import an .apkg or .colpkg file**

**Actions:** Open the navigation drawer \-\> tap "Import"/use the "+" button \-\> select the .apkg or .colpkg file from the picker \-\> review the import summary \-\> tap Import.

**37\. Import notes from a CSV/text file**

**Actions:** Open the import screen \-\> select the .csv or .txt file \-\> map the columns to the note-type fields \-\> choose the target deck, the field separator and the duplicate handling \-\> tap Import.

**38\. Export a deck or the whole collection**

**Actions:** Open the deck list \-\> tap the gear icon on a deck \-\> tap "Export"; or open the drawer \-\> Export collection \-\> choose whether to include scheduling data and media \-\> tap OK \-\> pick the destination.

**39\. Create and manage note types**

**Actions:** Open Settings \-\> tap "Manage note types" \-\> tap "+" to add a note type (clone or standard) \-\> tap an existing type to rename it, edit its fields or edit its card templates \-\> tap Save.

**40\. Edit card templates and styling**

**Actions:** Open "Manage note types" \-\> tap the note type \-\> tap "Cards" \-\> edit the front template, the back template and the shared styling CSS \-\> tap the preview to check the result \-\> tap Save.

**41\. Add or reorder note type fields**

**Actions:** Open "Manage note types" \-\> tap the note type \-\> tap "Fields" \-\> tap "+" to add a field, drag to reorder, or tap a field to rename it and set its font, size, sort order and RTL flag \-\> tap Save.

**42\. Use the whiteboard during review**

**Actions:** Start reviewing \-\> tap the overflow menu \-\> tap "Enable whiteboard" \-\> draw the answer with a finger or stylus \-\> use the undo, eraser, colour and clear controls \-\> tap the toggle again to hide it.

**43\. Play card audio and use text to speech**

**Actions:** During review, tap the replay-audio control to hear the attached audio; to have fields read aloud, open deck options or Settings \-\> enable the text-to-speech/read-aloud option and select the voice and speed.

**44\. Configure review gestures and controls**

**Actions:** Open Settings \-\> tap "Controls"/"Gestures" \-\> enable gestures \-\> assign an action (for example Show Answer, Answer Good, Undo, Bury, Edit) to each tap zone, swipe direction and hardware key \-\> return.

**45\. Configure reviewer appearance**

**Actions:** Open Settings \-\> tap "Reviewing"/"Appearance" \-\> set the card font size and default font, the answer button placement, whether the timer and remaining counts are shown, and whether the screen stays on \-\> return.

**46\. Enable full screen review mode**

**Actions:** Open Settings \-\> Appearance/Reviewing \-\> tap the "Fullscreen mode" entry \-\> choose the level (for example hide the status bar, hide the status bar and navigation bar) \-\> return.

**47\. Switch the app theme (including night mode)**

**Actions:** Open Settings \-\> tap "Appearance" \-\> tap the theme entry \-\> choose the day theme, the night theme, and whether to follow the system setting \-\> return.

**48\. Set a deck study reminder notification**

**Actions:** Open the deck list \-\> tap the gear icon on the deck \-\> tap "Set reminder"/"Custom study reminder" \-\> pick the time \-\> confirm. General notification behaviour is set in Settings \-\> Notifications.

**49\. Configure the minimum card count for notifications**

**Actions:** Open Settings \-\> tap "Notifications" \-\> set the minimum number of due cards that triggers a notification and the vibration/blink options \-\> return.

**50\. Change the AnkiDroid collection folder**

**Actions:** Open Settings \-\> tap "Advanced" \-\> tap "AnkiDroid directory" \-\> select the new storage path \-\> confirm and restart the app when prompted.

**51\. Create a backup of the collection**

**Actions:** Open Settings \-\> Advanced/Backups \-\> set the number of automatic backups to keep, or trigger a manual backup from the deck list overflow menu \-\> confirm.

**52\. Restore the collection from a backup**

**Actions:** Open Settings \-\> Advanced \-\> tap "Backups"/"Restore from backup" \-\> select the backup file by date \-\> confirm; the current collection is replaced.

**53\. Check the database for errors**

**Actions:** Open the navigation drawer \-\> tap the overflow menu \-\> tap "Check database" \-\> wait for the check \-\> review the reported result.

**54\. Check for unused or missing media**

**Actions:** Open the drawer overflow menu \-\> tap "Check media" \-\> review the list of missing and unused files \-\> tap the delete action to remove the unused files if wanted.

**55\. Delete empty cards**

**Actions:** Open the drawer overflow menu \-\> tap "Empty cards" \-\> review the report \-\> confirm the deletion.

**56\. Add the AnkiDroid home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find AnkiDroid \-\> drag the deck-picker or card-count widget onto the home screen \-\> select the decks to display if prompted.

**57\. Enable the AnkiDroid API for third-party apps**

**Actions:** Open Settings \-\> tap "Advanced" \-\> enable the API/third-party app access option \-\> grant the permission when another app requests it.

**58\. Change the interface language**

**Actions:** Open Settings \-\> tap "General" \-\> tap "Language" \-\> select the language \-\> restart the app if prompted.

**59\. View help, the manual and the about screen**

**Actions:** Open the navigation drawer \-\> tap "Help"/"About" \-\> open the linked manual, the support page or the version and licence information.

 

### **App Name: Tasks.org**

*Package: org.tasks  |  Version documented: 15.9.1  |  Reference: Official Tasks.org documentation and in-app menus*

**Features:**

**1\. Create a task**

**Actions:** Open a list \-\> tap the "+" floating action button \-\> enter the task title \-\> tap Save (the tick) or press back to save.

**2\. Add a description to a task**

**Actions:** Open a task \-\> tap the description/notes field \-\> type the text \-\> tap Save.

**3\. Set a due date and time**

**Actions:** Open a task \-\> tap the due date row \-\> pick the date in the calendar \-\> pick the time (or choose a quick option such as Today, Tomorrow, Next week) \-\> tap OK \-\> tap Save.

**4\. Set a start ("hide until") date**

**Actions:** Open a task \-\> tap the "Hide until"/start date row \-\> choose the option (for example due date, day before due, week before due, or a specific date) \-\> tap OK \-\> Save.

**5\. Set a task priority**

**Actions:** Open a task \-\> tap the priority selector \-\> choose High, Medium, Low or None \-\> tap Save; the priority colour appears on the checkbox in the list.

**6\. Add reminders to a task**

**Actions:** Open a task \-\> tap the reminders row \-\> tap "Add reminder" \-\> choose "At due time", "When overdue", "Randomly" or a custom offset before or after the due time \-\> tap OK \-\> Save.

**7\. Set a repeating task**

**Actions:** Open a task \-\> tap the repeat row \-\> choose the frequency (daily, weekly, monthly, yearly or custom) \-\> set the interval, the weekdays and the end condition \-\> choose whether repetition counts from the due date or the completion date \-\> tap OK \-\> Save.

**8\. Create subtasks**

**Actions:** Open a task \-\> tap the subtasks row \-\> tap "Add subtask" \-\> enter the subtask title \-\> repeat for more \-\> tap Save; subtasks appear indented under the parent in the list.

**9\. Add tags to a task**

**Actions:** Open a task \-\> tap the tags row \-\> select existing tags or type a new tag name and confirm \-\> tap OK \-\> Save.

**10\. Attach a place/location to a task**

**Actions:** Open a task \-\> tap the location row \-\> search for the address or pick the point on the map \-\> set the arrival/departure notification and the geofence radius \-\> tap Save; the reminder fires on arrival or departure.

**11\. Attach files or pictures to a task**

**Actions:** Open a task \-\> tap the attachments row \-\> tap "Add attachment" \-\> choose a file from storage or take a photo \-\> confirm \-\> Save.

**12\. Complete a task**

**Actions:** Open the list \-\> tap the checkbox beside the task; repeating tasks are automatically rescheduled to the next occurrence.

**13\. Create a local list**

**Actions:** Open the navigation drawer \-\> tap the "+" beside "My lists"/local lists \-\> enter the list name \-\> pick a colour and an icon \-\> tap Save.

**14\. Rename, recolour or delete a list**

**Actions:** Open the drawer \-\> tap the settings/gear icon beside the list (or long-press the list) \-\> change the name, colour or icon and tap Save, or tap the delete action and confirm.

**15\. Move a task to another list**

**Actions:** Open the task \-\> tap the list selector at the top of the task editor \-\> choose the target list \-\> tap Save.

**16\. Use the built-in filters**

**Actions:** Open the navigation drawer \-\> tap one of the built-in filters (for example My Tasks, Today, Recently Modified, Snoozed) \-\> the filtered task list is displayed.

**17\. Create a custom filter**

**Actions:** Open the drawer \-\> tap the "+" beside Filters \-\> enter the filter name \-\> tap "Add criteria" \-\> pick the criteria (for example list, tag, due date, priority, hidden state) \-\> combine them with AND/OR/NOT \-\> tap Save.

**18\. Sort a task list**

**Actions:** Open a list \-\> tap the overflow menu (three dots) \-\> tap "Sort" \-\> choose the sort field (due date, alphabetical, importance, creation date, modification date, start date or manual) \-\> set ascending or descending \-\> confirm.

**19\. Group tasks in a list**

**Actions:** Open a list \-\> tap the overflow menu \-\> tap Sort \-\> choose the grouping option (for example by due date, by priority, by list) \-\> confirm; grouped headers appear in the list.

**20\. Reorder tasks by dragging**

**Actions:** Set the list sort order to manual/drag-and-drop \-\> long-press a task \-\> drag it to its new position (drag right to make it a subtask) \-\> release.

**21\. Show or hide completed and hidden tasks**

**Actions:** Open a list \-\> tap the overflow menu \-\> toggle "Show completed tasks" and "Show hidden tasks".

**22\. Search tasks**

**Actions:** Open the drawer or the toolbar \-\> tap the search icon \-\> type the query \-\> tap a matching task to open it.

**23\. Select and edit multiple tasks at once**

**Actions:** Long-press a task in the list \-\> tap further tasks to add them to the selection \-\> use the contextual toolbar to complete, move, delete or reschedule them in bulk.

**24\. Snooze a reminder**

**Actions:** When the notification appears, tap "Snooze" \-\> pick a preset delay or a custom date and time \-\> confirm.

**25\. Duplicate a task**

**Actions:** Open the task \-\> tap the overflow menu (three dots) \-\> tap "Make a copy"/Duplicate; a copy is created in the same list.

**26\. Delete a task**

**Actions:** Open the task \-\> tap the overflow menu \-\> tap Delete \-\> confirm.

**27\. Synchronise with a CalDAV server**

**Actions:** Open Settings \-\> tap "Synchronisation" \-\> tap "Add account" under CalDAV \-\> enter the server URL, the username and the password \-\> tap the tick to save; the remote task lists appear in the drawer.

**28\. Synchronise with Google Tasks**

**Actions:** Open Settings \-\> Synchronisation \-\> tap "Google Tasks" \-\> tap "Add account" \-\> choose the Google account and grant access \-\> the Google task lists appear in the drawer.

**29\. Synchronise with Microsoft To Do**

**Actions:** Open Settings \-\> Synchronisation \-\> tap Microsoft \-\> sign in with the Microsoft account and grant access \-\> the To Do lists appear in the drawer. (This connector is part of the paid/subscription tier.)

**30\. Synchronise with a Tasks.org account (EteSync/DAVx5 style accounts also supported)**

**Actions:** Open Settings \-\> Synchronisation \-\> tap the relevant provider \-\> enter the account details \-\> tap save; lists sync in the background at the configured interval.

**31\. Set the background sync interval and constraints**

**Actions:** Open Settings \-\> Synchronisation \-\> set the background sync interval \-\> toggle whether syncing is allowed on metered connections or while the battery is low.

**32\. Configure default task values**

**Actions:** Open Settings \-\> tap "Task defaults" \-\> set the default list, the default due time, the default reminders, the default priority and the default recurrence for new tasks.

**33\. Configure notification appearance and behaviour**

**Actions:** Open Settings \-\> tap "Notifications" \-\> set the ringtone, vibration, LED colour, persistent notifications, the "wear notifications" and the badge/count options.

**34\. Set quiet hours**

**Actions:** Open Settings \-\> Notifications \-\> enable "Quiet hours" \-\> set the start and end time; reminders are held back during that window.

**35\. Change the theme, accent colour and launcher icon**

**Actions:** Open Settings \-\> tap "Look and feel"/Appearance \-\> select the theme (light, dark, black, system) \-\> pick the accent and primary colours \-\> choose the launcher icon.

**36\. Change the date, time and language settings**

**Actions:** Open Settings \-\> Look and feel/Date and time \-\> set the language, the first day of the week, the 12/24-hour time display and the start-of-day time.

**37\. Add the task list home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Tasks.org \-\> drag the widget onto the home screen \-\> choose the list or filter, the theme, the opacity, the row height and which fields to show \-\> tap Save.

**38\. Reconfigure an existing widget**

**Actions:** Tap the settings/gear icon on the widget (or long-press the widget and open its settings) \-\> change the displayed filter and appearance options \-\> tap Save.

**39\. Show tasks alongside calendar events**

**Actions:** Open Settings \-\> tap the calendar integration section \-\> enable the calendar event display and select which calendars are shown in the task list.

**40\. Create a calendar event from a task**

**Actions:** Open the task \-\> tap the overflow menu \-\> tap "Create calendar event"/the calendar action \-\> confirm the calendar and time \-\> save.

**41\. Back up the task database**

**Actions:** Open Settings \-\> tap "Backup" \-\> tap "Create backup"/Export \-\> choose the destination folder \-\> confirm.

**42\. Restore from a backup**

**Actions:** Open Settings \-\> Backup \-\> tap "Import"/Restore \-\> select the backup file \-\> confirm; existing data is replaced or merged as described in the prompt.

**43\. Enable automatic backups**

**Actions:** Open Settings \-\> Backup \-\> toggle the automatic backup option \-\> choose the destination folder \-\> confirm.

**44\. Purge deleted tasks and unused tags**

**Actions:** Open Settings \-\> tap "Advanced" \-\> tap "Delete completed tasks"/"Purge deleted tasks"/"Remove unused tags" \-\> confirm the operation.

**45\. Create a task by voice with Google Assistant**

**Actions:** Say the assistant phrase for adding a task naming Tasks.org (for example "add a task in Tasks") \-\> speak the task title \-\> confirm; the task is created in the default list.

**46\. Create a task from text shared by another app**

**Actions:** In another app select text or a link \-\> tap Share \-\> choose Tasks.org \-\> edit the pre-filled title \-\> tap Save.

**47\. Subscribe to the paid tier**

**Actions:** Open Settings \-\> tap the subscription/"Support Tasks" entry \-\> choose the plan \-\> complete the purchase; the paid connectors and features are unlocked.

 

### **App Name: OpenTasks**

*Package: org.dmfs.tasks  |  Version documented: 1.4.2  |  Reference: Official OpenTasks repository documentation and F-Droid listing*

*Note: OpenTasks stores tasks in the Android task provider. Remote synchronisation is performed by a separate sync adapter such as DAVx5; OpenTasks itself does not contain sync accounts.*

**Features:**

**1\. Create a task**

**Actions:** Open the app \-\> tap the "+" floating action button \-\> choose the task list to create it in \-\> enter the title \-\> fill in the optional fields \-\> tap the save (tick) button.

**2\. Set the task title and description**

**Actions:** Open the task editor \-\> tap the title field and type the title \-\> tap the description field and type the details \-\> tap Save.

**3\. Set a due date and time**

**Actions:** Open the task editor \-\> tap the "Due" field \-\> pick the date in the calendar \-\> pick the time (or toggle the all-day option) \-\> tap OK \-\> Save.

**4\. Set a start date**

**Actions:** Open the task editor \-\> tap the "Start" field \-\> select the date and time \-\> tap OK \-\> Save.

**5\. Set the task priority**

**Actions:** Open the task editor \-\> tap the priority selector \-\> choose the level (for example high, medium, low or undefined) \-\> tap Save.

**6\. Set the classification/privacy level**

**Actions:** Open the task editor \-\> tap the classification/privacy field \-\> choose Public, Private or Confidential \-\> tap Save.

**7\. Set the task status**

**Actions:** Open the task editor \-\> tap the status field \-\> choose Needs action, In process, Completed or Cancelled \-\> tap Save.

**8\. Set the completion percentage**

**Actions:** Open the task editor \-\> drag the progress slider (or enter the percentage) \-\> tap Save; setting it to 100% marks the task completed.

**9\. Add a location to a task**

**Actions:** Open the task editor \-\> tap the location field \-\> type the location text \-\> tap Save; the value is stored with the task and can be opened in a map app from the detail view.

**10\. Add a URL to a task**

**Actions:** Open the task editor \-\> tap the URL field \-\> enter the web address \-\> tap Save; tapping it in the detail view opens the link.

**11\. Add a checklist to a task**

**Actions:** Open the task editor \-\> tap the checklist section \-\> tap "Add item" \-\> type the item text \-\> repeat for further items \-\> tap Save; tick the items from the task detail view.

**12\. Set an alarm/reminder**

**Actions:** Open the task editor \-\> tap the alarms/reminder section \-\> tap "Add alarm" \-\> choose the offset relative to the start or due date (or an absolute date and time) \-\> tap Save.

**13\. Create a recurring task**

**Actions:** Open the task editor \-\> tap the recurrence field \-\> choose the pattern (daily, weekly, monthly, yearly or a custom rule) \-\> set the interval and the end condition \-\> tap OK \-\> Save.

**14\. Complete a task**

**Actions:** Open the task list \-\> tap the checkbox/round completion control on the task row (or open the task and tap the complete action); the task moves to the completed group.

**15\. Edit an existing task**

**Actions:** Tap the task in the list to open the detail view \-\> tap the edit (pencil) icon \-\> change the fields \-\> tap Save.

**16\. Delete a task**

**Actions:** Open the task detail view \-\> tap the delete (bin) icon \-\> confirm.

**17\. Browse tasks grouped by due date**

**Actions:** Open the app \-\> select the "Due" tab \-\> the tasks are grouped into overdue, today, tomorrow, this week and later sections.

**18\. Browse tasks grouped by start date**

**Actions:** Open the app \-\> select the "Start" tab \-\> tasks are grouped by their start dates.

**19\. Browse tasks grouped by list**

**Actions:** Open the app \-\> select the "Lists" tab \-\> the tasks are grouped under their task list headers \-\> tap a header to collapse or expand it.

**20\. Browse tasks grouped by priority**

**Actions:** Open the app \-\> select the "Priority" tab \-\> the tasks are grouped by their priority values.

**21\. Browse tasks grouped by progress**

**Actions:** Open the app \-\> select the "Progress" tab \-\> the tasks are grouped by completion percentage bands.

**22\. Search for a task**

**Actions:** Tap the search icon in the toolbar \-\> type the search text \-\> review the matching tasks \-\> tap a result to open it.

**23\. Show or hide completed tasks**

**Actions:** Tap the overflow menu (three dots) in the task list \-\> toggle the "Show completed tasks" option.

**24\. Choose which task lists are visible**

**Actions:** Tap the overflow menu \-\> tap "Visible lists"/"Synchronised lists" \-\> tick the lists to display \-\> tap OK.

**25\. Create a local task list**

**Actions:** Open the overflow menu \-\> open the list management screen \-\> tap the add action \-\> enter the list name \-\> pick a colour \-\> tap Save. (Remote lists are created by the sync adapter.)

**26\. Change a task list's name or colour**

**Actions:** Open the list management screen \-\> tap the list \-\> change the name or colour \-\> tap Save.

**27\. Share a task**

**Actions:** Open the task detail view \-\> tap the share icon \-\> choose the destination app from the Android share sheet.

**28\. Add the OpenTasks home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find OpenTasks \-\> drag the widget onto the home screen \-\> configure the lists it shows \-\> confirm.

**29\. Open a task from the widget**

**Actions:** Tap a task row on the home screen widget \-\> the task detail view opens in the app; tap the "+" on the widget to create a new task.

**30\. Configure application settings**

**Actions:** Tap the overflow menu \-\> tap "Settings" \-\> adjust the available preferences (for example the theme/appearance, whether to open tasks in the detail view, and the visible lists) \-\> return.

**31\. View the about screen and licences**

**Actions:** Open the overflow menu \-\> tap "About" \-\> read the version number, the credits and the licence information.

 

### **App Name: Loop Habit Tracker**

*Package: org.isoron.uhabits  |  Version documented: 2.3.1  |  Reference: Official Loop Habit Tracker repository documentation and F-Droid listing*

**Features:**

**1\. Create a yes/no habit**

**Actions:** Open the app \-\> tap the "+" floating action button \-\> tap "Yes or No" \-\> enter the habit name \-\> enter the optional question \-\> pick a colour \-\> set the frequency \-\> tap Save.

**2\. Create a measurable habit**

**Actions:** Tap the "+" button \-\> tap "Measurable" \-\> enter the name and question \-\> enter the unit (for example km, pages, minutes) \-\> enter the daily target value \-\> choose the target type (at least / at most) \-\> pick a colour \-\> tap Save.

**3\. Set a habit frequency**

**Actions:** Open the habit editor \-\> tap the frequency row \-\> choose Every day, Every X days, X times per week, X times per month, or a custom ratio \-\> tap OK \-\> Save.

**4\. Set a habit reminder**

**Actions:** Open the habit editor \-\> tap the reminder row \-\> pick the time \-\> select the days of the week the reminder should fire \-\> tap OK \-\> Save.

**5\. Add notes to a habit**

**Actions:** Open the habit editor \-\> tap the notes field \-\> type the description \-\> tap Save.

**6\. Check off a habit for today**

**Actions:** Open the main habit list \-\> tap the checkmark square in today's column on the habit row; tap again to cycle the state (unchecked, checked, skipped depending on the settings).

**7\. Enter a value for a measurable habit**

**Actions:** Open the habit list \-\> tap today's cell on the measurable habit row \-\> type the value in the dialog \-\> tap Save.

**8\. Check off a habit for an earlier day**

**Actions:** Open the habit list \-\> scroll the date columns horizontally to the past date \-\> tap the cell for that date, or open the habit detail \-\> open the calendar/history view \-\> tap the day.

**9\. Mark a day as skipped**

**Actions:** Long-press (or repeatedly tap, depending on the settings) the day cell \-\> choose the skip state; skipped days do not break the streak.

**10\. Add a note to a specific day's entry**

**Actions:** Open the habit detail \-\> open the history/calendar view \-\> long-press the day \-\> enter the note text in the dialog \-\> tap Save.

**11\. View a habit's detailed statistics**

**Actions:** Open the habit list \-\> tap the habit name \-\> the detail screen opens showing the overview, the score chart, the history calendar, the streaks list and the frequency (best-time) chart.

**12\. View the score/strength chart**

**Actions:** Open the habit detail \-\> scroll to the Score card \-\> tap the interval control to switch between day, week, month, quarter and year granularity.

**13\. View the history calendar**

**Actions:** Open the habit detail \-\> scroll to the History card \-\> scroll horizontally to move through past months \-\> tap a day to toggle or edit it.

**14\. View the streaks chart**

**Actions:** Open the habit detail \-\> scroll to the Streaks card \-\> review the longest and most recent streaks with their date ranges.

**15\. View the frequency (weekday/time) chart**

**Actions:** Open the habit detail \-\> scroll to the Frequency card \-\> review which weekdays the habit is most often completed on.

**16\. Edit a habit**

**Actions:** Open the habit detail \-\> tap the edit (pencil) icon (or long-press the habit in the list and tap Edit) \-\> change the name, question, colour, unit, target, frequency or reminder \-\> tap Save.

**17\. Archive a habit**

**Actions:** Open the habit list \-\> long-press the habit \-\> tap the archive icon in the contextual toolbar; the habit is hidden from the main list but its data is kept.

**18\. Unarchive a habit**

**Actions:** Open the habit list \-\> tap the overflow menu (three dots) \-\> enable "Show archived" \-\> long-press the archived habit \-\> tap the unarchive action.

**19\. Delete a habit**

**Actions:** Open the habit list \-\> long-press the habit \-\> tap the delete (bin) icon \-\> confirm; the habit and all its records are removed.

**20\. Reorder habits manually**

**Actions:** Open the habit list \-\> tap the overflow menu \-\> set the sort order to manual \-\> long-press a habit \-\> drag it to the new position \-\> release.

**21\. Sort the habit list**

**Actions:** Open the habit list \-\> tap the overflow menu \-\> tap "Sort" \-\> choose the criterion (manual, by name, by colour, by score or by status) \-\> confirm.

**22\. Filter the habit list**

**Actions:** Open the habit list \-\> tap the overflow menu \-\> tap "Filter" \-\> toggle whether archived habits and completed habits are shown \-\> confirm.

**23\. Change the number of days shown in the list**

**Actions:** Rotate the device or resize the window; Loop adjusts the number of visible day columns. The display can also be adjusted from the appearance settings.

**24\. Snooze or dismiss a habit reminder**

**Actions:** When the reminder notification appears \-\> tap the check action to record the habit, or tap "Later"/snooze and choose the delay.

**25\. Enable persistent (sticky) reminder notifications**

**Actions:** Open Settings \-\> find the sticky/persistent notification option \-\> toggle it on so reminders remain in the notification shade until acted upon.

**26\. Add a habit widget to the home screen**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Loop Habit Tracker \-\> drag the required widget type (checkmark, history, score, streaks, frequency or target) onto the home screen \-\> select the habit it should show \-\> confirm.

**27\. Check off a habit directly from a widget**

**Actions:** Tap the checkmark area on the placed home screen widget; the habit is recorded for today without opening the app.

**28\. Export habit data as CSV**

**Actions:** Open Settings \-\> tap "Export as CSV" \-\> choose the destination \-\> confirm; a ZIP of CSV files with the habits and their check-marks is written.

**29\. Create a full database backup**

**Actions:** Open Settings \-\> tap "Export full backup" \-\> choose the destination folder \-\> confirm; a .db file containing the whole database is produced.

**30\. Restore a full backup**

**Actions:** Open Settings \-\> tap "Import data" \-\> select the previously exported .db backup file \-\> confirm; the existing data is replaced.

**31\. Import data from another habit app**

**Actions:** Open Settings \-\> tap "Import data" \-\> select the exported file from the supported app (for example Tickmate, HabitBull, Rewire or a Loop CSV/DB backup) \-\> confirm.

**32\. Repair the database**

**Actions:** Open Settings \-\> tap the "Repair database" entry \-\> confirm; the app rebuilds the cached scores and check-marks.

**33\. Change the app theme**

**Actions:** Open Settings \-\> tap the theme entry \-\> choose the light theme, the dark theme or the pure black (AMOLED) variant \-\> return.

**34\. Set the first day of the week**

**Actions:** Open Settings \-\> tap the "First day of the week" entry \-\> select the weekday \-\> return.

**35\. Set the hour the day starts (day offset)**

**Actions:** Open Settings \-\> tap the "New day starts at" entry \-\> select the hour \-\> return; entries recorded before that hour count towards the previous day.

**36\. Enable or disable the check-mark reverse order and skip days**

**Actions:** Open Settings \-\> toggle the options that control whether the newest day appears first and whether the skip state is available when tapping a cell.

**37\. Open the help and FAQ**

**Actions:** Open the navigation drawer or Settings \-\> tap "Help"/"FAQ" \-\> read the built-in help pages.

**38\. View the about screen**

**Actions:** Open Settings or the drawer \-\> tap "About" \-\> read the version number, the source link and the licence.

 

## **Category: Finance**

### **App Name: Money Manager Ex**

*Package: com.money.manager.ex  |  Version documented: 5.5.10  |  Reference: Official Money Manager Ex documentation and in-app menus*

**Features:**

**1\. Create a database**

**Actions:** Open the app \-\> tap the "+" icon on the database selection screen (or open the drawer \-\> Database \-\> Create) \-\> give a name for the database \-\> give a file path/storage location \-\> tap the Save button.

**2\. Open an existing database**

**Actions:** Open the drawer \-\> tap "Database"/"Open database" \-\> browse to the .mmb file \-\> tap it to open; the app reloads with that database.

**3\. Switch between recently used databases**

**Actions:** Open the drawer \-\> tap the database entry \-\> select a database from the recent list \-\> confirm.

**4\. Create an account**

**Actions:** Open the drawer \-\> tap "Accounts" \-\> tap the "+" button \-\> enter the account name \-\> select the account type (for example Checking, Savings, Credit Card, Cash, Investment, Loan) \-\> select the currency \-\> enter the initial balance \-\> optionally enter the account number, notes and holder \-\> tap Save.

**5\. Edit or close an account**

**Actions:** Open the Accounts list \-\> tap the account \-\> tap the edit action \-\> change the details, or set the status to Closed \-\> tap Save.

**6\. Delete an account**

**Actions:** Open the Accounts list \-\> long-press the account \-\> tap Delete \-\> confirm.

**7\. Record a withdrawal (expense)**

**Actions:** Open the account or the home screen \-\> tap the "+" button \-\> select the Withdrawal type \-\> enter the amount \-\> select the payee \-\> select the category \-\> set the date \-\> add optional notes \-\> tap Save.

**8\. Record a deposit (income)**

**Actions:** Tap the "+" button \-\> select the Deposit type \-\> enter the amount \-\> select the payee and category \-\> set the date \-\> tap Save.

**9\. Record a transfer between accounts**

**Actions:** Tap the "+" button \-\> select the Transfer type \-\> choose the source account \-\> choose the destination account \-\> enter the amount (and the converted amount if the currencies differ) \-\> set the date \-\> tap Save.

**10\. Create a split transaction**

**Actions:** Start a new transaction \-\> tap the category field \-\> tap the "Split" option \-\> tap "Add" to create each split line with its category and amount \-\> repeat until the total matches \-\> tap Done \-\> Save.

**11\. Set a transaction status**

**Actions:** Open the transaction editor \-\> tap the status selector \-\> choose the state (for example None, Reconciled, Void, Follow up, Duplicate) \-\> tap Save.

**12\. Attach a file or photo to a transaction**

**Actions:** Open a transaction \-\> tap the attachment action \-\> choose to take a photo or select a file \-\> confirm; the attachment is linked to the transaction.

**13\. Edit or delete a transaction**

**Actions:** Open the account transaction list \-\> tap the transaction to open it and change the fields \-\> tap Save; or long-press it in the list \-\> tap Delete \-\> confirm.

**14\. Duplicate a transaction**

**Actions:** Open the transaction list \-\> long-press the transaction \-\> tap the duplicate/copy action \-\> adjust the date and amount \-\> tap Save.

**15\. Create a recurring (scheduled) transaction**

**Actions:** Open the drawer \-\> tap "Recurring transactions" \-\> tap the "+" button \-\> fill in the transaction details \-\> set the next occurrence date \-\> choose the repeat frequency and the number of payments \-\> tap Save.

**16\. Enter or skip a due recurring transaction**

**Actions:** Open "Recurring transactions" \-\> find the due entry \-\> tap the enter action to post it to the ledger, or tap the skip action to move to the next occurrence.

**17\. Manage payees**

**Actions:** Open the drawer \-\> tap "Payees" \-\> tap "+" to add a payee and enter its name \-\> tap an existing payee to rename it \-\> long-press to delete it \-\> confirm.

**18\. Manage categories and subcategories**

**Actions:** Open the drawer \-\> tap "Categories" \-\> tap "+" to add a category \-\> enter the name and choose the parent category for a subcategory \-\> tap Save; long-press an entry to rename or delete it.

**19\. Manage currencies and exchange rates**

**Actions:** Open the drawer \-\> tap "Currencies" \-\> tap "+" to add a currency from the list \-\> tap a currency to edit its symbol, decimal separator and conversion rate \-\> use the update action to refresh online rates \-\> tap Save.

**20\. Set the base currency**

**Actions:** Open Settings \-\> open the currency/general section \-\> tap the base currency entry \-\> select the currency \-\> confirm.

**21\. Create a budget**

**Actions:** Open the drawer \-\> tap "Budgets"/"Budget setup" \-\> tap "+" to create a budget year or period \-\> enter the name and period \-\> tap Save \-\> open the budget and set the planned amount per category.

**22\. Review budget performance**

**Actions:** Open the drawer \-\> tap "Budgets" \-\> select the budget period \-\> review the planned, actual and remaining amounts per category.

**23\. View the account balances dashboard**

**Actions:** Open the app home screen \-\> review the account cards showing the reconciled and current balances and the overall total.

**24\. Search transactions**

**Actions:** Open the drawer \-\> tap "Search" \-\> enter the criteria (account, payee, category, date range, amount range, transaction type, status, notes) \-\> tap the search action \-\> review the matching transactions.

**25\. Filter and sort the transaction list**

**Actions:** Open an account \-\> tap the filter/sort control in the toolbar \-\> choose the date range and the sort order \-\> confirm.

**26\. View reports**

**Actions:** Open the drawer \-\> tap "Reports" \-\> select the report (for example "Where the money goes", "Where the money comes from", income versus expenses, or the category summary) \-\> choose the period \-\> review the chart and table.

**27\. Export transactions to CSV**

**Actions:** Open an account or the search result \-\> tap the overflow menu (three dots) \-\> tap "Export to CSV" \-\> choose the destination \-\> confirm.

**28\. Export transactions to QIF**

**Actions:** Open the account \-\> tap the overflow menu \-\> tap "Export to QIF" \-\> choose the destination \-\> confirm.

**29\. Import transactions from a QIF file**

**Actions:** Open the drawer \-\> tap the import entry \-\> select the QIF file \-\> map the target account \-\> confirm the import.

**30\. Synchronise the database with a cloud provider**

**Actions:** Open Settings \-\> tap "Synchronisation" \-\> select the provider (for example Dropbox) \-\> sign in and authorise \-\> select the remote database file \-\> set the sync interval \-\> confirm.

**31\. Trigger a manual synchronisation**

**Actions:** Open the drawer \-\> tap the sync/refresh action \-\> wait for the upload or download to complete.

**32\. Set a passcode lock for the app**

**Actions:** Open Settings \-\> tap "Security"/passcode \-\> enable the passcode \-\> enter the code twice \-\> confirm; the code is requested at each launch.

**33\. Change the theme and appearance**

**Actions:** Open Settings \-\> tap "Look and feel" \-\> choose the theme (light or dark), the font size and the list appearance options \-\> return.

**34\. Configure the date format and number formatting**

**Actions:** Open Settings \-\> tap "Look and feel"/general \-\> set the date format, the group separator and the decimal separator \-\> return.

**35\. Set the default account and default transaction status**

**Actions:** Open Settings \-\> tap the general/behaviour section \-\> select the default account for new transactions and the default status \-\> return.

**36\. Enable notifications for due recurring transactions**

**Actions:** Open Settings \-\> tap the notifications section \-\> enable the reminder for due recurring transactions \-\> set the timing \-\> return.

**37\. Perform database maintenance**

**Actions:** Open Settings \-\> tap the database section \-\> use the actions to check the database integrity, optimise/vacuum it, or view the database path and size.

**38\. Create a database backup**

**Actions:** Open Settings \-\> tap the database section \-\> tap the backup action \-\> choose the destination \-\> confirm; a copy of the .mmb file is written.

**39\. View the about screen, help and donation links**

**Actions:** Open the drawer or Settings \-\> tap "About" \-\> read the version, open the help/website link, or open the donation entry.

 

### **App Name: MyExpenses**

*Package: org.totschnig.myexpenses  |  Version documented: 4.1.0.2  |  Reference: Official My Expenses documentation (faq.myexpenses.mobi) and in-app menus*

*Note: My Expenses ships as a free version with Contrib, Extended and Professional in-app upgrades. Features restricted to a paid tier are labelled inline.*

**Features:**

**1\. Create an account**

**Actions:** Open the navigation drawer \-\> tap "Accounts"/the "+" beside the account list \-\> enter the account label \-\> enter the opening balance \-\> select the currency \-\> select the account type (for example cash, bank, credit card, asset, liability) \-\> pick a colour \-\> tap the tick to save.

**2\. Edit or delete an account**

**Actions:** Open the drawer \-\> long-press the account (or open it and use the overflow menu) \-\> tap Edit to change its properties, or tap Delete and confirm.

**3\. Hide or reorder accounts**

**Actions:** Open the drawer \-\> long-press the account \-\> tap the hide action, or use the sort option in the overflow menu to change the account ordering.

**4\. View the aggregate (all accounts) balance**

**Actions:** Open the drawer \-\> tap the aggregate/"Total" entry for a currency \-\> the combined transaction list and balance for all accounts in that currency are shown.

**5\. Record an expense**

**Actions:** Open the account \-\> tap the "+" floating action button \-\> keep the Expense tab selected \-\> enter the amount \-\> select the category \-\> select or type the payee \-\> set the date and time \-\> add optional notes and tags \-\> tap the tick to save.

**6\. Record income**

**Actions:** Tap the "+" button \-\> switch to the Income tab \-\> enter the amount, category and payer \-\> set the date \-\> tap save.

**7\. Record a transfer between accounts**

**Actions:** Tap the "+" button \-\> switch to the Transfer tab \-\> select the destination account \-\> enter the amount (and the equivalent amount for a different currency) \-\> set the date \-\> tap save.

**8\. Create a split transaction**

**Actions:** Tap the "+" button \-\> tap the overflow menu \-\> tap "Create split" \-\> tap "Add split part" for each line and enter its amount and category \-\> repeat until the parts add up \-\> tap save.

**9\. Use the built-in calculator for amounts**

**Actions:** Open the transaction editor \-\> tap the calculator icon beside the amount field \-\> enter the arithmetic expression \-\> tap the equals/confirm button to transfer the result into the amount field.

**10\. Attach a picture or file to a transaction**

**Actions:** Open a transaction \-\> tap the attachment (paper clip) icon \-\> choose to take a photo or select an existing file \-\> confirm; tap the thumbnail later to view it.

**11\. Scan a receipt with OCR**

**Actions:** Open the transaction editor \-\> tap the OCR/scan action \-\> take or select the receipt image \-\> wait for the recognition \-\> confirm or correct the detected amount, date and payee \-\> tap save. (Professional feature; requires the OCR engine to be configured in Settings.)

**12\. Add tags to a transaction**

**Actions:** Open the transaction editor \-\> tap the tags field \-\> select existing tags or create a new one \-\> confirm \-\> tap save.

**13\. Manage the tag list**

**Actions:** Open the drawer \-\> tap "Manage tags" \-\> tap "+" to create a tag \-\> long-press a tag to rename, recolour or delete it \-\> confirm.

**14\. Set the transaction status (cleared/reconciled)**

**Actions:** Open the transaction list \-\> long-press the transaction \-\> tap the status action \-\> choose uncleared, cleared or reconciled; or use the reconciliation banner in the account view.

**15\. Create a template for a recurring transaction**

**Actions:** Open a saved transaction \-\> tap the overflow menu \-\> tap "Save as template" \-\> enter the template title \-\> tap save; or open the drawer \-\> "Templates" \-\> tap "+" and fill in the details.

**16\. Create a plan (schedule) for a template**

**Actions:** Open the drawer \-\> tap "Templates and plans" \-\> open the template \-\> tap the plan/calendar row \-\> set the start date and the recurrence rule \-\> choose whether instances are created automatically or require confirmation \-\> tap save.

**17\. Apply a template manually**

**Actions:** Open the drawer \-\> tap "Templates" \-\> tap the template \-\> review the pre-filled transaction \-\> adjust the amount or date \-\> tap save.

**18\. Manage categories**

**Actions:** Open the drawer \-\> tap "Manage categories" \-\> tap "+" to create a category or subcategory \-\> enter the name \-\> pick an icon and colour \-\> tap save; long-press an existing category to edit, move or delete it.

**19\. Import a predefined category set**

**Actions:** Open "Manage categories" \-\> tap the overflow menu \-\> tap the "Set up categories"/import option \-\> choose the predefined set \-\> confirm.

**20\. Manage parties (payees and payers)**

**Actions:** Open the drawer \-\> tap "Manage parties" \-\> tap "+" to add a party \-\> enter the name \-\> tap save; long-press to rename, merge or delete.

**21\. Create and track a budget**

**Actions:** Open the drawer \-\> tap "Budgets" \-\> tap "+" \-\> select the account or aggregate \-\> choose the period (weekly, monthly, yearly or custom) \-\> enter the total budget \-\> allocate amounts to individual categories \-\> tap save.

**22\. Review budget progress**

**Actions:** Open the drawer \-\> tap "Budgets" \-\> select the budget \-\> review the progress bars per category and the remaining amount for the period.

**23\. Track debts (money lent and borrowed)**

**Actions:** Open the drawer \-\> tap "Debts" \-\> tap "+" \-\> enter the label, the party, the amount and the date \-\> tap save \-\> record repayments against the debt from the debt detail screen.

**24\. Filter the transaction list**

**Actions:** Open an account \-\> tap the filter icon in the toolbar \-\> select the criteria (category, payee, amount range, date range, transaction type, status, method, tag or free text) \-\> apply; tap the clear action to remove the filter.

**25\. Search transactions by text**

**Actions:** Open an account \-\> tap the search icon \-\> type the text \-\> review the matching transactions.

**26\. Group the transaction list by period**

**Actions:** Open an account \-\> tap the overflow menu \-\> tap "Group by" \-\> choose none, day, week, month or year \-\> confirm; group headers with subtotals appear.

**27\. Sort the transaction list**

**Actions:** Open an account \-\> tap the overflow menu \-\> tap the sort option \-\> choose the field and direction \-\> confirm.

**28\. View the distribution chart**

**Actions:** Open the drawer or the account overflow menu \-\> tap "Distribution" \-\> select the period \-\> review the pie/bar chart of spending by category \-\> tap a slice to drill into the subcategories.

**29\. View the history chart**

**Actions:** Open the drawer or the account overflow menu \-\> tap "History" \-\> select the grouping period \-\> review the income, expense and balance trend chart.

**30\. Print a report to PDF**

**Actions:** Open an account (optionally with a filter applied) \-\> tap the overflow menu \-\> tap "Print" \-\> confirm the layout options \-\> the PDF is generated and saved or sent to the printer.

**31\. Export data to CSV, QIF or JSON**

**Actions:** Open the account or the drawer \-\> tap the overflow menu \-\> tap "Export" \-\> choose the format (CSV, QIF or JSON) \-\> set the date range, the separator, the encoding and the handling of already-exported transactions \-\> tap the confirm button.

**32\. Import data from CSV**

**Actions:** Open the drawer \-\> tap "Import" \-\> tap CSV \-\> select the file \-\> set the separator and encoding \-\> map each column to a field \-\> choose the target account \-\> confirm.

**33\. Import data from QIF or other formats**

**Actions:** Open the drawer \-\> tap "Import" \-\> choose QIF (or another supported format such as OFX or Grisbi) \-\> select the file \-\> choose the target account and the currency \-\> confirm.

**34\. Create a backup**

**Actions:** Open Settings \-\> tap "Backup and restore"/Backup \-\> choose the destination folder \-\> optionally enable encryption and set the password \-\> tap the backup action.

**35\. Restore from a backup**

**Actions:** Open Settings \-\> tap "Backup and restore" \-\> tap Restore \-\> select the backup file \-\> enter the password if it is encrypted \-\> confirm; the current data is replaced.

**36\. Schedule automatic backups**

**Actions:** Open Settings \-\> Backup \-\> enable the automatic backup option \-\> set the time and the retention \-\> confirm.

**37\. Set up cloud synchronisation**

**Actions:** Open Settings \-\> tap "Synchronisation" \-\> tap "+" to add a backend (for example WebDAV/Nextcloud, Dropbox or Google Drive) \-\> enter the credentials or complete the OAuth flow \-\> choose the accounts to sync \-\> confirm. (Extended/Professional feature.)

**38\. Protect the app with a password or the device lock**

**Actions:** Open Settings \-\> tap "Protection"/Security \-\> choose password protection or device lock (screen lock/biometrics) \-\> set the password if required \-\> configure the delay and whether the account balances are hidden \-\> confirm.

**39\. Manage currencies and exchange rates**

**Actions:** Open Settings \-\> tap the currency section \-\> tap a currency to set its symbol and number of fraction digits \-\> configure the exchange-rate provider and download rates where supported.

**40\. Add a home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find My Expenses \-\> drag the required widget (for example the template, account balance or quick-expense widget) onto the home screen \-\> select the account or template \-\> confirm.

**41\. Configure the user interface**

**Actions:** Open Settings \-\> tap "User interface" \-\> set the theme (light, dark or system), the font size, the language, the grouping default, whether the running balance is shown and the home screen summary options.

**42\. Configure transaction entry defaults**

**Actions:** Open Settings \-\> tap the transaction/data entry section \-\> set options such as the default transaction type, whether the time is recorded, auto-fill of amount and category from the payee, and the default method.

**43\. Manage payment methods**

**Actions:** Open Settings (or the drawer) \-\> tap the payment methods entry \-\> tap "+" to add a method \-\> enter the label and select the applicable account types \-\> tap save.

**44\. Reset an account (delete its transactions)**

**Actions:** Open the drawer \-\> long-press the account \-\> tap "Reset" \-\> choose whether to export the transactions first and whether to keep the opening balance \-\> confirm.

**45\. Upgrade to a paid tier**

**Actions:** Open Settings or the drawer \-\> tap the Contrib/Professional entry \-\> review the feature comparison \-\> complete the in-app purchase or enter a licence key.

**46\. Open help and the FAQ**

**Actions:** Open Settings or the overflow menu \-\> tap "Help"/"FAQ" \-\> read the in-app help pages or open the online FAQ.

 

## **Category: File management**

### **App Name: Amaze File Manager**

*Package: com.amaze.filemanager  |  Version documented: 3.11.3  |  Reference: Official Amaze File Manager repository documentation and F-Droid listing*

**Features:**

**1\. Browse internal storage and the SD card**

**Actions:** Open the app \-\> open the navigation drawer (hamburger icon) \-\> tap the storage volume \-\> tap folders to navigate \-\> tap the back arrow or the breadcrumb to move up.

**2\. Create a new folder**

**Actions:** Navigate to the target directory \-\> tap the "+" floating action button \-\> tap "Folder" \-\> enter the folder name \-\> tap Create.

**3\. Create a new empty file**

**Actions:** Navigate to the target directory \-\> tap the "+" button \-\> tap "File" \-\> enter the file name \-\> tap Create.

**4\. Copy files and folders**

**Actions:** Long-press the item(s) to select them \-\> tap the copy icon in the contextual toolbar \-\> navigate to the destination folder \-\> tap the paste button.

**5\. Move (cut) files and folders**

**Actions:** Long-press the item(s) \-\> tap the cut/move icon \-\> navigate to the destination \-\> tap the paste button.

**6\. Rename a file or folder**

**Actions:** Long-press the item \-\> tap the overflow menu in the contextual toolbar \-\> tap "Rename" \-\> enter the new name \-\> tap OK.

**7\. Delete files and folders**

**Actions:** Long-press the item(s) \-\> tap the delete (bin) icon \-\> confirm the deletion.

**8\. Select multiple items**

**Actions:** Long-press the first item \-\> tap the further items to add them \-\> use the select-all action in the toolbar if required \-\> apply the wanted bulk operation.

**9\. Search for files in the current folder**

**Actions:** Tap the search icon in the toolbar \-\> type the file name \-\> review the results as they appear.

**10\. Run a deep search across subfolders**

**Actions:** Tap the search icon \-\> type the query \-\> tap the "Search in this folder and subfolders"/deep search option in the result banner \-\> wait for the recursive scan to finish.

**11\. Sort the file list**

**Actions:** Open a folder \-\> tap the overflow menu (three dots) \-\> tap "Sort by" \-\> choose the criterion (name, last modified, size or type) and the direction \-\> confirm.

**12\. Switch between list and grid view**

**Actions:** Open a folder \-\> tap the overflow menu \-\> tap the "View" / grid-list toggle \-\> the layout changes for that folder.

**13\. Show or hide hidden files**

**Actions:** Tap the overflow menu \-\> toggle "Show hidden files".

**14\. Open a file with an external app**

**Actions:** Tap the file \-\> if several handlers exist, choose the app in the chooser; or long-press the file \-\> tap the overflow menu \-\> tap "Open with" \-\> select the app.

**15\. Share files**

**Actions:** Long-press the item(s) \-\> tap the share icon \-\> choose the destination app in the Android share sheet.

**16\. View file properties**

**Actions:** Long-press the file \-\> tap the overflow menu \-\> tap "Properties" \-\> read the path, size, last-modified time, permissions and the MD5/SHA-1 checksums.

**17\. Change file permissions (root)**

**Actions:** Enable root access in Settings \-\> long-press the file \-\> tap Properties \-\> open the Permissions tab \-\> tick the read/write/execute boxes for owner, group and others \-\> tap Apply.

**18\. Compress files into an archive**

**Actions:** Long-press the item(s) \-\> tap the overflow menu \-\> tap "Compress" \-\> choose the archive format (for example ZIP, TAR or TAR.GZ) \-\> enter the archive name \-\> tap Create.

**19\. Extract an archive**

**Actions:** Tap an archive file (ZIP, RAR, TAR, TAR.GZ, 7Z) \-\> the archive viewer opens \-\> tap the extract action \-\> choose the destination folder \-\> confirm.

**20\. Browse inside an archive without extracting it**

**Actions:** Tap the archive file \-\> browse the entries \-\> tap a single entry to preview or extract just that item.

**21\. Encrypt a file**

**Actions:** Long-press the file \-\> tap the overflow menu \-\> tap "Encrypt" \-\> choose to use a password or the device fingerprint \-\> set the password \-\> confirm; an .aze encrypted file is produced.

**22\. Decrypt a file**

**Actions:** Tap the encrypted (.aze) file \-\> enter the password or authenticate with the fingerprint \-\> choose the destination \-\> confirm.

**23\. Edit a text file in the built-in editor**

**Actions:** Tap a text file \-\> choose the internal text editor \-\> edit the content \-\> tap the save icon \-\> tap back to exit.

**24\. Add a folder to the bookmarks**

**Actions:** Navigate to the folder \-\> open the navigation drawer \-\> tap the "+" beside Bookmarks (or long-press the folder \-\> "Add to bookmarks") \-\> confirm the name \-\> tap OK.

**25\. Edit or remove a bookmark**

**Actions:** Open the drawer \-\> long-press the bookmark \-\> choose Edit to change the name and path, or Delete to remove it \-\> confirm.

**26\. Open a second tab / use the dual pane**

**Actions:** Tap the tab indicator at the top of the file list \-\> swipe between the two tabs \-\> use one tab as the source and the other as the destination when copying.

**27\. Set a folder as the home directory**

**Actions:** Navigate to the folder \-\> tap the overflow menu \-\> tap "Set as home"; opening the app afterwards starts in that folder.

**28\. Open the app manager**

**Actions:** Open the navigation drawer \-\> tap "Apps" \-\> review the installed applications with their sizes and versions \-\> tap an app for the actions.

**29\. Uninstall an application from the app manager**

**Actions:** Open the Apps list \-\> long-press the application \-\> tap the uninstall action \-\> confirm the system prompt.

**30\. Back up an installed app's APK**

**Actions:** Open the Apps list \-\> long-press the application \-\> tap the backup/"Save APK" action \-\> choose the destination \-\> confirm.

**31\. Start the built-in FTP server**

**Actions:** Open the navigation drawer \-\> tap "FTP"/FTP server \-\> tap the start button \-\> note the displayed ftp:// address and port \-\> connect from a computer on the same network \-\> tap stop to end it.

**32\. Configure the FTP server**

**Actions:** Open the FTP screen \-\> tap the overflow menu/settings \-\> set the port, the shared directory, the login (anonymous or username and password), the read-only flag, the timeout and whether it stays on over Wi-Fi only \-\> confirm.

**33\. Connect to an SMB (Windows) share**

**Actions:** Open the navigation drawer \-\> tap the "+" beside Network/Cloud \-\> tap "SMB connection" \-\> enter the server IP or name, the share path, the username and the password \-\> tap Create \-\> tap the new entry to browse it.

**34\. Connect over SFTP/SSH**

**Actions:** Open the drawer \-\> tap the "+" beside the network section \-\> tap "SCP/SFTP connection" \-\> enter the host, port, username and password or key \-\> accept the host fingerprint \-\> tap Create.

**35\. Connect to a cloud storage account**

**Actions:** Open the drawer \-\> tap the "+" beside the cloud section \-\> choose the provider (for example Dropbox, Google Drive, OneDrive or Box) \-\> sign in and authorise \-\> the account appears in the drawer for browsing.

**36\. Enable root explorer mode**

**Actions:** Open Settings \-\> tap the "Root access"/root explorer option \-\> toggle it on \-\> grant the superuser request \-\> system directories become browsable and writable.

**37\. View recent files**

**Actions:** Open the navigation drawer \-\> tap "Recent files"/the recent section on the home screen \-\> tap a file to open it.

**38\. Browse files by category**

**Actions:** Open the drawer or the home screen \-\> tap a category (Images, Videos, Audio, Documents, Apps) \-\> review the collected files of that type.

**39\. Change the theme**

**Actions:** Open Settings \-\> tap "Appearance"/Theme \-\> choose Light, Dark, Black or "Follow system" \-\> return.

**40\. Change the accent and colour scheme**

**Actions:** Open Settings \-\> tap the colours entry \-\> select the primary, accent and icon colours (separate values can be set for the light and dark themes) \-\> confirm.

**41\. Configure behaviour settings**

**Actions:** Open Settings \-\> tap "Behaviour" \-\> toggle options such as showing the file size in the list, the thumbnail display, the file-count display, the "exit on back press" behaviour and the changing of the toolbar colour per folder.

**42\. Enable the encrypted folder/hidden files protection**

**Actions:** Open Settings \-\> open the security section \-\> enable the password/fingerprint protection for encrypted files \-\> confirm.

**43\. Add a shortcut to a folder on the home screen**

**Actions:** Long-press the folder \-\> tap the overflow menu \-\> tap "Add shortcut" \-\> confirm the placement on the Android home screen.

**44\. Copy a file path to the clipboard**

**Actions:** Long-press the file \-\> tap the overflow menu \-\> tap "Copy path"; the full path is placed on the clipboard.

**45\. View storage usage**

**Actions:** Open the navigation drawer \-\> the storage entries show the used and total space \-\> tap a volume to browse it.

**46\. Open the about screen and licences**

**Actions:** Open the navigation drawer \-\> tap "About" \-\> read the version, the changelog, the contributor list and the open-source licences.

 

### **App Name: Material Files**

*Package: me.zhanghai.android.files  |  Version documented: 1.7.4  |  Reference: Official Material Files repository documentation and F-Droid listing*

**Features:**

**1\. Browse local storage**

**Actions:** Open the app \-\> open the navigation drawer (hamburger icon or left-edge swipe) \-\> tap a storage volume or standard directory \-\> tap folders to navigate \-\> tap the breadcrumb path at the top to jump back to any ancestor folder.

**2\. Create a new folder**

**Actions:** Navigate to the target directory \-\> tap the "+" floating action button \-\> tap "Create folder" \-\> enter the name \-\> tap Create.

**3\. Create a new empty file**

**Actions:** Navigate to the directory \-\> tap the "+" button \-\> tap "Create file" \-\> enter the file name \-\> tap Create.

**4\. Copy files and folders**

**Actions:** Long-press the item(s) \-\> tap the copy icon in the contextual toolbar \-\> navigate to the destination \-\> tap the paste button in the bottom bar.

**5\. Move files and folders**

**Actions:** Long-press the item(s) \-\> tap the cut/move icon \-\> navigate to the destination \-\> tap the paste button.

**6\. Rename an item**

**Actions:** Long-press the item \-\> tap the overflow menu in the contextual toolbar \-\> tap "Rename" \-\> enter the new name \-\> tap OK.

**7\. Delete items**

**Actions:** Long-press the item(s) \-\> tap the delete icon \-\> confirm the deletion.

**8\. Select multiple items and use select all**

**Actions:** Long-press the first item \-\> tap the additional items \-\> tap the select-all action in the toolbar to select the whole folder \-\> apply the required action.

**9\. Search for files**

**Actions:** Open a folder \-\> tap the search icon in the toolbar \-\> type the query \-\> the recursive search results appear \-\> tap a result to open it.

**10\. Sort the file list**

**Actions:** Tap the overflow menu (three dots) \-\> tap "Sort by" \-\> choose name, last modified, type or size \-\> choose ascending or descending \-\> optionally enable "Directories first".

**11\. Remember the sort order per folder**

**Actions:** Set the sort order in a folder \-\> tap the overflow menu \-\> enable the "Sort paths for this folder"/per-folder sort option so the choice is remembered for that directory only.

**12\. Switch between list and grid view**

**Actions:** Tap the overflow menu \-\> tap the view/grid toggle \-\> the layout changes between the list and the grid of thumbnails.

**13\. Show or hide hidden files**

**Actions:** Tap the overflow menu \-\> toggle "Show hidden files".

**14\. View and open an archive**

**Actions:** Tap a ZIP, RAR, 7Z, TAR or TAR.GZ file \-\> the archive opens as a browsable folder \-\> navigate inside it \-\> tap a file to preview it.

**15\. Extract an archive**

**Actions:** Long-press the archive file \-\> tap "Extract" (or open the archive and use the extract action) \-\> choose the destination folder \-\> confirm.

**16\. Create an archive**

**Actions:** Long-press the item(s) to include \-\> tap the overflow menu \-\> tap "Compress"/"Add to archive" \-\> choose the format and enter the archive name \-\> confirm.

**17\. Open a file with another app**

**Actions:** Tap the file to open it with the default handler, or long-press it \-\> tap the overflow menu \-\> tap "Open with" \-\> pick the app from the chooser.

**18\. Share files**

**Actions:** Long-press the item(s) \-\> tap the share icon \-\> choose the target app in the Android share sheet.

**19\. Copy the path of a file**

**Actions:** Long-press the item \-\> tap the overflow menu \-\> tap "Copy path"; the path is placed on the clipboard.

**20\. View file properties**

**Actions:** Long-press the item \-\> tap the overflow menu \-\> tap "Properties" \-\> read the file tab (name, type, size, times), the permissions tab and, on rooted devices, the owner, group and SELinux context.

**21\. Change file permissions, owner and SELinux context (root)**

**Actions:** Enable root access in Settings \-\> open the file Properties \-\> open the Permissions tab \-\> tap the permission, owner, group or SELinux context row \-\> set the value \-\> confirm.

**22\. View an image in the built-in viewer**

**Actions:** Tap an image file \-\> the image viewer opens \-\> swipe left or right for the next image in the folder \-\> pinch to zoom \-\> tap the overflow menu for share, delete and info actions.

**23\. Edit a text file in the built-in editor**

**Actions:** Tap a text file \-\> the text editor opens \-\> edit the content \-\> tap the save icon \-\> tap back to exit.

**24\. Change the text file encoding in the editor**

**Actions:** Open a text file in the editor \-\> tap the overflow menu \-\> tap the encoding option \-\> choose the character set \-\> confirm.

**25\. Bookmark a directory**

**Actions:** Navigate to the folder \-\> tap the overflow menu \-\> tap "Add bookmark"; the entry appears in the navigation drawer.

**26\. Manage bookmark directories**

**Actions:** Open Settings \-\> tap "Bookmark directories" \-\> tap an entry to rename it or change its path \-\> drag the handle to reorder \-\> tap the delete action to remove one.

**27\. Add a shortcut to a folder on the home screen**

**Actions:** Navigate to the folder \-\> tap the overflow menu \-\> tap "Add to home screen"/"Create shortcut" \-\> confirm the placement.

**28\. Connect to an FTP or FTPS server**

**Actions:** Open the navigation drawer \-\> tap "Add server"/the "+" beside the network section \-\> choose FTP or FTPS \-\> enter the host, port, username and password (or select anonymous) \-\> tap the tick to save \-\> tap the entry to browse it.

**29\. Connect to an SFTP server**

**Actions:** Open the drawer \-\> tap "Add server" \-\> choose SFTP \-\> enter the host, port and credentials (password or private key) \-\> accept the host key \-\> tap save.

**30\. Connect to an SMB share**

**Actions:** Open the drawer \-\> tap "Add server" \-\> choose SMB \-\> enter the host, share name, domain, username and password \-\> tap save \-\> tap the entry to browse it.

**31\. Connect to a WebDAV server**

**Actions:** Open the drawer \-\> tap "Add server" \-\> choose WebDAV or WebDAVS \-\> enter the URL and credentials \-\> tap save.

**32\. Edit or remove a saved server**

**Actions:** Open the drawer \-\> long-press the server entry \-\> tap Edit to change the settings, or tap Remove \-\> confirm.

**33\. Start the built-in FTP server to share files with a computer**

**Actions:** Open the navigation drawer \-\> tap "FTP server" \-\> tap the start/toggle control \-\> note the ftp:// URL shown \-\> connect from another device on the same network \-\> tap stop when finished.

**34\. Configure the FTP server settings**

**Actions:** Open Settings \-\> tap the FTP server section \-\> set the anonymous login or the username and password, the port, the shared directory and the writable flag \-\> return.

**35\. Enable root access**

**Actions:** Open Settings \-\> tap the root section \-\> toggle the root strategy/"Always use root" option \-\> grant the superuser request when prompted.

**36\. Show a "root directory" entry in the navigation**

**Actions:** Open Settings \-\> enable the option that shows the file system root ("/") in the drawer \-\> return to the file list.

**37\. Change the theme and colours**

**Actions:** Open Settings \-\> tap "Appearance"/Theme \-\> choose the theme colour, enable Material You dynamic colours, choose the night mode behaviour and enable the pure-black night theme \-\> return.

**38\. Change the app language**

**Actions:** Open Settings \-\> tap the Language entry \-\> select the interface language \-\> confirm.

**39\. Configure the file list behaviour**

**Actions:** Open Settings \-\> open the file list section \-\> set the default sort order, whether the file size is shown for directories, whether thumbnails are generated, and the default view type.

**40\. Configure the standard directories shown in the navigation drawer**

**Actions:** Open Settings \-\> tap "Standard directories" \-\> toggle the individual entries (for example Downloads, Documents, Pictures, Music, Movies, DCIM) \-\> drag to reorder them.

**41\. Configure the storage volumes shown**

**Actions:** Open Settings \-\> tap the storage section \-\> enable or disable the individual volumes and add an external SD card or a document-provider tree \-\> confirm.

**42\. Open the about screen and licences**

**Actions:** Open the navigation drawer or Settings \-\> tap "About" \-\> read the version, the author information and the open-source licences.

 

### **App Name: Fossify File Manager**

*Package: org.fossify.filemanager  |  Version documented: 1.6.1  |  Reference: Official Fossify repository documentation and F-Droid listing*

**Features:**

**1\. Browse internal storage, the SD card and USB storage**

**Actions:** Open the app \-\> tap the Storage tab \-\> tap the volume to browse \-\> tap folders to navigate \-\> use the breadcrumb bar at the top to move back up.

**2\. View storage usage by category**

**Actions:** Open the Storage tab \-\> review the used/free space bar \-\> tap a category tile (Images, Videos, Audio, Documents, Archives, Others) to list all files of that type.

**3\. View recent files**

**Actions:** Open the "Recents" tab \-\> scroll the list of recently modified files \-\> tap a file to open it.

**4\. Add and open favourites**

**Actions:** Long-press a folder \-\> tap the overflow menu \-\> tap "Add to favourites" \-\> open the Favourites section from the drawer/top bar to reach it later.

**5\. Create a new folder**

**Actions:** Navigate to the target directory \-\> tap the "+" floating action button \-\> tap "Folder" \-\> enter the folder name \-\> tap OK.

**6\. Create a new file**

**Actions:** Navigate to the directory \-\> tap the "+" button \-\> tap "File" \-\> enter the file name \-\> tap OK.

**7\. Copy files and folders**

**Actions:** Long-press the item(s) \-\> tap the copy icon (or the overflow menu \-\> "Copy to") \-\> select the destination folder \-\> tap the confirm button.

**8\. Move files and folders**

**Actions:** Long-press the item(s) \-\> tap the move icon (or the overflow menu \-\> "Move to") \-\> choose the destination folder \-\> tap the confirm button.

**9\. Rename items**

**Actions:** Long-press the item \-\> tap the rename (pencil) icon \-\> enter the new name \-\> tap OK; selecting several items offers batch renaming with a name pattern or an appended value.

**10\. Delete items**

**Actions:** Long-press the item(s) \-\> tap the delete (bin) icon \-\> confirm the deletion.

**11\. Select multiple items**

**Actions:** Long-press the first item \-\> tap the further items to add them, or tap the select-all action in the contextual toolbar \-\> apply the bulk operation.

**12\. Search for files**

**Actions:** Tap the search icon in the toolbar \-\> type the file name \-\> the current folder and its subfolders are searched \-\> tap a result to open it.

**13\. Sort the file list**

**Actions:** Tap the overflow menu (three dots) \-\> tap "Sort by" \-\> choose name, date modified, size, extension or a random order \-\> choose ascending or descending \-\> optionally enable per-folder sorting \-\> tap OK.

**14\. Switch between list and grid view**

**Actions:** Tap the overflow menu \-\> tap "Change view type" \-\> select Grid or List \-\> optionally apply it to that folder only \-\> tap OK.

**15\. Show or hide hidden items**

**Actions:** Tap the overflow menu \-\> toggle "Temporarily show hidden"/"Show hidden items"; the permanent setting is in Settings.

**16\. Compress files into a ZIP archive**

**Actions:** Long-press the item(s) \-\> tap the overflow menu \-\> tap "Compress" \-\> enter the archive name \-\> optionally set a password \-\> tap OK.

**17\. Decompress a ZIP archive**

**Actions:** Long-press the archive \-\> tap the overflow menu \-\> tap "Decompress" \-\> choose the destination \-\> enter the password if the archive is protected \-\> tap OK.

**18\. Open a file with another app**

**Actions:** Tap the file \-\> pick the handler from the chooser; or long-press it \-\> tap the overflow menu \-\> tap "Open with" \-\> select the app.

**19\. Share files**

**Actions:** Long-press the item(s) \-\> tap the share icon \-\> select the target app in the Android share sheet.

**20\. View file properties and checksums**

**Actions:** Long-press the item \-\> tap the overflow menu \-\> tap "Properties" \-\> read the path, size, last-modified time, resolution or duration where relevant, and the MD5 checksum.

**21\. Print a file**

**Actions:** Open an image or text file \-\> tap the overflow menu \-\> tap "Print" \-\> choose the printer or "Save as PDF" \-\> confirm.

**22\. Edit a text file in the built-in editor**

**Actions:** Tap a text file \-\> the built-in editor opens \-\> edit the content \-\> tap the save icon \-\> tap back.

**23\. Set a folder as the home folder**

**Actions:** Navigate to the folder \-\> tap the overflow menu \-\> tap "Set as home"; the app opens in that folder from then on.

**24\. Create a home screen shortcut to a folder**

**Actions:** Long-press the folder \-\> tap the overflow menu \-\> tap "Create shortcut" \-\> confirm the placement on the Android home screen.

**25\. Copy the path of an item**

**Actions:** Long-press the item \-\> tap the overflow menu \-\> tap "Copy path to clipboard".

**26\. Enable root access to browse system folders**

**Actions:** Open Settings \-\> enable the root access option \-\> grant the superuser request \-\> the root ("/") volume becomes browsable.

**27\. Protect hidden items with a PIN, pattern or fingerprint**

**Actions:** Open Settings \-\> tap "Password protect hidden items" \-\> choose PIN, pattern or fingerprint \-\> set the secret \-\> confirm; hidden items now require authentication.

**28\. Protect the whole app with a lock**

**Actions:** Open Settings \-\> tap the app-lock/"Password protect the whole app" entry \-\> choose the lock type \-\> set the secret \-\> confirm; the app asks for it on launch.

**29\. Customise the colours and theme**

**Actions:** Open Settings \-\> tap "Customise colours" \-\> choose a preset theme (light, dark, black and white, system default) or set the text, background, primary and app-icon colours individually \-\> tap the tick to save.

**30\. Change the app language**

**Actions:** Open Settings \-\> tap the Language entry \-\> select the language from the system language picker.

**31\. Change the font size**

**Actions:** Open Settings \-\> tap the font size entry \-\> choose small, medium, large or extra large \-\> confirm.

**32\. Configure the delete confirmation and recycle bin behaviour**

**Actions:** Open Settings \-\> toggle the "Show a confirmation dialog before deleting" option and the "Move deleted files into the recycle bin" option.

**33\. Empty or restore the recycle bin**

**Actions:** Open the drawer/overflow menu \-\> tap "Recycle bin" \-\> long-press an item and tap Restore, or tap the "Empty the recycle bin" action \-\> confirm.

**34\. Configure what the "+" button and the tabs show**

**Actions:** Open Settings \-\> open the tabs/visibility section \-\> enable or disable the Files, Recents and Storage tabs \-\> confirm.

**35\. Keep the last-modified date when copying**

**Actions:** Open Settings \-\> toggle the "Keep the last modified date of copied files" option.

**36\. Enable thumbnails for media files**

**Actions:** Open Settings \-\> toggle the option that shows image and video thumbnails in the file list.

**37\. Open the about screen, FAQ and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the FAQ, the version number, the licence list, the privacy policy and the links to the source repository.

 

## **Category: Calendar and contacts**

### **App Name: Etar Calendar**

*Package: ws.xsoh.etar  |  Version documented: 1.0.57  |  Reference: Official Etar repository documentation and F-Droid listing*

**Features:**

**1\. Create an event**

**Actions:** Open the app \-\> tap the "+" floating action button \-\> enter the event title \-\> set the start date and time \-\> set the end date and time \-\> choose the calendar \-\> tap Save.

**2\. Create an all-day event**

**Actions:** Tap the "+" button \-\> enter the title \-\> toggle the "All day" switch on \-\> pick the date (or the date range) \-\> tap Save.

**3\. Create an event by long-pressing a time slot**

**Actions:** Open the day or week view \-\> long-press the empty time slot \-\> the new-event editor opens with that time pre-filled \-\> complete the details \-\> tap Save.

**4\. Add a location to an event**

**Actions:** Open the event editor \-\> tap the location field \-\> type the address or pick a suggestion \-\> tap Save; tapping the location in the event detail opens it in a map app.

**5\. Add a description to an event**

**Actions:** Open the event editor \-\> tap the description/notes field \-\> type the text \-\> tap Save.

**6\. Set an event as repeating**

**Actions:** Open the event editor \-\> tap the repetition row \-\> choose the pattern (daily, weekly, monthly, yearly or custom) \-\> set the interval, the weekdays and the end condition \-\> tap Done \-\> Save.

**7\. Add reminders to an event**

**Actions:** Open the event editor \-\> tap "Add reminder" \-\> choose the lead time (for example 10 minutes, 1 hour, 1 day before) and the method \-\> add further reminders if needed \-\> tap Save.

**8\. Invite guests to an event**

**Actions:** Open the event editor \-\> tap the guests field \-\> type or select the email addresses \-\> tap Save; invitations are sent by the account provider where the calendar supports it.

**9\. Set the availability and privacy of an event**

**Actions:** Open the event editor \-\> tap the availability selector and choose Busy or Free \-\> tap the privacy selector and choose Default, Private or Public \-\> tap Save.

**10\. Set an event's time zone**

**Actions:** Open the event editor \-\> tap the time zone control beside the start time \-\> select the time zone from the list \-\> tap Save.

**11\. Edit an event**

**Actions:** Tap the event in any view \-\> tap the edit (pencil) icon \-\> change the fields \-\> tap Save \-\> for a repeating event choose whether the change applies to this occurrence, this and future occurrences, or the whole series.

**12\. Delete an event**

**Actions:** Tap the event \-\> tap the delete (bin) icon \-\> confirm \-\> for a repeating event choose the scope of the deletion.

**13\. Duplicate an event**

**Actions:** Tap the event \-\> tap the overflow menu (three dots) \-\> tap "Duplicate" \-\> adjust the date and details of the copy \-\> tap Save.

**14\. Share an event**

**Actions:** Tap the event \-\> tap the overflow menu \-\> tap "Share"/the share icon \-\> choose the target app in the Android share sheet.

**15\. Switch to the day view**

**Actions:** Open the navigation drawer (hamburger icon) \-\> tap "Day" \-\> swipe horizontally to move between days.

**16\. Switch to the week view**

**Actions:** Open the drawer \-\> tap "Week" \-\> swipe horizontally to move between weeks.

**17\. Switch to the month view**

**Actions:** Open the drawer \-\> tap "Month" \-\> swipe to move between months \-\> tap a day to see its events.

**18\. Switch to the agenda view**

**Actions:** Open the drawer \-\> tap "Agenda" \-\> scroll the chronological list of upcoming events \-\> tap an entry to open it.

**19\. Jump to today**

**Actions:** Tap the "Today" icon in the toolbar (the calendar icon showing the current date) \-\> the view scrolls to the current date.

**20\. Go to a specific date**

**Actions:** Tap the overflow menu (three dots) \-\> tap "Go to date" \-\> select the date in the picker \-\> tap OK.

**21\. Search events**

**Actions:** Tap the search icon in the toolbar \-\> type the text to look for \-\> review the matching events \-\> tap one to open it.

**22\. Choose which calendars are displayed**

**Actions:** Open the navigation drawer \-\> tap "Calendars to display" (or Settings \-\> Calendars) \-\> tick the calendars to show \-\> tap OK.

**23\. Create a local (offline) calendar**

**Actions:** Open Settings \-\> tap the calendars/"Add offline calendar" entry \-\> enter the calendar name \-\> pick a colour \-\> tap Save; it is stored on the device only.

**24\. Import events from an ICS file**

**Actions:** Open the overflow menu \-\> tap "Import"/"Import ICS" \-\> select the .ics file with the picker \-\> choose the destination calendar \-\> confirm.

**25\. Export events to an ICS file**

**Actions:** Open the overflow menu \-\> tap "Export" \-\> choose the calendars and the date range \-\> choose the destination \-\> confirm.

**26\. Refresh/sync calendars**

**Actions:** Tap the overflow menu \-\> tap "Refresh" \-\> the account sync adapters are triggered and the views reload.

**27\. Snooze or dismiss an event notification**

**Actions:** When the reminder notification appears \-\> tap "Snooze" to postpone it by the configured interval, or tap "Dismiss" to clear it.

**28\. Add the calendar home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Etar \-\> drag the agenda or month widget onto the home screen \-\> configure the calendars and the theme \-\> confirm.

**29\. Change the theme and colours**

**Actions:** Open Settings \-\> tap the theme entry \-\> choose light, dark, black or "follow system" \-\> set the primary colour \-\> return.

**30\. Set the first day of the week**

**Actions:** Open Settings \-\> tap "General"/"Week starts on" \-\> select the weekday \-\> return.

**31\. Show or hide week numbers**

**Actions:** Open Settings \-\> General \-\> toggle the "Show week number" option.

**32\. Hide declined events**

**Actions:** Open Settings \-\> General \-\> toggle "Hide declined events".

**33\. Use a fixed (home) time zone**

**Actions:** Open Settings \-\> General \-\> tap the time zone entry \-\> enable "Use home time zone" \-\> choose the time zone; the calendar keeps showing that zone while travelling.

**34\. Set the default reminder time for new events**

**Actions:** Open Settings \-\> General \-\> tap "Default reminder time" \-\> choose the lead time.

**35\. Set the default event duration**

**Actions:** Open Settings \-\> General \-\> tap the default duration entry \-\> select the length used for newly created events.

**36\. Configure reminder notifications**

**Actions:** Open Settings \-\> tap "Reminders"/Notifications \-\> set the notification sound, vibration, pop-up behaviour and the default snooze delay \-\> return.

**37\. Set quiet hours for notifications**

**Actions:** Open Settings \-\> Reminders \-\> enable quiet hours \-\> set the start and end time \-\> return.

**38\. Change the number of days shown in the week/custom view**

**Actions:** Open Settings \-\> General \-\> tap the "Days per week"/custom view range entry \-\> select the number of days.

**39\. Adjust the text and font size**

**Actions:** Open Settings \-\> tap the appearance/text size entry \-\> select the size \-\> return.

**40\. View the about screen and version**

**Actions:** Open Settings \-\> tap "About"/"Copyright" \-\> read the version number, the licences and the source link.

 

### **App Name: Fossify Calendar**

*Package: org.fossify.calendar  |  Version documented: 1.10.3  |  Reference: Official Fossify repository documentation and F-Droid listing*

**Features:**

**1\. Create an event**

**Actions:** Open the app \-\> tap the "+" floating action button \-\> tap "Event" \-\> enter the title \-\> set the start and end date and time \-\> choose the event type/calendar \-\> tap the save (tick) icon.

**2\. Create a task**

**Actions:** Tap the "+" button \-\> tap "Task" \-\> enter the task title \-\> set the date and time \-\> add a reminder \-\> tap the save icon; tasks can be ticked off from the event list.

**3\. Mark a task as done**

**Actions:** Open the event list or the day view \-\> tap the task \-\> tap the "Mark completed"/checkbox action; the task is shown struck through.

**4\. Create an all-day event**

**Actions:** Tap the "+" button \-\> tap Event \-\> toggle "All-day" on \-\> set the date or the date range \-\> tap save.

**5\. Add a location to an event**

**Actions:** Open the event editor \-\> tap the location field \-\> type the address \-\> tap save; tap the location in the detail view to open it in a map app.

**6\. Add a description to an event**

**Actions:** Open the event editor \-\> tap the description field \-\> type the text \-\> tap save.

**7\. Set a repeating event with a custom rule**

**Actions:** Open the event editor \-\> tap the repetition row \-\> choose the interval (daily, weekly, monthly, yearly or a custom number of days/weeks/months) \-\> set the repeat rule (for example the same weekday of the month or the last day of the month) \-\> set the repeat limit (forever, until a date or after N occurrences) \-\> tap save.

**8\. Add several reminders to an event**

**Actions:** Open the event editor \-\> tap the first reminder row and pick the lead time \-\> tap the additional reminder rows to add up to three reminders \-\> optionally set the notification type per reminder \-\> tap save.

**9\. Add attendees to an event**

**Actions:** Open an event stored in a synced (CalDAV) calendar \-\> tap the attendees row \-\> type or select the contacts \-\> tap save.

**10\. Set the event time zone**

**Actions:** Open the event editor \-\> tap the time zone control \-\> pick the time zone \-\> tap save.

**11\. Edit an event**

**Actions:** Tap the event \-\> tap the edit (pencil) icon \-\> change the values \-\> tap save \-\> for a repeating event choose whether to apply the change to this occurrence, this and future occurrences, or all occurrences.

**12\. Duplicate an event**

**Actions:** Open the event \-\> tap the overflow menu (three dots) \-\> tap "Duplicate" \-\> adjust the copy \-\> tap save.

**13\. Delete an event**

**Actions:** Open the event \-\> tap the delete (bin) icon \-\> choose the deletion scope for a repeating event \-\> confirm.

**14\. Share an event**

**Actions:** Open the event \-\> tap the overflow menu \-\> tap "Share"/export as .ics \-\> choose the destination app.

**15\. Switch between the calendar views**

**Actions:** Tap the view selector in the toolbar (or open the drawer) \-\> choose Daily, Weekly, Monthly, Monthly by day, Yearly or Event list \-\> the calendar redraws in that mode.

**16\. Navigate between periods**

**Actions:** In any view \-\> swipe horizontally to move to the previous or next day, week, month or year \-\> tap the "Today" icon in the toolbar to jump back to the current date.

**17\. Go to a specific date**

**Actions:** Tap the overflow menu \-\> tap "Go to date" \-\> select the date \-\> tap OK.

**18\. Search events**

**Actions:** Tap the search icon in the toolbar \-\> type the text \-\> tap a result to open the event.

**19\. Create an event type with its own colour**

**Actions:** Open Settings (or the overflow menu) \-\> tap "Manage event types" \-\> tap the "+" button \-\> enter the type name \-\> pick a colour \-\> tap OK.

**20\. Filter which event types are shown**

**Actions:** Tap the overflow menu \-\> tap "Filter events by type" \-\> tick the types to display \-\> tap OK.

**21\. Import events from an ICS file**

**Actions:** Tap the overflow menu \-\> tap "Import events" \-\> select the .ics file \-\> choose the target event type \-\> confirm.

**22\. Export events to an ICS file**

**Actions:** Tap the overflow menu \-\> tap "Export events" \-\> choose the event types to include and whether to export past events \-\> choose the destination file \-\> confirm.

**23\. Import contact birthdays**

**Actions:** Open Settings \-\> tap "Add birthdays from contacts"/the birthdays entry \-\> grant the contacts permission \-\> confirm; birthdays appear as yearly events.

**24\. Import contact anniversaries**

**Actions:** Open Settings \-\> tap the anniversaries entry \-\> grant the contacts permission \-\> confirm; anniversaries are added as yearly events.

**25\. Import public holidays**

**Actions:** Open Settings \-\> tap "Add holidays" \-\> select the country/region \-\> confirm; the public holidays are added as a separate event type.

**26\. Show events from synced CalDAV calendars**

**Actions:** Open Settings \-\> tap "CalDAV sync" \-\> enable it \-\> tick the accounts and calendars to display \-\> confirm.

**27\. Add the monthly calendar home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Fossify Calendar \-\> drag the monthly widget onto the home screen \-\> set the background colour, transparency and text colour \-\> tap OK.

**28\. Add the event list home screen widget**

**Actions:** Long-press the home screen \-\> tap Widgets \-\> find Fossify Calendar \-\> drag the event-list widget onto the home screen \-\> configure its colours and the period it covers \-\> tap OK.

**29\. Change the start day of the week**

**Actions:** Open Settings \-\> tap "Start week on" \-\> select the weekday \-\> confirm.

**30\. Show week numbers**

**Actions:** Open Settings \-\> toggle the "Show week numbers" option.

**31\. Set the default event duration, reminder and event type**

**Actions:** Open Settings \-\> open the "New events" section \-\> set the default start time, the default duration, the default reminder and the default event type for new entries.

**32\. Configure reminder notification behaviour**

**Actions:** Open Settings \-\> open the reminders section \-\> set the notification sound, vibration, whether reminders loop until dismissed, and the snooze delay.

**33\. Configure the weekly view display**

**Actions:** Open Settings \-\> open the weekly view section \-\> set the number of days shown, whether to start at the current time, whether all-day events are shown at the top and the row height.

**34\. Configure the monthly view display**

**Actions:** Open Settings \-\> open the monthly view section \-\> toggle whether events are shown as dots or as text and whether grid lines are drawn.

**35\. Customise the app colours and theme**

**Actions:** Open Settings \-\> tap "Customise colours" \-\> choose a preset theme or set the text, background, primary and app-icon colours \-\> tap the tick to save.

**36\. Protect the app with a PIN, pattern or fingerprint**

**Actions:** Open Settings \-\> tap the app-lock entry \-\> choose the lock type \-\> set the secret \-\> confirm.

**37\. Change the app language and font size**

**Actions:** Open Settings \-\> tap the Language entry and choose the language \-\> tap the font size entry and choose the size.

**38\. View the about screen, FAQ and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the FAQ, version, licences and the source repository link.

 

### **App Name: Fossify Contacts**

*Package: org.fossify.contacts  |  Version documented: 1.6.0  |  Reference: Official Fossify repository documentation and F-Droid listing*

**Features:**

**1\. Create a contact**

**Actions:** Open the app \-\> tap the "+" floating action button \-\> choose the storage account (device or a synced account) \-\> enter the first name, middle name and surname \-\> add the phone number \-\> tap the save (tick) icon.

**2\. Add a photo to a contact**

**Actions:** Open the contact editor \-\> tap the photo placeholder at the top \-\> choose "Take photo" or "Choose photo" \-\> crop the image \-\> tap save.

**3\. Add multiple phone numbers with types**

**Actions:** Open the contact editor \-\> tap the "+" beside the phone section \-\> enter the number \-\> tap the type selector and choose Mobile, Home, Work, Main, Fax, Pager or a custom label \-\> repeat for further numbers \-\> tap save.

**4\. Add email addresses**

**Actions:** Open the contact editor \-\> tap the "+" beside the email section \-\> enter the address \-\> pick the type \-\> tap save.

**5\. Add postal addresses**

**Actions:** Open the contact editor \-\> tap the "+" beside the address section \-\> enter the address \-\> pick the type \-\> tap save.

**6\. Add important dates (birthday and anniversary)**

**Actions:** Open the contact editor \-\> tap the "+" beside the events section \-\> pick the date \-\> select Birthday or Anniversary \-\> tap save.

**7\. Add the organisation and job title**

**Actions:** Open the contact editor \-\> scroll to the organisation section \-\> enter the company name and the job title \-\> tap save.

**8\. Add websites and instant messaging handles**

**Actions:** Open the contact editor \-\> tap the "+" beside the website or IM section \-\> enter the value \-\> pick the type \-\> tap save.

**9\. Add notes to a contact**

**Actions:** Open the contact editor \-\> scroll to the notes field \-\> type the text \-\> tap save.

**10\. Set a custom ringtone for a contact**

**Actions:** Open the contact editor \-\> tap the ringtone row \-\> select the tone from the picker \-\> tap save.

**11\. Edit a contact**

**Actions:** Open the contact \-\> tap the edit (pencil) icon \-\> change the fields \-\> tap the save icon.

**12\. Delete a contact**

**Actions:** Open the contact \-\> tap the overflow menu (three dots) \-\> tap Delete \-\> confirm; or long-press the contact in the list and tap the delete icon.

**13\. Mark a contact as a favourite**

**Actions:** Open the contact \-\> tap the star icon in the toolbar; or long-press the contact in the list \-\> tap "Add to favourites". Favourites appear in the Favourites tab.

**14\. Remove a contact from favourites**

**Actions:** Open the Favourites tab \-\> long-press the contact \-\> tap "Remove from favourites" \-\> confirm.

**15\. Call a contact**

**Actions:** Open the contact \-\> tap the phone number (or the call icon beside it); the dialler is opened with the number.

**16\. Send an SMS to a contact**

**Actions:** Open the contact \-\> tap the message icon beside the phone number \-\> the messaging app opens with the recipient filled in.

**17\. Send an email to a contact**

**Actions:** Open the contact \-\> tap the email address \-\> select the mail app \-\> compose and send.

**18\. Create a contact group**

**Actions:** Open the Groups tab \-\> tap the "+" button \-\> enter the group name \-\> tap OK.

**19\. Add contacts to a group**

**Actions:** Open the Groups tab \-\> tap the group \-\> tap the "+"/add-members action \-\> tick the contacts \-\> confirm.

**20\. Rename or delete a group**

**Actions:** Open the Groups tab \-\> long-press the group \-\> tap Rename and enter the new name, or tap Delete and confirm.

**21\. Send a message or email to a whole group**

**Actions:** Open the Groups tab \-\> tap the group \-\> tap the overflow menu \-\> tap "Send SMS to group"/"Send email to group" \-\> confirm the recipients.

**22\. Search contacts**

**Actions:** Tap the search icon in the toolbar \-\> type the name, number or email fragment \-\> tap a matching contact.

**23\. Sort the contact list**

**Actions:** Tap the overflow menu \-\> tap "Sort by" \-\> choose first name, middle name, surname or date created \-\> choose ascending or descending \-\> tap OK.

**24\. Filter which contact sources are shown**

**Actions:** Tap the overflow menu \-\> tap "Filter contacts by source"/"Manage shown contact fields" \-\> tick the accounts to display \-\> tap OK.

**25\. Choose which fields are visible in the contact detail**

**Actions:** Open Settings \-\> tap "Manage shown contact fields" \-\> tick the fields (for example prefix, phone numbers, emails, addresses, IM, events, notes, organisation, groups, websites) \-\> tap OK.

**26\. Show only contacts with phone numbers**

**Actions:** Open Settings \-\> toggle the "Show only contacts with phone numbers" option.

**27\. Merge duplicate contacts**

**Actions:** Open the contact list \-\> long-press the contacts to select them \-\> tap the overflow menu \-\> tap "Merge"/the merge action \-\> confirm; the details are combined into one entry.

**28\. Share a contact as a vCard**

**Actions:** Open the contact \-\> tap the share icon \-\> choose the destination app; or long-press several contacts and use the share action to send them together.

**29\. Export contacts to a vCard (.vcf) file**

**Actions:** Open Settings (or the overflow menu) \-\> tap "Export contacts" \-\> choose the accounts to include \-\> choose the destination file name and folder \-\> confirm.

**30\. Import contacts from a vCard file**

**Actions:** Open Settings (or the overflow menu) \-\> tap "Import contacts" \-\> select the .vcf file \-\> choose the target account \-\> confirm.

**31\. Create a home screen shortcut to a contact**

**Actions:** Open the contact \-\> tap the overflow menu \-\> tap "Create shortcut" \-\> confirm the placement on the Android home screen.

**32\. Choose the default tab shown at start-up**

**Actions:** Open Settings \-\> tap the "Default tab" entry \-\> choose Contacts, Favourites, Groups or "Last used" \-\> confirm.

**33\. Show or hide the individual tabs**

**Actions:** Open Settings \-\> open the tabs section \-\> tick the tabs (Contacts, Favourites, Groups) to keep visible \-\> confirm.

**34\. Customise the app colours and theme**

**Actions:** Open Settings \-\> tap "Customise colours" \-\> choose a preset theme or set the text, background, primary and app-icon colours \-\> tap the tick to save.

**35\. Protect the app with a PIN, pattern or fingerprint**

**Actions:** Open Settings \-\> tap the app-lock entry \-\> choose the lock type \-\> set the secret \-\> confirm.

**36\. Change the app language and font size**

**Actions:** Open Settings \-\> tap the Language entry and pick the language \-\> tap the font size entry and choose the size.

**37\. Show contact thumbnails and phone numbers in the list**

**Actions:** Open Settings \-\> toggle the "Show contact thumbnails" and "Show phone numbers" options.

**38\. View the about screen, FAQ and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the FAQ, the version, the licences and the source repository link.

 

## **Category: Media**

### **App Name: VLC**

*Package: org.videolan.vlc  |  Version documented: 3.7.1  |  Reference: Official VideoLAN documentation and in-app menus*

**Features:**

**1\. Browse the video library**

**Actions:** Open the app \-\> tap the Video tab \-\> wait for the media library scan \-\> scroll the thumbnails \-\> tap a video to play it.

**2\. Browse the audio library**

**Actions:** Open the app \-\> tap the Audio tab \-\> switch between the Artists, Albums, Tracks, Genres and Playlists sub-tabs \-\> tap an item to open or play it.

**3\. Browse device folders and storage**

**Actions:** Open the "Browse" tab \-\> tap the internal storage or SD card entry \-\> navigate the folders \-\> tap a media file to play it.

**4\. Browse network shares**

**Actions:** Open the "Browse" tab \-\> under Local Network tap a discovered server (UPnP/DLNA, SMB, FTP, SFTP or NFS) \-\> enter credentials if prompted \-\> browse and tap a file to play it.

**5\. Add a network share manually**

**Actions:** Open the Browse tab \-\> tap the "+"/"New network share" action \-\> choose the protocol \-\> enter the server address, port, path and credentials \-\> tap Save; the share appears in the favourites list.

**6\. Open a network stream from a URL**

**Actions:** Open the navigation drawer (hamburger icon) \-\> tap "New stream"/"Open network stream" \-\> paste the stream URL \-\> tap the play/go button.

**7\. Mark a folder or share as a favourite**

**Actions:** Open the Browse tab \-\> long-press the folder or server \-\> tap the favourite (star/heart) action; it appears at the top of the Browse screen.

**8\. Search the media library**

**Actions:** Tap the search icon in the toolbar \-\> type the title, artist or album \-\> tap a result to play it.

**9\. Sort the media lists**

**Actions:** Open a library tab \-\> tap the sort icon (or the overflow menu \-\> Sort by) \-\> choose the field (name, length, date, artist, album, file size) \-\> tap again to reverse the direction.

**10\. Switch between list and grid display**

**Actions:** Open a library tab \-\> tap the overflow menu (three dots) \-\> tap the display/"List or grid" toggle.

**11\. Resume playback where you left off**

**Actions:** Reopen a partially watched video \-\> tap it \-\> choose "Resume" in the prompt (or set the automatic behaviour in Settings \-\> Video \-\> Resume playback).

**12\. Control video playback**

**Actions:** Start a video \-\> tap the screen to show the controls \-\> use play/pause, the seek bar and the skip buttons \-\> tap the lock icon to lock the controls.

**13\. Use gesture controls for volume, brightness and seeking**

**Actions:** During playback \-\> swipe vertically on the right half for volume \-\> swipe vertically on the left half for brightness \-\> swipe horizontally to seek \-\> the change is shown as an overlay.

**14\. Select an audio track**

**Actions:** Start playback \-\> tap the screen \-\> tap the audio track icon (or the overflow menu \-\> Audio track) \-\> choose the track or disable audio.

**15\. Load and select subtitles**

**Actions:** Start playback \-\> tap the subtitle icon \-\> choose an embedded subtitle track, or tap "Select subtitle file" and pick a local file.

**16\. Download subtitles**

**Actions:** Long-press a video in the library (or open the player overflow menu) \-\> tap "Download subtitles" \-\> choose the language \-\> select the matching result to download and apply it.

**17\. Adjust the subtitle delay**

**Actions:** During playback \-\> tap the overflow menu in the player \-\> tap "Subtitle delay" \-\> use the plus/minus controls to shift the subtitles \-\> tap outside to close.

**18\. Adjust the audio delay**

**Actions:** During playback \-\> tap the player overflow menu \-\> tap "Audio delay" \-\> shift the audio with the plus/minus controls.

**19\. Change the playback speed**

**Actions:** During playback \-\> tap the player overflow menu \-\> tap "Playback speed" \-\> drag the slider or use the preset buttons \-\> tap outside to close.

**20\. Change the aspect ratio, crop and zoom**

**Actions:** During playback \-\> tap the aspect-ratio/size icon repeatedly to cycle through the modes (best fit, fit screen, fill, 16:9, 4:3, original), or open the player overflow menu \-\> tap the video size entry.

**21\. Lock the screen orientation**

**Actions:** During playback \-\> tap the player overflow menu \-\> tap the orientation lock icon \-\> choose the orientation (sensor, portrait, landscape or locked to the current one).

**22\. Jump to a specific time**

**Actions:** During playback \-\> tap the player overflow menu \-\> tap "Jump to time" \-\> enter the timestamp \-\> tap OK.

**23\. Set an A-B repeat loop**

**Actions:** During playback \-\> tap the player overflow menu \-\> tap the A-B repeat control \-\> tap once to set point A and again to set point B; the segment repeats until you clear it.

**24\. Play video in picture-in-picture / a floating window**

**Actions:** During playback \-\> tap the player overflow menu \-\> tap "Picture in picture"/the popup icon \-\> grant the permission if prompted \-\> drag the floating window to reposition it.

**25\. Play a video as audio only (background playback)**

**Actions:** During playback \-\> tap the player overflow menu \-\> tap "Play as audio"; or long-press a video in the library \-\> tap "Play as audio". Playback continues in the notification.

**26\. Use the equaliser**

**Actions:** Open the navigation drawer \-\> tap "Equalizer" \-\> toggle it on \-\> choose a preset or drag the band sliders \-\> set the pre-amp \-\> the setting applies to the current playback.

**27\. Set a sleep timer**

**Actions:** Open the audio player and expand it (or open the drawer \-\> Sleep timer) \-\> tap the sleep timer entry \-\> pick the time \-\> confirm; playback stops at that moment.

**28\. Adjust video filters (brightness, contrast, hue, saturation, gamma)**

**Actions:** During video playback \-\> tap the player overflow menu \-\> tap the "Video filters"/adjustment entry \-\> enable it \-\> drag the sliders \-\> close the panel.

**29\. Cast to a renderer (Chromecast or DLNA)**

**Actions:** Ensure the device is on the same network \-\> tap the cast icon in the toolbar or in the player \-\> select the renderer from the list \-\> playback moves to that device \-\> tap the icon again and choose "Local" to bring it back.

**30\. Create a playlist**

**Actions:** Open the Audio tab \-\> Playlists \-\> tap the "+"/new playlist action \-\> enter the playlist name \-\> select the tracks \-\> confirm; or long-press a track \-\> "Add to playlist" \-\> "New playlist".

**31\. Add media to an existing playlist**

**Actions:** Long-press a track, album or video \-\> tap "Add to playlist" \-\> select the playlist.

**32\. Manage the play queue**

**Actions:** Start playback \-\> expand the player \-\> tap the playlist/queue icon \-\> drag items to reorder them \-\> swipe an item away to remove it \-\> tap the clear action to empty the queue.

**33\. Use repeat and shuffle**

**Actions:** Expand the player \-\> tap the repeat icon to cycle off/repeat all/repeat one \-\> tap the shuffle icon to toggle random playback.

**34\. Add media to the queue without interrupting playback**

**Actions:** Long-press a track or video \-\> tap "Append"/"Add to queue" \-\> the item is placed at the end of the current queue; use "Play next" to insert it after the current item.

**35\. View media information**

**Actions:** Long-press a media item \-\> tap "Information" \-\> read the file path, size, duration, resolution, codecs and track list.

**36\. Delete a media file from the device**

**Actions:** Long-press the item in the library \-\> tap the delete action \-\> confirm.

**37\. Share a media file**

**Actions:** Long-press the item \-\> tap the share action \-\> choose the target app in the Android share sheet.

**38\. View the playback history**

**Actions:** Open the navigation drawer \-\> tap "History" \-\> tap an entry to resume it \-\> use the clear action to empty the history.

**39\. Choose which folders the media library scans**

**Actions:** Open Settings \-\> tap "Media library"/"Directories" \-\> tick the folders to include and untick the ones to skip \-\> tap the refresh/rescan action.

**40\. Force a media library rescan**

**Actions:** Open Settings \-\> Media library \-\> tap "Rescan"/"Reset the media library" \-\> confirm; the library is rebuilt.

**41\. Configure video playback settings**

**Actions:** Open Settings \-\> tap "Video" \-\> set the resume behaviour, the hardware acceleration mode, the default video aspect, the screen orientation, the brightness handling and whether the video is played in the background.

**42\. Configure audio playback settings**

**Actions:** Open Settings \-\> tap "Audio" \-\> set the audio output mode, digital audio passthrough, the resume behaviour, the headphone behaviour and the audio-focus handling.

**43\. Configure subtitle appearance**

**Actions:** Open Settings \-\> tap "Subtitles" \-\> set the preferred subtitle language, the text encoding, the font size, the colour, the background and the bold option.

**44\. Change the interface settings**

**Actions:** Open Settings \-\> tap "Interface" \-\> set the app theme (light, dark or system), the daily-night switch, the start-up screen, the visible tabs, the interface language and whether the TV interface is used.

**45\. Add the VLC home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find VLC \-\> drag the widget onto the home screen \-\> configure the size and theme \-\> confirm; use it to control playback without opening the app.

**46\. View the about screen and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the version, the build information, the authors and the licence.

 

### **App Name: Auxio**

*Package: org.oxycblt.auxio  |  Version documented: 4.1.5  |  Reference: Official Auxio repository documentation and F-Droid listing*

**Features:**

**1\. Browse the music library by songs**

**Actions:** Open the app \-\> tap the Songs tab in the home screen \-\> scroll the alphabetically indexed list \-\> tap a song to start playback.

**2\. Browse by album**

**Actions:** Open the Albums tab \-\> scroll or use the fast-scroll index \-\> tap an album to open its detail page with the track list.

**3\. Browse by artist**

**Actions:** Open the Artists tab \-\> tap an artist \-\> review their albums and songs on the artist detail page.

**4\. Browse by genre**

**Actions:** Open the Genres tab \-\> tap a genre \-\> review the artists, albums and songs in it.

**5\. Browse by playlist**

**Actions:** Open the Playlists tab \-\> tap a playlist to open it \-\> tap a track to play it from that playlist.

**6\. Play a song**

**Actions:** Tap any song in a list \-\> playback begins and the bottom playback bar appears \-\> tap the bar to expand the full player.

**7\. Control playback from the expanded player**

**Actions:** Tap the playback bar to expand it \-\> use play/pause, previous, next and the seek bar \-\> tap the cover art or swipe down to collapse it.

**8\. Use repeat and shuffle**

**Actions:** Expand the player \-\> tap the repeat icon to cycle through off, repeat all and repeat one \-\> tap the shuffle icon to toggle shuffled playback.

**9\. Shuffle the whole library**

**Actions:** Open the home screen \-\> tap the shuffle action in the toolbar (or the shuffle floating button) \-\> the entire library is queued in random order.

**10\. View and edit the play queue**

**Actions:** Expand the player \-\> tap the queue icon \-\> drag the handle beside an item to reorder it \-\> swipe an item away to remove it.

**11\. Add a song, album or artist to the queue**

**Actions:** Long-press the item (or tap its overflow menu) \-\> tap "Play next" to insert it after the current track, or "Add to queue" to append it.

**12\. Create a playlist**

**Actions:** Open the Playlists tab \-\> tap the "+"/new playlist action \-\> enter the playlist name \-\> select the songs to add \-\> confirm.

**13\. Add songs to an existing playlist**

**Actions:** Long-press a song, album, artist or genre \-\> tap "Add to playlist" \-\> select the target playlist (or create a new one).

**14\. Rename, reorder or delete a playlist**

**Actions:** Open the Playlists tab \-\> open the playlist \-\> tap the overflow menu \-\> tap Rename and enter the new name, tap the edit action to drag the tracks into a new order, or tap Delete and confirm.

**15\. Import a playlist from an M3U file**

**Actions:** Open the Playlists tab \-\> tap the overflow menu \-\> tap the import option \-\> select the .m3u/.m3u8 file \-\> confirm; the referenced songs are matched against the library.

**16\. Export a playlist to an M3U file**

**Actions:** Open the playlist \-\> tap the overflow menu \-\> tap the export option \-\> choose the destination and the path format \-\> confirm.

**17\. Search the library**

**Actions:** Tap the search icon in the toolbar \-\> type the query \-\> filter the results by type using the chips \-\> tap a result to play or open it.

**18\. Sort a list**

**Actions:** Open any library tab or detail page \-\> tap the sort icon in the toolbar \-\> choose the sort field (for example name, artist, album, year, duration, date added or track number) \-\> choose ascending or descending.

**19\. View song details and file information**

**Actions:** Long-press a song \-\> tap "Song properties"/details \-\> read the title, artist, album, track number, disc, year, genre, format, bitrate, sample rate and file path.

**20\. Jump from a song to its album or artist**

**Actions:** Long-press a song (or open the player overflow menu) \-\> tap "Go to album" or "Go to artist" \-\> the corresponding detail page opens.

**21\. Share a song**

**Actions:** Long-press the song \-\> tap the share action \-\> choose the destination app in the Android share sheet.

**22\. Configure which folders are scanned**

**Actions:** Open Settings \-\> tap "Music"/the music folders entry \-\> add folders to the include or exclude list \-\> tap the rescan action to rebuild the library.

**23\. Rescan the music library**

**Actions:** Open Settings \-\> tap the "Rescan music library" action (or pull down to refresh on the home screen) \-\> wait for the indexing notification to finish.

**24\. Configure how multi-value tags are separated**

**Actions:** Open Settings \-\> Music \-\> tap the separators entry \-\> select the characters (for example comma, semicolon, slash, plus, ampersand) used to split artist and genre tags \-\> confirm.

**25\. Enable or disable ReplayGain**

**Actions:** Open Settings \-\> tap "Audio"/playback \-\> tap the ReplayGain entry \-\> choose the mode (off, track, album, or dynamic) \-\> optionally set the pre-amp values for tracks with and without ReplayGain data.

**26\. Open the system equaliser**

**Actions:** Open Settings \-\> tap the equaliser entry (or the equaliser action in the player overflow menu) \-\> the system audio effects panel opens \-\> adjust the bands \-\> return.

**27\. Configure headset and audio focus behaviour**

**Actions:** Open Settings \-\> Audio \-\> toggle whether playback resumes when headphones are plugged in, whether playback pauses on focus loss and whether playback pauses when a song is repeated.

**28\. Choose what the playback bar and notification show**

**Actions:** Open Settings \-\> open the personalisation/UI section \-\> set the cover art behaviour, the round-mode option and the information shown in the notification.

**29\. Change the theme and accent colour**

**Actions:** Open Settings \-\> tap "Personalise"/Appearance \-\> choose the theme (light, dark, system) \-\> enable the black theme for dark mode \-\> select the accent colour or enable Material You dynamic colours.

**30\. Choose which library tabs are visible and their order**

**Actions:** Open Settings \-\> Personalise \-\> tap the tabs/home entry \-\> tick the tabs to show (Songs, Albums, Artists, Genres, Playlists) \-\> drag them into the required order \-\> confirm.

**31\. Set the playback behaviour when selecting a song**

**Actions:** Open Settings \-\> open the playback section \-\> choose whether tapping a song plays from the whole library, the current list, the album or the artist \-\> confirm.

**32\. Add the Auxio home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Auxio \-\> drag the widget onto the home screen \-\> resize it to reveal the additional controls.

**33\. Save and restore the playback state**

**Actions:** Open Settings \-\> use the "Save playback state" and "Restore playback state"/wipe actions in the playback section \-\> confirm; the queue and position are stored so playback resumes after a restart.

**34\. View the about screen and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the version, the song/album/artist counts, the source link and the open-source licences.

 

### **App Name: Fossify Music Player**

*Package: org.fossify.musicplayer  |  Version documented: 1.8.1  |  Reference: Official Fossify repository documentation and F-Droid listing*

**Features:**

**1\. Browse tracks**

**Actions:** Open the app \-\> grant the media permission \-\> tap the Tracks tab \-\> scroll the list \-\> tap a track to play it.

**2\. Browse albums**

**Actions:** Open the Albums tab \-\> scroll the album grid or list \-\> tap an album to see its track list \-\> tap a track to play.

**3\. Browse artists**

**Actions:** Open the Artists tab \-\> tap an artist \-\> review their albums \-\> tap an album or track to play.

**4\. Browse genres**

**Actions:** Open the Genres tab \-\> tap a genre \-\> review the tracks in it \-\> tap one to play.

**5\. Browse folders**

**Actions:** Open the Folders tab \-\> tap a folder \-\> review the audio files it contains \-\> tap a file to play it.

**6\. Browse and open playlists**

**Actions:** Open the Playlists tab \-\> tap a playlist \-\> review its tracks \-\> tap a track to start playback from that playlist.

**7\. Create a playlist**

**Actions:** Open the Playlists tab \-\> tap the "+" floating action button \-\> enter the playlist name \-\> tap OK \-\> add tracks to it.

**8\. Add tracks to a playlist**

**Actions:** Long-press a track, album, artist, genre or folder \-\> tap "Add to playlist" \-\> select the target playlist (or create a new one) \-\> confirm.

**9\. Remove a track from a playlist**

**Actions:** Open the playlist \-\> long-press the track \-\> tap "Remove from playlist" \-\> confirm.

**10\. Rename or delete a playlist**

**Actions:** Open the Playlists tab \-\> long-press the playlist \-\> tap Rename and enter the new name, or tap Delete and confirm.

**11\. Control playback**

**Actions:** Start a track \-\> tap the playback bar at the bottom to open the full player \-\> use play/pause, previous, next and the seek bar \-\> tap the back arrow to collapse.

**12\. Use shuffle and repeat**

**Actions:** Open the full player \-\> tap the shuffle icon to toggle random order \-\> tap the repeat icon to cycle through repeat off, repeat all and repeat one track.

**13\. Change the playback speed**

**Actions:** Open the full player \-\> tap the playback speed control \-\> drag the slider or use the preset buttons \-\> tap outside to close.

**14\. Open the equaliser**

**Actions:** Open the full player \-\> tap the equaliser icon (or the overflow menu \-\> Equalizer) \-\> choose a preset or drag the band sliders \-\> tap the back arrow to apply.

**15\. Set a sleep timer**

**Actions:** Open the full player or the overflow menu \-\> tap "Sleep timer" \-\> select the duration (or set a custom value) \-\> confirm; playback stops when the timer expires.

**16\. View and manage the play queue**

**Actions:** Open the full player \-\> tap the queue icon \-\> drag the handle to reorder items \-\> swipe an item away to remove it \-\> tap a track to jump to it.

**17\. Add tracks to the current queue**

**Actions:** Long-press a track or album \-\> tap "Add to queue"/"Play next" \-\> the items are added to the queue without stopping the current track.

**18\. Search the library**

**Actions:** Tap the search icon in the toolbar \-\> type the track, album or artist name \-\> tap a result to play it.

**19\. Sort the lists**

**Actions:** Open a tab \-\> tap the overflow menu (three dots) \-\> tap "Sort by" \-\> choose the field (title, artist, album, duration, date added or track number) and the direction \-\> tap OK.

**20\. Edit track metadata**

**Actions:** Long-press a track \-\> tap the overflow menu \-\> tap "Edit"/Properties edit \-\> change the title, artist, album, track number or year \-\> tap Save.

**21\. View track properties**

**Actions:** Long-press a track \-\> tap "Properties" \-\> read the file name, path, size, duration, format and last-modified date.

**22\. Delete a track from the device**

**Actions:** Long-press the track \-\> tap the delete (bin) icon \-\> confirm; the file is removed (or moved to the recycle bin if enabled).

**23\. Share a track**

**Actions:** Long-press the track \-\> tap the share icon \-\> choose the destination app.

**24\. Exclude folders from the library**

**Actions:** Long-press a folder in the Folders tab \-\> tap "Exclude folder"; or open Settings \-\> "Manage excluded folders" \-\> add or remove folders \-\> confirm.

**25\. Control playback from the notification and the lock screen**

**Actions:** Start playback \-\> pull down the notification shade (or wake the lock screen) \-\> use the play/pause, previous, next and close controls shown there.

**26\. Add the music player home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Fossify Music Player \-\> drag the widget onto the home screen \-\> set the background colour and transparency \-\> tap OK.

**27\. Show or hide the individual library tabs**

**Actions:** Open Settings \-\> open the tabs section \-\> tick the tabs to display (Playlists, Folders, Artists, Albums, Tracks, Genres) \-\> confirm.

**28\. Customise the app colours and theme**

**Actions:** Open Settings \-\> tap "Customise colours" \-\> choose a preset theme or set the text, background, primary and app-icon colours \-\> tap the tick to save.

**29\. Configure playback behaviour**

**Actions:** Open Settings \-\> open the playback section \-\> toggle options such as gapless-style auto-advance, whether playback resumes on headset connection, whether the album cover is shown on the lock screen and the swipe gesture behaviour.

**30\. Configure the recycle bin for deleted tracks**

**Actions:** Open Settings \-\> toggle "Move deleted files into the recycle bin" \-\> use the recycle bin entry later to restore or permanently delete them.

**31\. Protect the app with a PIN, pattern or fingerprint**

**Actions:** Open Settings \-\> tap the app-lock entry \-\> choose the lock type \-\> set the secret \-\> confirm.

**32\. Change the app language and font size**

**Actions:** Open Settings \-\> tap the Language entry and pick the language \-\> tap the font size entry and choose the size.

**33\. View the about screen, FAQ and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the FAQ, the version number, the licences and the source repository link.

 

### **App Name: RadioDroid**

*Package: net.programmierecke.radiodroid2  |  Version documented: 0.86  |  Reference: Official RadioDroid repository documentation and F-Droid listing*

**Features:**

**1\. Browse popular radio stations**

**Actions:** Open the app \-\> open the "Stations" screen \-\> switch between the sub-lists (for example most popular/top clicked, top voted, trending/recently clicked and recently changed) \-\> tap a station to play it.

**2\. Search for a station by name**

**Actions:** Tap the search icon in the toolbar \-\> type the station name \-\> tap the search key \-\> tap a result to play it.

**3\. Search stations by tag, country, language or state**

**Actions:** Open the search screen \-\> switch to the advanced/category search \-\> choose the tag, country, state, language, codec or minimum bitrate criteria \-\> run the search \-\> tap a station.

**4\. Play a station**

**Actions:** Tap the station in any list \-\> playback starts and the player bar appears at the bottom \-\> tap the bar to expand the full player.

**5\. Stop playback**

**Actions:** Tap the stop control in the player bar, the expanded player or the notification.

**6\. Add a station to favourites**

**Actions:** Long-press the station in a list (or open its detail page) \-\> tap the star/"Add to favourites" action; the station appears in the Favourites/Starred screen.

**7\. Remove a station from favourites**

**Actions:** Open the Favourites screen \-\> long-press the station \-\> tap the remove/unstar action \-\> confirm.

**8\. Reorder favourite stations**

**Actions:** Open the Favourites screen \-\> long-press a station \-\> drag it to the new position \-\> release.

**9\. View station details**

**Actions:** Tap a station \-\> open its detail page \-\> read the bitrate, codec, country, language, tags, click and vote counts, and the homepage link.

**10\. Vote for a station**

**Actions:** Open the station detail page \-\> tap the vote/thumbs-up action; the vote is sent to the radio-browser directory.

**11\. Open a station's homepage**

**Actions:** Open the station detail page \-\> tap the homepage/website link \-\> the page opens in the browser.

**12\. Share a station**

**Actions:** Long-press the station (or open its detail page) \-\> tap the share action \-\> choose whether to share the stream URL or the station page \-\> pick the target app.

**13\. Record the stream to a file**

**Actions:** Start playing a station \-\> tap the record button in the player (or the overflow menu \-\> Record) \-\> the stream is written to the configured recordings folder \-\> tap the record button again to stop.

**14\. Browse and play saved recordings**

**Actions:** Open the navigation drawer \-\> tap "Recordings" \-\> tap a recording to play it \-\> long-press to rename, share or delete it.

**15\. View the played-track history**

**Actions:** Open the navigation drawer \-\> tap "History"/the track history \-\> review the songs reported by the stations you have listened to \-\> tap an entry to search for it.

**16\. Set a sleep timer**

**Actions:** Open the expanded player or the overflow menu \-\> tap "Sleep timer" \-\> set the duration \-\> confirm; playback stops when the timer runs out.

**17\. Set a radio alarm clock**

**Actions:** Open the navigation drawer \-\> tap "Alarm" \-\> tap the "+"/add action \-\> pick the time \-\> select the station to wake up to \-\> choose the repeat days \-\> set the volume ramp options \-\> tap Save.

**18\. Enable, edit or delete an alarm**

**Actions:** Open the Alarm screen \-\> toggle the switch to enable or disable an alarm \-\> tap it to change the time, station or repeat days \-\> long-press to delete it.

**19\. Import favourite stations from an M3U file**

**Actions:** Open the navigation drawer or the Favourites overflow menu \-\> tap the import option \-\> select the .m3u file \-\> confirm; the stations are added to the favourites.

**20\. Export favourite stations to an M3U file**

**Actions:** Open the Favourites screen \-\> tap the overflow menu \-\> tap the export option \-\> choose the destination \-\> confirm.

**21\. Cast a station to a Chromecast device**

**Actions:** Ensure the phone and the Chromecast are on the same network \-\> tap the cast icon in the toolbar \-\> select the device \-\> playback moves to it.

**22\. Send playback to an MPD server**

**Actions:** Open Settings \-\> open the MPD section \-\> add the server address and port \-\> confirm \-\> then use the MPD action in the player or the overflow menu to send the current station to that server.

**23\. Control playback from the notification**

**Actions:** Start a station \-\> pull down the notification shade \-\> use the play/stop and record controls displayed there.

**24\. Choose the media player engine**

**Actions:** Open Settings \-\> tap the player/playback section \-\> choose between the system MediaPlayer and ExoPlayer \-\> confirm.

**25\. Adjust the streaming buffer and resume behaviour**

**Actions:** Open Settings \-\> playback section \-\> set the buffer size and the automatic reconnect/resume behaviour after a network interruption.

**26\. Set the recordings folder and naming**

**Actions:** Open Settings \-\> open the recordings section \-\> choose the destination directory \-\> set the file naming scheme \-\> confirm.

**27\. Restrict playback or downloads to Wi-Fi**

**Actions:** Open Settings \-\> find the network/metered connection option \-\> enable the Wi-Fi-only behaviour \-\> confirm.

**28\. Change the theme**

**Actions:** Open Settings \-\> tap the theme entry \-\> choose the light, dark or black theme \-\> return.

**29\. Change the station list layout and icon display**

**Actions:** Open Settings \-\> open the appearance section \-\> toggle whether station icons are loaded, and choose the list or grid layout \-\> confirm.

**30\. Select the radio-browser server or mirror**

**Actions:** Open Settings \-\> open the server/advanced section \-\> choose the automatic server selection or enter a specific radio-browser mirror \-\> confirm.

**31\. Add the home screen shortcut for a station**

**Actions:** Long-press a station \-\> tap the shortcut action (where available) \-\> confirm the placement on the Android home screen.

**32\. View the about screen and licences**

**Actions:** Open the navigation drawer \-\> tap "About" \-\> read the version, the credits, the licence and the radio-browser attribution.

 

### **App Name: Transistor**

*Package: org.y20k.transistor  |  Version documented: 4.3.8  |  Reference: Official Transistor repository documentation and F-Droid listing*

*Note: Transistor is deliberately minimal and has no station discovery feed; stations are added by search, playlist address or raw stream address.*

**Features:**

**1\. Add a station by searching the radio-browser directory**

**Actions:** Open the app \-\> tap the "+" icon in the top bar \-\> tap the search option \-\> type the station name \-\> tap a result from the radio-browser.info list \-\> confirm to add it to the collection.

**2\. Add a station from an M3U or PLS playlist address**

**Actions:** Tap the "+" icon in the top bar \-\> paste the playlist file address (.m3u or .pls) into the input field \-\> tap the add/confirm button; the station name and image are read from the playlist.

**3\. Add a station from a raw stream address**

**Actions:** Tap the "+" icon \-\> paste the direct stream URL (MP3, AAC or Ogg/Opus) \-\> tap the add button; note that stations added this way cannot use the update feature.

**4\. Add a station by opening a stream file in the browser**

**Actions:** In a web browser tap a .m3u or .pls link \-\> choose Transistor in the "Open with" chooser (or set it as the default handler for those file types) \-\> confirm the import.

**5\. Play a station**

**Actions:** Open the station list \-\> tap the station (or its play button) \-\> the stream starts and the player sheet appears at the bottom.

**6\. Stop playback**

**Actions:** Tap the stop button in the player sheet or in the notification, or disconnect the headphones according to the configured behaviour.

**7\. View the now-playing metadata**

**Actions:** Start a station \-\> expand the player sheet \-\> read the station name and the currently reported track title where the stream provides it.

**8\. Delete a station**

**Actions:** Open the station list \-\> swipe the station row sideways \-\> the station is removed from the collection.

**9\. Enable station editing**

**Actions:** Open Settings \-\> toggle the "Edit stations" option on \-\> return to the station list.

**10\. Rename a station**

**Actions:** With editing enabled \-\> tap and hold the station in the list \-\> tap the rename/edit name option \-\> enter the new name \-\> confirm.

**11\. Change a station's image**

**Actions:** With editing enabled \-\> tap and hold the station \-\> tap the image option \-\> pick an image from the device \-\> confirm; the custom icon replaces the default one.

**12\. Change a station's stream address**

**Actions:** With editing enabled \-\> tap and hold the station \-\> tap the stream URI/edit option \-\> enter the new address \-\> confirm.

**13\. Update station information from the source**

**Actions:** Open the overflow/settings menu \-\> tap the "Update station information" action \-\> Transistor re-reads the playlist source to refresh the stream address, name and image (this does not work for stations added by raw stream address).

**14\. Reorder stations in the list**

**Actions:** Open the station list \-\> tap and hold a station \-\> drag it to the required position \-\> release.

**15\. Set a sleep timer**

**Actions:** Start playback \-\> open the player sheet \-\> tap the sleep timer icon \-\> the timer starts counting down \-\> tap it again to cancel or extend it.

**16\. Control playback from the notification**

**Actions:** Start a station \-\> pull down the notification shade \-\> use the play/stop control shown in the media notification.

**17\. Add a home screen shortcut for a station**

**Actions:** Open the station list \-\> tap and hold the station \-\> tap the "Add shortcut"/place on home screen action \-\> confirm; tapping the shortcut starts that station directly.

**18\. Import stations by copying M3U files into the collection folder**

**Actions:** Connect the device to a computer (or use a file manager) \-\> place the .m3u files into /Android/data/org.y20k.transistor/files/Collection \-\> reopen the app; the stations appear in the list.

**19\. Back up and restore the station collection**

**Actions:** Copy the Collection folder from /Android/data/org.y20k.transistor/files/ to a safe location; restore it by copying the folder back before opening the app. On devices with Android auto-backup enabled the collection is backed up with the account automatically.

**20\. Choose the playback behaviour on Bluetooth/headphone disconnect**

**Actions:** Open Settings \-\> find the playback behaviour options \-\> set whether playback stops when the audio device is disconnected \-\> return.

**21\. Change the theme**

**Actions:** Open Settings \-\> tap the theme/appearance entry \-\> choose light, dark or the system default \-\> return.

**22\. Delete all stations (reset the collection)**

**Actions:** Open Settings \-\> find the collection/clear action \-\> confirm; all stations are removed from the list.

**23\. View the about screen and licence information**

**Actions:** Open Settings \-\> scroll to the About section \-\> read the app version, the radio-browser.info attribution and the MIT licence information.

 

## **Category: Security and utility**

### **App Name: Aegis Authenticator**

*Package: com.beemdevelopment.aegis  |  Version documented: 3.4.2  |  Reference: Official Aegis repository documentation and F-Droid listing*

**Features:**

**1\. Create and encrypt the vault on first launch**

**Actions:** Install and open the app \-\> tap through the welcome screens \-\> choose to protect the vault with a password \-\> enter the password twice \-\> tap Next \-\> optionally enable biometric unlock \-\> tap Finish.

**2\. Unlock the vault with a password**

**Actions:** Open the app \-\> type the vault password in the unlock screen \-\> tap the unlock button.

**3\. Unlock the vault with biometrics**

**Actions:** Open Settings \-\> Security \-\> enable biometric unlock and authenticate \-\> from then on, open the app and present the fingerprint (or face) at the unlock prompt.

**4\. Add an entry by scanning a QR code**

**Actions:** Tap the "+" floating action button \-\> tap "Scan a QR code" \-\> grant the camera permission \-\> point the camera at the QR code \-\> review the pre-filled details \-\> tap Save.

**5\. Add an entry from a QR code image**

**Actions:** Tap the "+" button \-\> tap "Scan an image"/"Scan image from gallery" \-\> select the picture containing the QR code \-\> confirm the parsed entry \-\> tap Save.

**6\. Add an entry manually**

**Actions:** Tap the "+" button \-\> tap "Enter manually" \-\> enter the issuer and the account name \-\> paste the shared secret \-\> choose the type (TOTP, HOTP, Steam, Yandex or mOTP) \-\> set the algorithm, digit count and period or counter \-\> tap Save.

**7\. Edit an entry**

**Actions:** Tap the entry in the list (or long-press it) \-\> tap the edit action \-\> change the issuer, name, note, icon, group or token parameters \-\> tap Save.

**8\. Set a custom icon for an entry**

**Actions:** Open the entry editor \-\> tap the icon placeholder \-\> choose to select an image from the device or pick one from an installed icon pack \-\> crop it \-\> tap Save.

**9\. Import an icon pack**

**Actions:** Open Settings \-\> tap "Icon packs" \-\> tap the import action \-\> select the icon pack archive \-\> confirm; the icons become available in the entry editor.

**10\. Copy a code to the clipboard**

**Actions:** Open the entry list \-\> tap the entry (or its copy icon) \-\> the current code is copied to the clipboard and a confirmation appears.

**11\. Reveal a hidden code**

**Actions:** With the "tap to reveal" option enabled \-\> tap the entry in the list \-\> the code is shown for the configured number of seconds before being hidden again.

**12\. Generate the next HOTP code**

**Actions:** Open the list \-\> find the counter-based entry \-\> tap the refresh/next-code button on that entry; the counter is incremented and the new code is displayed.

**13\. Search entries**

**Actions:** Tap the search icon in the toolbar \-\> type part of the issuer or account name \-\> the list filters as you type.

**14\. Sort the entry list**

**Actions:** Tap the overflow menu (three dots) \-\> tap "Sort" \-\> choose the order (custom/manual, alphabetical by issuer, alphabetical by account, or last used) \-\> confirm.

**15\. Reorder entries manually**

**Actions:** Set the sort order to custom \-\> long-press an entry \-\> drag it to its new position \-\> release.

**16\. Create a group**

**Actions:** Open the overflow menu \-\> tap "Manage groups" \-\> tap the "+"/add action \-\> enter the group name \-\> tap Save.

**17\. Assign an entry to a group**

**Actions:** Open the entry editor \-\> tap the group selector \-\> tick the group(s) \-\> confirm \-\> tap Save.

**18\. Filter the list by group**

**Actions:** Tap the group chip bar at the top of the list (or the filter icon) \-\> select the group \-\> only its entries are shown \-\> tap the "All" chip to clear the filter.

**19\. Rename or delete a group**

**Actions:** Open the overflow menu \-\> tap "Manage groups" \-\> tap the group \-\> tap Rename and enter the new name, or tap Delete and confirm.

**20\. Delete an entry**

**Actions:** Long-press the entry \-\> tap the delete (bin) icon in the contextual toolbar \-\> confirm.

**21\. Select and act on multiple entries**

**Actions:** Long-press the first entry \-\> tap the further entries to add them \-\> use the contextual toolbar to assign a group, delete or share/export them together.

**22\. Export the vault as an encrypted file**

**Actions:** Open Settings \-\> tap "Import and export" \-\> tap "Export" \-\> choose the encrypted format \-\> confirm the warning \-\> pick the destination file \-\> the encrypted JSON vault is written.

**23\. Export the vault in plain text or as HTML**

**Actions:** Open Settings \-\> Import and export \-\> tap Export \-\> choose the plain-text JSON or the HTML/QR-code output \-\> read and accept the security warning \-\> pick the destination.

**24\. Import a vault from Aegis or another authenticator**

**Actions:** Open Settings \-\> tap "Import and export" \-\> tap "Import from file" \-\> choose the source application format (for example Aegis, andOTP, FreeOTP, FreeOTP+, Authy, Google Authenticator, Microsoft Authenticator, 2FAS, Bitwarden, Steam, WinAuth or Duo) \-\> select the exported file \-\> enter its password if required \-\> confirm the entries to import.

**25\. Import entries by scanning a Google Authenticator transfer QR code**

**Actions:** Tap the "+" button \-\> tap "Scan a QR code" \-\> scan the export QR code produced by Google Authenticator \-\> review the batch of entries \-\> confirm the import.

**26\. Set or change the vault password**

**Actions:** Open Settings \-\> tap "Security" \-\> tap the password entry \-\> enter the current password \-\> enter the new password twice \-\> tap Save.

**27\. Add a second unlock method (password slot)**

**Actions:** Open Settings \-\> Security \-\> tap the credential/slot management entry \-\> add a biometric slot or an additional password slot \-\> authenticate to confirm.

**28\. Configure automatic locking**

**Actions:** Open Settings \-\> Security \-\> tap the auto-lock entry \-\> tick when the vault should lock (for example when the screen turns off, when the back button is pressed, when the app is minimised, or after a timeout) \-\> confirm.

**29\. Set the lock timeout**

**Actions:** Open Settings \-\> Security \-\> tap the timeout entry \-\> select the period of inactivity after which the vault relocks.

**30\. Block screenshots and screen recording**

**Actions:** Open Settings \-\> Security \-\> enable the "Secure screen"/screenshot-blocking option; the entry list no longer appears in screenshots or in the recent-apps preview.

**31\. Enable a panic trigger**

**Actions:** Install a compatible panic-trigger app \-\> open Settings \-\> Security \-\> enable the panic trigger and choose the response (for example lock the vault or wipe it) \-\> confirm.

**32\. Enable automatic backups to a folder**

**Actions:** Open Settings \-\> tap "Backups" \-\> enable the automatic backup option \-\> choose the destination folder \-\> set the number of backup versions to keep \-\> confirm.

**33\. Enable Android system backups**

**Actions:** Open Settings \-\> Backups \-\> enable the Android built-in backup option \-\> confirm the warning about where the data is stored.

**34\. Change the theme**

**Actions:** Open Settings \-\> tap "Appearance" \-\> tap the theme entry \-\> choose light, dark, AMOLED black or "follow system" \-\> return.

**35\. Change the accent colour and dynamic colours**

**Actions:** Open Settings \-\> Appearance \-\> tap the accent colour entry \-\> select the colour or enable the Material You dynamic colour option.

**36\. Change the entry list view mode**

**Actions:** Open Settings \-\> Appearance \-\> tap the view mode entry \-\> choose Normal, Compact or Small \-\> return; the list density changes accordingly.

**37\. Configure code display and copy behaviour**

**Actions:** Open Settings \-\> Appearance/Behaviour \-\> toggle "Tap to reveal", set the reveal duration, choose whether tapping copies the code, choose whether codes are grouped into digit blocks, and set whether the account name is shown.

**38\. Highlight the entry whose code is about to expire**

**Actions:** Open Settings \-\> Appearance \-\> enable the option that highlights entries or shows the expiry progress \-\> return to the list.

**39\. Change the app language**

**Actions:** Open Settings \-\> Appearance \-\> tap the Language entry \-\> select the interface language \-\> confirm.

**40\. View the about screen and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the version number, the source repository link, the licence and the credits.

 

### **App Name: KeePassDX**

*Package: com.kunzisoft.keepass.libre  |  Version documented: 4.4.5  |  Reference: Official KeePassDX documentation (keepassdx.com) and in-app menus*

**Features:**

**1\. Create a database**

**Actions:** Open the app \-\> tap the "+" icon (Create new database) \-\> give a name for the database \-\> give a file path/storage location and confirm it with the system file picker \-\> set the master password and/or select a key file \-\> tap the save button to create the .kdbx file.

**2\. Open an existing database**

**Actions:** Open the app \-\> tap "Open existing database"/the file browse icon \-\> select the .kdbx file through the file picker \-\> enter the master password \-\> tap the unlock button.

**3\. Unlock a database with a key file**

**Actions:** On the unlock screen \-\> tap the key file selector \-\> browse to and select the key file \-\> enter the password if the database also uses one \-\> tap unlock.

**4\. Unlock a database with a hardware key (challenge-response)**

**Actions:** On the unlock screen \-\> enable the hardware key option \-\> select the challenge-response method \-\> present the YubiKey over NFC or connect it by USB when prompted \-\> tap unlock.

**5\. Unlock with biometrics or the device credential**

**Actions:** Open Settings \-\> "Advanced unlock" \-\> enable biometric or device-credential unlock \-\> unlock the database once with the password and store the credential when prompted \-\> afterwards, present the fingerprint at the unlock screen.

**6\. Create an entry**

**Actions:** Open the database \-\> navigate to the target group \-\> tap the "+" floating action button \-\> tap "Add entry" \-\> enter the title, username, password and URL \-\> add notes \-\> tap the save (tick) button.

**7\. Generate a password**

**Actions:** Open the entry editor \-\> tap the generate (dice/refresh) icon beside the password field \-\> set the length and the character sets (upper case, lower case, digits, special characters, brackets, extended ASCII) \-\> tap the generate action \-\> tap Accept to insert it.

**8\. Add custom fields to an entry**

**Actions:** Open the entry editor \-\> scroll to the custom/extra fields section \-\> tap "Add field" \-\> enter the field name and value \-\> mark it protected if it should be hidden \-\> tap Save.

**9\. Add an attachment to an entry**

**Actions:** Open the entry editor \-\> tap the attachment (paper clip) action \-\> select the file from the picker \-\> confirm \-\> tap Save.

**10\. Download or open an attachment**

**Actions:** Open the entry \-\> tap the attachment name \-\> choose to open it or to download it to a folder \-\> confirm.

**11\. Set an expiration date on an entry**

**Actions:** Open the entry editor \-\> toggle the expiration option \-\> pick the date and time \-\> tap Save; expired entries are marked in the list.

**12\. Configure a one-time password (OTP) token for an entry**

**Actions:** Open the entry editor \-\> tap the OTP/token action \-\> choose to scan a QR code, paste an otpauth:// URI or enter the secret manually \-\> set the type (TOTP or HOTP), the algorithm, the digits and the period \-\> tap Save; the rotating code is then shown on the entry screen.

**13\. Copy a username or password to the clipboard**

**Actions:** Open the entry \-\> tap the copy icon beside the username or password field \-\> the value is placed on the clipboard and cleared automatically after the configured timeout.

**14\. Reveal a hidden password**

**Actions:** Open the entry \-\> tap the eye icon beside the password field to show it \-\> tap it again to hide it.

**15\. Open the entry URL in the browser**

**Actions:** Open the entry \-\> tap the URL field/the open-link action \-\> the address opens in the default browser.

**16\. Edit an entry**

**Actions:** Open the entry \-\> tap the edit (pencil) icon \-\> change the fields \-\> tap the save button.

**17\. View an entry's history**

**Actions:** Open the entry \-\> scroll to the history section (KDBX databases keep previous versions) \-\> tap a historic version to inspect it \-\> optionally restore it.

**18\. Duplicate an entry**

**Actions:** Long-press the entry in the list \-\> tap the copy/duplicate action \-\> choose the destination group \-\> confirm.

**19\. Move an entry to another group**

**Actions:** Long-press the entry \-\> tap the move action \-\> navigate to the destination group \-\> tap the paste/confirm button.

**20\. Delete an entry**

**Actions:** Long-press the entry \-\> tap the delete (bin) icon \-\> confirm; if the recycle bin is enabled the entry is moved there instead of being erased.

**21\. Create a group**

**Actions:** Open the database \-\> navigate to the parent group \-\> tap the "+" button \-\> tap "Add group" \-\> enter the group name \-\> choose an icon \-\> tap Save.

**22\. Edit, move or delete a group**

**Actions:** Long-press the group \-\> tap Edit to rename it or change its icon and notes, tap the move action to relocate it, or tap Delete and confirm.

**23\. Use the recycle bin**

**Actions:** Open the database settings and enable the recycle bin \-\> deleted entries and groups are moved into it \-\> open the recycle bin group to restore an item (move it back) or to delete it permanently.

**24\. Change an entry or group icon**

**Actions:** Open the entry or group editor \-\> tap the icon \-\> choose a standard KeePass icon or a custom icon added to the database \-\> confirm \-\> tap Save.

**25\. Search the database**

**Actions:** Open the unlocked database \-\> tap the search icon in the toolbar \-\> type the query \-\> review the matching entries \-\> tap one to open it.

**26\. Configure search behaviour**

**Actions:** Open Settings \-\> the search section \-\> choose which fields are searched (title, username, URL, notes, custom fields), whether the search is case sensitive and whether the recycle bin is included.

**27\. Sort the entry list**

**Actions:** Open a group \-\> tap the overflow menu (three dots) \-\> tap "Sort" \-\> choose the field (title, username, creation time, modification time or last access) and the direction \-\> optionally group entries before groups \-\> confirm.

**28\. Use the KeePassDX autofill service**

**Actions:** Open the Android system settings \-\> Passwords and accounts/Autofill service \-\> select KeePassDX \-\> return to any app with a login form \-\> tap the field \-\> choose the KeePassDX suggestion \-\> unlock the database \-\> pick the matching entry; the fields are filled automatically.

**29\. Use the Magikeyboard to type credentials**

**Actions:** Open Settings \-\> enable the Magikeyboard and add it in the Android keyboard settings \-\> open an app with a login form \-\> switch to the Magikeyboard \-\> unlock the database \-\> pick the entry \-\> tap the username and password keys to type them.

**30\. Save changes to the database**

**Actions:** Make the changes \-\> tap the save icon in the toolbar (or enable automatic saving in Settings) \-\> wait for the confirmation that the .kdbx file has been written.

**31\. Open a database in read-only mode**

**Actions:** On the unlock screen \-\> enable the read-only toggle before unlocking \-\> the database opens without allowing modifications.

**32\. Lock the database manually**

**Actions:** Tap the lock icon in the toolbar (or use the lock action in the notification) \-\> the database is closed and the unlock screen returns.

**33\. Configure automatic locking**

**Actions:** Open Settings \-\> the security/"App timeout" section \-\> set the inactivity timeout, whether the database locks when the screen turns off and whether it locks when the app is closed \-\> confirm.

**34\. Configure clipboard timeout**

**Actions:** Open Settings \-\> the security section \-\> tap the clipboard timeout entry \-\> select how long copied values remain on the clipboard before being cleared.

**35\. Block screenshots**

**Actions:** Open Settings \-\> security section \-\> enable the "Screenshot prohibited"/secure screen option; the app content is excluded from screenshots and the recents preview.

**36\. Change the master key of a database**

**Actions:** Open the unlocked database \-\> open the database settings \-\> tap the master key entry \-\> enter the new password and/or select a new key file \-\> confirm; save the database afterwards.

**37\. Change the database encryption settings**

**Actions:** Open the unlocked database \-\> tap the database settings \-\> set the encryption algorithm (for example AES or ChaCha20), the key derivation function (AES-KDF or Argon2), the number of iterations, the memory usage and the parallelism \-\> save.

**38\. Edit the database name, description and default username**

**Actions:** Open the unlocked database \-\> open the database settings \-\> edit the name, the description, the default username and the database colour \-\> save.

**39\. Configure history and compression settings**

**Actions:** Open the database settings \-\> set the maximum number of history items per entry, the maximum history size and whether the database is compressed \-\> save.

**40\. Use entry templates**

**Actions:** Open the database settings and set the templates group (KDBX 4\) \-\> tap "+" \-\> "Add entry" \-\> choose a template such as email, Wi-Fi, credit card or note \-\> fill in the template fields \-\> tap Save.

**41\. Merge/synchronise changes from another copy of the database**

**Actions:** Open the unlocked database \-\> tap the overflow menu \-\> tap the merge/synchronise action \-\> select the other .kdbx file \-\> enter its credentials \-\> confirm; the differences are merged into the open database.

**42\. Save a copy of the database (Save as)**

**Actions:** Open the unlocked database \-\> tap the overflow menu \-\> tap "Save as"/export \-\> choose the destination file with the system picker \-\> confirm.

**43\. Add a database to the recent list and pin it**

**Actions:** Open a database once; it appears on the start screen list \-\> long-press the entry there to remove it, or use the option to keep the file reference for quick reopening.

**44\. Change the app theme and appearance**

**Actions:** Open Settings \-\> tap "Appearance"/Form \-\> choose the theme (light, dark, black or system), the icon pack style, the list density and the text size \-\> return.

**45\. Change the app language**

**Actions:** Open Settings \-\> tap the Language entry \-\> select the interface language \-\> confirm.

**46\. Configure keyboard and form-filling behaviour**

**Actions:** Open Settings \-\> "Form filling" \-\> toggle the autofill inline suggestions, whether the app asks to save new credentials, and the Magikeyboard behaviour (auto-open, entry selection, notification).

**47\. View the about screen, contribution and licence information**

**Actions:** Open Settings \-\> tap "About" \-\> read the version, the changelog, the contribution options and the licence.

 

### **App Name: App Manager**

*Package: io.github.muntashirakon.AppManager  |  Version documented: 4.1.0  |  Reference: Official App Manager documentation (docs.muntashirakon.github.io) and in-app menus*

*Note: App Manager works without root but many operations require root access or an ADB/wireless-debugging connection; those are labelled inline.*

**Features:**

**1\. Browse the list of installed applications**

**Actions:** Open the app \-\> grant the requested permissions \-\> the main list shows every installed package with its icon, version, size, target SDK and status flags \-\> scroll or use the fast-scroll bar.

**2\. Search for an application**

**Actions:** Tap the search icon in the toolbar \-\> type part of the app name or package name \-\> the list filters as you type.

**3\. Sort the application list**

**Actions:** Tap the overflow menu (three dots) \-\> tap "Sort by" \-\> choose the field (app name, package name, last update, installation date, shared user ID, target SDK, signature, size or blocked component count) \-\> confirm.

**4\. Filter the application list**

**Actions:** Tap the filter icon \-\> tick the filters (for example user apps, system apps, disabled apps, apps with rules, apps with activities, installed via Play Store, running apps) \-\> confirm.

**5\. View an application's details**

**Actions:** Tap an app in the list \-\> the App Details page opens on the Information tab showing the version, installer, data directories, SDK versions, signatures, install time and the action buttons.

**6\. Browse an application's activities**

**Actions:** Open App Details \-\> swipe to the "Activities" tab \-\> review the declared activities with their export state.

**7\. Launch an exported activity directly**

**Actions:** Open App Details \-\> Activities tab \-\> tap the launch action beside the activity \-\> the activity opens (non-exported activities require root or ADB).

**8\. Create a shortcut to an activity**

**Actions:** Open App Details \-\> Activities tab \-\> tap the shortcut action beside the activity \-\> confirm the placement on the Android home screen.

**9\. Browse services, broadcast receivers and content providers**

**Actions:** Open App Details \-\> swipe to the Services, Receivers or Providers tab \-\> review each component and its export state.

**10\. Block or unblock an application component**

**Actions:** Open App Details \-\> open the Activities, Services, Receivers or Providers tab \-\> tap the block (shield) toggle beside the component \-\> tap the apply/save action in the toolbar (requires root).

**11\. Review and change app permissions**

**Actions:** Open App Details \-\> swipe to the "Permissions" tab \-\> tap a runtime permission toggle to grant or revoke it (requires root or ADB) \-\> review the protection level of each permission.

**12\. Review and change app operations (App Ops)**

**Actions:** Open App Details \-\> swipe to the "App Ops" tab \-\> tap an operation \-\> choose Allow, Deny, Ignore or Default \-\> confirm (requires root or ADB).

**13\. Review signatures and certificate details**

**Actions:** Open App Details \-\> swipe to the "Signatures" tab \-\> read the certificate issuer, subject, validity dates and the MD5/SHA-1/SHA-256 fingerprints.

**14\. Read an application's manifest**

**Actions:** Open App Details \-\> tap the manifest action in the toolbar \-\> the decoded AndroidManifest.xml is displayed \-\> use the search and save actions to look through or export it.

**15\. Scan an app for trackers and libraries**

**Actions:** Open App Details \-\> tap the scanner action (or open Scanner from the main overflow menu) \-\> wait for the analysis \-\> review the detected trackers, libraries and native libraries \-\> tap a category for the class list.

**16\. Check an APK against VirusTotal**

**Actions:** Open the Scanner result for an app \-\> tap the VirusTotal action \-\> confirm the upload/lookup \-\> read the returned scan summary (requires an API key configured in Settings).

**17\. Force-stop, disable or uninstall an application**

**Actions:** Open App Details \-\> use the action buttons at the top (Force stop, Disable, Uninstall) \-\> confirm the system prompt; disabling requires root or ADB.

**18\. Freeze or unfreeze an application**

**Actions:** Open App Details \-\> tap the freeze/unfreeze action \-\> confirm; the chosen freezing method (disable, suspend or hide) is set in Settings (requires root or ADB).

**19\. Clear an app's data or cache**

**Actions:** Open App Details \-\> tap the overflow menu \-\> tap "Clear data" or "Clear cache" \-\> confirm.

**20\. Back up an application with its data**

**Actions:** Open App Details \-\> tap the backup/restore action \-\> tap "Backup" \-\> tick the components to include (APK files, internal data, external data, OBB, cache, rules) \-\> optionally name the backup \-\> confirm.

**21\. Restore an application from a backup**

**Actions:** Open App Details or the Backups view \-\> tap the backup/restore action \-\> tap "Restore" \-\> select the backup \-\> tick the parts to restore \-\> confirm.

**22\. Delete a stored backup**

**Actions:** Open the backup/restore dialog for the app \-\> select the backup entry \-\> tap the delete action \-\> confirm.

**23\. Encrypt backups**

**Actions:** Open Settings \-\> "Backup/Restore" \-\> tap the encryption entry \-\> choose the method (for example OpenPGP or AES) \-\> configure the key or password \-\> confirm; subsequent backups are encrypted.

**24\. Perform batch operations on several apps**

**Actions:** On the main list \-\> long-press the first app \-\> tap the further apps to add them \-\> tap the batch action in the toolbar \-\> choose the operation (backup, restore, uninstall, disable, force-stop, clear data or cache, export blocking rules, add to a profile, block trackers) \-\> confirm.

**25\. Run one-click operations**

**Actions:** Open the navigation drawer \-\> tap "1-Click Ops" \-\> choose the operation (for example block trackers, block components by signature, deny app ops, trim caches, import existing rules) \-\> review the affected apps \-\> confirm.

**26\. Create a profile**

**Actions:** Open the navigation drawer \-\> tap "Profiles" \-\> tap the "+" button \-\> enter the profile name \-\> select the applications to include \-\> configure the actions (components to block, app ops, permissions, backup, freeze, force-stop) \-\> save.

**27\. Apply a profile**

**Actions:** Open Profiles \-\> tap the profile \-\> tap the apply action \-\> choose whether to apply or undo the profile state \-\> confirm.

**28\. Create a shortcut for a profile**

**Actions:** Open Profiles \-\> open the profile \-\> tap the overflow menu \-\> tap the shortcut action \-\> confirm the placement on the home screen.

**29\. View running applications and processes**

**Actions:** Open the navigation drawer \-\> tap "Running apps" \-\> review the running processes with their memory and CPU usage \-\> tap an entry for the details \-\> tap the kill action to terminate it (requires root or ADB).

**30\. View application usage statistics**

**Actions:** Open the navigation drawer \-\> tap "App usage" \-\> grant the usage-access permission when prompted \-\> select the period \-\> review the screen time, launch count and mobile/Wi-Fi data usage per app.

**31\. Read the system log with the log viewer**

**Actions:** Open the navigation drawer \-\> tap "Log viewer" \-\> grant the required permission (root or ADB) \-\> filter by level, tag or PID \-\> use the search and save actions to inspect or export the log.

**32\. Intercept and modify an intent**

**Actions:** Open the navigation drawer \-\> tap "Interceptor" \-\> paste or share an intent into it \-\> edit the action, data URI, MIME type, package, class, categories, flags and extras \-\> tap the launch/resend action.

**33\. Install an APK with the built-in installer**

**Actions:** Tap an APK file in a file manager and choose App Manager, or open the drawer \-\> tap the install action \-\> select the APK, APKS, APKM or XAPK file \-\> choose the installation user and installer source \-\> confirm the installation.

**34\. Browse APK files on the device**

**Actions:** Open the navigation drawer \-\> tap "APKs"/the APK updater view \-\> review the APK files found on the device \-\> tap one to install or inspect it.

**35\. Save an installed app's APK**

**Actions:** Open App Details \-\> tap the overflow menu \-\> tap the "Save APK"/export action \-\> choose the destination folder \-\> confirm.

**36\. Share an APK**

**Actions:** Open App Details \-\> tap the share action \-\> choose whether to share the APK or the split bundle \-\> pick the destination app.

**37\. Use the built-in file manager**

**Actions:** Open the navigation drawer \-\> tap "Files"/the file manager entry \-\> browse the storage \-\> use the copy, move, rename, delete, compress and open-with actions on files.

**38\. Edit shared preferences of an app (root)**

**Actions:** Open App Details \-\> tap the overflow menu \-\> open the shared preferences/data viewer \-\> select the XML file \-\> tap a key to change its value \-\> save.

**39\. View an app's databases (root)**

**Actions:** Open App Details \-\> open the data/databases viewer \-\> select the database file \-\> browse the tables and rows.

**40\. Configure the mode of operation (root, ADB or no-root)**

**Actions:** Open Settings \-\> tap "Mode of operation" \-\> choose Auto, Root, ADB over TCP, Wireless debugging or No-root \-\> follow the pairing instructions for the ADB modes \-\> confirm.

**41\. Pair over wireless debugging**

**Actions:** Enable developer options and wireless debugging on the device \-\> open App Manager Settings \-\> Mode of operation \-\> choose wireless debugging \-\> tap the pair action \-\> enter the pairing code shown by Android \-\> confirm.

**42\. Set the backup storage location and options**

**Actions:** Open Settings \-\> "Backup/Restore" \-\> choose the backup volume/folder \-\> set the compression method, whether device-specific data is included and the number of backups to keep.

**43\. Lock App Manager with a screen lock or biometrics**

**Actions:** Open Settings \-\> tap the security/screen-lock entry \-\> enable it \-\> authenticate; the app then requires authentication at each launch.

**44\. Change the theme, language and layout**

**Actions:** Open Settings \-\> tap "Appearance" \-\> choose the theme (light, dark, system or black), enable the pure-black option, set the app language and choose the list layout.

**45\. Import and export component blocking rules**

**Actions:** Open Settings \-\> "Rules" \-\> tap the import or export action \-\> choose the format (App Manager, Watt or Blocker) \-\> select the file \-\> confirm.

**46\. View the about screen, changelog and documentation**

**Actions:** Open the navigation drawer \-\> tap "About"/"Changelog" \-\> read the version, the changelog and the link to the online user manual.

 

### **App Name: Open Camera**

*Package: net.sourceforge.opencamera  |  Version documented: 1.56.2  |  Reference: Official Open Camera help pages (opencamera.org.uk) and in-app settings*

**Features:**

**1\. Take a photo**

**Actions:** Open the app \-\> grant the camera and storage permissions \-\> frame the shot on the preview \-\> tap the shutter button (or press a volume key if configured).

**2\. Record a video**

**Actions:** Open the app \-\> tap the photo/video mode toggle to switch to video \-\> tap the record button \-\> tap it again to stop; tap the pause control to pause and resume where supported.

**3\. Switch between the front and rear cameras**

**Actions:** Tap the camera-switch icon on the preview overlay \-\> the preview changes to the other lens; on multi-camera devices, tap repeatedly to cycle through the available cameras.

**4\. Zoom in and out**

**Actions:** Pinch on the preview with two fingers, or drag the on-screen zoom slider, or use the volume keys if they are configured for zoom.

**5\. Focus by tapping**

**Actions:** Tap the point on the preview you want in focus \-\> the focus box appears and the camera focuses there; enable "touch to capture" in Settings to also take the shot.

**6\. Change the focus mode**

**Actions:** Tap the settings/popup icon on the preview \-\> tap the focus entry \-\> choose the mode (continuous picture, continuous video, auto, macro, infinity, fixed or manual) \-\> for manual, drag the distance slider.

**7\. Set the flash mode**

**Actions:** Tap the flash icon on the preview \-\> choose Off, Auto, On, Torch or Red-eye reduction.

**8\. Use the front screen flash for selfies**

**Actions:** Switch to the front camera \-\> tap the flash icon \-\> choose the front screen flash option; the screen flashes white when the shot is taken.

**9\. Set exposure compensation**

**Actions:** Tap the exposure (+/-) icon on the preview \-\> drag the exposure compensation slider \-\> tap outside to close.

**10\. Set the ISO and shutter speed manually**

**Actions:** Open Settings and enable the Camera2 API \-\> tap the exposure icon \-\> switch the ISO from Auto to a manual value \-\> drag the ISO slider \-\> drag the shutter speed/exposure time slider \-\> tap outside to apply.

**11\. Set the white balance**

**Actions:** Tap the popup settings icon \-\> tap the white balance entry \-\> choose a preset (auto, daylight, cloudy, incandescent, fluorescent, shade or twilight) or select manual and drag the colour temperature slider.

**12\. Choose a scene mode**

**Actions:** Tap the popup settings icon \-\> tap the scene mode entry \-\> choose the mode (for example auto, portrait, landscape, night, sports, fireworks or snow).

**13\. Apply a colour effect**

**Actions:** Tap the popup settings icon \-\> tap the colour effect entry \-\> select the effect (for example mono, negative, sepia, solarise, posterise or aqua).

**14\. Set the photo resolution**

**Actions:** Tap the popup settings icon \-\> tap the resolution entry \-\> select the megapixel/aspect option for the current camera.

**15\. Set the image quality and format**

**Actions:** Open Settings \-\> "Photo settings" \-\> set the JPEG quality slider and choose the image format (JPEG, WebP or PNG) \-\> return.

**16\. Capture RAW (DNG) files**

**Actions:** Open Settings \-\> enable the Camera2 API \-\> open Photo settings \-\> enable RAW capture \-\> choose whether to save RAW only or RAW plus JPEG \-\> return and take the shot.

**17\. Use the self-timer**

**Actions:** Tap the popup settings icon \-\> tap the timer entry \-\> choose the delay (for example 3, 5 or 10 seconds) \-\> tap the shutter; the countdown runs before the shot is taken.

**18\. Take a repeated series of photos (auto-repeat)**

**Actions:** Tap the popup settings icon \-\> tap the repeat/burst entry \-\> choose the number of photos and the interval between them \-\> tap the shutter.

**19\. Take an HDR photo**

**Actions:** Tap the photo mode selector in the popup settings \-\> choose HDR \-\> hold the phone steady \-\> tap the shutter; the exposures are merged automatically.

**20\. Take a DRO (dynamic range optimised) photo**

**Actions:** Open the photo mode selector \-\> choose DRO \-\> tap the shutter; a single exposure is tone-mapped for a wider dynamic range.

**21\. Take an exposure bracketing series**

**Actions:** Open the photo mode selector \-\> choose Exposure bracketing \-\> set the number of images and the stops between them in Settings \-\> tap the shutter.

**22\. Take a noise-reduction (low light) photo**

**Actions:** Open the photo mode selector \-\> choose NR/Noise reduction \-\> hold the device steady \-\> tap the shutter; several frames are combined.

**23\. Capture a panorama**

**Actions:** Open the photo mode selector \-\> choose Panorama \-\> tap the shutter \-\> pan slowly following the on-screen guide until enough frames are captured \-\> the panorama is stitched and saved.

**24\. Enable face detection**

**Actions:** Open Settings \-\> "Camera preview"/Photo settings \-\> enable face detection \-\> detected faces are outlined on the preview and used for focus and exposure.

**25\. Enable auto-level (auto-stabilise)**

**Actions:** Open Settings \-\> Photo settings \-\> enable the auto-level/auto-stabilise option; photos are rotated and cropped so the horizon is level.

**26\. Show composition guides and crop guides**

**Actions:** Open Settings \-\> "Camera preview" \-\> tap the grid entry and choose the guide (for example rule of thirds, golden ratio, crosshair, or a 4:3/16:9 crop guide).

**27\. Show the histogram, zebra stripes and focus peaking**

**Actions:** Open Settings \-\> Camera preview (on-screen GUI) \-\> enable the histogram, the zebra-stripe overexposure warning and the focus-peaking overlay as required.

**28\. Show the angle, level, battery and free-memory indicators**

**Actions:** Open Settings \-\> "On screen GUI" \-\> toggle the individual on-screen indicators (angle, geo-direction, ISO, free memory, remaining time, battery, time) \-\> return to the preview.

**29\. Enable geotagging of photos and videos**

**Actions:** Open Settings \-\> "Location settings" \-\> enable "Store location data" \-\> grant the location permission \-\> wait for the GPS fix indicator on the preview before shooting.

**30\. Store the compass direction with photos**

**Actions:** Open Settings \-\> Location settings \-\> enable the geo-direction option; the bearing is written into the image metadata.

**31\. Stamp the date, time and location on photos**

**Actions:** Open Settings \-\> "Photo stamp"/stamp settings \-\> enable the photo stamp \-\> choose whether to include the date, time, location and a custom text \-\> set the font size, colour and alignment.

**32\. Add a custom text stamp**

**Actions:** Open Settings \-\> stamp settings \-\> tap the custom text entry \-\> type the text (for example a copyright line) \-\> confirm.

**33\. Set the video resolution and frame rate**

**Actions:** Switch to video mode \-\> tap the popup settings icon \-\> tap the video resolution entry and choose the size \-\> tap the frame rate entry and choose the fps.

**34\. Record slow-motion or high-speed video**

**Actions:** Switch to video mode \-\> open the popup settings \-\> select a high frame rate mode supported by the device \-\> set the slow-motion playback factor \-\> record.

**35\. Record a time-lapse video**

**Actions:** Switch to video mode \-\> open the popup settings \-\> tap the time-lapse/capture rate entry \-\> choose the interval factor \-\> record.

**36\. Set the video bitrate**

**Actions:** Open Settings \-\> "Video settings" \-\> tap the bitrate entry \-\> choose a preset or enter a custom value.

**37\. Limit the video duration or file size**

**Actions:** Open Settings \-\> Video settings \-\> set the maximum duration and the maximum file size \-\> choose whether recording restarts automatically when the limit is reached.

**38\. Enable video stabilisation**

**Actions:** Open Settings \-\> Video settings \-\> enable the video stabilisation option (device support required) \-\> return and record.

**39\. Choose the audio source and control audio recording**

**Actions:** Open Settings \-\> Video settings \-\> tap the audio source entry (for example default, microphone, camcorder, voice recognition or unprocessed) \-\> or disable audio recording entirely.

**40\. Record GPS/time subtitles for videos**

**Actions:** Open Settings \-\> Video settings \-\> enable the subtitle option \-\> choose what is recorded (GPS coordinates and/or the timestamp); an .SRT file is written alongside the video.

**41\. Use voice control to take a photo**

**Actions:** Open Settings \-\> enable voice control \-\> grant the microphone permission \-\> tap the voice control icon on the preview to arm it \-\> say the trigger word ("cheese") to take the shot.

**42\. Use audio (noise) triggering**

**Actions:** Open Settings \-\> enable the audio trigger \-\> choose the loud-noise mode and the sensitivity \-\> arm it from the preview \-\> make the noise to trigger the shutter.

**43\. Use a Bluetooth LE remote control**

**Actions:** Open Settings \-\> "Remote control" \-\> enable it \-\> scan for and pair the supported Bluetooth LE remote \-\> use the remote button to trigger the shutter or start recording.

**44\. Configure the volume key behaviour**

**Actions:** Open Settings \-\> "More camera controls" \-\> tap the volume keys entry \-\> choose the action (take photo, zoom, change exposure, change focus, adjust volume or do nothing).

**45\. Enable touch-to-capture**

**Actions:** Open Settings \-\> More camera controls \-\> enable "Touch to capture"; tapping anywhere on the preview then takes the photo.

**46\. Lock the screen orientation**

**Actions:** Open Settings \-\> Camera preview \-\> tap the lock orientation entry \-\> choose portrait, landscape or none \-\> return.

**47\. Use immersive (full screen) mode**

**Actions:** Open Settings \-\> Camera preview \-\> tap the immersive mode entry \-\> choose which controls are hidden (for example hide the GUI or hide everything) \-\> return.

**48\. Set the photo and video save location**

**Actions:** Open Settings \-\> "More camera controls"/Save location \-\> tap the save folder entry \-\> choose the folder (or enable the Storage Access Framework and pick a tree with the system picker) \-\> confirm.

**49\. Use the Storage Access Framework for saving**

**Actions:** Open Settings \-\> enable "Use Storage Access Framework" \-\> tap the save folder entry \-\> select the destination folder with the Android picker \-\> grant persistent access.

**50\. Open the last photo in the gallery**

**Actions:** Tap the thumbnail in the corner of the preview \-\> the last captured photo or video opens in the gallery app.

**51\. Pause the preview after taking a photo**

**Actions:** Open Settings \-\> Photo settings \-\> enable "Pause after taking photo"; the captured image is shown with share, delete and info options before returning to the preview.

**52\. Enable or disable the shutter sound**

**Actions:** Open Settings \-\> "More camera controls" \-\> toggle the shutter sound option (where local regulations allow it).

**53\. Enable the Camera2 API**

**Actions:** Open Settings \-\> "Camera API" \-\> select Camera2 \-\> confirm the restart prompt; manual controls, RAW and high-speed modes become available on supported devices.

**54\. Reset all settings to the defaults**

**Actions:** Open Settings \-\> scroll to the reset entry \-\> tap "Reset settings" \-\> confirm.

**55\. Read the built-in help and about information**

**Actions:** Open Settings \-\> tap "About"/"Online help" \-\> read the version and device capability report or open the online help pages.

 

## **Category: Additional applications**

### **App Name: Fossify Gallery**

*Package: org.fossify.gallery  |  Version documented: F-Droid build 28  |  Reference: Official Fossify repository documentation and F-Droid listing*

**Features:**

**1\. Browse media folders**

**Actions:** Open the app \-\> grant the media permission \-\> the folder grid lists every folder containing images or videos \-\> tap a folder to open its contents.

**2\. View a photo full screen**

**Actions:** Open a folder \-\> tap a thumbnail \-\> the full-screen viewer opens \-\> swipe left or right to move to the next or previous item \-\> pinch to zoom \-\> double-tap to zoom quickly.

**3\. Play a video**

**Actions:** Open a folder \-\> tap a video thumbnail \-\> the built-in player opens \-\> use play/pause, the seek bar and the skip controls \-\> rotate the device or tap the fullscreen control for landscape playback.

**4\. Edit a photo**

**Actions:** Open the photo \-\> tap the edit (pencil) icon \-\> choose the tool (crop and rotate, filters, or draw) \-\> apply the change \-\> tap Save \-\> choose to overwrite the file or save a copy.

**5\. Crop, rotate and flip a photo**

**Actions:** Open the photo \-\> tap the edit icon \-\> select the crop/rotate tool \-\> pick the aspect ratio or drag the crop handles \-\> use the rotate and flip buttons \-\> tap Save.

**6\. Apply a filter to a photo**

**Actions:** Open the photo \-\> tap the edit icon \-\> switch to the Filters tab \-\> tap the filter thumbnail to preview it \-\> tap Save.

**7\. Draw on a photo**

**Actions:** Open the photo \-\> tap the edit icon \-\> switch to the Draw tab \-\> pick the brush colour and stroke width \-\> draw on the image \-\> use undo if needed \-\> tap Save.

**8\. Resize a photo**

**Actions:** Open the photo \-\> tap the overflow menu (three dots) \-\> tap "Resize" \-\> enter the new width and height (the aspect ratio can be locked) \-\> tap OK \-\> choose the destination.

**9\. Rotate a photo without re-encoding**

**Actions:** Open the photo \-\> tap the overflow menu \-\> tap "Rotate" \-\> choose left, right or 180 degrees; the change is written to the file.

**10\. Set a photo as the wallpaper**

**Actions:** Open the photo \-\> tap the overflow menu \-\> tap "Set as" \-\> choose Wallpaper \-\> select the home screen, lock screen or both \-\> confirm.

**11\. Share media**

**Actions:** Open the item (or long-press it in the grid) \-\> tap the share icon \-\> choose the destination app from the Android share sheet.

**12\. Print a photo**

**Actions:** Open the photo \-\> tap the overflow menu \-\> tap "Print" \-\> choose the printer or "Save as PDF" \-\> confirm.

**13\. View media properties**

**Actions:** Long-press the item \-\> tap the overflow menu \-\> tap "Properties" \-\> read the name, path, size, resolution or duration, date taken, camera details and EXIF data.

**14\. Mark media as a favourite**

**Actions:** Long-press the item \-\> tap the favourite (heart) action; or open it and tap the heart icon. Favourites are collected in a dedicated Favourites folder.

**15\. Copy or move media to another folder**

**Actions:** Long-press the item(s) \-\> tap the copy or move icon \-\> select the destination folder \-\> tap the confirm button.

**16\. Rename media or a folder**

**Actions:** Long-press the item or folder \-\> tap the rename action \-\> enter the new name (batch renaming with a pattern is offered for multiple selections) \-\> tap OK.

**17\. Delete media**

**Actions:** Long-press the item(s) \-\> tap the delete (bin) icon \-\> confirm; deleted items go to the recycle bin when it is enabled.

**18\. Restore or empty the recycle bin**

**Actions:** Open the folder list \-\> tap the "Recycle bin" entry \-\> long-press an item and tap Restore, or tap "Empty the recycle bin" \-\> confirm.

**19\. Hide a folder from the gallery**

**Actions:** Long-press the folder \-\> tap the overflow menu \-\> tap "Hide folder" \-\> confirm; use "Temporarily show hidden" or the settings toggle to see it again.

**20\. Exclude a folder from the gallery**

**Actions:** Long-press the folder \-\> tap the overflow menu \-\> tap "Exclude folder" \-\> confirm; manage the exclusion list later from Settings \-\> "Manage excluded folders".

**21\. Pin a folder to the top of the list**

**Actions:** Long-press the folder \-\> tap the pin action; pinned folders stay at the top of the folder grid.

**22\. Create a new folder**

**Actions:** Open the destination view \-\> tap the overflow menu \-\> tap "Create new folder" \-\> enter the name \-\> tap OK.

**23\. Run a slideshow**

**Actions:** Open a folder or a photo \-\> tap the overflow menu \-\> tap "Slideshow" \-\> set the interval, the animation, whether videos are included and whether it loops randomly \-\> tap Start.

**24\. Search for media**

**Actions:** Tap the search icon in the toolbar \-\> type part of the file name \-\> tap a result to open it.

**25\. Sort media and folders**

**Actions:** Tap the overflow menu \-\> tap "Sort by" \-\> choose the field (name, date taken, date modified, size, extension or random) and the direction \-\> optionally apply it to the current folder only \-\> tap OK.

**26\. Group media inside a folder**

**Actions:** Open a folder \-\> tap the overflow menu \-\> tap "Group by" \-\> choose none, folder, last modified, date taken, file type or extension \-\> confirm; headers appear between the groups.

**27\. Filter the media types shown**

**Actions:** Tap the overflow menu \-\> tap "Filter media" \-\> tick the types to show (images, videos, GIFs, RAW images, SVGs, portraits) \-\> tap OK.

**28\. Change the grid column count**

**Actions:** Open a folder \-\> pinch on the grid to increase or decrease the number of columns, or open the overflow menu \-\> "Change view type" \-\> select grid or list and the column count.

**29\. Show hidden items**

**Actions:** Tap the overflow menu \-\> toggle "Temporarily show hidden" (or enable the permanent setting in Settings) \-\> hidden folders and .nomedia folders become visible.

**30\. Open a folder as a home screen shortcut**

**Actions:** Long-press the folder \-\> tap the overflow menu \-\> tap "Create shortcut" \-\> confirm the placement on the Android home screen.

**31\. Fix the "date taken" value of media**

**Actions:** Long-press the item(s) \-\> tap the overflow menu \-\> tap "Fix date taken" \-\> confirm; the EXIF date is written back into the file metadata.

**32\. Protect hidden items or the whole app with a lock**

**Actions:** Open Settings \-\> tap the security section \-\> enable the protection for hidden items, for the recycle bin, for the whole app or for excluded folders \-\> choose PIN, pattern or fingerprint \-\> set the secret.

**33\. Customise the app colours and theme**

**Actions:** Open Settings \-\> tap "Customise colours" \-\> choose a preset theme or set the text, background, primary and app-icon colours \-\> tap the tick to save.

**34\. Configure the full-screen viewer behaviour**

**Actions:** Open Settings \-\> open the viewer section \-\> toggle options such as hiding the system bars, the swipe-down-to-close gesture, looping through the folder, showing the file name, allowing deep zoom and the double-tap zoom behaviour.

**35\. Configure video playback behaviour**

**Actions:** Open Settings \-\> open the videos section \-\> toggle automatic playback on open, looping, remembering the last playback position and whether the volume/brightness gestures are enabled.

**36\. Change the app language and font size**

**Actions:** Open Settings \-\> tap the Language entry and choose the language \-\> tap the font size entry and choose the size.

**37\. View the about screen, FAQ and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the FAQ, the version, the licences and the source repository link.

 

### **App Name: Fossify Notes**

*Package: org.fossify.notes  |  Version documented: F-Droid build 13  |  Reference: Official Fossify repository documentation and F-Droid listing*

**Features:**

**1\. Create a text note**

**Actions:** Open the app \-\> tap the overflow menu (three dots) \-\> tap "New note"/the "+" action \-\> enter the note title \-\> choose the "Text note" type \-\> tap OK \-\> type the content; the text is saved automatically.

**2\. Create a checklist note**

**Actions:** Tap the overflow menu \-\> tap "New note" \-\> enter the title \-\> choose the "Checklist" type \-\> tap OK \-\> tap the "+" to add each item \-\> type the item text \-\> tap OK.

**3\. Tick and untick checklist items**

**Actions:** Open the checklist note \-\> tap the checkbox beside an item to mark it done \-\> tap it again to clear it.

**4\. Reorder or remove checklist items**

**Actions:** Open the checklist note \-\> long-press an item \-\> drag it to a new position, or tap the delete action on the item \-\> confirm.

**5\. Switch between notes**

**Actions:** Tap the note title in the toolbar (or open the overflow menu \-\> "Open note") \-\> select the note from the list; the editor switches to it.

**6\. Rename a note**

**Actions:** Open the note \-\> tap the overflow menu \-\> tap "Rename note" \-\> enter the new title \-\> tap OK.

**7\. Delete a note**

**Actions:** Open the note \-\> tap the overflow menu \-\> tap "Delete note" \-\> confirm.

**8\. Undo and redo edits**

**Actions:** While editing a text note \-\> tap the undo arrow in the toolbar to revert the last change \-\> tap the redo arrow to reapply it.

**9\. Search inside a note**

**Actions:** Open the note \-\> tap the search icon in the toolbar \-\> type the search term \-\> step through the highlighted matches with the up/down chevrons.

**10\. Lock a note with a PIN, pattern or fingerprint**

**Actions:** Open the note \-\> tap the overflow menu \-\> tap "Lock note" \-\> choose the protection type \-\> set the secret \-\> confirm; the note content is hidden until it is unlocked.

**11\. Unlock a protected note**

**Actions:** Open the locked note \-\> enter the PIN or pattern, or present the fingerprint \-\> the content is revealed.

**12\. Export a note to a file**

**Actions:** Open the note \-\> tap the overflow menu \-\> tap "Export as file" \-\> choose the destination folder and the file name \-\> confirm.

**13\. Export all notes at once**

**Actions:** Open the overflow menu \-\> tap "Export all notes" \-\> choose the destination folder \-\> confirm; each note is written as a separate file.

**14\. Import a note from a file**

**Actions:** Open the overflow menu \-\> tap "Import a note"/"Open file" \-\> select the text file \-\> choose whether to keep the note synchronised with the file \-\> confirm.

**15\. Keep a note synchronised with a file on disk**

**Actions:** Import or create a note \-\> open the overflow menu \-\> tap the "Open file"/sync option \-\> select the target file \-\> confirm; changes to the note are written back to that file.

**16\. Share a note**

**Actions:** Open the note \-\> tap the overflow menu \-\> tap "Share" \-\> choose the destination app in the Android share sheet.

**17\. Print a note**

**Actions:** Open the note \-\> tap the overflow menu \-\> tap "Print" \-\> choose the printer or "Save as PDF" \-\> confirm.

**18\. Add the note home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Fossify Notes \-\> drag the widget onto the home screen \-\> select the note it should display \-\> set the background colour, transparency and text colour \-\> tap OK.

**19\. Change the editor font size and typeface**

**Actions:** Open Settings \-\> tap the font size entry and choose the size \-\> toggle the monospaced font option if a fixed-width font is preferred.

**20\. Enable or disable line wrapping**

**Actions:** Open Settings \-\> toggle the "Use line wrap"/word-wrap option; with it off, long lines can be scrolled horizontally.

**21\. Set where the cursor is placed when a note is opened**

**Actions:** Open Settings \-\> tap the cursor placement entry \-\> choose the start or the end of the note.

**22\. Configure checklist behaviour**

**Actions:** Open Settings \-\> toggle whether completed items are moved to the bottom of the checklist and whether new items are added at the top.

**23\. Show a word and character count**

**Actions:** Open Settings \-\> enable the "Show word count" option; the counter is displayed while editing a text note.

**24\. Set the note text alignment**

**Actions:** Open Settings \-\> tap the gravity/alignment entry \-\> choose left, centre or right \-\> return.

**25\. Enable automatic saving**

**Actions:** Open Settings \-\> toggle the automatic save option; with it off, a save icon appears in the toolbar and changes must be saved manually.

**26\. Protect the whole app with a lock**

**Actions:** Open Settings \-\> tap the app-lock entry \-\> choose PIN, pattern or fingerprint \-\> set the secret \-\> confirm.

**27\. Customise the app colours and theme**

**Actions:** Open Settings \-\> tap "Customise colours" \-\> choose a preset theme or set the text, background, primary and app-icon colours \-\> tap the tick to save.

**28\. Change the app language**

**Actions:** Open Settings \-\> tap the Language entry \-\> select the interface language.

**29\. View the about screen, FAQ and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the FAQ, the version, the licences and the source repository link.

 

### **App Name: Fossify Clock**

*Package: org.fossify.clock  |  Version documented: F-Droid build 10  |  Reference: Official Fossify repository documentation and F-Droid listing*

**Features:**

**1\. View the current time on the clock tab**

**Actions:** Open the app \-\> the Clock tab shows the current time and date for the device time zone.

**2\. Add a time zone to the clock**

**Actions:** Open the Clock tab \-\> tap the "+" floating action button \-\> tick the time zones to display \-\> tap OK; the selected cities are listed with their local time.

**3\. Remove or reorder time zones**

**Actions:** Open the Clock tab \-\> tap the "+" button and untick a zone to remove it, or open Settings \-\> "Manage time zones"/edit the list \-\> drag the handles to reorder \-\> confirm.

**4\. Open the full-screen (screensaver) clock**

**Actions:** Open the Clock tab \-\> tap the clock face \-\> the dimmed full-screen clock is displayed \-\> tap the screen or press back to exit.

**5\. Create an alarm**

**Actions:** Open the Alarm tab \-\> tap the "+" button \-\> set the hour and minute in the picker \-\> tap OK \-\> select the repeat days \-\> tap the label field and enter a name \-\> choose the alarm sound \-\> tap Save.

**6\. Enable or disable an alarm**

**Actions:** Open the Alarm tab \-\> tap the toggle switch beside the alarm row.

**7\. Edit an alarm**

**Actions:** Open the Alarm tab \-\> tap the alarm row \-\> change the time, repeat days, label, sound or vibration \-\> tap Save.

**8\. Delete an alarm**

**Actions:** Open the Alarm tab \-\> long-press the alarm \-\> tap the delete (bin) icon \-\> confirm.

**9\. Set the alarm sound and vibration**

**Actions:** Open an alarm for editing \-\> tap the alarm sound entry and select a tone (or a file from storage) \-\> toggle the vibration option \-\> tap Save.

**10\. Snooze or dismiss a ringing alarm**

**Actions:** When the alarm rings \-\> tap Snooze to postpone it by the configured interval, or tap Dismiss to stop it.

**11\. Configure the snooze duration and maximum ring time**

**Actions:** Open Settings \-\> tap the snooze time entry and choose the delay \-\> tap the "Alarm max reminder duration" entry and choose how long the alarm rings before it stops.

**12\. Make the alarm volume increase gradually**

**Actions:** Open Settings \-\> enable the "Increase volume gradually" option \-\> set the ramp period if offered.

**13\. Use the stopwatch**

**Actions:** Open the Stopwatch tab \-\> tap Start \-\> tap the lap button to record a lap \-\> tap Stop to pause \-\> tap Reset to clear it.

**14\. Sort the recorded stopwatch laps**

**Actions:** Open the Stopwatch tab with laps recorded \-\> tap the sort/overflow control \-\> choose the lap ordering (for example by lap number or lap time) \-\> confirm.

**15\. Create a timer**

**Actions:** Open the Timer tab \-\> set the hours, minutes and seconds \-\> tap Start; tap the "+" button to create an additional timer.

**16\. Label a timer and set its sound**

**Actions:** Open the Timer tab \-\> tap the settings/edit control on the timer \-\> enter the label \-\> choose the alert sound and the vibration option \-\> confirm.

**17\. Pause, resume, reset or delete a timer**

**Actions:** Open the Timer tab \-\> tap the pause control to hold the countdown \-\> tap it again to resume \-\> tap the reset control to return it to the start value \-\> tap the delete action to remove the timer.

**18\. Add the digital clock home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Fossify Clock \-\> drag the widget onto the home screen \-\> set the text colour, background colour and transparency \-\> tap OK.

**19\. Set the time format**

**Actions:** Open Settings \-\> toggle the "Use 24-hour time format" option (or follow the system setting).

**20\. Set the first day of the week**

**Actions:** Open Settings \-\> tap the "Start week on"/Sunday-first option \-\> choose the weekday used by the alarm repeat selector.

**21\. Keep the screen on in the clock tab**

**Actions:** Open Settings \-\> enable the "Keep the screen on" option for the clock view.

**22\. Choose which tabs are visible**

**Actions:** Open Settings \-\> open the tabs section \-\> tick the tabs to show (Clock, Alarm, Stopwatch, Timer) \-\> confirm.

**23\. Make alarms ignore silent mode**

**Actions:** Open Settings \-\> toggle the option that allows alarms to sound even when the device is in silent or do-not-disturb mode.

**24\. Customise the app colours and theme**

**Actions:** Open Settings \-\> tap "Customise colours" \-\> choose a preset theme or set the text, background, primary and app-icon colours \-\> tap the tick to save.

**25\. Change the app language and font size**

**Actions:** Open Settings \-\> tap the Language entry and choose the language \-\> tap the font size entry and choose the size.

**26\. View the about screen, FAQ and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the FAQ, the version, the licences and the source repository link.

 

### **App Name: Fossify Voice Recorder**

*Package: org.fossify.voicerecorder  |  Version documented: F-Droid build 18  |  Reference: Official Fossify repository documentation and F-Droid listing*

**Features:**

**1\. Record audio**

**Actions:** Open the app \-\> grant the microphone and storage permissions \-\> tap the record (microphone) button \-\> speak \-\> tap the stop button to finish and save the recording.

**2\. Pause and resume a recording**

**Actions:** While recording \-\> tap the pause control \-\> tap it again to continue the same recording \-\> tap stop when finished.

**3\. Watch the live audio level while recording**

**Actions:** Start a recording \-\> the visualiser/level meter on the recording screen shows the incoming signal in real time.

**4\. Continue recording in the background**

**Actions:** Start a recording \-\> press the home button or switch apps \-\> the recording continues and is controlled from the persistent notification \-\> tap the notification action to pause or stop it.

**5\. Browse saved recordings**

**Actions:** Open the "Recordings" tab \-\> scroll the list of saved files with their duration, size and date.

**6\. Play a recording**

**Actions:** Open the Recordings tab \-\> tap a recording \-\> the inline player opens \-\> use play/pause and the seek bar \-\> tap the skip controls to move forward or back.

**7\. Rename a recording**

**Actions:** Open the Recordings tab \-\> long-press the recording \-\> tap the rename action \-\> enter the new name \-\> tap OK.

**8\. Delete a recording**

**Actions:** Long-press the recording \-\> tap the delete (bin) icon \-\> confirm; the file goes to the recycle bin when that option is enabled.

**9\. Restore or empty the recycle bin**

**Actions:** Open the "Deleted recordings"/recycle bin tab \-\> long-press an item and tap Restore, or tap the "Empty recycle bin" action \-\> confirm.

**10\. Share a recording**

**Actions:** Long-press the recording (or open it) \-\> tap the share icon \-\> choose the destination app in the Android share sheet.

**11\. View recording properties**

**Actions:** Long-press the recording \-\> tap the overflow menu \-\> tap "Properties" \-\> read the file name, path, size, duration and last-modified date.

**12\. Search recordings**

**Actions:** Open the Recordings tab \-\> tap the search icon \-\> type part of the file name \-\> tap a result to play it.

**13\. Sort the recordings list**

**Actions:** Open the Recordings tab \-\> tap the overflow menu (three dots) \-\> tap "Sort by" \-\> choose the field (title, date or size) and the direction \-\> tap OK.

**14\. Choose the recording audio format**

**Actions:** Open Settings \-\> tap the "Audio format"/extension entry \-\> choose the format (for example M4A, MP3 or OGG/Opus) \-\> confirm.

**15\. Set the recording bitrate and quality**

**Actions:** Open Settings \-\> tap the bitrate entry \-\> choose the value; higher values give better quality and larger files.

**16\. Choose the folder where recordings are saved**

**Actions:** Open Settings \-\> tap the "Save recordings in" entry \-\> browse to and select the destination folder \-\> confirm.

**17\. Hide the recording notification**

**Actions:** Open Settings \-\> toggle the "Hide notification"/silent recording option \-\> confirm; a persistent notification may still be required by Android for background recording.

**18\. Keep the screen on while recording**

**Actions:** Open Settings \-\> enable the "Keep the screen on" option \-\> return to the recording screen.

**19\. Add the quick-record home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Fossify Voice Recorder \-\> drag the widget onto the home screen \-\> set the colour and transparency \-\> tap OK; tapping it starts a recording immediately.

**20\. Protect the app with a PIN, pattern or fingerprint**

**Actions:** Open Settings \-\> tap the app-lock entry \-\> choose the lock type \-\> set the secret \-\> confirm.

**21\. Customise the app colours and theme**

**Actions:** Open Settings \-\> tap "Customise colours" \-\> choose a preset theme or set the text, background, primary and app-icon colours \-\> tap the tick to save.

**22\. Change the app language and font size**

**Actions:** Open Settings \-\> tap the Language entry and choose the language \-\> tap the font size entry and choose the size.

**23\. View the about screen, FAQ and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the FAQ, the version, the licences and the source repository link.

 

### **App Name: Feeder**

*Package: com.nononsenseapps.feeder  |  Version documented: F-Droid build 4050  |  Reference: Official Feeder repository documentation and F-Droid listing*

**Features:**

**1\. Add a feed by URL**

**Actions:** Open the app \-\> tap the "+" floating action button (Add feed) \-\> paste or type the feed or website address \-\> tap the search/find action \-\> select the discovered feed from the results \-\> optionally set the title and tag \-\> tap OK/Save.

**2\. Add a feed by sharing a link from another app**

**Actions:** In a browser or another app, tap Share on the page link \-\> choose Feeder \-\> the add-feed screen opens with the URL pre-filled \-\> confirm the discovered feed \-\> tap Save.

**3\. Edit a feed**

**Actions:** Open the navigation drawer \-\> long-press the feed (or open it and use the overflow menu) \-\> tap "Edit feed" \-\> change the title, the tag, the full-text setting, the notification setting and the article opener \-\> tap Save.

**4\. Delete a feed**

**Actions:** Open the drawer \-\> long-press the feed \-\> tap "Delete feed" \-\> confirm.

**5\. Organise feeds into tags/groups**

**Actions:** Open the feed editor \-\> tap the tag field \-\> type a new tag name or pick an existing one \-\> tap Save; the drawer then groups the feeds under that tag.

**6\. Read an article**

**Actions:** Open a feed or the "All feeds" view \-\> tap an article \-\> the reader view opens with the title, image and text \-\> scroll to read \-\> swipe or use the navigation arrows to move to the next article.

**7\. Fetch the full article text**

**Actions:** Open the article \-\> tap the "Full text"/reader toggle in the toolbar (or enable "Fetch full articles" for the feed in its editor) \-\> the complete page content is downloaded and rendered.

**8\. Open an article in the browser**

**Actions:** Open the article \-\> tap the "Open in browser"/globe icon \-\> the page opens in the default browser or a custom tab according to the settings.

**9\. Mark an article as read or unread**

**Actions:** In the article list \-\> swipe the item sideways to toggle its read state, or open the article (which marks it read) and use the overflow menu \-\> "Mark as unread".

**10\. Mark all articles as read**

**Actions:** Open a feed or the All feeds view \-\> tap the "Mark all as read"/tick-all icon in the toolbar \-\> confirm.

**11\. Star (bookmark) an article**

**Actions:** Open the article \-\> tap the star/bookmark icon in the toolbar; starred articles are kept and can be filtered separately.

**12\. Filter the article list**

**Actions:** Open the article list \-\> tap the filter icon \-\> choose to show all articles, only unread articles, only starred articles or only recently read ones \-\> confirm.

**13\. Sort the article list**

**Actions:** Open the article list \-\> tap the overflow menu (three dots) \-\> tap the sort option \-\> choose newest first or oldest first.

**14\. Search articles**

**Actions:** Tap the search icon in the toolbar \-\> type the query \-\> review the matching articles \-\> tap one to open it.

**15\. Listen to an article with text to speech**

**Actions:** Open the article \-\> tap the "Read aloud"/text-to-speech icon in the toolbar \-\> use the play, pause and stop controls \-\> the reading continues in a notification.

**16\. Share an article**

**Actions:** Open the article \-\> tap the share icon \-\> choose the destination app in the Android share sheet.

**17\. Refresh feeds manually**

**Actions:** Open the article list \-\> pull down to refresh, or tap the sync/refresh icon in the toolbar \-\> wait for the update to complete.

**18\. Configure automatic background syncing**

**Actions:** Open Settings \-\> open the synchronisation section \-\> set the sync interval (for example every hour, every few hours or manually) \-\> choose whether syncing is limited to Wi-Fi and whether it runs while charging only.

**19\. Enable new-article notifications**

**Actions:** Open Settings (or the feed editor) \-\> enable notifications for the feed or globally \-\> grant the Android notification permission \-\> new items then produce a notification.

**20\. Import feeds from an OPML file**

**Actions:** Open the navigation drawer or Settings \-\> tap "Import feeds from OPML" \-\> select the .opml file with the picker \-\> confirm; the feeds and their tags are added.

**21\. Export feeds to an OPML file**

**Actions:** Open the drawer or Settings \-\> tap "Export feeds to OPML" \-\> choose the destination file name and folder \-\> confirm.

**22\. Synchronise read state between devices**

**Actions:** Open Settings \-\> open the device synchronisation section \-\> tap "Set up sync" \-\> create a sync chain on one device and copy the code/link \-\> on the other device tap "Join sync chain" and paste it \-\> confirm; read and starred states are then shared.

**23\. Set how many articles are kept per feed**

**Actions:** Open Settings \-\> tap the "Maximum number of items per feed"/retention entry \-\> choose the value \-\> confirm.

**24\. Choose the default article opener**

**Actions:** Open Settings (or the feed editor) \-\> tap the "Open articles with" entry \-\> choose the reader view, the custom tab or the external browser.

**25\. Change the theme**

**Actions:** Open Settings \-\> tap the theme entry \-\> choose light, dark, e-ink or "follow system" \-\> optionally enable dynamic (Material You) colours or the pure-black dark theme.

**26\. Change the reader font, text size and alignment**

**Actions:** Open Settings \-\> open the reader/text section \-\> set the font, the text size and whether the text is justified \-\> return.

**27\. Control image loading**

**Actions:** Open Settings \-\> open the image section \-\> choose whether images are loaded always, only on Wi-Fi or never \-\> optionally enable the thumbnail display in the article list.

**28\. Choose the swipe gesture behaviour**

**Actions:** Open Settings \-\> open the behaviour section \-\> set what a swipe on an article row does (for example mark as read or nothing) and whether swiping between articles is enabled.

**29\. Block articles by keyword**

**Actions:** Open Settings \-\> open the block list section \-\> tap "Add" \-\> enter the word or phrase to filter out \-\> confirm; matching articles are hidden from the lists.

**30\. Change the article list layout**

**Actions:** Open Settings \-\> tap the feed item style/layout entry \-\> choose the compact, card or super-compact presentation \-\> return.

**31\. View the about screen and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the version, the source link, the privacy policy and the open-source licences.

 

### **App Name: FitoTrack**

*Package: de.tadris.fitness  |  Version documented: F-Droid build 1630  |  Reference: Official FitoTrack repository (Codeberg) documentation and F-Droid listing*

**Features:**

**1\. Record a GPS workout**

**Actions:** Open the app \-\> tap the "+"/record button \-\> choose the activity type (for example running, cycling, hiking or walking) \-\> grant the location permission \-\> wait for the GPS fix indicator \-\> tap Start \-\> tap Stop and confirm when finished.

**2\. Choose the activity type before recording**

**Actions:** Tap the record button \-\> swipe or tap through the activity selector at the top \-\> select the sport \-\> the map and statistics adapt to that type.

**3\. Pause and resume a workout manually**

**Actions:** During recording \-\> tap the pause control \-\> the timer and distance stop accumulating \-\> tap resume to continue the same workout.

**4\. Use automatic pause detection**

**Actions:** Open Settings \-\> the recording section \-\> enable the auto-pause option and set the speed threshold \-\> during recording the workout pauses when you stop moving and resumes automatically.

**5\. See live statistics while recording**

**Actions:** Start a recording \-\> the screen shows the map with the current track and the live values (duration, distance, current and average speed, pace, ascent and heart rate where available).

**6\. Hear spoken announcements during a workout**

**Actions:** Open Settings \-\> open the announcements/voice section \-\> enable the spoken updates \-\> choose the interval (by time or by distance) and which values are announced (for example duration, distance, pace, speed, heart rate and workout state changes) \-\> start a workout.

**7\. Record an interval training session**

**Actions:** Open the navigation drawer \-\> tap "Interval sets" \-\> tap "+" to create a set \-\> add each interval with its name and duration \-\> save \-\> when starting a workout, select the interval set \-\> the app announces each interval change.

**8\. Record a heart rate with a Bluetooth sensor**

**Actions:** Open Settings \-\> the sensor/heart rate section \-\> scan for and pair the Bluetooth LE heart-rate strap \-\> start a workout; the live heart rate is shown and stored with the track.

**9\. Record an indoor workout**

**Actions:** Tap the record button \-\> select an indoor activity type (for example gym, rowing or exercise) \-\> tap Start \-\> enter the repetitions or let the app count the duration \-\> tap Stop to save.

**10\. Add a workout manually**

**Actions:** Open the workout list \-\> tap the overflow menu (three dots) \-\> tap "Add workout"/enter workout \-\> choose the activity type \-\> enter the date, duration, distance and comment \-\> tap Save.

**11\. Browse the workout list**

**Actions:** Open the app \-\> the main screen lists the recorded workouts with the date, type, duration and distance \-\> scroll and tap an entry to open it.

**12\. View a workout in detail**

**Actions:** Tap a workout in the list \-\> review the summary (date, duration, distance, average and maximum speed, pace, ascent, descent and energy) \-\> scroll to the map of the route and the charts.

**13\. View workout charts**

**Actions:** Open a workout \-\> tap the chart/diagram action \-\> switch between the speed, pace, height and heart-rate diagrams \-\> tap a point on the chart to see the value and its position on the map.

**14\. View the route on a map**

**Actions:** Open a workout \-\> tap the map \-\> the full-screen map opens \-\> pinch to zoom and drag to pan along the recorded track.

**15\. Edit a workout**

**Actions:** Open the workout \-\> tap the edit action \-\> change the activity type, the comment/title or the date \-\> tap Save.

**16\. Delete a workout**

**Actions:** Open the workout \-\> tap the overflow menu \-\> tap Delete \-\> confirm.

**17\. Share a workout**

**Actions:** Open the workout \-\> tap the share action \-\> choose whether to share the summary or the GPX file \-\> pick the destination app.

**18\. Export a workout as a GPX file**

**Actions:** Open the workout \-\> tap the overflow menu \-\> tap "Export as GPX"/share as file \-\> choose the destination \-\> confirm.

**19\. Import workouts from GPX files**

**Actions:** Open the navigation drawer or Settings \-\> tap the import option \-\> select the .gpx file(s) \-\> confirm; the tracks are added to the workout list.

**20\. Resume a stopped workout**

**Actions:** Open the workout list shortly after stopping \-\> open the workout \-\> tap the resume action \-\> recording continues and is appended to that workout.

**21\. View aggregated statistics**

**Actions:** Open the navigation drawer \-\> tap "Statistics" \-\> choose the activity type and the period (week, month or year) \-\> review the totals and the trend charts for distance, duration, speed and count.

**22\. Record and track body weight**

**Actions:** Open the navigation drawer or Settings \-\> open the user data section \-\> enter the current weight \-\> save; the value is used for the energy calculation and the history is kept.

**23\. Set the user data used for calculations**

**Actions:** Open Settings \-\> tap "User data" \-\> enter the weight and the other personal values \-\> confirm; the energy/calorie estimates are recalculated.

**24\. Create a backup of all workouts**

**Actions:** Open Settings \-\> tap the backup section \-\> tap "Export backup" \-\> choose the destination \-\> confirm; the complete database is written to a backup file.

**25\. Restore workouts from a backup**

**Actions:** Open Settings \-\> the backup section \-\> tap "Import backup" \-\> select the backup file \-\> choose whether to replace or merge \-\> confirm.

**26\. Change the map style and tile source**

**Actions:** Open Settings \-\> tap the map section \-\> choose the map style/tile server \-\> optionally enter a custom tile URL \-\> return.

**27\. Set the measurement units**

**Actions:** Open Settings \-\> tap the unit system entry \-\> choose metric or imperial \-\> optionally choose whether pace or speed is displayed \-\> return.

**28\. Adjust the GPS recording accuracy and interval**

**Actions:** Open Settings \-\> the recording section \-\> set the location update interval and the minimum accuracy threshold \-\> return.

**29\. Show the workout on the lock screen**

**Actions:** Open Settings \-\> the recording section \-\> toggle the "Show on lock screen" option; the live workout information appears above the lock screen while recording.

**30\. Change the app theme**

**Actions:** Open Settings \-\> tap the theme entry \-\> choose light, dark or "follow system" \-\> return.

**31\. View the about screen and licences**

**Actions:** Open the navigation drawer \-\> tap "About" \-\> read the version, the source repository link, the licence and the map data attribution.

 

### **App Name: OpenTracks**

*Package: de.dennisguse.opentracks  |  Version documented: F-Droid build 6741  |  Reference: Official OpenTracks repository documentation and F-Droid listing*

**Features:**

**1\. Record a track**

**Actions:** Open the app \-\> tap the record (play) floating action button \-\> grant the location permission \-\> wait for the GPS fix \-\> move along the route \-\> tap the stop button and confirm to finish the recording.

**2\. Choose the activity type for a recording**

**Actions:** Start or open a recording \-\> tap the activity type selector \-\> choose the sport (for example running, walking, cycling, mountain biking, skiing or driving) \-\> confirm; the icon and the speed/pace display change accordingly.

**3\. Pause and resume a recording**

**Actions:** While recording \-\> tap the pause control in the recording screen or the notification \-\> tap resume to continue the same track.

**4\. View live statistics while recording**

**Actions:** Start a recording \-\> the statistics screen shows the moving time, total time, distance, current speed or pace, average and maximum speed, altitude gain and the sensor values.

**5\. Add a marker (waypoint) during a recording**

**Actions:** While recording \-\> open the markers screen (or tap the marker action in the toolbar) \-\> tap "Add marker" \-\> enter the name, description and category \-\> optionally attach a photo \-\> tap Save.

**6\. Attach a photo to a marker**

**Actions:** Open the add-marker screen \-\> tap the camera action \-\> grant the camera permission \-\> take the picture \-\> confirm; the photo is stored with the marker.

**7\. Browse the track list**

**Actions:** Open the app \-\> the main screen lists the recorded tracks with their name, activity type, date, distance and duration \-\> scroll and tap an entry to open it.

**8\. View a track's statistics**

**Actions:** Tap a track \-\> open the statistics tab \-\> review the total distance, moving and total time, average and maximum speed or pace, altitude gain and loss, and the sensor summaries.

**9\. View a track's chart**

**Actions:** Open a track \-\> switch to the chart tab \-\> review the speed, pace, altitude and heart-rate curves plotted against distance or time \-\> switch the x-axis using the chart options.

**10\. View a track on a map**

**Actions:** Open a track \-\> tap the map action \-\> the track is displayed in the installed map application (for example the OSMDashboard companion app) showing the route and markers.

**11\. Edit a track's name, description and activity type**

**Actions:** Open the track \-\> tap the edit (pencil) action \-\> change the name, the description and the activity type \-\> tap Save.

**12\. Delete a track**

**Actions:** Open the track list \-\> long-press the track \-\> tap the delete action \-\> confirm; select several tracks first to delete them together.

**13\. Select and act on multiple tracks**

**Actions:** Long-press a track in the list \-\> tap further tracks to add them to the selection \-\> use the toolbar actions to share, export or delete them in one operation.

**14\. Share a track**

**Actions:** Open the track (or select it in the list) \-\> tap the share action \-\> choose the export format \-\> pick the destination app.

**15\. Export tracks to GPX, KML or KMZ**

**Actions:** Open the track list \-\> tap the overflow menu (three dots) \-\> tap "Export"/"Export all" \-\> choose the format (GPX, KML or KMZ, with or without photos) \-\> select the destination folder \-\> confirm.

**16\. Import tracks from files**

**Actions:** Open the overflow menu \-\> tap "Import" \-\> select the folder or the individual GPX/KML/KMZ files \-\> confirm; the tracks are added to the list.

**17\. View aggregated statistics**

**Actions:** Open the navigation drawer or the overflow menu \-\> tap "Aggregated statistics" \-\> filter by activity type and period \-\> review the totals for distance, time and number of activities.

**18\. Connect a Bluetooth heart-rate sensor**

**Actions:** Open Settings \-\> tap the sensors section \-\> tap the heart rate entry \-\> scan for and select the Bluetooth LE strap \-\> confirm; the heart rate is recorded with the track.

**19\. Connect cycling cadence, speed and power sensors**

**Actions:** Open Settings \-\> the sensors section \-\> tap the cadence, cycling speed or power entry \-\> pair the corresponding Bluetooth LE sensor \-\> enter the wheel circumference for the speed sensor \-\> confirm.

**20\. Connect a running speed and cadence sensor**

**Actions:** Open Settings \-\> the sensors section \-\> tap the running sensor entry \-\> pair the Bluetooth LE foot pod \-\> confirm.

**21\. Enable spoken announcements**

**Actions:** Open Settings \-\> tap the voice announcements section \-\> enable it \-\> set the frequency by distance or by time \-\> choose which values are spoken \-\> start a recording.

**22\. Configure the recording accuracy and intervals**

**Actions:** Open Settings \-\> the recording section \-\> set the minimum recording interval, the recording distance, the minimum GPS accuracy threshold and the idle-speed threshold \-\> return.

**23\. Set default track names and activity types**

**Actions:** Open Settings \-\> the recording/defaults section \-\> choose the default track name pattern (for example date and time or the activity type) and the default activity \-\> return.

**24\. Change the measurement units**

**Actions:** Open Settings \-\> tap the units entry \-\> choose metric or imperial \-\> choose whether speed or pace is shown \-\> return.

**25\. Customise which statistics are displayed**

**Actions:** Open Settings \-\> tap the layout/"Customise statistics screen" entry \-\> tick the values to show and drag them into the required order \-\> confirm.

**26\. Keep the screen on while recording**

**Actions:** Open Settings \-\> enable the option that prevents the screen from turning off during a recording \-\> return.

**27\. Change the theme**

**Actions:** Open Settings \-\> tap the theme entry \-\> choose light, dark or "follow system" \-\> return.

**28\. Allow other apps to read the track data**

**Actions:** Open Settings \-\> the API/dashboard section \-\> enable the public API/dashboard access \-\> confirm; companion apps such as the map dashboard can then display the recorded data.

**29\. Reset settings to the defaults**

**Actions:** Open Settings \-\> scroll to the reset entry \-\> tap it \-\> confirm.

**30\. View the about screen and licences**

**Actions:** Open the overflow menu \-\> tap "About" \-\> read the version, the source repository link and the licence.

 

### **App Name: ActivityDiary**

*Package: de.rampro.activitydiary  |  Version documented: F-Droid build 136  |  Reference: Official ActivityDiary repository, wiki and F-Droid listing*

**Features:**

**1\. Select the current activity to start tracking it**

**Actions:** Open the app \-\> the main screen shows the activity cards \-\> tap the activity you are starting; the previous activity is closed and the new one begins with the current timestamp.

**2\. Create a new activity**

**Actions:** Open the main screen \-\> tap the "+"/add action \-\> enter the activity name \-\> pick a colour \-\> tap Save; the app warns if a similar name already exists.

**3\. Edit an activity's name and colour**

**Actions:** Open the main screen \-\> long-press the activity card (or open its detail) \-\> tap the edit action \-\> change the name or colour \-\> tap Save.

**4\. Delete an activity**

**Actions:** Long-press the activity card \-\> tap the delete action \-\> confirm; the activity is removed from the selection list.

**5\. Attach a note to the current activity**

**Actions:** Start an activity \-\> tap the note field on the main screen \-\> type the text (for example what exactly you did) \-\> the note is stored with the current diary entry.

**6\. Attach a picture to the current activity**

**Actions:** With an activity running \-\> tap the camera action on the main screen \-\> grant the camera permission \-\> take the photo \-\> confirm; the picture is linked to the diary entry.

**7\. View attached pictures**

**Actions:** Open the main screen or the history entry \-\> tap the thumbnail of an attached image \-\> the picture opens full screen.

**8\. Browse the activity history (diary)**

**Actions:** Open the navigation drawer \-\> tap "History"/Diary \-\> scroll the chronological list of entries showing the activity, start time, duration, notes and pictures.

**9\. Edit a past diary entry**

**Actions:** Open the History view \-\> tap an entry \-\> change its activity, start or end time, or its note \-\> confirm the change.

**10\. Delete a diary entry**

**Actions:** Open the History view \-\> long-press the entry (or open it and use the delete action) \-\> confirm the deletion.

**11\. Undo the last activity change**

**Actions:** Immediately after switching activities \-\> tap the Undo action in the snackbar shown at the bottom of the screen; the previous activity is restored.

**12\. Search for an activity**

**Actions:** Open the main screen \-\> tap the search icon in the toolbar \-\> type part of the activity name \-\> the card list filters as you type \-\> tap the matching card to select it.

**13\. View statistics for your activities**

**Actions:** Open the navigation drawer \-\> tap "Statistics" \-\> select the period \-\> review how much time has been spent on each activity and how often each was started.

**14\. Use the ordering by likelihood**

**Actions:** Open the main screen \-\> the activity cards are ordered by how likely the activity is at the current time based on your history \-\> tap the most relevant card to start it.

**15\. See the current activity in the notification**

**Actions:** Start an activity \-\> pull down the notification shade \-\> the ongoing notification shows the running activity and its elapsed time \-\> tap it to return to the app.

**16\. Filter or reorder the activity list**

**Actions:** Open the main screen \-\> tap the overflow menu (three dots) \-\> choose the available sorting/filtering option \-\> confirm.

**17\. Configure application settings**

**Actions:** Open the navigation drawer \-\> tap "Settings" \-\> adjust the available preferences (for example the date and time display, the picture storage behaviour and the notification behaviour) \-\> return.

**18\. Read the built-in user guide and FAQ**

**Actions:** Open the navigation drawer \-\> tap the help/user guide entry \-\> read the built-in documentation or open the linked online wiki and FAQ.

**19\. Read the privacy policy**

**Actions:** Open the navigation drawer or Settings \-\> tap the privacy policy entry \-\> read the statement about what the app stores.

**20\. View the about screen and licences**

**Actions:** Open the navigation drawer \-\> tap "About" \-\> read the version number, the source repository link and the GPL licence information.

**21\. Export or back up the diary database**

**Actions:** Unable to verify for this build. A user-facing database export/backup action could not be confirmed against the official documentation for this version, so it is not documented here as an available feature.

 

### **App Name: Wikimedia Commons**

*Package: fr.free.nrw.commons  |  Version documented: F-Droid build 1066  |  Reference: Official Wikimedia Commons Android app repository documentation and F-Droid listing*

**Features:**

**1\. Log in with a Wikimedia account**

**Actions:** Open the app \-\> tap "Log in" on the welcome screen \-\> enter the Wikimedia username and password \-\> tap Login \-\> enter the two-factor code if the account uses 2FA.

**2\. Create a Wikimedia account**

**Actions:** Open the app \-\> tap "Sign up"/"Create an account" on the welcome screen \-\> complete the registration form in the opened view \-\> return to the app and log in.

**3\. Complete the introductory tutorial**

**Actions:** On first launch \-\> swipe through the welcome/tutorial screens explaining what may be uploaded \-\> tap "Yes" on the copyright question \-\> tap the finish/skip control.

**4\. Upload a photo from the device**

**Actions:** Tap the "+"/upload floating action button \-\> choose "Custom selector"/gallery \-\> select one or more images \-\> tap Next \-\> enter the title and description \-\> add categories \-\> choose the licence \-\> tap the upload/submit button.

**5\. Take a photo and upload it**

**Actions:** Tap the "+" button \-\> choose the camera option \-\> grant the camera permission \-\> take the picture \-\> continue through the title, description, category and licence steps \-\> tap upload.

**6\. Upload several files in one batch**

**Actions:** Tap the "+" button \-\> select multiple images in the picker \-\> tap Next \-\> complete the details for each image using the paging controls \-\> tap upload; the queue is processed in the background.

**7\. Add a title and description to an upload**

**Actions:** On the upload details screen \-\> enter the caption/title \-\> enter the description \-\> optionally switch the language selector to add the text in another language \-\> tap Next.

**8\. Add categories to an upload**

**Actions:** On the upload categories screen \-\> type a keyword in the search field \-\> tick the matching categories from the suggestions \-\> tap Next.

**9\. Add "depicts" statements to an upload**

**Actions:** On the depicts step of the upload flow \-\> search for the Wikidata item that the image shows \-\> tap the matching item to select it \-\> tap Next.

**10\. Choose the licence for an upload**

**Actions:** On the upload details screen \-\> tap the licence selector \-\> choose the licence (for example CC BY-SA 4.0, CC BY 4.0 or CC0) \-\> continue.

**11\. Add or edit location information for an upload**

**Actions:** On the upload details screen \-\> tap the location entry \-\> allow the app to read the image coordinates, or pick the position on the map \-\> confirm.

**12\. Monitor and manage the upload queue**

**Actions:** Open the navigation drawer \-\> tap "Contributions"/the uploads list \-\> review the pending, uploading and failed items \-\> tap the retry action on a failed upload or the cancel action to remove it.

**13\. Browse your own contributions**

**Actions:** Open the drawer \-\> tap "Contributions" \-\> scroll the grid of your uploaded files \-\> tap one to open its media details.

**14\. Find nearby places that need photos**

**Actions:** Open the drawer \-\> tap "Nearby" \-\> grant the location permission \-\> review the map pins or switch to the list view \-\> tap a place to see what is missing \-\> tap the camera action to photograph and upload it.

**15\. Filter the Nearby results**

**Actions:** Open the Nearby screen \-\> tap the filter/chip control \-\> choose the place types to show and whether places that already have pictures are included \-\> confirm.

**16\. Explore featured images and categories**

**Actions:** Open the drawer \-\> tap "Explore" \-\> switch between the featured pictures, picture of the day, mobile uploads and category browsing tabs \-\> tap an image to open it.

**17\. Search for images, categories and depictions**

**Actions:** Open the Explore or search screen \-\> tap the search field \-\> type the query \-\> switch between the media, categories and depictions result tabs \-\> tap a result.

**18\. View media details**

**Actions:** Tap any image in Explore, Nearby or Contributions \-\> read the title, description, author, upload date, licence, coordinates and the category list \-\> tap a category to browse it.

**19\. Bookmark images, categories or locations**

**Actions:** Open the media detail (or a Nearby place) \-\> tap the bookmark icon \-\> the item is saved \-\> open the drawer \-\> tap "Bookmarks" to review the saved items.

**20\. Edit the categories or depicts of an existing file**

**Actions:** Open a file you uploaded \-\> tap the edit action on the categories or depicts section \-\> add or remove the entries \-\> confirm; the change is submitted to Commons.

**21\. Review other users' uploads (peer review)**

**Actions:** Open the drawer \-\> tap "Review" \-\> a recent upload is shown \-\> answer the review questions about copyright, category and usefulness \-\> tap the appropriate action (for example "Yes", "No" or "Skip") to move to the next file.

**22\. View achievements and upload statistics**

**Actions:** Open the drawer \-\> tap "Achievements"/Profile \-\> review the counts of uploads, uploads used in articles, images featured and the level progress.

**23\. Read notifications from Commons**

**Actions:** Open the drawer \-\> tap "Notifications" \-\> read the messages from the Commons community \-\> tap one to open the related page.

**24\. Enable limited connection mode**

**Actions:** Open Settings \-\> enable the "Limited connection mode" option; uploads are then queued and only sent when a suitable connection is available.

**25\. Manage EXIF metadata redaction**

**Actions:** Open Settings \-\> tap the "Manage EXIF metadata"/redaction entry \-\> tick which metadata categories (for example location, camera model, date, author) are kept in uploaded files \-\> confirm.

**26\. Set the default licence for uploads**

**Actions:** Open Settings \-\> tap the default licence entry \-\> choose the licence used to pre-fill new uploads \-\> return.

**27\. Change the theme**

**Actions:** Open Settings \-\> tap the theme entry \-\> choose the light or dark theme \-\> return.

**28\. Change the app and description languages**

**Actions:** Open Settings \-\> tap the language entries \-\> choose the interface language and the default description language used in the upload form.

**29\. Enable or disable the campaign banners**

**Actions:** Open Settings \-\> toggle the campaigns option; running photo campaigns are then shown or hidden on the home screen.

**30\. Send log files to the developers**

**Actions:** Open Settings \-\> tap "Send log file"/feedback \-\> confirm; the diagnostic logs are attached to a report for the development team.

**31\. Log out of the account**

**Actions:** Open the drawer or Settings \-\> tap "Log out" \-\> confirm; the stored credentials are removed.

**32\. View the about screen and licences**

**Actions:** Open the drawer \-\> tap "About" \-\> read the version, the privacy policy, the user agreement, the credits and the open-source licences.

 

### **App Name: Breezy Weather**

*Package: org.breezyweather  |  Version documented: F-Droid build 60202  |  Reference: Official Breezy Weather repository documentation and F-Droid listing*

**Features:**

**1\. Add the current location**

**Actions:** Open the app \-\> tap the location/manage-locations entry \-\> tap the "+" button \-\> choose "Current location" \-\> grant the location permission \-\> confirm; the weather for the detected position is loaded.

**2\. Add a location by searching**

**Actions:** Open the location manager \-\> tap the "+" button \-\> tap the search option \-\> type the city or place name \-\> tap the matching result \-\> confirm; the location is added to the list.

**3\. Switch between saved locations**

**Actions:** Open the main screen \-\> swipe horizontally between the location pages, or open the location manager and tap the entry you want to view.

**4\. Reorder or delete saved locations**

**Actions:** Open the location manager \-\> long-press a location and drag it to a new position; swipe a location sideways (or use its overflow menu) and tap Delete \-\> confirm.

**5\. View the current conditions**

**Actions:** Open a location \-\> the header shows the current temperature, the "feels like" value, the condition text and the refresh time.

**6\. View the hourly forecast**

**Actions:** Open a location \-\> scroll to the hourly card \-\> swipe horizontally through the hours \-\> tap an hour to open the detailed hourly view.

**7\. View the daily forecast**

**Actions:** Open a location \-\> scroll to the daily card \-\> tap a day to expand the detail with the day and night conditions, the temperature range, wind, precipitation and sun times.

**8\. View the detailed weather charts**

**Actions:** Open the hourly or daily card \-\> tap the chart tabs to switch between temperature, precipitation, wind, humidity, UV index, cloud cover and visibility.

**9\. View precipitation nowcasting**

**Actions:** Open a location whose source supports nowcasting \-\> scroll to the precipitation/nowcast card \-\> read the minute-by-minute forecast for the next hour.

**10\. View the air quality index**

**Actions:** Open a location \-\> scroll to the air quality card \-\> read the AQI value and the individual pollutant levels (for example PM2.5, PM10, O3, NO2, SO2 and CO) \-\> tap the card for the hourly AQI trend.

**11\. View pollen levels**

**Actions:** Open a location whose source provides pollen data \-\> scroll to the pollen/allergen card \-\> read the levels for the individual allergens.

**12\. View sun, moon and moon phase information**

**Actions:** Open a location \-\> scroll to the sun and moon card \-\> read the sunrise, sunset, moonrise and moonset times and the current moon phase.

**13\. Read severe weather alerts**

**Actions:** Open a location \-\> tap the alert banner at the top of the screen (shown when a warning is active) \-\> read the full text, the severity and the validity period.

**14\. Refresh the weather data**

**Actions:** Open the main screen \-\> pull down to refresh \-\> wait for the update; the refresh time is shown at the bottom of the page.

**15\. Choose the weather data source for a location**

**Actions:** Open the location manager \-\> tap the location (or its edit action) \-\> tap the weather source entry \-\> choose the provider (for example Open-Meteo, MET Norway, AccuWeather, or another supported service) \-\> optionally set separate sources for air quality, pollen, minutely precipitation, alerts and normals \-\> confirm.

**16\. Configure API keys for sources that need them**

**Actions:** Open Settings \-\> tap the weather sources section \-\> select the provider \-\> enter the API key in the field \-\> confirm.

**17\. Set the background update interval**

**Actions:** Open Settings \-\> tap the background updates section \-\> choose the refresh interval (for example every one, two, four or eight hours, or never) \-\> optionally allow updates only when charging or on Wi-Fi.

**18\. Enable the ongoing weather notification**

**Actions:** Open Settings \-\> tap the notifications section \-\> enable the persistent/ongoing notification \-\> choose what it displays (temperature, condition icon, feels-like value) \-\> grant the notification permission.

**19\. Enable the daily forecast notification**

**Actions:** Open Settings \-\> notifications \-\> enable the today and/or tomorrow forecast notification \-\> set the delivery time \-\> confirm.

**20\. Enable alert and precipitation notifications**

**Actions:** Open Settings \-\> notifications \-\> enable the severe-weather alert notification and the precipitation notification \-\> confirm.

**21\. Add a home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Breezy Weather \-\> drag the required widget type (for example the day, day and week, clock and weather, multi-city, text or trend widget) onto the home screen \-\> configure the appearance \-\> tap Save.

**22\. Configure the widget appearance**

**Actions:** Open Settings \-\> tap the widgets section (or tap the settings control on the widget) \-\> set the card style, the text colour, the transparency, the displayed values and whether the widget follows the app theme \-\> confirm.

**23\. Change the units**

**Actions:** Open Settings \-\> tap the units section \-\> set the temperature unit (Celsius or Fahrenheit), the precipitation unit, the wind speed unit, the pressure unit and the distance unit \-\> return.

**24\. Change the theme and colours**

**Actions:** Open Settings \-\> tap the appearance section \-\> choose the day/night theme behaviour \-\> optionally enable the Material You dynamic colours \-\> return.

**25\. Choose an icon pack**

**Actions:** Open Settings \-\> appearance \-\> tap the icon pack entry \-\> select an installed icon pack \-\> confirm; the weather icons change throughout the app.

**26\. Reorder or hide the detail cards**

**Actions:** Open Settings \-\> appearance \-\> tap the "Cards"/main screen entry \-\> tick the cards to show (for example hourly, daily, precipitation, air quality, pollen, sun and moon, wind, UV, humidity, pressure, visibility) \-\> drag them into the required order \-\> confirm.

**27\. Set the app language**

**Actions:** Open Settings \-\> tap the language entry \-\> choose the interface language \-\> confirm.

**28\. Enable the live wallpaper**

**Actions:** Open Settings \-\> tap the live wallpaper entry \-\> configure the weather animation options \-\> apply it through the Android wallpaper picker.

**29\. Import and export the app settings and locations**

**Actions:** Open Settings \-\> tap the backup/data section \-\> tap Export to write the configuration to a file, or tap Import and select a previously exported file \-\> confirm.

**30\. View the about screen, changelog and licences**

**Actions:** Open Settings \-\> tap "About" \-\> read the version, the changelog, the data source attributions, the privacy policy and the open-source licences.

 

### **App Name: Organic Maps**

*Package: app.organicmaps  |  Version documented: F-Droid build 26072306  |  Reference: Official Organic Maps documentation and F-Droid listing*

**Features:**

**1\. Download an offline map**

**Actions:** Open the app \-\> open the main menu (the hamburger/menu button) \-\> tap "Download Maps" \-\> browse the continent and country list (or search for the region) \-\> tap the download icon beside the region \-\> wait for the download to finish.

**2\. Update or delete a downloaded map**

**Actions:** Open the menu \-\> tap "Download Maps" \-\> open the "Downloaded" list \-\> tap the update icon on a region with a newer version, or long-press the region \-\> tap Delete \-\> confirm.

**3\. Find your current position**

**Actions:** Tap the location (arrow) button on the map \-\> grant the location permission \-\> the map centres on your position \-\> tap the button again to enable the follow-and-rotate compass mode.

**4\. Search for a place by name**

**Actions:** Tap the search field at the top of the map \-\> type the place, address or POI name \-\> tap a result in the list \-\> the place page opens and the map moves to it.

**5\. Search by category**

**Actions:** Tap the search field \-\> tap one of the category buttons (for example Food, Fuel, ATM, Hotel, Transport, Pharmacy, Toilets or Attractions) \-\> review the nearby results in the list or on the map.

**6\. Reuse a recent search**

**Actions:** Tap the search field \-\> open the History tab \-\> tap a previous query to run it again; use the clear action to erase the history.

**7\. View a place page**

**Actions:** Tap a point of interest on the map (or a search result) \-\> the place sheet opens showing the name, category, address, opening hours, phone number, website, Wikipedia extract and coordinates \-\> drag the sheet up for the full detail.

**8\. Build a route**

**Actions:** Open a place page \-\> tap the "Route to"/directions button \-\> choose the travel mode (driving, walking, cycling, public transport or the ruler) \-\> tap "Start" to begin turn-by-turn navigation.

**9\. Set a custom start point for a route**

**Actions:** Open the routing panel \-\> tap the start field \-\> tap "My position" or long-press a point on the map and choose "Route from" \-\> the route is recalculated.

**10\. Add intermediate stops to a route**

**Actions:** With a route planned \-\> open a place page or long-press the map \-\> tap "Add stop"/the intermediate point action \-\> the waypoint is inserted into the route.

**11\. Use turn-by-turn voice guidance**

**Actions:** Start navigation \-\> the app announces the manoeuvres; tap the sound icon in the navigation panel to mute or unmute it, or open Settings \-\> "Voice instructions" to change the language and the announcement options.

**12\. See speed limits and speed camera warnings**

**Actions:** Start driving navigation \-\> the current speed and speed limit are displayed; open Settings \-\> the speed camera entry \-\> choose whether cameras are announced always, only in navigation, or never.

**13\. Measure a distance with the ruler**

**Actions:** Open a place page or the routing panel \-\> select the ruler travel mode \-\> tap the start and end points on the map \-\> read the straight-line distance shown.

**14\. Save a place as a bookmark**

**Actions:** Open the place page \-\> tap the bookmark (star/heart) icon \-\> choose the bookmark list, the colour and the icon \-\> optionally add a description \-\> confirm.

**15\. Create and manage bookmark lists**

**Actions:** Open the menu \-\> tap "Bookmarks and Tracks" \-\> tap the "+"/new list action \-\> enter the list name \-\> tap OK; use the visibility toggle to show or hide a list on the map, and the overflow menu to rename, delete or share it.

**16\. Import bookmarks and tracks from a file**

**Actions:** Open a KML, KMZ or GPX file from a file manager or an email attachment \-\> choose Organic Maps \-\> confirm the import; the list appears under "Bookmarks and Tracks".

**17\. Export or share a bookmark list**

**Actions:** Open "Bookmarks and Tracks" \-\> tap the overflow menu on the list \-\> tap "Export"/Share \-\> choose the file format \-\> pick the destination app or folder.

**18\. Record a track**

**Actions:** Open the menu \-\> tap the track recorder entry \-\> tap Start \-\> move along the route \-\> tap Stop and confirm to save the recording into a bookmark list.

**19\. Share your location or a place**

**Actions:** Open a place page (or long-press your position) \-\> tap the share icon \-\> choose whether to share the coordinates or the link \-\> pick the destination app.

**20\. Switch the map style between day and night**

**Actions:** Open the menu \-\> tap the map style/appearance entry \-\> choose Day, Night or Auto (which follows the sunset and sunrise) \-\> return to the map.

**21\. Enable the subway layer**

**Actions:** Open the layers control on the map \-\> tap "Subway" \-\> the metro network and stations are drawn on top of the map.

**22\. Enable the isolines (terrain contour) layer**

**Actions:** Open the layers control \-\> tap "Isolines" \-\> download the additional data if prompted \-\> the contour lines are displayed.

**23\. Enable the outdoor/hiking layer**

**Actions:** Open the layers control \-\> tap the outdoor layer \-\> hiking, cycling and piste routes are highlighted on the map.

**24\. Show or hide the traffic-free extras (3D buildings, zoom buttons)**

**Actions:** Open Settings \-\> toggle the "3D buildings" and "Zoom buttons" options \-\> return to the map.

**25\. Edit a place in OpenStreetMap**

**Actions:** Open the place page \-\> tap the "Edit place" action \-\> change the name, category, opening hours, phone, website or other attributes \-\> tap the save (tick) button \-\> upload the change when connected.

**26\. Add a new place to OpenStreetMap**

**Actions:** Long-press the map at the position of the missing place \-\> tap "Add place" on the sheet \-\> choose the category \-\> enter the name and details \-\> tap the save button.

**27\. Log in with an OpenStreetMap account**

**Actions:** Open the menu \-\> tap "OpenStreetMap profile"/the login entry \-\> sign in with the OSM credentials \-\> your edits are then attributed to that account.

**28\. Review and upload pending map edits**

**Actions:** Open the menu \-\> tap the OSM edits entry \-\> review the local changes \-\> tap the upload action \-\> confirm.

**29\. Report a mapping problem**

**Actions:** Open the place page \-\> tap the overflow/"Report a problem" action \-\> choose the issue type (for example the place does not exist or the data is incorrect) \-\> confirm.

**30\. Change the measurement units**

**Actions:** Open Settings \-\> tap the units entry \-\> choose kilometres or miles \-\> return.

**31\. Calibrate the compass**

**Actions:** Open Settings \-\> tap the "Calibrate compass" entry \-\> follow the on-screen figure-of-eight movement instruction.

**32\. Keep the screen on while navigating**

**Actions:** Open Settings \-\> enable the "Keep the screen on"/power-saving option \-\> choose the behaviour (never, always or automatic).

**33\. Restrict mobile data usage**

**Actions:** Open Settings \-\> tap the mobile data entry \-\> choose whether the app may use mobile data always, ask each time, or never; offline maps are used otherwise.

**34\. Enable automatic map downloads**

**Actions:** Open Settings \-\> enable the "Auto-download maps" option; the map for the region you enter is fetched automatically over the allowed connection.

**35\. View the about screen, help and donation links**

**Actions:** Open the menu \-\> tap "Settings" \-\> tap "About"/Help \-\> read the version, the FAQ, the OpenStreetMap attribution, the licences and the donation link.

 

### **App Name: Odyssey**

*Package: org.gateshipone.odyssey  |  Version documented: F-Droid build 42  |  Reference: Official Odyssey repository documentation and F-Droid/store listing*

**Features:**

**1\. Browse the music library by album**

**Actions:** Open the app \-\> grant the media permission \-\> tap the "Albums" tab in My Music \-\> scroll the album grid \-\> tap an album to open its track list.

**2\. Browse the music library by artist**

**Actions:** Open the "Artists" tab \-\> tap an artist \-\> review their albums \-\> tap an album to see its tracks.

**3\. Browse all tracks**

**Actions:** Open the "All tracks"/Tracks tab \-\> scroll the alphabetical list \-\> tap a track to play it.

**4\. Browse recently added albums**

**Actions:** Open the "Recent albums"/recently added section \-\> tap an album to open or play it.

**5\. Browse the file system with the file browser**

**Actions:** Open the navigation drawer \-\> tap "Files"/the file browser \-\> navigate the folders on the device \-\> tap an audio file to play it, or use the folder action to play or enqueue the whole folder.

**6\. Play a track**

**Actions:** Tap a track in any list \-\> playback starts and the now-playing bar appears at the bottom \-\> drag the bar upwards to open the full player.

**7\. Control playback from the full player**

**Actions:** Drag up the now-playing bar \-\> use play/pause, previous and next \-\> drag the seek bar to move within the track \-\> tap the down arrow to collapse the player.

**8\. Use repeat and shuffle**

**Actions:** Open the full player \-\> tap the repeat icon to cycle through off, repeat all and repeat one \-\> tap the shuffle icon to toggle random playback.

**9\. View and edit the play queue**

**Actions:** Open the full player \-\> switch to the queue/playlist view \-\> drag an item to reorder it \-\> swipe an item away to remove it \-\> tap an item to jump to it.

**10\. Add an album, artist or track to the queue**

**Actions:** Long-press the item (or tap its overflow menu) \-\> choose "Play", "Enqueue"/"Add to queue" or "Play next" \-\> the selection is appended to or inserted into the queue.

**11\. Clear the play queue**

**Actions:** Open the full player or the queue view \-\> tap the overflow menu \-\> tap the clear/"Clear playlist" action \-\> confirm.

**12\. Save the current queue as a playlist**

**Actions:** Open the full player or queue view \-\> tap the overflow menu \-\> tap "Save playlist" \-\> enter the playlist name \-\> tap OK.

**13\. Browse and play saved playlists**

**Actions:** Open the "Playlists" tab \-\> tap a playlist to see its tracks \-\> tap a track to play from that playlist, or use the overflow menu to play or enqueue the whole playlist.

**14\. Delete a playlist**

**Actions:** Open the Playlists tab \-\> long-press the playlist \-\> tap the delete action \-\> confirm.

**15\. Create a bookmark to resume an audiobook or podcast**

**Actions:** While playing \-\> open the full player or the overflow menu \-\> tap "Create bookmark" \-\> enter a name \-\> tap OK; the current queue and playback position are stored.

**16\. Resume from a bookmark**

**Actions:** Open the navigation drawer \-\> tap "Bookmarks" \-\> tap the bookmark \-\> the saved queue is restored and playback resumes from the stored position.

**17\. Delete a bookmark**

**Actions:** Open the Bookmarks view \-\> long-press the bookmark \-\> tap the delete action \-\> confirm.

**18\. Search the library**

**Actions:** Tap the search icon in the toolbar \-\> type the query \-\> review the matching artists, albums and tracks \-\> tap a result to play or open it.

**19\. Jump from a track to its album or artist**

**Actions:** Long-press a track (or open the player overflow menu) \-\> tap "Show album" or "Show artist" \-\> the corresponding detail view opens.

**20\. View track and album information**

**Actions:** Long-press a track \-\> tap the details/information action \-\> read the title, artist, album, track number, duration and file path.

**21\. Download artwork for artists and albums**

**Actions:** Open Settings \-\> the artwork section \-\> choose the artwork provider (Fanart.tv, Last.fm or MusicBrainz) \-\> enable the automatic download \-\> optionally tap the bulk download action to fetch the missing images.

**22\. Clear the artwork cache**

**Actions:** Open Settings \-\> the artwork section \-\> tap the "Clear image cache"/clear artwork action \-\> confirm.

**23\. Restrict artwork downloads to Wi-Fi**

**Actions:** Open Settings \-\> the artwork section \-\> enable the Wi-Fi-only download option \-\> return.

**24\. Control playback from the lock screen and the notification**

**Actions:** Start playback \-\> pull down the notification shade or wake the lock screen \-\> use the play/pause, previous, next and stop controls shown with the album art.

**25\. Add the Odyssey home screen widget**

**Actions:** Long-press an empty area of the Android home screen \-\> tap Widgets \-\> find Odyssey \-\> drag the widget onto the home screen \-\> use its controls to play, pause and skip without opening the app.

**26\. Scrobble to Last.fm through a scrobbler app**

**Actions:** Install a compatible scrobbler such as Simple Last.fm Scrobbler \-\> configure it with the Last.fm account \-\> play music in Odyssey; the track changes are broadcast and scrobbled automatically.

**27\. Open the system equaliser**

**Actions:** Open the navigation drawer or the player overflow menu \-\> tap the equaliser entry \-\> the system audio effects panel opens \-\> adjust the bands and presets \-\> return.

**28\. Change the theme**

**Actions:** Open Settings \-\> tap the theme entry \-\> choose one of the Material colour themes and the light, dark or OLED-black variant \-\> the app restarts the view with the new theme.

**29\. Change the library view style**

**Actions:** Open Settings \-\> the library/appearance section \-\> choose whether albums and artists are shown as a grid or as a list \-\> return.

**30\. Change the album and track sort order**

**Actions:** Open Settings \-\> the library section \-\> tap the album sort entry \-\> choose the ordering (for example by name or by year) \-\> return.

**31\. Configure playback behaviour**

**Actions:** Open Settings \-\> the playback section \-\> set the resume step size for the seek controls, the behaviour on headphone disconnect and the hardware media-button handling \-\> return.

**32\. Rescan the media library**

**Actions:** Open Settings (or the drawer) \-\> tap the library refresh/rescan action \-\> wait for the Android media scanner to finish \-\> the new files appear in the lists.

**33\. View the about screen and licences**

**Actions:** Open the navigation drawer \-\> tap "About" \-\> read the version number, the source repository link and the GPL licence information.

