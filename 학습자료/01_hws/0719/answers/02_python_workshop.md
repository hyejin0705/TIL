### 02_python_workshop.md

1. 숫자의 입력과 출력과 입력

   * 받은 데이터를 숫자로 변환하고 계산하여 출력하는 프로그램을 작성하시오

     ```python
     a = int(input())
     b = int(input())
     print(a+b)
     ```

     

2. Dictionary를 활용하여 평균 구하기

  * 좋아하는 점심메뉴 정보를 이용하여 key 는 메뉴 , value 는 가격인 dictionary 를 만들고
    점심메뉴의 평균 값을 출력하시오

    ```python
    lunch = {
        	'김밥' : 4000,
            '햄버거' : 15000,
    		}
    print((lunch['김밥']+lunch['햄버거'])/2)
    ```

    
