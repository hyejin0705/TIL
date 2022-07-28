1. 도형 만들기
    아래의 명세를 읽고 Python 클래스를 활용하여 점(Point)과 사각형(Rectangle)을 표현하시오.

```python
class Point:
    # 인스턴스가 생성될 때, 전달 받은 int 값들로 인스턴스 변수 x와 y를 초기화 한다.
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        # p1 = Position 클래스의 객체
        # p1.x, p1.y, p2.x, p2.y 이런 식으로 찾아들어가야 하나씩 꺼내올 수 있음.
        a = abs(self.p1.x - self.p2.x)
        b = abs(self.p1.y - self.p2.y)
        return a * b
    
    def get_perimeter(self):
        a = abs(self.p1.x - self.p2.x)
        b = abs(self.p1.y - self.p2.y)
        return (a + b) * 2        

    def is_square(self):
        a = abs(self.p1.x - self.p2.x)
        b = abs(self.p1.y - self.p2.y)
        return a == b

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())       # 4
print(r1.get_perimeter())  # 8
print(r1.is_square())      # True


p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())       # 9
print(r2.get_perimeter())  # 12
print(r2.is_square())      # True
```
