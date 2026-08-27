-- Write your query below

WITH team_count AS (
    SELECT team_id, COUNT(employee_id) AS team_size
    FROM employee
    GROUP BY team_id
)

SELECT employee_id, team_size
FROM employee
LEFT JOIN team_count ON team_count.team_id = employee.team_id;