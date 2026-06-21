from src.common.db import get_connection


def log_etl_job(
    job_name,
    start_time,
    end_time,
    status,
    rows_processed=0,
    error_message=None
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO audit.etl_job_log
        (
            job_name,
            start_time,
            end_time,
            status,
            rows_processed,
            error_message
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s
        )
        """,
        (
            job_name,
            start_time,
            end_time,
            status,
            rows_processed,
            error_message
        )
    )

    conn.commit()

    cursor.close()
    conn.close()