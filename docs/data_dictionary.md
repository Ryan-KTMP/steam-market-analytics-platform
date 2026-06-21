# Data Dictionary

## warehouse.dim_game

| Column | Description |
|----------|----------|
| game_key | Surrogate key |
| app_id | Steam application ID |
| game_name | Game title |
| release_date | Release date |
| is_free | Free-to-play flag |
| metacritic_score | Metacritic score |
| product_type | Game type |
| effective_date | SCD2 start date |
| expiry_date | SCD2 end date |
| is_current | Current version indicator |

## warehouse.fact_game_snapshot

| Column | Description |
|----------|----------|
| snapshot_id | Snapshot key |
| date_key | Date dimension key |
| game_key | Game dimension key |
| positive_reviews | Positive reviews |
| negative_reviews | Negative reviews |
| review_score | Review percentage |
| ccu | Concurrent users |
| owners_min | Minimum owner estimate |
| owners_max | Maximum owner estimate |
| owners_estimated | Midpoint estimate |