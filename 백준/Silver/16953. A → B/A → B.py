A, B = map(int, input().split())

cnt = 1
while B != A:     # 같아지는 순간 종료
    if B < A:         # B < A 보다 작으면, 실패 
        cnt = -1
        break

    if B % 10 == 1:    # 1의 자리 수가 1이면, 1제거
        B //= 10
        cnt += 1

    elif B % 2 == 0:   # 짝수이면, 2로 나누기
        B //= 2
        cnt += 1

    else:            # 무한루프로 시간초과 해결방안 >> 홀수일 경우, 실패..
        cnt = -1
        break

print(cnt)
