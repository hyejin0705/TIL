N = input()

if int(N) >= 1 and int(N) <= 9999:
    # 리스트 안에는 total += int(i)는 안 되는 건가....
    N = [int(i) for i in N]
    
    total = 0
    for i in N:
        total += i
    print(total)
    
else:
    print('N값을 잘못 입력했습니다.')
