### 02_python_homework.md

1. Mutable & Immutable

   - 제시 된 컨테이너들을 각각, 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오.

   ```
   string, tuple, range => immutable
   list, set, dictionary => mutable
   ```


2. Dictionary 만들기

   - 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.

   ```python
   student_dict = {
       'haley': 28,
       'isaac': 29
   }
   ```


3. 평균 구하기

   - 제시된 list의 평균 값을 출력하시오.

   ```python
   #1 
   result = 0
   for num in scores:
       result += num
   print(result / len(scores)) # 87.75
   ```

   ```python
   #2
   print(sum(scores) / len(scores)) # 87.75
   ```

