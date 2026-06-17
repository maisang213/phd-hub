"""Tests for the research-project evaluation framework."""

from datetime import date
from pathlib import Path

import pytest

from phd_hub.evaluation.rubric import (
    DIMENSIONS,
    WEIGHT_PROFILES,
    DimensionScore,
    GateResult,
    Scorecard,
    WeightProfile,
    rank,
    rank_by,
    sensitivity,
)
from phd_hub.evaluation.loader import (
    load_scorecards,
    scorecard_from_dict,
    suggest_signals,
)

EXAMPLE = Path(__file__).parent.parent / "examples" / "rmit_vn_scores.example.json"


def _full_scores(value: int) -> list[DimensionScore]:
    return [DimensionScore(d.key, value, "x") for d in DIMENSIONS]


class TestWeights:
    def test_weights_sum_to_100(self):
        assert sum(d.weight for d in DIMENSIONS) == 100


class TestDimensionScore:
    def test_rejects_out_of_range(self):
        with pytest.raises(ValueError, match="must be 1–5"):
            DimensionScore("significance", 6, "too high")

    def test_rejects_unknown_dimension(self):
        with pytest.raises(ValueError, match="Unknown dimension"):
            DimensionScore("not_a_dim", 3, "x")


class TestScorecard:
    def test_requires_all_dimensions(self):
        with pytest.raises(ValueError, match="missing scores"):
            Scorecard("P", [DimensionScore("significance", 3, "x")])

    def test_all_fives_is_100(self):
        card = Scorecard("P", _full_scores(5))
        assert card.overall == 100.0
        assert card.weighted_score == 5.0

    def test_all_threes_is_60(self):
        card = Scorecard("P", _full_scores(3))
        assert card.overall == pytest.approx(60.0)

    def test_weighting_favours_heavier_dimensions(self):
        # 5 on the two 20-weight dims, 1 elsewhere vs the inverse.
        heavy = {"significance", "originality"}
        a = Scorecard("A", [DimensionScore(d.key, 5 if d.key in heavy else 1, "x") for d in DIMENSIONS])
        b = Scorecard("B", [DimensionScore(d.key, 1 if d.key in heavy else 5, "x") for d in DIMENSIONS])
        assert a.overall < b.overall  # heavy dims are only 40 of 100, so b (other 60) wins

    def test_gate_failure_disqualifies(self):
        card = Scorecard(
            "P",
            _full_scores(5),
            gates=[GateResult("availability", False, "closed")],
        )
        assert card.disqualified
        assert card.overall == 100.0  # weighted score still reported


class TestRank:
    def test_disqualified_sinks_below_lower_scorer(self):
        strong_closed = Scorecard("closed", _full_scores(5), [GateResult("availability", False, "x")])
        weak_open = Scorecard("open", _full_scores(2))
        ranked = rank([strong_closed, weak_open])
        assert [c.project for c in ranked] == ["open", "closed"]


class TestWeightProfiles:
    def test_builtin_profiles_cover_all_dimensions(self):
        keys = {d.key for d in DIMENSIONS}
        for p in WEIGHT_PROFILES:
            assert set(p.weights) == keys

    def test_profile_rejects_missing_dimension(self):
        with pytest.raises(ValueError, match="dimension mismatch"):
            WeightProfile("bad", "Bad", "x", {"significance": 1})

    def test_profile_rejects_zero_sum(self):
        with pytest.raises(ValueError, match="sum to zero"):
            WeightProfile("z", "Z", "x", {d.key: 0 for d in DIMENSIONS})

    def test_overall_with_equal_weights_is_plain_average(self):
        # Equal weights -> overall is just the mean score rescaled to 0–100.
        equal = {d.key: 1.0 for d in DIMENSIONS}
        values = [(i % 5) + 1 for i in range(len(DIMENSIONS))]  # 1..5 cycling, all in range
        scores = [DimensionScore(d.key, v, "x") for d, v in zip(DIMENSIONS, values)]
        card = Scorecard("P", scores)
        expected = sum(values) / len(values) / 5 * 100
        assert card.overall_with(equal) == pytest.approx(expected)

    def test_default_overall_unchanged_by_refactor(self):
        card = Scorecard("P", [DimensionScore(d.key, 3, "x") for d in DIMENSIONS])
        assert card.overall == pytest.approx(60.0)
        assert card.overall_with() == card.overall


class TestRankBy:
    def test_reweighting_can_change_order(self):
        # A strong on the merit dims; B strong on the career dims (fit + impact).
        merit = {"significance", "originality"}
        career = {"candidate_fit", "impact"}
        a = Scorecard("A", [DimensionScore(d.key, 5 if d.key in merit else 2, "x") for d in DIMENSIONS])
        b = Scorecard("B", [DimensionScore(d.key, 5 if d.key in career else 2, "x") for d in DIMENSIONS])
        merit_first = next(p for p in WEIGHT_PROFILES if p.key == "merit_first").weights
        career_first = next(p for p in WEIGHT_PROFILES if p.key == "career_first").weights
        assert rank_by([a, b], merit_first)[0].project == "A"
        assert rank_by([a, b], career_first)[0].project == "B"


class TestSensitivity:
    def test_pead_robust_across_all_profiles(self):
        cards = load_scorecards(EXAMPLE)
        report = sensitivity(cards)
        assert report.is_robust
        assert all(w.startswith("PEAD") for w in report.winners.values())

    def test_report_covers_every_project_and_profile(self):
        cards = load_scorecards(EXAMPLE)
        report = sensitivity(cards)
        assert len(report.rows) == len(cards)
        for row in report.rows:
            assert set(row.by_profile) == {p.key for p in WEIGHT_PROFILES}

    def test_fragile_when_winner_flips(self):
        merit = {"significance", "originality"}
        career = {"candidate_fit", "impact"}
        a = Scorecard("A", [DimensionScore(d.key, 5 if d.key in merit else 1, "x") for d in DIMENSIONS])
        b = Scorecard("B", [DimensionScore(d.key, 5 if d.key in career else 1, "x") for d in DIMENSIONS])
        report = sensitivity([a, b])
        assert not report.is_robust


class TestLoader:
    def test_scorecard_from_dict_roundtrip(self):
        card = scorecard_from_dict({
            "project": "P",
            "scores": {d.key: {"score": 4, "rationale": "r"} for d in DIMENSIONS},
            "gates": {"ethics": {"passed": True, "rationale": "ok"}},
        })
        assert card.overall == 80.0
        assert not card.disqualified

    def test_load_example_file_ranks_pead_first_mas_last(self):
        cards = load_scorecards(EXAMPLE)
        ranked = rank(cards)
        assert ranked[0].project.startswith("PEAD")
        assert ranked[-1].project.startswith("MAS")
        assert ranked[-1].disqualified  # MAS is closed


class TestSignals:
    def test_unfunded_and_passed_date(self):
        hints = suggest_signals(
            {"funded": False, "close_date": "2020-01-01"},
            today=date(2026, 6, 17),
        )
        assert "UNFUNDED" in hints["resourcing"]
        assert "PASSED" in hints["availability"]

    def test_funded_and_open(self):
        hints = suggest_signals(
            {"funded": True, "close_date": "2027-12-31", "team_leader": "Dr X"},
            today=date(2026, 6, 17),
        )
        assert "FUNDED" in hints["resourcing"]
        assert "Dr X" in hints["resourcing"]
        assert "open until" in hints["availability"]
