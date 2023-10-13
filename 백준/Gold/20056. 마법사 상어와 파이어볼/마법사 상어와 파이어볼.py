from collections import deque

def move():
    while fireballs:
        # 좌표
        r, c = fireballs.popleft()
        # 질량, 속도, 방향
        m, s, d = data[r][c].popleft()

        # 1번 행과 N번 행, 1번 열과 N번 열이 연결되어 있으므로 n으로 나눈 나머지를 
        # 좌표로 설정한다.
        nr = (r + dx[d] * s) % n
        nc = (c + dy[d] * s) % n

	    # 해당 좌표에 파이어볼의 정보를 추가
        data[nr][nc].append(deque((m, s, d)))

    # 칸에 두개 이상의 파이어볼이 있는지 체크
    for i in range(n):
        for j in range(n):
            # 두개 이상의 파이어볼이 있다면
            if len(data[i][j]) > 1:
                mass, speed = 0, 0
                count = [0, 0]
                length = len(data[i][j])
				
                # 총 질량과 속도를 구해준다.
                while data[i][j]:
                    m, s, d = data[i][j].popleft()
                    mass += m
                    speed += s
                    count[d % 2] += 1
                    
                # 만약 나뉜 질량이 0이라면 소멸
                if mass // 5 == 0:
                    continue

			    # 파이어볼의 방향이 모두 짝수거나 홀수라면
                if count[0] * count[1] == 0:
                    directions = [0, 2, 4, 6]
                # 파이어볼의 방향이 모두 짝수거나 홀수가 아니라면
                else:
                    directions = [1, 3, 5, 7]

                # 파이어볼에 좌표를 추가해준다.
                # 해당 좌표에 파이어볼의 정보를 추가해준다.
                for direction in directions:
                    fireballs.append((i, j))
                    data[i][j].append(deque((mass // 5, speed // length, direction)))
            # 한개의 파이어볼만 존재한다면 좌표 정보만 추가해준다.
            elif len(data[i][j]) == 1:
                fireballs.append((i, j))


n, m, k = map(int, input().split())
fireballs = deque()
data = [[deque() for _ in range(n)] for _ in range(n)]
answer = 0

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r - 1, c - 1))
    data[r - 1][c - 1].append((deque((m, s, d))))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    move()

# 존재하는 파이어볼의 질량을 더해준다.
for i in range(n):
    for j in range(n):
        answer += sum(arr[0] for arr in data[i][j])

print(answer)