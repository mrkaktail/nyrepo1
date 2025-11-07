import Shape as Shape

class Rectangle(Shape):
    def __init__(self, x=0, y=0, width=1, length=1):
        super().__init__(x,y)
        if not isinstance(width,(float,int)) and not isinstance(length,(float, int)):
            raise TypeError("Width and height must be numbers (float or int)")
        if width <= 0 or length <= 0: 
            raise ValueError("Length & Width must be bigger than 0") #value of arg error
        self.width = width
        self.length = length

    def IsItSquare(self):
        if self.width == self.length:
            return True
        return False
    
    @property
    def area(self):
        return self.width * self.length
    
    @property
    def perimeter(self):
        return (self.width + self.length) * 2
    
    