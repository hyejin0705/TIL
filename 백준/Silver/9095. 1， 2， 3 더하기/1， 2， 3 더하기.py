N = int(input())

dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 12):
    dp[i] = sum(dp[i-3:])

for _ in range(N):
    print(dp[int(input())])