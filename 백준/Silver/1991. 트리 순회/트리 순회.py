def travel(n):
    if n:        # 실행조건
        pre_lst.append(lst[n])   # 전위순회
        travel(ch1[n])
        in_lst.append(lst[n])    # 중위순회
        travel(ch2[n])
        post_lst.append(lst[n])  # 후위순회
        
        
N = int(input())    # 노드의 개수

# 1 ~ 26까지 알파벳 리스트 생성
lst = ['.', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
       'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
       'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
       'X', 'Y', 'Z']

# 위의 리스트를 기반으로 한 사전 생성
dic = {key: idx for idx, key in enumerate(lst)}

ch1 = [0] * (N + 1)    # 왼
ch2 = [0] * (N + 1)    # 오

for _ in range(N):
    P, L, R = input().split()
    
    # 사전으로 값 찾기
    p = dic.get(P)
    l = dic.get(L)
    r = dic.get(R)

    ch1[p] = l     # 왼 추가
    ch2[p] = r     # 오 추가

pre_lst = []    # 전위순회 리스트
in_lst = []     # 중위순회 리스트
post_lst = []   # 후위순회 리스트

travel(1)

print(*pre_lst, sep='')
print(*in_lst, sep='')
print(*post_lst, sep='')