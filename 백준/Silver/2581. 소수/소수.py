M = int(input())
N = int(input())
lst = []

for n in range(M, N + 1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            lst.append(n)

if not lst:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))