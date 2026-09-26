# Experiment summary

Budget: 3600s wall clock per tool per app (grace 300s).

| App | Package | Methods | Status | TestCube | LLMDroid | Elapsed | Note |
| --- | --- | ---: | --- | --- | --- | ---: | --- |
| money | com.money.manager.ex | - | skipped_instrumentation | - | - | 0h00m00s | Soot [0..1] bug (Integer1Type leaked from the type assigner) |
| newpipe | org.schabi.newpipe | 74478 | partial | ok | rc=1 | 0h29m42s | steps not clean: llmdroid |
| markor | net.gsantner.markor | 61884 | partial | ok | rc=1 | 0h09m55s | steps not clean: llmdroid |
| omninotes | it.feio.android.omninotes.foss | 33780 | partial | ok | rc=1 | 0h29m20s | steps not clean: llmdroid |
| joplin | net.cozic.joplin | - | skipped_instrumentation | - | - | 0h00m00s | Soot [0..1] bug (Integer1Type leaked from the type assigner) |
| nononsensenotes | com.nononsenseapps.notepad | 15514 | partial | ok | rc=1 | 0h28m18s | steps not clean: llmdroid |
| ankidroid | com.ichi2.anki | - | skipped_instrumentation | - | - | 0h00m00s | Soot [0..1] bug (Integer1Type leaked from the type assigner) |
| opentasks | org.dmfs.tasks | 25768 | partial | ok | rc=1 | 0h30m51s | steps not clean: llmdroid |
| loophabits | org.isoron.uhabits | 41715 | partial | ok | rc=1 | 0h27m58s | steps not clean: llmdroid |
| myexpenses | org.totschnig.myexpenses | - | skipped_instrumentation | - | - | 0h00m00s | instrumentation failed (rc=1) |
| amaze | com.amaze.filemanager | 60810 | partial | ok | rc=1 | 0h39m49s | steps not clean: llmdroid |
| materialfiles | me.zhanghai.android.files | 33328 | partial | ok | rc=1 | 0h05m24s | steps not clean: llmdroid |
| fossifyfiles | org.fossify.filemanager | - | skipped_instrumentation | - | - | 0h00m00s | Soot [0..1] bug (Integer1Type leaked from the type assigner) |
| etar | ws.xsoh.etar | - | skipped_instrumentation | - | - | 0h00m00s | Soot [0..1] bug (Integer1Type leaked from the type assigner) |
| fossifycalendar | org.fossify.calendar | - | skipped_instrumentation | - | - | 0h00m00s | Soot [0..1] bug (Integer1Type leaked from the type assigner) |
| fossifycontacts | org.fossify.contacts | 62716 | partial | ok | rc=1 | 0h31m37s | steps not clean: llmdroid |
| vlc | org.videolan.vlc | - | skipped_instrumentation | - | - | 0h00m00s | instrumentation failed (rc=1) |
| auxio | org.oxycblt.auxio | - | skipped_instrumentation | - | - | 0h00m00s | Soot [0..1] bug (Integer1Type leaked from the type assigner) |
| fossifymusic | org.fossify.musicplayer | - | skipped_instrumentation | - | - | 0h00m00s | instrumentation failed (rc=1) |
| odyssey | org.gateshipone.odyssey | 55027 | partial | ok | rc=1 | 0h39m42s | steps not clean: llmdroid |
| radiodroid | net.programmierecke.radiodroid2 | 91188 | partial | ok | rc=1 | 0h29m08s | steps not clean: llmdroid |
| transistor | org.y20k.transistor | - | skipped_instrumentation | - | - | 0h00m00s | Soot [0..1] bug (Integer1Type leaked from the type assigner) |
| aegis | com.beemdevelopment.aegis | 26432 | partial | ok | rc=1 | 0h16m50s | steps not clean: llmdroid |
| keepassdx | com.kunzisoft.keepass.libre | 111626 | partial | ok | rc=1 | 0h26m02s | steps not clean: llmdroid |
| opencamera | net.sourceforge.opencamera | 36079 | partial | ok | rc=1 | 0h38m45s | steps not clean: llmdroid |
| fossifygallery | org.fossify.gallery | 44309 | skipped_verify | - | - | 0h00m00s | dex does not verify (5 VerifyError/FATAL lines) |
| fossifynotes | org.fossify.notes | - | skipped_instrumentation | - | - | 0h00m00s | instrumentation failed (rc=1) |
| fossifyclock | org.fossify.clock | 27793 | partial | ok | rc=1 | 0h29m34s | steps not clean: llmdroid |
| fossifyvoicerecorder | org.fossify.voicerecorder | 29941 | partial | ok | rc=1 | 0h32m08s | steps not clean: llmdroid |
| feeder | com.nononsenseapps.feeder | 58186 | skipped_verify | - | - | 0h00m00s | dex does not verify (1 VerifyError/FATAL lines) |

0 of 30 completed cleanly; 14 never got past the instrumentation gate.

Gated out (compatibility is measured, not assumed):

- `money` - Soot [0..1] bug (Integer1Type leaked from the type assigner)
- `joplin` - Soot [0..1] bug (Integer1Type leaked from the type assigner)
- `ankidroid` - Soot [0..1] bug (Integer1Type leaked from the type assigner)
- `myexpenses` - instrumentation failed (rc=1)
- `fossifyfiles` - Soot [0..1] bug (Integer1Type leaked from the type assigner)
- `etar` - Soot [0..1] bug (Integer1Type leaked from the type assigner)
- `fossifycalendar` - Soot [0..1] bug (Integer1Type leaked from the type assigner)
- `vlc` - instrumentation failed (rc=1)
- `auxio` - Soot [0..1] bug (Integer1Type leaked from the type assigner)
- `fossifymusic` - instrumentation failed (rc=1)
- `transistor` - Soot [0..1] bug (Integer1Type leaked from the type assigner)
- `fossifygallery` - dex does not verify (5 VerifyError/FATAL lines)
- `fossifynotes` - instrumentation failed (rc=1)
- `feeder` - dex does not verify (1 VerifyError/FATAL lines)
