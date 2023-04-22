n, h = map(int, input().split(' '))

data = []
for i in range(n):
  data.append(int(input()))

answer = [0] * (h + 1)
top = [0] * (h + 1)
bottom = [0] * (h + 1)

count = 0
for number in data:
  if count % 2 == 0:
    count += 1
    top[number] += 1
  else:
    count += 1
    bottom[h-number+1] += 1

for i in range(h - 1, 0, -1):
  top[i] += top[i + 1]

for i in range(1, h + 1):
  bottom[i] += bottom[i-1]

for i in range(1, h + 1):
  answer[i] = top[i] + bottom[i]

answer = answer[1:]
print(min(answer), answer.count(min(answer)))