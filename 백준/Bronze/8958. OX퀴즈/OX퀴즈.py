T = int(input())

for _ in range(T):
    check = list(input())

    result = cnt = 0
    for c in check:
        if c == 'O':     # 'O'가 나오면, count 1증가
            cnt += 1
            result += cnt  # 결과에 count 더하기
        else:
            cnt = 0      # 'X'나오면 count 갱신
    
    print(result)