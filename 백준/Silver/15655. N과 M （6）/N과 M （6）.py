def dfs(n, lst):
    if n == N:
        if len(lst) == M:
            print(*lst)
        return

    dfs(n + 1, lst + [check[n]])
    dfs(n + 1, lst)


N, M = map(int, input().split())

check = list(map(int, input().split()))

check.sort()

dfs(0, [])