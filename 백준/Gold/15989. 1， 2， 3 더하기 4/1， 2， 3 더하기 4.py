import sys

t = int(sys.stdin.readline())
dp = [1 for i in range(10001)] # 1로만 표현하는 것은 무조건 존재하므로 1부터 시작
nums = [int(sys.stdin.readline()) for _ in range(t)]

for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]
    
for i in nums:
    print(dp[i])