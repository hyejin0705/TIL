# heapq는 최소힙 라이브러리이기 때문에,
# 최대힙을 사용하기 위해서는 약간의 트릭을 활용해야 한다.

# 원소를 넣을 때, (-item, item)의 튜플 형식으로 넣는다.
# 그러면, 앞의 원소인, 음수 값으로 최소힙 정렬을 해준다.
# 음수 값 최소힙 정렬 -> 양수 값은 최대힙 정렬!

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
        heapq.heappush(max_heap, (-T, T))