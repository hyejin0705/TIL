T = int(input())

for test_case in range(1, T + 1):
    st = input()

    N = len(st) // 3

    card = {'S': 13, 'D': 13, 'H': 13, 'C': 13}  # 카드 총 개수 사전 생성

    lst = []
    for i in range(N):
        n = i * 3
        lst.append(st[n: n + 3])  				# 카드 분리

        ans = []
    if len(set(lst)) < len(lst):  					# 중복되는 카드를 가지고 있으면, ERROR 출력
        ans.append('ERROR')

    else:  								# 중복되지 않으면,
        for l in lst:
            card[l[0]] -= 1 		 # 무늬가 나오면, 총 개수에서 하나 감소

        ans = card.values()  		# 카드의 개수(dict의 값)

    print(f'#{test_case}', *ans)