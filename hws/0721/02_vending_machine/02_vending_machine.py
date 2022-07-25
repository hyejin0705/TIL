print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menus = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
budget = 0  # 자판기에 넣은 총 누적 금액

while True:
    print()
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))

# 1. 금액넣기
    if money < 0:
        print('금액은 1원 이상 넣어주세요.')

    elif money != 0:
        budget += money
        print(f'현재 누적 금액은 {budget}원입니다.')

# 2. 메뉴 출력
    else:
        if budget < min(costs):
            print(f'{budget}원으로 구매 가능한 메뉴가 없습니다.')
            break
        else:
            menu_lst = []
            print(f'{budget}원으로 구매 가능한 메뉴는 다음과 같습니다.')
            for idx, cost in enumerate(costs):
                if cost <= budget:
                    menu_lst.append(idx + 1)  # 인덱스 번호 리스트 생성
                    print(f'{idx + 1}. {menus[idx]} {cost}원')
            break

# 3. 메뉴선택
while True:
    num = int(input('구매하실 메뉴의 번호를 입력하세요.'))

    # 입력받은 숫자가 인덱스 번호 리스트에 존재한다면, 구매 성공
    if num in menu_lst:
        print(f'{menus[num-1]}를 구매하셨습니다.')
        print(f'거스름돈은 {budget - costs[num-1]}원입니다. 감사합니다.')
        break

    else:
        print(' 구매할 수 없는 메뉴입니다. ')
