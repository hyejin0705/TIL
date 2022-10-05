# x좌표와 y좌표는 1이상이고 100이하인 정수
arr = [[0] * 101 for _ in range(101)]

cnt = 0

# 입력은 네 줄
for _ in range(4):

    # 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고
    # 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다.
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1

print(cnt)