T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N * M 배열

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        cnt1 = 0
        for j in range(M):
            if arr[i][j] == 1:    # 가로
                cnt1 += 1
                ans = max([ans, cnt1])    # 최대값 갱신

            else:
                cnt1 = 0

    # N, M이 서로 다른 숫자일 수도 있기 때문에
    for j in range(M):           # 세로
        cnt2 = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt2 += 1
                ans = max([ans, cnt2])    # 최대값 갱신
            else:
                cnt2 = 0

    print(f'#{test_case} {ans}')