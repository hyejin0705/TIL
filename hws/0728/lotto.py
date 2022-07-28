# 여기에 필요한 모듈을 추가합니다.
import random
import json

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []   # 로또번호 담을 빈리스트 생성


    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for _ in range(n):   # n번 반복하는 반복문 생성

            # random.sample(범위, 개수) : 범위에서 개수만큼 무작위 숫자를 가져와서 리스트로 반환
            self.number_lines.append(sorted(random.sample(range(1, 46), 6)))
            # sorted() : .sort()와 달리 정렬된 값을 반환


    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        # 내부의 함수를 불려올 때에도 클래스.함수명(인자)를 적어줘야 한다.
        year, month, day = Lotto.get_draw_date(draw_number)  
        print("="* 45)
        print(f"              제 {draw_number} 회 로또")
        print("="* 45)
        print(f"추첨일 : {year}/{month}/{day} (토)")
        print("="* 45)

        alpha = ['A', 'B', 'C', 'D', 'E']        # 출력할 때 A: B: 를 사용하기 위해 리스트에 담기

        ##### 디버깅
        # alpha의 값이 아니라 로또 리스트의 길이만큼 가져와야 몇 줄이든 결과를 볼 수 있음
        for idx, line in enumerate(self.number_lines):
            print(f'{alpha[idx]} : {line}')


    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        main_numbers, bonus_number = Lotto.get_lotto_numbers(draw_number)
        print("="* 45)
        print(f"당첨 번호 : {main_numbers} + {bonus_number}")
        print("="* 45)

        alpha = ['A', 'B', 'C', 'D', 'E']
        for idx, line in enumerate(self.number_lines):
            same_main_counts, is_bonus = Lotto.get_same_info(main_numbers, bonus_number, line)
            ranking = Lotto.get_ranking(same_main_counts, is_bonus)
            
            if ranking > 0:  # 랭킹이 0보다 크다면 당첨!! 결과 출력
                print(f'{alpha[idx]} : {same_main_counts}개 일치 ({ranking}등 당첨!)')
            else:
                if is_bonus:  # 보너스 일치 결과도 출력
                    print(f'{alpha[idx]} : {same_main_counts}개 + 보너스 일치 (낙첨)')
                else:
                    print(f'{alpha[idx]} : {same_main_counts}개 일치 (낙첨)')


    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        lotto_list = json.load(lotto_json)

        # "drwNoDate": "2022-07-09"
        date = lotto_list.get("drwNoDate").split('-')

        year, month, day = date  # 리스트 값만큼 변수를 할당하면 그대로 들어감.

        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        lotto_list = json.load(lotto_json) 

        main_numbers = []
        # 키값에서 drwt가 존재하면 값들을 담아주기 위해 item()으로 키-값의 쌍을 불러온다.
        for key, value in lotto_list.items():
            if key.startswith('drwt'):
                main_numbers.append(value)
        
        main_numbers.sort()  # 리스트 원본에 직접 정렬.

        bonus_number = lotto_list.get('bnusNo')

        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = 0
        for num in line:
            if num in main_numbers:  # 메인번호와 일치하면 일치개수를 하나씩 증가
                same_main_counts += 1
        
        is_bonus = bonus_number in line  # 보너스 번호 일치하는지 여부 

        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        # 1등 : 6개 번호 일치
        if same_main_counts == 6:
            ranking = 1
        
        # 2등 : 5개 번호 일치 + 보너스 번호 일치
        elif (same_main_counts == 5) and (is_bonus == True):
            ranking = 2

        # 3등 : 5개 번호 일치
        elif same_main_counts == 5:
            ranking = 3

        # 4등 : 4개 번호 일치
        elif same_main_counts == 4:
            ranking = 4
        
        # 5등 : 3개 번호 일치
        elif same_main_counts == 3:
            ranking = 5
        
        # 낙첨 : 2개 이하 번호 일치
        else:
            ranking = -1 
            #### 디버깅
            # test.py에서 6개가 틀리는 이유
            # 낙첨이면 ranking 값을 0이나 None 대신에 -1를 대입!!

        return ranking
