# 완전탐색 방법

N = int(input())  # 1m^2 당 참외 개수

# 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4

lst = []            # 방향과 변의 길이를 담을 리스트
mx_ga = mx_se = 0   # 가로길이의 최대길이, 세로 길이의 최대길이
for _ in range(6):
    lst.append(list(map(int, input().split())))   # 리스트에 추가

    if lst[-1][0] in [1, 2]:            # 리스트에 마지막으로 추가한 요소들로 방향체크
        mx_ga = max(lst[-1][1], mx_ga)  # 가로길이의 최대길이 갱신

    else:
        mx_se = max(lst[-1][1], mx_se)  # 세로길이의 최대길이 갱신

ans = mx_ga * mx_se               # 정답 : 가로, 세로 최대길이의 곱 - 빈 네모 넓이
for idx in range(len(lst)-1):     # 2개씩 확인
    d, ga = lst[idx]

    # 방향이 2번째로 나오면, 앞의 길이와 곱하기 (완전탐색의 방식으로 방향을 조사해서 if문으로...)
    if (d == 2 and lst[idx + 1][0] == 4) or (d == 1 and lst[idx+1][0] == 3) \
            or (d == 4 and lst[idx + 1][0] == 1) or (d == 3 and lst[idx+1][0] == 2):
        _, se = lst[idx + 1]
        ans -= ga * se       # 빈 네모를 빼기
        break

else:                 # 만약 빈 네모 방향이 존재하지 않는다면,
    ga = lst[0][1]    # 첫번째 요소를 가로
    se = lst[-1][1]   # 마지막 요소를 세로로 지정
    ans -= ga * se    # 넓이를 뺀다.

print(ans * N)        # 면적만큼 참외 개수를 곱한다.
