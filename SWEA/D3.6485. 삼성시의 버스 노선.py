T = int(input())  # 테스트 케이스

for test_case in range(1, T+1):
    N = int(input())  # 버스 노선 개수

    bus_lst = []   # 버스 노선의 처음과 끝을 담을 리스트 생성
    for _ in range(N):
        bus = list(map(int, input().split()))

        # N개의 버스 노선을 리스트에 추가(이중리스트)
        bus_lst.append(bus)  
    
    P = int(input()) # P: 버스 정류장의 수

    cnt = [0] * P  # 정류장 수만큼의 카운팅 리스트 생성

    for idx in range(P):
        C = int(input())   # 정류장 수만큼 정류장 불러오기
        
        # 버스 노선들의 처음과 끝 사이에 정류장 번호가 존재하면 1 추가
        for mn, mx in bus_lst: 
            if mn <= C <= mx:
                cnt[idx] += 1
    
    print(f'#{test_case}', *cnt)
