# 킹의 위치, 돌의 위치, 이동횟수
king, stone, N = input().split()

dir_dict = {
    'R': (0, 1),        # 한 칸 오른쪽으로
    'L': (0, -1),       # 한 칸 왼쪽으로
    'B': (-1, 0),       # 한 칸 아래로
    'T': (1, 0),        # 한 칸 위로
    'RT': (1, 1),       # 오른쪽 위 대각선으로
    'LT': (1, -1),      # 왼쪽 위 대각선으로
    'RB': (-1, 1),      # 오른쪽 아래 대각선으로
    'LB': (-1, -1),     # 왼쪽 아래 대각선으로
}

# 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고,
# 행은 가장 아래가 1이고 가장 위가 8이다.
dir = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

ki = int(king[1]) -1    # 킹의 행 위치
kj = dir.index(king[0]) # 킹의 열 위치

si = int(stone[1]) -1    # 돌의 행 위치
sj = dir.index(stone[0]) # 돌의 열 위치

for _ in range(int(N)):   # 이동횟수만큼 반복
    d = input()
    di, dj = dir_dict[d]  # 이동방향

    ni, nj = ki + di, kj + dj   # 킹의 이동위치

    if 0 <= ni < 8 and 0 <= nj < 8:   # 킹의 위치가 체스판(8*8) 안에 존재
        if ni == si and nj == sj:     # 킹의 이동 위치가 돌의 위치와 같고
            if 0 <= si + di < 8 and 0 <= sj + dj < 8:   # 돌의 이동 위치가 체스판에 존재한다면,
                si += di      # 돌도 같이 이동
                sj += dj      # 돌도 같이 이동

            else:            # 돌을 이동했는데 밖에 나간다면,
                continue     # 다음 이동으로

        ki = ni    # 킹의 행 위치 재정의
        kj = nj    # 킹의 열 위치 재정의

print(dir[kj], ki + 1, sep='')   # 킹의 마지막 위치
print(dir[sj], si + 1, sep='')   # 돌의 마지막 위치
