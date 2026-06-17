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
from phd_hub.evaluation.rubric import (
    DIMENSIONS,
    WEIGHT_PROFILES,
    Scorecard,
    rank,
    sensitivity,
)


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


def _truncate(text: str, width: int) -> str:
    return text if len(text) <= width else text[: width - 1] + "…"


def render_sensitivity(cards: list[Scorecard]) -> str:
    report = sensitivity(cards)
    name_w = 30
    col_w = max(13, max(len(p.key) for p in report.profiles) + 2)

    lines: list[str] = []
    lines.append("Sensitivity analysis — overall score (rank) under each weight profile")
    lines.append("=" * (name_w + col_w * len(report.profiles)))
    lines.append("")
    lines.append("Profile emphases:")
    for p in report.profiles:
        lines.append(f"  {p.key:<18} {p.description}")
    lines.append("")

    header = "Project".ljust(name_w) + "".join(p.key.center(col_w) for p in report.profiles)
    lines.append(header)
    lines.append("-" * len(header))

    # Keep rows in default-profile rank order for a stable, readable table.
    ordered = sorted(report.rows, key=lambda r: r.by_profile["default"][1])
    for row in ordered:
        label = row.project + (" (DQ)" if row.disqualified else "")
        cells = ""
        for p in report.profiles:
            score, pos = row.by_profile[p.key]
            cells += f"{score:.0f} (#{pos})".center(col_w)
        lines.append(_truncate(label, name_w).ljust(name_w) + cells)

    lines.append("")
    if report.is_robust:
        winner = next(iter(report.winners.values()))
        lines.append(
            f"✓ Robust: {_truncate(winner, 40)} ranks #1 under all "
            f"{len(report.profiles)} weight profiles."
        )
    else:
        lines.append("⚠ Fragile: the top choice changes with the weights —")
        for pkey, proj in report.winners.items():
            lines.append(f"    under {pkey:<18} #1 is {_truncate(proj, 40)}")
        lines.append("  The ranking is sensitive to weight assumptions; decide the")
        lines.append("  weights deliberately before reading the result.")
    return "\n".join(lines)


def render_sensitivity_json(cards: list[Scorecard]) -> str:
    report = sensitivity(cards)
    payload = {
        "profiles": [
            {"key": p.key, "name": p.name, "description": p.description, "weights": p.weights}
            for p in report.profiles
        ],
        "robust": report.is_robust,
        "winners": report.winners,
        "rows": [
            {
                "project": r.project,
                "disqualified": r.disqualified,
                "by_profile": {
                    k: {"overall": round(v[0], 1), "rank": v[1]}
                    for k, v in r.by_profile.items()
                },
            }
            for r in report.rows
        ],
    }
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
    parser.add_argument(
        "--sensitivity",
        action="store_true",
        help="Re-rank under several weight profiles to test how robust the ranking is",
    )
    args = parser.parse_args()

    try:
        cards = load_scorecards(args.scores)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error loading scores: {exc}", file=sys.stderr)
        raise SystemExit(1)

    if args.sensitivity:
        out = render_sensitivity_json(cards) if args.format == "json" else render_sensitivity(cards)
    else:
        out = render_json(cards) if args.format == "json" else render_text(cards)
    print(out)


if __name__ == "__main__":
    main()
