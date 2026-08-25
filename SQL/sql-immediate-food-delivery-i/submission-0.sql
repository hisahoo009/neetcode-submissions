-- Write your query below

SELECT ROUND((SUM((order_date = customer_pref_delivery_date)::INT) * 100.00) / COUNT(delivery_id), 2) AS immediate_percentage
FROM delivery;