from src.common.db import get_connection


def load_fact_game_snapshot():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO warehouse.fact_game_snapshot
        (
            date_key,
            game_key,
            owners_min,
            owners_max,
            owners_estimated,
            positive_reviews,
            negative_reviews,
            review_score,
            ccu
        )
        SELECT
            CAST(TO_CHAR(CURRENT_DATE, 'YYYYMMDD') AS INTEGER),
            d.game_key,
            s.owners_min,
            s.owners_max,
            ((s.owners_min + s.owners_max) / 2),
            s.positive_reviews,
            s.negative_reviews,
            s.review_score_pct,
            s.ccu
        FROM staging.stg_steam_games s
        INNER JOIN warehouse.dim_game d
            ON d.app_id = s.app_id
        WHERE d.is_current = TRUE
        ON CONFLICT (date_key, game_key)
        DO NOTHING;
        """
    )

    inserted = cursor.rowcount

    conn.commit()

    cursor.close()
    conn.close()

    print(
        f"Inserted snapshots: {inserted}"
    )


if __name__ == "__main__":
    load_fact_game_snapshot()