-- 1.
-- SELECT '/home/grep/src/' || board_id || '/' || file_id || file_name || file_ext AS file_path
-- FROM used_goods_file
-- WHERE board_id IN ( SELECT board_id
--                     FROM ( SELECT board_id
--                            FROM used_goods_board
--                            ORDER BY views DESC
--                          )
--                     WHERE ROWNUM = 1
--                   )
-- ORDER BY file_id DESC;


-- 2. Join 활용하기
SELECT '/home/grep/src/' || f.board_id || '/' || file_id || file_name || file_ext AS file_path
FROM used_goods_file f
LEFT JOIN used_goods_board b
ON f.board_id = b.board_id
WHERE views = ( SELECT max(views)
                FROM used_goods_board
              )
ORDER BY file_id DESC;