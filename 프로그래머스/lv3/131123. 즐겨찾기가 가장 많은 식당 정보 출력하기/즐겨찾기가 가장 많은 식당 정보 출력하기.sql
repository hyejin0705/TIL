-- 코드를 입력하세요
SELECT I2.food_type, 
    I2.rest_id, 
    I2.rest_name, 
    I2.favorites
FROM ( SELECT food_type, MAX(favorites) AS favorites
       FROM rest_info
       GROUP BY food_type
     ) I1
INNER JOIN rest_info I2
    ON I1.food_type = I2.food_type 
    AND I1.favorites = I2.favorites
ORDER BY food_type DESC;