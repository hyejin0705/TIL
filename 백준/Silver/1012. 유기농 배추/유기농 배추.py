def bfs():
    v = [[0] * M for _ in range(N)]
    cnt = 0

    while q:
        i, j = q.pop(0)

        if not v[i][j]:
            que2 = [[i, j]]
            cnt += 1

            while que2:
                si, sj = que2.pop(0)

                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = si + di, sj + dj

                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not v[ni][nj]:
                        v[ni][nj] = 1
                        que2.append([ni, nj])

    return cnt


N = int(input())

for _ in range(N):
    # 가로길이 : M, 세로길이: N, 배추 개수: K
    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]

    q = []

    for _ in range(K):
        j, i = map(int, input().split())
        q.append([i, j])
        arr[i][j] = 1

    ans = bfs()

    print(ans)