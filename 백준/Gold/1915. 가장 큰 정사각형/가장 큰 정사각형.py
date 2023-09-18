n, m = map(int, input().split())    # n, m 입력 받음.

arr = []
dp = [[0] * m for _ in range(n)]    # 2차원 리스트 초기화. 사각형 크기의 최댓값을 저장하기 위한 리스트.

for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))      # 한 줄씩 입력받은 숫자들의 공백 모두 제거하여 리스트로 매핑.

answer = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:            # i 또는 j가 0일 경우, i-1 및 j-1 인덱스는 존재하지 않으므로, 예외처리.
            dp[i][j] = arr[i][j]
         
        elif arr[i][j] == 0:            # 사각형 크기의 최댓값을 구하는 것이므로, 공간값이 0이라면 0으로 설정.
            dp[i][j] = 0
         
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            # 정사각형의 오른쪽 아래칸을 기준으로 하여, 나머지 칸들이 값이 0이 아니라면,
            # 결국 오른쪽 아래칸에 크기를 +1로 설정 하여, 해당 정사각형의 크기를 저장할 수 있음.
     
        answer = max(dp[i][j], answer)

print(answer * answer)
