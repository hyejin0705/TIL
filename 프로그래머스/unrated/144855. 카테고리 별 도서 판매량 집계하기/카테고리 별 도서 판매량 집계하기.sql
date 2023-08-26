-- 코드를 입력하세요
SELECT b.category,
       SUM(s.sales) AS total_sales
FROM book_sales s
LEFT JOIN book b
    ON s.book_id = b.book_id
WHERE TO_CHAR(s.sales_date, 'YYYY-MM') = '2022-01'
GROUP BY b.category
ORDER BY b.category;
