import sys

def is_in(ix, iy, n):
    if 0 <= ix < n and 0 <= iy < n:
        return True
    return False


N = int(sys.stdin.readline())

# 학생: *좋아하는 친구들 딕셔너리
like_friends = {}
for _ in range(N ** 2):
    student, *friends = list(map(int, sys.stdin.readline().split()))
    like_friends[student] = friends

# 교실
classroom = [[0 for _ in range(N)] for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for stu, likes in like_friends.items():
    max_like = 0  # 붙어있는 자리에 좋아하는 최대
    max_blank = 0  # 붙어있는 자리에 빈자리 최대
    loc = -1, -1  # 그 위치
    for i in range(N):
        for j in range(N):
            if classroom[i][j] != 0:  # 자리가 비어있는 경우만
                continue

            if loc == (-1, -1):  # 주의! 빈자리나 좋아하는 친구가 있는 자리가 모두 0일 수 있다.
                loc = i, j  # 처음 나오는 빈자리를 기준으로 진행
            blank = 0
            like = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if is_in(nx, ny, N):
                    if classroom[nx][ny] == 0:  # 1. 빈자리
                        blank += 1
                    elif classroom[nx][ny] in like_friends[stu]:  # 2. 좋아하는 학생 자리
                        like += 1

            if like > max_like or (like == max_like and blank > max_blank):
                # 1. 좋아하는 사람 옆자리, 2. 같으면 빈자리
                max_blank = blank
                max_like = like
                loc = i, j

    x, y = loc
    classroom[x][y] = stu

    # td(classroom)

# 점수 계산
total = 0
satisfaction = [0, 1, 10, 100, 1000]
for i in range(N):
    for j in range(N):
        stu = classroom[i][j]
        like = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if is_in(nx, ny, N) and classroom[nx][ny] in like_friends[stu]:
                like += 1

        total += satisfaction[like]

print(total)