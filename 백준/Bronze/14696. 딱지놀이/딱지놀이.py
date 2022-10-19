T = int(input())

for test_case in range(1, T + 1):
    # A의 딱지 개수, 딱지의 그림 리스트
    A, *A_lst = list(map(int, input().split()))

    # B의 딱지 개수, 딱지의 그림 리스트
    B, *B_lst = list(map(int, input().split()))

    ans = 'D'

    # 4: 별, 3: 동그라미, 2: 네모, 1: 세모
    # 높은 숫자가 많으면 승리.
    for idx in range(4, 0, -1):
        if A_lst.count(idx) == B_lst.count(idx):
            continue

        elif A_lst.count(idx) > B_lst.count(idx):
            ans = 'A'
            break

        else:
            ans = 'B'
            break

    print(ans)