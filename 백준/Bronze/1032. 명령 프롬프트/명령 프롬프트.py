N = int(input())

lst = [list(input()) for _ in range(N)]

check = list(zip(*lst))

ans = ''
for i in range(len(check)):
    if len(set(check[i])) == 1:
        ans += check[i][0]
    else:
        ans += '?'

print(ans)