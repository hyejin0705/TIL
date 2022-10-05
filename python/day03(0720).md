## 1) 제어문

- 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행하거나 계속하여 실행하는 제어가 필요함
- 제어문은 순서도로 표현이 가능

### 1. **조건문**

**1.1 조건문 기본**

- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

**1.2 기본형식**

- 조건에는 참/거짓에 대한 조건식
- if 조건이 참인 경우 뒤에 들여쓰기 되어있는 코드블록을 실행
- 이외의 경우 else: 뒤에 들여쓰기 되어있는 코드블록 실행
- else는 선택적으로 활용
    
    ```python
    # 조건문을 통해 변수 num의 값의 홀수/짝수 여부를 출력하시오
    num = int(input('숫자를 입력하시오 >> '))

    # if num % 2 == 1:
    if num % 2:        # 1은 True이기 때문에 Pythonic한 형식
        print('홀수')

    else:
        print('짝수')
    ```

**1.3 복수조건문**

- 복수의 조건식을 활용할 경우 elif를 활용하여 표현함
- 조건식을 동시에 검사하는 것이 아니라 순차적으로 비교
    
- 미세먼지 조건식 만들기(실습)
    
    ```python
    dust = 80
    if dust <= 30:
    	print('좋음')
    elif dust <= 80:
    	print('보통')
    elif dust <= 150:
    	print('나쁨')
    else:
    	print('매우 나쁨')
    ```
    

**1.4 중첩조건문**

- 조건문은 다른 조건문에 중첩되어 사용될 수 있음
    - 들여쓰기에 유의하여 작성할 것

    ```python
    dust = 500
    if dust <= 30:
        print('좋음')
        if dust <= 0:
            print('값이 잘못되었습니다.')
    elif dust <= 80:
        print('보통')
    elif dust <= 150:
        print('나쁨')
    else:
        print('매우 나쁨')

    if dust > 300:
        print('실외 활동을 자제하세요.')
    ```

**1.5 조건 표현식**

- 조건표현식을 일반적으로 조건에 따라 값을 정할 때 활용
- 삼항 연산자로 부르기도 함
- **true인 경우 값 if 조건 else false인 경우 값**

    ```python
    # 절댓값을 저장하기 위한 조건표현식 생성
    value = num if num >= 0 else -num

    # 짝수, 홀수 찾는 코드
    result = '홀수' if num % 2 else '짝수'

    num = -5
    value = num if num >= 0 else 0
    print(value)

    if num >= 0:
        print(num)
    else:
        print(0)
    ```

### 2. 반복문

- 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용

**2.1 반복문의 종류**

1. while문
- 주로 반복 횟수를 모르는 경우 활용
- 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함

1. for 문
- 반복횟수가 정해진 경우 활용
- 반복가능한 객체를 모두 순회하면 종료(별도의 종료 조건이 필요 없음)

1. 반복제어
- break(종료), continue(건너띄기), for-else

**2.2 while문** 

- while문은 조건식이 참인 경우 반복적으로 코드를 실행
- 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨.
- 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨.
- while문은 무한 루프를 하지 않도록 종료 조건이 반드시 필요

    ```python
    a = 0
    while a<5:   # 종료조건
        print(a)
        a += 1  # 반복시 a는 계속 증가
    print('끝')
    ```

- [python tutor]([https://pythontutor.com/visualize.html#mode=edit](https://pythontutor.com/visualize.html#mode=edit)) : 파이썬 코드를 시각적으로 보여주는 사이트

**2.2.1 복합연산자**

- 복합연사자는 연산과 할당을 합쳐놓은 것
ex) +=, -=, *=......

**2.3 for문**

- for문은 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체(iterable)의 요소를 모두 순회
- 처음부터 끝까지 모두 순회하므로 별도의 종료 조건이 필요하지 않음
- Iterable
    - 순회할 수 있는 자료형(string, list, dict, tuple, range, set 등)
    - 순회형 함수(range, enumerate)
    
    ```python
    for 변수명 in iterable:
    	# Code block
    ```
    

1. 딕셔너리(Dictionary) 순회

- 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용
- 추가 메서드를 활용하여 순회할 수 있음
    - keys( ) : key로 구성된 결과
    - values( ) : value로 구성된 결과
    - items( ) : (key, value)의 튜플로 구성된 결과
    
    ```python
    grades = {'john' : 80, 'eric' : 90}
    for student, grade in grades.items():
    	print(student, grade)
    ```
    

2. enumerate(iterable, start = (시작숫자지정)) 순회

- 인덱스와 객체를 쌍으로 담은 열거형 객체 반
    - (index, value) 형태의 tuple로 구성된 열거 객체를 반환

**2.4 Comprehension**

1. List Comprehension (리스트 컴프리핸션)

    - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
    - [code for 변수 in iterable]
    - [code for 변수 in iterable if 조건식]

        ```python
        # 1~3의 세제곱 리스트 만들기
        # 1. 기본 반복문
        cubic_lst = []
        for number in range(1, 4):
            cubic_list.append(number ** 3)
        print(cubic_list)
        # [1, 8, 27]

        # 2. 리스트 컴프리핸션 활용
        cubic_list = [number ** 3 for number in range(1, 4)]
        print(cubic_list)
        # [1, 8, 27]
        ```

1. Dictionary Comprehension
    - 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법
    - {code for 변수 in iterable}
    - {code for 변수 in iterable if 조건식}
    
        ```python
        # 1~3의 세제곱 딕셔너리 만들기
        # 1. 기본 반복문
        cubic_dict = {}
        for number in range(1, 4):
            cubic_dict[number] = number ** 3
        print(cubic_dict)
        # {1 : 1, 2 : 8, 3 : 27}

        # 2. 리스트 컴프리핸션 활용
        cubic_dict = {number : number ** 3 for number in range(1, 4)}
        print(cubic_dict)
        # {1 : 1, 2 : 8, 3 : 27}
        ```
    

**2.5 반복문 제어**

- break : 종료
- continue : skip, 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
- for-else
    - 끝까지(온전히) 반복문을 실행한 이후에 else문 실행
    - break를 통해 중간에 종료되는 경우 else문은 실행되지 않음
    (else문은 break로 중단되었는지 여부에 따라 실행)

        ```python
        for char in 'banana':
            if char == 'b':
                print(b!)
                break
        else:
            print('b가 없습니다.')

        # b!
        ```

- pass : 아무것도 하지 않음.
    - 특별히 할 일이 없을 때 자리를 채우는 용도로 사용
        
        (일단 전체적인 로직을 짜는 경우 자리를 채우는 용도)
        
    - 반복문 아니어도 사용 가능


## 2) 함수

### 1. 함수 기초

- Decomposition(분해)
    - 기능을 분해하고 재사용을 가능하게 한다
    
- Abstraction(추상화)
    - 복잡한 내용을 모르더라도 사용할 수 있도록 재사용성과 가독성, 생산성
    - 사실 내부 구조를 변경할 게 아니라면 몰라도 무방

**1.1 함수의 종류**

- 내장 함수
    - 파이썬에 기본적으로 포함된 함수
- 외장 함수
    - import문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
- 사용자 정의 함수
    - 직접 사용자가 만드는 함수 (def)

**1.2 함수의 정의**

- 특정한 기능을 하는 코드의 조각(묶음)
- 특정 코드를 매번 다시 작성하지 않고, 필요시에만 호출하여 간편히 사용

**1.3 함수 기본 구조**

- 선언과 호출
- 입력
- 문서화
- 범위
- 결과값

**1.4 선언과 호출**

- 함수의 선언은 **def 키워드**를 활용함
    - 함수를 사용하기 위해서는 먼저 함수를 정의해야 함
    
- 들여쓰기를 통해 코드블록을 작성함
    - Docstring은 함수 body 앞에 선택적으로 작성 가능
    - 작성 시에는 반드시 첫 번째 문장에 문자열 ''' '''

- 함수는 **parameter**를 넘겨줄 수 있음

- 함수는 동작 후에 **return**을 통해 결괏값을 전달함
    - return : 값 반환 후 함수가 바로 종료
    - 함수는 항상 return를 사용해야 한다?  XXX

- 함수는 함수명 ( )으로 호출하여 사용
    - parameter가 있는 경우, 함수명(값1, 값2, ...로 호출)
    
    ```python
    num = 0
    num = 1
    
    def func1(a, b):
    	return a + b
    
    def func2(a, b):
    	return a - b
    
    def func3(a, b):
    	return func(a, 5) + func(5, b)
    
    result = func3(num1, num2)
    
    print(result)  # 9
    ```
    

### 2. 함수의 결괏값(Output)

- 값에 따른 함수의 종류
    - Void function
        - 명시적인 return 값이 없는 경우, None을 반환하고 종료
    - Value returning function
        - 함수 실행 후, return문을 통해 값 반환
        - return을 하게 되면, 값 반환 후 함수가 바로 종료

- 주의 : print vs return
    - print 함수와 return의 차이점
        - print를 사용하면 호출될 때마다 값이 출력됨.(주로 테스트를 위해 사용)
        - 데이터 처리를 위해서는 return 사용
        - REPL(Read-Eval-Print-Loop) 환경에서는
        마지막으로 작성된 코드의 리턴 값을 보여주므로
        같은 동작을 하는 것으로 착각할 수 있지만, 둘은 다르다.
        
- 두 개 이상의 값을 반환하는 방법은?
    
    ```python
    return x - y, x + y  # 반환 값으로 튜플을 사용
    ```
    

- 함수 반환 정리
    - 파이썬 내부에서는 함수 안에 return 대신 print가 있다면,
        
        함수 출력시 None를 반환받는다.
        
    - return x -> None
    - return 0 -> 하나를 반환, 여러 개를 원하면, 튜플 활용(혹은 리스트 활용)
    

### 3. 함수의 입력

- Parameter (매개변수, 인수) : 함수를 정의할 때, 함수 내부에서 사용되는 변수
- Argument (인자) : 함수를 호출할 때, 넣어주는 값
    - 함수 호출 시 함수의 parameter를 통해 전달되는 값
    - Argument는 소괄호 안에 할당 func_name(argument)
        - 필수 Argument : 반드시 전달되어야 하는 argument
        - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본값이 전달
        
    - Positional Arguments : 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨.
    
    - Keyword Arguments
        - 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
        - Keyword Argument 다음에 Positional Argument를 활용할 수 없음
            
            ```python
            def add(x, y):
            	return x + y
            
            add(x=2, y=5)   # Keyword Argument
            add(2, y=5)     # 처음은 Positional Argument
            add(x=2, 5)     # Error
            add(y=3, x=2)
            ```
            
        
    - Default Argument Values
        - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함.
            - 정의된 것보다 더 적은 개수의 argument들로 호출될 수 있음.
            
            ```python
            def add(x, y=0):
            	return x + y
            
            add(2)  # y는 기본값 0으로 자동 지정
            ```
            
        
    - 정해지지 않은 여러 개의 Arguments처리
        - 애스터리스크(Asterisk) 혹은 언패킹 연산자라고 불리는 *를 사용
            - 패킹 : 여러 개의 데이터를 묶어서 변수에 할당하는 것
            - 언패킹 : 스퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
                - 언패킹시 변수의 개수와 할당하고자 하는 요소의 개수가 동일해야 함
                - 언패킹시 왼쪽 변수에 asterisk(*)를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음
            
            ```python
            numbers = [1, 2, 3, 4, 5]  # 패킹
            
            a, b, *rest = numbers
            print(rest)   # [3, 4, 5]
            
            a, *rest, e = numbers
            print(rest)   # [2, 3, 4]
            ```
            
        - Asterisk(*)와 가변인자
            - *는 스퀀스 언패킹 연산자라고도 불리며, 말 그대로 시퀀스를 풀어 헤치는 연산자
                - 주로 튜플이나 리스트를 언패킹하는데 사용
                - *를 활용하여 가변인자를 만들 수 있음
                    
                    
    - 가변인자(*args)
        - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
        - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용
        
        ```python
        def add(*args):
            for arg in args:
        		    print(arg)
        
        add(2)
        add(2, 3, 4, 5)
        ```
        
    - 가변 키워드 인자(**kwargs)
        - 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
        - **kwargs는 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현
        - 반드시 받아야 하는 키워드 인자와, 추가적인 키워드 인자를 구분해서 사용할 수 있음
        
    - 가변인자와 가변키워드인자를 동시에 사용할 수 있을까?
        - 함께 사용할 수 있음
        
        ```python
        def print_family_name(*parents, **pets):
            print("아버지 : ", parents[0])
            print("어머니 : ", parents[1])
        
            if pets:
                print("반려동물들....")
        	      for title, name in pets.items():
                    print('{} : {}'.format(title, name)
        
        print_family_name('아부지', '어무이', dog = '멍멍이', cat = '냥냥이')
        ```
        

### 4. Python의 범위 (Scope)

- 함수는 코드 내부에 **local scope**를 생성, 그 외의 공간인 **global scope**로 구분
    - scope
        - global scope : 코드 어디에서든 참조할 수 있는 공간
        - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
    - variable(변수)
        - global variable : global scope에 정의된 변수
        - local variable : local scope에 정의된 변수
- 변수 수명주기
    - 변수는 각자의 수명주기가 존재
        - built-in scope : 파이썬이 존재하는 한 영원히 유지
        - global scope : 프로젝트가 살아있는 한 유지,
        모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
        - local scope : 함수 안에서만 유지,
        함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
        
        ```python
        def func():
        	a = 20
        	print('local', a)
        
        func()   # local 20
        
        print('global', a)
        # NameError : name 'a' is not defined
        ```
        
- 이름 검색 규칙 (Name Resolution)
    
    - 파이썬에서 사용되는 이름(식별자)들은 이름공간에 저장되어 있음
    - 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
        - Local scope : 지역 범위(현재 작업 중인 범위)
        - Enclosed scope : 지역 범위 한 단계 위 범위
        - Global scope : 최상단에 위치한 범위
        - Built-in score : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)
    
    - 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음
        
- global문
    - 현재 코드블록 전체에 적용되며, 나열된 식별자가 global variable임을 나타냄
        - global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
        - global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함.
        
        ```python
        # 함수 내부에서 글로벌 변수 변경하기
        a = 10
        def func1():
        		global a   # 선언
        		a = 3      # 할당
        
        print(a)   # 10
        func1()
        print(a)   # 3
        ```
        
    
    - Local scope에서 global 변수 값의 변경
        
        global 키워드를 사용하지 않으면, Local scope에 a변수가 생성됨.
        

### 5. 함수의 응용

- 내장함수 (Built-in Functions)
    - 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수와 형이 내장되어 있음

- **map**
    - map(function, iterable)
    - 순회 가능한 데이터 구조(iterable)의 모든 요소에 함수 적용하고,
        
        그 결과를 map object로 반환
        
        ```python
        numbers = [1, 2, 3]
        result = map(str, numbers)
        print(result, type(result))
        # <map object at 0x0000020984097A0> <class 'map'>
        
        print(list(result))  # ['1', '2', '3']
        # 리스트 형변환을 통해 결과 직접 확인
        ```
        
    
- **filter**
    - filter(function, iterable)
    - iterable 데이터의 모든 요소에 함수적용,
        
        그 결과가 True인 것들을 filter object로 반환
        
        ```python
        def odd(n):
        	return n % 2
        
        numbers = [1, 2, 3]
        result = filter(odd, numbers)
        print(result, type(result))
        # <filter object at 0x000001FB4B217F40> <class 'filter>
        
        print(list(result))  # [1, 3]
        # 리스트 형변환을 통해 결과 직접 확인
        ```
        
- zip # 2차원?
    - zip(*iterables)
    - 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
        
        ```python
        girls = ['jane', 'ashley']
        boys = ['justin', 'eric']
        
        pair = zip(girls, boys)
        print(pair, type(pair))
        #
        print(list(pair))  # [('jane', 'justin), ('ashley', 'eric')]
        # 리스트 형변환을 통해 결과 확인
        ```
        
    
- lambda함수   —   lambda[parameter] : 표현식
    - 한 줄 함수, 한번만 사용하는 함수
    - 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
    
    - 특징
        - return문을 가질 수 없음
        - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
        
    - 장점
        - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
        - def를 사용할 수 없는 곳에서도 사용 가능
        
        ```python
        # 삼각형의 넓이를 구하는 공식 - def
        def triangle_area(b, h):
        		return 0.5 * b * h
        print(triangle_area(5, 6))   # 15.0
        
        # 삼각형의 넓이를 구하는 공식 - lambda
        triangle_area = lambda b, h : 0.5 * b * h
        print(triangle_area(5, 6))   # 15.0
        ```
        

- 재귀함수
    - 자기 자신을 호출하는 함수
    - 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
        - 알고리즘 중 재귀함수로 로직을 표현하기 쉬운 경우가 있음 (예, 점화식)
        - 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
    - 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
        
        ```python
        def factorial(n):
        	if n == 0 or n == 1:
        		return 1
        
        	else:
        		return n * factorial(n-1)  # 함수를 다시 실행
        		# 4 * f(3)
        		#     3 * f(2)
        		#         2 * f(1)
                #             1     = 4 * 3 * 2 * 1
        
        print(factorial(4))   # 24
        ```
        
- 재귀함수 주의사항
    - 재귀 함수는 base case에 도달할 때까지 함수를 호출함
    - 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨.
    - 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1000번으로,
    호출 횟수가 이를 넘어가게 되면 Recursion Error 발생

- 반복문과 재귀함수 비교
    - 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용함.
    - 재귀 호출은 변수 사용을 줄여줄 수 있음.
    - 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림.
        
        (웬만하면 사용 지양)
        

## 모듈

- 모듈(module) : 다양한 기능을 하나의 파일로
- 패키지(package) : 다양한 파일을 하나의 폴더로
- 라이브러리(library) : 다양한 패키지를 하나의 묶음으로
- 프레임워크 : 라이브러리보다는
- pip : 이것을 관리하는 관리자
- 가상환경 : 패키지의 활용 공간, 버전관리를 해주는 역할

### 1. 모듈과 패키지

- 모듈(module) : 특정 기능을 하는 코드를 파이썬 파일(.py)단위로 작성한 거
- 패키지
    - 특정 기능과 관련된 여러 모듈의 집합
    - 패키지 안에는 또 다른 서브 패키지를 포함
    
    ```python
    import module as md  # as 별칭, 별칭으로 모듈을 사용할 수 있음
    
    from module import var, function, Class 
    # import되는 함수들의 이름으로만 사용
    
    from module import *   # * : 모든
    
    from package import module
    from package.module import var, function, Class
    ```
    

### 2. 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 내장 함수
    - [https://docs.python.org/ko/3/library/index.html](https://docs.python.org/ko/3/library/index.html)

- 파이썬 패키지 관리자(pip)
    - PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
    
    - 패키지 설치
        - 최신 버전/ 특정버전/ 최소버전을 명시하여 설치
        - 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음
            - pip install Somepackage == 1.0.5 (버전 명시)
    
    - 패키지 삭제
        - pip는 패키지 업그레이드를 하는 경우 과거 버전을 자동으로 지워줌
        - pip uninstall somepackage
        
    - 패키지 목록 및 등록 패키지 정보
        - pip list
        - pip show somepackage
    
    - 패키지 관리하기
        - 아래의 명령어들을 통해 패키지 목록을 관리하고 설치
        - 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함
            - pip freeze > requirements.txt
            - pip install -r requirements.txt    # r옵션 : 순서대로 가져옴.
    
    - 다양한 파이썬 프로젝트에서 사용됨.

### 3. 사용자 모듈과 패키지

- 패키지는 여러 모듈/하위 패키지로 구조화
    - 활용 예시 : package.module
- 모든 폴더에는 **init**.py를 만들어 패키지로 인식
    - python 3.3부터는 파일이 없어도 되지만, 하위버전 호환 및 프레임워크 등에서의 동작을 위해 파일을 생성하는 것을 권장
        
        ```python
        # calculator/tools.py
        from calculator import tools
        
        # dir : tools에 어떤 변수와 메소드(method)를 가지고 있는지 나열
        print(dir(tools))
        '''
        ['__builtins__', '__cached__', '__doc__',.....
        'add', 'minus']
        '''
        
        print(tools.add(5, 3))    # 8
        print(tools.minus(5, 3))  # 2
        ```
        

### 4. 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우
모두 pip를 통해 설치를 해야 함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
    - 과거 - django 버전 2.
    - 현재 - django 버전 3.
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음

- 가상환경을 만들고 관리하는데 사용되는 모듈
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
    - 특정 폴더에 가상 환경이(패키지 집합 폴더 등)있고
    - 실행 환경(예 - bash)에서 가상환경을 활성화시켜
    - 해당 폴더에 있는 패키지를 관리/사용함

- 가상환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨.
    - python -m venv <폴더명>