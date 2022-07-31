### 08_python_workshop.md

#### 도형 만들기

* 좌측 상단 좌표 (1, 3)과 우측 하단 좌표 (3, 1)의 점으로 만든 사각형.

```python
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 


class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1  
        self.p2 = p2 
    
    def get_area(self):
        return abs((self.p2.x - self.p1.x) * (self.p2.y - self.p1.y))
    
    def get_perimeter(self):
        return (abs(self.p2.x - self.p1.x) + abs(self.p2.y - self.p1.y)) * 2 
    
    def is_square(self):
        return abs(self.p2.x - self.p1.x) == abs(self.p2.y - self.p1.y)
```



#### 명세

| 인스턴스 변수 | 타입 | 설명   |
| ------------- | ---- | ------ |
| x             | int  | x 좌표 |
| y             | int  | y 좌표 |



| 메서드   | 매개변수       | 반환값(타입) | 설명                                                         |
| -------- | -------------- | ------------ | ------------------------------------------------------------ |
| (생성자) | x 좌표, y 좌표 | 없음         | 인스턴스가 생성될 때, 전달받은 int 값들로<br />인스턴스 변수 x와 y를 초기화한다. |



* Rectangle 클래스에 대한 명세

  | 인스턴스 변수 | 타입           | 설명           |
  | ------------- | -------------- | -------------- |
  | p1            | Point 인스턴스 | 좌측 상단 좌표 |
  | p2            | Point 인스턴스 | 우측 하단 좌표 |

  | 메서드        | 매개변수                            | 반환값(타입)        | 설명                                                         |
  | ------------- | ----------------------------------- | ------------------- | ------------------------------------------------------------ |
  | (생성자)      | Point 인스턴스,<br />Point 인스턴스 | 없음                | 인스턴스가 생성 될 때 2개의 Point 인스턴스를 전달 받아, <br />인스턴스 변수 p1과 p2를 초기화한다. |
  | get_area      | 없음                                | 넓이(int)           | 사각형의 넓이를 계산하여 반환한다.                           |
  | get_perimeter | 없음                                | 둘레 길이(int)      | 사각형의 둘레 길이를 계산하여 반환한다.                      |
  | is_square     | 없음                                | 정사각형 유무(bool) | 사각형이 정사각형이면 True, 정사각형이 아니면 False를 반환한다. |

  ​		
