def make(y, x, dy, dx, num):
    cy = y + dy
    cx = x + dx
    if dy == 0 and dx == 0:
        made.add(num)
        return
    if 0 <= cy < n and 0 <= cx < m:
        num = num*10 + arr[cy][cx]
        make(cy, cx, dy, dx, num)
    made.add(num)


n, m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
made = set()
for y in range(n):
    for x in range(m):
        for dy in range(-n, n):
            for dx in range(-m, m):
                make(y, x, dy, dx, arr[y][x])
answer = -1
for x in made:
    if x**0.5 == int(x**0.5):
        answer = max(answer, x)
print(answer)