import sys

n = int(sys.stdin.readline())
max_dp = [0 for _ in range(3)]
min_dp = [0 for _ in range(3)]
max_tmp = [0 for _ in range(3)]
min_tmp = [0 for _ in range(3)]

# 반복문을 통해 각 줄을 확인
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split()) # 3칸의 수

    # 반복문을 통해 각 칸의 들어갈 수 있는 최대/최소 값을 구한다.
    for j in range(3):
        if j == 0:
            max_tmp[j] = max(max_dp[j], max_dp[j + 1]) + a
            min_tmp[j] = min(min_dp[j], min_dp[j + 1]) + a

        elif j == 1:
            max_tmp[j] = max(max_dp[j], max_dp[j - 1], max_dp[j + 1]) + b
            min_tmp[j] = min(min_dp[j], min_dp[j - 1], min_dp[j + 1]) + b

        else:
            max_tmp[j] = max(max_dp[j], max_dp[j - 1]) + c
            min_tmp[j] = min(min_dp[j], min_dp[j - 1]) + c

    # 각 칸의 들어갈 수 있는 최대/최소 값을 max_dp/min_dp에 초기화
    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]


print(max(max_dp), min(min_dp))