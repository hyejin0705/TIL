N, K = map(int, input().split())

check = [i + 1 for i in range(N)]

idx = 0    # 제거 인덱스
ans = []   # 제거될 사람 담을 곳
for _ in range(N):
    idx += K - 1    # 인덱스이기 때문에, K-1
    if idx >= len(check):
        idx %= len(check)   # 2바퀴 돌 수 있기 때문에, 나머지로 저장
                            # 예) 제거: 3, 길이: 2

    ans.append(str(check.pop(idx)))

print('<', ', '.join(ans), '>', sep='')
