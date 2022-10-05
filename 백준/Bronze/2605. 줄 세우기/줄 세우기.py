N = int(input())       # 사람 수

lst = list(map(int,input().split()))    # 학생들이 뽑은 번호

result = []
for i in range(1, N + 1):        # 1 ~ N번의 학생
    idx = (i - 1) - lst[i-1]     # 번호가 인덱스의 반대
    result.insert(idx, i)        # insert(idx, x): idx 자리에 x 삽입.

print(*result)    # 출력주의!!