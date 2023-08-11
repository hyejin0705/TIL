-- 코드를 입력하세요
SELECT product_id, product_name, product_cd, category, price
FROM ( SELECT *
       FROM food_product
       ORDER BY price DESC
)
WHERE ROWNUM = 1;