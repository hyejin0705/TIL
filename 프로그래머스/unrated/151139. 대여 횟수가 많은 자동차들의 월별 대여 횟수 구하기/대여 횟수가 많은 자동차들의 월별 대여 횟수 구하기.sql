-- 코드를 입력하세요
SELECT TO_NUMBER(TO_CHAR(start_date, 'MM')) AS month, 
    car_id, 
    COUNT(history_id) AS records
FROM car_rental_company_rental_history
WHERE car_id IN ( SELECT car_id
                  FROM car_rental_company_rental_history
                  WHERE start_date BETWEEN TO_DATE('2022-08-01', 'YYYY-MM-DD') and TO_DATE('2022-10-31', 'YYYY-MM-DD')
                  GROUP BY car_id
                  HAVING count(history_id) >= 5
                 )
    AND start_date BETWEEN TO_DATE('2022-08-01', 'YYYY-MM-DD') and TO_DATE('2022-10-31', 'YYYY-MM-DD')
GROUP BY TO_NUMBER(TO_CHAR(start_date, 'MM')), car_id
ORDER BY month, car_id DESC;