import sys
inf = 10e9

D, N = map(int, sys.stdin.readline().split())
oven = list(map(int, sys.stdin.readline().split()))
pizza = list(map(int, sys.stdin.readline().split()))

for i in range(1, D):
    oven[i] = min(oven[i], oven[i-1])

pizzaIdx = 0
depth = D-1
for i in reversed(range(D)):
    if pizzaIdx >= len(pizza):
        print(depth+1)
        sys.exit(0)

    if oven[i] >= pizza[pizzaIdx]:
        pizzaIdx += 1
        depth = i
        
print(0)