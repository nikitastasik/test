from abc import *

class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        # pass
        print('calc perimeter')

    def drag(self):
        print('Basic dragging functionality')

# s = Shape()

from math import *
class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f'Drawing triangle with sides: {self.a}, {self.b}, {self.c}')

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return  sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        super().perimeter()
        return self.a + self.b + self.c

    def drag(self):
        super().drag()
        print('Additional actions')

t = Triangle(10, 10, 10)
print(t.area())
t.drag()
print(t.perimeter())