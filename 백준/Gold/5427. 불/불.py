from collections import deque
import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(start_r, start_c):

    q.append([start_r, start_c])

    global time
    while q:
        time += 1
        qlen = len(q)
        for _ in range(qlen):
            y, x = q.popleft()
            matrix[y][x] = '@'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if ny < 0 or ny >=h or nx < 0 or nx >= w:
                    return time

                if 0 <= ny < h and 0 <= nx < w:
                    if matrix[ny][nx] == '.':
                        matrix[ny][nx] = '@'
                        q.append([ny, nx])

        fire()
    return 'IMPOSSIBLE'


def fire():
    qlen = len(fire_q)
    for i in range(qlen):
        y, x = fire_q.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= ny < h and 0 <= nx < w and matrix[ny][nx] == '.':
                matrix[ny][nx] = '*'
                fire_q.append([ny, nx])



for _ in range(int(sys.stdin.readline())):
    w, h = map(int, sys.stdin.readline().split())
    q = deque()
    fire_q = deque()
    matrix = []


    time = 0

    for i in range(h):
        matrix.append(list(sys.stdin.readline().strip()))
        for j in range(w):
            if matrix[i][j] == '@':
                start_r, start_c = i, j
            elif matrix[i][j] == '*':
                fire_q.append([i, j])

    fire()
    print(bfs(start_r, start_c))