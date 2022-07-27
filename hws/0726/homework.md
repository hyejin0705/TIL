1. Built-in 함수와 메서드
    sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

    ```python
    lst = [1, 3, 2, 8, 5]
    print(lst, lst.sort())  # [1, 2, 3, 5, 8] None

    lst = [1, 3, 2, 8, 5]
    print(lst, sorted(lst))  # [1, 3, 2, 8, 5] [1, 2, 3, 5, 8]
    ```

- sorted()와 .sort()의 차이점
    - .sort()는 리스트의 원본을 직접 정렬시켜주고, print하면 None값이 반환된다.
    - sorted()는 원본에 영향을 미치지 않고, 정렬된 리스트를 반환한다.


2. .extend()와 .append()
    .extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오

    ```python
    a = [1, 2, 3, 4]
    
    a.append(6)
    print(a)  # [1, 2, 3, 4, 6]

    a.append([6])
    print(a)  # [1, 2, 3, 4, 6, [6, 3]]


    a.extend(16)
    print(a)  # TypeError: 'int' object is not iterable

    a.extend([16])
    print(a)  # [1, 2, 3, 4, 6, [6, 3], 16]
    ```

- .extend()와 .append()의 차이점
    - .append()는 요소로서 추가할 수 있고,
    - .extend()는 추가할 대상이 iterable한 객체여야 한다. 
        즉, 숫자 하나만 넣으면 에러 발생, []같은 걸로 감싸줘야 추가 가능


3. 복사가 잘 된 건가?
    아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지 여부를 판단하고 그 이유를 작성하시오

    ```python
    a = [1, 2, 3, 4, 5]
    b = a

    a[2] = 5

    print(a)
    print(b)
    ```
- a, b의 출력결과가 같을 것이다. (a의 변경내역이 b에도 적용되었을 것이다.)
    왜냐하면, a의 경우 리스트자료형인데 b가 할당연산자(=)를 통해 얕은 복사를 했기 때문에, 같은 주소값을 가지게 되었기 때문입니다.
