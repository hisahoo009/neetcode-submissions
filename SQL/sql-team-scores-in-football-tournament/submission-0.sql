-- Write your query below
-- CREATE NEW COLUMN win_lose: host_goals - guest_goals
-- CREATE TWO NEW COLUMNS host_points, guest_points

WITH points AS (
    SELECT match_id, 
            host_team, 
            guest_team,
            CASE
                WHEN host_goals > guest_goals THEN 3
                WHEN host_goals = guest_goals THEN 1
                WHEN host_goals < guest_goals THEN 0
            END AS host_points,
            CASE
                WHEN host_goals < guest_goals THEN 3
                WHEN host_goals = guest_goals THEN 1
                WHEN host_goals > guest_goals THEN 0
            END AS guest_points
    FROM matches
),

host_points AS (
    SELECT teams.team_id, teams.team_name, SUM(COALESCE(p.host_points, 0)) AS total_score_host
    FROM points AS p
    FULL OUTER JOIN teams ON p.host_team = teams.team_id
    GROUP BY teams.team_id, teams.team_name
),

guest_points AS (
    SELECT teams.team_id, teams.team_name, SUM(COALESCE(p.guest_points, 0)) AS total_score_guest
    FROM points AS p
    FULL OUTER JOIN teams ON p.guest_team = teams.team_id
    GROUP BY teams.team_id, teams.team_name
)

SELECT hp.team_id, hp.team_name, (COALESCE(hp.total_score_host, 0) + COALESCE(gp.total_score_guest, 0)) AS num_points
FROM host_points AS hp
FULL OUTER JOIN guest_points AS gp ON hp.team_id = gp.team_id
ORDER BY num_points DESC, team_id ASC;
        