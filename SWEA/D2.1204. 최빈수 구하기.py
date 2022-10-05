# 내장함수 사용하지 않기!
T = int(input())

for _ in range(1, T + 1):
    test_case = int(input())

    # 1000명의 점수를 받기
    scores = list(map(int, input().split()))

    # 0 ~ 100점의 카운팅 리스트 생성
    c = [0] * 101

    # 점수들이 나오면, 카운팅 리스트[점수]의 1증가
    for score in scores:
        c[score] += 1

    # 최빈수 찾기 : count 함수를 사용하지 않기!
    max_cnt = 0
    
    # range(len(c))이여야 한다. 단, len 함수 사용 자제!
    for idx in range(100):  
        # 중복이 된다면, 큰 수를 출력해야 하기 때문에 >= 를 사용.
        if c[idx] >= max_cnt:
            max_cnt = c[idx]  # 계속 재정의하면서
            max_num = idx    # 최빈수 점수를 저장.

    print(f'#{test_case} {max_num}')
