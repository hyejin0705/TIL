N = int(input())

check_dic = {}
for _ in range(N):
    check = input()

    if not check_dic.get(check[0], 0):
        check_dic.setdefault(check[0], 1)

    else:
        check_dic[check[0]] += 1

ans = []
for s, num in check_dic.items():
    if num >= 5:
        ans.append(s)

if ans:
    ans.sort()
    print(''.join(ans))
else:
    print('PREDAJA')
