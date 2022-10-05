# 내장함수 find, count 사용하지 않고 푼 방식.

def len_cnt(string):  # count 함수를 대신할 함수
    cnt = 0
    for _ in string:
        cnt += 1
    return cnt


T = 10

for test_case in range(1, T + 1):
    _ = int(input())
    
    find_word = input()
    string = input()

    find_len = len_cnt(find_word)  # 문장의 길이를 생성

    string_len = len_cnt(string)   # 문장의 길이를 생성

    cnt = 0
    # find 함수를 사용하지 못하기 때문에
    # 하나씩 돌면서 맞는 단어 찾기
    for idx in range(string_len - find_len + 1):
        if string[idx : idx + find_len] == find_word:
            cnt += 1
    
    print(f'#{test_case} {cnt}')
