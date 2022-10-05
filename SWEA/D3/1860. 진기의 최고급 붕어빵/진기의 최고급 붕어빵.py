def bread():
    second = bbang = 0          # 시간, 붕어빵 개수 초기화

    result = "Possible"

    if lst[0] < M:              # 처음 만들기 전에 손님이 온다면, 실패
        result = "Impossible"
        return result

    while lst:                  # lst에 값이 없을 때까지 반복
        second += 1
        if not second % M:      # M초가 지나면
            bbang += K          # 붕어빵 K개 생성

        while lst and lst[0] == second:
            if bbang:           # 붕어빵이 존재하면 성공
                lst.pop(0)      # 한 손님 보내고,
                bbang -= 1      # 붕어빵 개수를 감소
                continue

            else:
                result = "Impossible"  # 붕어빵이 없다면 실패
                return result

    return result


T = int(input())

for test_case in range(1, T + 1):

    # 손님 N명, M초에 붕어빵 K개 생성
    N, M, K = map(int, input().split())

    # 손님들 도착시간 리스트
    lst = list(map(int, input().split()))

    lst.sort()                 # 정렬

    print(f'#{test_case} {bread()}')