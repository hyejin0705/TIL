import sys
import heapq

N = int(input())

heap = []
for _ in range(N):
    T = int(sys.stdin.readline())

    if T == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, T)