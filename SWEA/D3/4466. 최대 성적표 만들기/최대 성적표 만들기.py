# 내장함수 사용X
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    score = list(map(int, input().split()))

    result = 0
    for idx in range(K):        # 내림차순 정렬을 K번만 실행
        mx_idx = idx            # 최대값을 찾아
        for j in range(idx, N):
            if score[mx_idx] <= score[j]:
                mx_idx = j

        result += score[mx_idx]   # 결과값에 더하고

        # 최대값이랑 맨 앞이랑 변경.
        score[mx_idx], score[idx] = score[idx], score[mx_idx]

    print(f'#{test_case} {result}')