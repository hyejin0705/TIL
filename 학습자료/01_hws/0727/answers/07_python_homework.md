### 07_python_homework.md

1. Type Class

```
int, float, complex, str, map, zip, ...
```

- 파이썬에서 int, float라고 그냥 실행 했을 때, `<class 'int'>`의 형태로 나오는데 이렇게 나오는 모든 것들.



2. Magic Method

- `__init__` : 인스턴스가 생성될 때 실행
- `__del__` : 인스턴스가 삭제될 때 실행
- `__str__` : 인스턴스를 `print()` 할 때 보여질 값을 반환
- `__repr__` : 인스턴스 자체가 반환할 값을 반환



3. Instance Method

- list - `.sort()`, `.append()`, `.extend()` ...
- str - `.upper()`, `.lower()`, `.swapcase()`, `.isalpha()`, ...
- dict - `.get()`, `.update()`, ...



4. 오류의 종류

   ```
   ZeroDivisionError # 0으로 나누려고 할 때
   NameError # 정의 되지 않은 변수 사용
   TypeError # 자료형에 대한 잘못된 사용
   IndexError # Index 범위를 벗어나서 참조하려 할 때
   KeyError # Dict에 없는 Key를 찾으려 할 때
   ModuleNotFoundError # 모듈을 찾을 수 없는 경우
   ImportError # 모듈은 있으나 없는 클래스나 메소드를 가져오려 할 때
   ```