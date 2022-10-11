N = int(input())

for _ in range(N):
    lst = list(map(int, input().split()))

    lst.sort()      # 오름차순 정렬

    print(lst[-3])   # 끝에서 3번째 출력