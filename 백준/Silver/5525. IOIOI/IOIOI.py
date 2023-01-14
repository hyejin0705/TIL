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