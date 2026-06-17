# Worked example — three RMIT Vietnam PhD projects

Applying the [evaluation framework](../phd_hub/evaluation/framework.md) to the three
candidate projects, from the perspective of a CFA-holding quant trader targeting a
**PhD → quantitative-research (QR)** career. This is the kind of justification memo
the framework is meant to produce.

## Weights used

Default weights, which already privilege the things that matter for a research career:
Significance (20) and Originality (20) lead, then Rigour (15) and Feasibility (15),
then Resourcing / Impact / Candidate-Fit (10 each). For a career-driven choice this is
a reasonable default; if anything, Candidate Fit could be raised — doing so only widens
the gap in PEAD's favour, so the ranking is robust to that adjustment.

## Result

Reproduce with:

```bash
python evaluate.py examples/rmit_vn_scores.example.json
```

```
#1  PEAD/Sentiment — Investor Sentiment, Earnings Surprises & Market Anomalies
    Overall:  82.0/100   (weighted 4.10/5)

#2  LLM — Large Language Models for Business Innovation & Decision-Making
    Overall:  74.0/100   (weighted 3.70/5)

#3  MAS — Multi-AI Agents System for Adaptive Portfolio Management   ⛔ DISQUALIFIED
    Overall:  56.0/100   (weighted 2.80/5)
    GATE FAILED — Capacity / Availability: CLOSED — candidate already recruited.
```

## Reading the result

- **PEAD/Sentiment (82)** wins on the dimension that the framework — and a QR career —
  weight most: it is the only project scoring **5 on Candidate Fit**, because anomaly
  prediction *is* alpha, and it pairs that with a **falsifiable success metric**
  (out-of-sample, risk-adjusted returns) that lifts its Rigour score above LLM's.
- **LLM (74)** is a genuinely strong backup — same funding, same anchor supervisor
  (Ha Xuan Son) — but loses ground on **Rigour** and **Feasibility**: LLM price-prediction
  is harder to pin to a falsifiable claim and carries compute/data-licensing risk.
  An 8-point gap, not a chasm: a sensible fallback if PEAD supervision falls through.
- **MAS (56) is disqualified by a gate, not by its score.** Even at a weighted 2.8/5 the
  point is that *availability* is a necessary condition: the project is closed and the
  lead supervisor is at capacity (confirmed 2026-06-16). The framework reports the
  score anyway, so you can see there was nothing worth reopening it for — it was the
  weakest on merit too (poor QR fit, unfunded).

## How to use this as justification

The per-dimension rationales *are* the argument. To justify the choice to a supervisor
or yourself, you don't say "it scored 82" — you say: *"PEAD ranks first because it is the
only option that is simultaneously alpha-shaped (Candidate Fit 5), falsifiable (a clean
out-of-sample return metric), and fully resourced — and the one project that beat it on
nothing did so on no dimension."* That is a defensible claim, traceable to explicit
criteria, which is exactly what the framework is for.

> Scores reflect the candidate's stated context (see project memory) and are first-pass
> estimates. Edit `examples/rmit_vn_scores.example.json` and re-run to test how sensitive
> the ranking is to your assumptions.
