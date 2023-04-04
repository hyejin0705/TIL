def distance(xa, yb, xc, yd):
    return abs(xa-xc) + abs(yb-yd)

def dfs(x, y, status):
    global end_x, end_y, visited
    # 상근이네에서 페스티벌까지 1000m 이내인 경우
    if distance(x, y, end_x, end_y) <= 1000:
        return True
    for i in range(s):
        store_x, store_y = store[i]
        if distance(x, y, store_x, store_y) <= 1000:
            if not visited[i]:
                visited[i] = True
                status = dfs(store_x, store_y, status)
    return status


for _ in range(int(input())):
    s = int(input())
    start_x, start_y = map(int, input().split())
    store = [tuple(map(int, input().split())) for _ in range(s)]
    end_x, end_y = map(int, input().split())
    visited = [False for _ in range(s)]
    check = dfs(start_x, start_y, False)
    print('happy' if check else 'sad')