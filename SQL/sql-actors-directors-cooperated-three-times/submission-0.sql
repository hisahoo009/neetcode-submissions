-- Write your query below

-- GROUP BY actor_id, director_id
-- COUNT (*)
-- COUNT (*) >= 3

WITH actor_director_total AS (
    SELECT actor_id, director_id, COUNT(timestamp) AS total_collab
    FROM actor_director
    GROUP BY actor_id, director_id
)

SELECT actor_id, director_id
FROM actor_director_total
WHERE total_collab >= 3;