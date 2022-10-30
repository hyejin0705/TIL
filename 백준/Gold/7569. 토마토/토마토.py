## 앞서 푼 7576. 토마토 문제와 비슷하지만, 2차원을 3차원으로 바꿔서 생각해야 함.

## 3차원으로 변경하면서, 문제에서의 H와 N의 개념이 헷갈려서 정답을 도출하는데 시간이 걸림.ㅜㅜ

## 높이 H : 상자의 높이
## 행 N : 상자의 행

## 둘을 바꿔서 생각(행 H, 높이 N)함.

import sys
from collections import deque

def bfs():
    ans = 1         # 리턴 값이 -1이기 때문에 초기값 설정 1로 함. ( 처음부터 모든 토마토가 존재했다면, 0 출력)
    q = deque()

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:      # 토마토가 존재한다면, 인큐
                    q.append([h, i, j])

    while q:
        sh, si, sj = q.popleft()       

        for dh, di, dj in [[0, 1, 0], [0, -1, 0], [0, 0, 1], [1, 0, 0], [0, 0, -1], [-1, 0, 0]]:   # 6방향

            nh, ni, nj = sh + dh, si + di, sj + dj

            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and not arr[nh][ni][nj]:   # 범위 내이고, 토마토가 익지 않았다면,
                arr[nh][ni][nj] = arr[sh][si][sj] + 1      # day 1 증가
                q.append([nh, ni, nj])                 # 인큐
                ans = arr[nh][ni][nj]              # 마지막 날 저장.

    return ans - 1


# M: 상자의 가로 칸의 수
# N: 상자의 세로 칸의 수
# H: 상자의 수

M, N, H = map(int, input().split())

arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

ans = bfs()

# H와 N의 위치 잊지 않기
# arr[H][N][M]

for h in range(H):
    for i in range(N):
        if 0 in arr[h][i]:     # 익지 않은 토마토가 존재하면, -1 출력
            ans = -1
            break

print(ans)
