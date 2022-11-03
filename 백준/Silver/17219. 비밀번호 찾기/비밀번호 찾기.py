## python Time: 10880 ms, Memory: 49788 KB
## pypy3 Time: 4936 ms, Memory: 140252 KB

## python의 시간초과의 가능성이 존재.  ->  해시 맵에 대해 공부하고 다시 제출하는 걸로...

## 풀이방법 >> lookup table를 통해 비밀번호 찾기

import sys

N, M = map(int, input().split())

dic = {}
for _ in range(N):
    a, b = sys.stdin.readline().split()
    dic[a] = b

for _ in range(M):
    check = input()
    print(dic[check])
    

    
##---------------------------------------------------------
## 첫번째 시도 -> 시간초과를 염두해서 풀음 
## 찾는 사이트를 받으면 -> 저장한 사이트 순회 (반복이 너무 많음)
## 그래서 저장한 사이트를 순회하면서, 찾는 사이트에 존재하면, index 찾아서 저장.

## 하지만 20%에서 틀림  >>>  만약 찾는 사이트가 중복되어 들어온다면, 찾을 수 없음.


# site = [sys.stdin.readline().split() for _ in range(N)]

# ans = [0] * M
# check = [input() for _ in range(M)]

# for idx in range(N):
#     if site[idx][0] in check:
#         i = check.index(site[idx][0])
#         ans[i] = site[idx][1]

# print(*ans, sep='\n')
