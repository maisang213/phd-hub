"""Load scorecards from JSON and derive optional signals from project metadata.

The scores file is the assessor's input — a list of projects, each with 1–5
dimension scores (+ rationale) and gate results. See ``examples/`` for the shape.

``suggest_signals`` is deliberately *advisory only*: structured metadata (funding,
close date, supervisors) can hint at the Resourcing and Availability axes, but it
never sets a score. Research merit stays a human judgement.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Optional

from phd_hub.evaluation.rubric import (
    DimensionScore,
    GateResult,
    Scorecard,
)


def scorecard_from_dict(data: dict) -> Scorecard:
    """Build a Scorecard from a plain dict (one project of a scores file)."""
    scores = [
        DimensionScore(key=k, score=v["score"], rationale=v.get("rationale", ""))
        for k, v in data.get("scores", {}).items()
    ]
    gates = [
        GateResult(key=k, passed=v["passed"], rationale=v.get("rationale", ""))
        for k, v in data.get("gates", {}).items()
    ]
    return Scorecard(project=data["project"], scores=scores, gates=gates)


def load_scorecards(path: Path) -> list[Scorecard]:
    """Load a scores JSON file → list of Scorecards.

    File shape: ``{"projects": [ {project, scores, gates}, ... ]}``.
    """
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [scorecard_from_dict(p) for p in data["projects"]]


def suggest_signals(project: dict, today: Optional[date] = None) -> dict[str, str]:
    """Advisory hints derived from a fetched project dict (never a score).

    Returns a mapping of dimension/gate key → human-readable hint so an assessor
    can sanity-check their scores against the structured metadata.
    """
    today = today or date.today()
    hints: dict[str, str] = {}

    funded = project.get("funded")
    if funded is True:
        hints["resourcing"] = "metadata: project is FUNDED (supports a higher resourcing score)"
    elif funded is False:
        hints["resourcing"] = "metadata: project is UNFUNDED (consider a lower resourcing score)"

    close = project.get("close_date")
    if close:
        try:
            closed = date.fromisoformat(close)
            if closed < today:
                hints["availability"] = f"metadata: close date {close} has PASSED (check it is still open)"
            else:
                hints["availability"] = f"metadata: open until {close}"
        except ValueError:
            pass

    leader = project.get("team_leader")
    if leader:
        hints["resourcing"] = (
            hints.get("resourcing", "") + f" | lead supervisor: {leader}"
        ).strip(" |")

    return hints
