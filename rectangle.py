import math 
from shape import Shape 


class Rectangle(Shape): 
    def __init__(self, width, height, x = 0, y = 0):
        super().__init__(x,y)
        if width <= 0 or height <= 0: 
            raise ValueError(f"Width and height need to be positive values, not {width, height}")
        
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
    
        
