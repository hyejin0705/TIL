-- 코드를 입력하세요
SELECT SUBSTR(product_code,1, 2) AS category, 
    count(product_id) AS products
FROM product
GROUP BY SUBSTR(product_code,1, 2)
ORDER BY category;