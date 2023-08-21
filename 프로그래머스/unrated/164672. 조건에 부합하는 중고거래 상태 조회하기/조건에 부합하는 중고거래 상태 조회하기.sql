-- 코드를 입력하세요
SELECT board_id, writer_id, title, price, 
    CASE status 
        WHEN 'SALE' THEN '판매중'
        WHEN 'DONE' THEN '거래완료'
        ELSE '예약중'
    END AS status
FROM used_goods_board
WHERE TO_CHAR(created_date, 'YYYY-MM-DD') = '2022-10-05'
ORDER BY board_id DESC;