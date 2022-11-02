## 1927. 최소힙
## 11279. 최대힙

## 최대힙 응용
## 음수일 때, 양수로 고치고 heap에 추가
## 작은 수부터 꺼내면, 동순위일 경우 작은 값부터 pop

import sys
import heapq

N = int(input())

max_heap = []
for _ in range(N):
    T = int(sys.stdin.readline())
    if T == 0:
        if not max_heap:
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    else:
        if T < 0:
            heapq.heappush(max_heap, (-T, T))
        else:
            heapq.heappush(max_heap, (T, T))