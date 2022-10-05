## 2안. 정답

T = int(input())

for test_case in range(1, T + 1):
    lst = list(input())
    
    # 레이저, 열리는 인덱스, 막대 인덱스 리스트 생성.
    laser_lst = []
    bar = []
    bar_lst = [] 
    cnt = 0
    for idx, ap in enumerate(lst):
        if ap == '(':                   # 열리는 게 있으면,
            bar.append(idx)             # 위치를 저장

        else:                           # 닫히는 게 나왔는데
            if lst[idx-1] == '(':       # 앞에 열리는 게 나왔으면
                laser_lst.append(idx)   # 레이저에 저장

                bar.pop()   # 그리고 저장된 열리는 인덱스 삭제

                cnt += len(bar)     # 남은 '(' 개수 세기
            
            else: 
                # 아니면, 열리는 인덱스 마지막 번호와, 같이 저장.
                bar_lst.append([bar[-1], idx])

                cnt += 1          # 닫히는 게 발견하면, 1증가

                bar.pop()   # 그리고 저장된 열리는 인덱스 삭제     


## 초안. 20개의 테스트 케이스를 돌리면, 시간초과 걸림.
## 이중 for문을 통해서 불필요한 반복문이 존재함. (이를 제거하고 실행.)

    #         bar.pop()   # 그리고 저장된 열리는 인덱스 삭제
 
    # result = 0 
    # for start, end in bar_lst:        
    #     cnt = 0
    #     for laser in laser_lst:
 
    #         # 막대의 시작과 끝 사이에 레이저가 존재한다면,
    #         if start <= laser <= end:
    #             cnt += 1               # 빈도수 1증가
                 
    #     # 레이저 한번에 두개로 쪼개지니깐, 빈도수 + 1저장
    #     result += cnt + 1              
 
    # print(f'#{test_case} {result}')

    print(f'#{test_case} {cnt}')
                
