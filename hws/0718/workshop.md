## Python 01. 기초문법과 데이터의 입•출력

1. 문자 print
    It’s SSAFY 8 을 출력하는 프로그램을 작성하시오. (중간에 작은따옴표가 있다.)

```
print("It’s SSAFY 8")
```


2. 숫자 print
    458345 + 623576 를 계산하여 출력하는 프로그램을 작성하시오.

```
a = 458345
b = 623576

print(a + b)
```



3. 변수를 사용해서 데이터 출력하기
    두 변수 greeting, month를 사용해서 Hello July 를 출력하는 프로그램을 작성하시오.

```
greeting = ‘Hello’
month = ‘July’

print(greeting + ' ' + month)
```



4. 문자형의 입력과 출력
    입력 받은 문자를 출력하는 프로그램을 작성하시오.
    (힌트 : input() 함수를 활용하여 데이터를 입력받을 수 있다.) 

```
'''
[입력]
문자를 입력받는다.
[출력]
입력 받은 문자를 출력한다.
[입력 예시]
Hello! SSAFY 8
[출력 예시]
Hello! SSAFY 8
'''

hello = input()

print(hello)
```