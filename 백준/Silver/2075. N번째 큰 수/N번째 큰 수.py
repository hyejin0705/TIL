N = int(input())

ans = list(map(int, input().split()))
ans.sort(reverse = True)
for _ in range(1, N):
    check = list(map(int, input().split()))
    for j in range(N):
        if min(ans) <= check[j]:
            ans.append(check[j])
            ans.sort(reverse=True)
            ans.pop()

print(ans[N-1])