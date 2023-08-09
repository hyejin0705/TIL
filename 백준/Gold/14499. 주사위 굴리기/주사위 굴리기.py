import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m, x, y, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
order = list(map(int, sys.stdin.readline().split()))
dice = [0,0,0,0,0,0]

for i in range(k):
    way = order[i] - 1
    nx = x + dx[way]
    ny = y + dy[way]
    if not 0 <= nx < n or not 0 <= ny < m:
        continue

    if way == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif way == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif way == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif way == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])