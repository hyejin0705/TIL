N = int(input()) 

lst = []
for _ in range(N):
    lst += list(map(int, input().split()))

max_num = max(lst) + 11
# 최대값을 구하고 + 11 (색종이가 범위를 나가지 않게)

# 위에서 구한 범위로 2차원 배열 생성
arr = [[0] * max_num for _ in range(max_num)]

# 넓이 변수
cnt = 0
for idx in range(N):             # A, B, C의 범위 가져오기
    i, j = lst[idx * 2], lst[idx * 2 + 1]
    for ni in range(i, i + 10):     # 각 색종이의 행
        for nj in range(j, j + 10): #           열
            if arr[ni][nj] == 0:      # 위치가 0이면,
                arr[ni][nj] += 1      # 1를 지정해주고
                cnt += 1            # 넓이 1증가
                
print(cnt)