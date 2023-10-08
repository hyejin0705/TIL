import sys

S = list(sys.stdin.readline().rstrip())
T = list(sys.stdin.readline().rstrip())

# T에서 S로 바꾼다고 생각하면 편함!
while len(S) != len(T):
    if T[-1] == "A":    # T의 마지막 문자가 "A"이면 pop
        T.pop()
    else:               # T의 마지막 문자가 "B" 이면 pop하고 뒤집기
        T.pop()
        T.reverse()

# 같으면 1 다르면 0 출력
if S == T:
    print(1)
else:
    print(0)