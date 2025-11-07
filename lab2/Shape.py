class Shape:
    """
    Superclass for 2 dimensional shapes

    Attributes:
    x: x-cordinate of shapes center
    y: y-cordinate of shapes center

    Methods: 
    translate(xstep, ystep): Moves shape from its current position by x and y steps
    """
    #Object initialization
    def __init__(self, x:float=0.0, y:float=0.0):
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)): #checks at runtime if input is not a number
            raise TypeError("x and y must be numbers")
        self.x = x
        self.y = y
        print(f"created shape on x:{self.x} y:{self.y}")
    
    #Moving the object
    def translate(self, xstep:float, ystep:float):
        if not isinstance(xstep, (float, int)) or not isinstance(ystep, (float, int)): #checks at runtime if input is not a number
            raise TypeError("x(x-path) and y(y-path) must be numbers")
        self.x += xstep
        self.y += ystep

    #representations of object
    def __repr__(self):
        return f"{self.__class__.__name__}(x:{self.x}, y:{self.y})"
    
    def __str__(self):
        return f"{self.__class__.__name__} positioned at x:{self.x}, y:{self.y}"



