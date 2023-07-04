import sys, heapq

n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    
    graph[a].append((b,c))
    graph[b].append((a,c))
    
start,end = map(int, sys.stdin.readline().split())

dist = [float('inf')] * (n+1)
dist[start] = 0
hq = [(0, start)] # 순서 중요. 가중치가 앞으로
ans = 0

while hq:
    curDist, curNode = heapq.heappop(hq)
    
    if curNode == end:
        ans = curDist
        break
        
    for toNode, toDist in graph[curNode]:
        totalDist = curDist + toDist
        
        if totalDist >= dist[toNode]:
            continue
            
        dist[toNode] = totalDist
        heapq.heappush(hq, (totalDist, toNode))

print(ans)
