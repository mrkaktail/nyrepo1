from Shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, radius, x=0, y=0):
        super.__init__(Circle.x,Circle.y)
        if not isinstance(radius, (float, int)):
            raise ValueError("radius must be a number")
        self.radius = radius
        return f"Circle with radius:{self.radius}"

    @property
    def area(self):
        return pi * (self.radius ** 2)
    
    @property
    def perimeter(self):
        return self.radius * pi * 2

circ1 = Circle(5, 2, 6)