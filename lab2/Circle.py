from Shape import Shape
from math import pi
"""
Class representing a circle on a 2D (x,y) plane

Attributes: 
    radius: representing the radius of given circle
    x: x-cordinate of circles center
    y: y-cordinate of circles center

Properties:
    area(float): The area of given circle (read-only)
    perimeter: The perimeter(circumference) of given circle (read-only)

Methods:
    CircleCheck: Checks if object passed to this comparison is a circle, raises a TypeError if not.
    UnitCircleCheck: Checks if given circle is a unit circle by returning True if radius=1 and (x,y)cordinates are (0,0)

Overloaded comparison operators:
    Compares areas of circles with (==,<,>,<=,>=) operators

"""

class Circle(Shape):
    #Object initialization
    def __init__(self, radius:float, x:float=0.0, y:float=0.0):
        super().__init__(x,y)
        if not isinstance(radius, (float, int)):
            raise TypeError("Radius must be a number") 
        if radius <= 0: 
            raise ValueError("Radius must be bigger than 0")
        self.radius = radius

    #Area and perimeter properties
    @property
    def area(self):
        return pi * (self.radius ** 2)
    
    @property
    def perimeter(self):
        return self.radius * pi * 2
    
    #Cheks if instance is a circle
    def _circle_check(self, other):
        if not isinstance(other, Circle):   #to avoid DRY repeating line on each operator overload
            raise TypeError("only Circles can be compared")    
    
    #Operator overloading
    def __eq__(self, other):
        self._circle_check(other)
        return self.area == other.area
    
    def __lt__(self, other):
        self._circle_check(other)
        return self.area < other.area
    
    def __gt__(self, other):
        self._circle_check(other)
        return self.area > other.area
    
    def __le__(self, other):
        self._circle_check(other)
        return self.area <= other.area
    
    def __ge__(self, other):
        self._circle_check(other)
        return self.area >= other.area 
    
    #Checks if instance is a unit circle
    def unit_circle_check(self) -> bool:
        if self.radius == 1 and self.x == 0 and self.y == 0:
            return True
        return False
