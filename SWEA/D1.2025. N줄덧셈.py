num = int(input())

if num <= 10000:  # 입력받는 숫자는 10000을 넘지 않는다.
    total = 0
    for i in range(1, num + 1):
        total += i
    print(total)

else:
    print("10000이하의 숫자를 넣어주세요.")
