# A Framework for Evaluating and Justifying Research Projects

> A structured, defensible way to decide *which* research project to pursue and to
> *justify* that decision — for a PhD candidate choosing between advertised projects,
> or a researcher triaging a portfolio of ideas.

This framework does not invent criteria. It synthesises four widely used,
peer-recognised instruments for judging research and adapts them into a single
weighted scorecard suited to selecting a **PhD / HDR project**.

---

## 1. Why a framework (the case for structure)

Choosing a research project is a high-stakes, hard-to-reverse decision made under
uncertainty. People default to gut feel ("this one sounds interesting") and to
salience bias (funding, a famous supervisor). A scorecard does three things that
intuition does not:

1. **Makes the criteria explicit** — you can be challenged on, and defend, each one.
2. **Forces comparison on the same axes** — projects are scored on identical
   dimensions, so the ranking is *commensurable* rather than apples-to-oranges.
3. **Separates merit from feasibility from fit** — a brilliant but unresourced
   project and a trivial but easy one no longer look the same.

The output is not a verdict the number hands you; it is a **structured argument**
you can put in front of a supervisor, a panel, or yourself.

---

## 2. The source instruments

| Instrument | Origin | What it contributes |
|---|---|---|
| **FINER** | Hulley & Cummings, *Designing Clinical Research* | The canonical test of a research *question*: **F**easible, **I**nteresting, **N**ovel, **E**thical, **R**elevant. |
| **Heilmeier Catechism** | George H. Heilmeier, DARPA | Eight questions every proposal must answer — forces a clear contribution, a "who cares", explicit risk, cost/time, and **success metrics** ("midterm and final exams"). |
| **REF assessment criteria** | UK Research Excellence Framework | Research quality decomposed into **Originality, Significance, Rigour** (and Impact). The standard the work will eventually be judged by. |
| **ARC assessment** | Australian Research Council | Significance & innovation, approach & feasibility, research environment, investigator capacity. Directly relevant — RMIT is an Australian institution. |

The dimensions below map back to these so each criterion is **traceable to an
established standard**, not a personal preference.

---

## 3. The dimensions

Seven weighted **merit/fit dimensions** (scored 1–5) plus two **gates** (pass/fail).
Weights sum to 100 and express how much each dimension should move the decision for
a PhD-project choice. They are defaults — override them and state why.

| # | Dimension | Weight | Source mapping | The question it answers |
|---|---|---:|---|---|
| 1 | **Significance & Relevance** | 20 | FINER-R, REF-Significance, Heilmeier "who cares?" | If this succeeds, does it matter — to the field, to practice, to the world? |
| 2 | **Originality & Novelty** | 20 | FINER-N, REF-Originality | Does it make a new contribution, or restate known results? |
| 3 | **Rigour & Tractability** | 15 | REF-Rigour, Heilmeier "how will you measure success?" | Is there a sound method and a *falsifiable, measurable* success criterion? |
| 4 | **Feasibility** | 15 | FINER-F, ARC-feasibility | Can it actually be done in the time, with the data, scope and skills available? |
| 5 | **Resourcing & Supervision** | 10 | ARC research environment | Funding, supervisor expertise *and capacity*, data/infrastructure access. |
| 6 | **Impact & Dissemination** | 10 | REF-Impact, Heilmeier "what's the payoff?" | Will it publish in good venues and/or change practice? What is the reach? |
| 7 | **Candidate Fit** | 10 | (PhD-specific) | Does it match the candidate's skills, motivation and career trajectory? |
| — | **Ethics & Integrity** | GATE | FINER-E | Is it ethical and approvable? A fail disqualifies regardless of score. |
| — | **Capacity / Availability** | GATE | (practical) | Is the project actually *open* and is a supervisor able to take a student? |

### Why gates, not weights
Best practice treats ethics and basic availability as **necessary conditions**, not
tradeable points. A maximally significant, novel, feasible project that is unethical —
or that is already filled — scores zero in practice. Encoding them as gates prevents a
high merit score from masking a disqualifying flaw.

---

## 4. The scoring anchors

Each dimension is scored **1–5** against anchored descriptions so two assessors mean
the same thing by a "4". Full anchors live in `rubric.py` (`Dimension.anchors`);
the shape is:

| Score | Meaning |
|---|---|
| **5** | Exemplary — clearly at the top of this dimension; a strong, defensible claim. |
| **4** | Strong — above the bar with minor reservations. |
| **3** | Adequate — acceptable but unremarkable; the default/"on the fence" score. |
| **2** | Weak — a real concern that needs mitigation. |
| **1** | Poor — a serious deficiency on this dimension. |

Every score **must carry a one-line rationale**. A number without a reason is not
evidence; the rationale is what you defend in front of a panel.

---

## 5. Computing the result

```
weighted_score (1–5)  = Σ(weightᵢ · scoreᵢ) / Σ(weightᵢ)
overall (0–100)       = weighted_score / 5 · 100
gate                  = PASS only if every gate passes
```

- A project that **fails any gate** is reported as **DISQUALIFIED** and ranked last,
  regardless of its weighted score. The weighted score is still shown — it tells you
  what you would lose if the gate could be cleared (e.g. the project reopens).
- Ranking is by `(gate_pass, overall)` descending.

The score is a **decision aid, not a decision rule**. If the ranking and your
judgement disagree, that disagreement is information: usually it means a weight is
wrong for your situation, or a rationale is hiding an unscored consideration. Adjust
the weights *before* you see the scores, not after, to avoid rationalising.

---

## 6. Sensitivity analysis (is the ranking robust?)

Because the weights are value judgements, a ranking is only trustworthy if it
**survives reasonable disagreement about the weights**. The framework ships five
defensible weight profiles and re-ranks the same scores under each:

| Profile | Emphasis |
|---|---|
| `default` | Balanced — merit-led with feasibility close behind |
| `merit_first` | Significance + Originality + Rigour (a pure-research lens) |
| `career_first` | Candidate Fit + Impact (a career-driven lens) |
| `feasibility_first` | Feasibility + Resourcing ("will I actually finish?") |
| `equal` | Every dimension weighted the same |

```bash
python evaluate.py examples/rmit_vn_scores.example.json --sensitivity
```

- If the **same project wins under every profile**, the conclusion is **robust** —
  you can defend it without having to win the argument about exact weights.
- If the **winner flips** between profiles, the result is **fragile** — the decision
  genuinely turns on the weights, so you must justify the weighting itself, not just
  the scores. The tool flags this explicitly and names the winner under each profile.

This is standard practice for any weighted decision model: report the headline result
*and* how sensitive it is to the assumptions behind it.

## 7. How to use it

1. **Set/confirm weights** for your situation (career-driven? weight Candidate Fit and
   Impact up. Exploratory? weight Originality up). Do this *first*.
2. **Score each project** 1–5 on the seven dimensions, with a rationale per score.
3. **Set the two gates** (ethics, availability).
4. **Run** `evaluate.py` to compute weighted scores, apply gates, and rank.
5. **Run `--sensitivity`** to confirm the ranking holds under different weightings.
6. **Read the argument, not just the number.** Use the per-dimension rationales as the
   body of your justification memo / email to a supervisor.

A worked example over three real RMIT Vietnam PhD projects is in
[`docs/worked_example.md`](../../docs/worked_example.md).

---

## 8. Limitations (state these when you present it)

- **Weights are value judgements.** The framework makes them explicit and arguable; it
  does not make them objective — which is exactly why §6 re-ranks under several weightings.
- **Scores are human judgement.** The structured data we hold on a project (funding,
  close date, supervisors) can *signal* some dimensions but cannot score research merit.
  The tool deliberately requires human scores and only *suggests* signals.
- **It ranks, it does not choose.** Treat a near-tie as a tie and break it on
  considerations the rubric doesn't capture.

---

## 9. References

- Hulley, S. B., Cummings, S. R., Browner, W. S., Grady, D. G., & Newman, T. B.
  *Designing Clinical Research* — the FINER criteria.
- Heilmeier, G. H. *The Heilmeier Catechism*, DARPA.
- UK Research Excellence Framework (REF 2021), *Panel criteria and working methods* —
  originality, significance and rigour.
- Australian Research Council, *Instructions to Applicants / Assessor handbooks* —
  significance & innovation, feasibility, research environment.
- Phillips, E. M. & Pugh, D. S. *How to Get a PhD* — forms of originality.
- Booth, W. C., Colomb, G. G., & Williams, J. M. *The Craft of Research*.
