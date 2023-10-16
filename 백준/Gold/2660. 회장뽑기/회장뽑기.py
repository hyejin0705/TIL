import sys

def bfs(v):
    q = [v]
    visited = [False] * (N + 1)
    visited[v] = True
    level = 0
    while q:
        for _ in range(len(q)):
            v = q.pop(0)
            for e in adj[v]:
                if not(visited[e]):
                    visited[e] = True
                    q.append(e)
        if q:
            level += 1
    return level

N = int(sys.stdin.readline())

leader = []
leader_score = 100
adj = [[] for _ in range(N+1)]
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, N+1):
    score = bfs(i)
    if score < leader_score:
        if leader:
            leader = []
        leader.append(i)
        leader_score = score
    elif score == leader_score:
        leader.append(i)
print(leader_score, len(leader))
leader.sort()
for e in leader:
    print(e, end=" ")