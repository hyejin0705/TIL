import sys

N, M = map(int, sys.stdin.readline().split())

arr = [[0] * (N + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

check = [[0] * (N + 1) for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        check[i][j] = check[i-1][j] + check[i][j-1] - check[i-1][j-1] + arr[i][j]

# print(arr)
# print(check)

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2:
        print(arr[x1][y1])
    else:
        ans = check[x2][y2] - check[x1-1][y2] - check[x2][y1-1] + check[x1-1][y1-1]
        print(ans)