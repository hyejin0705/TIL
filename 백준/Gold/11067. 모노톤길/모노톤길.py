import sys

t = int(sys.stdin.readline())

for i in range(t):   
    n = int(sys.stdin.readline())    
    answer = [[0, 0]]
    dic = {}
    
    for j in range(n):
        x, y = map(int, sys.stdin.readline().split())
        if x not in dic:
            dic[x] = list()
        dic[x].append(y)
        
    sdic = sorted(dic.items())

    for j in range(len(sdic)):
        sdic[j][1].sort()
        if answer[-1][1] != sdic[j][1][0]:
            sdic[j][1].sort(reverse = True)   
        for k in range(len(sdic[j][1])):
            answer.append([sdic[j][0], sdic[j][1][k]])
            
    m = list(map(int, sys.stdin.readline().split()))

    for j in range(1, len(m)):
        print(*(answer[m[j]]))