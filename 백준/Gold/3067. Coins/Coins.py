T = int(input())
for _ in range(T):
    n = int(input())
    coins = list(map(int, input().rsplit()))
    ans = int(input())

    # dp[i] = i원 동전을 이용해 j원을 만들 수 있는 경우의 수
    dp = [0 for _ in range(ans+1)]
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], ans+1):
            dp[j] += dp[j-coins[i]]

    print(dp[ans])