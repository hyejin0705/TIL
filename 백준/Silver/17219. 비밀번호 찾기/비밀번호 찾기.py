import sys

N, M = map(int, input().split())

dic = {}
for _ in range(N):
    a, b = sys.stdin.readline().split()
    dic[a] = b

for _ in range(M):
    check = input()
    print(dic[check])