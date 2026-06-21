from src.common.db import get_connection


def load_dim_game():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO warehouse.dim_game
        (
            app_id,
            game_name,
            effective_date,
            is_current
        )
        SELECT
            s.app_id,
            s.game_name,
            CURRENT_DATE,
            TRUE
        FROM staging.stg_steam_games s
        WHERE NOT EXISTS
        (
            SELECT 1
            FROM warehouse.dim_game d
            WHERE d.app_id = s.app_id
            AND d.is_current = TRUE
        );
        """
    )

    inserted = cursor.rowcount

    conn.commit()

    cursor.close()
    conn.close()

    print(
        f"Inserted games: {inserted}"
    )


if __name__ == "__main__":
    load_dim_game()