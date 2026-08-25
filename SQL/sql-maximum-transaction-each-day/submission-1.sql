-- Write your query below
WITH RankedTable AS (
    SELECT transaction_id,
            day::DATE AS transaction_date,
            amount,
            RANK() OVER (
                PARTITION BY day::DATE
                ORDER BY amount DESC
            ) AS rnk
    FROM transactions
)

SELECT transaction_id
FROM RankedTable
WHERE rnk = 1
ORDER BY transaction_id ASC;