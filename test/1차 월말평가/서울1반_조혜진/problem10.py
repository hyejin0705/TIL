# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def get_final_position(N, mat, moves):
    for idx, one in enumerate(mat):
        if 1 in one:        # 1이 있는 리스트를 찾으면,
            y = one.index(1)  # 1이 있는 인덱스를 반환.
            x = idx
    for move in moves:
        if move == 0:
            x -= 1
        elif move == 1:
            x += 1
        elif move == 2:
            y -= 1
        else:
            y += 1

    # 범위 안에 있으면 [범위] 반환
    if (0 <= x <= N-1) and (0 <= y <= N-1):
        return [x, y]
    else:    
        return None   # 범위 밖에 존재하면 None 출력


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    N = 3
    mat = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ] 
    moves1 = [1, 1, 3]
    print(get_final_position(N, mat, moves1)) # [2, 1]
    
    moves2 = [1, 3, 3]
    print(get_final_position(N, mat, moves2)) # [1, 2]