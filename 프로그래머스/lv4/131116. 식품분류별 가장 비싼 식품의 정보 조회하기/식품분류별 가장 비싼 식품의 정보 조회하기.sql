-- 1.
-- SELECT category, price AS max_price, product_name
-- FROM food_product
-- WHERE price IN ( SELECT MAX(price) AS max_price
--                  FROM food_product
--                  WHERE category IN ('과자', '국', '김치', '식용유')
--                  GROUP BY category
--                )
--     AND category IN ('과자', '국', '김치', '식용유')
-- ORDER BY max_price DESC;

-- 2. Join 활용
SELECT a.category, a.price AS max_price, a.product_name
FROM food_product a
JOIN ( SELECT category, MAX(price) AS max_price
       FROM food_product
       WHERE category IN ('과자', '국', '김치', '식용유')
       GROUP BY category 
     ) b
ON a.category = b.category 
    AND a.price = b.max_price
ORDER BY max_price DESC;