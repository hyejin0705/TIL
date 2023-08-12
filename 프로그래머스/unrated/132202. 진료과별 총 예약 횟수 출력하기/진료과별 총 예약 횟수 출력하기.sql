-- 코드를 입력하세요
SELECT mcdp_cd AS "진료과코드", count(apnt_no) AS "5월예약건수"
FROM appointment
WHERE TO_CHAR(apnt_ymd, 'YYYY-MM') = '2022-05'
GROUP BY mcdp_cd
ORDER BY "5월예약건수", "진료과코드";