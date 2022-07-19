## Jupyter notebook

- 설치 및 설정
    
    pip install notebook

    jupyter notebook  :  노트북 실행
    
    pip install jupyter_contrib_nbextensions
    
    jupyter contrib nbextension install --user
    

- 장점
    1. 파이썬 코드와 마크다운을 같이 작성 가능
    2. 파이썬 코드의 실행결과를 함께 파일로 저장
    
    1. 전체 파일 단위가 아닌, 셀 단위의 실행 가능
    
- 단축키
    - ctrl + enter : 셀 실행
    - shift + enter : 셀 실행 후 다음 셀 이동
    - 셀 선택 후 + m : 마크다운 작성 가능
    - 셀 선택 후 + y : 코드 셀로 변경
    - d, d : 셀 삭제
    

## 복습

- 해당 데이터 타입을 확인하기 위해서는 `type()`을 활용합니다.
- 해당 값의 메모리 주소를 확인하기 위해서는 `id()`를 활용합니다.

**2) 변수  2. 식별자** - 파이썬 키워드/예약어 출력

```python
# import 구문을 사용하여 keyword를 불러옵니다.
# print를 이용하여 파이썬이 가지고 있는 키워드 / 예약어를 출력해봅시다.

import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 
#  'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
#  'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
#  'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
#  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

**3) 자료형 1. 정수 자료형(int)** 

```python
import sys
max_int = sys.maxsize
# sys.maxsize 의 값은 2**63 - 1 => 64비트에서 부호비트를 뺀 63개의 최대치
```

- round(값, 소수점자릿수) : 반올림 함수
    - round() 는 0~4는 내림, 5는 동일하게 작동하지 않고 반올림 방식에 따라 다릅니다.
    - 짝수에서 5는 내림 / 홀수에서 5는 올림
    
- divmod( ) : 나눗셈 함수
    
    ```python
    print(divmod(5, 2))  # (2, 1) # 몫, 나머지 출력
    
    quotient, remainder = divmod(5, 2)
    
    print(f'몫은 {quotient}, 나머지는 {remainder}입니다.')
    # 몫은 2, 나머지는 1입니다.
    ```
    

## 연산자

1. 산술 연산자  - 0718 연산자
2. 비교 연산자  - 0718 불린형
3. 논리 연산자  - 0718 불린형
4. 복합 연산자

5. 식별 연산자
    - `is` 연산자를 통해 동일한 object인지 확인할 수 있습니다.
    - 파이썬에서 -5 부터 256 까지의 id는 동일합니다.
    
6. 멤버십 연산자
    - 요소가 시퀀스에 속해있는지 확인할 수 있습니다.
        - `in` 연산자
        - `not in` 연산자
            
            ```python
            print('a' in 'apple') # True
            print('b' in 'apple') # False
            ```


## [파이썬 기초 100제](https://codeup.kr/problemsetsol.php?psid=33)
