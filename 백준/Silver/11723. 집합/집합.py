import sys

N = int(sys.stdin.readline())

ans = set()
for _ in range(N):
    temp = sys.stdin.readline().strip().split()  # all, empty는 단독으로 나옴.

    if len(temp) == 1:
        if temp[0] == 'all':
            ans = {i for i in range(1, 21)}

        else:
            ans = set()

    else:
        n = int(temp[1])

        if temp[0] == 'add':
            ans.add(n)
        elif temp[0] == 'remove':
            if n in ans:
                ans.remove(n)
            else:
                continue
        elif temp[0] == 'check':
            if n in ans:
                print(1)
            else:
                print(0)
        else:
            if n in ans:
                ans.remove(n)
            else:
                ans.add(n)