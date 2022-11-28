import sys

N = int(input())

lst = list(map(int, sys.stdin.readline().split()))

dic = {num: 1 for num in lst}


M = int(input())

check = list(map(int, sys.stdin.readline().split()))

for ch in check:
    print(dic.get(ch, 0))