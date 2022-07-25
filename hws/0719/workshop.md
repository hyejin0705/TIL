## Python 02. 데이터 타입 및 형 변환
1. 숫자의 입력과 출력
  입력 받은 데이터를 숫자로 변환하고 덧셈해서 출력하는 프로그램을 작성하시오.
  (힌트 : input() 함수를 활용하여 데이터를 입력받을 수 있다.)

```
num = [int(input()) for _ in range(2)]
total = sum(num)
print(total)
```


2. Dictionary를 활용하여 평균 구하기
  좋아하는 점심메뉴를 이용하여 key는 메뉴, value는 가격인 dictionary를 만들고,
  점심메뉴의 평균 값을 출력하시오.

```
lunch = {'김밥': 3000, '샌드위치': 2500, '김치찌개':6500}

print(sum(lunch.values()) / len(lunch.values()))
```