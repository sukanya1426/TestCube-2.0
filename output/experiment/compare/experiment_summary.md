# Experiment summary

Budget: 3600s wall clock per tool per app (grace 300s).

| App | Package | Methods | Status | TestCube | LLMDroid | Elapsed | Note |
| --- | --- | ---: | --- | --- | --- | ---: | --- |
| markor | net.gsantner.markor | 61884 | ok | - | ok | 1h00m18s |  |
| materialfiles | me.zhanghai.android.files | 33328 | ok | - | ok | 1h00m21s |  |
| nononsensenotes | com.nononsenseapps.notepad | 15514 | ok | - | ok | 1h00m19s |  |
| odyssey | org.gateshipone.odyssey | 55027 | ok | - | ok | 1h00m19s |  |
| omninotes | it.feio.android.omninotes.foss | 33780 | ok | - | ok | 1h00m16s |  |
| opencamera | net.sourceforge.opencamera | 36079 | ok_hard_stop | - | hard_stop | 1h05m20s | llmdroid overran its budget and was stopped by the watchdog; coverage was still written |
| opentasks | org.dmfs.tasks | 25768 | ok | - | ok | 1h00m25s |  |
| radiodroid | net.programmierecke.radiodroid2 | 91188 | ok_hard_stop | - | hard_stop | 1h05m17s | llmdroid overran its budget and was stopped by the watchdog; coverage was still written |

6 of 8 completed cleanly; 0 never got past the instrumentation gate.
