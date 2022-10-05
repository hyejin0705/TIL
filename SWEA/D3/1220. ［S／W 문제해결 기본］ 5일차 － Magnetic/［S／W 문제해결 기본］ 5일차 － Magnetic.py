T = 10

for test_case in range(1, T + 1):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for j in range(N):                    # 열
        stack = []
        for i in range(N):                # 행
            if lst[i][j] == 1:
                stack.append(lst[i][j])   # 1이 나오면, 넣기
            if lst[i][j] == 2 and stack:  # 2가 나오고, stack에 1이 있으면,
                cnt += 1                  # count 하고
                stack = []                # 다시 빈 리스트 만들기(갱신)

    print(f'#{test_case} {cnt}')
