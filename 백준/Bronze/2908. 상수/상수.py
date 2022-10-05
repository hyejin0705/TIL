lst = input().split()

num = [i[::-1] for i in lst]

m, n = num

print(max([int(m), int(n)]))
