def dfs(n, lst):
    if n == N + 1:
        if len(lst) == M:
            print(*lst)
        return

    dfs(n + 1, lst + [arr[n]])
    dfs(n + 1, lst)


M = 6

while True:
    arr = list(map(int, input().split()))
    N = arr[0]

    if not N:   # 0이 나오면 종료
        break

    dfs(1, [])

    print()