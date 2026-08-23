-- Write your query below
WITH user_balance AS (
    SELECT u.name, SUM(tr.amount) AS balance
    FROM transactions AS tr
    INNER JOIN users AS u ON u.account = tr.account
    GROUP BY tr.account, u.name
)

SELECT name, balance
FROM user_balance
WHERE balance > 10000;