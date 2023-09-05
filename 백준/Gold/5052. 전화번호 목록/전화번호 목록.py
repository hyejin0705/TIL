import sys

t = int(sys.stdin.readline())
for _ in range(t):
	n = int(sys.stdin.readline())
	number = [sys.stdin.readline().strip() for _ in range(n)]
	number.sort()
	is_yes = True
	for i in range(1, n):
		if number[i].startswith(number[i-1]):
			is_yes = False
			break
	if is_yes: print("YES")
	else: print("NO")