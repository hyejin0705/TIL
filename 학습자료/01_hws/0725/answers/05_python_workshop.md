### 05_python_workshop.md



1. 평균 점수 구하기

   ```
   key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.
   ```
   
   ```python
   def get_dict_avg(student):
       scores = []
   
       for score in student.values():
           scores.append(score)
   
       result = sum(scores) / len(student)
       return result
   
   # 또는 
   student = {'python':80, 'web':83, 'algorithm':90, 'django':89}
   sum(student.values()) / len(student.keys()) # 85.5
   ```
   
   



2. 혈액형 분류하기

   ```
   여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 반환하는 count_blood 함수를 작성하시오.
   ```
   
   ```python
   # basic
   
   def count_blood(blood_types):
       blood_dict = {}
       for blood in blood_types:
           if blood_dict.get(blood):
               blood_dict[blood] += 1
           else:
               blood_dict[blood] = 1
       return blood_dict 
   ```
   
   ```python
   # 'dict.get()'
   
   def count_blood(blood_types):
       result = {}
   
       for blood in blood_types:
           result[blood] = result.get(blood, 0) + 1
   
       return result
   ```
   
   

