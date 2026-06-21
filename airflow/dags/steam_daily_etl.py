from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "steam_dw",
    "depends_on_past": False,
}


with DAG(
    dag_id="steam_daily_etl",
    default_args=default_args,
    start_date=datetime(2026, 6, 19),
    schedule="0 1 * * *",
    catchup=False,
    tags=["steam", "etl", "warehouse"],
) as dag:

    run_daily_etl = BashOperator(
        task_id="run_daily_etl",
        bash_command="""
        cd /opt/project &&
        python -m src.jobs.daily_etl
        """
    )

    run_daily_etl