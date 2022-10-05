T = 10
pri = {'(': -1, '+': 1, '*': 2, ')': 3}

for test_case in range(1, T + 1):
    _ = int(input())        # 수식의 길이

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
                

    for ch in ans:
        if pri.get(ch, 100) == 100:     # 숫자라면, stack에 저장
            stack.append(int(ch))

        else:
            # 순서 주의! : stack은 후입선출 방식.
            #              나중에 넣은 순서대로 빼낼 수 있음.
            b = stack.pop()
            a = stack.pop()
            if ch == '+':
                stack.append(a + b)

            # 문자열 계산식을 구성하는 연산자는 +, * 두 종류
            else:
                stack.append(a * b)

    print(f'#{test_case}', *stack)