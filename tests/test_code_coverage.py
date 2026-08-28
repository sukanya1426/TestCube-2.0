"""Tests for runtime code-coverage monitoring (droidbot/coverage)."""

import json
import os
import zipfile

import pytest

from droidbot.coverage import make_monitor
from droidbot.coverage.androlog_monitor import (
    AndroLogCVMonitor,
    total_methods_from_apk,
)


def _monitor(tmp_path, total=100, tag="TEST_LOG"):
    return AndroLogCVMonitor(save_dir=str(tmp_path), tag=tag, total_methods=total)


def test_make_monitor_none_disabled(tmp_path):
    assert make_monitor("none", str(tmp_path)) is None
    assert make_monitor(None, str(tmp_path)) is None


def test_make_monitor_unknown_method(tmp_path):
    with pytest.raises(ValueError):
        make_monitor("jacoco", str(tmp_path), tag="T", total_methods=1)


def test_total_methods_requires_positive(tmp_path):
    with pytest.raises(ValueError):
        AndroLogCVMonitor(save_dir=str(tmp_path), tag="T", total_methods=0)


def test_counts_distinct_methods_only(tmp_path):
    mon = _monitor(tmp_path, total=200)
    line = "D TEST_LOG: METHOD=<com.x.A: void a()>"
    for _ in range(5):
        mon._consume(line)
    mon._consume("D TEST_LOG: METHOD=<com.x.A: void b()>")
    # Five hits on one method still count once.
    assert mon.sample() == pytest.approx(2 / 200.0 * 100)


def test_classes_tracked_separately(tmp_path):
    mon = _monitor(tmp_path)
    mon._consume("D TEST_LOG: CLASS=com.x.A")
    mon._consume("D TEST_LOG: CLASS=com.x.A")
    mon._consume("D TEST_LOG: CLASS=com.x.B")
    mon._consume("D TEST_LOG: METHOD=<com.x.A: void a()>")
    summary = mon.summary()
    assert summary["classes_hit"] == 2
    assert summary["methods_hit"] == 1


def test_sample_never_raises(tmp_path):
    """A broken monitor must not be able to abort a test run."""
    mon = _monitor(tmp_path)

    def boom():
        raise RuntimeError("device gone")

    mon._get_code_coverage = boom
    assert mon.sample() == 0.0  # falls back to last known value


def test_file_format_matches_llmdroid(tmp_path):
    mon = _monitor(tmp_path, total=50)
    mon._consume("D TEST_LOG: METHOD=<com.x.A: void a()>")
    mon.sample(action_count=10)
    text = open(os.path.join(str(tmp_path), "codecoverage.txt")).read()
    lines = text.strip().splitlines()
    assert lines[0] == "code coverage"
    assert lines[1].startswith("start time: ")
    assert "tag: TEST_LOG" in text
    assert "total methods: 50" in text
    # Sample line carries tag, percentage and the hit/total pair.
    assert "[TEST_LOG]" in lines[-1]
    assert "(1/50)" in lines[-1]


def test_samples_recorded_with_action_count(tmp_path):
    mon = _monitor(tmp_path)
    mon._consume("D TEST_LOG: METHOD=<com.x.A: void a()>")
    mon.sample(action_count=42)
    assert mon.samples[-1]["action_count"] == 42
    assert mon.samples[-1]["methods_hit"] == 1
    assert "elapsed" in mon.samples[-1]


def test_total_methods_from_apk_counts_probes(tmp_path):
    """The denominator comes from the probes the APK actually carries."""
    apk = str(tmp_path / "fake.apk")
    dex1 = b"junk METHOD=<com.a.A: void x()> junk METHOD=<com.a.A: void y()>"
    # Duplicate across dex files must not be double counted.
    dex2 = b"METHOD=<com.a.A: void y()> METHOD=<com.b.B: int z()>"
    with zipfile.ZipFile(apk, "w") as archive:
        archive.writestr("classes.dex", dex1)
        archive.writestr("classes2.dex", dex2)
        archive.writestr("resources.arsc", b"not a dex METHOD=<ignored: void q()>")
    assert total_methods_from_apk(apk) == 3


def test_coverage_percentage_progression(tmp_path):
    mon = _monitor(tmp_path, total=10)
    assert mon.sample() == 0.0
    for i in range(5):
        mon._consume("D TEST_LOG: METHOD=<com.x.A: void m%d()>" % i)
    assert mon.sample() == pytest.approx(50.0)
    assert mon.current == pytest.approx(50.0)


# --- activity coverage -------------------------------------------------

DECLARED = ["com.app.MainActivity", "com.app.SettingsActivity", "com.app.DetailActivity"]


def _act_monitor(tmp_path, activities=DECLARED):
    return AndroLogCVMonitor(
        save_dir=str(tmp_path), tag="TEST_LOG", total_methods=100, activities=activities
    )


def test_activity_coverage_counts_declared_only(tmp_path):
    """Abstract base activities are probed but are not launchable screens."""
    mon = _act_monitor(tmp_path)
    mon._consume("D TEST_LOG: ACTIVITY=com.app.MainActivity")
    # Bases AndroLog also probes — must not inflate the numerator.
    mon._consume("D TEST_LOG: ACTIVITY=androidx.appcompat.app.AppCompatActivity")
    mon._consume("D TEST_LOG: ACTIVITY=com.app.base.AbsBaseActivity")
    assert mon.activity_coverage() == pytest.approx(1 / 3.0 * 100)
    summary = mon.summary()
    assert summary["activities_hit"] == 1
    assert summary["total_activities"] == 3


def test_activity_coverage_cannot_exceed_100(tmp_path):
    mon = _act_monitor(tmp_path)
    for name in DECLARED:
        mon._consume("D TEST_LOG: ACTIVITY=%s" % name)
    for extra in ("androidx.activity.ComponentActivity", "com.other.Thing"):
        mon._consume("D TEST_LOG: ACTIVITY=%s" % extra)
    assert mon.activity_coverage() == pytest.approx(100.0)


def test_activity_coverage_absent_without_manifest_list(tmp_path):
    mon = AndroLogCVMonitor(
        save_dir=str(tmp_path), tag="TEST_LOG", total_methods=100, activities=None
    )
    mon._consume("D TEST_LOG: ACTIVITY=com.app.MainActivity")
    assert mon.activity_coverage() is None
    assert "activity_coverage" not in mon.summary()


def test_activity_line_does_not_count_as_class(tmp_path):
    """ACTIVITY= must be consumed before the CLASS= branch."""
    mon = _act_monitor(tmp_path)
    mon._consume("D TEST_LOG: ACTIVITY=com.app.MainActivity")
    assert mon.summary()["classes_hit"] == 0
    assert mon.summary()["activities_hit"] == 1


def test_activity_coverage_in_sample_and_file(tmp_path):
    mon = _act_monitor(tmp_path)
    mon._consume("D TEST_LOG: ACTIVITY=com.app.MainActivity")
    mon.sample(action_count=1)
    assert mon.samples[-1]["activity_coverage"] == pytest.approx(33.33333, abs=1e-4)
    text = open(os.path.join(str(tmp_path), "codecoverage.txt")).read()
    assert "total activities: 3" in text
    assert "activities" in text.strip().splitlines()[-1]


# --- reader liveness ---------------------------------------------------
# AndroLog emits a line per executed method and overruns the default 2 MiB
# logcat ring buffer within seconds. When that happened the counter froze
# while the app kept exercising new code, and the frozen number looked like
# genuine saturation. These pin the detection of that state.


def test_stall_detected_when_no_new_lines(tmp_path, caplog):
    mon = _monitor(tmp_path, total=100)
    mon._consume("D TEST_LOG: METHOD=<com.x.A: void a()>")
    mon.sample()
    for _ in range(3):
        mon.sample()  # no new lines arriving
    assert mon._stalled_samples >= 3
    assert mon.summary()["stalled_samples"] >= 3


def test_stall_counter_resets_when_lines_resume(tmp_path):
    mon = _monitor(tmp_path, total=100)
    mon.sample()
    mon.sample()
    assert mon._stalled_samples == 2
    mon._consume("D TEST_LOG: METHOD=<com.x.B: void b()>")
    mon.sample()
    assert mon._stalled_samples == 0


def test_lines_seen_counts_every_line(tmp_path):
    mon = _monitor(tmp_path, total=100)
    mon._consume("D TEST_LOG: METHOD=<com.x.A: void a()>")
    mon._consume("D TEST_LOG: CLASS=com.x.A")
    mon._consume("D TEST_LOG: irrelevant noise")
    assert mon.summary()["lines_seen"] == 3


def test_buffer_size_is_configurable(tmp_path):
    mon = AndroLogCVMonitor(
        save_dir=str(tmp_path), tag="T", total_methods=1, buffer_size="32M"
    )
    assert mon.buffer_size == "32M"


# --- minSdk patching for instrumentation -------------------------------
# Soot cannot split dex for minSdk < 21, so scripts/instrument_apk.py raises
# the floor first. The <uses-sdk> record is found by matching the ADJACENT
# minSdk/targetSdk pair — an earlier "lowest integer value" heuristic silently
# patched an unrelated attribute instead.

import struct
import sys as _sys

_sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))
from instrument_apk import _find_uses_sdk, bump_min_sdk  # noqa: E402

INT_DEC = 0x10000008
ANDROID_NS = 130


def _attr(ns, name, raw_value, typ, data):
    return struct.pack("<IIIII", ns, name, raw_value, typ, data)


def _manifest(min_sdk, target_sdk, decoys=()):
    """Synthesise the attribute region of a binary manifest."""
    blob = b"\x00" * 64
    for ns, name, typ, value in decoys:
        blob += _attr(ns, name, 0xFFFFFFFF, typ, value)
    blob += _attr(ANDROID_NS, 15, 0xFFFFFFFF, INT_DEC, min_sdk)
    blob += _attr(ANDROID_NS, 19, 0xFFFFFFFF, INT_DEC, target_sdk)
    return bytearray(blob + b"\x00" * 64)


def test_find_uses_sdk_locates_the_pair():
    raw = _manifest(19, 33)
    found = _find_uses_sdk(raw)
    assert found is not None
    _off, current, target = found
    assert (current, target) == (19, 33)


def test_find_uses_sdk_ignores_unrelated_int_attribute():
    """A lone android:INT_DEC attribute is not <uses-sdk>."""
    raw = _manifest(19, 33, decoys=[(ANDROID_NS, 10, INT_DEC, 3)])
    _off, current, target = _find_uses_sdk(raw)
    assert (current, target) == (19, 33)


def test_bump_min_sdk_rewrites_only_min(tmp_path):
    src = str(tmp_path / "in.apk")
    dst = str(tmp_path / "out.apk")
    with zipfile.ZipFile(src, "w") as archive:
        archive.writestr("AndroidManifest.xml", bytes(_manifest(19, 33)))
        archive.writestr("classes.dex", b"METHOD=<a.B: void c()>")
    assert bump_min_sdk(src, dst, 21) is True
    with zipfile.ZipFile(dst) as archive:
        raw = bytearray(archive.read("AndroidManifest.xml"))
        assert archive.read("classes.dex") == b"METHOD=<a.B: void c()>"
    _off, current, target = _find_uses_sdk(raw)
    assert current == 21
    assert target == 33  # untouched


def test_bump_min_sdk_noop_when_already_high(tmp_path):
    src = str(tmp_path / "in.apk")
    dst = str(tmp_path / "out.apk")
    with zipfile.ZipFile(src, "w") as archive:
        archive.writestr("AndroidManifest.xml", bytes(_manifest(29, 36)))
    assert bump_min_sdk(src, dst, 21) is False
    assert not os.path.exists(dst)


def test_bump_min_sdk_noop_when_no_uses_sdk(tmp_path):
    """Manifests we cannot parse are left alone rather than corrupted."""
    src = str(tmp_path / "in.apk")
    dst = str(tmp_path / "out.apk")
    with zipfile.ZipFile(src, "w") as archive:
        archive.writestr("AndroidManifest.xml", b"\x00" * 128)
    assert bump_min_sdk(src, dst, 21) is False
    assert not os.path.exists(dst)


# --- cross-tool comparison parsing -------------------------------------
# LLMDroid writes a different sample line ("--> growth rate" instead of
# "@ elapsed") and its AndroLog monitor tracks methods only, so activity
# coverage and wall time have to be recovered from utg.js.

from compare_coverage import read_coverage_file, read_utg, load_run  # noqa: E402


def _write(path, text):
    with open(path, "w") as handle:
        handle.write(text)


def test_reads_llmdroid_sample_format(tmp_path):
    _write(str(tmp_path / "codecoverage.txt"), "\n".join([
        "code coverage",
        "start time: 2026-08-27 00:30:32",
        "[MONEY_SUPER_LOG]  2.77192% (4085/147371) --> 4084.00000",
        "[MONEY_SUPER_LOG]  3.96143% (5838/147371) -->  0.00000",
    ]) + "\n")
    parsed = read_coverage_file(str(tmp_path / "codecoverage.txt"))
    assert parsed["tag"] == "MONEY_SUPER_LOG"
    assert parsed["total"] == 147371
    assert len(parsed["samples"]) == 2
    assert parsed["samples"][-1]["methods_hit"] == 5838
    assert parsed["samples"][-1]["coverage"] == pytest.approx(3.96143)


def test_reads_testcube_sample_format(tmp_path):
    _write(str(tmp_path / "codecoverage.txt"), "\n".join([
        "code coverage",
        "tag: MONEY_SUPER_LOG",
        "total methods: 147371",
        "total activities: 51",
        "[MONEY_SUPER_LOG]  6.69060% (9860/147371) @ 3114.23s | activities  21.57% (11/51)",
    ]) + "\n")
    parsed = read_coverage_file(str(tmp_path / "codecoverage.txt"))
    last = parsed["samples"][-1]
    assert last["elapsed"] == pytest.approx(3114.23)
    assert last["activity_coverage"] == pytest.approx(21.57)
    assert parsed["total_activities"] == 51


def _utg(path, reached, total, spent):
    _write(path, "var utg = \n" + json.dumps({
        "num_reached_activities": reached,
        "app_num_total_activities": total,
        "time_spent": spent,
    }))


def test_read_utg_computes_activity_coverage(tmp_path):
    _utg(str(tmp_path / "utg.js"), 4, 51, 1299.9)
    info = read_utg(str(tmp_path))
    assert info["activity_coverage"] == pytest.approx(4 / 51.0 * 100)
    assert info["activity_source"] == "utg"
    assert info["duration"] == pytest.approx(1299.9)


def test_read_utg_finds_hidden_droidbot_copy(tmp_path):
    """TestCube writes utg.js under .droidbot/, LLMDroid at the top level."""
    hidden = tmp_path / ".droidbot"
    hidden.mkdir()
    _utg(str(hidden / "utg.js"), 10, 51, 2835.9)
    assert read_utg(str(tmp_path))["activities_hit"] == 10


def test_utg_fills_llmdroid_gaps(tmp_path):
    """A run with no activity data picks it up from utg.js."""
    _write(str(tmp_path / "codecoverage.txt"), "\n".join([
        "code coverage",
        "[MONEY_SUPER_LOG]  3.96143% (5838/147371) -->  0.00000",
    ]) + "\n")
    _utg(str(tmp_path / "utg.js"), 4, 51, 1299.9)
    run = load_run(str(tmp_path))
    assert run["activity_coverage"] == pytest.approx(7.84313, abs=1e-4)
    assert run["activity_source"] == "utg"
    # LLMDroid's parsed duration is 0.0 (no elapsed field) — utg.js must win.
    assert run["duration"] == pytest.approx(1299.9)


def test_androlog_activity_data_beats_utg(tmp_path):
    """A tool's own instrumented numbers are never overwritten by utg.js."""
    _write(str(tmp_path / "codecoverage.txt"), "\n".join([
        "code coverage",
        "total activities: 51",
        "[T]  6.69060% (9860/147371) @ 3114.23s | activities  21.57% (11/51)",
    ]) + "\n")
    _utg(str(tmp_path / "utg.js"), 10, 51, 2835.9)
    run = load_run(str(tmp_path))
    assert run["activity_coverage"] == pytest.approx(21.57)
    assert run["activities_hit"] == 11
    assert run["activity_source"] == "androlog"
    assert run["duration"] == pytest.approx(3114.23)


# --- run effort reporting ----------------------------------------------


def test_summary_reports_total_actions(tmp_path):
    """Coverage is only interpretable next to the effort that produced it."""
    mon = _monitor(tmp_path, total=100)
    mon._consume("D TEST_LOG: METHOD=<com.x.A: void a()>")
    mon.sample(action_count=57)
    assert mon.summary()["total_actions"] == 57


def test_summary_total_actions_zero_without_samples(tmp_path):
    assert _monitor(tmp_path).summary()["total_actions"] == 0


def test_compare_counts_actions_from_events_dir(tmp_path):
    """LLMDroid records no action_count, so events/ is the fallback."""
    _write(str(tmp_path / "codecoverage.txt"), "\n".join([
        "code coverage",
        "[T]  3.96143% (5838/147371) -->  0.00000",
    ]) + "\n")
    events = tmp_path / "events"
    events.mkdir()
    for i in range(7):
        _write(str(events / ("event_%d.json" % i)), "{}")
    _write(str(events / "notes.txt"), "ignored")
    assert load_run(str(tmp_path))["total_actions"] == 7


# --- restart-between-features toggle -----------------------------------
# Each feature switch costs a stop+start pair that re-runs already covered
# startup code; on a 28-feature app that was 21% of every action issued.


def test_restart_between_features_defaults_on():
    from droidbot.feature_tester.config import FeatureTesterConfig
    assert FeatureTesterConfig().restart_between_features is True


def test_no_restart_flag_disables_it():
    from droidbot.feature_tester.config import FeatureTesterConfig

    class Opts(object):
        no_restart_between_features = True

    assert FeatureTesterConfig.from_options(Opts()).restart_between_features is False
