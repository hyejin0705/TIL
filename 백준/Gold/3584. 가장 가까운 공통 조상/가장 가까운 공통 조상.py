import sys
        
def parent(a):
    p = []
    p.append(a)  # 자기 자신도 조상으로 포함
    for _ in range(N):
        if tree[a] == []:
            break
        else:
            p.append(tree[a])
        a = tree[a]    
    return p
        
T = int(input())
for _ in range(T):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    a_par = []
    b_par = []
    for _ in range(N-1):
        A, B = map(int, sys.stdin.readline().split())
        tree[B] = A   # 자신의 부모노드 저장
        
    a, b = map(int, sys.stdin.readline().split())
    a_par = parent(a)
    b_par = parent(b)
    
    common = [x for x in a_par if x in b_par]
    
    print(common[0])