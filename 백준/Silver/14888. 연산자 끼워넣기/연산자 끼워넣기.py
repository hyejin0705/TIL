def dfs(n, sm, n1, n2, n3, n4):
    global mx, mn
    if n == N:
        mx = max(sm, mx)
        mn = min(sm, mn)
        return

    if n1:
        dfs(n + 1, sm + lst[n], n1 - 1, n2, n3, n4)
    if n2:
        dfs(n + 1, sm - lst[n], n1, n2 - 1, n3, n4)
    if n3:
        dfs(n + 1, sm * lst[n], n1, n2, n3 - 1, n4)
    if n4:
        dfs(n + 1, int(sm / lst[n]), n1, n2, n3, n4 - 1)
        # 나눗셈은 정수 나눗셈으로 몫만 취한다. -> // 사용?? NO!!
        # 음수일 경우 //를 사용하면, -1 값이 나옴.
        # 그래서 나눗셈 후 int로 형변환으로 정수부분으로 절삭해야 한다.


N = int(input())

lst = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

mx = -1e9   # -10억
mn = 1e9    # 10억

dfs(1, lst[0], add, sub, mul, div)

print(mx)
print(mn)