def preorder(n):
    global cnt
    if n <= V:
        preorder(n*2)

        # 전위순회한 결과를 중위순회하면, 원래 트리의 값을 알 수 있음.
        ans[n] = lst[cnt]     
        cnt += 1
        
        preorder(n*2 + 1)


N = int(input())

V = 2 ** N - 1

lst = [0] + list(map(int, input().split()))

ans = [0] * (V + 1)
cnt = 1

preorder(1)

i = 1
for i in range(N):
    i = 2 ** i
    print(*ans[i: i*2])