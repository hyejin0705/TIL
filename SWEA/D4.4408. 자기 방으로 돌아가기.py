# 4번의 Fail...
# Fail의 원인 : 앞 뒤 사람만 비교하면 안 됨. 전체적으로 비교해서 겹치지 않아야 함.
#               그리고, 구조상, (1, 2) (3, 4)가 마주보고 있음. (문제를 꼼꼼히 읽기ㅜㅜ)

T = int(input())
R = 400

for test_case in range(1, T + 1):
    N = int(input())  # 돌아가야 할 학생들의 수

    # 현재 방, 돌아가야 할 방 번호 리스트 생성
    root = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * (R//2)
    mx_n = 0
    for here, go in root:
        # here > go인 경우에는 표시가 안 될 수 있음.
        if here > go:
            here, go = go, here

        # 빈도수 표시
        for i in range((here - 1)//2, (go - 1)//2 + 1):
            cnt[i] += 1

    for n in cnt:
        if n > mx_n:
            mx_n = n

    print(f'#{test_case} {mx_n}')
