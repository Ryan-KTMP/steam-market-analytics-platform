from datetime import date, timedelta

from src.common.db import get_connection


def load_dim_date():

    conn = get_connection()
    cursor = conn.cursor()

    start_date = date(2025, 1, 1)
    end_date = date(2030, 12, 31)

    current_date = start_date

    inserted = 0

    while current_date <= end_date:

        date_key = int(
            current_date.strftime("%Y%m%d")
        )

        cursor.execute(
            """
            INSERT INTO warehouse.dim_date
            (
                date_key,
                full_date,
                day_of_month,
                month_number,
                month_name,
                quarter_number,
                year_number,
                week_of_year,
                day_name,
                is_weekend
            )
            VALUES
            (
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
            )
            ON CONFLICT (date_key)
            DO NOTHING
            """,
            (
                date_key,
                current_date,
                current_date.day,
                current_date.month,
                current_date.strftime("%B"),
                (current_date.month - 1) // 3 + 1,
                current_date.year,
                current_date.isocalendar()[1],
                current_date.strftime("%A"),
                current_date.weekday() >= 5,
            ),
        )

        inserted += 1

        current_date += timedelta(days=1)

    conn.commit()

    cursor.close()
    conn.close()

    print(
        f"Inserted dates: {inserted}"
    )


if __name__ == "__main__":
    load_dim_date()