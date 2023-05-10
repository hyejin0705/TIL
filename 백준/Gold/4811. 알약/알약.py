def solve(w, h):
    if dp[w][h] != -1: # 이미 계산한 경우에는 그대로 리턴 
        return dp[w][h]
    dp[w][h] = 0

    if w == 0: # H만 남았을 경우에는 남은 H를 모두 사용하여 만드는 문자 하나의 경우만 존재
        dp[w][h] = 1
        return dp[w][h]
    if h < 0: # H가 음수 개 되는 경우는 없기 때문에 0을 리턴 
        return 0

    # W를 사용한 경우 + H를 사용한 경우 
    dp[w][h] = solve(w - 1, h + 1) + solve(w, h - 1)
    return dp[w][h]


# dp[w][h] : W가 w개 있고 H가 h개 있을 때 만들 수 있는 문자열 경우의 수 
dp = [[-1] * 31 for _ in range(31)] 

while True:
    N = int(input())

    if N == 0:
        break

    # 문자열의 첫 번째 문자는 항상 W가 오기 때문에 N - 1개가 된다.
    # 알약 하나를 반으로 쪼갠 후 하나를 집어 넣기 때문에 초기 H의 개수는 1이 된다.
    print(solve(N - 1, 1))