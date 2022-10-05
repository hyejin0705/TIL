N = int(input())  # 스위치의 개수

arr = list(map(int, input().split()))  # 스위치들의 상태

M = int(input())  # 사람의 수

# 성별 및 스위치 규칙 : 남자는 배수 스위치, 여자는 대칭인 범위까지의 스위치들
lst = [list(map(int, input().split())) for _ in range(M)]

for s, idx in lst:
    if s == 1:
        for n in range(idx-1, N, idx):   # 인덱스는 0부터 시작이기 때문에, idx-1
            if arr[n] == 0:
                arr[n] = 1
            else:
                arr[n] = 0

    else:
        idx -= 1                       # 인덱스는 0부터 시작이기 때문에, idx-1
        for n in range(idx + 1):       # 양쪽을 확인해야 하기 때문에 idx까지 생성
            if idx + n < N:            # 범위확인

                if arr[idx - n] != arr[idx + n]:   # 같지 않다면, 바로 break
                    break

                else:                              # 같다면, 스위치 변경
                    if arr[idx - n] == 0:
                        arr[idx - n] = arr[idx + n] = 1
                    else:
                        arr[idx - n] = arr[idx + n] = 0
            
            else:            # 범위 밖을 나갔다면, break
                break

# 20번째에서 줄바꿈.
for i in range(N//20 + 1):
    print(*arr[20*i : 20*(i+1)])