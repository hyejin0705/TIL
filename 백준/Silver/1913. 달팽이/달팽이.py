N = int(input())

target = int(input())

arr = [[0]*N for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

num = N * N
si = -1
sj = k = 0

while num > 0:
    ni, nj = si + di[k], sj + dj[k]
    if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
        arr[ni][nj] = num
        si, sj = ni, nj
        if num == target:
            ans = [si + 1, sj + 1]
        num -= 1

    else:
        k = (k + 1) % 4

for lst in arr:
    print(*lst)
print(*ans)