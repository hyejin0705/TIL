N, M = map(int, input().split())

arr = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

check = [[0] * (M + 1)] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, M + 1):
        MAX = max(check[i-1][j], check[i][j-1])
        check[i][j] = arr[i][j] + MAX

print(check[N][M])