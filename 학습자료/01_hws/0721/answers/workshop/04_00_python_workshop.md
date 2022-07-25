### 04_python_workshop.md

1. 간단한 N의 약수 (SWEA #1933)

   - 반복, 출력(end=), 조건

     ```
     입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하시오.
     ```

     ```python
     N = int(input())
     
     for i in range(1, N+1):
         if N % i == 0:
             print(i, end=' ')
     ```


   

2. List의 합 구하기

   * 정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

     ```python
     list_sum([1, 2, 3, 4, 5]) #=> 15
     ```

     ```python
     def list_sum(numbers):
     		sum_value = 0
     		for number in numbers:
     				sum_value += number
     		return sum_value
     ```

   

3. Dictionary로 이루어진 List의 합 구하기

   * Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

     ```python
     dict_list_sum([{'name': 'kim', 'age': 12}, 
                    {'name': 'lee', 'age': 4}]) #=> 16
     ```

     ```python
     def dict_list_sum(infos):
     		age_sum = 0
     		for info in infos:
     				age_sum += info['age']
     		return age_sum
     ```

     

   

   

4. 2차원 List의 전체 합 구하기

   * 정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

     ```python
     all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) #=> 55
     ```

     ```python
     def all_list_sum(num_lists):
     		lists_sum = 0
     		for num_list in num_lists:
     				for num in num_list:
     						lists_sum += num
     		return lists_sum
     ```

   

5. 숫자의 의미

   * 정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인문자열을 반환하는 get_secret_word 함수를 작성하시오. 
     단, list는 65이상 90이하 그리고 97이상 122이하의 정수로만 구성되어 있다.

     ```python
     def get_secret_word(numbers):
         word = ''
         for number in numbers:
             word += chr(number)
         return word
     
     print(get_secret_word([83, 115, 65, 102, 89]))
     ```



6. 내 이름은 몇일까?

   * 문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다.

     ```
     def get_secret_number(word):
         total = 0
     
         for char in word:
             total += ord(char)
     		
     		return total
     
     get_secret_number('happy') # => 546
     ```



7. 강한 이름

   * 문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.

     ```python
     def get_strong_word(word1, word2):
         word1_total = 0
         word2_total = 0
     
         for char in word1:
             word1_total += ord(char)
     
         for char in word2:
             word2_total += ord(char)
     
         if word1_total > word2_total:
             return word1
         elif word1_total < word2_total:
             return word2
         else:
             return word1, word2
     
     print(get_strong_word('delilah', 'dixon')) # delilah
     ```

     





