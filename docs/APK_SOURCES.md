# APK sources

The exact builds this experiment uses. `apks/` is **not** in git (it is 1.1 GB and
`*.apk` is gitignored); it is rebuilt from this table instead.

```bash
python scripts/fetch_apks.py            # all 30
python scripts/fetch_apks.py --only markor,aegis
```

`run_experiment.py` also fetches a missing APK automatically at run time
(`auto_fetch_apks` in `experiment/config.json`), so a fresh clone can go straight
to running an experiment.

**20 of 30 instrument cleanly.** The rest are listed so the set stays reproducible.

| App | Package | Version | Instruments | URL |
| --- | --- | --- | --- | --- |
| `money` | `com.money.manager.ex` | 5.5.10 | yes | [apk](https://f-droid.org/repo/com.money.manager.ex_1115.apk) |
| `newpipe` | `org.schabi.newpipe` | code 997 *(pinned)* | yes | [apk](https://f-droid.org/repo/org.schabi.newpipe_997.apk) |
| `markor` | `net.gsantner.markor` | 2.16.1 | yes | [apk](https://f-droid.org/repo/net.gsantner.markor_163.apk) |
| `omninotes` | `it.feio.android.omninotes.foss` | 6.3.1 | yes | [apk](https://f-droid.org/repo/it.feio.android.omninotes.foss_331.apk) |
| `joplin` | `net.cozic.joplin` | 3.7.8 | **no** | [apk](https://f-droid.org/repo/net.cozic.joplin_2097817.apk) |
| `nononsensenotes` | `com.nononsenseapps.notepad` | 7.2.6 | yes | [apk](https://f-droid.org/repo/com.nononsenseapps.notepad_72600.apk) |
| `ankidroid` | `com.ichi2.anki` | 2.24.0 | **no** | [apk](https://f-droid.org/repo/com.ichi2.anki_22400300.apk) |
| `opentasks` | `org.dmfs.tasks` | 1.4.2 | yes | [apk](https://f-droid.org/repo/org.dmfs.tasks_82200.apk) |
| `loophabits` | `org.isoron.uhabits` | 2.3.1 | yes | [apk](https://f-droid.org/repo/org.isoron.uhabits_20301.apk) |
| `myexpenses` | `org.totschnig.myexpenses` | 4.1.0.2 | **no** | [apk](https://f-droid.org/repo/org.totschnig.myexpenses_871.apk) |
| `amaze` | `com.amaze.filemanager` | 3.11.3 | yes | [apk](https://f-droid.org/repo/com.amaze.filemanager_125.apk) |
| `materialfiles` | `me.zhanghai.android.files` | 1.7.4 | yes | [apk](https://f-droid.org/repo/me.zhanghai.android.files_39.apk) |
| `fossifyfiles` | `org.fossify.filemanager` | 1.6.1 | **no** | [apk](https://f-droid.org/repo/org.fossify.filemanager_13.apk) |
| `etar` | `ws.xsoh.etar` | 1.0.57 | **no** | [apk](https://f-droid.org/repo/ws.xsoh.etar_57.apk) |
| `fossifycalendar` | `org.fossify.calendar` | 1.10.3 | **no** | [apk](https://f-droid.org/repo/org.fossify.calendar_20.apk) |
| `fossifycontacts` | `org.fossify.contacts` | 1.6.0 | yes | [apk](https://f-droid.org/repo/org.fossify.contacts_13.apk) |
| `vlc` | `org.videolan.vlc` | 3.7.1 | yes | [apk](https://f-droid.org/repo/org.videolan.vlc_13070108.apk) |
| `auxio` | `org.oxycblt.auxio` | 4.1.5 | **no** | [apk](https://f-droid.org/repo/org.oxycblt.auxio_75.apk) |
| `fossifymusic` | `org.fossify.musicplayer` | 1.8.1 | **no** | [apk](https://f-droid.org/repo/org.fossify.musicplayer_14.apk) |
| `odyssey` | `org.gateshipone.odyssey` | 1.4.0 | yes | [apk](https://f-droid.org/repo/org.gateshipone.odyssey_42.apk) |
| `radiodroid` | `net.programmierecke.radiodroid2` | 0.86 | yes | [apk](https://f-droid.org/repo/net.programmierecke.radiodroid2_96.apk) |
| `transistor` | `org.y20k.transistor` | 4.3.8 | **no** | [apk](https://f-droid.org/repo/org.y20k.transistor_115.apk) |
| `aegis` | `com.beemdevelopment.aegis` | 3.4.2 | yes | [apk](https://f-droid.org/repo/com.beemdevelopment.aegis_81.apk) |
| `keepassdx` | `com.kunzisoft.keepass.libre` | 4.5.4 | yes | [apk](https://f-droid.org/repo/com.kunzisoft.keepass.libre_45400.apk) |
| `opencamera` | `net.sourceforge.opencamera` | 1.56.2 | yes | [apk](https://f-droid.org/repo/net.sourceforge.opencamera_96.apk) |
| `fossifygallery` | `org.fossify.gallery` | 1.13.1 | yes | [apk](https://f-droid.org/repo/org.fossify.gallery_28.apk) |
| `fossifynotes` | `org.fossify.notes` | 1.7.0 | yes | [apk](https://f-droid.org/repo/org.fossify.notes_13.apk) |
| `fossifyclock` | `org.fossify.clock` | 1.6.0 | yes | [apk](https://f-droid.org/repo/org.fossify.clock_10.apk) |
| `fossifyvoicerecorder` | `org.fossify.voicerecorder` | 1.7.1 | yes | [apk](https://f-droid.org/repo/org.fossify.voicerecorder_18.apk) |
| `feeder` | `com.nononsenseapps.feeder` | 2.22.0 | **no** | [apk](https://f-droid.org/repo/com.nononsenseapps.feeder_4050.apk) |

## Notes

- Builds are served from the official F-Droid repository; older ones move to
  `https://f-droid.org/archive/`, which the fetcher falls back to automatically.
- Every download is verified as a real APK whose package matches this table before
  it is kept, so a truncated or wrong file never reaches an experiment run.
- **newpipe is pinned to 0.27.0 (versionCode 997).** F-Droid's latest is 0.29.1,
  which fails instrumentation on the Soot `[0..1]` bug. Without the pin a clean
  rebuild of `apks/` would quietly produce an unusable APK. Set `pin_version_code`
  in `experiment/apps.json` whenever latest-is-broken applies.
- Licensing: these are third-party open-source apps. Redistributing the binaries is
  not necessary and is not done; only the download instructions live in git.
