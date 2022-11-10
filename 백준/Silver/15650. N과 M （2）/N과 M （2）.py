def dfs(n, lst):
    if n == N + 1:
        if len(lst) == M:
            print(*lst)
        return

    dfs(n + 1, lst + [n])
    dfs(n + 1, lst)


N, M = map(int, input().split())

dfs(1, [])