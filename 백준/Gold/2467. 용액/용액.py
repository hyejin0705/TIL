value = 2000000000
N = int(input())
x, y = 0, 0
l = 0
r = N - 1

liquid = [int(x) for x in input().split()]
# 문제에서 이미 오름차순으로 정렬

while l < r:
    result = liquid[l] + liquid[r]

    if abs(result) <= value:
        x = liquid[l]
        y = liquid[r]
        value = abs(result)

    if result <= 0:
        l += 1

    else:        # result > 0
        r -= 1

print(x, y)