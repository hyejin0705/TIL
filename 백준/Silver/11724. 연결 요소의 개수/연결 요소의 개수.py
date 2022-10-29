def find(a):
    while lst[a] != a:
        a = lst[a]
    return a


def union(a, b):
    lst[find(a)] = find(b)


# 정점의 개수 N과 간선의 개수 M
N, M = map(int, input().split())

lst = [i for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

ans = 0
for idx in range(1, N + 1):
    if idx == lst[idx]:
        ans += 1

print(ans)