## 시간초과 해결하기 

import sys

N = int(input())

lst = list(map(int, sys.stdin.readline().split()))

lst2 = sorted(set(lst))

# lookup 테이블 생성
dic = {lst2[i]: i for i in range(len(lst2))}

for num in lst:
    print(dic[num], end=' ')
    # print(lst2.index(num), end=' ')    # 시간초과
    
print()


## ----------------------------------------------------------------
# 시간초과의 이유 -> 정렬의 문제라고 생각했지만, 정렬의 문제가 아니라
# 출력할 때의 문제였음

# 출력할 때, 내장함수 index를 이용해서 하면, 시간초과 발생
#  >>>  중복된 숫자가 많은 경우, 계속 함수를 사용하고 반복하는 경우가 생김.

# 해결방법 : lookup 테이블 생성하고 출력 (카운팅 정렬과 비슷한 시간절감 효과)


## -------------------------------------------------------------------
# 힙정렬 -> heapq 라이브러리 활용

# def heap_sort():
#     heap = []
#     for num in lst:
#         if num not in heap:
#             heapq.heappush(heap, num)

#     sorted_nums = []
#     while heap:
#         sorted_nums.append(heapq.heappop(heap))
#     return sorted_nums


# N = int(input())

# lst = list(map(int, sys.stdin.readline().split()))

# lst2 = heap_sort()

# for num in lst:
#     print(lst2.index(num), end=' ')          # index 활용 -> 시간초과의 원인
# print()
