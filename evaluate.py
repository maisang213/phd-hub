#!/usr/bin/env python3
"""CLI to score and rank research projects against the evaluation framework.

Reads a scores JSON file (assessor input — see examples/), computes weighted
scores, applies the ethics/availability gates, and prints a ranked report.

    python evaluate.py examples/rmit_vn_scores.example.json
    python evaluate.py scores.json --format json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from phd_hub.evaluation.loader import load_scorecards
from phd_hub.evaluation.rubric import DIMENSIONS, Scorecard, rank


def _card_to_dict(card: Scorecard, position: int) -> dict:
    return {
        "rank": position,
        "project": card.project,
        "overall": round(card.overall, 1),
        "weighted_score": round(card.weighted_score, 2),
        "disqualified": card.disqualified,
        "failed_gates": [g.gate.name for g in card.failed_gates],
        "scores": {
            s.key: {"score": s.score, "rationale": s.rationale} for s in card.scores
        },
    }


def render_text(cards: list[Scorecard]) -> str:
    ranked = rank(cards)
    lines: list[str] = []
    lines.append("Research Project Evaluation — ranked")
    lines.append("=" * 60)
    for i, card in enumerate(ranked, start=1):
        flag = "  ⛔ DISQUALIFIED" if card.disqualified else ""
        lines.append("")
        lines.append(f"#{i}  {card.project}{flag}")
        lines.append(f"    Overall: {card.overall:5.1f}/100   (weighted {card.weighted_score:.2f}/5)")
        if card.disqualified:
            for g in card.failed_gates:
                lines.append(f"    GATE FAILED — {g.gate.name}: {g.rationale}")
        for d in DIMENSIONS:
            s = next(s for s in card.scores if s.key == d.key)
            bar = "█" * s.score + "·" * (5 - s.score)
            lines.append(f"    {bar} {s.score}  {d.name:<26} {s.rationale}")
    lines.append("")
    lines.append("Score is a decision aid, not a decision rule. Read the rationales,")
    lines.append("and re-rank under different weights to sensitivity-test the result.")
    return "\n".join(lines)


def render_json(cards: list[Scorecard]) -> str:
    ranked = rank(cards)
    payload = [_card_to_dict(c, i) for i, c in enumerate(ranked, start=1)]
    return json.dumps(payload, ensure_ascii=False, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(description="Score and rank research projects")
    parser.add_argument("scores", type=Path, help="Path to a scores JSON file")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    args = parser.parse_args()

    try:
        cards = load_scorecards(args.scores)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error loading scores: {exc}", file=sys.stderr)
        raise SystemExit(1)

    out = render_json(cards) if args.format == "json" else render_text(cards)
    print(out)


if __name__ == "__main__":
    main()
