"""
SteamSpy Extractor

Purpose:
    Extract multiple pages from SteamSpy API
    and save raw JSON files locally.
"""

from pathlib import Path
import json
import logging
import time

import requests


STEAMSPY_URL = "https://steamspy.com/api.php"

MAX_PAGE = 30


def fetch_all_games_page(page: int) -> dict:
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

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = (
        output_dir /
        f"steamspy_page_{page}.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2,
        )

    return output_file


def main() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    total_games = 0

    for page in range(MAX_PAGE):

        logging.info(
            "Fetching SteamSpy page %s",
            page,
        )

        data = fetch_all_games_page(page)

        games_count = len(data)

        total_games += games_count

        output_file = save_raw_json(
            data,
            page,
        )

        logging.info(
            "Page %s -> %s games",
            page,
            games_count,
        )

        logging.info(
            "Saved file: %s",
            output_file,
        )

        time.sleep(1)

    logging.info(
        "TOTAL GAMES COLLECTED: %s",
        total_games,
    )


if __name__ == "__main__":
    main()