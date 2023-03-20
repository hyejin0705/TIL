from collections import deque

T = int(input())
for tc in range(T):
    query = input()
    k = int(input())
    
    # deque에 담기
    q = deque(input()[1:-1].split(','))  # [1, 2, 3, 4]로 받음
    
    flag = 0           # flag: R(뒤집기)를 한 번만 실행하기 위함
    
    # TIP! deque는 [''] 의 길이를 0이 아닌 1로 취급하기 때문에 초기화 필요!
    if k == 0:  
        q = []
    
    for c in query:
        if c == 'R':
            flag += 1
        elif c == 'D':
            if len(q) == 0:
                print('error')
                break
            else:
                if flag % 2:
                    q.pop()
                else:
                    q.popleft()
                        
    else:
        if flag % 2:
            q.reverse()
        print('[' + ','.join(q) + ']')