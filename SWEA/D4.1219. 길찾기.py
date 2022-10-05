def DFS(s):
    visited[s] = 1
    result = 0
    while True:         
        for w in adj[s]:
            if w == 0:           # 출발지점에 도착하면
                result = 1       # 성공하면 1 출력
                return result    # return으로 while 종료

            if visited[w] == 0:
                stack.append(w)
                visited[w] = 1
                s = w
                break

        else:
            if stack:
                s = stack[-1]
                stack.pop()
            else:
                return result   # return으로 while 종료


T = 3
N = 100

for test_case in range(1, T + 1):
    _, M = map(int, input().split())

    lst = list(map(int, input().split()))

    # 정점 데이터 생성 (0 ~ 99)
    adj = [[] for _ in range(N)]
    for i in range(M):
        idx = i * 2     # 짝수인덱스 생성.

        # 짝수 인덱스 = 출발, 홀수 인덱스 = 도착
        # 목적지부터 거꾸로 거슬러 올라오기 위해, 반대방향으로 저장.
        adj[lst[idx + 1]].append(lst[idx])

    visited = [0] * N
    stack = []

    s = 99               # 목적지부터 출발지점까지 거슬러 올라감.

    result = DFS(s)      # 함수호출

    print(f'#{test_case} {result}')
