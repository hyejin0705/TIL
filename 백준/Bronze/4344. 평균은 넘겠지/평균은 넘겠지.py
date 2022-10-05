T = int(input())

for test_case in range(1, T + 1):
    
    # 첫번째는 학생수, 나머지는 성적 : *lst(리스트로 생성가능)
    N, *score = list(map(int, input().split()))
    
    avg = sum(score)/N     # 평균

    cnt = 0
    for s in score:
        if s > avg:
            cnt += 1     # 평균 넘는 사람들 count
    
    # f-string에서의 소수점 표현 :.(소수점)f
    print(f'{cnt/N * 100:.3f}%')