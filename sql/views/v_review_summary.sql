CREATE OR REPLACE VIEW analytics.v_review_summary AS

SELECT
    d.app_id,

    d.game_name,

    f.positive_reviews,

    f.negative_reviews,

    f.review_score,

    CASE

        WHEN f.review_score >= 90
            THEN 'Overwhelmingly Positive'

        WHEN f.review_score >= 80
            THEN 'Very Positive'

        WHEN f.review_score >= 70
            THEN 'Positive'

        WHEN f.review_score >= 50
            THEN 'Mixed'

        ELSE 'Negative'

    END AS review_category

FROM warehouse.fact_game_snapshot f

JOIN warehouse.dim_game d
ON f.game_key = d.game_key;