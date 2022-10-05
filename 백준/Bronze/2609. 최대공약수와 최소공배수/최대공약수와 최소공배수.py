### 최종제출안

A, B = map(int, input().split())

num = 2   # 나누는 숫자
gcd = 1   # 최대공약수

# A와 B가 나누는 숫자보다 작아질 때까지 while문 계속
while A >= num and B >= num:
    if A % num == 0 and B % num == 0:   # A, B의 공통된 약수이면,
        gcd *= num                      # 최대공약수에 곱하기
        A /= num                        
        B /= num                        # A, B 재정의
    
    else:            # 공통된 약수가 아니라면, 1증가하여 다시 탐색.
        num += 1

lcm = gcd * A * B    # 최소공배수는 공통약수로 나눈 나머지 곱한 값
       
print(gcd)
print(int(lcm))      # 나눗셈으로 인해 float  >> int로 형변환



#### 첫번째 시도(+ 4번의 에러, 디버깅 ) ----------------------------------------------------------------
# 약수리스트 함수생성, pop() 활용한 방법.
# 서로소인 경우 고려, 작은 숫자가 큰 숫자와 나누어지는 경우 고려 등...
# 테스트 케이스나, 다른 반려들의 출력은 제대로 나왔는데, 결과는 틀렸다고 나옴ㅜㅜ
# 채점 10%가 되면 틀렸다고 나옴... 반려 및 이유를 찾을 예정...

# def div(N):
#     lst = [1, ]
#     n = 2               # 2부터 시작.
#     while N > 1:        # 입력숫자가 1보다 크다면, 반복.
#         if N % n == 0:  # 나눠서 0이 된다면,
#             lst.append(n)    # 나눈 숫자를 출력하고,
#             N /= n      # 나눈 수로 재정의.
#         else:
#             n += 1      # 아니면, 숫자를 더해 다시 시도.
    
#     return lst

# A, B = map(int, input().split())

# if not max([A, B]) % min([A, B]):  # 나누어 떨어지는 경우
#     gcd = min([A, B])              # 작은 쪽이 최대공약수
#     lcm = max([A, B])              # 큰 쪽이 최소공배수

# else:
#     a_lst = div(A)    # 함수호출: 약수리스트 만들기
#     b_lst = div(B)    # 함수호출: 약수리스트 만들기

#     gcd = 1   # 최대공약수
#     lcm = 1   # 최소공배수

#     for a in a_lst:         # A의 약수들을 하나씩 곱하기 (최소공배수)
#         lcm *= a                     
#         for idx, b in enumerate(b_lst):  
#             if a == b:              # A의 약수와 B의 약수가 같다면,
#                 g = b_lst.pop(idx)  # b_lst에서 빼고
#                 gcd *= g            # 공통된 약수 곱하기 (최대공약수)


#     while b_lst:            # B의 약수들이 남아있다면,
#         lcm *= b_lst.pop()  # b_lst에서 빼서 최소공배수에 곱하기

# # print(gcd, lcm, sep = '\n')
# print(gcd)
# print(lcm)
