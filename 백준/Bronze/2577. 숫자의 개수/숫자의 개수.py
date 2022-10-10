total = 1
for _ in range(3):
    total *= int(input())

total = str(total)
for i in range(10):
    print(total.count(str(i)))