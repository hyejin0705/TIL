lst = list(map(int, input().split()))

N = cnt = 0
while cnt < 3:
    N += 1          # 반복하면서 하나씩 증가
    cnt = 0         # lst 내 약수 개수

    for idx in range(len(lst)):   # lst 반복
        if not N % lst[idx]:      # N의 약수이면,
            cnt += 1              # count
            if cnt >= 3:      # 약수가 3개 이상이면,
                break         # 종료

print(N)