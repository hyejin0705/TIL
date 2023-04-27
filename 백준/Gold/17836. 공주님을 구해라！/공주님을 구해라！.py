from sys import stdin
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    visited = [[-1] * M for _ in range(N)]
    visited[sr][sc] = 0
    Q = deque([(sr, sc)])
    gramTime = 0
    while Q:
        r, c = Q.popleft()
        if (r, c) == (N-1, M-1):    # 목적지까지 정상 도달
            if gramTime:
                return min(visited[r][c], gramTime)
            return visited[r][c]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):       # 격자 밖이면
                continue
            if A[nr][nc] == 1 or visited[nr][nc] > -1:  # 벽이거나 이미 방문했다면
                continue

            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))
            if A[nr][nc] == 2:      # 그람 구했다면 현 위치에서 목적지까지 직통시간 미리 구함
                gramTime = visited[nr][nc] + (abs(N-1-nr) + abs(M-1-nc))

    # 목적지까지 정상적으로 도달하지 못한 경우
    if gramTime:
        return gramTime
    return T + 1	# 실패한 경우로 처리

# main
N, M, T = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]

temp = bfs(0, 0)
if temp <= T:       # T시간 이내 도달
    print(temp)
else:
    print("Fail")