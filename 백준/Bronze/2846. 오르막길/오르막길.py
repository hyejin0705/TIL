N = int(input())

lst = list(map(int, input().split()))

ans = up = 0
for idx in range(N-1):
    check = lst[idx + 1] - lst[idx]
    if check > 0:
        up += check

        ans = max(up, ans)

    else:
        up = 0

print(ans)