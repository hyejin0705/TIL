import sys

graph = [list(sys.stdin.readline().rstrip()) for _ in range(4)]
# N이 0 이고 S가 1이다.
    
k = int(sys.stdin.readline())
data = []

def rotate_clock(graph):
    temp = graph[7]
    for i in range(6, -1, -1):
        graph[i+1] = graph[i]
    graph[0] = temp

def rotate_ban_clock(graph):
    temp = graph[0]
    for i in range(7):
        graph[i] = graph[i + 1]
    graph[7] = temp

def dfs(x, y):
    global visited
    if visited[x] == 0:
        visited[x] = 1
        left = graph[x][6]
        right = graph[x][2]
        
        if y == 1: # 시계방향일떄
            rotate_clock(graph[x])
        else:
            rotate_ban_clock(graph[x])
            
        if x-1 >= 0 and left != graph[x-1][2]:
            dfs(x-1, -y) # 방향은 지금 톱니바퀴가 도는 방향과 반대로 돈다.
            
        if x+1 <=3 and right != graph[x+1][6]:
            dfs(x+1, -y)

for _ in range(k):
    a,b = map(int,input().split())
    visited = [0] * 4
    dfs(a - 1, b)

cnt = 0
for i in range(4):
    if graph[i][0] == '1':
        cnt += (2 ** i)
        
print(cnt)