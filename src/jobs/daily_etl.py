import logging

from src.extract import steamspy_extractor
from src.extract import load_raw_steamspy

from src.staging.staging_loader import (
    load_to_staging
)

from src.warehouse.load_dim_game import (
    load_dim_game
)

from src.warehouse.load_fact_game_snapshot import (
    load_fact_game_snapshot
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_daily_etl():

    logging.info(
        "STEP 1 - Extract SteamSpy data"
    )

    steamspy_extractor.main()

    logging.info(
        "STEP 2 - Load Raw Layer"
    )

    load_raw_steamspy.main()

    logging.info(
        "STEP 3 - Load Staging Layer"
    )

    load_to_staging()

    logging.info(
        "STEP 4 - Load Dim Game"
    )

    load_dim_game()

    logging.info(
        "STEP 5 - Load Fact Snapshot"
    )

    load_fact_game_snapshot()

    logging.info(
        "DAILY ETL COMPLETED"
    )


if __name__ == "__main__":
    run_daily_etl()