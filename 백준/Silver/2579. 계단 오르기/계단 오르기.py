N = int(input())

lst = [int(input()) for _ in range(N)]

ans = [[0, 0], [lst[0]]*2]

for idx in range(1, N):
    one = ans[idx][1] + lst[idx]
    two = max(ans[idx-1]) + lst[idx]
    ans.append([one, two])

print(max(ans[N]))