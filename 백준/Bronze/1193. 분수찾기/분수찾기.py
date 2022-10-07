N = int(input())

line = 0            # 대각선 줄
mx_num = 0          # 대각선 줄의 끝번호 
while mx_num < N:   # 끝번호보다 입력숫자가 작다면,
    line += 1       # 대각선 줄 1증가
    mx_num += line  # 끝번호 줄의 수 누적합

# 입력숫자의 대각선에서의 순서    
num = line - (mx_num - N)  

# 대각선 줄이 홀수라면, 분자가 더 크게 시작
if line % 2:
    result = f'{line - num + 1}/{num}'

# 대각선 줄이 짝수라면, 분모가 더 크게 시작
else:
    result = f'{num}/{line - num + 1}'

print(result)