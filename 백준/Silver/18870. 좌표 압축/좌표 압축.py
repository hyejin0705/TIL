import sys

N = int(input())

lst = list(map(int, sys.stdin.readline().split()))

lst2 = sorted(set(lst))

dic = {lst2[i]: i for i in range(len(lst2))}
for num in lst:
    print(dic[num], end=' ')
print()