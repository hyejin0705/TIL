from collections import deque

def bfs(s, e):
    global cnt
    q = deque()

    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()

        if c == e:
            cnt += 1     # count 세기

        for n in [c + 1, c - 1, c * 2]:
            
            # 조건을 비방문지로만 하면, 최소값이 발견되면, 반복이 끝남.
            # 즉, 비방문지거나, 값이 같을 경우에도 돌아가게 해야 가지 수를 셀 수 있음.
            if 0 <= n <= MAX and (not v[n] or v[n] == v[c] + 1):
                q.append(n)
                v[n] = v[c] + 1


S, E = map(int, input().split())

MAX = 100000

v = [0] * (MAX + 1)

cnt = 0

bfs(S, E)

print(v[E] - 1)    # 최소 시간 
print(cnt)       # 방문 가지 수
