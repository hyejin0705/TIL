import sys

n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

diff = [[0] * n for _ in range(n)]
for i in range(n):
    max_n, min_n = -1, 1e10

    for j in range(i,-1,-1):
        if max_n < scores[j]: 
            max_n = scores[j]
        if min_n > scores[j]: 
            min_n = scores[j]
        
        diff[i][j] = max_n - min_n
        
dp = [0] * n
max_n, min_n = -1, 1e10

for i in range(n):
    if scores[i] > max_n: 
        max_n = scores[i]
    if scores[i] < min_n: 
        min_n = scores[i]
    
    dp[i] = max_n - min_n

    for j in range(i):
        if dp[i] < dp[j] + diff[i][j+1]:
            dp[i] = dp[j] + diff[i][j+1]

print(dp[n-1])