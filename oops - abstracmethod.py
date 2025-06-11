from abc import ABC, abstractmethod

class car(ABC):
    @abstractmethod
    def milage(self):
        pass

    def coluor(self):  # This is a regular method (not abstract).
        print("white")

class tata(car):  # concrete subclasses of car.
    def milage(self):
        print("20 kmph")

class maruti(car):  # concrete subclasses of car.
    def milage(self):
        print("25 kmph")

obj1 = tata()
obj1.milage()
obj2 = maruti()
obj2.milage()
obj2.coluor()



print()
print("peremeter of ractangle")
from abc import ABC, abstractmethod
class ractangle(ABC):
    @abstractmethod
    def peremeter(self):
        pass

class p(ractangle):
    def __init__(self, l, w):
        self.l = l
        self.w = w
        self.c = 2 * (self.l + self.w)
        print("area of ractangle = ", self.c)

    def peremeter(self):
        return self.c

obj = p(10, 5)


print()
print("area of ractangle and perimeter of ractangle")
from abc import ABC, abstractmethod


class rectangle(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class math(rectangle):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def perimeter(self):
        self.result1 = 2 * (self.l + self.w)
        print("perimeter of rectangle =", self.result1)

    def area(self):
        self.result2 = self.l * self.w
        print("area of rectangle =", self.result2)


obj = math(5, 5)
obj.perimeter()
obj.area()
































