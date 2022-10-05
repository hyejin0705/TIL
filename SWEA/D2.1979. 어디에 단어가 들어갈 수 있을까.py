T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    ans = 0 
    for i in range(N):                # 행
        cnt_1 = 0
        cnt_2 = 0
        for j in range(N):            # 열
            if puzzle[i][j] == 1:      # 1이 나오면 count
                cnt_1 += 1
                if cnt_1 == K:        # 1이  연속으로 K개가 나오면, 답 1증가
                    ans += 1
                elif cnt_1 > K:      # K개가 넘으면 cnt 초기화, 답 1 감소 
                    ans -= 1
                    cnt_1 = 0
            else:                     # 0이 나오면, cnt 초기화
                cnt_1 = 0

            if puzzle[j][i] == 1:      # 열 검색은 위와 동일.
                cnt_2 += 1
                if cnt_2 == K:
                    ans += 1
                elif cnt_2 > K:
                    ans -= 1
                    cnt_2 = 0
            else:
                cnt_2 = 0

    print(f'#{test_case} {ans}')
    
