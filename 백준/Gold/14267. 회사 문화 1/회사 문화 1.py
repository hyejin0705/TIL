import sys

n, m = map(int, sys.stdin.readline().split())
superior = list(map(int, sys.stdin.readline().split()))
ans = list(0 for _ in range(n+1))

for _ in range(m):
    i, w = map(int, sys.stdin.readline().split())
    ans[i] += w
    
for i in range(2, n + 1):
    ans[i] += ans[superior[i-1]]    
    
ans.pop(0)           
print(*ans)