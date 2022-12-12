def dfs(n, lst):
    if n == M:
        print(*lst)
        return

    for i in range(1, N + 1):
        lst.append(i)
        dfs(n + 1, lst)
        lst.pop()


N, M = map(int, input().split())

dfs(0, [])