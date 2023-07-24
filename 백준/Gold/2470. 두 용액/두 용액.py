import sys
INF = 1e11

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

i = 0
j = len(arr) - 1
pair = []
min_val = INF
while i < j:
    tmp = arr[i] + arr[j]

    # 합의 절대값이 현재 상황에서 최솟값보다 작은 경우
    if abs(tmp) < min_val:
        pair = [arr[i], arr[j]]
        min_val = abs(tmp)

    # 0보다 큰지 작은지로 포인터 이동 판단
    if tmp >= 0:
        j -= 1
    else:
        i += 1

print(*pair)