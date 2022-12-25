from collections import deque

def bfs(s, e):
    q = deque()

    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()

        if c == e:
            print(v[c] - 1)
            return

        for n, move in [(c + 1, 1), (c - 1, 1), (c * 2, 0)]:

            # 순간이동하면, 0이기 때문에, 나중에 작은 경우가 올 수 있음.
            if 0 <= n <= MAX and (not v[n] or v[n] > v[c] + move):
                q.append(n)
                v[n] = v[c] + move


S, E = map(int, input().split())

MAX = 100000

v = [0] * (MAX + 1)

bfs(S, E)