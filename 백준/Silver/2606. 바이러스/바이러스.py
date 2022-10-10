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


V = int(input())   # 정점의 개수
E = int(input())   # 간선의 개수

adj = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


bfs_result = []

bfs(1)    # 1번부터 바이러스 탐색 시작
 
print(len(bfs_result) - 1)   # 1번이 포함되어 있기 때문에 -1