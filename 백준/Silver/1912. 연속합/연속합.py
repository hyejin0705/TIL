import sys

N = int(input())

lst = list(map(int, sys.stdin.readline().split()))

d = [0] * N

d[0] = lst[0]
for i in range(1, N):
    d[i] = max(lst[i], d[i-1] + lst[i])

print(max(d))