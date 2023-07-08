import sys

# 아래, 오른쪽만(최단 경로로)
dy, dx = (1, 0), (0, 1)

def dfs(i, j, curr_num, before):  # 좌표, 그때까지 계산한 값
    global max_answer, min_answer

    if i == N - 1 and j == N - 1:  # 학교 도착했으면
        # 정답 업데이트
        max_answer = max(max_answer, int(curr_num))
        min_answer = min(min_answer, int(curr_num))

    # 아래, 오른쪽만
    for k in range(2):
        ni = i + dy[k]
        nj = j + dx[k]

        # 범위
        if ni < 0 or nj < 0 or ni >= N or nj >= N:
            continue

        if map_arr[ni][nj].isdigit():  # 숫자라면
            dfs(ni, nj, str(eval(curr_num + before + map_arr[ni][nj])), '')
        else:  # 기호라면
            dfs(ni, nj, curr_num, map_arr[ni][nj])


N = int(sys.stdin.readline())
map_arr = list(sys.stdin.readline().split() for _ in range(N))

max_answer = -(5 ** 20)
min_answer = 5 ** 20

dfs(0, 0, map_arr[0][0], '')
print(max_answer, min_answer)