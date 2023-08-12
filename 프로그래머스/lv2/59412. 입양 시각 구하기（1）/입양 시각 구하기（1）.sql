-- TO_CHAR(datetime, 'HH') : 01 ~ 12
-- TO_CHAR(datetime, 'HH24') : 01 ~ 24

SELECT TO_NUMBER(TO_CHAR(datetime, 'HH24')) AS hour, 
    count(animal_id) AS count
FROM animal_outs
WHERE TO_CHAR(datetime, 'HH24') BETWEEN 9 AND 19
GROUP BY TO_CHAR(datetime, 'HH24')
ORDER BY hour;