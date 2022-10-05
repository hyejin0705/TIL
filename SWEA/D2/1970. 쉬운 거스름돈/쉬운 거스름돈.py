T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for test_case in range(1, T + 1):
    N = int(input())

    c = [0] * 8      # 잔돈 카운팅 리스트

    idx = 0
    while idx < 8:                    # 계속 반복해야 하기 때문에 while 활용
        if N - money[idx] >= 0:   # N에서 잔돈을 빼고 나서 양수라면, count
            c[idx] += 1
            N -= money[idx]        # N 갱신.
        else:                            # 음수라면, 다음 잔돈으로 넘어감.
            idx += 1

    print(f'#{test_case}')
    print(*c)