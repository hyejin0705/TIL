import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

check = list(map(int, sys.stdin.readline().split()))

dic = {num: 0 for num in check}

for num in lst:
    if num in dic.keys():
        dic[num] += 1

for num in check:
    if num in dic.keys():
        print(dic[num], end=' ')
print()