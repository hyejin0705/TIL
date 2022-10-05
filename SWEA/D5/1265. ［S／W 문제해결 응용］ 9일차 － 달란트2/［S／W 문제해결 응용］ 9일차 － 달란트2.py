T = int(input())

# 달란트 수와 묶음의 수가 주어질 때 받을 수 있는 사탕의 최대 개수
# 최대한 똑같은 수로 곱했을 때
for test_case in range(1, T + 1):
    N, P = map(int, input().split())

    n = N//P     # 달란트를 묶음의 수로 나눈 몫
    m = N%P      # 달란트를 묶음의 수로 나눈 나머지

    if m == 0:        # 달란트가 나누어 떨어지면,
        ans = n**P    # 몫^P(묶음)

    else:
        ans = ((n)**(P-m)) * ((n+1)**m)
        # 몫^(묶음의 수 - 나머지) * 몫^(나머지)

    print(f'#{test_case} {ans}')