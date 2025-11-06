class Shape:
    def __init__(self, x=0, y=0):
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)): # if input is not a number
            raise ValueError("x and y must be numbers")
        self.x = x
        self.y = y
        print(f"created shape on x:{self.x}y:{self.y}")
    
    def translate(self, xpath, ypath):
        if not isinstance(xpath, (float, int)) or not isinstance(ypath, (float, int)): # if input is not a number
            raise TypeError("x (x-path) and y (y-path) must be numbers")
        self.x = xpath
        self.y = ypath
    
    def __str__(self):
        return f"{self.__class__.__name__} centered at x: {self.x} and y: {self.y}  " #str repr
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})" #str repr

#def __lt__(self, other): #     < #area and we will not have area
    
def __gt__(self, other): #     >
    return self == other or self > other
def __le__(self, other): #    <=
    return not self <= other
def __ge__(self,other): #     >=
    return not self >= other 

# def __eq__(self, other): return self == other #cant have yet if we compare area(each shape different)




