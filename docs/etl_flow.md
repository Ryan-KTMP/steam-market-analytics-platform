# ETL Flow

## Extract

steamspy_extractor.py

Downloads SteamSpy data and stores JSON files.

## Raw Load

load_raw_steamspy.py

Loads JSON into raw.raw_steamspy_games.

## Staging

staging_loader.py

Cleans and standardizes source data.

## Warehouse

load_dim_date.py

load_dim_game.py

load_fact_game_snapshot.py

Loads warehouse tables.

## Validation

data_quality_check.py

Runs quality rules.

## Monitoring

etl_logger.py

Logs ETL executions.