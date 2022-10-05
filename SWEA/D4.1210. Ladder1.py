T = 10
N = 100

for _ in range(1, T + 1):
    test_case = int(input())

    ladder_lst = [list(map(int, input().split())) for _ in range(N)]

    # 마지막 줄에서 2(성공)를 찾기 -> 거꾸로 올라가기
    for s_idx in range(N):
        if ladder_lst[N - 1][s_idx] == 2:
            ni = N - 1
            nj = s_idx
            break

    # 범위 밖을 나가는 것을 방지하기 위해
    # ni가 0일 때 도착하기 때문에, 0를 포함하지 않음.
    while 0 < ni:

        # out of index를 방지하기 위해 범위설정
        # 오른쪽 값이 1이라면, 오른쪽으로
        if nj + 1 < N and ladder_lst[ni][nj + 1] == 1:
            ladder_lst[ni][nj] = 0  # 방향을 틀었다면, 초기화
            nj += 1

        # out of index를 방지하기 위해 범위설정
        # 왼쪽 값이 1이라면, 왼쪽으로
        elif 0 <= nj - 1 and ladder_lst[ni][nj - 1] == 1:
            ladder_lst[ni][nj] = 0  # 방향을 틀었다면, 초기화
            nj -= 1

        # 양 옆에 1이 없다면, 앞으로 전진.
        else:
            ni -= 1
        # else로 주지 않고, while 밑에 주면, 앞에 길이 없어도 그냥 전진함.(디버깅)
    
    # 도착했을 때의 nj의 값이 시작점.
    print(f'#{test_case} {nj}')


## 나중에 델타를 이용해서 한번 풀어볼 생각중.
