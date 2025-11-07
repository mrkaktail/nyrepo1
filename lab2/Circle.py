from Shape import Shape
from math import pi

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
    
#circ1 = Circle(5, 2, 6)

#circ1
