from Shape import Shape
from math import pi
"""
Class representing a circle on a 2D (x,y) plane

Attributes: 
radius: representing the radius of given circle
x: x-cordinate of circles center
y: y-cordinate of circles center

Properties:
area: The area of given circle (read-only)
perimeter: The perimeter(circumference) of given circle (read-only)

Methods:
CircleCheck: Checks if object passed to this comparison is a circle, raises a TypeError if not.
UnitCircleCheck: Checks if given circle is a unit circle by returning True if radius=1 and (x,y)cordinates are (0,0)

Overloaded comparison operators:
Compares areas of circles with (==,<,>,<=,>=) operators

"""

class Circle(Shape):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x,y)
        if not isinstance(radius, (float, int)):
            raise ValueError("Radius must be a number") #type of arg error 
        if radius <= 0: 
            raise ValueError("Radius must be bigger than 0") #value of arg error
        self.radius = radius

    
    @property
    def area(self):
        return pi * (self.radius ** 2)
    
    @property
    def perimeter(self):
        return self.radius * pi * 2
    
    
    def CircleCheck(self, other):           #extended method to raies error if other is indeed a circle,
        if not isinstance(other, Circle):   #to avoid DRY repeating line on each operator overload
            raise TypeError("only Circles can be compared")    
    
    def __eq__(self, other):
        self.CircleCheck(other)
        return self.area == other.area                  #i could basically compare them as circ1.area == circ2.area without the method because its just two numbers genreally
    
    def __lt__(self, other):
        self.CircleCheck(other)
        return self.area < other.area
    
    def __gt__(self, other):
        self.CircleCheck(other)
        return self.area > other.area
    
    def __le__(self, other):
        self.CircleCheck(other)
        return self.area <= other.area
    
    def __ge__(self, other):
        self.CircleCheck(other)
        return self.area >= other.area 
    
    def UnitCircleCheck(self):
        if self.radius == 1 and self.x == 0 and self.y == 0:
            return True
        return False
    
#circ1 = Circle(5, 2, 6)

#circ1
