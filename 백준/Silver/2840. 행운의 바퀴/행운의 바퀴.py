N, K = map(int, input().split())

lst = [input().split() for _ in range(K)]

target = lst[-1][1]

cnt = ['?'] * N
idx = 0

for num, alpha in lst:
    idx += int(num)

    i = idx % N

    if cnt[i] == '?':
        cnt[i] = alpha
        if cnt.count(cnt[i]) >= 2:
            cnt = '!'
            break

    elif cnt[i] != alpha:
        cnt = '!'
        break

else:
    while len(cnt) >= 2:
        n = cnt.pop(0)
        cnt.append(n)
        if n == target:
            break

print(''.join(cnt[::-1]))