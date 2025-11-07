from Shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x,y)
        if not isinstance(radius, (float, int)):
            raise ValueError("radius must be a number")
        self.radius = radius
        return None

    
    @property
    def area(self):
        return pi * (self.radius ** 2)
    
    @property
    def perimeter(self):
        return self.radius * pi * 2
    
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self.area == other.area                  #i could basically compare them as circ1.area == circ2.area without the method because its just two numbers genreally
    
    def __lt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("only areas of circles can be compared")
        return self.area < other.area
    
    def __gt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("only areas of circles can be compared")
        return self.area > other.area
    def __le__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("only areas of circles can be compared")
        return self.area <= other.area
    def __ge__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("only areas of circles can be compared")
        return self.area >= other.area 
    
#circ1 = Circle(5, 2, 6)

#circ1