"""Research-project evaluation framework.

A weighted scorecard for selecting a PhD/HDR research project, grounded in FINER,
the Heilmeier Catechism, and REF/ARC assessment criteria. See ``framework.md``.
"""

from phd_hub.evaluation.rubric import (
    DIMENSIONS,
    GATES,
    WEIGHT_PROFILES,
    DimensionScore,
    GateResult,
    Scorecard,
    SensitivityReport,
    WeightProfile,
    rank,
    rank_by,
    sensitivity,
)

__all__ = [
    "DIMENSIONS",
    "GATES",
    "WEIGHT_PROFILES",
    "DimensionScore",
    "GateResult",
    "Scorecard",
    "SensitivityReport",
    "WeightProfile",
    "rank",
    "rank_by",
    "sensitivity",
]
