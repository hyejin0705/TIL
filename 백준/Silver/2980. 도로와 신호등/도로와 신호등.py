N, L = map(int, input().split())

sec = bef = 0          # 시간, 이전 신호등의 거리 초기화

for _ in range(N):
    # D는 신호등의 위치이며, R과 G는 빨간색, 초록색이 지속되는 시간
    d, r, g = list(map(int, input().split()))

    sec += d - bef    # 시간 = 신호등까지 거리 - 이전 신호등의 거리

    while True:
        # 시간 % (빨간불 + 초록불)의 나머지가 빨간불 초보다 작다면,
        if sec % (r + g) < r:     
            sec += 1            # 기다리기
            
        else:             
            break   # 빨간 불의 시간보다 크다면, 초록불 -> 그냥 지나가기

    bef = d      # 이전 신호등의 거리 초기화

sec += L - bef   # 마지막 신호등부터 길 끝까지 거리 더하기

print(sec)