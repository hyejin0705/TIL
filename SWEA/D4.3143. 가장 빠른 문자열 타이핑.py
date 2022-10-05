def length(str):
    cnt = 0
    for _ in str:
        cnt += 1
    return cnt

T = int(input())

for test_case in range(1, T + 1):
    string, target = input().split()

    N = length(string)   # 전체 문장의 길이
    M = length(target)   # 한묶음 타이핑의 길이

    cnt = 0   # 빈도수
    idx = 0   # 인덱스
    
    # 한묶음 단어를 찾으면 그 다음 인덱스부터 찾기 시작.
    while idx < N - M + 1:
        if string[idx : idx + M] == target:
            cnt += 1
            idx += M   # 인덱스를 다음 인덱스로 
        else:
            idx += 1

    # 최소 타이핑의 수
    # 전체 문장의 길이 - (한묶음의 개수 * 빈도수) + 빈도수
    result = N - (cnt * M) + cnt

    print(f'#{test_case} {result}')
