-- 코드를 입력하세요
SELECT i.ingredient_type, SUM(f.total_order) AS total_order
FROM first_half f
LEFT OUTER JOIN icecream_info i 
    ON f.flavor = i.flavor
GROUP BY i.ingredient_type;