N = int(input())

scores = list(map(int, input().split()))

result = sum(scores)/max(scores)/N*100

print(result)