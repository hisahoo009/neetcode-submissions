-- Write your query below
SELECT warehouse.name AS warehouse_name, SUM(units * width * length * height) AS volume
FROM warehouse
LEFT JOIN products ON warehouse.product_id = products.product_id
GROUP BY warehouse.name