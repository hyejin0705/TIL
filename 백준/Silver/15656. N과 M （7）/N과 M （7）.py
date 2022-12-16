def dfs(n, lst):
    if n == M:
        print(*lst)
        return

    for i in range(N):
        lst.append(check[i])
        dfs(n + 1, lst)
        lst.pop()


N, M = map(int, input().split())

check = list(map(int, input().split()))

check.sort()

dfs(0, [])