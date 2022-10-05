N = int(input())

lst = list(map(int, input().split()))  # N개의 숫자

ans = high = low = 0
for idx in range(1, N):         # 앞의 숫자와 비교하기
    if lst[idx-1] >= lst[idx]:  # 같거나 작아지면
        low += 1                # 작아지는 수열 증가
        ans = max(ans, low)     # 그때그때 수열의 최대값 갱신

    else:                       # 커지면, 재정의
        low = 0

    if lst[idx - 1] <= lst[idx]:  # 같거나 크면,
        high += 1                 # 커지는 수열 증가
        ans = max(ans, high)      # 수열의 최대값 갱신
    else:
        high = 0                # 작아지는 순간, 재정의

print(ans + 1)     # 숫자의 개수는 + 1