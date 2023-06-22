from collections import deque

N, K = map(int, input().split())
L = list(input().split())

visitedS = set("".join(L))
q = deque([["".join(L),0]])

ans = -1
while(q):
    word, cnt = q.popleft()
    tempL = list(word)

    # 오름차순이면 그만
    if tempL == sorted(tempL):
        ans = cnt
        break

    isFirst = False
    
    # i를 뒤집기
    for i in range(N - K+1):
        newL = list(tempL)
        targetL = newL[i:i+K]
        targetL.reverse()
        
        for j in range(K):
            newL[i + j] = targetL[j]
            
        newWord="".join(newL)
        
        if newWord not in visitedS:
            visitedS.add(newWord)
            q.append([newWord, cnt+1])

print(ans)
