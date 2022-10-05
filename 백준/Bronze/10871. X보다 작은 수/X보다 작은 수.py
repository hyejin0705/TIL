N, X = map(int, input().split())

lst = list(map(int, input().split()))

x = []
for l in lst:
    if l < X:
        x.append(l)

print(*x)