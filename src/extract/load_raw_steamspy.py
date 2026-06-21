"""
Load SteamSpy raw JSON into PostgreSQL Raw Layer
"""

import json
import logging
from pathlib import Path

from psycopg2.extras import Json

from src.common.db import get_connection


INPUT_FILE = Path("data/raw/steamspy_page_0.json")


def load_json() -> dict:
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
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

    data = load_json()

    inserted = insert_raw_games(data)

    logging.info("Inserted rows: %s", inserted)


if __name__ == "__main__":
    main()