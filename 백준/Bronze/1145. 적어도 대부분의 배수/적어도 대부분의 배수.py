## python3 이용시 - 30840kb   740ms
## pypy 이용시 -   114976kb   192ms

## pypy가 python3보다는 실행속도가 빨랐지만, 메모리 측면에서는 많음... 왜??

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

#----------------------------------------------------------------------
## N의 초기값을 1부터 시작하니 비효율적임.
## N의 초기값을 정하는 방법은??? (즉, 시간단축하는 방법)
