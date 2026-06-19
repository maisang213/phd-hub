#!/usr/bin/env python3
"""Render Quy-Sang Mai's one-page ACADEMIC CV to PDF.

Single-column, academic conventions: Education & Research lead, a standalone
Publications section, Referees line, credentials below. Same facts as the source.
Standalone: depends only on fpdf2 (core Helvetica, no external fonts).

Run:  python3 docs/cv/build_cv_pdf.py
Out:  docs/cv/quy-sang-mai-cv.pdf
"""
from pathlib import Path
from fpdf import FPDF

ACCENT = (43, 108, 176)   # section headers / accents (navy-blue)
DARK = (38, 38, 38)
GREY = (105, 105, 105)
LINK = (43, 108, 176)

OUT = Path(__file__).resolve().parent / "quy-sang-mai-cv.pdf"


def clean(s: str) -> str:
    return (s.replace("–", "-").replace("—", "-")
             .replace("’", "'").replace("‘", "'")
             .replace("“", '"').replace("”", '"')
             .replace("·", "-"))


class CV(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


def flow(pdf, x, width, segments, size=9, lh=4.3, gap_after=1.6, indent=0):
    """Word-wrapped rich text. segments: (text, bold, link)."""
    x = x + indent
    width = width - indent
    pdf.set_x(x)
    cur_w = 0.0
    line_started = False

    def newline():
        nonlocal cur_w, line_started
        pdf.ln(lh)
        pdf.set_x(x)
        cur_w = 0.0
        line_started = False

    for text, bold, link in segments:
        style = "B" if bold else ""
        for raw_word in text.split(" "):
            if raw_word == "":
                continue
            word = clean(raw_word)
            pdf.set_font("Helvetica", style, size)
            sw = pdf.get_string_width(" ")
            ww = pdf.get_string_width(word)
            need = (sw if line_started else 0) + ww
            if cur_w + need > width and line_started:
                newline()
            if line_started:
                pdf.cell(sw, lh, " ")
                cur_w += sw
            if link:
                pdf.set_text_color(*LINK)
                pdf.set_font("Helvetica", style + "U", size)
                pdf.cell(ww, lh, word, link=link)
                pdf.set_text_color(*DARK)
                pdf.set_font("Helvetica", style, size)
            else:
                pdf.set_text_color(*DARK)
                pdf.cell(ww, lh, word)
            cur_w += ww
            line_started = True
    pdf.ln(lh + gap_after)
    pdf.set_x(x)


def section(pdf, x, width, title, size=10.5):
    pdf.ln(0.8)
    pdf.set_x(x)
    pdf.set_font("Helvetica", "B", size)
    pdf.set_text_color(*ACCENT)
    pdf.cell(width, 5.2, clean(title.upper()))
    pdf.ln(5.3)
    y = pdf.get_y()
    pdf.set_draw_color(*ACCENT)
    pdf.set_line_width(0.3)
    pdf.line(x, y, x + width, y)
    pdf.ln(1.6)
    pdf.set_x(x)


def entry_head(pdf, x, width, left, right):
    """Bold left-aligned title with grey right-aligned date on the same row."""
    pdf.set_x(x)
    pdf.set_font("Helvetica", "B", 9.3)
    pdf.set_text_color(*DARK)
    pdf.cell(width * 0.7, 4.6, clean(left))
    pdf.set_font("Helvetica", "I", 8.3)
    pdf.set_text_color(*GREY)
    pdf.cell(width * 0.3, 4.6, clean(right), align="R")
    pdf.ln(4.6)
    pdf.set_x(x)


def subline(pdf, x, width, text, size=8.4):
    pdf.set_x(x)
    pdf.set_font("Helvetica", "I", size)
    pdf.set_text_color(*GREY)
    pdf.multi_cell(width, 3.9, clean(text))
    pdf.set_x(x)


pdf = CV(format="A4")
pdf.set_auto_page_break(False)
pdf.set_margins(12, 11, 12)
pdf.add_page()

X = 12
W = 210 - 24

# ---------- Header ----------
pdf.set_xy(X, 11)
pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(*DARK)
pdf.cell(W * 0.72, 10, "Quy-Sang Mai, CFA")
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(*GREY)
pdf.cell(W * 0.28, 10, clean("quysang.mai@gmail.com"), align="R",
         link="mailto:quysang.mai@gmail.com")
pdf.ln(9.5)
pdf.set_x(X)
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(*GREY)
pdf.cell(0, 4.5, clean("(+84) 901.350.009  -  Ho Chi Minh City, Vietnam"))
pdf.ln(5)
pdf.set_x(X)
pdf.set_font("Helvetica", "I", 8.8)
pdf.set_text_color(*ACCENT)
pdf.multi_cell(0, 4, clean("Research interests: ML-driven signal combination for abnormal returns in "
                           "emerging equity markets; investor sentiment and earnings-surprise prediction."))
pdf.ln(1.2)
pdf.set_draw_color(190, 190, 190)
pdf.set_line_width(0.2)
y = pdf.get_y()
pdf.line(X, y, X + W, y)

# ---------- Education ----------
section(pdf, X, W, "Education")
entry_head(pdf, X, W, "MSc, Applied Mathematics (Quantitative & Computational Finance)", "2016 - 2018")
subline(pdf, X, W, "University of Science, Vietnam National University HCMC  -  Distinction")
pdf.ln(1.0)
entry_head(pdf, X, W, "BA, Economics and Finance", "2012 - 2015")
subline(pdf, X, W, "RMIT University  -  Distinction")
pdf.ln(1.0)
entry_head(pdf, X, W, "Mathematics (specialised), High School for the Gifted, VNU-HCMC", "2009 - 2012")

# ---------- Research Experience ----------
section(pdf, X, W, "Research Experience")
entry_head(pdf, X, W, "Capstone Project - HCMC University of Science", "Jan - Mar 2018")
flow(pdf, X, W, [
    ("Applied the three-layered boosting and expert-weighting online-learning framework of ", False, None),
    ("Creamer and Freund (2010)", True, "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=937847"),
    (" to the Vietnamese stock market, using an event-study / abnormal-return methodology to find optimal "
     "combinations of technical indicators and parameters for positive abnormal returns. The same "
     "signal-combination approach is what the proposed PhD would extend from technical indicators to text- "
     "and LLM-derived sentiment signals for earnings-surprise prediction. Supervised by ", False, None),
    ("Dr Minh Dang", True, "https://www.linkedin.com/in/ngocminhdang/"),
    (".", False, None),
], gap_after=1.6)
entry_head(pdf, X, W, "Master's Thesis - HCMC University of Science", "2018")
flow(pdf, X, W, [
    ("Extended the smile-adjusted delta-hedging approach of ", False, None),
    ("Hull and White (2017)", True, "https://www.sciencedirect.com/science/article/pii/S0378426617301085"),
    (" with supervised ML (gradient-boosted trees) to reduce hedging variance for options on the S&P 500 "
     "index and its constituents, 2004-2015. Supervised by ", False, None),
    ("Dr Minh Dang", True, "https://www.linkedin.com/in/ngocminhdang/"),
    (".", False, None),
], gap_after=1.6)
entry_head(pdf, X, W, "Research Assistant - RMIT University Vietnam", "Aug 2016 - Mar 2017")
flow(pdf, X, W, [
    ("Co-authored learning-and-teaching research with ", False, None),
    ("A/Prof. Mathews Nkhoma", True, "https://www.linkedin.com/in/mathews-nkhoma-281a5891/"),
    (": literature review, database searches, and qualitative & quantitative data analysis, resulting in "
     "the peer-reviewed conference paper listed below.", False, None),
], gap_after=1.4)

# ---------- Publications ----------
section(pdf, X, W, "Publications")
flow(pdf, X, W, [
    ("Nkhoma, C. A., Nkhoma, M., Ulhaq, I., & ", False, None),
    ("Mai, S. Q.", True, None),
    (" (2017). ", False, None),
    ("Enhancing students' learning through early class preparation.", False, "https://doi.org/10.28945/3756"),
    (" Proceedings of InSITE 2017, 85-95. ", False, None),
    ("doi:10.28945/3756", False, "https://doi.org/10.28945/3756"),
], gap_after=1.2)

# ---------- Professional Experience ----------
section(pdf, X, W, "Professional Experience")
entry_head(pdf, X, W, "Ho Chi Minh City Securities Corporation (HSC)", "2017 - Present")
subline(pdf, X, W, "One of Vietnam's leading brokerage and investment-banking firms.")
pdf.ln(0.6)
pdf.set_x(X)
pdf.set_font("Helvetica", "B", 8.8); pdf.set_text_color(*DARK)
pdf.cell(W * 0.72, 4.2, clean("Manager / Senior Manager - Quant & Warrant Trading"))
pdf.set_font("Helvetica", "I", 8.2); pdf.set_text_color(*GREY)
pdf.cell(W * 0.28, 4.2, "Jan 2024 - Present", align="R"); pdf.ln(4.4)
for b in [
    "Established the equity quant trading desk from the ground up;",
    "Build models to backtest and construct quantitative portfolios maximising absolute and "
    "risk-adjusted equity returns; supervise the covered-warrant desk.",
]:
    flow(pdf, X, W, [("-  " + b, False, None)], size=8.6, lh=3.9, gap_after=0.3, indent=3)
pdf.ln(0.6)
pdf.set_x(X)
pdf.set_font("Helvetica", "B", 8.8); pdf.set_text_color(*DARK)
pdf.cell(W * 0.72, 4.2, clean("Senior / Covered Warrant Trader; ETF Trader"))
pdf.set_font("Helvetica", "I", 8.2); pdf.set_text_color(*GREY)
pdf.cell(W * 0.28, 4.2, "Sep 2017 - Dec 2023", align="R"); pdf.ln(4.4)
flow(pdf, X, W, [("-  Product development, pricing, market-making and reporting for HSC's covered-warrant and "
                  "ETF portfolios (authorised participant); backup coverage for index arbitrage.", False, None)],
     size=8.6, lh=3.9, gap_after=1.2, indent=3)

entry_head(pdf, X, W, "Investment Analyst - Saigon Asset Management (SAM)", "Aug 2014 - Aug 2015")
flow(pdf, X, W, [("Research and valuation of Vietnamese listed companies (DCF and comparables) for funds "
                  "with once over USD$200m AUM.", False, None)], size=8.6, lh=3.9, gap_after=1.2)

# ---------- Technical Skills ----------
section(pdf, X, W, "Technical Skills")
flow(pdf, X, W, [("Econometrics & event studies  -  Supervised ML (gradient boosting, online learning)  -  "
                  "Python (pandas, scikit-learn)  -  C++  -  LaTeX", False, None)], gap_after=1.2)

# ---------- Credentials ----------
section(pdf, X, W, "Credentials")
flow(pdf, X, W, [("CFA Charterholder (2022)  -  Fund Management Professional License, Vietnam (2023)",
                  False, None)], gap_after=1.2)

# ---------- Referees ----------
section(pdf, X, W, "Referees")
flow(pdf, X, W, [("Available on request.", False, None)], gap_after=0)

pdf.output(str(OUT))
print("wrote", OUT, "| final y = %.1f mm (limit ~286)" % pdf.get_y())
