def solution(n):
    sequence = list(map(int, input().split()))
 
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0], dp[0][1] = sequence[0], sequence[0]
 
    res = sequence[0]
 
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0] + sequence[i], sequence[i])
        dp[i][1] = max(dp[i-1][1] + sequence[i], dp[i-1][0])
        res = max(dp[i][0], dp[i][1], res)
 
    return res
 

N = int(input())
print(solution(N))