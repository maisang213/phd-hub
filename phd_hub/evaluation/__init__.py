"""Research-project evaluation framework.

A weighted scorecard for selecting a PhD/HDR research project, grounded in FINER,
the Heilmeier Catechism, and REF/ARC assessment criteria. See ``framework.md``.
"""

from phd_hub.evaluation.rubric import (
    DIMENSIONS,
    GATES,
    DimensionScore,
    GateResult,
    Scorecard,
    rank,
)

__all__ = [
    "DIMENSIONS",
    "GATES",
    "DimensionScore",
    "GateResult",
    "Scorecard",
    "rank",
]
