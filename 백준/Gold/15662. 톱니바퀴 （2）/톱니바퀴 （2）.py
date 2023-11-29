import sys
from collections import deque

def solution(T, gears, K, turn):
    for t, direction in turn:
        turnElement = []
        # t 기준 오른쪽 기어
        for i in range(t+1, T+1):
            if gears[i][6] != gears[i-1][2]: turnElement.append(i)
            else: break
        # t 기준 왼쪽 기어
        for i in range(t-1, 0, -1):
            if gears[i][2] != gears[i+1][6]: turnElement.append(i)
            else: break
        # t 기어 회전
        gears[t].rotate(direction)
        # t 기어와 맞닿은 극이 다른 기어 회전
        for element in turnElement:
            gears[element].rotate(-direction if (element-t)%2 else direction)
    return sum([gears[i][0] for i in range(1, T+1)])

T = int(sys.stdin.readline())
gears = [0] + [deque(map(int, list(sys.stdin.readline().strip()))) for _ in range(T)]
K = int(sys.stdin.readline())
turn = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

res = solution(T, gears, K, turn)
print(res)