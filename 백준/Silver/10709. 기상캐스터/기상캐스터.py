def bfs(arr):
    que = []
    visited = [[-1] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if arr[i][j] == 'c':       # 'c'를 찾으면 que에 저장
                que.append((i, j))
                visited[i][j] = 0

    while que:
        i, j = que.pop(0)              # 'c'인 모든 방향에서 시작

        for di, dj in [[0, 1]]:        # 오른쪽으로 한 칸씩
            ni, nj = i + di, j + dj

            if nj < W and arr[ni][nj] != 'c':  # 범위 내이고, 구름이 없다면
                que.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1  # 방문표시 + 1

    return visited


H, W = map(int, input().split())

arr = [list(input()) for _ in range(H)]

visited = bfs(arr)   # 함수호출

for v in visited:
    print(*v)        # 한 행씩 출력