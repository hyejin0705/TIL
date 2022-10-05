lst = list(map(int, input().split()))

for idx in range(len(lst)-1, 0, -1):
    for j in range(idx):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            print(*lst)