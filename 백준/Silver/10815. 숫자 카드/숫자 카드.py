## list보다는 dict가 더 빠름.

import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))

dic = {}          # 속도는 dictionary!
for num in lst:
    dic[num] = 1  # 숫자카드 존재하면, 1 저장

for num in lst2:
    print(dic.get(num, 0), end=' ')  # 숫자카드.get(숫자, 없으면 0)
print()


## -----------------------------------------------------------------
## 시간초과

# import sys

# N = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))

# M = int(sys.stdin.readline())
# lst2 = list(map(int, sys.stdin.readline().split()))

# for num in lst2:
#     if num in lst:
#         print(1, end=' ')
#         continue
#     print(0, end=' ')
# print()
