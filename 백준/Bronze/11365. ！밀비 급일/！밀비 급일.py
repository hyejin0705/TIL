while True:
    check = input().split()
    if check[0] == 'END':
        break
    else:
        for ch in check[::-1]:
            print(ch[::-1], end=' ')
        print()