import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @staticmethod
    def validate_number(value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected int or float type")
        if value <= 0:
            raise ValueError("Value must be a positive number.")


class Circle(Shape):
    def __init__(self, radius: int | float) -> None:
        self.validate_number(radius)
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


class Triangle(Shape):
    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        self.validate_number(a)
        self.validate_number(b)
        self.validate_number(c)
        if (a < b + c) and (b < a + c) and (c < a + b):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError(
                "Sum of any 2 sides of a triangle is greater than the 3 side")

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

# class Quadrangle(Shape):
#     def __init__(self, a, b, c, d, h):
#         """
#         Стороны a и c параллельны
#         Выстоа h проведенна к a
#         """
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.h = h

#     def is_trapeze(self) -> bool:
#         return self.a != self.c

#     def is_parallelogram(self) -> bool:
#         return not self.is_trapeze() and self.b == self.d

#     def is_rhomb(self) -> bool:
#         return self.is_parallelogram and self.a == self.b

#     def is_rectangle(self) -> bool:
#         return self.is_parallelogram() and self.h == self.b

#     def is_square(self) -> bool:
#         return self.is_rectangle() and self.a == self.b

#     def area(self) -> float:
#         if self.is_trapeze():
#             return (self.a + self.c)/2 * self.h
#         else:
#             return self.a * self.h


class ShapeFactory:
    @staticmethod
    def create_shape(*args):
        if len(args) == 1:
            return Circle(*args)
        elif len(args) == 3:
            return Triangle(*args)
        else:
            raise ValueError("Unknown shape type")
