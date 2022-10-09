def dfs(s):
    dfs_result.append(s)
    stk = []

    while True:
        adj[s].sort()      # 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
        for e in adj[s]:
            if e not in dfs_result:   # 미방문지라면,
                stk.append(s)         # 방문할 곳으로 체크

                s = e                 # 방문할 곳 갱신
                dfs_result.append(s)  # 방문 표시
                break

        else:
            if stk:
                s = stk.pop()

            else:
                break


def bfs(s):
    bfs_result.append(s)
    q = [s]

    while q:
        i = q.pop(0)

        adj[i].sort()      # 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
        for w in adj[i]:
            if w not in bfs_result:   # 미방문지라면,
                bfs_result.append(w)  # 방문 표시
                q.append(w)           # 방문할 곳으로 체크


V, E, S = map(int, input().split())

adj = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


dfs_result = []
bfs_result = []

dfs(S)
bfs(S)

print(*dfs_result)
print(*bfs_result)