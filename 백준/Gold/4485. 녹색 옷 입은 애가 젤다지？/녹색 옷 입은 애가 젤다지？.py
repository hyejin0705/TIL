import sys
import heapq as hq
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
index = 1

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    heap = list()
    visited[0][0] = True
    # 잃는 소지금이 적을 수록 우선 순위가 높음
    hq.heappush(heap, (a[0][0], 0, 0))
    while heap:
        cost, tx, ty = hq.heappop(heap)
        # 마지막 좌표에 도달하면 끝
        if tx == N-1 and ty == N-1:
            print("Problem %d: %d" % (index, cost))
            break
        for k in range(4):
            x = tx + dx[k]
            y = ty + dy[k]
            if 0 <= x < N and 0 <= y < N and not visited[x][y]:
                visited[x][y] = True
                hq.heappush(heap, (cost + a[x][y], x, y))
    index += 1