s = list(input().strip())
length = len(s)
dp = [0 for i in range(length + 1)]
dp[0], dp[1] = 1, 1

if s[0] == "0":
    print(0)
else:
    for i in range(2, length + 1):
        if int(s[i - 1]) > 0:
            dp[i] += dp[i - 1]
        num = int(s[i - 1]) + int(s[i - 2]) * 10
        if 10 <= num <= 26:
            dp[i] += dp[i - 2]
    print(dp[length] % 1000000)