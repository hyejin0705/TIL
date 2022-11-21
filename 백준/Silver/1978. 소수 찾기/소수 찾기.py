n = int(input())
data = list(map(int, input().split()))
count = 0

for x in data:
    if x > 1:         # 1은 소수가 아님
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            count += 1

print(count)
