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