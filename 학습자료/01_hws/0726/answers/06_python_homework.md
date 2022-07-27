### 06_python_homework.md

1. Built-in 함수와 메서드

   - sort() 메서드는 원본 리스트를 정렬하며, 반환 값이 없다.
   - sorted() 함수는 정렬된 새로운 리스트를 반환한다.

   ```python
   # 예시
   
   numbers = [20, 10, 4, 16, 8, 1]
   result1 = numbers.sort()
   
   numbers = [20, 10, 4, 16, 8, 1]
   result2 = sorted(numbers)
   
   print(result1) # None
   print(result2) # [1, 4, 8, 10, 16, 20]
   ```

   



2. `.extend()`와 `.append()` 

   - extend() 메서드는 인자로 들어오는 iterable한 객체를 순회하며 요소를 하나씩 리스트에 삽입한다.
   - append() 메서드는 인자로 들어오는 요소를 그대로 리스트에 삽입한다.

   ```python
   # 예시
   
   students = ['김싸피', '이사피', '조싸피']
   
   students.extend('강싸피')
   students.append('강싸피')
   
   print(students)
   ```

   

3. 복사가 잘 된건가?

   변수 b에는 변수 a에 담긴 리스트의 "참조 값"이 들어있다.

   따라서 `a[2] = 5`와 같이 원본을 바꾸게 되면 b를 출력했을 때도 해당 인덱스의 값이 같이 변해있는 것을 확인할 수 있다.

