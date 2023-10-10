from collections import deque

n=int(input())
a=[list(map(int,input())) for i in range(n)]
ch=[[-1] * n for i in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs():
    de=deque()
    de.append([0,0])
    ch[0][0]=0 

    while de:
        x,y=de.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if ch[nx][ny] == -1:
                    if a[nx][ny] == 0:
                        ch[nx][ny]= ch[x][y] + 1
                        de.append([nx,ny])
                    else:
                        ch[nx][ny]= ch[x][y]
                        de.appendleft([nx,ny])
                       
bfs()
print(ch[n-1][n-1])