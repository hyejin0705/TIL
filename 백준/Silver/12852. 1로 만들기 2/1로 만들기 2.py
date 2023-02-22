import sys
from collections import deque


# bfs 탐색
def bfs(v):

    queue = deque([[v]])

    while queue:
        # 큐 리스트에서 제일 작은 리스트부터 확인
        target = queue.popleft()
        # 제일 작은 리스트에서 제일 작은 원소부터 확인
        temp = target[0]

        # 원소가 1이면 그 리스트를 리턴
        if temp == 1:

            return target

        # 원소가 3으로 나눠지면 큐에 추가
        if temp % 3 == 0:
            queue.append([temp // 3] + target)

        # 원소가 2로 나눠지면 큐에 추가
        if temp % 2 == 0:
            queue.append([temp // 2] + target)

        # 원소에서 - 1한 값을 큐에 추가
        queue.append([temp - 1] + target)


n = int(sys.stdin.readline())
# bfs 탐색해서 리스트에 값을 리턴 받는다.
res = bfs(n)

# 리턴 받은 리스트의 길이에서 - 1한 값을 출력
print(len(res) - 1)
# 리스트를 역수로 출력
print(*res[::-1])