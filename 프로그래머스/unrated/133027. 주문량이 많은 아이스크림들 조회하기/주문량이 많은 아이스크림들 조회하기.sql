-- 1. 서브절 + JOIN 서브절
-- SELECT flavor
-- FROM ( SELECT f.flavor, 
--            f.total_order + j.total_order AS total_order
--        FROM first_half f
--        JOIN ( SELECT flavor, SUM(total_order) AS total_order
--               FROM july
--               GROUP BY flavor
--             ) j
--            ON f.flavor = j.flavor 
--        ORDER BY total_order DESC
--      )
-- WHERE ROWNUM <= 3;


-- 2. 서브절(JOIN)
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
