CREATE OR REPLACE VIEW analytics.v_market_overview AS

SELECT

    COUNT(*) AS total_games,

    SUM(ccu) AS total_ccu,

    AVG(review_score) AS avg_review_score,

    SUM(owners_estimated) AS total_estimated_owners

FROM analytics.v_game_performance;