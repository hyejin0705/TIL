def binomial(n, k):
    res = 1
    for i in range(k):
        res = res * (n - i)
        res = res // (i + 1)
    return res
 
def catalan(n):
    c = binomial(2 * n, n)
    return c // (n + 1)
 
T = int(input())
 
for i in range(T):
    n = int(input())
    
    if n % 2 != 0:
        print(0)
        continue
        
    print(catalan(n // 2) % 1000000007)