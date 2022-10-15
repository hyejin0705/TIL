### 시간초과 해결방안.
# 하나씩 값을 바꾸는 게 아니라 한꺼번에 변경(인덱스 활용)

N = int(input())    # 색종이의 수

# 색종이가 놓여지는 칸 1001 * 1001  (범위 확인 : 101이 아니라 1001)
arr = [[0] * 1001 for _ in range(1001)]

sq = [list(map(int, input().split())) for _ in range(N)]

idx = 0
for x, y, w, h in sq:           # 색종이 하나씩 꺼내기
    idx += 1                    # 색종이 번호 
    for i in range(x, x + w):      # 행
        arr[i][y: y + h] = [idx] * h  


for num in range(1, N + 1):     # 하나씩 출력.
    cnt = 0
    for lst in arr:
        cnt += lst.count(num)   # 한 행마다, count하여 누적합
    print(cnt)     