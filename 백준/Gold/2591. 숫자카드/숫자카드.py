num = input()
l = len(num)
num = '0'+num

if l == 1:
    print(1)
else:
    cnt = [0]*(l+1)

    cnt[1] = 1
    cnt[2] = 2 if 10 <= int(num[1:3]) <= 34 and num[2] != '0' else 1

    for i in range(3, l+1):
        if num[i] != '0':
            cnt[i] += cnt[i-1]
            if 10 <= int(num[i-1]+num[i]) <= 34:
                cnt[i] += cnt[i-2]
        else:
            if 10 <= int(num[i-1]+num[i]) <= 34:
                cnt[i] += cnt[i-2]

print(cnt[-1])