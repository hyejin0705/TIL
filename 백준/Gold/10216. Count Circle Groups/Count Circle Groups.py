import sys

def calcD(c1, c2):
    return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)

def dfs(i):
    for j in range(N):
        if i == j or visit[j]: 
            continue
        if calcD(cs[i], cs[j]) > (cs[i][2] + cs[j][2]) ** 2: 
            continue
        visit[j] = 1
        dfs(j)

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cnt = 0
    visit = [0] * N
    for i in range(N):
        if visit[i]: 
            continue
        dfs(i)
        cnt += 1
    print(cnt)