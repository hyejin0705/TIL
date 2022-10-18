T = int(input())

for test_case in range(1, T + 1):
    _, *lst = list(map(int, input().split()))

    ans = 0
    for idx in range(1, len(lst)):   # 2번째 순서부터 시작.
        for i in range(idx):         # 앞사람이 키가 크면, 자리 바꾸기
            if lst[i] > lst[idx]:
                lst[i], lst[idx] = lst[idx], lst[i]
                ans += 1             # 자리를 바꿀 때마다 count

    print(test_case, ans)