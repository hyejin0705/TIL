-- 코드를 입력하세요
SELECT p.product_id, p.product_name, 
    SUM(o.amount * p.price) AS total_sales
FROM food_order o
JOIN food_product p
    ON o.product_id = p.product_id
WHERE TO_CHAR(o.produce_date, 'YYYY-MM') = '2022-05'
GROUP BY p.product_id, p.product_name
ORDER BY total_sales DESC, product_id;