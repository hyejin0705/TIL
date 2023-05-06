import sys

n, m = map(int, sys.stdin.readline().split())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

array.sort()
result = sys.maxsize
start, end = 0, 0

while start < n and end < n:
    diff = array[end] - array[start]
    if diff < m:
        end += 1
    else:
        result = min(result, diff)
        start+= 1

print(result)