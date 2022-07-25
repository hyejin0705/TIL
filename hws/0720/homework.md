1. Built-in 함수
    Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.

- 파이썬 내장함수 : print, len, sum, round, range


2. 홀수만 담기
    range와 slicing을 활용하여 1부터 50까지의 숫자 중,
    홀수로만 이루어진 리스트를 만드시오.

   ```python
   
   num_lst = [n for n in range(1, 51)]

   odd_lst = num_lst[::2]

   print(odd_lst)
   ```


3. 반복문으로 네모 출력
    두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오.

   ```python
   
   n = 5
   m = 9
   
   for _ in range(m):
      print('*' * n)
   ```


4. 조건 표현식
    주어진 코드의 조건문을 조건 표현식으로 바꾸어 작성하시오.

   ```python
   
    # temp = 36.5
    # if temp >= 37.5:
    # print('입실 불가')
    # else:
    # print('입실 가능')

    temp = 36.5
    result = '입실 불가' if temp >= 37.5 else '입실 가능'
    print(result)
   ```


5. 정중앙 문자
    문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를
    작성하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.

   ```python

    def get_middle_char(string):
        idx = len(string) // 2    # 문자 길이에서 2로 나눈 값

        if len(string) % 2:       # 문자길이가 홀수인 경우
            result = string[idx]  # 인덱스는 0부터 시작

        else:                     # 문자길이가 짝수인 경우
            result = string[idx - 1 : idx + 1] 
            # 짝수일 경우 정중앙 문자 2개를 반환

        return result

    print(get_middle_char('ssafy')) # => a
    print(get_middle_char('coding')) # => di
   ```