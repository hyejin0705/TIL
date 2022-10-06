N = int(input())

lst = [0, 1, 2] * (N//3)

reset = lst[:]

P = list(map(int, input().split()))   # 정답

S = list(map(int, input().split()))   # 셔플

cnt = 0
change = [0] * N
while lst != P:
    for idx, ch in enumerate(S):
        change[idx] = lst[ch]

    cnt += 1
    lst = change[:]

    if change == reset:
        cnt = -1
        break

print(cnt)