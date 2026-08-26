-- Write your query below

WITH new_orders AS (
    SELECT ord.order_id, ord.customer_id, ord.product_id, ord.order_date, ord.quantity, prod.price AS unit_price
    FROM orders AS ord
    LEFT JOIN product AS prod ON prod.product_id = ord.product_id
),

order_total AS (
    SELECT new_ord.customer_id,
            cust.name,  
            SUM(new_ord.unit_price * new_ord.quantity) AS monthly_total, 
            EXTRACT(YEAR FROM new_ord.order_date::DATE) AS order_year, 
            EXTRACT(MONTH FROM new_ord.order_date::DATE) as order_month
    FROM new_orders AS new_ord
    LEFT JOIN customers AS cust ON cust.customer_id = new_ord.customer_id
    --WHERE order_year = 2020 AND order_month IN (6, 7)
    GROUP BY new_ord.customer_id, cust.name, order_year, order_month
)

SELECT DISTINCT(customer_id), name
FROM order_total
WHERE customer_id IN (
    SELECT customer_id
    FROM order_total
    WHERE monthly_total >= 100 AND order_year = 2020 AND order_month = 6
    ) AND customer_id IN (
       SELECT customer_id
       FROM order_total
       WHERE monthly_total >= 100 AND order_year = 2020 AND order_month = 7
    );