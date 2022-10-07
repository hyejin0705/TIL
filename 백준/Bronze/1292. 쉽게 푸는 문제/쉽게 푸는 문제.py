lst = []
for i in range(1, 100):  # 1 ≤ A ≤ B ≤ 1,000
    lst += [i] * i       # 일정한 수열 리스트 생성

A, B = map(int, input().split())

print(sum(lst[A-1: B]))   # 인덱스는 0부터 시작, 끝에 번호는 미포함.