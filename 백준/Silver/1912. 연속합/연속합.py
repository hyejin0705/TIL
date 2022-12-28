# 모든 연속된 수들의 합을 구해서 비교할 필요 없음.
# 다음에 음수가 나오면, 최대값이 될 수 없기 때문에, 앞의 누적합만 알면 됨.
import sys

N = int(input())

lst = list(map(int, sys.stdin.readline().split()))

d = [0] * N

d[0] = lst[0]
for i in range(1, N):
    d[i] = max(lst[i], d[i-1] + lst[i])

print(max(d))


# # -------------------------------------------------
# # 단순한 풀이법 (이중 for문) >>> 시간초과

# N = int(input())

# lst = list(map(int, sys.stdin.readline().split()))

# MAX = -1000
# for i in range(N):
#     total = 0
#     for j in range(i, N):
#         total += lst[j]
#         MAX = max(MAX, total)

# print(MAX)
