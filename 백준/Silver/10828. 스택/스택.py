import sys

stack = []

N = int(sys.stdin.readline())

for _ in range(N):
    check = sys.stdin.readline().split()

    if check[0] == 'push':
        stack.append(check[1])
    elif check[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif check[0] == 'size':
        print(len(stack))
    elif check[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif check[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)