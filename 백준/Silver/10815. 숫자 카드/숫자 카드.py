import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))

dic = {}
for num in lst:
    dic[num] = 1

for num in lst2:
    print(dic.get(num, 0), end=' ')
print()