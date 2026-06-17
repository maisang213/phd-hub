"""Fetcher for RMIT Vietnam PhD research projects."""

import json
import logging
import re
from dataclasses import asdict, dataclass
from typing import Optional
import requests

logger = logging.getLogger(__name__)

API_URL = "https://hdrprojects.its.rmit.edu.au/project-list-vietnam/gApi/index.php?sheet_name=Data"
SOURCE_KEY = "rmit_vn"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; rmit-phd-projects/1.0)",
    "Referer": "https://www.rmit.edu.au/research/research-degrees/find-a-project-vn",
}

# The response contains multiple JSONP calls; we only need initializeData(...)
_INIT_CALL_RE = re.compile(r"initializeData\(")


@dataclass
class Project:
    title: str
    description: str
    college: str
    school: str
    discipline: str
    program_code: str
    campus: str
    team_leader: str
    sdg: list[str]           # Sustainable Development Goals, e.g. ["2","3","11"]
    funded: Optional[bool]   # True / False / None (not specified)
    close_date: Optional[str]  # ISO date string or None
    ecp: list[str]           # Research platforms
    for_codes: list[str]     # Field of Research codes
    source: str = SOURCE_KEY

    def to_dict(self) -> dict:
        return asdict(self)


def _parse_sdg(raw: str) -> list[str]:
    return [s.strip() for s in raw.split(",") if s.strip()] if raw else []


def _parse_list(raw: str, sep: str = ",") -> list[str]:
    return [s.strip() for s in raw.split(sep) if s.strip()] if raw else []


def _parse_funded(raw: str) -> Optional[bool]:
    if raw.strip().lower() == "yes":
        return True
    if raw.strip().lower() == "no":
        return False
    return None


def _row_to_project(row: dict) -> Project:
    return Project(
        title=row.get("title", "").strip(),
        description=row.get("description", "").strip(),
        college=row.get("college", "").strip(),
        school=row.get("school", "").strip(),
        discipline=row.get("discipline", "").strip(),
        program_code=row.get("programcode", "").strip(),
        campus=row.get("campus", "").strip(),
        team_leader=row.get("teamleader", "").strip(),
        sdg=_parse_sdg(row.get("sdg", "")),
        funded=_parse_funded(row.get("funded", "")),
        close_date=row.get("closedate", "").strip() or None,
        ecp=_parse_list(row.get("ecp", "")),
        for_codes=_parse_list(row.get("forcodes", ""), sep="\n"),
    )


def _extract_initialize_data(text: str) -> dict:
    """Extract the JSON payload from the first initializeData(...) call.

    The response may contain several chained JSONP calls; raw_decode stops at
    the first balanced closing brace so we never accidentally span into a
    second call.
    """
    match = _INIT_CALL_RE.search(text)
    if not match:
        raise ValueError("Unexpected response format — initializeData() call not found")
    json_start = match.end()   # position right after the opening "("
    data, _ = json.JSONDecoder().raw_decode(text, json_start)
    return data


def fetch() -> list[Project]:
    """Fetch all PhD research projects from RMIT Vietnam."""
    logger.info("Fetching from %s", API_URL)
    resp = requests.get(API_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    data = _extract_initialize_data(resp.text)
    if data.get("status") != 1:
        raise ValueError(f"API returned non-OK status: {data.get('status')}")

    rows = data.get("result", [])
    projects = [_row_to_project(r) for r in rows]
    logger.info("Fetched %d projects", len(projects))
    return projects
