for test_case in range(1, 11):
    num_len = int(input())
    build = list(map(int, input().split()))
 
    result = 0
    for i in range(2, num_len - 2):          # 0, 1, -2, -1 인덱스에는 0만 존재. 빼고 진행

        # 앞 뒤 2칸씩 5개의 숫자의 최댓값과 중간값이 같다면
        if build[i] == max(build[i-2 : i+3]):  

            # 중간값 빼고 양쪽 2칸의 값(4개의 값을 리스트로 담기)
            result_lst = build[i-2 : i] + build[i+1 :i+3]
            
            # 중간값 - 4개의 값들 중 최대값 : 조망권이 확보된 빌딩의 층 수
            result += build[i] - max(result_lst)
             
    print(f'#{test_case} {result}')



# max 사용하지 않은 방법

for test_case in range(1, 11):
    num_len = int(input())
    build = list(map(int, input().split()))
 
    result = 0
    for i in range(2, num_len - 2):
        # 앞 뒤 2칸과 중간의 빌딩과의 층수 비교로 중간값이 최대값임을 찾기.
        if (build[i] > build[i-2]) and (build[i] > build[i-1]) and (build[i] > build[i+1]) and (build[i] >build[i+2]):
             
            result_lst = build[i-2 : i] + build[i+1 :i+3]

            # 내장함수 max 대신에, 최대값 찾는 방법. 
            max_num = 0
            for num in result_lst:
                if max_num < num:
                    max_num = num
                     
            result += build[i] - max_num
             
    print(f'#{test_case} {result}')
