CREATE OR REPLACE VIEW analytics.v_game_performance AS

SELECT
    f.date_key,
    d.app_id,
    d.game_name,

    f.owners_min,
    f.owners_max,
    f.owners_estimated,

    f.positive_reviews,
    f.negative_reviews,
    f.review_score,

    f.ccu

FROM warehouse.fact_game_snapshot f

JOIN warehouse.dim_game d
ON f.game_key = d.game_key;