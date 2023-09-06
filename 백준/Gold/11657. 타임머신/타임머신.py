# 노드개수, 간선개수
n,m = map(int, input().split())
# 간선정보를 담을 리스트
edges = []
# 최단거리 테이블 초기화
INF = int(1e9)
dist = [INF] * (n+1)

# 간선정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))

def bf(start):
    # 시작노드에 대해 초기화
    dist[start] = 0

    # 전체 n번의 라운드를 반복 (전체노드를 방문)
    for i in range(n):
        # 방문할때마다 모든간선을 확인
        for j in range(m):
            curr = edges[j][0] # 현재노드
            next_node = edges[j][1] # 목적지노드
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더짧은 경우
            if dist[curr] != INF and dist[next_node] > dist[curr] + cost:
                dist[next_node] = dist[curr] + cost
                if i==n-1: #n번째 라운드에서 값이 갱신되었다면 음수순환이 존재한다는것
                    return True

    return False


negative_cycle = bf(1)

if negative_cycle:
    #print("음수순환이 존재한다.")
    print(-1)
else:
    # 1번노드를 제외한 다른 모든 노드로 가는 최단거리
    for i in range(2, n+1):
        if dist[i] == INF:
            print('-1') #출발노드에서 그 지점까지 가는방법 없음
        else:
            print(dist[i])