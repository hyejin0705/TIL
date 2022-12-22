import sys
import heapq

def dij(s):
    q = []
    
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    
    D[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, c = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시   >>>   시간초과 해결 방안
        if D[c] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for e, w in arr[c]:
            check = dist + w
            
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if check < D[e]:
                D[e] = check
                heapq.heappush(q, (check, e))
                
              

# 무한을 의미하는 INF                
INF = 10e8

# 정점의 개수 V, 간선의 개수 E
V, E = map(int, sys.stdin.readline().split())

N = V + 1

# 시작 정점의 번호
start = int(sys.stdin.readline())

# 그래프 초기화
arr = [[] * N for _ in range(N)]


# 간선 정보 입력
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    
    # s -> e : w(가중치)
    arr[s].append((e, w))

    
# 최단 거리 테이블을 모두 무한으로 초기화    
D = [INF] * N

# 다익스트라 알고리즘을 수행
dij(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, N):
    if D[i] == INF:
        print('INF')
    else:
        print(D[i])



# ---------------------------------------------------------------------
# bfs 응용버전 -> 시간초과

# deque, heapq까지 이용하였지만, 시간초과 발생
# 탐색하지 않아도 되는 경우를 고려하지 않아서 시간초과 발생
# ---------------------------------------------------------------------

# import sys
# from collections import deque

# def bfs(start):
#     visited = [INF] * (V + 1)
#     q = deque()

#     q.append(start)
#     visited[start] = 0

#     while q:
#         c = q.popleft()

#         for e, w in arr[c]:
#             if visited[e] > visited[c] + w:
#                 visited[e] = visited[c] + w
#                 q.append(e)

#     return visited


# V, E = map(int, sys.stdin.readline().split())
# start = int(input())
# INF = 10e8

# arr = [[] for _ in range(V + 1)]

# for _ in range(E):
#     s, e, w = map(int, sys.stdin.readline().split())
#     arr[s].append((e, w))

# visited = bfs(start)

# for i in range(1, V + 1):
#     if visited[i] == INF:
#         print('INF')
#     else:
#         print(visited[i])



# ---------------------------------------------------------------------
# 다익스트라 초기버전 -> 메모리초과

# 이중리스트로 생성했더니, 메모리초과 문제 발생???
# ---------------------------------------------------------------------

# def dij(s, e):
#     visited = [INF] * (V + 1)
#     visited[s] = 0

#     for i in range(1, V + 1):
#         for j in range(V + 1):
#             visited[j] = min(visited[i] + arr[i][j], visited[j])

#     return visited


# V, E = map(int, sys.stdin.readline().split())
# start = int(input())
# INF = 10e8

# arr = [[INF] * (V + 1) for _ in range(V + 1)]

# for _ in range(E):
#     s, e, w = map(int, sys.stdin.readline().split())
#     arr[s][e] = w

# visited = dij(start, V)

# for i in range(1, V + 1):
#     if visited[i] == INF:
#         print('INF')
#     else:
#         print(visited[i])
