pri = {'(': -1, '+': 1, '-':1, '*': 2, '/':2, ')': 3}

st = list(input())      # 수식 받기

stack = []              # 연산자 담을 리스트

ans = ''                # 후위표현식

for s in st:
    if pri.get(s, 100) == 100:    # 피연산자라면, ans에 담기
        ans += s

    else:
        # ')'가 나오면, 여는 괄호가 나올 때까지 pop()
        if pri[s] == 3:
            while stack and pri[stack[-1]] > 0:
                ans += stack.pop()
            stack.pop()             # 여는 괄호 삭제

        # '('가 나오면, 그냥 저장.
        elif pri[s] < 0:
            stack.append(s)
            continue

        # 0 < pri[s] < 3 : 즉, '+', '*'가 나오면,
        else:
            # 연산자가 존재하고, 우선순위가 낮다면, 높은 게 나올 때까지 꺼냄.
            while stack and pri[s] <= pri[stack[-1]]:
                ans += stack.pop()
            stack.append(s)         # 반복이 끝나면, 저장.

while stack:              # 혹시 모르는 예외처리
    ans += stack.pop()

print(ans)