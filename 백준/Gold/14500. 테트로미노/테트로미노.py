import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, step, tot):
    global n, m, ans, max_val
    
    # 남은 블럭이 모두 최댓값이라 해도 현재의 최대를 넘길수 없을때 조기종료 해버림
    if tot + max_val * (4 - step) <= ans:
        return
    
    # 사각형 4개가 된 순간 최댓값을 갱신한다.
    if step == 4:
        ans = max(ans, tot)
        return
    
    # 상하좌우 이동
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny]:
                visit[nx][ny] = 1
                dfs(nx, ny, step + 1, tot + a[nx][ny])
                visit[nx][ny] = 0  # 목적지 갱신

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

#세로-n-행, 가로-m-열
n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

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
