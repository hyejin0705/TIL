import heapq
import sys

n = int(sys.stdin.readline())

# heapq를 사용하면, 오름차순 정렬 필요하지 않음...
# arr = [list(map(int, input().split())) for _ in range(n)]
# arr.sort(key = lambda x:x[1]) # 시작 시간으로 오름차순 정렬

heap = []
q = []
count = 0
for _ in range(n):
    num, start, end = map(int,sys.stdin.readline().split())
    
    # 시작시간으로 오름차순 정렬해야 하기 때문에, 배열 달리해서 넣기
    heapq.heappush(heap, [start,end,num])

classroom = []
start, end, num = heapq.heappop(heap)  # 첫 강의시간 가져오기
heapq.heappush(classroom, end)   # 끝나는 시간 넣기

while heap:
    start, end, num = heapq.heappop(heap)
    if classroom[0] <= start:     # 끝나는 시간이 시작시간보다 작다면, 
        heapq.heappop(classroom)  # 비교시간 빼기
    heapq.heappush(classroom, end)  # 다시 넣기
    
print(len(classroom))