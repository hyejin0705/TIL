from collections import deque

def bfs(s, e):
    global cnt
    # q = []
    q = deque()

    q.append(s)
    v[s] = 1

    while q:
        # c = q.pop(0)
        c = q.popleft()

        if c == e:
            cnt += 1

        for n in [c + 1, c - 1, c * 2]:
            if 0 <= n <= MAX and (not v[n] or v[n] == v[c] + 1):
                q.append(n)
                v[n] = v[c] + 1


S, E = map(int, input().split())

MAX = 100000

v = [0] * (MAX + 1)

cnt = 0

bfs(S, E)

print(v[E] - 1)
print(cnt)