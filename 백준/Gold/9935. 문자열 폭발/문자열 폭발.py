string = list(input())
s = list(input())
stack = []
if len(s) == 1:
    for i in range(len(string)):
        if string[i] != s[0]:
            stack.append(string[i])
else:
    for i in range(len(string)):
        stack.append(string[i])
        if stack[-1] == s[-1] and stack[-len(s):] == s:
            for _ in range(len(s)):
                stack.pop()
print(''.join(stack)) if stack else print('FRULA')