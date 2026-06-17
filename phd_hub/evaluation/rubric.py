"""Research-project evaluation rubric.

A weighted scorecard for selecting a PhD/HDR research project, synthesised from
four established instruments — FINER (Hulley & Cummings), the Heilmeier Catechism
(DARPA), the REF criteria (originality/significance/rigour), and ARC assessment.

See ``framework.md`` for the full rationale and source mapping.

Design choice: research *merit* cannot be scored from structured metadata — it is a
human judgement. This module therefore models the rubric and the arithmetic; the
1–5 scores are supplied by an assessor (see ``evaluate.py`` / the example scores
file). Ethics and availability are modelled as **gates**, not weighted dimensions:
failing either disqualifies a project regardless of its weighted score.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Dimension:
    """One weighted, 1–5 scored axis of the rubric."""

    key: str
    name: str
    weight: int          # relative weight; the set of weights sums to 100
    source: str          # which established instrument this maps back to
    question: str        # the question the dimension answers
    anchors: dict[int, str]  # 1/3/5 anchored descriptions


# Score anchors are written at 1/3/5; 2 and 4 are interpolations ("between").
DIMENSIONS: tuple[Dimension, ...] = (
    Dimension(
        key="significance",
        name="Significance & Relevance",
        weight=20,
        source="FINER-Relevant; REF-Significance; Heilmeier 'who cares?'",
        question="If this succeeds, does it matter — to the field, to practice, to the world?",
        anchors={
            5: "Addresses a question the field/practice openly cares about; success "
               "would change how people think or act.",
            3: "A legitimate but incremental question; matters to a sub-community.",
            1: "Of marginal interest; success would change little.",
        },
    ),
    Dimension(
        key="originality",
        name="Originality & Novelty",
        weight=20,
        source="FINER-Novel; REF-Originality",
        question="Does it make a new contribution, or restate known results?",
        anchors={
            5: "Clear, identifiable gap; a genuinely new question, method, dataset or angle.",
            3: "A new application or combination of known ideas; modest novelty.",
            1: "Largely replicates existing work; unclear what is new.",
        },
    ),
    Dimension(
        key="rigour",
        name="Rigour & Tractability",
        weight=15,
        source="REF-Rigour; Heilmeier 'how will you measure success?'",
        question="Is there a sound method and a falsifiable, measurable success criterion?",
        anchors={
            5: "Credible methodology and an explicit, falsifiable success metric "
               "('what result would prove/disprove the claim?').",
            3: "Reasonable method; success criteria present but loosely defined.",
            1: "Method unclear or unfalsifiable; no way to tell success from failure.",
        },
    ),
    Dimension(
        key="feasibility",
        name="Feasibility",
        weight=15,
        source="FINER-Feasible; ARC approach & feasibility",
        question="Can it be done in the time, with the data, scope and skills available?",
        anchors={
            5: "Scope fits the candidature; data/tools accessible now; required skills in reach.",
            3: "Achievable but with real scope, data-access or skills risk to manage.",
            1: "Scope, data or skills make completion unlikely within the candidature.",
        },
    ),
    Dimension(
        key="resourcing",
        name="Resourcing & Supervision",
        weight=10,
        source="ARC research environment",
        question="Funding, supervisor expertise AND capacity, data/infrastructure access?",
        anchors={
            5: "Funded; expert supervisor(s) with confirmed capacity; infrastructure in place.",
            3: "Partial support; supervisor fit good but capacity or funding uncertain.",
            1: "Unfunded and/or no available expert supervisor; infrastructure gaps.",
        },
    ),
    Dimension(
        key="impact",
        name="Impact & Dissemination",
        weight=10,
        source="REF-Impact; Heilmeier 'what's the payoff?'",
        question="Will it publish in good venues and/or change practice? What is the reach?",
        anchors={
            5: "Clear path to strong publications and/or real-world adoption; broad reach.",
            3: "Publishable in mid-tier venues; limited but real practical reach.",
            1: "Hard to publish; negligible external reach.",
        },
    ),
    Dimension(
        key="candidate_fit",
        name="Candidate Fit",
        weight=10,
        source="PhD-specific (skills, motivation, career trajectory)",
        question="Does it match the candidate's skills, motivation and career trajectory?",
        anchors={
            5: "Squarely on the candidate's skills and career path; high intrinsic motivation.",
            3: "Adjacent to the candidate's strengths/goals; would require some stretch.",
            1: "Off the candidate's skills or career direction.",
        },
    ),
)

DIMENSION_BY_KEY: dict[str, Dimension] = {d.key: d for d in DIMENSIONS}


@dataclass(frozen=True)
class Gate:
    """A pass/fail necessary condition. A fail disqualifies the project."""

    key: str
    name: str
    source: str
    question: str


GATES: tuple[Gate, ...] = (
    Gate(
        key="ethics",
        name="Ethics & Integrity",
        source="FINER-Ethical",
        question="Is it ethical and approvable (human-subjects, data, integrity)?",
    ),
    Gate(
        key="availability",
        name="Capacity / Availability",
        source="practical",
        question="Is the project actually open and can a supervisor take a student?",
    ),
)

GATE_BY_KEY: dict[str, Gate] = {g.key: g for g in GATES}

MIN_SCORE, MAX_SCORE = 1, 5


@dataclass
class DimensionScore:
    """An assessor's 1–5 score for one dimension, with a defended rationale."""

    key: str
    score: int
    rationale: str

    def __post_init__(self) -> None:
        if self.key not in DIMENSION_BY_KEY:
            raise ValueError(f"Unknown dimension: {self.key!r}")
        if not (MIN_SCORE <= self.score <= MAX_SCORE):
            raise ValueError(
                f"Score for {self.key!r} must be {MIN_SCORE}–{MAX_SCORE}, got {self.score}"
            )

    @property
    def dimension(self) -> Dimension:
        return DIMENSION_BY_KEY[self.key]


@dataclass
class GateResult:
    """Pass/fail for a gate, with a rationale."""

    key: str
    passed: bool
    rationale: str

    def __post_init__(self) -> None:
        if self.key not in GATE_BY_KEY:
            raise ValueError(f"Unknown gate: {self.key!r}")

    @property
    def gate(self) -> Gate:
        return GATE_BY_KEY[self.key]


@dataclass
class Scorecard:
    """A fully scored project: dimension scores, gate results, derived totals."""

    project: str
    scores: list[DimensionScore]
    gates: list[GateResult] = field(default_factory=list)

    def __post_init__(self) -> None:
        missing = {d.key for d in DIMENSIONS} - {s.key for s in self.scores}
        if missing:
            raise ValueError(
                f"{self.project!r} missing scores for: {sorted(missing)}"
            )

    @property
    def weighted_score(self) -> float:
        """Weighted average on the native 1–5 scale."""
        total_w = sum(s.dimension.weight for s in self.scores)
        weighted = sum(s.dimension.weight * s.score for s in self.scores)
        return weighted / total_w

    @property
    def overall(self) -> float:
        """Weighted score rescaled to 0–100 (percentage of the maximum)."""
        return self.weighted_score / MAX_SCORE * 100

    @property
    def failed_gates(self) -> list[GateResult]:
        return [g for g in self.gates if not g.passed]

    @property
    def disqualified(self) -> bool:
        return bool(self.failed_gates)


def rank(cards: list[Scorecard]) -> list[Scorecard]:
    """Rank by (not disqualified, overall) descending. Gated projects sink last."""
    return sorted(cards, key=lambda c: (not c.disqualified, c.overall), reverse=True)
