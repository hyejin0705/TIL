n = int(input())
a, b = map(int, input().split())
m = int(input())
ans = 2147000000
flow = [-1]
door = [0 if i == a or i == b else 1 for i in range(n+1)]
for _ in range(m):
    flow.append(int(input()))


def go(x, cnt, a):
    global ans
    if x == m+1:
        ans = min(ans, cnt)
        return
    cur = flow[x]  # 현재위치
    for i in range(cur, 0, -1):  # 왼쪽으로 찾음
        if a[i] == 0:
            tmp = a[:]
            tmp[i], tmp[cur] = tmp[cur], tmp[i]
            go(x+1, cnt+abs(cur-i), tmp)
    for i in range(cur, n+1): #오른쪽
        if a[i] == 0:
            tmp = a[:]
            tmp[i], tmp[cur] = tmp[cur], tmp[i]
            go(x+1, cnt+abs(cur-i), tmp)


go(1, 0, door)
print(ans)