-- 코드를 입력하세요
SELECT member_id, member_name, gender, 
    TO_CHAR(date_of_birth, 'YYYY-MM-DD') AS date_of_birth
FROM member_profile
WHERE tlno IS NOT NULL 
    AND gender = 'W'
    AND TO_CHAR(date_of_birth, 'MM')  = '03'
    -- AND SUBSTR(date_of_birth, 4, 3) = 'MAR' 
    --     -- 3-MAR-93
ORDER BY member_id;