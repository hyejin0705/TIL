SELECT u.user_id, u.nickname, 
    SUM(b.price) AS total_sales
FROM used_goods_board b
LEFT JOIN used_goods_user u
    ON b.writer_id = u.user_id
WHERE b.status = 'DONE'
GROUP BY u.user_id, u.nickname
-- ORA-00979: not a GROUP BY expression >> SELECT 절에 없는 컬럼을 사용하려고 할 때 발생
-- u.user_id 하나만 하면 에러 발생 (u.user_id, u.nickname 같이 활용)
HAVING SUM(b.price) >= 700000
ORDER BY total_sales;
