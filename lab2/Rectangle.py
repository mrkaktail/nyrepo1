import Shape as Shape

"""
Class representing a rectangle on a 2D (x,y) plane

Attributes:
    Width (float): representing a width side of given rectangle
    Length (float): representing a length side of given rectangle
    x (float): x-cordinate of the rectangles center
    y (float): y-cordinate of the rectangles center

Properties:
    area (float): Read-only area of given rectangle
    perimeter (float): Read-only perimeter(circumference) of given rectangle

Methods:
    IsItaSquare: Returns True if the created bject is a square by comparing length and width sides
    CheckIfComparable: returns True if two object areas are from class Rectangle, raises TypeError otherwise

Overloaded comparison operators:
    Compares areas of rectangles with (==,<,>,<=,>=) operators

"""

class Rectangle(Shape):
    #Object initialization
    def __init__(self, x:float=0.0, y:float=0.0, width: float=1.0, length:float=1.0):
        super().__init__(x,y)
        if not isinstance(width,(float,int)) or not isinstance(length,(float, int)): #executes if the values are numeric at runtime
            raise TypeError("Width and height must be numbers (float or int)")
        if width <= 0 or length <= 0: 
            raise ValueError("Length & Width must be bigger than 0") #value of arg error
        self.width = width
        self.length = length

    #Checks if instance is a square
    def is_it_square(self) -> bool:
        if self.width == self.length:
            return True
        return False
    
    #Checks if two objects can be compared
    def _check_if_comparible(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Only rectangle or square areas can be compared")
    
    #Area and perimeter properties
    @property
    def area(self):
        return self.width * self.length
    
    @property
    def perimeter(self):
        return (self.width + self.length) * 2
    
    #Operator overloading
    def __eq__(self, other):
        self._check_if_comparible(other)
        return self.area == other.area
    
    def __lt__(self, other):
        self._check_if_comparible(other)
        return self.area < other.area
    
    def __gt__(self, other):
        self._check_if_comparible(other)
        return self.area > other.area
    
    def __le__(self, other):
        self._check_if_comparible(other)
        return self.area <= other.area
    
    def __ge__(self, other):
        self._check_if_comparible(other)
        return self.area >= other.area
