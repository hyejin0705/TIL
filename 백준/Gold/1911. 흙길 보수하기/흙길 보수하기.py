import sys

n, l = map(int, sys.stdin.readline().split())
holes = []
for _ in range(n):
    holes.append(list(map(int, sys.stdin.readline().split())))
    
holes.sort(key=lambda holes: holes[0])

cur = 0
cnt = 0
for start, end in holes:
    if cur > start:
        start = cur
    while start < end:
        start += l
        cnt += 1
    cur = start
print(cnt)