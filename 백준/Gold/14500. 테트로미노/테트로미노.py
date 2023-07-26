import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, step, tot):
    global n, m, ans, max_val

    if tot + max_val * (4 - step) <= ans:
        return

    if step == 4:
        ans = max(ans, tot)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny]:
                visit[nx][ny] = 1
                dfs(nx, ny, step + 1, tot + a[nx][ny])
                visit[nx][ny] = 0

def adj(x, y):
    global n, m, ans
    t = []
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            t.append(a[nx][ny])
    
    if len(t) >= 3:
        tmp = a[x][y] + sum(sorted(t, reverse = True)[:3])
        ans = max(ans, tmp)

n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visit = [[0] * m for _ in range(n)]
ans = 0
max_val = max(map(max, a))

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, a[i][j])
        visit[i][j] = 0
        adj(i, j)

print(ans)