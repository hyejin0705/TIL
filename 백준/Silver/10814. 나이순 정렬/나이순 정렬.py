N = int(input())

lst = [[] for _ in range(N)]
for idx in range(N):
    age, name = input().split()

    # 정렬의 기준: 나이, 가입한 순서(index)
    lst[idx] = [int(age), name, idx]

# 나이 순으로 정렬, 동순위일 경우, 먼저 가입한 순으로
lst.sort(key=lambda x: [x[0], x[2]])

for ans in lst:
    print(*ans[:-1])  # 인덱스를 제거하고 출력