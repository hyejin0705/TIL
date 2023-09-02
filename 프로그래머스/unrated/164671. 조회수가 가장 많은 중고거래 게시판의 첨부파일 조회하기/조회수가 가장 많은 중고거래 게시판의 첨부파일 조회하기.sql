-- 코드를 입력하세요
SELECT '/home/grep/src/' || board_id || '/' || file_id || file_name || file_ext AS file_path
FROM used_goods_file
WHERE board_id IN ( SELECT board_id
                    FROM ( SELECT board_id
                           FROM used_goods_board
                           ORDER BY views DESC
                         )
                    WHERE ROWNUM = 1
                  )
ORDER BY file_id DESC;