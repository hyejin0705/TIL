# 시간초과 해결 >>>> stack 구조를 활용해야 한다. (+ 내장함수 del 활용)

import sys

check = list(sys.stdin.readline().strip())
remov = list(sys.stdin.readline().strip())
length = len(remov)
stack = []

for ch in check:
    stack.append(ch)
    # print(stack[-length:])   # out of range 에러 해결

    if stack[-length:] == remov:
        # stack = stack[-length:]      # 이 또한 시간초과
        del stack[-length:]        # 내장함수 del 활용하여 시간초과 해결!!!

if stack:
    print(''.join(stack))
else:
    print('FRULA')
    

# # ----------------------------------------------------
# # 시간초과
# # replace를 사용하니 시간초과 생김...ㅡㅜ

# str = sys.stdin.readline().strip()

# check = sys.stdin.readline().strip()

# while check in str:
#     str = str.replace(check, '')

# if str:
#     print(str)
# else:
#     print('FRULA')
