-- Write your query below
SELECT sales_apple.sale_date, apples - oranges AS diff
FROM (
    SELECT sale_date, sold_num AS apples
    FROM sales
    WHERE fruit = 'apples'
) AS sales_apple
INNER JOIN
(
    SELECT sale_date, sold_num AS oranges
    FROM sales
    WHERE fruit = 'oranges'
) AS sales_orange
ON sales_apple.sale_date = sales_orange.sale_date