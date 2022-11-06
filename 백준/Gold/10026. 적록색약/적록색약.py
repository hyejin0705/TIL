def bfs(arr):
    v = [[0] * N for _ in range(N)]
    q = []
    cnt = 0

    for i in range(N):
        for j in range(N):

            if not v[i][j]:
                v[i][j] = 1
                cnt += 1
                q.append([i, j])

                while q:
                    si, sj = q.pop(0)

                    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        ni, nj = si + di, sj + dj

                        if 0 <= ni < N and 0 <= nj < N and arr[si][sj] == arr[ni][nj] and not v[ni][nj]:
                            v[ni][nj] = 1
                            q.append([ni, nj])

    return cnt


# 적록색약
N = int(input())

arr = [list(input()) for _ in range(N)]

arr2 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr2[i][j] = 'R'

        else:
            arr2[i][j] = arr[i][j]

cnt = bfs(arr)      # 적록색약이 아닌 사람
cnt2 = bfs(arr2)    # 적록색약인 경우

print(cnt, cnt2)