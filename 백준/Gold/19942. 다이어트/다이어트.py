def calculate(do, picked, pick_sum):
    global chosen, tot_prc
    if pick_sum[4] >= tot_prc:
        return
    for i in range(4):
        if req_nut[i] > pick_sum[i]:
            break
    else:
        chosen = picked.copy()
        tot_prc = pick_sum[4]
        return
    if do == n:
        return

    picked.append(do+1)
    for i in range(5):
        pick_sum[i] += nuts[do][i]
    calculate(do+1, picked, pick_sum)

    picked.pop()
    for i in range(5):
        pick_sum[i] -= nuts[do][i]
    calculate(do+1, picked, pick_sum)
    return


inf = 9876543210
n = int(input())
req_nut = tuple(map(int, input().split()))
nuts = tuple(tuple(map(int, input().split())) for _ in range(n))
chosen = []
tot_prc = inf

calculate(0, [], [0]*5)

if tot_prc == inf:
    print(-1)
else:
    print(tot_prc)
    print(*chosen)