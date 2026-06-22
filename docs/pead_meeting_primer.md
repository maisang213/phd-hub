# PEAD call — SUBSTANCE PRIMER (read tonight)

> Backs up the moves in `pead_meeting_cheatsheet.md` with the facts to hold a real conversation.
> Numbers flagged *(approx)* come from secondary summaries — say "roughly" if you quote them.

---

## 1. The team's OWN paper — your single best read

**"Decoding market sentiment: the power of ChatGPT in explaining Bitcoin returns from X data"** — *China Finance Review International*, 2025. DOI 10.1108/CFRI-05-2024-0278.
**Authors: Binh Nguyen Thanh, Anh Tuan Nguyen, Thanh Tuan Chu, Son Ha (Hà Xuân Sơn).**

> ⚠️ **Correction to your brief/memory:** Buertey is **NOT** a co-author. This is **Anh + Son + Binh's** paper. It ties *Anh and Son and the LLM-#192 team* together — not Buertey. Cite it **to Anh and Son**, not as "Buertey's group's work."

- **Method:** zero-shot prompting — clean tweets → ChatGPT-4o/3.5 classifies Bullish/Bearish/Neutral "from a Bitcoin investor's perspective." Aggregated into a Bullishness Index + Agreement Index. Benchmarked vs BERT and VADER. No fine-tuning.
- **Data:** crypto-influencer tweets + Bitcoin daily close (Bitstamp), **3 Jan 2018 – 13 Jun 2023**; controls = Fear&Greed, Google Trends, Wikipedia views, etc.
- **Explain vs predict:** **EXPLANATORY / in-sample.** Daily-return regressions on *lagged* sentiment, Newey-West SEs, heavy controls. A Sharpe "strategy" is shown as illustration but **no train/test split, no OOS window, no after-cost backtest.** The title's "explaining" matches the evaluation exactly.
- **Findings:** ChatGPT sentiment significantly explains BTC returns beyond rival indicators; beats BERT/VADER.
- **Quote:** *"Sentiment indicators crafted with ChatGPT4o/ChatGPT3.5 significantly affect Bitcoin returns, even when accounting for a broad array of control variables and other pre-established sentiment indicators."*

**Why this is gold:** it *proves* the house frames sentiment as explain-not-predict, and it leaves an obvious open door. Your pitch writes itself:
> "Your Bitcoin paper already has a sentiment-as-signal Sharpe element — I'd make that rigorous: VN equities, genuine out-of-sample, after-cost. That's the complement your current design doesn't yet test."

---

## 2. The predictive template — Lopez-Lira & Tang (2023), "Can ChatGPT Forecast Stock Price Movements?"

The alpha-native twin of the team's paper. Cite it as the model for your predictive chapter.
- **Method:** news headlines → ChatGPT ("YES good / NO bad / UNKNOWN") → score {+1,−1,0} → predict **next-day** returns. ~50k headlines, post knowledge-cutoff = genuinely OOS.
- **Result:** long-short (long YES / short NO) predicts the drift; *(approx)* ~34 bps/day, annualized Sharpe ~3 pre-cost. Decays over time as LLM adoption spreads.
- **THE caveat (have this ready):** **does NOT survive realistic costs** — ~190% daily turnover; unprofitable at ~20 bps/round-trip. Alpha concentrates in **small-caps + negative news**, exactly where costs bite hardest.
- **Models:** predictability rises with model size; GPT-4 > GPT-3.5; BERT/GPT-2 can't. "Emergent" financial reasoning.

**Use it for:** showing you know predictive ≠ naive. The honest framing is *capacity-aware, after-cost* evaluation — which is the rigorous thing to propose, and disarms a "but is it tradable?" push before it lands.

---

## 3. PEAD canon + "is it still tradable?"

**Canon (table stakes with an accounting lead):**
- **Ball & Brown (1968):** prices move with the earnings surprise — founding capital-markets-accounting paper.
- **Bernard & Thomas (1989/90):** the drift — abnormal returns keep drifting ~60 days post-announcement; investors **underreact** (treat earnings as more random-walk than they are). The anchor PEAD cite.
- **Debate:** risk premium (efficient) vs behavioral underreaction (mispricing) — unsettled; frame as open, don't pick a side in the room.

**Is it still tradable? (you'll be pressed on this):**
- **Decay:** McLean & Pontiff (2016, JF): anomalies ~58% lower **post-publication**; worst for high-return, low-liquidity, high-idio-risk predictors = PEAD's exact profile.
- **Costs:** Chordia et al. (2009): PEAD return ~0.14%/mo (liquid) vs ~1.60%/mo (illiquid) *(approx deciles)*; **costs eat ~63–100%** of the long-short profit. Drift lives where you can't cheaply trade.

**Ready answer (memorize the shape):**
> "Naive drift capture is largely arbitraged away — McLean–Pontiff show ~half the return gone post-publication, Chordia shows the rest concentrates in illiquid names where costs eat 60–100%. So the honest claim isn't 'PEAD prints money' — it's *conditional* residual alpha: evaluate net-of-cost, screen on liquidity, combine the surprise with orthogonal signals like LLM sentiment. That's a measurement-and-signal-combination thesis, not a free-lunch one."

This answer is also your bridge: it makes *sentiment-conditioned PEAD* the natural research question — uniting their interest and yours.

---

## 4. People + LLM #192 fluency

**Anh Tuan Nguyen** (your method ally) — Lecturer in Finance, RMIT VN; ex-UT Arlington. Themes: REIT/property mispricing, mutual-fund flows & spillovers, market efficiency. Name-drop one:
- *"Do Informed REIT Market Participants Respond to Property Sector Mispricing?"* (J. Property Research, 2023)
- *"The information and liquidity effects of mutual fund flows: international spillovers"*
- **Co-author of the ChatGPT-Bitcoin paper** → asset-pricing/efficiency questions land naturally to him.

**LLM #192 — "LLMs for Business Innovation & Decision-Making"** (your pivot target):
- **Leaders:** Hà Xuân Sơn + A/Prof Binh Nguyen Thanh — *both co-authors of the Bitcoin paper.* Direct method link.
- **Program:** DR201 / DR205 / **DR203** ✅ (DR203 = Finance — the enrolment you'd ask for).
- **Predictive language to quote back:** "predict asset prices… characterise investor behaviour… informational efficiency"; benchmarks "**from ARIMA and factor models** to early deep learning"; "capture predictive signals traditional quantitative models miss"; "**LLM-based trading systems**."
- ⚠️ **FoR reality (keep private):** 40% Organisational Behaviour / 35% Pattern Recognition & Data Mining / 25% Innovation Mgmt — **0% finance**. This is the missing prong you'd import via DR203 + Anh. *Do not say this in the room* — it's your reason for the two structural asks, not a critique to voice.

---

## One-line map of the table
**Anh** = finance/asset-pricing method (your ally). **Son + Binh** = the LLM/AI engine (and #192). **Buertey** = accounting lead, the explanatory gravity. The Bitcoin paper already binds Anh+Son+Binh around exactly your topic — your job is to add the *predictive, after-cost* lens and a *finance enrolment*.
</content>
