check = input()

ans = ['U', 'C', 'P', 'C']
for a in ans:
    if a in check:
        check = check[check.index(a) + 1:]
    else:
        print('I hate UCPC')
        break

else:
    print('I love UCPC')