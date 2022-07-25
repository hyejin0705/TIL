# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    x, y = position
    if M == 0:    # 위로
        x -= 1
    elif M == 1:  # 아래로
        x += 1
    elif M == 2:  # 왼쪽으로
        y -= 1
    else:        # 오른쪽으로
        y += 1
    
    return (0 <= x <= N-1) and (0 <= y <= N-1)


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0))) # True
    print(is_position_safe(3, 0, (0, 0))) # False
