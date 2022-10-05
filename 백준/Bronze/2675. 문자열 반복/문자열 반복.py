T = int(input())

for _ in range(T):
    N, string = input().split()

    for s in string:
        print(s * int(N), end = '')  # 나란히 붙여서 출력
    print()                          # 다음 출력을 위해 한 줄 띄기
