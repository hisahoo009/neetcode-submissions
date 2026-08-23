-- Write your query below
WITH pages_liked AS (
    SELECT page_id
    FROM likes
    WHERE user_id = 1
), friend1 AS (
    SELECT user1_id
    FROM friendship
    WHERE user2_id = 1
), friend2 AS (
    SELECT user2_id
    FROM friendship
    WHERE user1_id = 1
)

SELECT DISTINCT(page_id) AS recommended_page
FROM likes
WHERE (user_id IN (SELECT * FROM friend1) OR user_id IN (SELECT * FROM friend2)) AND (page_id NOT IN (SELECT * FROM pages_liked))
