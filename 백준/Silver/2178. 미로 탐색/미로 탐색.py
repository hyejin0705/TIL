def bfs(i, j):
    q = [[i, j]]
    v[i][j] = 1

    while q:
        si, sj = q.pop(0)

        if (si, sj) == (N, M):
            return

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = si + di, sj + dj

            if 1 <= ni < N + 1 and 1 <= nj < M + 1 and not v[ni][nj] and arr[ni][nj]:
                v[ni][nj] = v[si][sj] + 1
                q.append([ni, nj])


N, M = map(int, input().split())

arr = [[0] * (M + 1)] + [[0] + list(map(int, input())) for _ in range(N)]

v = [[0] * (M + 1) for _ in range(N + 1)]

ans = (N + 1) * (M + 1)

bfs(1, 1)

print(v[N][M])