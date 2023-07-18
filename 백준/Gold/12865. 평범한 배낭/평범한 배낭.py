import sys

n, k = map(int, sys.stdin.readline().split()) # 물건의 개수 n, 버틸수있는 무게 k
arr = [] # 물건 무게 가치 받아놓을 배열만들어놓기
for _ in range(n): # 물건의 개수만큼
    w, v = map(int, sys.stdin.readline().split()) # 무게, 가치
    arr.append([w, v])

d = [0 for _ in range(k + 1)]  # 무게 리스트

for item in arr: # arr에 담겨있는 item 하나씩 꺼내온다
    w, v = item
    # print(w, v)
    for i in range(k, w - 1, - 1): # 최대 무게부터 역순으로 물건 무게 체크
        d[i] = max(d[i], d[i - w] + v) # 해당 위치의 최대가치 d[i]와 들어갈 물건의 무게w만큼 뺸 d[i-w] + 가치 v를 더한값중 최대값 구하기
print(d[-1])