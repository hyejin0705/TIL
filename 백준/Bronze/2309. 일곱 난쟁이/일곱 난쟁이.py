lst = [int(input()) for _ in range(9)]

K = 100

for i in range(1, 1 << 9):         # 1 ~ 2^9
    total = 0
    result = []           # 리스트 재정의
    for j in range(9):
        if (i >> j) & 1:           # 포함한다면,
            total += lst[j]        # 누적합
            result.append(lst[j])  # 리스트에 저장

    # 누적합이 100이고, result의 요소가 7개라면
    if total == K and len(result) == 7:
        result.sort()              # 오름차순 정렬

        for n in result:
            print(n)        # 리스트의 원소 하나씩 출력

        # 가능한 정답이 여러 가지인 경우에는 아무거나 출력
        break