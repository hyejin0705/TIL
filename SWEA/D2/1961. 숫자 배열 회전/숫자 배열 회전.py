# 시계방향으로 90도 회전하는 리스트 생성
def turn(lst):
    result = []            # 결과 리스트
    for j in range(N):             # 열
        num = ''           # 문자열   
        for i in range(N):         # 행
            num += str(lst[i][j])  # 1열의 모든 행의 번호를 가져와서 문자열로 합치기
            
        result.append(num[::-1])   # 합친 문자열을 거꾸로 정렬해서 결과 리스트에 넣기
    return result


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    lst_90 = turn(lst)      # 90도 회전
    lst_180 = turn(lst_90)  # 180도 회전
    lst_270 = turn(lst_180) # 270도 회전

    print(f'#{test_case}')
    for idx in range(N):
        print(lst_90[idx], lst_180[idx], lst_270[idx])  # 결과도출
       

### 결과 도출을 위한 노트?

# 입력 리스트
# 1 2 3
# 4 5 6
# 7 8 9

# 90도 회전 180도   270도
#   741     987     369 
#   852     654     258 
#   963     321     147 
