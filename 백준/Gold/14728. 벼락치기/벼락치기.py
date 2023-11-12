import sys

n, t = map(int, sys.stdin.readline().split())
dp = [0] * (t+1)
    
for _ in range(n):
    k, s = map(int, sys.stdin.readline().split())
    for i in range(t, -1, -1):
        if i >= k:
            dp[i] = max(dp[i], dp[i-k] + s)
            
print(dp[t])