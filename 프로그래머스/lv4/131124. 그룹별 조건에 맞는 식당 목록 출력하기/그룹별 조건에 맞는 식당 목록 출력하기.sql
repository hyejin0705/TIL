-- 코드를 입력하세요
SELECT member_name, review_text, TO_CHAR(review_date, 'YYYY-MM-DD') AS review_date
FROM rest_review r
JOIN member_profile p
    ON r.member_id = p.member_id
WHERE r.member_id IN ( SELECT member_id
                      FROM ( SELECT member_id, 
                                 count(review_id) AS total
                             FROM rest_review
                             GROUP BY member_id
                             ORDER BY total DESC
                           )
                      WHERE ROWNUM <= 1
                    )
ORDER BY review_date, review_text;