import sys

def dfs(v, depth):

    # 친구 관계가 존재한다면 1출력 후 종료
    if depth == 4:
        print(1)
        exit()

    # 반복문을 통해 친구 관계 확인
    for j in graph[v]:
        # 탐색하지 않은 친구라면
        if not visited[j]:
            visited[j] = True
            dfs(j, depth + 1) # 백 트래킹을 통해 깊이 확인
            visited[j] = False


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 반복문을 통해 각 친구들의 친구관계를 확인
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

# 친구 관계가 존재하지 않으므로 0 출력
print(0)