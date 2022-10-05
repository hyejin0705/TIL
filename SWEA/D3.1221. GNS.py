T = int(input())

# 숫자로 정렬이 가능하게 사전형식으로 만듦
num_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5,
            "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

for _ in range(1, T + 1):
    test_case, N = input().split()  # #1 7041(문자로)

    lst = input().split()

    num_lst = []  # 숫자 리스트 생성
    for key in lst:
        num_lst.append(num_dict[key])  # 사전의 키로 값(숫자)를 가져옴

    # 최소값이 앞쪽으로 위치하게 정렬하기
    for i in range(int(N)):
        min_idx = i
        for j in range(i + 1, int(N)):
            if num_lst[min_idx] >= num_lst[j]:
                min_idx = j
        
        # 최소값 인덱스를 찾으면, 숫자 리스트를 변경하는 게 아니라 원본 리스트를 변경하기.
        # 변경이 되지 않아서, 숫자 리스트 정렬하고
        num_lst[i], num_lst[min_idx] = num_lst[min_idx], num_lst[i]
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    print(test_case)
    print(*lst)

    # 처음 코드...

    #     # 최소값 인덱스를 찾으면, 숫자 리스트를 변경하는 게 아니라 원본 리스트를 변경하기.
    #     # 변경이 되지 않아서, 숫자 리스트 정렬하고
    #     num_lst[i], num_lst[min_idx] = num_lst[min_idx], num_lst[i]

    # # 따로 문자 리스트 정렬
    # result = []
    # num = list(num_dict.keys())
    # for idx in num_lst:
    #     result.append(num[idx])

    # print(test_case)
    # print(*result)
