### 04_python_homework.md

1. 위치 인자와 키워드 인자

   * 다음과 같은 함수가 선언되어 있을 때, 보기 (1)~(4) 중에서 실행 시 오류가 발생하는 코드를 고르시오.

   ```PYTHON
   def ssafy(name, location='서울'):
       print(f'{name}의 지역은 {location}입니다.')
   
   # (1)
   ssafy('가흔')
   
   # (2)
   ssafy(location='부울경', name='승현')
   
   # (3)
   ssafy('지우', location='서울')
   
   # (4)
   ssafy(name='승호', '광주') # <- 정답
   ```

   * 키워드 인자를 사용한 뒤에 위치 인자를 활용할 수는 없습니다.

     * ```PYTHON
       ssafy(name='승호', '광주')
       ```



2. 가변 인자 리스트

   * 가변 인자 리스트를 사용하여, 갯수가 정해지지 않은 여러 정수들를 전달 받아 해당 정수들의 평균 값을 반환하는 my_avg 함수를 작성하시오.

   ```PYTHON
   my_avg(77, 83, 95, 80, 70) #=> 81.0
   ```

   ```PYTHON
   # 1
   def my_avg(*args):
       return sum(args) / len(args) 
   ```

   ```PYTHON
   # 2
   def my_avg(*args):
       count = 0
       for num in args:
           count += num
       avg = count / len(args)
       return avg
   ```

   

3. 반환값

   * 다음과 같이 함수를 선언하고 호출하였을 때, 변수 result에 저장된 값을 작성하시오.
     그 값이 나온 이유를 작성하시오.

   ```PYTHON
   def my_func(a, b):
       c = a + b
       print(c)
   
   result = my_func(3, 7)
   ```

   ```PYTHON
   None
   함수에서 반환하는 값이 으면 `None`을 리턴한다.
   `my_func` 는 반환하는 값이 없어서 result에 None이 저장된다.
   ```



4. 이름 공간 (Namespace)

   1. Local scope  

   1. Enclosed scope 

   1. Global scope 

   1. Built-in scope



5. 매개변수와 인자, 그리고 반환

   * 답: 1번

     `return a, b`처럼 사용이 가능하다.

   - 2개를 리턴하는 것 처럼 보이지만, 실제로는 튜플 `(a, b)`가 리턴되는 것이고 이는 하나의 튜플 객체인 것이다.



6. 재귀 함수
   * 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용된다. 
   * 코드가 더 직관적이고 이해하기 쉬운 경우가 있음. (하지만, 만들기는 어려움) 
   * Python Tutor에 보면, 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있다. 
   * 이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생긴다. 
   * 파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료된다.

