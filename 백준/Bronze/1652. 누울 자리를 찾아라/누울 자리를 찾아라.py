N = int(input())

arr = [list(input()) for _ in range(N)]

ans = 0
ans2 = 0
for i in range(N):
    cnt = 0
    cnt2 = 0
    for j in range(N):
        if arr[i][j] == '.':
            cnt += 1
            if cnt == 2:
                ans += 1
        else:
            cnt = 0

        if arr[j][i] == '.':
            cnt2 += 1
            if cnt2 == 2:
                ans2 += 1
        else:
            cnt2 = 0

print(ans, ans2)