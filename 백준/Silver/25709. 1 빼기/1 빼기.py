N = input()
ans = 0
while N:
    if int(N) == 1:
        ans += 1
        break

    if N.count('1'):
        idx = N.index('1')
        N = N[:idx] + N[idx+1:]
        if not int(N):
            ans += 1
            break
    else:
        N = str(int(N) - 1)
    ans += 1

print(ans)