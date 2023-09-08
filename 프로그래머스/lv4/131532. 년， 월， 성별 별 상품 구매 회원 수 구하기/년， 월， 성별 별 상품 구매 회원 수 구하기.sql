-- 코드를 입력하세요
SELECT TO_CHAR(o.sales_date, 'YYYY') AS year, 
    TO_NUMBER(TO_CHAR(o.sales_date, 'MM')) AS month, 
    u.gender, 
    COUNT(DISTINCT o.user_id) AS users
FROM online_sale o
LEFT JOIN user_info u
    ON u.user_id = o.user_id
WHERE u.gender IS NOT NULL
GROUP BY TO_CHAR(o.sales_date, 'YYYY'), 
    TO_CHAR(o.sales_date, 'MM'),
    u.gender
ORDER BY year, month, gender;