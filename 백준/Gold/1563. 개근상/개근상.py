import sys
input = sys.stdin.readline

N = int(input())

DP_0 = [[0] * 4 for _ in range(N)]  # 지각 0번
DP_1 = [[0] * 3 for _ in range(N)]  # 지각 1번

# 출석, 결석1, 결석2, 지각
DP_0[0] = [1, 1, 0, 1]

k = 1000000
for i in range(1, N):
    DP_0[i][0] = (DP_0[i-1][0] + DP_0[i-1][1] + DP_0[i-1][2]) % k
    DP_0[i][1] = (DP_0[i-1][0]) % k
    DP_0[i][2] = (DP_0[i-1][1]) % k
    DP_0[i][3] = (DP_0[i-1][0] + DP_0[i-1][1] + DP_0[i-1][2]) % k

    DP_1[i][0] = (DP_0[i-1][3] + DP_1[i-1][0] + DP_1[i-1][1] + DP_1[i-1][2]) % k
    DP_1[i][1] = (DP_0[i-1][3] + DP_1[i-1][0]) % k
    DP_1[i][2] = (DP_1[i-1][1]) % k

print((sum(DP_0[N-1]) + sum(DP_1[N-1])) % k)