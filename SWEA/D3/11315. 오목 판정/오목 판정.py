def solve():
    for i in range(N):          # 모든 행, 열 검색
        for j in range(N):
            for di, dj in ((0, 1), (1, 0), (1, 1), (-1, 1)):   # 4방향 (-, |, /, \)  
                for m in range(5):
                    ni, nj = i + di * m, j + dj * m      # 5번 이동,  5개가 o이면 성공, 아니면 실패

                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        continue
                    
                    else:
                        break
                else:
                    return "YES"          # break가 발동하지 않았으면, 성공
    else:
        return "NO"					     # 'o' 5개 발견 break가 발동하지 않았으면, 실패. 


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = [input() for _ in range(N)]

    ans = solve()

    print(f'#{test_case} {ans}')