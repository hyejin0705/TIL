-- 코드를 입력하세요
SELECT name, datetime
FROM ( SELECT i.name, i.datetime
       FROM animal_ins i
       LEFT JOIN animal_outs o
           ON i.animal_id = o.animal_id
       WHERE o.datetime IS NULL
       ORDER BY i.datetime
     )
WHERE ROWNUM <= 3;