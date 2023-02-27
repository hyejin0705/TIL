## 주어지는 수가 커졌기 때문에, bfs방식보다는 DP방식으로 풂.
## 하지만, dp 알고리즘을 리스트 형식으로 풀었더니, 메모리 초과 발생

## 해결방안으로 딕셔너리(해쉬 테이블)형태로 풀이방식 변경 >>> 해결완료!

import sys
x = int(sys.stdin.readline())

dp = {1 : 0}  # 값이 크기 때문에, 딕셔너리 형태 사용

def rec(n):
    # 종료조건
    if n in dp.keys():
        return dp[n]
    
    # 3의 배수, 2의 배수인 경우
    if not n % 3 and not n % 2:
        dp[n] = min(rec(n//3) + 1, rec(n//2) + 1)
    
    # 3의 배수인 경우
    elif not n % 3:
        dp[n] = min(rec(n//3) + 1, rec(n - 1) + 1)
    
    # 2의 배수인 경우
    elif not n % 2:
        dp[n] = min(rec(n//2) + 1, rec(n - 1) + 1)
    
    # 3의 배수, 2의 배수가 아닌 경우
    else:
        dp[n] = rec(n - 1) + 1
    
    return dp[n]

print(rec(x))


# # ---------------------------------------------------------------
# # dp알고리즘 리스트 형식 >>> 메모리 초과

# N = int(10e8)

# dp = [0] * (N + 1)
# dp[1] = dp[2] = dp[3] = 1

# for i in range(4, N + 1):
#     dp[i] = dp[i - 1] + 1
#     if not i % 2:
#         dp[i] = min(dp[i], dp[i // 2] + dp[2])
#     elif not i % 3:
#         dp[i] = min(dp[i], dp[i // 3] + dp[3])

# print(dp[N])
