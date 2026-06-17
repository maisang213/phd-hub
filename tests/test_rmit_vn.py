"""Tests for the RMIT Vietnam fetcher."""

import json
import pytest
from unittest.mock import patch, MagicMock
from rmit_projects.fetchers.rmit_vn import (
    fetch,
    _parse_sdg,
    _parse_funded,
    _row_to_project,
    _extract_initialize_data,
)

SAMPLE_ROW = {
    "title": "AI in Healthcare",
    "description": "Research on AI applications.",
    "college": "STEM",
    "school": "Computing Technologies",
    "discipline": "Artificial Intelligence",
    "programcode": "DR221",
    "campus": "RMIT Vietnam",
    "teamleader": "Dr. Jane Smith",
    "sdg": "3,9,17",
    "funded": "Yes",
    "closedate": "2026-08-31",
    "ecp": "Information in Society, STEM",
    "forcodes": "461103 Deep learning (50%)\n461106 Semi-supervised learning (50%)",
}

SAMPLE_PAYLOAD = json.dumps({"status": 1, "result": [SAMPLE_ROW]})
SAMPLE_RESPONSE = f"initializeData({SAMPLE_PAYLOAD});"
# Simulate the real response which has a second JSONP call after the first
MULTI_CALL_RESPONSE = f"initializeData({SAMPLE_PAYLOAD}); showSheetData({SAMPLE_PAYLOAD});"


class TestParsers:
    def test_parse_sdg(self):
        assert _parse_sdg("3,9,17") == ["3", "9", "17"]
        assert _parse_sdg("") == []
        assert _parse_sdg(" 2, 11 ") == ["2", "11"]

    def test_parse_funded(self):
        from rmit_projects.fetchers.rmit_vn import _parse_funded
        assert _parse_funded("Yes") is True
        assert _parse_funded("No") is False
        assert _parse_funded("") is None
        assert _parse_funded("yes") is True

    def test_row_to_project(self):
        p = _row_to_project(SAMPLE_ROW)
        assert p.title == "AI in Healthcare"
        assert p.funded is True
        assert p.sdg == ["3", "9", "17"]
        assert p.close_date == "2026-08-31"
        assert len(p.for_codes) == 2
        assert p.source == "rmit_vn"


class TestExtractInitializeData:
    def test_single_call(self):
        data = _extract_initialize_data(SAMPLE_RESPONSE)
        assert data["status"] == 1
        assert len(data["result"]) == 1

    def test_multi_call_only_reads_first(self):
        data = _extract_initialize_data(MULTI_CALL_RESPONSE)
        assert data["status"] == 1
        assert len(data["result"]) == 1  # not doubled

    def test_raises_when_call_missing(self):
        with pytest.raises(ValueError, match="initializeData"):
            _extract_initialize_data('{"status": 1, "result": []}')


class TestFetch:
    def test_fetch_parses_jsonp(self):
        mock_resp = MagicMock()
        mock_resp.text = SAMPLE_RESPONSE
        mock_resp.raise_for_status = MagicMock()

        with patch("requests.get", return_value=mock_resp):
            projects = fetch()

        assert len(projects) == 1
        assert projects[0].title == "AI in Healthcare"

    def test_fetch_handles_multi_call_response(self):
        mock_resp = MagicMock()
        mock_resp.text = MULTI_CALL_RESPONSE
        mock_resp.raise_for_status = MagicMock()

        with patch("requests.get", return_value=mock_resp):
            projects = fetch()

        assert len(projects) == 1  # not doubled

    def test_fetch_raises_on_bad_status(self):
        mock_resp = MagicMock()
        mock_resp.text = f"initializeData({json.dumps({'status': 0, 'result': []})});"
        mock_resp.raise_for_status = MagicMock()

        with patch("requests.get", return_value=mock_resp):
            with pytest.raises(ValueError, match="non-OK status"):
                fetch()

    def test_fetch_raises_on_missing_jsonp_wrapper(self):
        mock_resp = MagicMock()
        mock_resp.text = '{"status": 1, "result": []}'
        mock_resp.raise_for_status = MagicMock()

        with patch("requests.get", return_value=mock_resp):
            with pytest.raises(ValueError, match="initializeData"):
                fetch()
