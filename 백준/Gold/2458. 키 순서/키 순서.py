import sys

def dfs(now, idx):
    for pre in arr[idx]:
        if not v[now][pre]:
            v[now][pre] = 1
            v[pre][now] = 1
            dfs(now, pre)


N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    p, c = map(int, sys.stdin.readline().split())
    arr[p].append(c)

v = [[0] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    v[i][i] = 1
    dfs(i, i)

answer = sum([1 if sum(v[i]) == N else 0 for i in range(1, N+1)])
print(answer)