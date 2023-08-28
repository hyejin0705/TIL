import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n - i):
        if arr[j] == arr[j + i]:
            if i < 2:
                dp[j][i + j] = 1
            elif dp[j + 1][i + j - 1] == 1:
                dp[j][i + j] = 1
           

r = int(input())
for _ in range(r):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a - 1][b - 1])