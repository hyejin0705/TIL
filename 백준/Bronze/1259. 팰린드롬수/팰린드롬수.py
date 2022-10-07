for _ in range(100000):
    string = input()

    if string == '0':
        break

    if string == string[::-1]:
        print('yes')
    
    else:
        print('no')