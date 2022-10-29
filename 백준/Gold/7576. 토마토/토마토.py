import sys
from collections import deque

def bfs():
    ans = 1
    q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append([i, j])

    while q:
        si, sj = q.popleft()

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = si + di, sj + dj

            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
                arr[ni][nj] = arr[si][sj] + 1
                q.append([ni, nj])
                ans = arr[ni][nj]

    return ans - 1


# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수
M, N = map(int, input().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = bfs()

for i in range(N):
    if 0 in arr[i]:
        ans = -1
        break

print(ans)