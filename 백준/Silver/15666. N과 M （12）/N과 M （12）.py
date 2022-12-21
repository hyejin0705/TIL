def dfs(cnt, n, ans):
    if cnt == M:
        print(*ans)
        return

    for i in range(n, len(lst)):
        ans.append(lst[i])
        dfs(cnt + 1, i, ans)
        ans.pop()

N, M = map(int, input().split())

lst = sorted(list(set(map(int, input().split()))))

dfs(0, 0, [])
