N = 500

# 1 ~ 500까지 0의 카운팅 배열 생성
# 5의 배수 나오면 count 1증가
# 디버깅 : 단, 5의 제곱이 나오면, count 지수만큼 증가

cnt = [0] * 501
zero_cnt = 0
for i in range(1, N + 1):

    # 500까지 총 5의 3제곱까지 등장.
    # 3제곱부터 거꾸로 확인 (제곱도 배수이기 때문에)
    for n in range(3, 0, -1):
        if not i % (5 ** n):
            zero_cnt += n
            break
    cnt[i] = zero_cnt

N = int(input())

print(cnt[N])