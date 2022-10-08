def mx_sum():
    global ans

    for idx in range(6):
        d = dices[0][:]
        s = idx
        e = check.get(s)
        up = d[e]

        d.pop(max(s, e))
        d.pop(min(s, e))

        sm = max(d)

        for next in dices[1:]:
            n = next[:]
            s = next.index(up)
            e = check.get(s)
            up = n[e]

            n.pop(max(s, e))
            n.pop(min(s, e))

            sm += max(n)

        ans = max(ans, sm)



check = {
    0: 5,       # A <-> F,
    1: 3,       # B <-> D,
    2: 4,       # C <-> E
    3: 1,
    4: 2,
    5: 0
}

N = int(input())

# A, B, C, D, E, F 의 순서로 입력
dices = [list(map(int, input().split())) for _ in range(N)]

ans = 0

mx_sum()

print(ans)