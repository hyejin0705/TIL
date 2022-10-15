C, R = map(int, input().split())

lst = [[0] * C for _ in range(R)]   # C * R 행렬 생성

di = [1, 0, -1, 0]     # 하 우 상 좌 (좌표)
dj = [0, 1, 0, -1]

i = -1                # 초기값
j = N = idx = 0

### 코드 리팩토링 : 시간을 단축하기 위해 breakpoint 생성
target = int(input())       # 타겟번호

ans = []                    # 정답

if target > C * R:
    ans.append(0)

else:
    while N < target:           # 숫자가 목표번호가 되면, 종료
        ni = i + di[idx % 4]
        nj = j + dj[idx % 4]    # 움직일 인덱스 : 인덱스 + 방향

        # 범위 안의 인덱스이고, 값이 0이라면, 값을 채우기
        if 0 <= ni < R and 0 <= nj < C and lst[ni][nj] == 0:
            N += 1
            lst[ni][nj] = N
            i, j = ni, nj     # 값을 채우고 나면, 인덱스를 재정의

        else:            # 만약 범위 밖이고, 값이 있다면,
            idx += 1     # 방향 변경


    ans.append(j + 1)   # 마지막 값을 정답에 넣기
    ans.append(i + 1)   # 주의! lst는 [0,0]부터 문제는 [1, 1]이 시작.

print(*ans)


### 예전 코드

# while N < C * R:          # 숫자가 C * R과 같아지지 않을 때까지 반복
#     ni = i + di[idx % 4]
#     nj = j + dj[idx % 4]    # 움직일 인덱스 : 인덱스 + 방향
#
#     # 범위 안의 인덱스이고, 값이 0이라면, 값을 채우기
#     if 0 <= ni < R and 0 <= nj < C and lst[ni][nj] == 0:
#         N += 1
#         lst[ni][nj] = N
#         i, j = ni, nj     # 값을 채우고 나면, 인덱스를 재정의
#
#     else:            # 만약 범위 밖이고, 값이 있다면,
#         idx += 1     # 방향 변경
#
#
# target = int(input())       # 타겟번호
# ans = []                    # 정답
#
# for col in range(R):                  # 행 하나씩 조사
#     if target in lst[col]:            # 행에 타켓번호가 존재하면,
#         row = lst[col].index(target)  # 인덱스 번호 찾기
#
#         ans.append(row + 1)    # 정답에 넣고 반복 끝내기
#         ans.append(col + 1)
#         break
#
# else:
#     ans.append(0)   # 만약 타겟 번호가 존재하지 않으면, 0 출력
#
# print(*ans)