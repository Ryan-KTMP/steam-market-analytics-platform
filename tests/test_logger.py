from datetime import datetime

from src.monitoring.etl_logger import log_etl_job


log_etl_job(
    job_name="test_job",
    start_time=datetime.now(),
    end_time=datetime.now(),
    status="SUCCESS",
    rows_processed=123
)

print("Logger test success")