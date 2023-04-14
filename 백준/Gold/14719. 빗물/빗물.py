h, w = map(int, input().split())
blocks = list(map(int, input().split()))
rain = 0

for i in range(1, w - 1):
    l = max(blocks[:i])
    r = max(blocks[i+1:])
    min_h = min(l, r)

    if blocks[i] < min_h:
        rain += min_h - blocks[i]

print(rain)