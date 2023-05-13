def dijkstra(start):
    distance[start] = 0 
    q = []
    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if distance[x[0]] > cost:
                heapq.heappush(q, [cost, x[0]])
                distance[x[0]] = cost

import sys, heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

INF = int(1e9)
distance = [INF for _ in range(n+1)]

dijkstra(1)

print(distance[n])