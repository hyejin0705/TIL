T = 10

for test_case in range(1, T + 1):
    N = int(input())

    st = list(input())

    pri = {'+': 1, '*': 2}  # 우선순위 lookup 테이블

    stack = []  # 연산자 담을 스택
    ans = []  # 정답

    # 수식에서 하나씩 검사
    for s in st:
        if s != '+' and s != '*':  # 연산자가 아니라면, 저장.
            ans.append(s)

        else:
            # 연산자라면, stack에 요소가 존재하고, * 다음에 + 가 들어온다면,
            while stack and pri[s] <= pri[stack[-1]]:
                top = stack.pop()
                ans.append(top)  # +가 나오거나, 스택에 요소가 없을 때까지 꺼내고, 저장.

            # 위의 조건에 충족되지 않거나, 반복이 끝나면, 그때 요소 추가.
            stack.append(s)

    # 마지막에 stack에 값이 존재한다면, 없을 때까지 꺼냄. (빈 스택 만듦.)
    while stack:
        top = stack.pop()
        ans.append(top)


    # 후위표현식에서 하나씩 꺼냄.
    for af in ans:
        if af != '*' and af != '+':  # 피연산자라면,
            stack.append(int(af))    # 정수로 변환하여 저장.

        else:                       # 연산자라면,
            a = stack.pop()         # 두 숫자 꺼내기
            b = stack.pop()

            if af == '*':           # 곱셈 연사자라면, 곱하고
                result = a * b
                stack.append(result)   # 결과저장.

            elif af == '+':         # 더하기면 더하고
                result = a + b
                stack.append(result)    # 결과저장.

    print(f"#{test_case} {result}")
