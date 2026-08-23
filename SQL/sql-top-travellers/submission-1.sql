-- Write your query below
SELECT users.name, COALESCE(SUM(rides.distance), 0) AS travelled_distance
FROM rides
RIGHT JOIN users ON users.id = rides.user_id
GROUP BY rides.user_id, users.name
ORDER BY travelled_distance DESC, name ASC;