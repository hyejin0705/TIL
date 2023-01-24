check = input()
N = len(check)

ans = set()
for idx in range(N):
    for i in range(N - idx):
        ans.add(check[i: i + idx + 1])

print(len(ans))