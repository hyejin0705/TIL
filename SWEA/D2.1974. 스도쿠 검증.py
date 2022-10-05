# 내장함수 count를 대신하는 함수 및 중복되는 숫자가 존재하면 0를 반환하는 함수
def cnt(lst):    
    c = [0] * 9
    for cn in lst:
        c[cn - 1] += 1

    for n in c:
        if n >= 2:
            return 0
    return 1


T = int(input())

# 상하좌우 대각선의 방향 (8 방향 + 자기자신)
di = [0, 1, 0, -1, 0, 1, -1, 1, -1]
dj = [0, 0, 1, 0, -1, 1, -1, -1, 1]

# 중심점 좌표
m = [1, 4, 7]

for test_case in range(1, T + 1):
    lst = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    for i in range(9):
        i_lst = []  # 행 검증
        j_lst = []  # 열 검증
        x_lst = []  # 3 * 3 배열 검증

        for j in range(9):
            i_lst.append(lst[i][j])
            j_lst.append(lst[j][i])

        # 결과들을 곱하게 되면, 0이 나오는 순간 결과는 무조건 0이 나옴.
        result *= cnt(i_lst) * cnt(j_lst)

    for i in m:
        for j in m:
            x_lst = []
            for k in range(9):
                ni = i + di[k]
                nj = j + dj[k]
                x_lst.append(lst[ni][nj])

            result *= cnt(x_lst)

    print(f'#{test_case} {result}')
