## 1. 내장함수 활용 없는 풀이방법
def mx(n, m):
    if n > m:
        return n
    else:
        return m


for _ in range(10):
    test_case = int(input())
    
    lst = [list(map(int, input().split())) for _ in range(100)]

    mx_num = 0  # 최대값

    sum1 = 0  # 대각선 정방향
    sum2 = 0  # 대각선 반대방향
    for i in range(100):
        sum1 += lst[i][i]    # (0,0) (1, 1).... 
        sum2 += lst[i][99 - i]  # (0, n-1) (1, n-2)...

        sum3 = 0   # 행의 합
        sum4 = 0   # 열의 합
        for j in range(100):
            sum3 += lst[i][j]  
            sum4 += lst[j][i]  # 행(i)과 열(j)의 위치를 바꾸어 방향 전환.

        mx_num = mx(sum3, mx_num)
        mx_num = mx(sum4, mx_num)
        
    mx_num = mx(sum1, mx_num)
    mx_num = mx(sum2, mx_num)

    print(f'#{test_case} {mx_num}')   



    #---------------------------------------------------------------------------
    # 2. 내장함수 활용
    for _ in range(10):
    test_case = int(input())
    
    lst = [list(map(int, input().split())) for _ in range(100)]

    total = []  
    sum1 = sum2 = 0 
    for i in range(100):
        sum1 += lst[i][i]    # (0,0) (1, 1).... 
        sum2 += lst[i][99 - i]  # (0, n-1) (1, n-2)...

        sum3 = sum4 = 0
        for j in range(100):
            sum3 += lst[i][j]  
            sum4 += lst[j][i]  # 행(i)과 열(j)의 위치를 바꾸어 방향 전환.
		
        total.append(max(sum3, sum4))

    total.append(max(sum1, sum2))

    print(f'#{test_case} {max(total)}')
