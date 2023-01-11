N = int(input())
lst = list(map(int, input().split()))

check = [1] * N

for i in range(1, N):
    for j in range(i):
        # 비교할 숫자보다 작으면
        if lst[i] < lst[j]:
            # 숫자가 가지고 있는 길이+1과 자신이 길이를 비교(최대값 찾기)
            check[i] = max(check[i], check[j] + 1)

print(max(check))