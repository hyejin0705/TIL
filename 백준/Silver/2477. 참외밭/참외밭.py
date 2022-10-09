# 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
N = int(input())  # 1m^2 당 참외 개수

lst = []
mx_ga = mx_se = 0
for _ in range(6):
    lst.append(list(map(int, input().split())))

    if lst[-1][0] in [1, 2]:
        mx_ga = max(lst[-1][1], mx_ga)

    else:
        mx_se = max(lst[-1][1], mx_se)

ans = mx_ga * mx_se
for idx in range(len(lst)-1):
    d, ga = lst[idx]

    if (d == 2 and lst[idx + 1][0] == 4) or (d == 1 and lst[idx+1][0] == 3) \
            or (d == 4 and lst[idx + 1][0] == 1) or (d == 3 and lst[idx+1][0] == 2):
        _, se = lst[idx + 1]
        ans -= ga * se
        break

else:
    ga = lst[0][1]
    se = lst[-1][1]
    ans -= ga * se

print(ans * N)