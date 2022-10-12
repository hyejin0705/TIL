import sys

def check():
    global ans

    for i in range(N):
        stack1 = [candy[i][0]]    # 맨 처음 값 넣어주기
        stack2 = [candy[0][i]]
        cnt1 = cnt2 = 1           # 카운트 변수

        for j in range(1, N):
            if candy[i][j] == stack1[-1]:   # 열 탐색: 같은 게 나오면
                cnt1 += 1                   # 카운트

                if ans < cnt1:
                    ans = cnt1

            else:
                cnt1 = 1     # 다르면, 초기화

            stack1.append(candy[i][j])      # 추가


            if candy[j][i] == stack2[-1]:   # 행 탐색 (위와 동일)
                cnt2 += 1

                if ans < cnt2:
                    ans = cnt2

            else:
                cnt2 = 1    # 다르면, 초기화

            stack2.append(candy[j][i])
            
    return


N = int(sys.stdin.readline())

candy = [list(sys.stdin.readline()) for _ in range(N)]

ans = 0

check()   # 아무것도 변경하지 않고 체크

for i in range(N):
    for j in range(N-1):
        if candy[i][j] != candy[i][j+1]:        # 다른 부분이 나오면,
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]  # 변경

            check()    # 사탕 개수 체크하고

            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]  # 원상복구

        if candy[j][i] != candy[j+1][i]:
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]

            check()

            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]

print(ans)