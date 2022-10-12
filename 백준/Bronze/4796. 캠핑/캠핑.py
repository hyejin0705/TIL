# 캠핑장을 연속하는 P일 중, L일동안만 사용
# 강산이는 이제 막 V일짜리 휴가를 시작
case = 0
while True:
    L, P, V = map(int,input().split())
    case += 1

    if L == P == V == 0:
        break

    ans = L * (V // P)     # 휴가 // 연속 P일

    if V % P < L:         # 나머지가 L일보다 작다면,
        ans += V % P      # 나머지 더하고
    else:
        ans += L          # L일 더해주기

    print(f'Case {case}: {ans}')