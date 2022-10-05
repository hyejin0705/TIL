T = int(input())
 
for test_case in range(1, T + 1):
    
    # 2 <= N <= 10000000
    N = int(input())

    num_lst = [2, 3, 5, 7, 11]  # 약수 리스트 생성
 
    result = [0] * 5   # 결과 카운팅 리스트 생성

## 1. 이중 반복문 풀이
    # for idx, num in enumerate(num_lst):  # 인덱스와 약수를 동시에 생성
    #     while True:     
    #         if N % num == 0:   # 정수를 약수로 나눈 나머지가 0이면, 반복
    #             result[idx] += 1  # 결과 1증가
    #             N /= num          # 정수를 나머지 몫으로 재저장
    #         
    #         else:      # 정수가 더이상 약수로 나누어지지 않으면 반복 끝
    #             break


## 2. 반복문 하나 풀이
    idx = 0   # 첫 인덱스 0
    while idx < 5:  # 인덱스가 5 이상이면 break

        # 정수를 약수로 나눈 나머지가 0이면,
        if N % num_lst[idx] == 0:
            result[idx] += 1     # 결과 1 증가
            N /= num_lst[idx]    # 정수를 나머지 몫으로 재저장

        else: # 0으로 나누어지지 않으면, 다음 약수로 나누기 위해
            idx += 1  # 인덱스 1증가

    print(f'#{test_case}', *result)
