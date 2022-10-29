## python 제출 : Time: 1956 ms, Memory: 106080 KB
## pypy 제출 : Time: 632 ms, Memory: 215180 KB

## 시간초과 오류 해결 : deque 라이브러리를 이용해서 시간 단축 
## (그냥 append, pop 사용하면, 시간초과)

import sys
from collections import deque

def bfs():
    ans = 1          # return 값이 ans -1 이기 때문에 초기값: 1로 지정
    q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:    # 토마토 존재하면, 인큐
                q.append([i, j])

    while q:
        si, sj = q.popleft()      # pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = si + di, sj + dj

            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
                arr[ni][nj] = arr[si][sj] + 1    # 전날 + 1 저장
                q.append([ni, nj])
                ans = arr[ni][nj]               # 마지막날 저장

    return ans - 1   # 마지막 날 - 1


# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수
M, N = map(int, input().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = bfs()

for i in range(N):
    if 0 in arr[i]:   # 익지 않은 토마토가 존재하면,
        ans = -1      # 실패
        break

print(ans)
