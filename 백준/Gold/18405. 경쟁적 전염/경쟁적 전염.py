## 문제를 풀 때 생각했던 점

# bfs로 푸는데 초를 추가하는 방법  (어느 시점에 count 해야 할지)
# 낮은 바이러스부터 시작하는 방법  (정렬)

def bfs(S):
    q = []

    for i in range(N):
        for n in range(1, K + 1):
            if n in arr[i]:
                j = arr[i].index(n)
                q.append([arr[i][j], i, j])     # 번호도 같이 저장해줘야 함.

    q.sort()              # 정렬하지 않으면, 낮은 숫자부터 해결하지 못함.

    cnt = 0
    while q:
        if cnt == S:
            break

        for _ in range(len(q)):           # 초를 세기 위해 for문 하나도 생성.
            virus, si, sj = q.pop(0)

            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:         # 4방향 탐색
                ni, nj = si + di, sj + dj
                if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:   # 범위 내이고, 0이라면,
                    arr[ni][nj] = virus                               # 바이러스 저장
                    q.append([virus, ni, nj])                      # 이동할 지역으로 저장.

        cnt += 1          # 한번의 반복이 끝나면, 1초 증가


N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

bfs(S)

print(arr[X-1][Y-1])       # 확인할 지역 출력 (인덱스는 0부터 시작이기 때문에 -1)
