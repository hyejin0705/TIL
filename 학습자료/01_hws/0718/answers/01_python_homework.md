### 01_python_homework.md

1. Python 예약어

   - Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하시오.

   ```python
   import keyword
   print(keyword.kwlist)
   ```


2. 실수 비교

   ```python
   import math
   math.isclose(num1, num2)
   ```


3. 이스케이프 시퀀스

   ```python
   '\n'
   '\t'
   '\\'
   ```


4. String Interpolation

   ```python
   print(f'안녕, {name}야')
   ```


5. 형 변환

   ```python
   int('3.5') #(5)
   ```


6. 네모 출력

   ```python
   print((('*' * n) + '\n') * m)
   ```


7. 이스케이프 시퀀스 응용

   ```python
   print('"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지.\'')
   ```


8. 근의 공식

   ```python
   (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
   (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)
   ```