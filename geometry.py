import math


class Shape:
    """
    This is a abstract class representing geometrical shape.
    """

    def get_area(self):

        return self.area

    def get_perimeter(self):

        return self.perimeter

    def __str__(self):

        classname = self.__class__.__name__
        area = self.get_area
        perimeter = self.get_perimeter

        return self.__class__.__name__ + " wpisz inne atrybuty" + str(self.area)

    @classmethod
    def check_if_args_not_below_zero(cls, *args):

        if list(map(abs, args)) != list(args):
            raise ValueError

    @classmethod
    def get_area_formula(cls):

        area_formulas = {"Circle": "π×r^2",
                         "Triangle": "√s(s−a)(s-b)(s−c)",
                         "EquilateralTriangle": "(a^2x√3)/4",
                         "Rectangle": "axb",
                         "Square": "a^2",
                         "RegularPentagon": "a^2xsqrt(5(5+2sqrt(5))))/4"}

        return area_formulas

    @classmethod
    def get_perimeter_formula(cls):

        perimeter_formulas = {"Circle": "2×π×r",
                              "Triangle": "a + b + c",
                              "EquilateralTriangle": "3xa",
                              "Rectangle": "2a + 2b",
                              "Square": "4xa",
                              "RegularPentagon": "5xa"}

        return perimeter_formulas


class Circle(Shape):

    r = 0.0

    def __init__(self, r):

        Shape.check_if_args_not_below_zero(r)

        self.r = r

        self.area = math.pi * r ** 2
        self.perimeter = 2 * math.pi * r


class Triangle(Shape):

    a = 0.0
    b = 0.0
    c = 0.0

    def __init__(self, a, b, c):

        Shape.check_if_args_not_below_zero(a, b, c)

        self.a = a
        self.b = b
        self.c = c

        self.s = (self.a + self.b + self.c) / 2
        self.perimeter = self.a + self.b + self.c
        self.area = math.sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))

        if self.area == 0.0:
            print("Warning: impossible triangle")


class EquilateralTriangle(Triangle):

    a = 0.0

    def __init__(self, a):

        Triangle.check_if_args_not_below_zero(a)

        if a < 0:
            raise ValueError

        self.a = self.b = self.c = a

        self.s = (3 * self.a) / 2
        self.perimeter = 3 * self.a
        self.area = self.a ** 2 * (math.sqrt(3) / 4)


class Rectangle(Shape):

    a = 0.0
    b = 0.0

    def __init__(self, a, b):

        Shape.check_if_args_not_below_zero(a, b)

        self.a = a
        self.b = b

        self.perimeter = 2 * a + 2 * b
        self.area = a * b


class Square(Rectangle):

    a = 0.0

    def __init__(self, a):

        Rectangle.check_if_args_not_below_zero(a)

        self.a = a
        self.b = a

        self.area = 2 * a
        self.perimeter = 4 * a


class RegularPentagon(Shape):

    a = 0.0

    def __init__(self, a):

        Shape.check_if_args_not_below_zero(a)

        self.a = a

        self.area = (a ** 2) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) / 4
        self.perimeter = 5 * a


class ShapeList:

    shapes = []

    def __init__(self):

        self.shapes = []

    def add_shape(self, shape):

        if not isinstance(shape, (Circle, Triangle, EquilateralTriangle, Rectangle, Square, RegularPentagon)):
            raise TypeError

        self.shapes.append(shape)

    def get_shapes_table(self):

        return ",".join(str(i) for i in self.shapes)

    def get_largest_shape_by_perimeter(self):

        return sorted(self.shapes, key=lambda x: x.perimeter)[-1]

    def get_largest_shape_by_area(self):

        return sorted(self.shapes, key=lambda x: x.area)[-1]
