## 시간초과 해결하는 게 큰 문제!

## 1. heapq 라이브러리 활용
## 2. input도 라이브러리 활용 -> sys.stdin.readline()

import sys
import heapq        # 시간 단축 방법 1

N = int(input())

heap = []           # 힙 리스트 생성
for _ in range(N):
    T = int(sys.stdin.readline())    # 시간 단축 방법 2

    if T == 0:
        if not heap:      # 리스트가 비어 있다면, 0 출력
            print(0)
            
        else:
            print(heapq.heappop(heap))    # 요소가 존재한다면, heapq.heappop(리스트) -> 최소값 출력
            
    else:
        heapq.heappush(heap, T)    # heapq.heappush(리스트, 요소)   ->  리스트에 요소 추가
         
        
        
## -------------------------------------------------
## 최소힙을 적용하지 않고 문제를 곧이곧대로 풀이한 코드

# N = int(input())

# lst = []
# for _ in range(N):
#     T = int(input())

#     if T == 0:
#         if not lst:
#             print(0)

#         else:
#             lst.sort()
#             print(lst.pop(0))

#     else:
#         lst.append(T)
