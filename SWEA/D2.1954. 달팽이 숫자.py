T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 행렬의 길이

    result = [[0]* N for _ in range(N)] # 리스트 생성

    # 우 하 좌 상
    bi = [0, 1, 0, -1]
    bj = [1, 0, -1, 0]

    # 시작위치
    i = 0
    j = -1   # 0,0를 만들기 위해 -1부터 시작.

    k = 0  
    cnt = 1

    while cnt <= N**2:
        ni = i + bi[k % 4]
        nj = j + bj[k % 4]   # 바로 0,0의 자리를 찾지 못함.(해결)

        # 범위 안에 존재하고, 움직인 위치의 값이 0이라면,
        if 0 <= ni < N and 0 <= nj < N and result[ni][nj] == 0:

            result[ni][nj] = cnt  
            cnt += 1
            
            i, j = ni, nj  # ni, nj로 i, j 재지정

        # 범위를 벗어나거나 움직인 위치의 값이 0이 아니라면,
        else:
            k += 1    # 방향 변경
    
    print(f'#{test_case}')
    for aws in result:
        print(*aws)
