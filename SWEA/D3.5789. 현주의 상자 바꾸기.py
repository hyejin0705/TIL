T = int(input())

for test_case in range(1, T + 1):
    N, Q = map(int, input().split())

    # 결과 카운팅 리스트 생성
    result = [0] * N

    # 작업의 인덱스 정보를 Q번만큼 받아서 리스트에 넣기 (2차 리스트)
    n_idx = [list(map(int, input().split())) for _ in range(Q)]

    # 인덱스 정보를 가져오면서, 작업순서(인덱스 1부터 시작)도 가져오기
    for i, idx_lst in enumerate(n_idx, start=1):  # enumerate 이용
        mn_idx, mx_idx = idx_lst

        # 최소 인덱스 -1 (0부터 시작이므로), 최대 인덱스 범위로 해서 하나씩 바꾸기
        for idx in range(mn_idx - 1, mx_idx):
            result[idx] = i

        # 2. 이중포문 없는 방법
        # 작은 인덱스 - 1(0부터 시작이므로) : 큰 인덱스로 슬라이싱해서 범위 추출
        result[mn_idx - 1: mx_idx] = [i] * (mx_idx - mn_idx + 1)
        # i의 개수를 mx_idx - mn_idx에다가 1를 추가

    print(f'#{test_case}', *result)
