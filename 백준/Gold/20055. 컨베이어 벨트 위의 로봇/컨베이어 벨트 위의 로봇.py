import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
# 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
# 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
# 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
ans = 0
belt = deque(map(int, sys.stdin.readline().split()))
# 로봇위치는 n개다 위에만 세면 된다 아래는 어차피 로봇 못 둔다.
robot = deque(list([0]*n))

while belt.count(0) < k:
    #한 칸씩 돌리기
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot) > 0 :
        for i in range(n-2,-1,-1):
            # robot[i] 가 0 이면 로봇이 없기 때문에 이동해줄 수 있음
            # 이동해주면 그자리는 내구성 -1 해주면 된다.
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1:
                    robot[i+1] = 1 
                    robot[i] = 0 
                    belt[i+1] -= 1
        robot[-1] = 0
    if robot[0] == 0 and belt[0]>=1: 
        robot[0] = 1 
        belt[0] -= 1 
    ans += 1 
print(ans)