N = int(input())

if N < 10:          # 한자리수라면, 10를 더함.
    N *= 10

x = N // 10         # 몫 : 10의 자리
y = N % 10          # 나머지 : 일의 자리

a = y
b = (x + y) % 10    # 합의 일의 자리

cnt = 1             # 빈도수
if a != b:          # 0의 경우 a = b 같음.
    while True:

        # a는 b로, b = 합의 일의자리로 재정의
        a, b = b, (a + b) % 10
        cnt += 1    
        if a == x and b == y:   # 만약 처음 숫자와 같다면,
            break               # while 종료
    
print(cnt)