import sys

N, K = map(int, sys.stdin.readline().split())
time = [[0]*(N+1), []]
s = 0

for _ in range(K):
    I, T = map(int, sys.stdin.readline().split())
    
    next_s = s^1
    time[next_s] = [0]*(N+1)
    for i in range(N+1):
        if time[s][i] > time[next_s][i]:
            time[next_s][i] = time[s][i]
        
        if time[s][i]:
            if i+T <= N and time[s][i]+I > time[s][i+T]:
                time[next_s][i+T] = time[s][i]+I
    
    if T <= N and I > time[s][T]:
        time[next_s][T] = I
    
    s ^= 1

print(max(time[s]))