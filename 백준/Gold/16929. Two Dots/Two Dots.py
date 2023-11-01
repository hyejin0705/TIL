dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, cnt):
    global tx, ty, flag
    if flag: return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M or a[nx][ny] != a[tx][ty]: # 범위 벗어나지 않고, 색깔이 같을 때만 하도록
            continue
        if not visit[nx][ny]:
            visit[nx][ny] = True # 방문처리 했다가
            dfs(nx, ny, cnt + 1)
            visit[nx][ny] = False # 안한 걸로
        else:
            if cnt >= 4 and tx == nx and ty == ny: # 4번 이상이고 위치가 같을 때 -> 사이클
                flag = True
                return

N, M = map(int, input().split())
a = [list(input()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
flag = False

for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            tx, ty = i, j
            visit[i][j] = True
            dfs(i, j, 1)
        if flag:
            print("Yes")
            exit(0)

print("No")