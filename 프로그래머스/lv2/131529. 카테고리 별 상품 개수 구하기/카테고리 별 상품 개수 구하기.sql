-- 코드를 입력하세요
SELECT category, count(product_id) AS products
FROM ( SELECT product_id, SUBSTR(product_code,1, 2) AS category, price
       FROM product
     )
GROUP BY category
ORDER BY category;
