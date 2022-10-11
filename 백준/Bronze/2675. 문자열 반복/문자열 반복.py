T = int(input())

for _ in range(T):
    N, string = input().split()

    for s in string:
        print(s * int(N), end = '')
    print()