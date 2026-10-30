"""Publication figure: per-app code and feature coverage, TestCube vs LLMDroid.

Two panels share one app axis so a reader can read across. Bars are grouped
rather than stacked (the two tools are alternatives, not parts of a whole), one
linear scale per panel, and LLMDroid is hatched as well as coloured so the
figure survives greyscale printing.
"""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

SP = "/private/tmp/claude-502/-Users-mahdiya-TestCube-2-0/164e572b-9c9b-4f35-a904-3b03b7958205/scratchpad"
D = json.load(open(SP + "/chart_data.json"))
apps = sorted(D["apps"], key=lambda d: d["app"])

TC, LD = "#2a78d6", "#eb6834"        # validated pair: CVD dE 24.7, normal dE 33.6
INK, INK2, GRID = "#16181d", "#55596a", "#dcdee6"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "font.size": 7.5,
    "axes.labelsize": 8,
    "axes.titlesize": 8.5,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7.5,
    "legend.fontsize": 7.5,
    "axes.edgecolor": INK2,
    "axes.linewidth": 0.6,
    "pdf.fonttype": 42,              # embed TrueType, not Type 3 (ACM/IEEE require it)
    "ps.fonttype": 42,
    "svg.fonttype": "none",
})

labels = [d["app"] for d in apps]
n = len(apps)
# a gap row, then the mean row, below the per-app rows
GAP = 1.0
y_apps = list(range(n))
y_mean = n + GAP
H = 0.38

fig, axes = plt.subplots(1, 2, figsize=(7.16, 4.35), sharey=True,
                         gridspec_kw={"wspace": 0.06})

panels = [
    (axes[0], "tc_code", "ld_code", "(a) Code coverage",
     "methods reached / methods in APK (%)", D["code"]),
    (axes[1], "tc_feat", "ld_feat", "(b) Feature coverage",
     "ground-truth steps executed (%)", D["feat"]),
]

for ax, k_tc, k_ld, title, xlabel, agg in panels:
    tc = [d[k_tc] for d in apps]
    ld = [d[k_ld] for d in apps]

    ax.barh([y - H / 2 for y in y_apps], tc, height=H, color=TC,
            edgecolor="white", linewidth=0.5, zorder=3)
    ax.barh([y + H / 2 for y in y_apps], ld, height=H, color=LD,
            edgecolor="white", linewidth=0.5, hatch="////", zorder=3)
    # aggregate
    ax.barh(y_mean - H / 2, agg["tc_mean"], height=H, color=TC,
            edgecolor=INK, linewidth=0.7, zorder=3)
    ax.barh(y_mean + H / 2, agg["ld_mean"], height=H, color=LD,
            edgecolor=INK, linewidth=0.7, hatch="////", zorder=3)

    top = max(max(tc), max(ld)) * 1.17
    for y, v in zip([y - H / 2 for y in y_apps] + [y_mean - H / 2], tc + [agg["tc_mean"]]):
        ax.text(v + top * 0.012, y, f"{v:.1f}", va="center", ha="left",
                fontsize=6.4, color=INK2)
    for y, v in zip([y + H / 2 for y in y_apps] + [y_mean + H / 2], ld + [agg["ld_mean"]]):
        ax.text(v + top * 0.012, y, f"{v:.1f}", va="center", ha="left",
                fontsize=6.4, color=INK2)

    ax.set_xlim(0, top)
    ax.set_xlabel(xlabel, color=INK2)
    ax.set_title(title, loc="left", color=INK, pad=6, fontweight="semibold")
    ax.xaxis.grid(True, color=GRID, linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", colors=INK2, length=2.5, width=0.6)
    # rule separating the aggregate row from the per-app rows
    ax.axhline(n + GAP / 2 - 0.1, color=INK2, linewidth=0.6, zorder=4)

axes[0].set_yticks(y_apps + [y_mean])
axes[0].set_yticklabels(labels + [f"mean (n={D['n']})"], color=INK)
for tick, lab in zip(axes[0].get_yticklabels(), labels + ["mean"]):
    if lab == "mean":
        tick.set_fontweight("semibold")
axes[0].set_ylim(-0.8, y_mean + 0.8)
axes[0].invert_yaxis()

fig.legend(handles=[Patch(facecolor=TC, edgecolor="white", label="TestCube"),
                    Patch(facecolor=LD, edgecolor="white", hatch="////", label="LLMDroid")],
           loc="upper left", bbox_to_anchor=(0.005, 1.0), ncol=2,
           frameon=False, handlelength=1.5, handleheight=0.9, columnspacing=1.4)

fig.subplots_adjust(left=0.165, right=0.995, top=0.895, bottom=0.085)
for ext in ("pdf", "png"):
    fig.savefig(f"{SP}/coverage_per_app.{ext}", dpi=300,
                facecolor="white", bbox_inches=None)
print("wrote coverage_per_app.pdf and .png")
print(f"  {n} apps + mean row; code xlim 0-{max(max(d['tc_code'] for d in apps), max(d['ld_code'] for d in apps))*1.30:.1f}")
