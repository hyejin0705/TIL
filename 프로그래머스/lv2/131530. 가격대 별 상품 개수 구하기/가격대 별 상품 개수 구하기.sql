-- 1.
-- SELECT price AS price_group, count(*) AS products
-- FROM ( SELECT product_id, product_code, 
--             TRUNC(price, -4) AS price
--        FROM product
--      )
-- GROUP BY price
-- ORDER BY price;

-- 2.
SELECT TRUNC(price, -4) AS price_group, 
    count(product_id) AS products
FROM product
GROUP BY TRUNC(price, -4)
ORDER BY price_group;