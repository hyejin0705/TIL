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