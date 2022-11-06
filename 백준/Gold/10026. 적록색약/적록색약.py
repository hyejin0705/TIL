def bfs(arr):
    v = [[0] * N for _ in range(N)]      # 방문표시 리스트
    q = []
    cnt = 0      

    for i in range(N):           # (0, 0)부터 순차 탐색
        for j in range(N):

            if not v[i][j]:      # 미방문지라면,
                v[i][j] = 1      # 방문표시
                cnt += 1          # 새로운 구역 체크
                q.append([i, j])  # 인큐

                while q:                # 구역 탐색
                    si, sj = q.pop(0)

                    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:    # 4방향 탐색
                        ni, nj = si + di, sj + dj
                        
                        # 이동할 구역이 범위 내이고, 비방문지이고, 앞의 색깔과 같다면,
                        if 0 <= ni < N and 0 <= nj < N and arr[si][sj] == arr[ni][nj] and not v[ni][nj]:  
                            # 비방문지라는 조건을 체크하지 않으면, 반복문에서 나올 수 없음ㅡㅜ
                            
                            v[ni][nj] = 1        # 방문표시
                            q.append([ni, nj])   # 인큐

    return cnt


# 적록색약
N = int(input())

arr = [list(input()) for _ in range(N)]

arr2 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':         # 적록색약st(G == R) arr 재생성
            arr2[i][j] = 'R'     

        else:
            arr2[i][j] = arr[i][j]

cnt = bfs(arr)      # 적록색약이 아닌 사람
cnt2 = bfs(arr2)    # 적록색약인 경우

print(cnt, cnt2)
