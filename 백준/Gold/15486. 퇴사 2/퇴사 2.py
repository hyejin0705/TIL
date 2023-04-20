import sys

n = int(input())
T = [0]*(n+2)
P = [0]*(n+2)
dp = [0]*(n+2)
for i in range(1,n+1):
    T[i],P[i] = map(int,sys.stdin.readline().split())

for i in range(1,n+1):
    if(i+T[i] <= n+1):
        dp[i+T[i]] = max(dp[i+T[i]],dp[i]+P[i])
    dp[i+1] = max(dp[i+1],dp[i])

print(max(dp))