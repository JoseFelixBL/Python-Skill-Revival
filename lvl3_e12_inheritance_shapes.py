"""
Inheritance: Shapes
    Create a base class `Shape` with a method `area()`.
    Derive classes `Rectangle` and `Circle` that inherit from `Shape` 
    and implement their own `area()` methods.
"""
import math
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def __str__(self):
        return f"Rectángulo: Base = {self.base}, Altura = {self.altura}"
    def area(self):
        return self.base * self.altura

class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio
    def __str__(self):
        return f"Círculo: Radio = {self.radio}"
    def area(self):
        return round(math.pi * (self.radio ** 2), 2)

forma_1 = Rectangle(4, 5)
forma_2 = Circle(3)
print(forma_1)
print(f"El área del rectángulo es: {forma_1.area()}")
print(forma_2)
print(f"El área del círculo es: {forma_2.area()}")