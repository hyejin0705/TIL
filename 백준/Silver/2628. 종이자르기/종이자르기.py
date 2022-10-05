W, H = map(int, input().split())  # 종이의 가로, 세로 길이

N = int(input())    # 가위질 횟수

ga = [0, H]         # 가로
se = [0, W]         # 세로
for _ in range(N):
    D, i = map(int, input().split())
    if D:               
        se.append(i)    # 방향체크해서 각자 리스트에 추가
    else:
        ga.append(i)

se.sort()
ga.sort()    # 오름차순으로 정렬

ans = 1      # 곱하는 거라 기본값 1

for lst in [se, ga]:
    result = []
    for idx in range(1, len(lst)):
        
        # 리스트 원소 앞에서 뒤를 뺀 값을 리스트에 추가
        result.append(lst[idx] - lst[idx-1])
    
    ans *= max(result)   # 완성된 리스트의 최대값(가로, 세로) 곱하기

print(ans)