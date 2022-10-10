def bingo(lst, call):
    i_cnt = [0] * N
    j_cnt = [0] * N

    cross_cnt = 0
    xcross_cnt = 0
    result = 0
    for idx, c in enumerate(call):
        for i in range(N):
            if c in lst[i]:
                j = lst[i].index(c)
                j_cnt[j] += 1
                i_cnt[i] += 1

                if i_cnt[i] == 5:
                    result += 1

                if j_cnt[j] == 5:
                    result += 1

                # 대각선 검증
                if i == j:
                    cross_cnt += 1

                    if cross_cnt == 5:
                        result += 1

                # 역대각선 검증
                if i + j == N - 1:
                    xcross_cnt += 1

                    if xcross_cnt == 5:
                        result += 1

                if result >= 3:
                    return idx

N = 5

lst = [list(map(int, input().split())) for _ in range(N)]

call_lst = [list(map(int, input().split())) for _ in range(N)]

call = []
for i in range(N):
    for j in range(N):
        call.append(call_lst[i][j])

ans = bingo(lst, call)

print(ans + 1)