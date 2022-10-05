# 0818 풀이

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(N)]

    # 델타 방향 리스트 생성
    d_lst = []
    for i in range(M):
        for j in range(M):
            d_lst.append((i, j))

    # 합계 리스트 생성
    total_lst = []
    for i in range(N - M + 1):      # 행
        for j in range(N - M + 1):  # 열
            total = 0
            for di, dj in d_lst:    # 방향리스트에서 하나씩 사용 
                ni = i + di
                nj = j + dj
                total += lst[ni][nj]
            total_lst.append(total)   # 합계 리스트에 저장.
    
    mx_total = 0
    for s in total_lst:    # 최대값 찾기.
        if mx_total < s:
            mx_total = s
    
    print(f'#{test_case} {mx_total}')


# -------------------------------------------------------------------------
# 0717 풀이
def bugs(lst, N, M):
    total_lst = []
    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            total = 0
            for x in range(M):
                total += sum(lst[i+x][j : M +j])

            total_lst.append(total)
    return max(total_lst)

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    
    result = bugs(lst, N, M)
 
    print(f'#{t} {result}')
