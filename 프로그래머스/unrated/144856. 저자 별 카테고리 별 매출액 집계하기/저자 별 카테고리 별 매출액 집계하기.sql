-- 코드를 입력하세요
SELECT i.author_id, i.author_name, i.category, 
    SUM(s.sales * i.price) AS total_sales
FROM book_sales s
JOIN ( SELECT a.author_id, a.author_name, b.category, b.book_id, b.price
       FROM book b
       JOIN author a
           ON b.author_id = a.author_id
     ) i
ON s.book_id = i.book_id
WHERE TO_CHAR(s.sales_date, 'YYYY-MM') = '2022-01'
GROUP BY i.author_id, i.author_name, i.category
ORDER BY i.author_id, category DESC;