# 알고리즘 적용보다는 수학적인 로직 구현
# 이분탐색으로 푸는 문제라고 하는데... 이분탐색으로 풀어보기!!

import sys

N, M = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)   # 내림차순 정렬
lst.append(0)    # 마지막에 0 넣기

check = 0
for i in range(1, N + 1):
    check += (lst[i - 1] - lst[i]) * i    # (앞 - 뒤) * 나무의 수

    if check == M:         # 원하는 길이만큼 잘랐다면, 종료
        ans = lst[i]
        break

    elif check > M:        # 원하는 길이를 초과한다면,
        ans = lst[i] + (check - M) // i  # 초과한 길이 * 나무의 수
        break

print(ans)
