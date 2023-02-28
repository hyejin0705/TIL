# 문제를 잘 읽어야...ㅜㅜ
# 0을 생각하지 못해서, 컴파일에러 발생ㅜ

def fibo_dp(n):
    table = [0] * (n + 1)
    table[0] = 0
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]

N = int(input())

if not N:
    print(0)
else:
    print(fibo_dp(N))
