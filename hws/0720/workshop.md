1. 세로로 출력하기
    자연수 number를 입력받아, 1부터 number까지의 수를 세로로 한 줄씩 출력하시오.

   ```python

    num = int(input("자연수를 입력하세요 >>> "))

    for i in range(1, num + 1):
        print(i)
   ```


2. 가로로 출력하기
    자연수 number를 입력받아, 1부터 number까지의 수를 가로로 한 칸씩 띄어 출력하시오.

   ```python

    num = int(input("자연수를 입력하세요 >>> "))

    for i in range(1, num + 1):
        print(i, end = ' ')     # end = print결과 끝을 결정하는 parameter?        
                # end = ' ' print출력하고 한칸 뛰고 다음 print 값을 출력해라

    # 1 2 3 4 5 6 7 8 9 10
   ```


3. 거꾸로 세로로 출력하기
    자연수 number를 입력받아, number부터 0까지의 수를 세로로 한 줄씩 출력하시오.

   ```python

    num = int(input("자연수를 입력하세요 >>> "))

    for i in range(num, 0, -1):  # 큰값, 작은값, 1씩 감소
        print(i)
   ```


4. 거꾸로 출력해 보아요 (SWEA #1545)
    자연수 number를 입력받아, number부터 0까지의 수를 가로로 한 칸씩 띄어 출력하시오.
   ```python

    num = int(input("자연수를 입력하세요 >>> "))

    for i in range(num, -1, -1):  # 0까지 출력되야 하기 때문에 -1를 입력
        print(i, end = ' ')       # 5 4 3 2 1 0
   ```


5. N줄 덧셈 (SWEA #2025)
    입력으로 자연수 number가 주어질 때, 1부터 주어진 자연수 number까지를 모두 더한
    값을 출력하시오. 단, 주어지는 숫자는 10000을 넘지 않는다. 
    예를 들어, 주어진 숫자가 10일 경우 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55이므로, 출력해야 할 값은 55이다

   ```python

    num = int(input("자연수를 입력하세요 >>> "))

    if num <= 10000:  # 입력받는 숫자는 10000을 넘지 않는다.
        total = 0
        for i in range(1, num + 1):
            total += i
        print(total)

    else:
        print("10000이하의 숫자를 넣어주세요.")
   ```


6. 삼각형 출력하기
    자연수 number를 입력받아, 아래와 같이 높이가 number인 삼각형을 출력하시오.

   ```python

    num = int(input("자연수를 입력하세요 >>> "))

    for i in range(1, num + 1):
        result = (' ' * (7 - i)) + ('*' * i)  # 공백은 7 - i 만큼, *은 i만큼 출력
        print(result)
   ```


7. 중간값 찾기 (SWEA #2063 변형)
    중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다. 리스트 numbers에 입력된 숫자에서 중간값을 출력하라.

   ```python

    numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24, ]

    numbers.sort()

    idx = len(numbers) // 2

    if len(numbers) % 2:     # 길이가 홀수일 때는 중앙값이 존재.
        print(numbers[idx])

    else:                    # 짝수일 때는 중앙값이 2개 존재.
        print(numbers[idx - 1 : idx + 1])    # 64
   ```