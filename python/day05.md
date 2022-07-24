#### 파일열기
```python
open('파일 경로', encoding='utf-8')
```

#### json 파일 불러오기
```python
import json
json.load(파일)
```

#### json or 딕셔너리 형 깔끔하게 출력하기
```python
from pprint import pprint
pprint()
```

#### 딕셔너리형태의 특징?
- keys(), values()에는 인덱싱, 슬라이싱이 되지 않는다.
    - 해결방안 : list(dict.keys())같이 리스트로 묶어주면 리스트 형태로 바뀌면서 순서가 있는 형태로 바뀜.

- json, 딕셔너리 형태에서 정보 추출
    1. dict['key']
    2. dict.get('key')


#### 숫자인지 확인
- 숫자이면 True, 아니면 False
    ' '.isnumeric() 
    ' '.isdigit()