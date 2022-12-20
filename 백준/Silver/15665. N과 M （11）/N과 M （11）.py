def dfs(n, ans):
    if n == M:
        check.add(tuple(ans))
        return

    for i in range(N):
        ans.append(lst[i])
        dfs(n + 1, ans)
        ans.pop()


N, M = map(int, input().split())

lst = list(map(int, input().split()))

check = set()

dfs(0, [])

for i in sorted(list(check)):
    print(*i)