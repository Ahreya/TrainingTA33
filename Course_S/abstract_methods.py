from abc import ABC, abstractmethod

###### abstrtact classes and abstract methods #######

# abstract method = a method that must be implemented in a subclass
# Clasele abstracte sunt create din meta Clasa ABC, care apartine modulului abc(Abstract base class)

## Abstract method in python
# ca sa definim o metoda abstracta in Python, aceasta trebuie decorata cu decoratorul @abstractmethod.
# Trebuie importat din modulul abc, abstractmethod

class MyClass(ABC):

    @abstractmethod
    def mymethod(self):
        pass

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    # def perimeter(self):
    #     return self.side * 4



square = Square(2)