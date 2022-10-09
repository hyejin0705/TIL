N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())

    ans = 0
    for n in range(i-1, x):
        ans += sum(arr[n][j-1: y])

    print(ans)