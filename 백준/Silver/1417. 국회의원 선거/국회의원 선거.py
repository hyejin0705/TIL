N = int(input())

lst = []
D = int(input())   # 다솜(기호 1번)의 표

for _ in range(N-1):
    lst.append(int(input()))  # 다른 후보자들의 표

cnt = 0         # 매수해야 하는 사람의 수
while lst:             # 다른 후보자들이 존재할 때 반복
    if D > max(lst):   # 다솜이의 표가 가장 많다면, 종료
        break

    else:                           # 다른 후보의 표가 많다면,
        idx = lst.index(max(lst))   # 그 후보가 누구인지 찾고
        lst[idx] -= 1               # 후보 지지자 매수해서
        D += 1                      # 내 지지자 추가
        cnt += 1

print(cnt)