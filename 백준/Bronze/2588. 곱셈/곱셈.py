N = int(input())
M = input()

total = 0
for idx, m in enumerate(M[::-1]):
    total += N * int(m) * (10**idx)
    print(N * int(m))
print(total)