-- 풀이 1
-- SELECT warehouse_id, warehouse_name, address, 
--     CASE 
--         WHEN freezer_yn IS NULL THEN 'N' 
--         ELSE freezer_yn
--     END AS freezer_yn
-- FROM food_warehouse
-- WHERE address LIKE '경기도%'
-- ORDER BY warehouse_id;


-- 풀이 2
SELECT warehouse_id, warehouse_name, address, 
    NVL(freezer_yn, 'N') as freezer_yn
    -- NVL 함수는 값이 NULL인 경우 지정값을 출력하고, NULL이 아니면 원래 값을 그대로 출력한다.
    -- 함수  :  NVL("값", "지정값") 
FROM food_warehouse
WHERE address LIKE '경기도%'
ORDER BY warehouse_id;