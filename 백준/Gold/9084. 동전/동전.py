T = int(input())
for _ in range(T):

    n = int(input())
    s = list(map(int,input().split()))
    goal = int(input())

    dp = [0 for i in range(goal+1)]
    dp[0] = 1
    for i in s:
        for j in range(1,goal+1):
            if j - i >= 0:
                dp[j] += dp[j-i]

    print(dp[goal])