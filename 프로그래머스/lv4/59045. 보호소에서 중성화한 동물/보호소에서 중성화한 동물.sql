-- 코드를 입력하세요
SELECT o.animal_id, o.animal_type, o.name
FROM animal_outs o
LEFT JOIN animal_ins i
ON o.animal_id = i.animal_id
WHERE SUBSTR(i.sex_upon_intake, 0, 6) = 'Intact'
    AND SUBSTR(o.sex_upon_outcome, 0, 6) IN ('Spayed', 'Neuter')
ORDER BY o.animal_id;