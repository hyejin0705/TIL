### 07_python_workshop.md

1. pip

   ```
   아래 명령어는 (1) 무엇을 위한 명령인지 (2) 실행은 어디에서 해야하는지 작성 하시오. 
   ```
   
   ```bash
   # 무엇을 위한 것인가
   faker 라는 패키지를 설치하기 위한 명령어
   
   # 실행은 어디서 해야하는가
   git bash에서 실행
   ```



2. basic usages ([https://github.com/joke2k/faker#basic-usage](https://github.com/joke2k/faker))

   ```
   Faker는 다양한 메서드를 통해 임의의 결과값을 반환해준다.
   임의의 영문 이름을 반환하는 아래 코드에서 라인별 의미를 주석을 참고하여 작성하시오.
   ```

   ```python
   from faker import Faker # 1 _______을 하기 위한 코드이다.
   fake = Faker()			# 2 Faker는 _____, fake는 ______이다.
   fake.name()				# 3 name()은 fake의 _____이다.
   ```

   ```
   # 1
   Faker 클래스를 faker 패키지에서 불러오기 위함
   
   # 2
   Faker는 클래스, fake는 Faker의 인스턴스
   
   # 3
   메서드
   ```

   

3. localization

   ```
   Faker는 다양한 언어의 Locale을 지원한다.
   1. 인자 없이 호출 시에는 영문이 기본 설정이다. (en_US)
   2. Locale 정보를 포함하여 호출 시에는 해당 언어 설정을 따른다.
   직접 해당하는 기능을 구현한다고 하였을 때, 빈칸 (a), (b), (c)에 들어갈 코드로 적절한 것을 작성하시오. (힌트: 생성자 메서드와 함수의 개념)
   
   ```

   ```python
   class Faker():
   
   		def __(a)__((b), (c)):
   				pass
   
   (a) init
   
   (b) self
   
   (c) locale='en_US'
   ```

   

4. seeding the generator(https://github.com/joke2k/faker#seeding-the-generator)
   
   ```
   컴퓨터 프로그래밍에서 임의의 값을 반환하는 경우(난수 생성 등) 시드라는 개념이 있다.
   
   시드를 설정하게 되면 동일한 순서로 난수를 발생시킬 수 있어 일반적으로 디버깅을 위하여 활용 된다.
   ```
   
   1. 아래의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고,seed()는 어떤 종류의 메서드인지 작성하시오.
   
      ```
      1. 이진호, 2. 강은주
      ```
   
      * seed()는 클래스 메서드에 해당한다.
   
   2. 아래의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고,  seed_instance()는 어떤 종류의 메서드인지 작성하시오.
   
      ```
      1. 이진호, 2. 랜덤배정
      ```
   
      * seed_instance는 인스턴스 메서드에 해당한다.

























