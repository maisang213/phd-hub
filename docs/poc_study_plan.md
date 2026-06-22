# Proof-of-concept study — LLM sentiment & post-earnings drift on VN equities

> **Why this exists.** Three independent reviewers (a QR hiring manager, the skeptical supervisor, the asset-pricing examiner) converged on the same move: *build the study, don't just prep the meeting.* This artifact is **no-regret** — it pays off whether or not you do the PhD, which project you pick, full- or part-time, this venue or a better one:
> - **QR hireability:** a public, reproducible, after-cost OOS result proves the one thing a CV can't — independent research ability.
> - **The meeting:** walking in with a working demo of the exact thesis dwarfs every diplomatic tactic in the brief.
> - **The NLP gap:** converts "no NLP yet" into "here's a pipeline I built."
> - **De-risks the PhD bet:** if it lands you interviews, you may not need the degree; if you still want it, you choose supervisors (and venue) from strength.

The smallest version (the **weekend demo**) is meeting-ready in days. The full version is a working paper.

---

## 0. The research question (lead with this, not the method)

**Limits-to-arbitrage identification — your most original, most defensible framing.**
Vietnam has **no equity short-selling** and **±7% daily price limits**. Limits-to-arbitrage theory therefore predicts post-earnings underreaction (PEAD) should be **larger and more persistent** than in the US — *but partly uncapturable* on the long-only side. The question:

> *How much of VN's residual post-earnings drift can an LLM sentiment signal capture, out-of-sample and net of realistic cost, for a long-only / VN30-futures investor?*

This turns VN's frictions from caveats into the **identification of the contribution** — and only someone with desk knowledge can pose it.

---

## 1. DO THIS FIRST — the feasibility gate (1 day, before anything else)

The quiet thesis-killer is data sufficiency. Before writing a line of pipeline:

1. **Count the events.** VN30 (≈30 firms) × 4 quarters × usable years of clean PIT data, then subtract: events without clean Vietnamese news coverage, events *before* your LLM's training cutoff, and events censored by ±7% price limits on the announcement window.
2. **Minimum-detectable-effect (MDE) calc.** Given that event count (clustered by announcement date — earnings cluster, so effective N is much smaller than raw N), what drift coefficient could you detect at 80% power? Compare to plausible PEAD magnitudes.
3. **Decision:** if the post-cutoff, clean, capturable event count is too thin for a powered OOS test → either (a) widen to liquid-HOSE beyond VN30 (reintroduces impact/illiquidity), (b) use a panel / Bayesian-shrinkage design *because* data are thin, or (c) accept the study is in-sample/explanatory and frame it honestly. **Know this number before the meeting** — it determines whether the predictive thesis is even feasible.

---

## 2. The weekend demo (meeting-ready; do this regardless)

Minimal artifact to walk in with:
- Pull ~30–50 VN earnings headlines/news snippets (HOSE, recent).
- Classify sentiment two ways: **GPT-4** (zero-shot, a clear bullish/bearish/neutral prompt) vs a **Vietnamese baseline (PhoBERT-class — NOT VADER, which is English-only)**.
- Eyeball where they diverge; note 2–3 concrete observations (e.g., GPT-4 handles Vietnamese financial idiom / negation better/worse; disagreement clusters on X).
- One slide / one paragraph: *"I ran N VN headlines through GPT-4 vs PhoBERT — here's where they diverged and what surprised me."*

That single demo reassures on the NLP gap better than any "I ramp fast."

---

## 3. Full PoC — pre-registered protocol (the rigor that survives an examiner)

**Pre-register before you run** (timestamp it — a public commit/OSF) to defuse data-snooping:
- **Universe:** VN30 (+ liquid-HOSE robustness). Liquidity screen stated upfront.
- **Events:** scheduled earnings announcements; announcement timestamp = the PIT anchor.
- **Sentiment:** Vietnamese-language model (PhoBERT-class) as primary; GPT-4 as the LLM arm; document prompt, model **vintage + training cutoff**, temperature, aggregation (e.g. bullishness index).
- **Label/feature freeze:** no field computed with future info (use as-reported, point-in-time fundamentals/prices).
- **Prediction target:** cumulative abnormal return over the post-announcement drift window (state window + abnormal-return model).
- **Split:** walk-forward, **test window strictly post-LLM-cutoff**; report robustness across ≥2 model vintages.
- **Benchmarks BY ROLE** (not one ladder): a no-predictability null; rival ML predictors (LSTM/GBRT/elastic-net on the *same* features, with vs without LLM sentiment); a VN-appropriate factor model for risk-adjustment (flag ~30-name factor fragility). *No ARIMA* — it's not a null for a cross-sectional drift.
- **Costs:** market-impact model (square-root / ADV-scaled), not a flat bps; include the 0.1% sell tax; report a **$-capacity curve.** Long-only or VN30-futures (no shorting).
- **Multiple-testing correction:** deflated Sharpe / SPA across the forks you tried; report it.

**Data:** FiinPro (point-in-time, best survivorship integrity) if accessible; document any `vnstock`/CafeF fallback and its biases. Cluster standard errors by announcement date.

---

## 4. Deliverable & timeline

| Stage | Output | Rough effort |
|---|---|---|
| Feasibility gate (§1) | event count + MDE memo | ~1 day |
| Weekend demo (§2) | 1 slide / 1 paragraph + notebook | ~1 weekend |
| Pipeline + pre-registration (§3) | timestamped protocol, data pull, sentiment pipeline | ~3–6 weeks p/t |
| Results + write-up | working paper (SSRN) + clean reproducible repo | ~2–3 months p/t |

**Target outputs that matter for QR:** a *Quantitative Finance* / *Journal of Financial Data Science*-tier working paper, plus a public GitHub repo a desk could rerun. In-sample sentiment papers in non-finance journals do **not** move the QR needle — predictive, after-cost, reproducible work does.

---

## 5. Compliance — settle before you publish anything

You trade VN equities at HSC. Before any public artifact: clear **data licensing** (can HSC/FiinPro data be used + published?), **MNPI** (nothing in the signal derives from non-public desk information), and **employer IP** (does HSC have any claim on research built on/around the day job?). Get this in writing. It's also exactly the conflict-of-interest worry a supervisor will raise — having it handled is a professionalism signal.

---

## 6. How this feeds the three decisions
- **Meeting (Tue 23 Jun):** bring the §2 demo + the §1 event-count number. Pitch the §0 hypothesis. Let it carry the conversation instead of the probe machinery.
- **PhD yes/no (later, with data):** if the artifact gets traction independently, the degree becomes optional and you can target a stronger venue. If you still want RMIT VN, you enter from strength.
- **QR career:** the artifact *is* the signal, regardless of the degree. This is the move that's right under every branch.
