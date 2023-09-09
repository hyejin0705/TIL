-- 코드를 입력하세요
SELECT flavor
FROM ( SELECT f.flavor, 
           SUM(f.total_order + j.total_order) AS total
       FROM first_half f
       JOIN july j
           ON f.flavor = j.flavor
       GROUP BY f.flavor
       ORDER BY total DESC
     )
WHERE ROWNUM <= 3;
