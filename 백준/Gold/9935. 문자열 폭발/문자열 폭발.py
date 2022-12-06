import sys

check = list(sys.stdin.readline().strip())
remov = list(sys.stdin.readline().strip())
length = len(remov)
stack = []

for ch in check:
    stack.append(ch)
    # print(stack[-length:])   # out of range 에러 XXXX

    if stack[-length:] == remov:
        del stack[-length:]

if stack:
    print(''.join(stack))
else:
    print('FRULA')