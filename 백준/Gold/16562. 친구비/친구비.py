import sys
input = sys.stdin.readline
INF = sys.maxsize
sys.setrecursionlimit(10**6)

def dfs(num):
    global money
    money = min(money, A[num])
    if len(graph[num]) == 0:
        return
    
    for go in graph[num]:
        if visited[go] == False:
            visited[go] = True
            dfs(go)

n, m, k = map(int, sys.stdin.readline().split()) # 학생 수, 친구 관계수, 돈
A = [0] + list(map(int, sys.stdin.readline().split())) # 친구 비

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n + 1)
ans = 0
for i in range(1, n + 1):
    if not(visited[i]):
        visited[i] = True
        money = INF
        dfs(i)
        ans += money
        
if k >= ans:
    print(ans)
else:
    print("Oh no")