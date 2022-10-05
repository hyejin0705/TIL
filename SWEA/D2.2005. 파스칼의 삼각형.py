# 재귀생각하지 않고, 푼 방식.
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 파스칼의 삼각형의 줄의 수

    # 1를 각 행에 행의 수만큼 생성.
    # N이 2 이하일 때 결과 생성.
    result= [[1] * (i+1) for i in range(N)]

    # N이 3 이상이라면,
    if N > 2:

        # 2번째 줄부터 돌기
        for idx in range(2, N):

            # 인덱스 1번부터 앞줄의 두 값을 더한 값으로 갱신
            for p in range(1, idx):
                result[idx][p] = result[idx-1][p-1] + result[idx-1][p]    

    print(f'#{test_case}')
    for lst in result:
        print(*lst)
