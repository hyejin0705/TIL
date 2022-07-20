T = int(input())
 
for t in range(1, T+1):
    N = int(input())
    alpha = ""
    for _ in range(N):
        Ci, Ki = input().split()
        alpha += Ci * int(Ki)
 
    print(f'#{t}')
    for i in range(0, len(alpha)+1, 10):
        print(alpha[i : i + 10])
