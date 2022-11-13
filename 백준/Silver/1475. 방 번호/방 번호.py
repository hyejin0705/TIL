# 카운트 배열 (0 ~ 9) 생성
lst = [0 for i in range(10)]

N = list(map(int, input()))   # 방번호 입력받기

for num in N:
    lst[num] += 1   # 방번호 하나씩 카운팅

# 6은 9를 뒤집어서 이용할 수 있고,
# 9는 6을 뒤집어서 이용할 수 있음
total = lst[6] + lst[9]     # 6와 9가 나온 총합
lst[6] = total // 2        # 6에는 2로 나눈 몫 입력
lst[9] = total - lst[6]    # 9에는 6의 값을 뺀 나머지 입력

print(max(lst))     # 카운팅의 최대값 출력