N, M = map(int, input().split())

par = N
son = M
for num in range(1, M):
    son *= num
    par *= N - num

print(par//son)