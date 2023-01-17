check = input()

ans = ['U', 'C', 'P', 'C']

for a in ans:
    if a in check:   # 문자열에 'UCPC' 해당 문자가 존재하면,
        check = check[check.index(a) + 1:]   # 문자열 재정의
    else:
        print('I hate UCPC')   # 없다면, 실패
        break

else:     # 중간에 종료되지 않고, 끝까지 돌았다면, 성공
    print('I love UCPC')
