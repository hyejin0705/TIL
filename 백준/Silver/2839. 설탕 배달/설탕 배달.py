def suger():
    while True:
        for i in range(check, -1, -1):
            ch = N - (5 * i)

            if not ch % 3:
                return ch // 3 + i

        else:
            return -1


N = int(input())

check = N // 5    # 5의 최대 몫 확인

cnt = suger()

print(cnt)