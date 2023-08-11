-- 코드를 입력하세요
SELECT animal_type, count(animal_id) AS count
FROM animal_ins
GROUP BY animal_type
ORDER BY animal_type;