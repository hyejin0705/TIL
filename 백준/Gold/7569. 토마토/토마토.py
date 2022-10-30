import sys
from collections import deque

def bfs():
    ans = 1
    q = deque()

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:
                    q.append([h, i, j])

    while q:
        sh, si, sj = q.popleft()

        for dh, di, dj in [[0, 1, 0], [0, -1, 0], [0, 0, 1], [1, 0, 0], [0, 0, -1], [-1, 0, 0]]:

            nh, ni, nj = sh + dh, si + di, sj + dj

            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and not arr[nh][ni][nj]:
                arr[nh][ni][nj] = arr[sh][si][sj] + 1
                q.append([nh, ni, nj])
                ans = arr[nh][ni][nj]

    return ans - 1


# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수
M, N, H = map(int, input().split())

arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

ans = bfs()

for h in range(H):
    for i in range(N):
        if 0 in arr[h][i]:
            ans = -1
            break

print(ans)