-- 코드를 입력하세요
SELECT price AS price_group, count(*) AS products
FROM ( SELECT product_id, product_code, 
            TRUNC(price, -4) AS price
       FROM product
     )
GROUP BY price
ORDER BY price;