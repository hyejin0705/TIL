# [Silver II] Title: N과 M (9), Time: 140 ms, Memory: 35032 KB -BaekjoonHub

def dfs(n, ans):
    if n == M:
        check.add(tuple(ans))
        return

    for i in range(N):
        if not visited[i]:
            ans.append(lst[i])
            visited[i] = 1
            dfs(n + 1, ans)
            ans.pop()
            visited[i] = 0


N, M = map(int, input().split())

lst = list(map(int, input().split()))

check = set()
visited = [0] * N

dfs(0, [])

for i in sorted(list(check)):
    print(*i)




# -----------------------------------------------------------------
# [Silver II] Title: N과 M (9), Time: 96 ms, Memory: 30616 KB -BaekjoonHub

# N , M = map(int,input().split())
# List = sorted(list(map(int,input().split())))
# use_check = [True]*N
# Answer = []
 
# def bubun(idx):
#     if idx == M:
#         print(*Answer)
#         return
    
#     else:
#         last = 0
#         for i in range(N):
#             if use_check[i] and last != List[i]:
#                 use_check[i] = False
#                 Answer.append(List[i])
#                 last = List[i]
#                 bubun(idx+1)
#                 Answer.pop()
#                 use_check[i] = True
 
# bubun(0)
