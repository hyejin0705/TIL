import sys

def make_area(idx, powerset):
    global min_dif
    if idx == N:
        if 0 < len(powerset) < N:
            area1 = powerset
            area2 = list(set(cities) - set(area1))
            if is_linked(area1) and is_linked(area2):
                dif = abs(get_population(area1) - get_population(area2))
                if dif < min_dif:
                    min_dif = dif
    else:
        make_area(idx + 1, powerset)
        make_area(idx + 1, powerset + [cities[idx]])

def is_linked(area): #dfs
    if len(area) == 1:
        return True
    stack = [area[0]]
    visited = [0] * (N + 1)
    visited[stack[0]] = 1
    cnt = 1
    while stack:
        v = stack.pop()
        for ad in adjacency[v]:
            if visited[ad] == 0 and ad in area: #방문한적 없고 방문해야할 도시이면 방문
                visited[ad] = 1
                stack.append(ad)
                cnt += 1
                if cnt == len(area):
                    return True
    return False

def get_population(area):
    total = 0
    for city in area:
        total += population[city]
    return total

N = int(sys.stdin.readline())
population = [0] + list(map(int, sys.stdin.readline().split()))
adjacency = {} #인접리스트 저장
cities = []
min_dif = 987654321
for i in range(1, N + 1):
    cities.append(i)
    adjacency[i] = list(map(int, sys.stdin.readline().split()))[1:] #갯수 빼고 리스트로 받아서

make_area(0, [])
print(min_dif if min_dif != 987654321 else -1)
#구역을 2개로 나눔
#구역이 연결되어있는지 체크
#인구수 계산