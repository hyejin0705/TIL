N , M = map(int,input().split())
List = sorted(list(map(int,input().split())))
use_check = [True]*N
Answer = []
 
def bubun(idx):
    if idx == M:
        print(*Answer)
        return
    
    else:
        last = 0
        for i in range(N):
            if use_check[i] and last != List[i]:
                use_check[i] = False
                Answer.append(List[i])
                last = List[i]
                bubun(idx+1)
                Answer.pop()
                use_check[i] = True
 
bubun(0)