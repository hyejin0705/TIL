n = int(input())
n_list = list(map(int,input().split()))

arrow = [0] * 1000001
cnt = 0
for i in range(n):
    if arrow[n_list[i]] == 0:
        cnt += 1
        arrow[n_list[i]-1] += 1
    else:
        arrow[n_list[i]] -= 1
        arrow[n_list[i]-1] += 1
print(cnt)