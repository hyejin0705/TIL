N = int(input())
lst = list(map(int, input().split()))

check = lst[:]

for i in range(1, N):
    for j in range(i):
        # 비교할 숫자보다 크면
        if lst[i] > lst[j]:
            check[i] = max(check[i], check[j] + lst[i])

print(max(check))