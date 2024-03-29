import sys
 
N, M = map(int, sys.stdin.readline().split())
time = [int(sys.stdin.readline()) for _ in range(N)]
result = 0
left = 0
right = M * max(time)
 
while left <= right:
    mid = (left + right) // 2
 
    judgedPeople = 0
    for t in time:
        judgedPeople += mid // t
    
    if judgedPeople < M:
        left = mid + 1
    else:
        result = mid
        right = mid - 1
 
print(result)