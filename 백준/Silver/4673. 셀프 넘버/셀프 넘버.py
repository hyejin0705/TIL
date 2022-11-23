numbers = set(range(1, 10001))
remove_set = set()  # 생성자가 있는 숫자 set
for num in numbers :
    for n in str(num):
        num += int(n)
    remove_set.add(num)  # add: 집합에 요소를 추가할 때

self_numbers = sorted(numbers - remove_set)  # set의 '-' 연산자로 차집합을 구함
for self_num in self_numbers:  # sorted 함수로 정렬
    print(self_num)