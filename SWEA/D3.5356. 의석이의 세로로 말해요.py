def length(string):    # 내장함수 len
    cnt = 0
    for _ in string:
        cnt += 1
    return cnt

T = int(input())

for test_case in range(1, T+1):
    lst = [list(input()) for _ in range(5)]

    len_lst = []    # 길이 리스트
    max_len = 0  # 최대길이
    for l in lst:
        l_len = length(l)  # 함수호출
        len_lst.append(l_len)  
        if max_len < l_len: 
            max_len = l_len  # 최대길이 갱신

    string = ''
    for i in range(max_len):
        for j in range(5):
            if i < len_lst[j]:   # out of index 에러 방지
                string += lst[j][i]

    print(f'#{test_case} {string}')
