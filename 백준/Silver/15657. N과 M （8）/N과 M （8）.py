def dfs(cnt, n, lst):
    if cnt == M:
        print(*lst)
        return

    for i in range(n, N):
        lst.append(check[i])
        dfs(cnt + 1, i, lst)
        lst.pop()


N, M = map(int, input().split())

check = list(map(int, input().split()))

check.sort()

dfs(0, 0, [])