def fibo_dp(n):
	table[0] = 0
	table[1] = 1
	
	for i in range(2, n + 1):
		table[i] = table[i -1] + table[i - 2]
	return 

# append보다는 갱신이 실행속도가 빠름.
table = [0] * 101
fibo_dp(100)

N = int(input())
print(table[N])
            