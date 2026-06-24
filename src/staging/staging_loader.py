from src.common.db import get_connection


def parse_owners(owners_text):

    if not owners_text:
        return None, None

    parts = owners_text.split("..")

    if len(parts) != 2:
        return None, None

    try:

        owners_min = int(
            parts[0]
            .replace(",", "")
            .strip()
        )

        owners_max = int(
            parts[1]
            .replace(",", "")
            .strip()
        )

        return owners_min, owners_max

    except ValueError:
        return None, None


def calculate_review_score(positive, negative):

    total = positive + negative

    if total == 0:
        return 0

    return round((positive / total) * 100, 2)


def load_to_staging():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            app_id,
            raw_payload
        FROM raw.raw_steamspy_games
        """
    )

    rows = cursor.fetchall()

    inserted = 0

    for app_id, payload in rows:

        game_name = payload.get("name")

        owners_min, owners_max = parse_owners(
            payload.get("owners")
        )

        positive = payload.get("positive", 0)
        negative = payload.get("negative", 0)

        review_total = positive + negative

        review_score_pct = calculate_review_score(
            positive,
            negative
        )

        # CCU (Concurrent Current Users)
        ccu_raw = payload.get("ccu", 0)

        try:
            ccu = int(ccu_raw)
        except (ValueError, TypeError):
            ccu = 0

        # Price
        price_raw = payload.get("price", 0)

        try:
            price = float(price_raw) / 100
        except (ValueError, TypeError):
            price = 0

        cursor.execute(
            """
            INSERT INTO staging.stg_steam_games
            (
                app_id,
                game_name,
                owners_min,
                owners_max,
                positive_reviews,
                negative_reviews,
                review_total,
                review_score_pct,
                price,
                ccu
            )
            VALUES
            (
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
            )
            ON CONFLICT (app_id)
            DO UPDATE;
            """,
            (
                app_id,
                game_name,
                owners_min,
                owners_max,
                positive,
                negative,
                review_total,
                review_score_pct,
                price,
                ccu,
            )
        )

        inserted += 1

    conn.commit()

    cursor.close()
    conn.close()

    print(
        f"Inserted into staging: {inserted}"
    )


if __name__ == "__main__":
    load_to_staging()