# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    string = ''
    for char in word:
        idx = ord(char) + n
        if char.islower():  # 소문자일때
            while idx > 122:   # 다시 a부터 시작 (while로 반복)
                idx -= 26
        else:
            while idx > 90:   # 대문자일때 (while로 반복)
                idx -= 26
        string += chr(idx)
    return string
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx