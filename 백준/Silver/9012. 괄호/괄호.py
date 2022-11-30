N = int(input())

for _ in range(N):
    stack = []
    check = input()
    ans = "YES"

    for ch in check:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                ans = "NO"
                break

            else:
                stack.pop()

    if stack:
        ans = "NO"

    print(ans)