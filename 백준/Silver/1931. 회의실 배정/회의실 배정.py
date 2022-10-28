N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x: [x[1], x[0]])
# 끝나는 시간으로 정렬 -> 같다면, 시작하는 시간으로 정렬

cnt = 0
while lst:
    cnt += 1
    sh, eh = lst.pop(0)

    while lst and eh > lst[0][0]:
        lst.pop(0)

print(cnt)