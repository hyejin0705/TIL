import sys

N, M = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

check = 0
lst.append(0)
for i in range(1, N + 1):
    check += (lst[i - 1] - lst[i]) * i

    if check == M:
        ans = lst[i]
        break

    elif check > M:
        ans = lst[i] + (check - M) // i
        break

print(ans)