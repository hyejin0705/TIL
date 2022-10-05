T = 10

for test_case in range(1, T + 1):
    N, string = input().split()

    stack = []

    for s in string:
        if not stack:
            stack.append(s)

        elif s == stack[-1]:
            stack.pop()

        else:
            stack.append(s)

    ans = ''.join(stack)

    print(f"#{test_case} {ans}")
