# 시간 축소를 위해 heapq 활용

import sys, heapq

N = int(input())

ans = []
for _ in range(N):
    check = list(map(int, sys.stdin.readline().split()))
    if not ans:
        for ch in check:
            heapq.heappush(ans, ch)

    else:
        for ch in check:
            if ans[0] < ch:
                heapq.heappush(ans, ch)
                heapq.heappop(ans)

print(ans[0])



# ----------------------------------------------------------------------------
# Time: 3636 ms, Memory: 121140 KB (pypy)

# 시간초과를 해결하기 위해 -> N개만 이용해서 계속 넣고, 빼고 정렬하고 반복함.
# python3에서는 시간초과
# pypy에서만 통과.
#-----------------------------------------------------------------------------

# N = int(input())

# ans = list(map(int, input().split()))
# ans.sort(reverse = True)
# for _ in range(1, N):
#     check = list(map(int, input().split()))
#     for j in range(N):
#         if min(ans) <= check[j]:
#             ans.append(check[j])
#             ans.sort(reverse=True)
#             ans.pop()

# print(ans[N-1])
