import sys

def getParent(parent, node):
    if parent[node] == node:
        return node
    return getParent(parent, parent[node])

def union(parent, x, y):

    parentOfX = getParent(parent, x)
    parentOfY = getParent(parent, y)
    if parentOfX > parentOfY:
        parent[parentOfX] = parentOfY
    else:
        parent[parentOfY] = parentOfX


def findMST():
    result = 0
    # 각 노드의 Parent 노드 정보 초기화 - 자기 자신
    parent = [i for i in range(m)]

    # 가장 적은 비용이 드는 간선 순으로 정렬
    edges.sort()

    for edge in edges:
        cost, x, y = edge
        
        # 싸이클이 없는 경우에 해당 간선 선택
        if getParent(parent,x) != getParent(parent, y):
            union(parent, x, y)
            result += cost
    return result

while True:
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        break

    edges = [] # 모든 간선 정보를 저장하는 리스트
    original_cost = 0 # 모든 길에 가로등이 있을 때 비용
    for _ in range(n):
        x, y, cost = map(int, sys.stdin.readline().split())
        edges.append((cost, x, y))
        original_cost += cost

    # 모든 집을 연결하는 최소 스패닝 트리 비용을 구한다.
    min_cost = findMST()
    
    saved_cost = original_cost - min_cost
    print(saved_cost)