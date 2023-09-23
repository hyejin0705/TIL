-- LEVEL은 숫자 형식으로 계층 수준(상위 → 하위)을 식별하기 위해 계층 쿼리에서 사용되는 의사 열을 나타낸다. LEVEL은 root 행에 대해 1을 부여하며 그 다음 행은 2, 3, 4 ..가 되는 구조로 반환한다. 이 같은 구조는 CONNECT BY 절 사용을 통해 만들 수 있다. 

-- CONNECT BY 절은 계층 구조의 상위 행과 하위 행 간의 계층 관계를 정의해주는 것이다.

SELECT h.hour, count(a.datetime)
FROM ( SELECT LEVEL - 1 AS hour
       FROM DUAL   -- DUAL은 더미 테이블
       CONNECT BY LEVEL <= 24
     ) h
LEFT JOIN animal_outs a
    ON h.hour = TO_CHAR(a.datetime, 'HH24')
GROUP BY hour
ORDER BY hour;


