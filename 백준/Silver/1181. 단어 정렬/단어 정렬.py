## 시간을 줄이는 게 관건 : 최대한 sort, sorted 함수를 활용해서 정렬할 것!!!

N = int(input())

lst = [input() for _ in range(N)]

lst = list(set(lst))

lst.sort(key=lambda x: [len(x), x])
# 정렬 sort의 다중 기준 [메인 기준, 동순위 기준]

print(*lst, sep='\n')


## 시간 초과 예시

# N = int(input())

# lst = [input() for _ in range(N)]

# lst = list(set(lst))

# # lst.sort(key=lambda x: len(x))   # 길이순 정렬

# lst.sort()    # 사전 순 정렬

# for idx in range(len(lst)-1):          # 길이순 정렬
#     for j in range(idx, len(lst)):
#         if len(lst[idx]) > len(lst[j]):         # 길이가 작은 단어와 변경
#             lst[idx], lst[j] = lst[j], lst[idx]

#     print(lst[idx])
# print(lst[-1])
