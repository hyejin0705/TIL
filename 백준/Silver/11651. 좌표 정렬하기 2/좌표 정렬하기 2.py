import sys

N = int(input())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr.sort(key=lambda x: [x[1], x[0]])

for lst in arr:
    print(*lst)