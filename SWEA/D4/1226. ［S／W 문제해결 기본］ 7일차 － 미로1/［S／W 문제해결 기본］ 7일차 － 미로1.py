def bfs(si, sj, G):
    global visited
    visited = [[0] * N for _ in range(N)]
    que = []

    que.append((si, sj))
    visited[si][sj] = 1

    while que:
        i, j = que.pop(0)

        if arr[i][j] == G:
            return

        # 4방향 탐색
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj

            # 범위 내이고, 미방문했고, 벽이 아니라면,
            if not visited[ni][nj] and arr[ni][nj] != 1:
                que.append((ni, nj))
                visited[ni][nj] = 1
    return


T = 10

for test_case in range(1, T + 1):
    _ = int(input())

    N = 16

    arr = [list(map(int, input())) for _ in range(N)]

    for idx in range(N):
        if 2 in arr[idx]:
            sj = arr[idx].index(2)
            si = idx

        if 3 in arr[idx]:
            ej = arr[idx].index(3)
            ei = idx

    visited = [[0] * N for _ in range(N)]

    # 출발은 2, 도착은 3
    bfs(si, sj, 3)

    print(f'#{test_case} {visited[ei][ej]}')