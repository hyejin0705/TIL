check = input()

ans = ''
string = ''
idx = 0

while idx < len(check):
    if check[idx] == '<':
        ans += string[::-1] + check[idx]
        string = ''
        while check[idx] != '>':
            idx += 1
            ans += check[idx]

    elif check[idx] == ' ':
        ans += string[::-1] + ' '
        string = ''

    else:
        string += check[idx]

    idx += 1

ans += string[::-1]

print(ans)