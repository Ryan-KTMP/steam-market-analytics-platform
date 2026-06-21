CREATE OR REPLACE VIEW analytics.v_top_games AS

SELECT
    d.app_id,
    d.game_name,

    f.ccu,

    f.owners_estimated,

    f.review_score,

    DENSE_RANK()
    OVER
    (
        ORDER BY f.ccu DESC
    ) AS ccu_rank

FROM warehouse.fact_game_snapshot f

JOIN warehouse.dim_game d
ON f.game_key = d.game_key;