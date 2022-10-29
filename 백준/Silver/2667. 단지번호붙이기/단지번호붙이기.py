def bfs(i, j):
    q = [[i, j]]
    v[i][j] = 1
    cnt = 1

    while q:
        si, sj = q.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = si + di, sj + dj

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] and not v[ni][nj]:
                q.append([ni, nj])
                v[ni][nj] = 1
                cnt += 1

    return cnt


N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

v = [[0] * N for _ in range(N)]

ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j] and not v[i][j]:
            ans.append(bfs(i, j))

ans.sort()
# 디버깅: 각 단지내 집의 수를 오름차순으로 정렬

print(len(ans), *ans, sep='\n')
