class Shape:
    def __init__(self, x=0, y=0):
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)): # if input is not a number
            raise ValueError("x and y must be numbers")
        self.x = x
        self.y = y
        print(f"created shape on x:{self.x} y:{self.y}")
    
    def translate(self, xstep, ystep):
        if not isinstance(xstep, (float, int)) or not isinstance(ystep, (float, int)): # if input is not a number
            raise TypeError("x(x-path) and y(y-path) must be numbers")
        self.x += xstep
        self.y += ystep

    def __repr__(self):
        return f"{self.__class__.__name__}(x:{self.x}, y:{self.y})"
    
    def __str__(self):
        return f"{self.__class__.__name__} positioned at x:{self.x}, y:{self.y}"

#circle1 = Shape(3, 5)
#print(circle1)



