#!/usr/bin/env python3
"""CLI to fetch and snapshot RMIT PhD research projects."""

import argparse
import json
import logging
import sys
from datetime import date
from pathlib import Path

from rmit_projects.fetchers import rmit_vn

DATA_DIR = Path(__file__).parent / "data"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch RMIT PhD project listings")
    parser.add_argument(
        "--source",
        choices=["rmit_vn"],
        default="rmit_vn",
        help="Data source to fetch (default: rmit_vn)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output file path (default: data/<source>_<date>.json)",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output",
    )
    args = parser.parse_args()

    fetchers = {"rmit_vn": rmit_vn.fetch}
    projects = fetchers[args.source]()

    output_path = args.output or DATA_DIR / f"{args.source}_{date.today()}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    indent = 2 if args.pretty else None
    payload = [p.to_dict() for p in projects]
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=indent))

    print(f"Saved {len(projects)} projects → {output_path}")


if __name__ == "__main__":
    main()
