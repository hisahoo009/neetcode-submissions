-- Write your query below
WITH ALL_WINS AS (
    SELECT wimbledon AS player_id FROM championships
    UNION ALL
    SELECT fr_open AS player_id FROM championships
    UNION ALL
    SELECT us_open AS player_id FROM championships
    UNION ALL
    SELECT au_open AS player_id FROM championships  
)

SELECT pl.player_id, 
    pl.player_name, 
    COUNT(*) AS grand_slams_count
FROM ALL_WINS AS a
INNER JOIN players AS pl ON pl.player_id = a.player_id
GROUP BY pl.player_id, pl.player_name
ORDER BY pl.player_id DESC;

