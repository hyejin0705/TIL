def dfs(cnt, n, lst):
    if cnt == M:
        print(*lst)
        return

    for i in range(n, N + 1):
        lst.append(i)
        dfs(cnt + 1, i, lst)
        lst.pop()


N, M = map(int, input().split())

dfs(0, 1, [])
