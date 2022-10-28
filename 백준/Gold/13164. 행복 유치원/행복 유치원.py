N, K = map(int, input().split())

lst = list(map(int, input().split()))

ans = []
for idx in range(N-1):
    ans.append(lst[idx+1]- lst[idx])

ans.sort()

print(sum(ans[:N-K]))