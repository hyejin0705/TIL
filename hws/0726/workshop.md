1. 무엇이 중복일까
    문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는 duplicated_letters 함수를 작성하시오

    ```python
    def duplicated_letters(string):
        letter_lst = []
        for letter in string:
            if string.count(letter) >= 2:  # 빈도수가 2이상이면 중복 확인
                letter_lst.append(letter)  

        # 중복된 글자들의 중복을 없애주기 위해 set로 변형 후 다시 리스트
        return list(set(letter_lst)) 

    print(duplicated_letters('apple')) # => [‘p’]
    print(duplicated_letters('banana')) # => [’a’, ‘n’]
    ```


2. 소대소대
    문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여 반환하는 low_and_up 함수를 작성하시오. 
    이때, 전달 받는 문자열은 알파벳으로만 구성된다

    ```python
    def low_and_up(string):
        word = ''
        for idx in range(len(string)):
            if idx % 2:
                word += string[idx].upper()
            else:
                word += string[idx].lower()
        return word

    print(low_and_up('apple')) # => aPpLe
    print(low_and_up('banana')) # => bAnAnA
    ```


3. 솔로 천국 만들기
    정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 
    이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다

    ```python
    def lonely(list):
        num_list = []
        for idx, num in enumerate(list):
            
            # 인덱스가 0이면 값을 그냥 넣어줘야 인덱스 에러가 나지 않음
            # 새로운 리스트의 마지막 요소와 새로 들어오는 요소가 같지 않으면,
            if (idx == 0) or (num_list[-1] != num):
                num_list.append(num)   # 새로운 숫자를 리스트에 추가.

        return num_list

    print(lonely([1, 1, 3, 3, 0, 1, 1])) # => [1, 3, 0, 1]
    print(lonely([4, 4, 4, 3, 3])) # => [4, 3]
    ```
