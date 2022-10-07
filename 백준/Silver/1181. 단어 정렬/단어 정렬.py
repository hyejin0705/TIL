N = int(input())

lst = [input() for _ in range(N)]

lst = list(set(lst))

lst.sort(key=lambda x: [len(x), x])
# 정렬 sort의 다중 기준 [메인 기준, 동순위 기준]

print(*lst, sep='\n')