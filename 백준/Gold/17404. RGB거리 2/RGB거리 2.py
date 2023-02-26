N = int(input())
INF = 10e9
arr = [list(map(int, input().split())) for _ in range(N)]

ans = INF
for i in range(3):
    # 새로운 배열 생성
    dp = [[INF, INF, INF] for _ in range(N)]

    # 첫번째 집 색깔 지정해주기
    dp[0][i] = arr[0][i]

    # 나머지 집 색 지정하기
    for j in range(1, N):
        # red
        dp[j][0] = arr[j][0] + min(dp[j-1][1], dp[j-1][2])
        # Green
        dp[j][1] = arr[j][1] + min(dp[j-1][0], dp[j-1][2])
        # Blue
        dp[j][2] = arr[j][2]+ min(dp[j-1][0], dp[j-1][1])
    
    # 마지막 인덱스랑 첫번째 인덱스랑 다른지 확인하기
    for k in range(3):
        if i != k:
            ans = min(ans, dp[N-1][k])   # 최소값 갱신.

print(ans)