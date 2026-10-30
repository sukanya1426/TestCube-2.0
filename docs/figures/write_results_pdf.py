"""One-off: write the TestCube vs LLMDroid results explanation as a PDF."""
from pathlib import Path

from fpdf import FPDF

HERE = Path(__file__).resolve().parent
OUT = HERE / "testcube_vs_llmdroid_results.pdf"
FIG = HERE / "coverage_per_app.png"

NAVY = (22, 24, 29)
SLATE = (85, 89, 106)
RULE = (220, 222, 230)
TC = (42, 120, 214)
LD = (235, 104, 52)


class Pdf(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*SLATE)
        self.cell(0, 8, "TestCube vs LLMDroid  |  how to read and report the comparison", align="L")
        self.ln(10)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*SLATE)
        self.cell(0, 8, str(self.page_no()), align="C")

    def h1(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(*NAVY)
        self.multi_cell(0, 8, ascii(text))
        self.ln(2)

    def h2(self, text):
        self.ln(3)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*NAVY)
        self.multi_cell(0, 7, ascii(text))
        self.ln(1)

    def body(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 10.5)
        self.set_text_color(*NAVY)
        self.multi_cell(0, 5.6, ascii(text))
        self.ln(1.5)

    def italic(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "I", 10.5)
        self.set_text_color(*SLATE)
        self.multi_cell(0, 5.6, ascii(text))
        self.ln(1.5)

    def bullet(self, title, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(*NAVY)
        self.multi_cell(0, 5.6, ascii(title))
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 10.5)
        self.multi_cell(0, 5.6, ascii(text))
        self.ln(1)


def ascii(text):
    return (
        text.replace("\u2014", "-")
        .replace("\u2013", "-")
        .replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u00d7", "x")
        .replace("\u2248", "~")
    )


def table(pdf, headers, rows, col_w):
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_fill_color(245, 246, 248)
    pdf.set_text_color(*SLATE)
    for h, w in zip(headers, col_w):
        pdf.cell(w, 7, ascii(h), border=0, fill=True)
    pdf.ln()
    pdf.set_draw_color(*RULE)
    pdf.set_line_width(0.2)
    y = pdf.get_y()
    pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*NAVY)
    for i, row in enumerate(rows):
        if i % 2:
            pdf.set_fill_color(250, 250, 251)
            fill = True
        else:
            fill = False
        h = 7
        x0 = pdf.l_margin
        y0 = pdf.get_y()
        # wrap last column
        pdf.set_xy(x0, y0)
        max_h = h
        cells = []
        for val, w in zip(row, col_w):
            lines = pdf.multi_cell(w, 5, ascii(str(val)), dry_run=True, output="LINES")
            max_h = max(max_h, 5 * len(lines) + 2)
            cells.append((val, w, lines))
        if y0 + max_h > pdf.h - 20:
            pdf.add_page()
            y0 = pdf.get_y()
        if fill:
            pdf.set_fill_color(250, 250, 251)
            pdf.rect(x0, y0, sum(col_w), max_h, style="F")
        x = x0
        for val, w, lines in cells:
            pdf.set_xy(x, y0 + 1)
            pdf.multi_cell(w, 5, ascii(str(val)))
            x += w
            pdf.set_y(y0 + max_h)
    pdf.set_x(pdf.l_margin)


def main():
    pdf = Pdf(format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(18, 16, 18)
    pdf.add_page()

    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*SLATE)
    pdf.cell(0, 5, "Results note  |  13 paired apps  |  1-hour budget  |  same instrumented APKs")
    pdf.ln(8)

    pdf.h1("TestCube vs LLMDroid: how to read the result")

    pdf.body(
        "The short version: on the same 13 apps, the two tools are roughly even. "
        "TestCube's averages look a bit higher, but that gap is not statistically solid. "
        "What is clear is when each tool wins, and that TestCube gets similar coverage with fewer taps."
    )
    pdf.body(
        "Feature coverage in this comparison is weighted coverage: the mean share of "
        "gold steps that actually happened (mean of each feature's completion ratio). "
        "It is not 'fully covered features / total', which is near zero for both tools."
    )

    pdf.h2("Final means (n = 13)")
    table(
        pdf,
        ["Metric", "TestCube", "LLMDroid", "Difference", "95% CI", "Per-app wins"],
        [
            ["Code coverage", "19.43%", "18.09%", "+1.33 pp", "-0.98 to +3.65", "8-5"],
            ["Feature coverage (weighted)", "15.58%", "12.04%", "+3.54 pp", "-0.32 to +7.40", "7-6"],
            ["Actions per run", "352", "594", "-41%", "-", "-"],
            ["Code coverage per 100 actions", "5.52", "3.05", "+81%", "-", "-"],
        ],
        [48, 24, 24, 28, 32, 28],
    )
    pdf.set_x(pdf.l_margin)
    pdf.ln(3)
    pdf.italic(
        "Both confidence intervals cross zero. Do not report these means as a demonstrated win. "
        "The efficiency ratio (fewer actions for similar coverage) is the number that holds up."
    )

    if FIG.is_file():
        pdf.h2("Per-app figure")
        # Keep aspect; page inner width ~174 mm
        pdf.image(str(FIG), w=174)
        pdf.ln(2)
        pdf.italic(
            "Figure: (a) code coverage from AndroLog probes; (b) weighted feature coverage. "
            "Blue = TestCube, hatched orange = LLMDroid. Mean row at the bottom."
        )

    pdf.h2("When TestCube is better")
    pdf.body(
        "TestCube wins when LLMDroid's exploration falls apart — not when the app is simply "
        "'harder'. Typical pattern: a first-run wall, permissions, login, or a fragile LLM loop. "
        "LLMDroid never really gets into the app, or it issues only a handful of actions and stops. "
        "TestCube still has a feature list, so it keeps trying those steps."
    )
    table(
        pdf,
        ["App", "Feature % (TC / LD)", "Why TestCube leads"],
        [
            ["markor", "13.51 / 1.63", "LLMDroid ran many actions but never left the permission screen."],
            ["money", "14.09 / 2.08", "LLMDroid issued very few actions (~138). TestCube kept the feature list."],
            ["newpipe", "17.16 / 6.37", "LLMDroid issued ~130 actions. Guided search still progressed."],
            ["radiodroid", "18.70 / 7.24", "LLMDroid stalled at ~90 actions after the LLM stopped."],
            ["nononsensenotes", "17.25 / 5.15", "LLMDroid explored a lot but did not complete gold steps."],
            ["omninotes", "11.50 / 8.79", "Smaller edge: guidance beat unfocused wandering."],
            ["materialfiles", "11.19 / 9.17", "Smaller edge; same pattern."],
        ],
        [38, 42, 94],
    )
    pdf.ln(2)
    pdf.italic(
        "Paper sentence: TestCube is stronger when the tester must stay on a specified capability "
        "after setup, dialogs, or a stalled LLM — not because it always covers more code."
    )

    pdf.h2("When LLMDroid won")
    pdf.body(
        "LLMDroid wins on small, shallow apps where coverage-guided wandering just works, and "
        "it is allowed to tap much more often. Typical pattern: few screens, easy navigation, "
        "no hard login wall. LLMDroid issued about 700+ actions; TestCube issued about 300. "
        "More wandering covers more of a small app. Margins are small (-0.04 to -6.7 pp on features), "
        "except Fossify Clock."
    )
    table(
        pdf,
        ["App", "Feature % (TC / LD)", "Why LLMDroid leads"],
        [
            ["fossifyclock", "9.94 / 16.60", "Small app; LLMDroid issued 729 actions vs TestCube 216."],
            ["fossifycontacts", "19.87 / 19.91", "Essentially a tie; LLMDroid slightly more exploration."],
            ["fossifyvoicerecorder", "15.72 / 18.99", "High-volume wandering on a shallow app."],
            ["loophabits", "19.44 / 23.12", "Easy navigation; ~747 vs 309 actions."],
            ["opentasks", "15.70 / 18.49", "Same: throughput, not a setup trap."],
            ["odyssey", "18.48 / 19.04", "Near tie; LLMDroid's extra actions barely move the needle."],
        ],
        [42, 42, 90],
    )
    pdf.ln(2)
    pdf.italic(
        "Paper sentence: LLMDroid is stronger when cheap, high-volume exploration is enough — "
        "small apps, no setup trap, coverage-driven wandering."
    )

    pdf.add_page()
    pdf.h2("How to portray this in the paper")
    pdf.body(
        "Do not write 'TestCube beats LLMDroid'. Reviewers will look at the confidence intervals "
        "(both cross zero) and the degraded LLMDroid runs (markor, radiodroid)."
    )
    pdf.bullet(
        "1. Headline: comparable means, mixed per-app outcomes.",
        "On paired 1-hour runs, mean code and weighted feature coverage are comparable. "
        "Per-app wins are mixed (code 8-5, feature 7-6).",
    )
    pdf.bullet(
        "2. Let the figure show heterogeneity.",
        "LLMDroid on Fossify; TestCube on markor / money / newpipe. That split is why the "
        "mean interval is wide. Put it in the caption.",
    )
    pdf.bullet(
        "3. The claim that survives is efficiency.",
        "TestCube reaches that coverage with 352 actions vs 594 (~41% fewer). Frame as "
        "efficiency and attribution, not as higher coverage.",
    )
    pdf.bullet(
        "4. Interpret, do not hide.",
        "TestCube wins on robustness to stalled exploration; LLMDroid wins on throughput "
        "on simple apps. That matches the method: TestCube pays for one-feature-at-a-time "
        "plus model calls; LLMDroid pays for more cheap DFS until coverage plateaus.",
    )
    pdf.bullet(
        "5. Name the degraded baseline runs.",
        "Markor and RadioDroid LLMDroid runs were degraded (never entered the app / LLM "
        "stalled at 90 actions). Either exclude them in a sensitivity row or say so in the "
        "caption. Keeping them is a real robustness result, but not a fair 'same healthy run' comparison.",
    )
    pdf.bullet(
        "6. Name the feature metric correctly.",
        "Call it weighted feature coverage (step completion ratio). Do not imply strict "
        "covered/total.",
    )

    pdf.h2("Paragraph you can paste")
    pdf.set_fill_color(245, 246, 248)
    pdf.set_draw_color(*RULE)
    text = (
        "Under a one-hour budget on 13 shared apps, TestCube and LLMDroid achieve similar mean "
        "code coverage (19.4% vs 18.1%) and weighted feature coverage (15.6% vs 12.0%); neither "
        "paired difference is statistically significant. Outcomes split by application: LLMDroid "
        "leads on small, easily explored apps (Fossify suite, Loop Habit Tracker, OpenTasks), "
        "where it issues roughly twice as many actions. TestCube leads when LLMDroid's exploration "
        "stalls in setup or issues few actions (Markor, Money Manager, NewPipe, RadioDroid, "
        "NoNonsense Notes). TestCube attains comparable coverage with 41% fewer actions (352 vs 594), "
        "consistent with feature-guided search rather than coverage-maximizing wandering."
    )
    pdf.set_font("Helvetica", "", 10.5)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(0, 5.8, ascii(text), fill=True)
    pdf.ln(4)

    pdf.h2("Suggested figure caption")
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(
        0,
        5.6,
        ascii(
            "Per-app coverage for TestCube and LLMDroid over a one-hour budget on identical "
            "instrumented APKs. (a) Code coverage from AndroLog bytecode probes; (b) weighted "
            "feature coverage (mean completion ratio of ground-truth steps). TestCube means: "
            "19.4% vs 18.1% code; 15.6% vs 12.0% feature. Neither paired difference is significant "
            "(code +1.33 pp, 95% CI [-0.98, +3.65]; feature +3.54 pp, 95% CI [-0.32, +7.40]). "
            "TestCube used 352 actions per run against LLMDroid's 594."
        ),
    )
    pdf.ln(4)
    pdf.body(
        "One-line takeaway: not a knockout — a split by app type, plus efficiency."
    )

    pdf.output(str(OUT))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
