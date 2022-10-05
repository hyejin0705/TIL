T = 10
N = 100

for test_case in range(1, T + 1):
    _ = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    # 시작점(1) 리스트 생성
    start = []
    for idx in range(N):
        if lst[0][idx] == 1:
            start.append(idx)

    min_cnt = 1000     # 최소값 지정
    for idx in start:  # 시작점 하나씩
        i = 0

        result = idx   # 시작점 저장.

        # 지나간 길을 저장할 리스트 생성.
        stack = [[0] * N for _ in range(N)]
        stack[0][idx] = 1

        i = 1
        cnt = 0   # 지나간 길 count
        
        # while 종료 범위 지정.
        while i < 100:
            
            # idx - 1 의 범위를 지정해줘야 lst[-1]로 가지 않음.
            # 왼쪽에 1이 존재하고, 지나 온 자리(stack = 1)가 아니라면,
            if idx - 1 >= 0 and lst[i][idx - 1] == 1 and stack[i][idx-1] == 0:
                stack[i][idx] = 1       # 지나간 길로 체크
                cnt += 1                # 빈도수 1증가
                idx -= 1

            # 오른쪽에 1이 존재하고, 지나온 자리(stack = 1)가 아니라면,
            elif idx + 1 < 100 and lst[i][idx + 1] == 1 and stack[i][idx+1] == 0:
                stack[i][idx] = 1
                cnt += 1
                idx += 1

            # 왼쪽, 오른쪽에 길이 없다면, 아래로 이동.
            else:
                stack[i][idx] = 1     # 지나간 길 체크
                i += 1
                cnt += 1

        # 빈도수가 최소값보다 작다면, 인덱스 저장.
        if min_cnt > cnt:
            min_cnt = cnt
            min_start = result

    print(f'#{test_case} {min_start}')
