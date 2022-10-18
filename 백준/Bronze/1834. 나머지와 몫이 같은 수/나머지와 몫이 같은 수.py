N = int(input())
 
total = 0
for i in range(N):        # 나머지 == 0 ~ N-1 까지의 수
    total += (N * i) + i  # 나머지 i와 몫이 같은 수들의 누적합

print(total)
