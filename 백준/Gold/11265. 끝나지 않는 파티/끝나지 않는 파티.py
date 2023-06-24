import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for k in range(N):
    for n1 in range(N):
        for n2 in range(N):
            # arr[n1][n2] = min(arr[n1][n2], arr[n1][k] + arr[k][n2])
            if arr[n1][n2] > arr[n1][k] + arr[k][n2]:   # 시간개선: 위에 코드로 무작정 min연산 하지 말고, 조건문을 걸어준다.
                arr[n1][n2] = arr[n1][k] + arr[k][n2]

result = []
for _ in range(M):  # 시간개선: for i in range 대신 for _ in range를 쓴다.
    s, e, t = map(int, sys.stdin.readline().split())
    if arr[s-1][e-1] <= t:
        print('Enjoy other party')
    else:
        print('Stay here')