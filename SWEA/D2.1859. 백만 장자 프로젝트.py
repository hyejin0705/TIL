def mx(lst, idx):
    max_num = max_idx = 0
    for i in range(idx, N):
        if max_num <= lst[i]:
            max_num = lst[i]
            max_idx = i
    return max_num, max_idx


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    idx = result = 0
    while idx < N:
        mx(lst, idx) = max_num, max_idx

        days = (max_idx - 1) - idx

        sell = 0
        for i in range(idx, max_idx):
            sell += lst[i]

        result += max_num * days - sell

        idx += max_idx + 1

    print(f'#{test_case} {result}')
