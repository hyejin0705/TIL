N = int(input())   # 피연산자의 수

# [1] 후위 표기식
ans = input()

# [2] 피연산자 숫자로 변경 사전 생성
dic = {}
for ch in ans:
    if ch not in ['-', '+', '*', '/'] and ch not in dic.keys():
        dic[ch] = int(input())


# [2] 후위 표기식 계산
stack = []  # stack 생성
for ch in ans:
    if dic.get(ch, 10000) != 10000:
        stack.append(dic.get(ch))

    else:
        B = stack.pop()  # 주의! stack에서 꺼낼 때, 나중에 들어간 게 먼저 나옴.
        A = stack.pop()

        # 사칙연산
        if ch == '+':
            stack.append(A + B)
        elif ch == '-':
            stack.append(A - B)
        elif ch == '*':
            stack.append(A * B)
        else:
            stack.append(A / B)


# [3] 소수점 표현

# 1. format 활용
print('{:.2f}'.format(*stack))

# 2. f-string 활용
# print(f'{stack[0]:.2f}')