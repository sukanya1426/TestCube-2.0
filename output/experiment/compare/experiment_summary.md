# Experiment summary

Budget: 3600s wall clock per tool per app (grace 300s).

| App | Package | Methods | Status | TestCube | LLMDroid | Elapsed | Note |
| --- | --- | ---: | --- | --- | --- | ---: | --- |
| amaze | com.amaze.filemanager | 60810 | skipped_verify | - | - | 0h00m00s | dex does not verify (4 VerifyError/FATAL lines) |
| fossifyclock | org.fossify.clock | 27793 | partial | - | rc=3 | 1h11m38s | steps not clean: llmdroid |
| fossifycontacts | org.fossify.contacts | 62716 | ok | - | ok | 1h09m01s |  |
| fossifyvoicerecorder | org.fossify.voicerecorder | 29941 | ok | - | ok | 1h04m09s |  |
| loophabits | org.isoron.uhabits | 41715 | ok | - | ok | 7h31m50s |  |

3 of 5 completed cleanly; 1 never got past the instrumentation gate.

Gated out (compatibility is measured, not assumed):

- `amaze` - dex does not verify (4 VerifyError/FATAL lines)
