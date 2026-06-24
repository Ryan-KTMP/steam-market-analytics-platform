"""
Load SteamSpy raw JSON into PostgreSQL Raw Layer
"""

import json
import logging
from pathlib import Path

from psycopg2.extras import Json

from src.common.db import get_connection


RAW_FOLDER = Path("data/raw")


def get_json_files():

    return sorted(
        RAW_FOLDER.glob(
            "steamspy_page_*.json"
        )
    )


def load_json(file_path: Path) -> dict:

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def insert_raw_games(data: dict) -> int:

    conn = get_connection()

    cursor = conn.cursor()

    inserted = 0

    try:

        for app_id, payload in data.items():

            cursor.execute(
                """
                INSERT INTO raw.raw_steamspy_games
                (
                    source_name,
                    app_id,
                    raw_payload
                )
                VALUES
                (
                    %s,
                    %s,
                    %s
                );
                """,
                (
                    "steamspy",
                    int(app_id),
                    Json(payload),
                ),
            )

            inserted += 1

        conn.commit()

        return inserted

    except Exception:

        conn.rollback()

        raise

    finally:

        cursor.close()

        conn.close()


def main() -> None:

    logging.basicConfig(level=logging.INFO)

    total_inserted = 0

    json_files = get_json_files()

    logging.info(
        "Files found: %s",
        len(json_files)
    )

    for file_path in json_files:

        logging.info(
            "Processing %s",
            file_path.name
        )

        data = load_json(file_path)

        inserted = insert_raw_games(data)

        total_inserted += inserted

    logging.info(
        "TOTAL INSERTED: %s",
        total_inserted
    )


if __name__ == "__main__":
    main()