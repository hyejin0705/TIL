T = 10

for test_case in range(1, T + 1):
    _ = int(input())

    lst = list(map(int, input().split()))

    cnt = 0
    while lst[-1] > 0:
        top = lst.pop(0)
        cnt += 1
        top -= cnt

        if top < 0:
            top = 0

        lst.append(top)

        if cnt == 5:
            cnt = 0

    print(f'#{test_case}', *lst)