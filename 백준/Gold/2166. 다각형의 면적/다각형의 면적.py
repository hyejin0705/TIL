import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.append(arr[0])

x, y = 0,0
for i in range(n):
    x += arr[i][0] * arr[i+1][1]
    y += arr[i][1] * arr[i+1][0]
    
print(round(abs((x-y)/2),1))