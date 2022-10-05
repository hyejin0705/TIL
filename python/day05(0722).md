#### 1. 파일열기
```python
open('파일 경로', encoding='utf-8')
```

#### 2. json 파일 불러오기
```python
import json
json.load(파일)
```

#### 3. json or 딕셔너리 형 깔끔하게 출력하기
```python
from pprint import pprint
pprint()
```

#### 4. 딕셔너리형태의 특징?
- keys(), values()에는 인덱싱, 슬라이싱이 되지 않는다.
    - 해결방안 : list(dict.keys())같이 리스트로 묶어주면 리스트 형태로 바뀌면서 순서가 있는 형태로 바뀜.

- json, 딕셔너리 형태에서 정보 추출
    1. dict['key']
    2. dict.get('key')


#### 5. 숫자인지 확인
- 숫자이면 True, 아니면 False
    ' '.isnumeric() 
    ' '.isdigit()

- 문자인지 확인
    ' '.isalpha

#### 6. 파이썬 함수
1. split() - 문자열을 구분자를 기준으로 나누는 함수
2. strip() - 문자열의 공백을 제거하는 함수
3. print()
    - 주요 파라미터
        - end : print의 실행 후 다음 print와의 사이의 구분해주는....
            ```python
            for i in range(5):
                print(i, end = ' ') # 0 1 2 3 4 
                print(i)  # end의 기본값은 \n(한 줄 띄기) 
                # 0
                # 1
                # 2
                # 3
                # 4
            ```
        - sep : print안의 여러 출력값들의 구분해주는..

4. 아스키문자 함수 
    - chr() : 숫자를 문자로 변환
    - ord() : 문자를 숫자로 변환

