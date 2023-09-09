-- 코드를 입력하세요
SELECT a.apnt_no, p.pt_name, a.pt_no, 
    a.mcdp_cd, d.dr_name, a.apnt_ymd
FROM appointment a
LEFT JOIN patient p
    ON a.pt_no = p.pt_no 
LEFT JOIN doctor d
    ON a.mddr_id = d.dr_id
WHERE TO_CHAR(a.apnt_ymd, 'YYYY-MM-DD') = '2022-04-13' 
    AND a.apnt_cncl_yn = 'N' 
    AND a.mcdp_cd = 'CS'
ORDER BY a.apnt_ymd;