-- 코드를 입력하세요
SELECT animal_id, name, TO_CHAR(datetime, 'YYYY-MM-DD') AS 날짜
FROM animal_ins
ORDER BY animal_id