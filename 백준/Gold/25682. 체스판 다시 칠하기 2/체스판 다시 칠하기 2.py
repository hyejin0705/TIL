import sys

n, m, k = map(int, sys.stdin.readline().split())
T = [list(str(sys.stdin.readline().rstrip())) for _ in range(n)]

def solve(color): # 1행 1열의 색이 color인 것을 조사
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                if T[i][j] != color: # 1행 1열의 색이 color인 것은 T[i][j]의 값이 color 가 나와야 하는데
                    value = 1  # 안나오면 패널티로 value 1을 준다.
                else:
                    value = 0 # 정상적이면 pass
            
            else:
                if T[i][j] == color: #1행 1열의 색이 color일때 color 반대 값이 나와야 하는데 color가 나왔으므로
                    value = 1 # 패널티로 value 1을 준다.
                
                else:
                    value = 0
            
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + value # 누적 패널티 적립
    
    target = n * m # 최대 패널티 점수 모두 1점을 얻어서 n*m일 것이다.
    for i in range(1, n - k + 2): #우리는 kXk 행렬의 점수만 궁금하므로 dp를 공부했으면 다음과 같은 식은 쉬울 것이다.(누적에서 빼는 것)
        for j in range(1, m - k + 2):
            target = min(target, dp[i + k - 1][j + k - 1] - dp[i + k - 1][j - 1] - dp[i - 1][j + k - 1] + dp[i - 1][j - 1])
    return target            
                
print(min(solve('B'), solve('W'))) # 적게 틀린 값을 찾으면 된다.