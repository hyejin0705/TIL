import sys
from collections import deque

MIISS = lambda: map(int, sys.stdin.readline().strip().split())


def sol():
    q = deque([word])
    while q:
        tmp = q.popleft()
        if tmp != tmp[::-1]:  # 팬린드롬이 아니면
            return len(tmp)
        elif len(tmp) == 1:  # 한글자이면 그만 두게
            return 1

        q.append(tmp[1:])
        q.append(tmp[:-1])

    return -1


word = sys.stdin.readline().strip()

flag = False  # 답이 존재하지 않지 -않는다.
if len(word) == 1:
    flag = True  # 답이 존재하지 않는다.

first_string = word[0]
for i in range(1, len(word)):
    if word[i] != first_string:
        break
else:
    flag = True  # 답이 존재하지 않는다.

if flag == True:
    print(-1)

else:
    print(sol())