import sys

T = int(sys.stdin.readline())
result = []
operator = [' ', '+', '-']

def recursion(now,ans):
    if now == n+1:
        calc(ans)
        return
    for o in operator:
      recursion(now+1,ans+o+str(now))

def calc(ans):
    tmp = ans.replace(' ','')
    if eval(tmp) == 0:
        result.append(ans)

for _ in range(T):
  n = int(input())
  recursion(2,'1') # N은 3부터
  result.append(' ')

print(*result, sep='\n')