def check(lst1, lst2, M):
    for lst in [lst1, lst2]:
        for arr in lst:
            for idx in range(N - M + 1):
                result = arr[idx: idx + M]
                if result == result[::-1]:
                    return M
 
T = 10
N = 100
for test_case in range(1, T+1):
    _ = int(input())
 
    lst1 = [list(input()) for _ in range(N)]
    lst2 = list(zip(*lst1))
 
    for M in range(2, 100):
        num = check(lst1, lst2, M)
        if num:
            max_len = num
 
    print(f'#{test_case} {max_len}')
