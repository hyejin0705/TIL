-- DISTINCT : 중복제거 명령어
SELECT COUNT(name) AS count
FROM ( SELECT DISTINCT name
       FROM animal_ins
);