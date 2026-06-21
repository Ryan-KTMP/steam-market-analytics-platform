from src.common.db import get_connection


def run_data_quality_checks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO audit.data_quality_issues
        (
            app_id,
            issue_type,
            issue_description
        )
        SELECT
            app_id,
            'MISSING_GAME_NAME',
            'Game name is NULL'
        FROM staging.stg_steam_games
        WHERE game_name IS NULL;
        """
    )

    cursor.execute(
        """
        INSERT INTO audit.data_quality_issues
        (
            app_id,
            issue_type,
            issue_description
        )
        SELECT
            app_id,
            'INVALID_OWNER_RANGE',
            'owners_min > owners_max'
        FROM staging.stg_steam_games
        WHERE owners_min > owners_max;
        """
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("Data quality check completed")


if __name__ == "__main__":
    run_data_quality_checks()