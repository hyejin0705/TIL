N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    # red
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    # Green
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    # Blue
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])

print(min(arr[N-1]))