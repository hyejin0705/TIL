T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))

    mx_cnt = 0
    cnt = 0
    for i in range(N):
        if lst[i] == 1:
            cnt += lst[i]
            if cnt > mx_cnt:
                mx_cnt = cnt
        else:
            cnt = 0

    print(f'#{test_case} {mx_cnt}')
