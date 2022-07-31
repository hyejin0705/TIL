### 08_python_homework.md

1. Circle 인스턴스 만들기

```python
class Circle:
    pi = 3.14

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return Circle.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)
```

```python
circle = Circle(3, 2, 4)

print(circle.area()) #=> 28.26
print(circle.circumference()) #=> 18.84
```



2. Dog과 Bird는 Animal이다

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!'
```

```python
class Dog(Animal):
    def run(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')
```



3. Module Import

```
from fibo import fibo_recursion as recursion

recursion(4)
```

