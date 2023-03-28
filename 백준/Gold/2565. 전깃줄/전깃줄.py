import sys

n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m.sort(key=lambda x: x[0]) # 0번째 idx를 기준으로 오름차순 정렬
dp = [0] * n

# 반복문을 통해 가장 길게 증가하는 부분 수열을 찾는다.
for i in range(n):
    result_max = 0
    for j in range(i):
        # 0번째 idx를 기준으로 오름차순 정렬을 했기 때문에
        # 1번째 idx를 기준으로 증가하는 부분 수열을 찾는다.
        if m[i][1] > m[j][1]:
            if result_max < dp[j]:
                result_max = dp[j]

    dp[i] = result_max + 1

print(n - max(dp))