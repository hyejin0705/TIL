N, K = map(int, input().split())   # N: 전체 수, K : 일

lst = list(map(int, input().split()))

mx_ans = num = sum(lst[:K])
for idx in range(len(lst) - K):
    # num = sum(lst[idx: idx+K])    # 시간초과
    num -= lst[idx]             # 처음꺼 빼고
    num += lst[idx+K]           # 뒤에꺼 더하면서
    mx_ans = max(mx_ans, num)      # 최대값 갱신

print(mx_ans)