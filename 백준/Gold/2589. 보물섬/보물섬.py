import sys
from collections import deque


# bfs 탐색
def bfs(a, b):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[a, b]])

    while queue:
        x, y = queue.popleft()

        # 상/하/좌/우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고
            if 0 <= nx < l and 0 <= ny < w:
                # 탐색하지 않았으며 육지라면 탐색
                if not visited[nx][ny] and graph[nx][ny] == "L":
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])

    # 시작 육지에서 제일 먼 거리에 육지를 확인
    temp = 0
    for k in range(l):
        temp = max(temp, max(visited[k]))

    return temp


l, w = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(l)]
answer = []

# 반복문을 통해 모든 육지에서 갈 수 있는 육지의 거리를 확인
for i in range(l):
    for j in range(w):
        if graph[i][j] == "L":
            visited = [[0 for _ in range(w)] for _ in range(l)]
            visited[i][j] = 1 # 처음 육지 탐색
            answer.append(bfs(i, j)) # 각 육지에서 제일 먼 거리에 육지를 저장

# 제일 먼 육지에서 -1
print(max(answer) - 1)