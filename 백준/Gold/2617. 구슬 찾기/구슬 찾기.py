import sys 
from collections import deque 

def DFS(x,graph):
    global cnt 
    for e in graph[x]:
        if not visited[e]:  # False면, 즉 첫 방문일때만
            visited[e] = True
            cnt += 1
            DFS(e, graph)


N, M = map(int, sys.stdin.readline().split())
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
mid = (N+1) / 2
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph1[b].append(a)
    graph2[a].append(b)
    

ans = 0
for i in range(1, N+1):
    cnt = 0
    visited = [False] * (N+1)
    DFS(i, graph1)
    if cnt >= mid:
        ans += 1
        
    cnt = 0
    DFS(i, graph2)
    if cnt >= mid:
        ans += 1

print(ans)