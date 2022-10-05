T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 버스의 수

    # 모든 정류장은 1번부터 1000번까지의 번호 부여
    c = [0] * 1001

    # 버스 타입(1 일반, 2 급행, 3 광역 급행)과 출발 정류장 번호 A, 종점인 정류장 번호 B
    for _ in range(N):
        T, A, B = map(int, input().split())

        c[A] += 1    # A, B 정류장은 무조건 정차
        c[B] += 1

        for idx in range(A + 1, B):
            if T == 1:             # 일반이면, A - B 모든 정류장
                c[idx] += 1

            elif T == 2:           # 급행이고, A가 짝수이면, 짝수정류장
                if A % 2:
                    if idx % 2:
                        c[idx] += 1

                else:               # A가 홀수이면, 홀수 정류장
                    if not idx % 2:
                        c[idx] += 1

            else:                   # 광역 급행이고, A가 짝수이면,
                if A % 2:
                    if not idx % 3 and idx % 10:    # 3의 배수이지만, 10의 배수가 아닌 정류장
                        c[idx] += 1

                else:                   # A가 홀수라면
                    if not idx % 4:     # 4의 배수 정류장
                        c[idx] += 1

    print(f'#{test_case} {max(c)}')