"""
SteamSpy Extractor V1

Purpose:
    Extract raw data from SteamSpy API.
"""

from pathlib import Path
import json
import logging

import requests


STEAMSPY_URL = "https://steamspy.com/api.php"


def fetch_all_games_page(page: int = 0) -> dict:
    """
    Fetch one page from SteamSpy.

    Args:
        page: page number

    Returns:
        dict
    """

    response = requests.get(
        STEAMSPY_URL,
        params={
            "request": "all",
            "page": page,
        },
        timeout=60,
    )

    response.raise_for_status()

    return response.json()


def save_raw_json(data: dict, page: int) -> Path:
    """
    Save raw JSON locally.
    """

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"steamspy_page_{page}.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2,
        )

    return output_file


def main() -> None:

    logging.basicConfig(level=logging.INFO)

    page = 0

    logging.info("Fetching SteamSpy page %s", page)

    data = fetch_all_games_page(page)

    logging.info("Games returned: %s", len(data))

    output_file = save_raw_json(data, page)

    logging.info("Saved file: %s", output_file)


if __name__ == "__main__":
    main()