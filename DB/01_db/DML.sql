CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);


-- SELECT 문
-- 1. 이름과 나이 조회
SELECT first_name, age FROM users;

-- 2. 전체 조회
SELECT * FROM users;

-- 3. rowid 조회
SELECT rowid, first_name FROM users;



-- 정렬
-- 1. 이름과 나이를 나이가 어린 순서대로 조회
SELECT first_name, age FROM users
ORDER BY age ASC;


-- 2. 이름과 나이를 나이가 많은 순서대로 조회
SELECT first_name, age FROM users
ORDER BY age DESC;


-- 3. 이름, 나이 계좌 잔고를 나이가 어린 순으로,
--  만약 같은 나이라면, 계좌 잔고가 많은 순으로 정렬해서 조회
SELECT first_name, age, balance FROM users
ORDER BY age, balance DESC;



-- 필터링
-- 1. 모든 지역 조회하기
SELECT country FROM users;


-- 2. 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users;


-- 3. 지역순으로 내림차순 정렬하여 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users
ORDER BY country DESC;


-- 4. 이름과 지역이 중복없이 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users;


-- 5. 이름과 지역 중복없이 지역순으로 내림차순 정렬하여 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users
ORDER BY country DESC;


-- WHERE 실습
-- 1. 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT DISTINCT first_name, age, balance 
FROM users
WHERE age >= 30;


-- 2. 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의
--    이름, 나이, 계좌 잔고 조회하기
SELECT DISTINCT first_name, age, balance 
FROM users
WHERE age >= 30 and balance > 500000;



-- like 실습
-- 1. 이름에 '호'가 포함되는 사람들의 이름과 성 조회
SELECT first_name, last_name
FROM users
WHERE first_name like '%호%';


-- 2. 이름이 '준'으로 끝나는 사람들의 이름을 조회하기
SELECT first_name
FROM users
WHERE first_name like '%준';


-- 3. 서울 지역번호를 가진 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone
FROM users
WHERE phone like '02-%';


-- 4. 나이가 20대인 사람들의 이름과 나이를 조회하기
SELECT first_name, age
FROM users
WHERE age like '2_';


-- 5. 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone
FROM users
WHERE phone like '%-51__-%';


-- in 실습
-- 1. 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
SELECT first_name, country
FROM users
WHERE country in ('경기도', '강원도');


-- 2. 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
SELECT first_name, country
FROM users
WHERE country not in ('경기도', '강원도');



-- betwwen 실습
-- 1. 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
SELECT first_name, age
FROM users
WHERE age BETWEEN 20 and 30;


-- 2. 나이가 20살 이상, 30살 이하가 아닌 사람들의 이름과 나이 조회하기
SELECT first_name, age
FROM users
WHERE age NOT BETWEEN 20 and 30;



-- LIMIT 실습
-- 1. 첫번째부터 열번째 데이터까지 rowid와 이름 조회하기
SELECT rowid, first_name
FROM users LIMIT 10;


-- 2. 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기
SELECT first_name, balance
FROM users
ORDER BY balance DESC LIMIT 10;


-- 3. 나이가 가장 어린 5명의 이름과 나이 조회하기
SELECT first_name, age
FROM users
ORDER BY age LIMIT 5;



-- offset 활용
-- LIMIT는 지정된 숫자 가져오기
-- OFFSET 지정된 숫자부터 시작

-- 21번째부터 30번째까지 데이터의 rowid, 이름 조회하기
SELECT rowid, first_name
FROM users
LIMIT 10 OFFSET 20;



-- GROUP BY 실습

-- 각 지역별로 몇 명씩 살고 있는지 조회하기
SELECT country, count(*)
FROM users
GROUP BY country;


-- 1. 각 성씨가 몇 명씩 있는지 조회하기
SELECT last_name, count(*) AS "합계"
FROM users
GROUP BY last_name;


-- 2. 인원이 많은 성씨 순으로 조회하기
SELECT last_name, count(*) AS "합계"
FROM users
GROUP BY last_name
ORDER BY 합계 DESC;


-- 3. 각 지역별 평균 나이 조회하기
SELECT country, avg(age) as "평균 나이"
FROM users
GROUP BY country;



-- changing data
-- 사전준비
CREATE TABLE classmate (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);


-- INSERT 사용
INSERT INTO classmate
VALUES ('홍길동', 20, '서울');


-- 여러 행 삽입
INSERT INTO classmate
VALUES 
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박지성', 26, '전라'),
    ('최지수', 12, '충청'),
    ('정요한', 28, '경상');



-- UPDATE 실습
-- 2번 데이터의 이름을 '김철수한무두루미' 주소를 '제주'로 수정하기
UPDATE classmate
SET name = '김철수한무두루미',
    address = '제주'
WHERE rowid = 2;



-- DELETE 실습
-- 1. 이름에 '영'이 포함되는 데이터 삭제하기
DELETE FROM classmate
WHERE name like '%영%';


-- 2. 테이블의 모든 데이터 삭제하기
DELETE FROM classmate;

