import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수
        
    while True :
        num = int(input("1이상 10000이하의 숫자를 입력하세요 >>> "))
        if (num >= 1) and (num <= 10000):
            if num == answer:
                counts += 1
                print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다.')
                is_playing = False
                break

            elif num > answer:
                print('Down!!')
                counts += 1
            else:
                print('Up!!')
                counts += 1                    

        else:
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.')
            
    replay = input('게임을 재시작하시려면 y, 종료하시려면 n을 입력하세요.')
    
    if replay == 'y':
        is_playing = True

    elif replay == 'n':
        print('이용해주셔서 감사합니다. 게임을 종료합니다.')
    
    else:
        print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')

