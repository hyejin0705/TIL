N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    rank = 1
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            rank += 1
    print(rank, end=' ')
print()