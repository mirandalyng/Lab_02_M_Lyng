import math 
from shape import Shape 

class Circle(Shape): 
    
    def __init__(self, radius, x=0 , y =0 ): 
        super().__init__(x,y)
        if radius <= 0: 
            raise ValueError(f"Radius must be a positive number, not {radius}")
        
        self.radius = radius 

    
    @property
    def area(self): 
        """Calculates the area of the circle"""
        return math.pi * self.radius **2
    
    @property
    def perimeter(self): 
        """Calculates the perimeter of the circle"""
        return 2 * math.pi * self.radius
    

    def is_unit_circle(self, x, y): 

        return x**2 + y**2 <= 1
