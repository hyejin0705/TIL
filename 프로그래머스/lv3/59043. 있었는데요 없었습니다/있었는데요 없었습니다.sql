-- 코드를 입력하세요
SELECT i.animal_id, i.name
FROM animal_ins i
LEFT JOIN animal_outs o
    ON i.animal_id = o.animal_id
WHERE o.datetime - i.datetime < 0
ORDER BY i.datetime;