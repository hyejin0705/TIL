def where(d, n):
    # 상점이 블록의 북쪽(1) 또는 남쪽(2)에 위치한 경우 블록의 왼쪽 경계로부터의 거리
    if d == 1:
        return (d, 0, n)     # 방향, x, y
    if d == 2:
        return (d, H, n)

    # 상점이 블록의 동쪽(4) 또는 서쪽(3)에 위치한 경우 블록의 위쪽 경계로부터의 거리
    if d == 3:
        return (d, n, 0)
    else:
        return (d, n, W)


W, H = map(int, input().split())

Len = (W + H) * 2   # 전체 둘레

store = int(input())

store_lst = []
for _ in range(store):
    d, n = map(int, input().split())

    store_lst.append(where(d, n))

d, n = map(int, input().split())
here = where(d, n)  # 방향, x, y

ans = 0
for st in store_lst:
    # 방향이 정반대인 경우 모든 x, y를 더하기?
    if (min(here[0], st[0]) == 1 and max(here[0], st[0]) == 2) \
            or (min(here[0], st[0]) == 3 and max(here[0], st[0]) == 4):
        dist = here[1] + here[2] + st[1] + st[2]
        ans += min(dist, Len - dist)

    # 방향이 양 옆, 같다면, |x1-x2| + |y1-y2|
    else:
        dist = abs(here[1] - st[1]) + abs(here[2] - st[2])
        ans += min(dist, Len - dist)

print(ans)