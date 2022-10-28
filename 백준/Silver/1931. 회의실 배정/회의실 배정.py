## pypy로 돌리면, 2280 ms 나옴

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x: [x[1], x[0]])
# 디버깅: 끝나는 시간으로 정렬 -> 같다면, 시작하는 시간으로 정렬

cnt = 0
while lst:
    cnt += 1
    sh, eh = lst.pop(0)

    while lst and eh > lst[0][0]:    # 앞에 끝나는 시간보다 시작하는 시간이 작다면, 패스
        lst.pop(0)

print(cnt)
