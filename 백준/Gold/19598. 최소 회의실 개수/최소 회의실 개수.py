import sys
import heapq

n = int(sys.stdin.readline().rstrip())  #회의 갯수 n

con = []  # 회의
for x in range(n) :
  start, end = map(int, sys.stdin.readline().split())
  con.append([start, end])  #시작시간, 끝나는시간 넣어주기

con.sort()  #정렬

rooms = []
heapq.heappush(rooms, con[0][1])  # 가장 첫 회의의 끝나는 시간을 넣어줌

for y in range(1,n):  # 첫 요소는 썼으니 1부터 시작
  if con[y][0] < rooms[0] : # 시작 시간이 현재 회의 끝나는 시간보다 빠르면
    heapq.heappush(rooms, con[y][1])  #끝나는 시간을 넣어줌(회의실+1)
  else:  # 시작 시간이 현재 회의 끝나는 시간보다 늦으면(이어서 쓸 수 있으면)
    heapq.heappop(rooms)  #이어하는 회의의 끝나는 시간으로 push
    heapq.heappush(rooms, con[y][1])

print(len(rooms))