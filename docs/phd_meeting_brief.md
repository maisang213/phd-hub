# PhD supervision meeting — Tue 23 Jun 2026, 1:00–4:00 pm (online)

> **Single source for the meeting.** Replaces the old brief / primer / cheatsheet split.
> Two adjacent projects, two opposite probes, one consolidated playbook.
> Numbers flagged *(approx)* come from secondary summaries — say "roughly" if you quote them.

---

## 0. The one thing to learn

Is the thesis judged on **predicting returns out-of-sample, after costs** — or on **explaining** a relationship?
That single answer routes the whole meeting. You ask the *neutral* version of the question; the **answer** is the diagnostic — never ask the diagnostic out loud.

---

## 1. The room & the situation

**In the room (all cc'd on Buertey's thread):**
- **Samuel Buertey** — DR200 (PhD Accountancy) lead. Accounting / ESG-disclosure (h-12, ~100% CSR/disclosure, **0 asset-pricing**). *Topic gatekeeper on the PEAD arm.*
- **Anh Tuan Nguyen** — Lecturer in Finance, RMIT VN (PhD-track ex-UT Arlington; REIT/property mispricing, fund flows, market efficiency). **Your method ally on EITHER project.** Junior output — pin alpha framing to him, but he can't anchor a thesis alone.
- **Hà Xuân Sơn** — Lecturer, Blockchain Enabled Business (~1.7k cites, **CS/security, not finance**). **Also leads the LLM project #192.** Brings the AI/LLM engine, not asset-pricing judgment.

**This is a DUAL-PURPOSE meeting.** It opens as the PEAD (DR200) conversation. But the team's own published work is in-sample/explanatory, so the ~80%-likely answer to the probe is "explanatory" — at which point **this becomes the LLM #192 meeting.** Son and Anh, the two people who matter for #192, are already in the room. So **both arms are prepped to the same depth.**

**Goal:** find the right *home* for ONE coherent research interest across two adjacent projects.
- **Target:** LLM #192 enrolled under **DR203 (Economics, Finance & Marketing)** + a finance co-sup.
- **Fallback:** PEAD #247 / DR200 — if its framing can be made genuinely predictive.
- **Leave with PEAD intact either way.** Don't burn the fallback.

**Why this configuration —** neither project passes *both* prongs of "predictive verbs AND finance discipline/code/supervisor":
- **LLM #192** — brief is alpha-native ("predict asset prices", benchmarks vs ARIMA/factor models, "LLM-based trading systems") ✅ … but no finance code / no named asset-pricing supervisor ❌.
- **PEAD #247** — has a finance co-sup (Anh) + sits adjacent to finance ✅ … but framing is accounting-EXPLANATORY ("explain over/under-reaction"), examined as Accountancy (DR200) ❌.

Starting from the alpha-native brief and *adding* a supervisor beats starting from an explanatory brief and *fighting* the framing past an accounting lead.

---

## 2. Decision tree

```
DUAL-PURPOSE: opens as PEAD/DR200; on the ~80%-likely "explanatory" answer it BECOMES the LLM #192 meeting.
Both decision-makers for BOTH projects are in the room — prep both arms equally.
│
├─[0] OPEN — both projects on the table, sentence one (legitimizes LLM early; not a fallback yet)
├─[1] FRAME self: quant desk → "does it predict returns OOS, after costs"
│
├─[2] PROBE PEAD (neutral question; the ANSWER is the diagnostic)
│       Q1 OOS-predictability vs explain · Q2 backtest/split vs panel/event-study (qual = hard red)
│       Q4 supervision split (never "will Anh own it?") · Q3 sentiment-source = already GREEN
│       └─ on "explain": YES-AND BRIDGE — "you've shown it explains; I'd add OOS, after-cost"
│
└─[3] BRANCH
      │
      ├── A) PEAD GREEN (predict + Anh owns method) ── ✅ PEAD PRIMARY
      │        → OOS research statement, Anh method lead; LLM = backup (don't kill)
      │
      ├── B) PEAD EXPLANATORY (~80%) ──► THE MEETING NOW BECOMES THE LLM #192 MEETING
      │     │   pivot is a consequence of Buertey's answer, not pre-decided
      │     ├─[B0] TURN TO SON — "your LLM brief frames it directly: predict asset prices,
      │     │       benchmark vs factor models, signals quant misses…"
      │     ├─[B1] PROBE #192 (its OWN diagnostic — INVERSE of PEAD's):
      │     │       QL1 predictive-for-real? "brief says predict & benchmark vs ARIMA/factor —
      │     │           evaluated OOS, after costs? or in-sample like the Bitcoin paper?"
      │     │       QL2 scope: VN equities? universe, data, horizon, which LLM?
      │     │       QL3 supervision split: Anh = asset-pricing method · Son+Binh = LLM engine
      │     ├─[B2] STRUCTURAL ASKS (the prong #192 lacks):
      │     │       1. DR203 (Economics, Finance & Marketing) enrolment — examined as finance
      │     │       2. Anh Nguyen as finance co-sup (LLM team has no asset-pricing lead)
      │     │       3. (verify) official #192 title + supervisory team + program code
      │     └─[B3] READ:
      │            ├─ predictive-real + DR203 + Anh ──────── ✅ LLM #192 PRIMARY (passes all prongs)
      │            ├─ alpha brief but they'd run it in-sample ── ⚠ SAME ceiling as PEAD → C
      │            └─ no DR203 / no finance co-sup ─────────── → C
      │
      └── C) NEITHER LANDS → no RMIT VN project passes predictive+finance → weigh other venues

RAILS (every branch): never voice "fallback"/"flawed"/the FoR-code critique · address asset-pricing to Anh ·
leave PEAD intact · cite the ChatGPT-Bitcoin paper TO ANH & SON (their paper, NOT Buertey's)
```

---

## 3. Logistics

- They pick the time inside the **1:00–4:00 pm** window. CV already sent (`docs/cv/quy-sang-mai-cv.pdf`).
- Fit line stays honest: quant / markets side — **not** claiming NLP / generative-AI experience yet.

---

## 4. SAY (in order)

**[0] Open — shared ground, legitimise both projects**
> "Both your DR200 sentiment project and Son's LLM project sit on the same ground I care about — sentiment, LLMs, earnings reactions, market anomalies. I wanted to use this to figure out which is the right home for the question I'd actually want to answer."

**[1] Frame myself (honest, QR)**
> "My background's a quant trading desk, so I instinctively frame a sentiment question as 'does this predict returns out-of-sample, after costs.' I want to check that fits how you'd build the thesis."

**[2] THE decisive question — neutral either/or, ask early**
> "Would the thesis be judged on whether the sentiment signal **predicts returns out-of-sample, after costs**, or on **explaining** investors' over/under-reaction to earnings? I want to build toward the right one."

**[2b] Supervision split — gets method-ownership WITHOUT asking for it**
> "Since it spans accounting, finance and AI across the three of you — how would supervision divide up? Who would I mainly work with on the empirical / asset-pricing side, versus the sentiment-extraction and earnings-surprise pieces?"
> → **Let Buertey describe it first.** Anh handed the empirical lead = confirmed.

---

## 5. PEAD arm — read the answers

| # | Ask | ✅ GREEN (predictive) | ❌ RED (explanatory/accounting) |
|-----|---------------------------------|-------------------------------|-------------------------------|
| Q1 | Judged on **OOS return predictability**, or explaining a relationship? | "predict / survive costs / tradable" | "establish / explain the channel" |
| Q2 | **Predictive backtest** w/ train-test split, or panel/event-study? | "walk-forward / hold-out / net-of-cost" | "panel / fixed effects" — **qual = hard red flag** |
| Q4 | *(diagnostic — never ask verbatim)* Does Anh own the empirical method? | "you'd work with Anh on the empirical side" | "I'd guide all the empirical framing myself" |

*(Q3 — sentiment source — is already GREEN: the brief specifies broad social media + news, **not** ESG/sustainability disclosure. Don't relitigate it.)*

**The instant you hear "explain" → YES-AND BRIDGE (don't act surprised — you already know this is likely):**
> "You've shown sentiment *explains* returns; I'd *add* the out-of-sample, after-cost predictive test on VN equities — same data, same LLM sentiment layer, one extra evaluation lens."

Their Bitcoin paper's own illustrative Sharpe element is the hook that makes this land. The gap (no OOS / no after-cost) **is** your thesis.

---

## 6. LLM #192 arm — read the answers

The inverse problem: #192's *brief* is already predictive, but the team's *house style* is explanatory. So you confirm they'd actually build it predictively, then import the missing finance prong.

| # | Ask | ✅ GREEN | ⚠ RED (same ceiling as PEAD) |
|-----|---------------------------------|-------------------------------|-------------------------------|
| QL1 | Evaluated **OOS, after costs, vs ARIMA/factor benchmarks** — or in-sample like the Bitcoin paper? | "walk-forward / hold-out / net-of-cost / beat the factor model" | "contemporaneous / in-sample / explain the relationship" |
| QL2 | **Scope** — VN equities? universe, data source, horizon, which LLM? | concrete, tradable framing | "we'd see / it's open" with no markets realism |
| QL3 | **Supervision split** — who owns the asset-pricing method? | "Anh on the empirical/finance side" | "Son and I would shape it" (no finance lead) |

**Structural asks (the prong #192 lacks) — float, don't demand:**
1. **DR203 enrolment** — confirm #192 can be taken under **PhD (Economics, Finance & Marketing)** so it's examined as finance, not Business/management.
2. **Anh Nguyen as finance co-sup** — the LLM team is Son (CS) + Binh (econ/crypto), with **no named asset-pricing lead**.
3. **Verify the basics** — "#192" is an internal tracking number; it isn't in RMIT's public HDR database. Naturally ask the official **title, full supervisory team, and which program code** it sits under.

**Scope answer — have this ready for "what would you actually build?" (shows quant-desk realism):**
> "VN30 / liquid-HOSE universe; LLM sentiment from Vietnamese financial news + earnings announcements; predict post-announcement drift returns. Walk-forward out-of-sample, net of ~0.2–0.5% round-trip including the 0.1% sell tax. **Long-only or via VN30 futures, because there's no real stock short-selling yet** — so a textbook long-short isn't tradable on the short leg. Control for the ±7% HOSE price-limit censoring and the FTSE Frontier→Secondary-Emerging upgrade (effective 21 Sep 2026) as a passive-flow confound. Point-in-time data (FiinPro) to avoid survivorship/restatement bias. Benchmark against ARIMA, a Fama-French factor model, and an LSTM."

---

## 7. Substance bank (shared across both arms)

### 7.1 The team's OWN paper — your single best read
**"Decoding market sentiment: the power of ChatGPT in explaining Bitcoin returns from X data"** — *China Finance Review International*, 2025. DOI 10.1108/CFRI-05-2024-0278.
**Authors: Binh Thanh Nguyen, Tuan Thanh Chu, Son Xuan Ha (= Hà Xuân Sơn), Anh Tuan Nguyen — all RMIT VN. ⚠ Buertey is NOT a co-author.** This binds **Anh + Son + Binh (the LLM #192 leaders)** to your exact topic. **Cite it to Anh and Son**, never as "Buertey's group's work."
- **Method:** zero-shot prompting — clean tweets → ChatGPT-4o/3.5 classifies Bullish/Bearish/Neutral → Bullishness + Agreement indices. Benchmarked vs BERT and VADER. No fine-tuning.
- **Data:** crypto-influencer tweets + BTC daily close (Bitstamp), 3 Jan 2018 – 13 Jun 2023; controls = Fear&Greed, Google Trends, Wikipedia views.
- **Explain vs predict:** **EXPLANATORY / in-sample** — contemporaneous (same-day) sentiment-on-returns regressions, heavy controls, BERT/VADER benchmarks. **No train/test split, no OOS window, no after-cost backtest.** The title's "explaining" matches the evaluation exactly.
- **Use it as:** proof the topic is live AND proof of the open door — *"you've shown sentiment explains returns; I'd make the Sharpe element rigorous: VN equities, genuine OOS, after-cost."*

### 7.2 The predictive template — Lopez-Lira & Tang (2023)
"Can ChatGPT Forecast Stock Price Movements?" arXiv:2304.07619 / SSRN 4412788 (forthcoming JFE). The alpha-native twin of the team's paper — cite as the model for your predictive chapter.
- News headlines → ChatGPT (good/bad/unknown) → score → predict **next-day** returns; tested only on **post-training-cutoff** data = genuinely OOS.
- Long-short predicts the drift; alpha concentrates in **small-caps + negative news**; rises with model size (GPT-4 > GPT-3.5; BERT/GPT-2 can't); **decays as LLM adoption spreads**.
- **THE caveat (have it ready):** cost/turnover figures *(approx, secondary — verify before quoting)* suggest it struggles at realistic costs; alpha sits exactly where costs bite hardest. So the honest framing is *capacity-aware, after-cost* evaluation.
- **Glasserman & Lin (2023/24):** look-ahead bias is *not* the dominant driver; LLM company knowledge can even hurt ("distraction effect").
- **Consensus (2025 "The New Quant" survey, arXiv:2510.05533):** **no settled evidence LLMs durably beat ARIMA/LSTM/factor baselines OOS net of costs** — value is conditional/complementary (events, regime shifts). Foreground this honesty; it disarms a "but is it tradable?" push.

### 7.3 PEAD canon + "is it still tradable?" (table stakes with an accounting lead)
- **Ball & Brown (1968):** prices move with the earnings surprise — founding capital-markets-accounting paper.
- **Bernard & Thomas (1989/90):** the drift — abnormal returns keep drifting ~60 days post-announcement; investors **underreact**. The anchor PEAD cite.
- **Debate:** risk premium (efficient) vs behavioral underreaction (mispricing) — unsettled; frame as open, don't pick a side.
- **Still tradable?** McLean & Pontiff (2016, JF): anomalies ~58% lower post-publication, worst for low-liquidity/high-idio-risk predictors = PEAD's exact profile. Chordia et al. (2009): drift ~0.14%/mo (liquid) vs ~1.60%/mo (illiquid) *(approx)*; **costs eat ~63–100%** of the long-short profit.
- **Ready answer:** *"Naive drift capture is largely arbitraged away — McLean–Pontiff show ~half gone post-publication, Chordia shows the rest concentrates in illiquid names where costs eat 60–100%. So the honest claim isn't 'PEAD prints money' — it's conditional residual alpha: net-of-cost, liquidity-screened, combined with orthogonal signals like LLM sentiment. A measurement-and-signal-combination thesis, not a free-lunch one."*

### 7.4 Benchmark fluency (for the LLM arm)
- **ARIMA** = univariate time-series null (≈ random walk for returns) — the "can you beat it OOS?" test.
- **Fama-French 3/5-factor (+ Carhart momentum)** = the alpha test; a significant intercept = unexplained return.
- **LSTM/GRU/CNN, Gu-Kelly-Xiu (2020)** = the nonlinear ML benchmark. *Caveat:* many LSTM "wins" are on price *levels* (trivially autocorrelated), not returns — know the difference.

### 7.5 Vietnam-equities realities (your edge — shows markets realism)
- **Exchanges:** HOSE (liquid large caps; VN-Index, VN30 = the investable universe), HNX (smaller), UPCoM (largely paper-only for backtests).
- **Price limits censor returns / block limit-up fills:** HOSE ±7%, HNX ±10%, UPCoM ±15%.
- **No real stock short-selling yet** → long-short untradeable on the short leg; use **long-only or VN30 futures**. (T+0 / SBL roadmapped 2026–28.)
- **Foreign Ownership Limit "two-price" problem:** at full FOL, foreigners transact at an off-screen premium on top blue chips (banks, VCB, FPT) — quoted price ≠ achievable foreign price. State your investor assumption. (Circular 68, Nov 2024, removed foreign pre-funding.)
- **Regime breaks to control for:** KRX system live on HOSE (5 May 2025); **FTSE Frontier→Secondary-Emerging upgrade effective 21 Sep 2026** (~28 stocks get passive inflows — a demand-shock confound). MSCI still Frontier *(re-verify)*.
- **Costs:** round-trip ~0.2–0.5% incl. mandatory 0.1% sell tax (charged even at a loss). T+2 settlement.
- **Data:** FiinGroup/FiinPro = academic standard (best point-in-time integrity). `vnstock` is convenient but survivorship/PIT-prone. Traps: survivorship (cross-exchange ticker migration), restatement/PIT bias, short history, stock-dividend back-adjustment, stale prices in thin names.

---

## 8. People — one-line map of the table
**Anh** = finance / asset-pricing method (your ally, on *either* path). **Son + Binh** = the LLM/AI engine (and #192). **Buertey** = accounting lead, the explanatory gravity. The Bitcoin paper already binds **Anh + Son + Binh** around exactly your topic — your job is to add the *predictive, after-cost* lens and a *finance enrolment*.

---

## 9. Diplomacy rails (the delicate part — apply on every branch)
- ❌ Never voice the FoR-code critique ("your project is 40% organisational behaviour") — private diagnostic, not for the team that wrote it.
- ❌ Never frame either project as "flawed." Frame as *fit between one coherent interest and two adjacent projects.*
- ❌ Never say "fallback" out loud.
- ❌ Never ask "will Anh own the method instead of you?" — insults the lead in his own meeting (esp. VN academic hierarchy). Ask the **split**; the answer is the diagnostic.
- ❌ Don't push back in the room if Buertey claims all empirical framing — note it silently.
- ✅ Address asset-pricing / method questions to **Anh** — signals you know who the finance brain is.
- ✅ **Leave with PEAD intact**, even if you're aiming for LLM/DR203.

---

## 10. On-the-spot decision rule
- **PEAD GREEN** (predictive + Anh owns method) → take PEAD; LLM = backup.
- **PEAD EXPLANATORY** **AND** Son open to **LLM-under-DR203 + Anh co-sup + genuine OOS evaluation** → that's your primary (the only configuration passing all prongs).
- **Neither lands** (PEAD explanatory AND LLM blocked/in-sample) → no RMIT VN project passes the predictive+finance test → seriously weigh other venues for a QR-track PhD.
