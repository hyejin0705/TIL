N = int(input())
lst = list(map(int,input().split()))
result = [-1] * N
stack = []
for i in range(N):
    while stack and lst[i] > lst[stack[-1]]: # Step 2. 저장한 인덱스와 현재 비교
    # 스택이 비어있지 않고 / lst의 인덱스 스택[-1] < lst의 인덱스 i

        result[stack[-1]] = lst[i]

        stack.pop() # Step 3. 뺀 뒤에 반복

    stack.append(i) # Step 1. 인덱스를 저장하기
    
print(*result)