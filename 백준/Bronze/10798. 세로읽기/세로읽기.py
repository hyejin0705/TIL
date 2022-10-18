arr = [input() for _ in range(5)]
sols = ''
for j in range(15):              # 최대 15글자
    for i in range(5):           # 항상 5줄
        if j < len(arr[i]):      # 확인 후 사용
            sols += arr[i][j]

print(sols)