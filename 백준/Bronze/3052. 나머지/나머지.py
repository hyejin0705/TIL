lst = [int(input()) for _ in range(10)]

num = [n % 42 for n in lst]

print(len(set(num)))
