N = int(input())

K = int(input())   # N < K 인 경우도 존재함...

lst = list(map(int, input().split()))

lst.sort()

ans = []
for idx in range(N-1):
    ans.append(lst[idx + 1] - lst[idx])

# 앞뒤의 차이 리스트 생성
# [2, 3, 0, 1, 2]

if ans:
    for _ in range(K-1):
        ans[ans.index(max(ans))] = 0

        if sum(ans) == 0:
            break

print(sum(ans))