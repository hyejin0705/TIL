from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS(x, y):
    for d in range(4):	# 상하좌우
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < 12 and 0 <= Y < 6:
            if board[X][Y] == board[x][y] and visited[X][Y] == 0:	# 같은 색깔이고 방문한 적이 없으면
                q.append([X, Y])	# 큐에 담음
                visited[X][Y] = 1	# 방문 기록

def gravity():
    for y in range(6):
        bag = deque([])	# 뿌요 순서를 담을 가방(큐)
        for x in range(11, -1, -1):
            if board[x][y] != '.':	# 위로 올라가며 뿌요가 있으면 가방에 담음
                bag.append(board[x][y])
        for x in range(11, -1, -1):
            if bag:	# 가방에 있는 뿌요를 하나씩 꺼내어 보드에 기록
                board[x][y] = bag.popleft()
            else:	# 가방이 비면 나머지는 뿌요가 없음
                board[x][y] = '.'

board = []
for _ in range(12):
    board.append(list(input()))

chk = 0
answer = 0
while True:		# 새로 터지는 뿌요가 없을 때까지 반복
    visited = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and visited[i][j] == 0:	# 뿌요가 있고 아직 방문한 적이 없다면
                visited[i][j] = 1	# 방문
                q = deque([[i, j]])	# BFS를 위해 큐 기록
                st = []	# 큐는 pop으로 없애므로 뿌요 위치를 기록할 스택
                while q:
                    now = q.popleft()
                    st.append(now)
                    BFS(now[0], now[1])	# 큐에서 하나 꺼내 상하좌우 체크하는 함수로 이동
                if len(st) >= 4:	# 이어진 뿌요가 4개 이상일 때
                    chk = 1		# 터진 뿌요가 있음을 알림
                    for s in st:
                        board[s[0]][s[1]] = '.'	# 뿌요 터뜨림
    gravity()	# 중력 작용
    if chk == 0:	# 터진 뿌요가 없다면 while문 종료
        break
    chk = 0
    answer += 1
print(answer)