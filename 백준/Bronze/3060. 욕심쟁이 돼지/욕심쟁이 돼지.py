T = int(input())

for _ in range(1, T + 1):
    N = int(input())      # 사료의 양
    lst = list(map(int, input().split()))    # 첫날 돼지의 식사량

    day = 1            # 첫날은 이미 먹음.
    total = sum(lst)   # 총 돼지들의 식사량이
    while total <= N:  # 사료의 양보다 많을 때까지 반복
        day += 1       
        eat_lst = []   # 오늘 식사량
        for idx in range(len(lst)):
            
            # 홀수라면, 본인 + 짝수 인덱스의 돼지들의 식사량
            if idx % 2:
                today = lst[idx] + lst[0] + lst[2] + lst[4]
                
            # 짝수라면, 본인 + 홀수 인덱스의 돼지들의 식사량
            else:
                today = lst[idx] + lst[1] + lst[3] + lst[5]

            # 오늘 식사량에 추가
            eat_lst.append(today)
        
        # 다 돌았다면, 오늘 식사량 갱신.
        lst = eat_lst
        total = sum(eat_lst)    # 총 식사량 계산

    print(day)