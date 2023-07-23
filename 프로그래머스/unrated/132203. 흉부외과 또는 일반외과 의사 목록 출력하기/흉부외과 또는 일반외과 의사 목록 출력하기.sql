-- 코드를 입력하세요
SELECT dr_name, dr_id, mcdp_cd, 
    TO_CHAR(hire_ymd, 'YYYY-MM-DD') AS hire_ymd
    -- 형변환 해주지 않으면, 년월일 시,분,초까지 출력됨.
    -- 정답 >> 년월일 표시
FROM doctor
WHERE mcdp_cd IN ('CS', 'GS')
ORDER BY hire_ymd DESC, dr_name;