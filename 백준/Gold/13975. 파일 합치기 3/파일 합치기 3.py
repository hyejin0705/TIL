import sys
import heapq

n = int(sys.stdin.readline().rstrip())  # n번의 연산

for i in range(n) :
  length = int(sys.stdin.readline().rstrip()) # 카드 갯수의 길이
  cards = list(map(int, sys.stdin.readline().split()))  # 카드 받아오기

  heapq.heapify(cards)

  cnt = 0

  for j in range(length-1):  # 길이보다 한 번 적게 연산
    temp = heapq.heappop(cards)  # 가장 작은 수와
    temp2 = heapq.heappop(cards)  # 그 다음 작은 수

    temp_sum = temp + temp2 # 가장 작은 두 수를 더해서 cnt 누적
    cnt += temp_sum
    heapq.heappush(cards, temp_sum)  # 더한 값을 다시 넣어줌

  print(cnt)