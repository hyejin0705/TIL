import sys
import heapq

N = int(sys.stdin.readline().rstrip())
my_list = []
for _ in range(N) :
    heapq.heappush(my_list, int(sys.stdin.readline().rstrip()))

answer = 0
while len(my_list) != 1 :
    a = heapq.heappop(my_list)
    b = heapq.heappop(my_list)
    
    heapq.heappush(my_list, a + b)
    answer += (a + b)
    
    if len(my_list) == 1 :
        break

print(answer)