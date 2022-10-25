def check(si, sj):
    for di, dj in [[-1, -1], [-1, 1]]:
        ni, nj = si + di, sj + dj
        while 0 <= ni < N and 0 <= nj < N:
            if chess[ni][nj]:
                return 0
            else:
                ni += di
                nj += dj

    else:
        return 1


def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if not v[j] and check(n, j):
            v[j] = chess[n][j] = 1
            dfs(n + 1)
            v[j] = chess[n][j] = 0


N = int(input())

chess = [[0] * N for _ in range(N)]

ans = 0

v = [0] * N

dfs(0)

print(ans)