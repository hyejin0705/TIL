import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = 1e10

def bfs(y, x):
    global ans
    
    dq = deque()
    dq.append((y, x))
    visited[y][x] = 1
    
    while dq:
        y, x = dq.popleft()
        if y == N-1 and x == M-1:
            ans = min(ans, visited[y][x])
            
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if not (0 <= ny < N and 0 <= nx < M):
                continue
                
            if not visited[ny][nx]:
                # 0인 곳을 먼저 방문 해준다.
                if board[ny][nx] == 0:
                    dq.appendleft((ny, nx))
                    visited[ny][nx] = visited[y][x]
                
                elif board[ny][nx] == 1:
                    dq.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1

bfs(0, 0)
print(ans - 1)