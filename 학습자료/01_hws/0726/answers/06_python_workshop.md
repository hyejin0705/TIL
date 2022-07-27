### 06_python_workshop_md

1. 무엇이 중복일까

   ```
   문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는 duplicated_letters 함수를 작성하시오.
   ```
   
   ```python
   # Basic
   
   def duplicated_letters(words):
       duplicates = []
       for word in words:
           if words.count(word) > 1 and word not in duplicates:
               duplicates.append(word)
       return duplicates
   ```
   
   ```python
   # Comprehension
   
   def duplicated_letters(words):
       # return [word for word in words if words.count(word)>1 and not (word in result or result.add(word))]
       return list({word for word in words if words.count(word) > 1})
   ```
   
   



2. 소대소대

   ```
   문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여반환하는 low_and_up 함수를 작성하시오. 이때, 전달 받는 문자열은 알파벳으로만구성된다.
   ```

   ```python
   # basic
   
   def low_and_up(word):
       new_str = ''
       for idx, char in enumerate(word):
           if idx % 2 == 1:
               new_str += char.upper()
           else:
               new_str += char.lower()
       return new_str
   ```

   ```python
   # list comprehension
   
   def low_and_up(word):
       new_str = [char.upper() if idx%2 else char.lower() for idx, char in enumerate(word)]
       return ''.join(new_str)
   ```

   

3. 솔로 천국 만들기

   ```
   정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.
   ```
   
   ```python
   # enumerate 함수 활용
   def lonely(numbers):
       result = []
       for idx, num in enumerate(numbers):
           if idx == 0:
               result.append(num)
           if result[-1] != num:
               result.append(num)
       return result
   ```
   
   ```python
   # 단순 반복
   def lonely(numbers):
       result = [numbers[0]]
       for num in numbers:
           if result[-1] != num:
               result.append(num)
       return result
   ```
   
   