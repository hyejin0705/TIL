def dfs(n, ans):
    if n == N:
        if len(ans) == M:
            check.add(tuple(ans))
        return

    dfs(n + 1, ans + [lst[n]])
    dfs(n + 1, ans)


N, M = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort()

check = set()

dfs(0, [])

for i in sorted(list(check)):
    print(*i)