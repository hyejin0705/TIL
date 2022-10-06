def fibo_dp(n):
    zero[0], zero[1] = 1, 0
    one[0], one[1] = 0, 1

    for i in range(2, n + 1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]
    return

zero = [0] * 101
one = [0] * 101

fibo_dp(100)

T = int(input())
for _ in range(T):
    N = int(input())
    print(zero[N], one[N])