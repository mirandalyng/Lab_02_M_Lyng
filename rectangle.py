import math 
from shape import Shape 


class Rectangle(Shape): 
    def __init__(self, width, height, x = 0, y = 0):
        super().__init__(x,y)

        if not all(isinstance(value, (int, float)) for value in (x,y,width,height)): 
            raise TypeError(f"Type must be int or float")
        
        if width <= 0 or height <= 0:  
            raise ValueError(f"Width and height need to be positive values")
        
        
        
        self.width = width 
        self.height = height

    
    @property
    def area(self): 
        return self.width * self.height
    
    @property
    def perimeter(self): 
        return 2*(self.width + self.height)

    def is_unit_square(self):
        return self.width == self.height
    
    
    def __repr__(self) -> str: 
        return f"{self.__class__.__name__}(width = {self.width}, height = {self.height}, x = {self.x}, y = {self.y})"


    def __str__(self) -> str: 
        return f"{self.__class__.__name__} with width = {self.width}, height= {self.height}= {self.x} and y = {self.y}, area = {self.area:.2f} and perimeter = {self.perimeter:.2f}"
