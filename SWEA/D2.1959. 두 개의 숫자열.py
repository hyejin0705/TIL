def mul(A, B):
    lst = [A, B]
    idx_1 = [len(A), len(B)].index(min(len(A), len(B)))  # 길이가 짧은 값 찾기 
                           # index : 값의 위치 알려줌

    if idx_1 == 0:
        idx_2 = 1
    else:
        idx_2 = 0
     
    min_lst = lst[idx_1]  # 길이가 짧은 값의 리스트
    max_lst = lst[idx_2]  # 길이가 긴 값의 리스트
 
    total_lst = []
    for i in range((len(max_lst) - len(min_lst)) + 1):
        total = 0    
        for j in range(len(min_lst)):
            total += min_lst[j] * max_lst[i + j]
        total_lst.append(total)
    return max(total_lst)   # 리스트의 최대값 추출
 
T = int(input())
 
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
 
    max_n = mul(A, B)   # 함수실행
     
    print(f'#{t} {max_n}')
