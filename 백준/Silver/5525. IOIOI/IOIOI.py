# 시간초과 해결 => Pn의 규칙을 파악 ('IOI' * n)

import sys

N = int(sys.stdin.readline())

M = int(sys.stdin.readline())

check = sys.stdin.readline()

ans, cnt, i = 0, 0, 0
while i < M - 1:
    if check[i:i + 3] == 'IOI':    # Pn = 'IOI' * n
        cnt += 1
        i += 2
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
        continue

print(ans)


# # -----------------------------------------------------
# 부분점수 획득 : 50점
# 완전탐색 => 시간초과 

import sys

IO = 'IO'

N = int(sys.stdin.readline())

IOI = IO * N + 'I'

M = int(sys.stdin.readline())

idx = 2 * N + 1
check = sys.stdin.readline()
cnt = 0
for i in range(M - idx):
    if check[i : i + idx] == IOI:
        cnt += 1

print(cnt)
