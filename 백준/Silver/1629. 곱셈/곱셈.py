# 분할정복(Divide and Conquer) 문제
# 10 ^ 11 % 12
# ((10 ^ 5) * (10 ^ 5) * 10) % 12
# (((10 ^ 2) ^ 2 * 10) ^ 2 * 10) % 12

import sys

def dac(a, b, c):
    if b == 1:
        return a % c    # 그냥 나머지 구하기

    else:
        # 일단, 함수를 돌리고, ^2하기
        check = dac(a, b//2, c) ** 2

        if b % 2:                # 지수가 홀수이면,
            return check * a % c   # a 곱하고, 나머지 구하기

        else:                  # 지수가 짝수이면,
            return check % c    # 바로 나머지 구하기


N, M, K = map(int, sys.stdin.readline().split())

ans = dac(N, M, K)

print(ans)



# ------------------------------------------------------------------
# 시간초과 코드

# 너무 단순하게 생각해서 풀었더니... 시간초과 발생ㅜㅠ

# N, M, K = map(int, sys.stdin.readline().split())
# print(N ** M % K)
