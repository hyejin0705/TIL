-- 대여 시작일과 종료일 사이에, 
-- 2022년 10월 16일이 존재하면, 1  존재하지 않으면, 0
-- 총합이 0이라면, 대여가능, 1이라면, 대여중?
SELECT car_id, 
    CASE WHEN availability = 0 THEN '대여 가능'
    ELSE '대여중' 
    END AS availability
FROM ( SELECT car_id,
            SUM(CASE WHEN TO_DATE('2022-10-16', 'YYYY-MM-DD') BETWEEN start_date AND end_date THEN 1 ELSE 0 END) AS availability
       FROM car_rental_company_rental_history
       GROUP BY car_id
     )
ORDER BY car_id DESC;